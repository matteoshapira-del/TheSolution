#!/usr/bin/env python3
"""Harvest the PeaceMaker (2015 Unity build) rules data into structured JSON.

Pipeline:
  1. tools/harvest/fetch.sh          -> harvest_raw/app/PeaceMaker.app/...
  2. python3 tools/harvest/extract.py --raw harvest_raw

Writes two kinds of output:

* harvest_raw/text/, harvest_raw/db/, harvest_raw/csv/  (LOCAL ONLY, git-ignored)
  Verbatim game files: rules XML, localized text in en/he/ar, the SQLite
  content DB, and CSV exports of every event/action text. ImpactGames owns
  this material; it is kept out of git and used for private reference only.

* data/harvest/*.json  (committed)
  The game's *mechanics*, restructured: variables and defaults, the action
  tree, outcome tables (conditions + numeric effects), the AI actor decision
  trees, the event index (ids/tags/locations — no prose), plot milestones and
  endings, map/interface structure, and engine constants recovered from the
  decompiled C#.

Requires: Python 3.9+, UnityPy (pip install UnityPy).
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import os
import sqlite3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

APP_DATA = Path("app/PeaceMaker.app/Contents/Resources/Data")
ROLE_BY_ID = {1: "israeli", 2: "palestinian"}

# Text assets inside the Unity bundles that carry game rules or text.
RULE_ASSETS = {
    "init": "Starting value and flags of every simulation variable, per role.",
    "outcomes": "Outcome tables: for each action id, ordered result branches with conditions and effects.",
    "actions-to-outcomes": "Maps player action ids to outcome table ids.",
    "ai2": "Decision trees for the non-player actors that act every turn.",
    "data.en-us": "Player action menus (headers, advisor lines) in English.",
    "events.en-us": "All news/feedback events in English (source of the events DB).",
    "interface.en-us": "UI strings, stakeholders, polls, cities, timeline, tutorial (English).",
    "interface.he": "UI strings (Hebrew).",
    "interface.ar": "UI strings (Arabic).",
    "Localization": "I2 Localization term table (CSV).",
}


# --------------------------------------------------------------------------- utils
def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def num(s):
    """Parse a numeric XML value; keep non-numeric strings (variable names, true/false)."""
    if s is None:
        return None
    s = s.strip()
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


# ----------------------------------------------------------------- 1. raw dumping
def dump_text_assets(data_dir: Path, out_dir: Path) -> dict:
    import UnityPy  # imported lazily so --help works without it

    out_dir.mkdir(parents=True, exist_ok=True)
    found = {}
    for bundle in ["resources.assets", "sharedassets2.assets"]:
        env = UnityPy.load(str(data_dir / bundle))
        for obj in env.objects:
            if obj.type.name != "TextAsset":
                continue
            ta = obj.read()
            name = getattr(ta, "m_Name", None) or ta.name
            raw = getattr(ta, "m_Script", None)
            if raw is None:
                raw = ta.script
            if isinstance(raw, str):
                raw = raw.encode("utf-8", "surrogateescape")
            ext = ".csv" if name == "Localization" else ".xml"
            (out_dir / f"{name}{ext}").write_bytes(raw)
            found[name] = {"bundle": bundle, "bytes": len(raw), "file": f"{name}{ext}"}
    return found


def export_db_csv(db: sqlite3.Connection, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    tables = [r[0] for r in db.execute("select name from sqlite_master where type='table'")]
    for t in tables:
        cur = db.execute(f'select * from "{t}"')
        cols = [d[0] for d in cur.description]
        with open(out_dir / f"{t}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(cols)
            w.writerows(cur)


# --------------------------------------------------------------- 2. mechanics data
def parse_variables(init_root: ET.Element) -> dict:
    out = {}
    for game in init_root.findall("Game"):
        rows = []
        for v in game.iter("Variable"):
            attrs = dict(v.attrib)
            attrs.update(v.find("ID").attrib)  # one entry puts its flag on <ID>
            rows.append({
                "id": v.findtext("ID").strip(),
                "default": num(v.findtext("Value")),
                "auto_decrement": attrs.get("auto-decrement") == "true",
                "can_be_negative": attrs.get("can-be-negative") == "true",
                "can_be_over_100": attrs.get("can-be-over-100") == "true",
                "debug_modify_ignored": attrs.get("ignoreDebugModify") == "true",
            })
        out[game.get("role")] = rows
    return out


def parse_condition(c: ET.Element) -> dict:
    d = {"op": (c.findtext("Name") or "").strip()}
    for i in (1, 2, 3):
        v = c.findtext(f"Argument{i}")
        if v is not None:
            d[f"arg{i}"] = num(v)
    if c.get("always") == "true":
        d["always"] = True
    return d


def parse_method(m: ET.Element) -> dict:
    d = {"op": (m.findtext("Name") or "").strip()}
    for i in (1, 2, 3):
        v = m.findtext(f"Argument{i}")
        if v is not None and v.strip() != "":
            d[f"arg{i}"] = num(v)
    return d


def parse_outcomes(root: ET.Element) -> tuple[dict, list]:
    # The engine looks tables up with SelectSingleNode, so the FIRST table with a
    # given actionID wins; later duplicates are dead data. Keep the first, list the rest.
    out, duplicates = {}, []
    for oc in root.findall("Outcomes"):
        if oc.get("actionID") in out:
            duplicates.append(oc.get("actionID"))
            continue
        branches = []
        for o in oc.findall("Outcome"):
            conds = o.find("Conditions")
            effects = []
            for ae in o.find("ActionEffects").findall("ActionEffect"):
                changes = {}
                for e in ae.findall("Effect"):
                    ch = (e.findtext("Change") or "").strip()
                    val = 1 if ch == "true" else -1 if ch == "false" else num(ch)
                    if val != 0:
                        changes[e.findtext("VariableID").strip()] = val
                effects.append({
                    "timing": num(ae.findtext("Timing")),
                    "type": (ae.findtext("Type") or None),
                    "event_tag": (ae.findtext("Tags") or "").strip() or None,
                    "changes": changes,
                    "methods": [parse_method(m) for m in ae.findall("Method")],
                })
            branches.append({
                "order": num(o.findtext("Order")),
                "result": (o.findtext("Result") or "").strip(),
                "conditions": [parse_condition(c) for c in conds.findall("Condition")] if conds is not None else [],
                "effects": effects,
            })
        out[oc.get("actionID")] = branches
    return out, duplicates


def parse_actions_to_outcomes(root: ET.Element) -> dict:
    m = {}
    for role in root.findall("Role"):
        for a in role.findall("ActionToOutcome"):
            m[a.get("actionId")] = a.text.strip()
    return m


def parse_ai_branch(b: ET.Element) -> dict:
    node = {"description": b.get("description")}
    if b.get("else") is not None:
        node["else"] = True
    if b.get("pollid"):
        node["poll_id"] = b.get("pollid")
    conds = b.find("Conditions")
    if conds is not None:
        node["conditions"] = [parse_condition(c) for c in conds.findall("Condition")]
    for key in ("Pass", "Fail"):
        el = b.find(key)
        if el is None:
            continue
        sub = {}
        if el.get("pollid"):
            # Player "Listen to Concerns" actions evaluate only this sub-tree.
            sub["poll_id"] = el.get("pollid")
        if el.find("Branch") is not None:
            sub["branches"] = [parse_ai_branch(x) for x in el.findall("Branch")]
        if el.find("Action") is not None:
            sub["action"] = el.find("Action").get("id")
        if el.find("PlayTrack") is not None:
            sub["music"] = el.find("PlayTrack").get("id")
        node[key.lower()] = sub
    return node


def parse_ai(root: ET.Element) -> dict:
    out = {}
    for game in root.findall("Game"):
        actors = []
        for a in game.find("AI_Actors").findall("AI_Actor"):
            tree = [parse_ai_branch(b) for b in a.findall("Branch")]
            reachable = sorted({x.get("id") for x in a.iter("Action")} - {"NoAction"})
            polls = []
            for el in a.iter():
                if el.get("pollid"):
                    polls.append(el.get("pollid"))
            actors.append({
                "id": a.get("id"),
                "call_frequency": int(a.get("callFrequency")),
                "bundled_with_player_feedback": a.get("bundleWithUserFeedback") is not None,
                "affected_by_difficulty": a.get("affectedByDifficulty") is not None,
                "poll_branches": polls,
                "reachable_outcomes": reachable,
                "tree": tree,
            })
        out[game.get("role")] = actors
    return out


def resolve_outcome_id(action_string_id: str, a2o: dict) -> str:
    # Mirrors Engine.doAction(): last ':' segment, looked up in actions-to-outcomes.
    last = action_string_id.split(":")[-1].strip()
    return a2o.get(last, action_string_id)


def build_actions(db: sqlite3.Connection, a2o: dict, outcomes: dict) -> dict:
    db.row_factory = sqlite3.Row
    var_name = {r["variable_id"]: r["name"] for r in db.execute("select * from variables")}
    cats = {r["action_category_id"]: r["name"] for r in db.execute("select * from action_categories")}
    prereqs = collections.defaultdict(list)
    for r in db.execute("select * from action_variable_prereqs"):
        prereqs[r["action_id"]].append({
            "variable": var_name.get(r["variable_id"]),
            "value": num(r["variable_value"]),
            "compare": r["compare"] or "#Equals",
        })
    rows = db.execute(
        "select a.*, t.menu_text, t.header from actions a "
        "left join action_text_enus t using(action_id) order by a.action_id"
    ).fetchall()
    by_id = {r["action_id"]: r for r in rows}
    children = collections.defaultdict(list)
    for r in rows:
        if r["parent_action_id"]:
            children[r["parent_action_id"]].append(r["action_id"])

    out = {"israeli": [], "palestinian": []}
    for r in rows:
        aid = r["action_id"]
        kids = children.get(aid, [])
        node = {
            "id": aid,
            "string_id": r["action_string_id"],
            "category": cats.get(r["action_category_id"]),
            "parent": r["parent_action_id"] or None,
            "is_root": bool(r["is_root"]),
            "label": r["menu_text"] or None,
            "header": r["header"] or None,
            "children": kids,
        }
        if r["require_action_id"]:
            node["then_requires"] = by_id[r["require_action_id"]]["action_string_id"]
        if r["variable_set_id"]:
            node["sets_variable"] = {"variable": var_name.get(r["variable_set_id"]),
                                     "from": r["variable_set_value"]}
        if r["variable_show_id"]:
            node["shown_if"] = {"variable": var_name.get(r["variable_show_id"]),
                                "value": num(r["variable_show_value"])}
        if prereqs.get(aid):
            node["enabled_if_any"] = prereqs[aid]
        if r["poll_actor"]:
            node["poll"] = {"actor": r["poll_actor"], "branch": r["poll_branch"]}
        if not kids:
            oid = resolve_outcome_id(r["action_string_id"], a2o)
            node["outcome_id"] = oid
            node["outcome_found"] = oid in outcomes or bool(r["poll_actor"])
        out[ROLE_BY_ID[r["role_id"]]].append(node)
    return out


def build_events(db: sqlite3.Connection) -> tuple[list, dict, list]:
    db.row_factory = sqlite3.Row
    scores = collections.defaultdict(dict)
    for r in db.execute("select * from event_scores"):
        scores[r["event_id"]][r["variable_name"]] = r["score"]
    headers = {r["event_id"]: r["header"] for r in db.execute("select event_id, header from event_text_enus")}
    events, plot = [], []
    by_tag = collections.defaultdict(lambda: {"variants": 0, "box_types": collections.Counter(),
                                              "locations": collections.Counter(), "sounds": collections.Counter()})
    for r in db.execute("select * from events order by event_id"):
        e = {
            "id": r["event_id"],
            "string_id": r["event_string_id"],
            "tag": r["tags"],
            "box_type": r["box_type"] or None,
            "location": r["location"] or None,
            "sound": r["sound"] or None,
            "image": r["image"] or None,
        }
        if r["event_type"]:
            e["event_type"] = r["event_type"]
            e["role"] = r["role"]
            e["video"] = r["video"]
            e["hold_for"] = r["score_hold_for"]
            e["compare"] = r["score_type"]          # 'more' => >=, 'less' => <=
            e["mode"] = r["score_mode"] or "milestone"
            e["thresholds"] = scores.get(r["event_id"], {})
            # Milestone/ending titles are short headlines and essential for design work.
            e["title"] = headers.get(r["event_id"])
            plot.append(e)
        events.append(e)
        t = by_tag[r["tags"]]
        t["variants"] += 1
        t["box_types"][r["box_type"] or ""] += 1
        t["locations"][r["location"] or ""] += 1
        t["sounds"][r["sound"] or ""] += 1
    tags = {k: {"variants": v["variants"], "box_types": dict(v["box_types"]),
                "locations": dict(v["locations"]), "sounds": dict(v["sounds"])}
            for k, v in sorted(by_tag.items())}
    return events, tags, plot


def build_interface(root: ET.Element) -> dict:
    rs = root.find("RoleSpecific")
    out = {"groups_and_leaders": {}, "polls": {}, "cities": [], "timeline_labels": [],
           "difficulties": [], "tutorial_steps": [], "advisors": {}}
    for el in rs:
        role = el.get("role")
        if el.tag == "Actors":
            out["groups_and_leaders"][role] = [
                {"variable": a.findtext("variable").strip(), "title": a.findtext("DialogTitle").strip()}
                for a in el.findall("Actor")]
        elif el.tag == "Books":
            out["polls"][role] = [
                {"variable": b.findtext("variable").strip(), "title": b.findtext("DialogTitle").strip()}
                for b in el.findall("Book")]
        elif el.tag in ("DoveHeader", "HawkHeader"):
            import re
            txt = re.sub(r"<[^>]+>", "", el.findtext("Text") or "").strip()
            out["advisors"].setdefault(role, {})[el.tag.replace("Header", "").lower()] = txt
    for c in root.find("Cities").findall("City"):
        out["cities"].append({"name": c.findtext("Name").strip(), "map_mask_color": c.findtext("Color")})
    out["timeline_labels"] = [e.findtext("Label") for e in root.find("Timeline").findall("Entry")]
    out["difficulties"] = [x.tag.lower() for x in root.find("DifficultyScreen")]
    out["tutorial_steps"] = [{"order": int(t.findtext("Order")), "header": t.findtext("Header")}
                             for t in root.find("Tutorial").findall("TutorialItem")]
    return out


# Constants recovered by reading the decompiled Assembly-CSharp.dll (Engine.cs,
# AIHelper.cs, EventsHelper.cs, EndReportWindow.cs). See docs/harvest/04-scoring-and-endings.md.
ENGINE = {
    "source": "Decompiled Assembly-CSharp.dll from the 2015 Unity build (ilspycmd).",
    "variable_clamp": "0..100 unless flagged can_be_negative / can_be_over_100",
    "score_formulas": {
        "israeli": {
            "internal_raw": "israel people + security + sympathy",
            "internal_map": {"zero_at": 95, "full_at": 280},
            "external_raw": "palestinian president + palestinian people + 0.33*(usa + un + arab world)",
            "external_map": {"zero_at": 70, "full_at": 270},
            "leadership": "0.33*(usa + un + arab world)",
        },
        "palestinian": {
            "internal_raw": "1.25*tolerance + palestinian public approval + fatah approval + economy + government authority + 0.75*hamas approval",
            "internal_map": {"zero_at": 136.25, "full_at": 500},
            "external_raw": "1.5*leadership + 1.25*israeli prime minister approval + usa approval + 0.75*(israeli public approval + un approval + arab world approval)",
            "external_map": {"zero_at": 155, "full_at": 500},
        },
        "map_rule": "raw<zero_at: (raw-zero_at)/zero_at*100 ; zero_at<=raw<=full_at: (raw-zero_at)/(full_at-zero_at)*100 ; raw>full_at: 100 ; truncated to int",
    },
    "budget_modifier_table": [[15, 0.0], [20, 0.25], [25, 0.5], [30, 0.75], [35, 1.0], [45, 1.25],
                              [55, 1.5], [65, 1.75], [75, 2.0], [None, 2.5]],
    "budget_modifier_rule": "first row whose bound > value; e.g. value 40 -> 1.25",
    "threshold_condition": "#Threshold(x, t, v) passes when x >= Uniform(t-v, t+v)",
    "roll_condition": "#Roll(name, n) stores UniformInt[0, n-1] in a temp variable",
    "ai": {
        "max_tagged_ai_actions_per_turn": 3,
        "initial_sleep_if_affected_by_difficulty": "call_frequency + 3 + 3 + UniformInt[0, N]; N = violent 3, tense 4, calm 8",
        "sleep_difficulty_adjust": {"violent": -1, "tense": 1, "calm": 3},
    },
    "plot_points": "checked once per turn after AI; condition must hold on hold_for+1 consecutive checks; at most one fires per turn; win/lose ends the game",
    "end_report_violence_tiers": [[0, "NONE"], [50, "LOW"], [100, "MODERATE"], [150, "HIGH"], [None, "EXTREME"]],
    "end_report_rule": "tier by final 'endreport' variable: >150 EXTREME, >100 HIGH, >50 MODERATE, >0 LOW, else NONE",
    "difficulty_default": "violent",
}


# ------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", default="harvest_raw", help="folder produced by fetch.sh")
    ap.add_argument("--out", default="data/harvest", help="where to write committed JSON")
    args = ap.parse_args()

    raw = Path(args.raw)
    data_dir = raw / APP_DATA
    if not data_dir.is_dir():
        print(f"Unity data folder not found: {data_dir}. Run tools/harvest/fetch.sh first.", file=sys.stderr)
        return 1
    out = Path(args.out)

    print("Dumping text assets…")
    text_dir = raw / "text"
    assets = dump_text_assets(data_dir, text_dir)

    db_src = data_dir / "StreamingAssets" / "peacemaker.db"
    (raw / "db").mkdir(parents=True, exist_ok=True)
    db_copy = raw / "db" / "peacemaker.db"
    db_copy.write_bytes(db_src.read_bytes())
    db = sqlite3.connect(f"file:{db_copy}?mode=ro", uri=True)
    print("Exporting DB tables to CSV…")
    export_db_csv(db, raw / "csv")

    def xml(name):
        return ET.parse(text_dir / f"{name}.xml").getroot()

    variables = parse_variables(xml("init"))
    outcomes, duplicate_outcomes = parse_outcomes(xml("outcomes"))
    a2o = parse_actions_to_outcomes(xml("actions-to-outcomes"))
    ai = parse_ai(xml("ai2"))
    actions = build_actions(db, a2o, outcomes)
    events, tags, plot = build_events(db)
    interface = build_interface(xml("interface.en-us"))

    sa = data_dir / "StreamingAssets"
    media = {d.name: sum(1 for f in d.rglob("*") if f.is_file()) for d in sa.iterdir() if d.is_dir()}
    build_info = (sa / "build_info.txt").read_text(encoding="utf-8", errors="replace").strip()

    manifest = {
        "game": "PeaceMaker (ImpactGames)",
        "build": build_info,
        "installer_sha256": sha256(raw / "installer" / "peacemaker.pkg") if (raw / "installer" / "peacemaker.pkg").exists() else None,
        "engine": "Unity (Mono), NGUI, I2 Localization, SQLite content DB",
        "text_assets": {k: {**v, "purpose": RULE_ASSETS.get(k)} for k, v in assets.items()},
        "streaming_asset_file_counts": media,
        "counts": {
            "variables": {r: len(v) for r, v in variables.items()},
            "action_nodes": {r: len(v) for r, v in actions.items()},
            "leaf_actions": {r: sum(1 for n in v if not n["children"]) for r, v in actions.items()},
            "outcome_tables": len(outcomes),
            "outcome_branches": sum(len(v) for v in outcomes.values()),
            "duplicate_outcome_tables_ignored_by_engine": len(duplicate_outcomes),
            "ai_actors": {r: len(v) for r, v in ai.items()},
            "events": len(events),
            "event_tags": len(tags),
            "plot_events": len(plot),
            "cities": len(interface["cities"]),
        },
    }

    manifest["duplicate_outcome_tables"] = sorted(set(duplicate_outcomes))
    manifest["leaf_actions_without_outcome"] = sorted(
        n["string_id"] for v in actions.values() for n in v if not n["children"] and not n["outcome_found"])
    write_json(out / "manifest.json", manifest)
    write_json(out / "engine.json", ENGINE)
    write_json(out / "variables.json", variables)
    write_json(out / "actions.json", actions)
    write_json(out / "actions_to_outcomes.json", a2o)
    write_json(out / "outcomes.json", outcomes)
    write_json(out / "ai_actors.json", ai)
    write_json(out / "events_index.json", events)
    write_json(out / "event_tags.json", tags)
    write_json(out / "milestones_and_endings.json", plot)
    write_json(out / "interface.json", interface)
    print(json.dumps(manifest["counts"], indent=1))
    print(f"Wrote mechanics JSON to {out}/ and verbatim text to {raw}/text, {raw}/csv (git-ignored).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build docs/guide/peacemaker-decoded.html from data/harvest/*.json and tools/harvest/guide_template.html.

    python3 tools/harvest/build_guide.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_docs import cond_text, method_text, split_changes  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "harvest"
TEMPLATE = Path(__file__).resolve().parent / "guide_template.html"
OUT = ROOT / "docs" / "guide" / "peacemaker-decoded.html"


def load(n):
    return json.loads((DATA / f"{n}.json").read_text(encoding="utf-8"))


def branches(table):
    out = []
    for b in table:
        when = " and ".join(cond_text(c) for c in b["conditions"] if c.get("op") != "#And") or "otherwise"
        eff, side, meth = [], [], []
        for e in b["effects"]:
            m, c, v = split_changes(e["changes"])
            eff += m
            side += c + v
            meth += [method_text(x) for x in e["methods"]]
        out.append({"r": b["result"], "w": when.replace("`", ""), "e": ", ".join(eff + meth).replace("`", ""),
                    "s": ", ".join(side), "imm": any(e.get("type") == "Immediate" for e in b["effects"])})
    return out


def action_tree(role, actions, outcomes):
    nodes = {n["id"]: n for n in actions[role]}
    cats = {}

    def leaves(n, path):
        if n["children"]:
            res = []
            for c in n["children"]:
                res += leaves(nodes[c], path + [nodes[c]["label"] or nodes[c]["header"] or ""])
            return res
        leaf = {"p": [p for p in path if p], "l": n["label"] or n["header"]}
        if n.get("poll"):
            leaf["poll"] = n["poll"]["actor"]
        else:
            leaf["b"] = branches(outcomes.get(n.get("outcome_id"), []))
        if n.get("then_requires"):
            leaf["fin"] = True
        if n.get("enabled_if_any"):
            leaf["gate"] = " or ".join(f"{p['variable']} = {p['value']}" if p["compare"] == "#Equals"
                                       else f"{p['variable']} ≥ {p['value']}" for p in n["enabled_if_any"])
        return [leaf]

    for n in actions[role]:
        if n["parent"]:
            continue
        top = {"t": n["header"] or n["string_id"].title(), "leaves": leaves(n, [])}
        cats.setdefault(n["category"], []).append(top)
    return cats


METERS = {
    "israeli": [
        ("israel people", "Israeli Public", "group", 1, 0), ("yesha", "Yesha (settlers' council)", "group", 0, 0),
        ("palestinian president", "PA President", "group", 0, 1), ("palestinian people", "Palestinian Public", "group", 0, 1),
        ("hamas", "Militant Groups", "group", 0, 0), ("un", "United Nations", "group", 0, 0.33),
        ("usa", "USA", "group", 0, 0.33), ("arab world", "Arab World", "group", 0, 0.33),
        ("security", "Israeli Security", "poll", 1, 0), ("sympathy", "Israeli Sympathy", "poll", 1, 0),
        ("suppression", "Militant Suppression", "poll", 0, 0), ("palestinian cooperation", "Palestinian Cooperation", "poll", 0, 0),
    ],
    "palestinian": [
        ("palestinian public approval", "Palestinian Public", "group", 1, 0), ("fatah approval", "Fatah", "group", 1, 0),
        ("hamas approval", "Hamas", "group", 0.75, 0), ("israeli prime minister approval", "Israeli PM", "group", 0, 1.25),
        ("israeli public approval", "Israeli Public", "group", 0, 0.75), ("usa approval", "United States", "group", 0, 1),
        ("un approval", "United Nations", "group", 0, 0.75), ("arab world approval", "Arab World", "group", 0, 0.75),
        ("economy", "Economy", "poll", 1, 0), ("government authority", "Government Authority", "poll", 1, 0),
        ("independence", "Independence", "poll", 0, 0), ("leadership", "Leadership", "poll", 0, 1.5),
        ("tolerance", "View of Israel", "poll", 1.25, 0), ("israeli cooperation", "Israeli Cooperation", "poll", 0, 0),
    ],
}

AI_NOTES = {
    "IsrClock": "Hidden upkeep every turn: suppression −2; PA trust grows cooperation, which grows security, which grows public approval.",
    "IsrMusicDJ": "Chooses the music loop from the score mood.",
    "PalMusicDJ": "Chooses the music loop from the score mood.",
    "Clock": "Hidden upkeep every turn: refills the eight funding pools in proportion to each patron's approval.",
    "IPMPalestinianPublic": "Rallies, protests, aggressive protests, quality-of-life reactions; keyed to Palestinian public mood and suppression.",
    "International Press": "Writes about your weakest meter (or praises your strongest).",
    "Israeli People": "Concern, praise, petitions, protests and rallies on your lowest domestic meter. Also answers 'Listen to Concerns'.",
    "Israeli Government": "Coalition concern or praise; statements for or against you. Also answers 'Listen to Concerns'.",
    "Palestinian President": "Concerns about violence, trust and quality of life; anti-militant moves; offers to meet. Also answers 'Listen to Concerns'.",
    "Yesha": "Settler protests and petitions; outposts, harassment and assaults on Palestinians.",
    "Israeli Prime Minister": "Offers construction aid, removes a security measure or apologises when approval is high; security crackdowns and blame when low.",
    "Palestinian Public": "Enthusiastic, angry, or wants reconstruction, material needs or rights; shifts support between Fatah, Hamas and you.",
}
AI_NOTES_ROLE = {
    ("israeli", "Hamas"): "Stands down with probability suppression/300; otherwise a d100 roll picks words, fundraising, an attack, an extreme attack or international terror, gated by low approval and low suppression.",
    ("palestinian", "Hamas"): "Very high approval: partial disarmament, reconstruction, joins politics. Very low: attacks you. Otherwise, if the view of Israel is low: attacks on Israel, funds, words.",
    ("palestinian", "Fatah"): "Same shape as Hamas: disarmament, anti-corruption and support when approval is high; attacks on you or on Israel when low.",
}


def main():
    actions, outcomes, ai = load("actions"), load("outcomes"), load("ai_actors")
    variables, plot, sim = load("variables"), load("milestones_and_endings"), load("simulation_results")
    defaults = {r: {v["id"]: v["default"] for v in variables[r]} for r in variables}
    data = {"roles": {}, "sim": {}}
    for role in ("israeli", "palestinian"):
        data["roles"][role] = {
            "meters": [{"id": i, "label": l, "kind": k, "wi": wi, "we": we, "def": defaults[role][i]}
                       for i, l, k, wi, we in METERS[role]],
            "endings": [{"id": p["string_id"], "mode": p["mode"], "title": p["title"], "cmp": p["compare"],
                         "th": p["thresholds"], "hold": p["hold_for"] + 1} for p in plot if p["role"] == role],
            "actions": action_tree(role, actions, outcomes),
            "ai": [{"id": a["id"], "freq": a["call_frequency"], "diff": a["affected_by_difficulty"],
                    "n": len(a["reachable_outcomes"]),
                    "note": AI_NOTES_ROLE.get((role, a["id"])) or AI_NOTES.get(a["id"], "")} for a in ai[role]],
        }
    for k, v in sim["runs"].items():
        data["sim"][k] = {"results": v["results"], "games": v["games"], "ttw": v["turns_to_win"],
                          "viol": v["end_report_violence_median"]}
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()

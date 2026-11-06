#!/usr/bin/env python3
"""Headless re-implementation of the PeaceMaker turn engine, driven only by data/harvest/*.json.

Purpose: prove the harvest is complete enough to *run* the game, and measure its balance
(game length, win/lose rates, which actions matter) before designing "The Solution".

    python3 tools/harvest/simulate.py --role israeli --difficulty tense --policy greedy --games 200

The control flow mirrors the decompiled Unity code (Engine.cs, AIHelper.cs, EventsHelper.cs,
ActionProgress.cs). Known simplifications are listed in docs/harvest/09-difficulty-and-balance.md:
UI-only behaviour (animations, music, tutorials) is skipped, and when a player outcome queues more
than one news event all of them are applied.
"""
from __future__ import annotations

import argparse
import collections
import copy
import json
import random
import statistics
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "harvest"


def load(name):
    with open(DATA / f"{name}.json", encoding="utf-8") as f:
        return json.load(f)


ACTIONS, OUTCOMES, AI, VARS, PLOT, ENGINE = (load(n) for n in (
    "actions", "outcomes", "ai_actors", "variables", "milestones_and_endings", "engine"))

BUDGET_TABLE = [(15, 0.0), (20, 0.25), (25, 0.5), (30, 0.75), (35, 1.0), (45, 1.25),
                (55, 1.5), (65, 1.75), (75, 2.0)]


def budget_mod(v: float) -> float:
    for bound, m in BUDGET_TABLE:
        if v < bound:
            return m
    return 2.5


def score_map(raw: float, zero: float, full: float) -> int:
    if raw < zero:
        s = (raw - zero) / zero * 100
    elif raw > full:
        s = 100
    else:
        s = (raw - zero) / (full - zero) * 100
    return int(s)  # C# (int) truncates toward zero


class Game:
    def __init__(self, role: str, difficulty: str, rng: random.Random):
        self.role, self.difficulty, self.rng = role, difficulty, rng
        self.v: dict[str, float] = {}
        self.flags = {}
        for r in VARS[role]:
            self.v[r["id"]] = float(r["default"])
            self.flags[r["id"]] = r
        self.pending: list[dict] = []          # Engine.actionEffectsMap
        self.pins: list[dict] = []             # AI news pins waiting on the map
        self.turn = 0
        self.over = None                       # None | 'win' | 'lose:<id>'
        self.milestones: list[tuple[int, str]] = []
        self.actors = []
        for a in AI[role]:
            st = {"def": a, "sleep": a["call_frequency"]}
            if a["affected_by_difficulty"]:
                n = {"violent": 3, "calm": 8}.get(difficulty, 4)
                st["sleep"] += rng.randint(0, n) + 3 + 3
            self.actors.append(st)
        self.plot = [dict(p, hold=0, fired=False) for p in PLOT if p["role"] == role]
        self.leaves = [n for n in ACTIONS[role] if not n["children"]]
        self.by_string = {n["string_id"]: n for n in ACTIONS[role]}
        self.log = collections.Counter()
        self.recalc()

    def clone(self, rng: random.Random) -> "Game":
        """Cheap copy of the mutable state (static data is shared)."""
        g = copy.copy(self)
        g.rng = rng
        g.v = dict(self.v)
        g.pending = [dict(p) for p in self.pending]
        g.pins = [dict(p) for p in self.pins]
        g.milestones = list(self.milestones)
        g.actors = [dict(st) for st in self.actors]
        g.plot = [dict(p) for p in self.plot]
        g.log = collections.Counter()
        return g

    # ------------------------------------------------------------------ variables
    def get(self, name):
        if isinstance(name, (int, float)):
            return float(name)
        return self.v.get(name, 0.0)

    def set(self, name, val):
        f = self.flags.get(name)
        if not (f and f["can_be_negative"]) and val < 0:
            val = 0.0
        if not (f and f["can_be_over_100"]) and val > 100:
            val = 100.0
        self.v[name] = float(val)

    def recalc(self):
        g = self.get
        if self.role == "israeli":
            raw = g("israel people") + g("security") + g("sympathy")
            self.set("internal authority score", score_map(raw, 95, 280))
            raw = g("palestinian president") + g("palestinian people") + 0.33 * (g("usa") + g("un") + g("arab world"))
            self.set("external authority score", score_map(raw, 70, 270))
            self.set("leadership", int(0.33 * (g("usa") + g("un") + g("arab world"))))
        else:
            raw = (1.25 * g("tolerance") + g("palestinian public approval") + g("fatah approval") + g("economy")
                   + g("government authority") + 0.75 * g("hamas approval"))
            self.set("internal authority score", score_map(raw, 136.25, 500))
            raw = (1.5 * g("leadership") + 1.25 * g("israeli prime minister approval") + g("usa approval")
                   + 0.75 * (g("israeli public approval") + g("un approval") + g("arab world approval")))
            self.set("external authority score", score_map(raw, 155, 500))

    @property
    def scores(self):
        return int(self.get("internal authority score")), int(self.get("external authority score"))

    # ----------------------------------------------------------------- conditions
    def test(self, conds: list[dict]) -> bool:
        ok = False
        for c in conds:
            op = c["op"]
            a1 = self.get(c.get("arg1"))
            if op == "#Equals":
                ok = a1 == self.get(c.get("arg2"))
            elif op in ("#NotEquals", "#NotEqual"):
                ok = a1 != self.get(c.get("arg2"))
            elif op == "#Greater":
                ok = a1 > self.get(c.get("arg2"))
            elif op == "#GreaterEquals":
                ok = a1 >= self.get(c.get("arg2"))
            elif op == "#Less":
                ok = a1 < self.get(c.get("arg2"))
            elif op == "#Threshold":
                t, w = self.get(c.get("arg2")), self.get(c.get("arg3"))
                ok = a1 >= self.rng.uniform(t - w, t + w)
            elif op in ("#NotThreshold", "#ThresholdNot"):
                t, w = self.get(c.get("arg2")), self.get(c.get("arg3"))
                ok = not (a1 >= self.rng.uniform(t - w, t + w))
            elif op == "#LowestTopic":
                topics = [t.strip() for t in str(conds[0].get("arg2", "")).split(",") if t.strip()]
                low, best = 100.0, topics[0] if topics else None
                for t in topics:
                    if self.get(t) < low:
                        low, best = self.get(t), t
                ok = c.get("arg1") == best
            elif op == "#HighestTopic":
                # The shipped code compares with '<' starting from 0, so it only ever returns the first topic.
                topics = [t.strip() for t in str(conds[0].get("arg2", "")).split(",") if t.strip()]
                ok = bool(topics) and c.get("arg1") == topics[0]
            elif op == "#Roll":
                self.v[c["arg1"]] = float(self.rng.randrange(int(c["arg2"])))
                ok = True
            elif op == "#Add":
                self.set(c["arg1"], self.get(c["arg1"]) + self.get(c.get("arg2")))
                ok = True
            elif op == "#Assign":
                self.set(c["arg1"], self.get(c.get("arg2")))
                ok = True
            else:  # '#And' and anything unknown count as success in the shipped engine
                ok = True
            if not ok:
                return False
        return ok

    # -------------------------------------------------------------------- effects
    def run_methods(self, methods, value_changes_allowed=True):
        for m in methods:
            op, a1, a2, a3 = m["op"], m.get("arg1"), m.get("arg2"), m.get("arg3")
            if op in ("#Sleep", "#SleepDifficulty"):
                n = int(a2)
                if op == "#SleepDifficulty":
                    n = max(0, n + {"violent": -1, "calm": 3}.get(self.difficulty, 1))
                for st in self.actors:
                    if st["def"]["id"].upper() == str(a1).upper():
                        st["sleep"] += n
                continue
            if not value_changes_allowed:
                continue  # AI-typed setScore() only records unchanged values (see docs 11)
            if op == "#Subtract":
                self.set(a1, self.get(a1) - self.get(a2))
            elif op == "#Addition":
                self.set(a1, self.get(a1) + float(a2))
            elif op == "#Divide":
                self.set(a1, self.get(a1) / float(a2))
            elif op in ("#AdditionBudgetMult", "#AddBudget"):
                self.set(a1, int(self.get(a1) + budget_mod(self.get(a2)) * float(a3)))

    def process_effects(self, effects, source: str):
        """source: 'player' | 'ai' | 'bundled'. Returns True if a news event was produced."""
        tagged = False
        for e in effects:
            self.run_methods(e["methods"], value_changes_allowed=(source != "ai"))
            self.pending.append({"timing": e["timing"], "changes": e["changes"], "tag": e["event_tag"],
                                 "immediate": e["type"] == "Immediate", "ai": source != "player"})
            tagged = tagged or bool(e["event_tag"])
        return tagged

    def apply_changes(self, changes):
        for k, val in changes.items():
            extra = 1 if (val > 0 and self.flags.get(k, {}).get("auto_decrement")) else 0
            self.set(k, self.get(k) + val + extra)

    def advance(self, is_ai: bool) -> list[dict]:
        """Engine.enqueueEventResults(immediate=False, ...)."""
        queued, keep = [], []
        for p in self.pending:
            if p["timing"] == 0:
                if p["tag"]:
                    if p["ai"] and is_ai:
                        self.pins.append(p)
                    elif not is_ai:
                        queued.append(p)
                    else:
                        keep.append(p)
                # untagged effects: the shipped engine never runs them (IEnumerator never iterated)
            else:
                p["timing"] -= 1
                keep.append(p)
        self.pending = keep
        for k, f in self.flags.items():
            if f["auto_decrement"] and self.get(k) > 0:
                self.set(k, self.get(k) - 1)
        if not is_ai:
            self.turn += 1
        return queued

    # ------------------------------------------------------------------------- AI
    def walk(self, branches):
        prev = True
        for b in branches:
            if b.get("else") and prev:
                continue
            ok = self.test(b["conditions"]) if b.get("conditions") else True
            prev = ok
            sub = b.get("pass") if ok else b.get("fail")
            if not sub:
                continue
            if "branches" in sub:
                r = self.walk(sub["branches"])
                if r:
                    return r
                if ok:
                    continue
            if "music" in sub and ok:
                return "NoAction"
            if "action" in sub:
                return sub["action"]
            if "music" in sub:
                return "NoAction"
        return None

    def find_poll(self, branches, poll_id):
        for b in branches:
            for key in ("pass", "fail"):
                sub = b.get(key) or {}
                if sub.get("poll_id") == poll_id:
                    return sub.get("branches", [])
                found = self.find_poll(sub.get("branches", []), poll_id)
                if found is not None:
                    return found
        return None

    def run_ai(self):
        self.recalc()
        acted = 0
        for st in self.actors:
            a = st["def"]
            if acted >= 3:
                break
            if st["sleep"] > 0:
                st["sleep"] -= 1
                continue
            st["sleep"] = a["call_frequency"]
            out = self.walk(a["tree"])
            if out and out != "NoAction":
                table = OUTCOMES.get(out)
                if not table:
                    continue
                src = "bundled" if a["bundled_with_player_feedback"] else "ai"
                if self.process_effects(table[0]["effects"], src):
                    acted += 1
                    self.log[f"ai:{a['id']}:{out}"] += 1
        self.advance(is_ai=True)

    # ------------------------------------------------------------------ plot points
    def check_plot(self):
        chosen = None
        for p in self.plot:
            if p["fired"]:
                continue
            ok = all((self.get(k) >= v) if p["compare"] == "more" else (self.get(k) <= v)
                     for k, v in p["thresholds"].items())
            if ok:
                if p["hold"] < p["hold_for"]:
                    if chosen is None:
                        p["hold"] += 1
                elif chosen is None:
                    p["fired"] = True
                    chosen = p
            else:
                p["hold"] = 0
        if chosen:
            self.milestones.append((self.turn, chosen["string_id"]))
            if chosen["mode"] == "win":
                self.over = "win"
            elif chosen["mode"] == "lose":
                self.over = "lose:" + chosen["string_id"]

    # ------------------------------------------------------------------- player
    def available(self):
        """Leaf actions the menu would currently show as enabled."""
        out = []
        for n in self.leaves:
            if n.get("shown_if") and self.get(n["shown_if"]["variable"]) != n["shown_if"]["value"]:
                continue
            if n["string_id"].startswith("FINANCING:"):
                continue  # financing is chosen as part of a construction project
            out.append(n)
        return out

    def _resolve(self, node) -> str | None:
        if node.get("poll"):
            actor = next(a for a in AI[self.role] if a["id"].upper() == node["poll"]["actor"].upper())
            sub = self.find_poll(actor["tree"], node["poll"]["branch"]) or []
            return self.walk(sub)
        return node.get("outcome_id")

    def do_outcome(self, oid):
        for b in OUTCOMES.get(oid, []):
            if not b["conditions"] or self.test(b["conditions"]):
                self.process_effects(b["effects"], "player")
                return b["result"]
        return None

    def flush_immediate(self) -> bool:
        """Engine.enqueueEventResults(immediate=True). Returns True if an immediate message was shown."""
        shown, keep = False, []
        for p in self.pending:
            if p["immediate"] and p["timing"] == 0:
                shown = shown or bool(p["tag"])  # the shipped game never applies these changes
            else:
                keep.append(p)
        self.pending = keep
        return shown

    def finance(self, project) -> bool:
        """Pick the funder most likely to pay; returns True if the project gets funded."""
        self.set("project cost", self.get(project["sets_variable"]["from"]))
        funders = [n for n in self.leaves if n["string_id"].startswith("FINANCING:")]
        cost = self.get("project cost")
        pool = {"FinanceUsa": "usa budget", "FinanceUn": "un budget", "FinanceEu": "eu budget",
                "FinanceIsrael": "israel budget", "FinanceOtherPalestinians": "other groups budget",
                "SelfFinance": "budget", "FinanceArab": None}
        self.rng.shuffle(funders)
        funders.sort(key=lambda n: -(self.get(pool[n["outcome_id"]]) if pool.get(n["outcome_id"]) else
                                     self.get("egypt budget") + self.get("jordan budget")))
        for f in funders:
            if f.get("enabled_if_any") and not any(self.get(p["variable"]) >= self.get(p["value"]) for p in f["enabled_if_any"]):
                continue
            res = self.do_outcome(f["outcome_id"])
            self.flush_immediate()
            if res == "success":
                return True
            if res != "repetition":
                return False  # one refusal/delay per attempt, as in the UI
        return False

    def take_turn(self, node) -> str:
        """Play one leaf action. Returns the result label; 'repetition' etc. cost no turn."""
        if node.get("then_requires"):
            if not self.finance(node):
                self.log["unfunded"] += 1
                return "unfunded"
        oid = self._resolve(node)
        res = self.do_outcome(oid) if oid else None
        if self.flush_immediate():
            self.log[f"immediate:{res}"] += 1
            return res or "immediate"
        for q in self.advance(is_ai=False):
            self.apply_changes(q["changes"])
        self.run_ai()
        self.recalc()
        self.check_plot()
        for pin in self.pins:  # the player must open every news pin before acting again
            self.apply_changes(pin["changes"])
        self.pins.clear()
        self.recalc()
        self.log[f"player:{node['label']}:{res}"] += 1
        return res or "none"


# ------------------------------------------------------------------------- policies
def policy_random(g: Game):
    return g.rng.choice(g.available())


def policy_greedy(g: Game, samples: int = 2):
    """One-step lookahead on min(internal, external), averaged over a few random rollouts."""
    best, best_val = None, -1e9
    for n in g.available():
        tot = 0.0
        for _ in range(samples):
            sim = g.clone(random.Random(g.rng.random()))
            res = sim.take_turn(n)
            if res in ("repetition", "unfunded") or res is None:
                tot -= 1000
                continue
            i, e = sim.scores
            tot += min(i, e) + 0.25 * (i + e)
        if tot > best_val:
            best, best_val = n, tot
    return best


def play(role, difficulty, policy, seed, max_turns):
    g = Game(role, difficulty, random.Random(seed))
    pick = {"random": policy_random, "greedy": policy_greedy}[policy]
    stalls = 0
    while not g.over and g.turn < max_turns and stalls < 50:
        before = g.turn
        g.take_turn(pick(g))
        stalls = stalls + 1 if g.turn == before else 0
    return g


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--role", choices=["israeli", "palestinian"], default="israeli")
    ap.add_argument("--difficulty", choices=["calm", "tense", "violent"], default="tense")
    ap.add_argument("--policy", choices=["random", "greedy"], default="greedy")
    ap.add_argument("--games", type=int, default=50)
    ap.add_argument("--max-turns", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--json", action="store_true", help="print a JSON summary")
    args = ap.parse_args()

    results, turns_win, first_ms, top = collections.Counter(), [], collections.defaultdict(list), collections.Counter()
    violence = []
    for i in range(args.games):
        g = play(args.role, args.difficulty, args.policy, args.seed * 100003 + i, args.max_turns)
        results[g.over or "timeout"] += 1
        if g.over == "win":
            turns_win.append(g.turn)
        for t, ms in g.milestones:
            first_ms[ms].append(t)
        violence.append(g.get("endreport"))
        top.update({k: v for k, v in g.log.items() if k.startswith("player:")})

    summary = {
        "role": args.role, "difficulty": args.difficulty, "policy": args.policy, "games": args.games,
        "results": dict(results),
        "turns_to_win": ({"median": statistics.median(turns_win), "min": min(turns_win), "max": max(turns_win)}
                         if turns_win else None),
        "milestone_turn_median": {k: statistics.median(v) for k, v in first_ms.items()},
        "end_report_violence_median": statistics.median(violence),
        "most_used_actions": top.most_common(12),
    }
    if args.json:
        print(json.dumps(summary, indent=1))
    else:
        for k, v in summary.items():
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

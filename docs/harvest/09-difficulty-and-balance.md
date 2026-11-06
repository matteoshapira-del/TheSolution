# 09 · Difficulty and balance (measured)

## What difficulty changes

From `Engine.getDifficultyDelay` and `getDifficultySleep`:

| | Calm | Tense | Violent |
|---|---|---|---|
| Extra opening sleep for each difficulty-scaled AI actor | 6 + U[0..8] turns | 6 + U[0..4] | 6 + U[0..3] |
| Every `#SleepDifficulty` nap (after attacks, protests…) | +3 turns | +1 turn | −1 turn |

That's all it changes. Probabilities, thresholds, effect sizes and scoring are identical at every level, so
difficulty only sets **how often the world interrupts you.**

## Simulation results

`tools/harvest/simulate.py` re-implements the turn loop ([03](03-turn-loop.md)) on top of `data/harvest/*.json`
and nothing else. That it runs and produces sensible arcs is our main evidence the harvest is complete. Two policies:

* **random**: uniform over currently available leaf actions (a naive player).
* **greedy**: one-step lookahead. Each candidate action is tried twice on a cloned state, and the one maximising
  `min(internal, external) + 0.25·(internal + external)` is picked (a competent player).

300 random and 100 greedy games per cell, 200-turn cap, seed 1 (`data/harvest/simulation_results.json`).

| Role | Difficulty | Random: win / lose / timeout | Random: turns to win (median) | Greedy: win rate | Greedy: turns to win, median (range) | Greedy: violence tally (median) |
|---|---|---|---|---|---|---|
| Israeli PM | calm | 5% / 89% / 6% | 136 | 100% | 27 (24–31) | 152 — EXTREME |
| Israeli PM | tense | 4% / 92% / 4% | 110 | 100% | 28 (24–33) | 175 — EXTREME |
| Israeli PM | violent | 2% / 95% / 3% | 155 | 100% | 29 (24–36) | 218 — EXTREME |
| Palestinian Pres. | calm | 97% / 3% / 0% | 63 | 100% | 21 (18–26) | 18 — LOW |
| Palestinian Pres. | tense | 85% / 14% / 1% | 67 | 100% | 21 (19–25) | 26 — LOW |
| Palestinian Pres. | violent | 48% / 47% / 5% | 75 | 100% | 22 (19–26) | 38 — LOW |

Greedy milestone timing (median turn): Israeli 9 / 14 / 19 / win 28; Palestinian 7 / 11 / 15 / win 21.

## What the numbers say

1. **The two sides are very unequal.** A naive Israeli player almost always loses to "The Third Intifada" (external
   score ≤ −50), with a median loss at turn 15. A naive Palestinian player usually wins. The Palestinian menu has
   many low-risk positive actions (16 foreign-negotiation leaves, mostly upside), while about a third of the Israeli
   menu is hawkish actions with heavy external costs.
2. **Difficulty barely matters to a competent player.** It moves the greedy win time by about one turn. It matters
   a lot to a naive Palestinian player (97% → 48%).
3. **There's a dominant Israeli line**: *Withdrawal Support* (government), *Demand / Ask for Anti-Militant
   Support* (PA president), *Suppress Violence* and *Arrest Extremist Leaders* (Yesha), *Educational / Cultural
   Initiatives*. These raise both scores, and their cooldowns interleave neatly.
4. **There's a dominant Palestinian line**: *Housing*, *Power Plant*, *Health Care*, *Pro Law and Order* speeches,
   *Request a Meeting* (foreign), *Seaport*, then *Declare Independence* once the external score is about 85.
5. **Winning and stability are decoupled.** Greedy Israeli wins leave an EXTREME violence verdict, because the
   dominant line includes forceful anti-militant measures. The game tells you the peace won't hold, and nothing
   follows from it.
6. **Games are short**: about 20–30 actions for a skilled player, which, with reading time, fits a single session.
   A naive player takes 60–150 turns to win, if they win at all.

## Simulator fidelity

The simulator follows the decompiled control flow, including its quirks ([11](11-quirks-and-bugs.md)). Where it
can't, it simplifies:

* If one player outcome queues several news events, the shipped UI applies only the first immediately and then
  depends on dialog flow. The simulator applies all of them. This affects very few tables.
* Financing picks the richest eligible funder rather than asking a human.
* Music, tutorials, animations and save/load are skipped.
* Unity's RNG is replaced by Python's, so distributions match but individual games don't.

Treat the table as a balance profile, not a guarantee of exact in-game rates. It's still enough to see the
asymmetry, the dominant strategies and the short game length.

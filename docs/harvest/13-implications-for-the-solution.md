# 13 · What the harvest means for *The Solution*

The goal: an upgraded successor in which the conflict can end in **many different ways**, not only a two-state
win or a loss. This chapter turns the harvest into design input. Detail on the real-world solution proposals is in
the companion research report (*Israeli Palestinian conflict solutions spectrum*, PDF).

## Keep (it works and is cheap to reuse as an *approach*)

* **Data-driven rules.** Outcome tables with a tiny condition language (`#Threshold` bands plus ordered fallbacks)
  are easy to author, balance and translate. Reimplement the idea in our own engine and schema. The
  `tools/harvest/simulate.py` loop is a working reference of about 400 lines.
* **Two audiences per leader** (home constituency vs. the other side and the world). This is the core tension and
  plays well.
* **Graded results** (success / sub-optimal / delay / refusal / failure) with backlash. Nothing is free.
* **Stakeholder AI** that reacts to its own meter. Simple, legible, and debuggable.
* **News as feedback**, with a tag ontology (`actor, menu, choice, feedback, result`) and several random variants
  per tag.
* **Opposing advisors** at every decision, and **three languages with RTL** from day one.
* **Cooldowns** that stop spam, and the **violence ledger** concept.

## Fix (gaps the harvest exposed)

| Gap in PeaceMaker | Evidence | Direction for The Solution |
|---|---|---|
| Endings are just two score thresholds; the world state is ignored | [04](04-scoring-and-endings.md): sovereignty flags and `independent state` aren't read by ending logic; the Israeli side has no final-status state | Make endings **regions of a final-status state space**, checked alongside legitimacy and stability |
| Only one win per side, always framed as two states | 2 win events + 4 losses | A catalogue of 10–15 endgames across the whole spectrum, each with *stable / fragile / collapsing* quality tiers |
| Violence has no consequence | EXTREME tallies still win ([09](09-difficulty-and-balance.md)) | Violence and rights violations feed ending quality, external legitimacy and AI escalation |
| Severe side asymmetry | Naive Israeli play 2–5% win vs. Palestinian 48–97% | Balance each role with the simulator in CI; target comparable naive and expert curves |
| Dominant strategies | Same 5–6 actions in every greedy win | Diminishing returns, constituency fatigue, events that invalidate strategies |
| Difficulty only changes AI tempo | [09](09-difficulty-and-balance.md) | Scenario-based difficulty: starting state, leaders, regional climate, demography |
| No real negotiation | Talks are one-shot menu items | A negotiation layer: offers on core issues, counter-offers, linkage, spoilers |
| Opaque scoring | Hidden formulas, Yesha shown but not counted | Show the formulas, and preview an action's likely effects |
| Fixed 2007-era world | Hamas–Fatah, US/UN/EU only | 2026 actors: Gulf states and normalisation, Egypt, Jordan, Iran and proxies, international stabilisation bodies |

## A proposed endgame model

**1. Final-status dimensions.** New state variables, each with a small set of discrete positions:

| Dimension | Example positions (the extremes are included, and all are reachable) |
|---|---|
| Sovereignty structure | Israeli rule without Palestinian rights · autonomy · Jordanian or Egyptian link · Palestinian state(s) · confederation · federation · one shared state |
| Territory and borders | % of the West Bank and Gaza under Palestinian authority; settlement status (expanded / frozen / evacuated / residents of Palestine) |
| Security | IDF control · joint · international force · demilitarised state · full Palestinian security |
| Jerusalem and holy sites | Israeli sovereignty · divided · shared capital · special international regime |
| Refugees | none · compensation · symbolic return · return to Palestine · large-scale return |
| Citizenship and rights | full equality · residency without citizenship · partial · denied |
| Population movement | none · voluntary, compensated · coerced *(a catastrophic branch, with legal and international costs)* |
| Regional frame | isolation · normalisation · regional security architecture |

PeaceMaker's Palestinian flags already map onto several of these (airspace, coast and water, which feed sovereignty;
the Gaza border, international troops, joint patrols and training, which feed security; holy-site control and access,
which feed Jerusalem; `independent state`, which feeds sovereignty). The Israeli side would need new state (settlement
footprint, fence route, checkpoint level, refugee policy), driven by the existing actions.

**2. Ending = arrangement + acceptance + stability.** Each turn, evaluate every endgame definition:

* the **arrangement** matches its region on the dimensions above,
* **acceptance**: each relevant constituency's legitimacy is above its threshold (an evolved form of the two scores),
* **stability**: the violence and grievance trend stays under a ceiling for N turns (an evolved form of `hold_for`).

Several endings can be "in reach" at once. Show the player which ones, and how close each is.

**3. Ending quality.** The same arrangement reached through mass violence, coercion or rights denial scores as
*fragile* or *collapsing*, with an epilogue showing why. That turns the existing violence ledger into consequence.

**4. Morally fraught outcomes.** Endpoints such as forced population transfer, or annexation without political
rights, are real proposals in the public debate, so the game can include them as *reachable states*. But it should
model them honestly: as violations of international law with cascading costs (sanctions, legitimacy collapse,
regional war, internal resistance), presented as outcomes to understand, not victories to aim for. The research
report documents the legal and empirical basis for each.

## Intellectual property hygiene

PeaceMaker's mechanics (meters, thresholds, turn order) are ideas and free to build on. Its **name, text, advisor
lines, events, photos, video, music and look** belong to ImpactGames and its licensors. The Solution should use
original writing and art and its own branding, and treat `harvest_raw/` as reference only. Committing only
mechanics-level data here keeps that line clear.

## Suggested next steps (stage 2)

1. Pick the endgame catalogue (from the research report) and write the final-status dimension schema.
2. Port `simulate.py` into the game's own engine model. Add the new dimensions and the ending evaluator.
3. Write a vertical slice: one role, one scenario, about 30 actions, 4–5 reachable endings.
4. Put balance in CI: run the simulator nightly per role and difficulty and fail the build if naive or expert win
   rates leave their target bands.

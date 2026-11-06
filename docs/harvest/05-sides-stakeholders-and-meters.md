# 05 · Sides, stakeholders and meters

Full table with every variable, default and flag: [catalog/variables.md](catalog/variables.md).

The two roles are **not mirror images**. The Israeli game is a 12-meter approval model. The Palestinian game adds an
economy, a funding system and a set of sovereignty flags.

## Israeli Prime Minister (62 variables)

**Groups and leaders** (portrait bar; each is an approval meter, 0–100):

| Meter | Default | Feeds |
|---|---|---|
| Israeli Public (`israel people`) | 55 | internal score ×1 |
| Yesha / settlers' council (`yesha`) | 40 | Yesha AI only |
| Palestinian Authority President (`palestinian president`) | 25 | external ×1 |
| Palestinian Public (`palestinian people`) | 20 | external ×1 |
| Militant Groups (`hamas`) | 7 | Hamas AI only |
| United Nations (`un`) | 20 | external ×0.33, leadership |
| USA (`usa`) | 40 | external ×0.33, leadership |
| The Arab World (`arab world`) | 15 | external ×0.33, leadership |

**Polls** (book icons):

| Poll | Default | Role |
|---|---|---|
| Israeli Security (`security`) | 30 | internal ×1. Grows passively with Palestinian cooperation |
| Israeli Sympathy (`sympathy`) | 10 | internal ×1. Also raises the odds that settlement building goes *badly* |
| Militant-activity Suppression (`suppression`) | 25 | Lowers Hamas attack odds. Decays by 2 each turn |
| Palestinian Cooperation (`palestinian cooperation`) | 10 | Grows each turn with the Palestinian president's approval, and in turn grows security |
| Israeli Leadership (`leadership`) | 25 | derived: 0.33·(usa + un + arab world) |

**Hidden:** 41 `reject …` cooldowns, `aggression`, `negative effects`, `endreport`, the speech timers and win counters.

**Passive per-turn upkeep (`IsrClock`)**: suppression −2; palestinian cooperation += 3 × mod(pres. approval);
security += 1 × mod(cooperation); israel people += 1 × mod(security); sympathy += 0.5 × mod(security), where mod() is
the budget-modifier step table (0 below 15, 1.0 at 30–34, 2.5 at 75+). This is the Israeli game's only feedback
loop: **trust → cooperation → security → public approval.** Win the Palestinian president's trust and the
domestic numbers follow.

## Palestinian President (109 variables)

**Groups and leaders:**

| Meter | Default | Feeds |
|---|---|---|
| Palestinian Public | 30 | internal ×1 |
| Fatah | 70 | internal ×1 |
| Hamas | 20 | internal ×0.75 |
| Israeli Prime Minister | 30 | external ×1.25 |
| Israeli Public | 20 | external ×0.75 |
| United States | 20 | external ×1 |
| United Nations | 50 | external ×0.75 |
| The Arab World | 50 | external ×0.75 |

**Polls:**

| Poll | Default | Role |
|---|---|---|
| Palestinian Economy (`economy`) | 5 | internal ×1. Drives the PA's own budget income |
| Government Authority | 10 | internal ×1 |
| Palestinian Independence (`independence`) | 5 | Raised by 63 outcome tables. **Not in either score**; only the Palestinian Public AI reads it (to pick its mood) |
| President's Leadership (`leadership`) | 5 | external ×1.5 (the heaviest single weight in the game) |
| Palestinian View of Israel (`tolerance`) | 5 | internal ×1.25. Also lowers Hamas/Fatah attack odds |
| Israeli Cooperation | 5 | Grows 3 × mod(IPM approval) per turn |

**Money.** Eight budget pools fill every turn in proportion to each patron's approval (`Clock` → `addBudgets`):

| Pool | Default | Grows by | Driven by |
|---|---|---|---|
| USA | 20 | 3 × mod | US approval |
| UN | 20 | 1.5 × mod | UN approval |
| EU | 20 | 2 × mod | UN approval (sic) |
| Egypt / Jordan | 5 / 5 | 1 × mod each | Arab world approval |
| Israel | 10 | 1.5 × mod | Israeli PM approval |
| Other Palestinian groups | 0 | 2 × mod | leadership |
| PA's own budget | 10 | 1 × mod | **economy** (so nothing comes in until the economy reaches 15) |

**Project costs** (fixed): roads, infrastructure 10 · reopen schools 10 · communications, police training/funding,
Fatah "favours", reclaim settlements 20 · housing, agriculture, industry, water plant, health, poor relief, new
schools, police station, prison, arms import 30 · power plant 40 · seaport 50 · airport 60.

A funder pays only if its pool ≥ cost and a threshold roll on its patron's approval passes. Paying costs that
patron 7 approval points (but see [11](11-quirks-and-bugs.md): that penalty is never actually applied).

**Sovereignty flags** (0/1): control of airspace, coast, water table, schools, holy sites, the Gaza border and
internal travel; holy-site access for Palestinians, Israelis and foreigners; joint patrols and training;
international border troops; curriculum reform; tourism; airports and seaports built; independent state.
Each "Push for control of X" action flips its flag and unlocks the matching construction.

**Police:** `police units total` 2, `police units out` 0.

## Asymmetry at a glance

| | Israeli PM | Palestinian President |
|---|---|---|
| Win metric inputs | 3 internal + 5 external meters | 6 internal + 6 external meters |
| Economy / money | none | 8 budget pools, project costs, financing step |
| Territory / sovereignty | implicit in action names | 18 explicit flags (unused by endings) |
| Built-in feedback loop | trust → cooperation → security → approval | approval → budgets → projects → economy → own budget |
| AI actors | 9 | 7 |
| Leaf actions | 76 | 99 (+7 funders) |

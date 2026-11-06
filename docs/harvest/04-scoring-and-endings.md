# 04 · Scoring, milestones and endings

Source: `Engine.recalculateScore`, `EventsHelper.getPlotPoint`, `EndReportWindow.SetViolenceLevel`, and the
`events` and `event_scores` DB tables. Machine-readable copies are in `data/harvest/engine.json` and
`data/harvest/milestones_and_endings.json`.

## Two scores per side

Each role has an **internal** score (your own constituency) and an **external** score (the other side and the
world). Both are shown as `n/100` and both may go negative.

| Role | Internal ("left") raw sum | Zero at | 100 at | External ("right") raw sum | Zero at | 100 at |
|---|---|---|---|---|---|---|
| Israeli PM | `israel people + security + sympathy` | 95 | 280 | `palestinian president + palestinian people + 0.33·(usa + un + arab world)` | 70 | 270 |
| Palestinian President | `1.25·tolerance + palestinian public approval + fatah approval + economy + government authority + 0.75·hamas approval` | 136.25 | 500 | `1.5·leadership + 1.25·israeli PM approval + usa approval + 0.75·(israeli public + un + arab world approval)` | 155 | 500 |

Mapping, truncated to an integer:

```
raw < zero          : score = (raw − zero) / zero × 100            → −100 … 0
zero ≤ raw ≤ full   : score = (raw − zero) / (full − zero) × 100   →    0 … 100
raw > full          : score = 100
```

* The zero points equal the starting values, so **every game starts at 0 / 0**.
* Losses are steep. Below zero, one raw point is worth about **2×** as much as above zero for the Israeli
  internal score (95 vs 185 spread) and about **2.6×** for the Palestinian internal score (136 vs 364). Damage costs
  more than repair earns.
* In the Israeli game, `leadership` is recomputed every turn as `0.33·(usa + un + arab world)`.
* **The Yesha settlers' council is not in the Israeli score.** The in-game explanation says the left score "is a
  sum of your public approval, the concerns of the Yesha settler's council and Israel's sense of security", but the
  code adds `sympathy` instead. Yesha matters only indirectly, through its AI actor's protests and attacks.
* The Hamas/"militant groups" meter in the Israeli game isn't in either score. It only feeds the Hamas AI.

## Milestones and endings (plot points)

Checked once per turn, right after the AI phase. A plot point fires only when its condition has held for
`hold_for + 1` consecutive checks. At most one fires per turn. Milestones fire once.

| Role | Plot point | Condition (both scores unless noted) | Consecutive turns | Result |
|---|---|---|---|---|
| both | Milestone 1 | ≥ 30 | 2 | Cut-scene video. Israeli: "Gaza Approaches Independence". Palestinian: same headline |
| both | Milestone 2 | ≥ 50 | 2 | Israeli: "Train Travels between Gaza and the West Bank". Palestinian: "Train Route between Gaza and West Bank" |
| both | Milestone 3 | ≥ 70 | 2 | Israeli: "Winds of Peace". Palestinian: "West Bank Approaches Independence" |
| Israeli | **Win** | ≥ 95 | 4 | "You Win: Two-State Solution" |
| Israeli | Lose (internal) | internal ≤ −50 | 4 | "You Lose: You Have Been Removed from Office" |
| Israeli | Lose (external) | external ≤ −50 | 4 | "You Lose: The Third Intifada" |
| Palestinian | **Win** | ≥ 95 | 4 | "You Win: Palestine Attains Statehood" |
| Palestinian | Lose (internal) | internal ≤ −50 | 4 | "You Lose: A Civil War Breaks Out" |
| Palestinian | Lose (external) | external ≤ −50 | 4 | "You Lose: International Support Pulled" |

So there are **exactly two kinds of win** (one per side, both framed as a two-state outcome) and four losses. The
milestones are a fixed narrative track (Gaza, then a corridor, then the West Bank, then statehood). They don't
depend on what you did, only on your score.

### Endings ignore the world state

The Palestinian game tracks concrete final-status facts as variables: `independent state`, `control airspace`,
`control seaspace`, `control water`, `control holy sites` and the three holy-site access flags, `control gaza border`,
`control internal travel`, `control education`, `airports`, `seaports`, `joint patrols`, `joint training`,
`curriculum restructured`, `tourism open`. **None of them is read by the ending logic.** They only gate menu items
(e.g. airport construction needs airspace control). Declaring independence gives a large score bonus and sets
`independent state = 1`, but the flag isn't checked anywhere.

The Israeli game has **no** final-status variables at all. Settlements, the fence, checkpoints, refugees and
Jerusalem exist only as actions that move approval meters.

In short, PeaceMaker models *legitimacy*, not *arrangements*. The "two-state solution" is narrative framing laid
over a two-meter score threshold. This is the main structural gap The Solution has to close
(see [13](13-implications-for-the-solution.md)).

## The violence "end report"

A separate tally, `endreport` (the only variable allowed above 100), accumulates a violence cost from almost every
security action and every attack (+5 to +20 per event). On the ending screen it's shown as a slider with a verdict:

| `endreport` | Verdict | Text tone |
|---|---|---|
| ≤ 0 | NONE | violence lower than anticipated, so peace has a bright future |
| 1–50 | LOW | same |
| 51–100 | MODERATE | consistent with previous times, so peace is not certain to hold |
| 101–150 | HIGH | very high, so peace is unlikely to be stable |
| > 150 | EXTREME | same |

The verdict is commentary only and doesn't change the outcome. In our simulations a strong Israeli player wins with
a **median violence tally of 150–220 (EXTREME)**, while a strong Palestinian player wins at **18–38 (LOW)**
(see [09](09-difficulty-and-balance.md)). The game tells you the peace you won won't last, but doesn't let that
change anything. That's a ready-made hook for multiple, *qualified* endgames.

# 06 · Actions and outcomes

Every leaf action, every result branch, every number:
[catalog/actions-israeli.md](catalog/actions-israeli.md) · [catalog/actions-palestinian.md](catalog/actions-palestinian.md).

## The menus

### Israeli Prime Minister (24 top-level actions, 76 leaves)

| Category | Action → choices |
|---|---|
| Construction | **Settlements**: expand existing / build new / freeze / remove existing · **Domestic initiatives**: economic stimulus / social programs / educational grants · **Fund Palestinian medical institutions**: directly / via UN · **Fund Palestinian education**: no conditions / only if incitement stops · **Fund reconstruction**: civilian / infrastructure / security aid · **Security fence**: along the Green Line / around or between settlements / remove part · **Refugee affairs**: allow refugee immigration / authorize compensation |
| Politics | **Speech to your people**: security / peace process / Palestinian cooperation / anti-militancy / *listen to concerns* · **Talk to your government**: unite for peace / less criticism / *listen to concerns* / promise more security / withdrawal support · **Speech to the world** (4 themes) · **Yesha issues**: ask for restraint / promise concessions / suppress violence / arrest extremist leaders · **Talk to the Palestinian president**: ask for anti-militant support / demand anti-militant action / *listen to concerns* / promise security concessions / promise reconstruction aid · **Negotiate with the world** (USA, UN, EU): mediation support / political pressure on Palestine · **Trade restrictions** ± · **Worker permits** ± · **Cultural initiatives**: cross-cultural projects / educational / trade / structured dialogue |
| Security | **Army**: secure area / arrest militants / destroy militant infrastructure / withdraw units · **Police**: patrol / secure area / withdraw · **Checkpoints** ± · **Curfews** ± · **Release prisoners**: non-violent / violent · **Missile strike**: militant HQ / government infrastructure / Palestinian police · **Assassinate a militant leader**: Apache strike / covert operation · **Bulldoze**: clear routes / punish militants |

### Palestinian President (22 top-level actions, 99 leaves + 7 funders)

| Category | Action → choices |
|---|---|
| Construction | **Civilian**: housing / agriculture / industry / reclaim evicted settlements · **Transportation**: roads / push for airspace control → airport / push for coastal control → seaport · **Natural & national resources**: infrastructure / communications / push for water-table control → water treatment plant / power plant · **Social services**: push for control of schools → reopen schools / build schools / reform curriculum (co-existence) or revert it / health care / care for the poor · **Governmental**: police station / prison / import arms · **Tourism**: open / close (needs an airport and a seaport) |
| Financing | **Finance project**: USA / UN / EU / Arab states / PA budget / Palestinian allies / Israeli investment (a step inside every construction project) |
| Politics | **Speech to Palestinians**: law & order / reconstruction / anti violent resistance / pro violent resistance · **Speech to the world**: demanding / hopeful / cautious · **Internal negotiations**: Fatah (law & order, peace agenda, anti-corruption, financial favours) and Hamas (law & order, two-state support, cease resistance, disarm & unify) · **Negotiate with Israel**: stop aggression / withdrawal / wall removal / offer thanks · **Foreign negotiations** (USA, UN, Egypt, Jordan): request a meeting / aid / investment / pressure on Israel · **Declare an independent state** · **Holy sites**: push for control, then restrict or permit access for Palestinians, Israelis or foreigners |
| Security | **Police presence**: maintain order / patrol for militants · **Manage police**: restructure / train / raise or cut funding · **Extreme measures**: arrest known militants / seize arms / assassinate a militant leader · **Joint forces with Israel**: start or stop joint training / joint patrols · **Internal travel**: push for control, then lower or raise restrictions · **Gaza border**: push for control / patrol presence ± / open or close / request or end an international presence |

## How a result is chosen

A typical table, *Order the Israeli Army › Arrest Palestinian Militants*:

| # | Result | Condition | Effect highlights |
|---|---|---|---|
| 10 | repetition | `reject idf` > 0 | nothing, and no turn passes |
| 20 | sub-optimal | `sympathy` ≥ rand(40–60) | Israeli public −4, Yesha +6, PA president −6, Palestinian public −6, USA +4, security +4, suppression +12, violence +12 |
| 30 | success | otherwise | Israeli public +8, Yesha +8, PA president −5, Palestinian public −5, USA +5, security +6, suppression +12, violence +12 |

The patterns that repeat across all 300 tables:

* **Cooldown first.** 136 tables open with a `repetition` branch keyed to a `reject <channel>` variable. Using a
  channel sets it +3 or +4, which blocks that channel for about two turns.
* **Thresholds on one or two meters.** 210 `#Threshold` checks. The success band is usually centred at 25–50 with
  ±5–10 of noise, so outcomes are predictable once a meter is clearly above or below the band.
* **Graded failure.** Results fall into success, sub-optimal, delay, refusal and failure. Even a "failure" usually
  moves the meters you aimed at, just less, and with backlash elsewhere.
* **Each action trades between constituencies.** Building settlements gains Yesha +15–20 and the Israeli public
  +8–10, but costs the PA president −15–17, the Palestinian public −20–22, the UN and Arab world about −15 each,
  and the USA −5–6.

## Score impact ranking

Change in the two scores (in score points, positive regime) from each action's *success* branch. Computed with
the formulas in [04](04-scoring-and-endings.md).

**Israeli PM, best for external (peace) score:** remove existing settlements (+27 ext), freeze settlements (+21),
security aid to the PA (+16), remove part of the fence (+16), allow refugee immigration (+14), arrest extremist
settler leaders (+12). **Best for internal:** demand anti-militant action from the PA (+14), ask for anti-militant
support (+10), strike government infrastructure or PA police (+9–11, but −20 ext). **Worst trade-offs:** build or
expand settlements (+7–8 int, −23 to −26 ext), missile strikes on the PA (−20 to −21 ext, +20 violence).

**Palestinian President, best overall:** declare independence (+32 int / +22 ext, but only if the external score is
already ≈ 85), airport (+13/+12), seaport (+11/+10), open tourism (+10/+11), power plant (+13/+5), health care
(+12/+4). **Worst:** close tourism (−10/−13), decrease border patrol presence (−12 ext), end international border
patrols (−10 ext), pro-violent-resistance speech (−8 ext).

## Special mechanics

* **Listen to Concerns** (Israeli people, Israeli government, Palestinian president) runs the stakeholder's own AI
  "concerns" sub-tree. That tree finds the stakeholder's *lowest* related meter (`#LowestTopic`) and returns a
  matching outcome, so these actions work as diagnostic polls with small side effects.
* **Financing** (Palestinian): choosing a project sets `project cost`. A funder is then tried. Success, delay or
  refusal come back as an *immediate* message. On success, closing the message launches the project as the turn's
  action, and the funder's pool is reduced by the cost (Arab states split it between Egypt and Jordan).
* **Gated menus** (Palestinian): each "push for control" action is an upstream step that unlocks construction.
  It's the only place PeaceMaker models a *sequence* of sovereignty steps.
* **Declare independence** is a threshold gamble on your *external* score: success at ≈ 85, "close" at ≈ 70,
  polite refusal at ≈ 55, strong refusal at ≈ 35.

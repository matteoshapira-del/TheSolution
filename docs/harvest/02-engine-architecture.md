# 02 · Engine architecture

PeaceMaker is a **data-driven stock-and-flow simulation**. Around 170 numeric variables (meters) hold the state.
Each player action and each AI actor move is an *outcome table*, which picks one result branch from the
current state plus some randomness. That branch then changes variables and shows a news event. Two derived scores
decide the ending.

```
            ┌──────────── init.xml ─────────────┐
            │ variables + defaults + flags      │
            └───────────────┬───────────────────┘
                            ▼
 player menu (DB actions) ──► actions-to-outcomes ──► outcomes.xml ──► effects ──► variables
         ▲                                              ▲                │            │
         │                                              │                ▼            ▼
   advisors / polls            ai2.xml (AI actors) ─────┘         news events   recalculateScore()
   (data.en-us, DB)            run every turn                     (events DB,   internal / external
                                                                  random variant)       │
                                                                                         ▼
                                                                 plot points (events DB: milestones, win, lose)
```

## 1. Variables (`init.xml` → `data/harvest/variables.json`)

* Each role has its own variable set: **62 Israeli** and **109 Palestinian**.
* Values are clamped to **0–100** unless a variable is flagged `can-be-negative` (only the two authority scores)
  or `can-be-over-100` (only `endreport`, the violence tally).
* `auto-decrement` variables (41 Israeli, 38 Palestinian) drop by 1 every time effects advance. These are the
  **`reject …` cooldowns**, plus `aggression` and `negative effects`.
* Unknown variable names that turn up in conditions are created on the fly at 0. `#Roll` uses this to store dice
  results (`roll`, `flip`, `roll2`).

## 2. Actions (DB `actions` table → `data/harvest/actions.json`)

* A tree per role: **category → top-level action → (sub-menu…) → leaf**. Israeli: 3 categories, 24 top-level
  actions, 76 leaves. Palestinian: 4 categories (with Financing), 22 top-level, 99 leaves.
* A leaf resolves to an outcome id. The engine takes the last `:` segment of the action string id, looks it up in
  `actions-to-outcomes`, and falls back to the id itself (`Engine.doAction`).
* Menu control columns:
  * `variable_show_id/value`: show the item only if *variable = value* (toggles such as Open/Close Tourism).
  * `action_variable_prereqs`: grey the item out unless *variable = value* (or ≥, with `#Greater`). This gates
    projects behind sovereignty, e.g. *Airport Construction* needs `control airspace = 1`.
  * `variable_set_id/value` + `require_action_id`: Palestinian construction projects copy their cost into
    `project cost`, then force the **Finance Project** sub-menu. The project only runs if a funder pays.
  * `poll_actor/poll_branch`: "Listen to Concerns" doesn't use its own outcome table. It runs part of an AI
    actor's decision tree and plays whatever that tree returns.

## 3. Outcome tables (`outcomes.xml` → `data/harvest/outcomes.json`)

```
Outcomes[actionID]
  Outcome (Order, Result, Conditions?, ActionEffects)   ← tested in document order; first pass wins
    ActionEffect (Timing, Type?, Tags, Effect*, Method*)
```

**Condition language** (`Engine.testOutcomeConditions`). All conditions in a list must pass:

| op | meaning |
|---|---|
| `#Threshold x t v` | pass if `x ≥ Uniform(t−v, t+v)`. This is the main source of randomness: P(pass) rises linearly from 0 at t−v to 1 at t+v |
| `#NotThreshold` / `#ThresholdNot` | negation of the above |
| `#Greater`, `#GreaterEquals`, `#Less`, `#Equals`, `#NotEquals` | plain comparisons (args are numbers or variable names) |
| `#Roll name n` | store a random integer in `[0, n)` in `name`; always passes |
| `#LowestTopic topic` | pass if `topic` has the lowest value in the list given in the first condition's Argument2 |
| `#HighestTopic` | intended mirror of the above; buggy (see [11](11-quirks-and-bugs.md)) |
| `#Assign`, `#Add` | arithmetic on temp variables (used to sum Egypt+Jordan budgets) |
| `#And` | no-op separator |
| anything else | logged, and treated as pass |

**Effect language:**

* `Effect` = add `Change` to `VariableID` (`true`/`false` become +1/−1). Positive changes to auto-decrement variables
  get a hidden +1, so a cooldown survives the decrement that same turn.
* `Method`s run as soon as the branch is chosen: `#Sleep actor n`, `#SleepDifficulty actor n`, `#Subtract a b`,
  `#Addition a n`, `#Divide a n`, `#AdditionBudgetMult a b k` (a += k × budgetModifier(b)).
* `Timing` = delay in effect-advances (698 effects at 0, 4 at 4).
* `Type`: `Immediate` (the message shows at once and **no turn passes**, e.g. "you just did this"), `Feedback`,
  `White-Event`, `Red-Event` (map pin colour), `Hidden` (silent per-turn upkeep).
* `Tags` = the news event key. The engine counts every event row with that tag and **shows one at random**
  (`EventsHelper.getEvent`). The tag's variants share the effect; only the prose differs.

**Result labels** across all branches: success 163, repetition 136, sub-optimal 65, delay 53, refusal 53 (plus
polite/strong/violent variants), failure 30, aggression 29, words 13, neutral 9, plus about 60 bespoke labels, mostly
for AI moves ("join political process", "partial disarmament", "blame you", "offer to meet for negotiations"…).

## 4. AI actors (`ai2.xml` → `data/harvest/ai_actors.json`)

* An ordered list per role: Israeli game 9 actors, Palestinian game 7. Each is a **branching decision tree** over
  the same condition language, ending in an outcome id, `NoAction`, or a music cue.
* `callFrequency` is how many turns the actor sleeps after acting. `affectedByDifficulty` adds a random initial
  delay and scales `#SleepDifficulty` naps. `bundleWithUserFeedback` makes the actor's effects apply with the
  player's turn (used by the "clock" upkeep actors).
* **AI moves always apply the first branch of their outcome table.** The AI path doesn't test conditions
  (`AIHelper.RunAICheck`), because the tree already did the deciding.

## 5. Events and plot points (DB `events`, `event_scores`)

* 1,350 events: 1,338 tagged feedback/news events, plus 12 *plot* events (6 per role: 3 milestones, 1 win, 2 losses).
* Plot events carry score thresholds and a `score_hold_for` count. They're checked once per turn (see [04](04-scoring-and-endings.md)).

## 6. Scoring layers

`Engine` keeps a history list per variable plus a per-turn *feedback* overlay (`m_feedbackScores`). Player changes go
to the overlay first, so the UI can show green/red deltas, and get committed in `IntegrateScores()`. Reads always see
the overlay, so for simulation purposes changes are effectively immediate.

## 7. Persistence and telemetry

* Save games are stored in the DB (`save_games`, `save_game_variables` with full history, `save_game_plot_points`).
  One autosave per role. The game saves after every turn once all news pins are opened.
* **Research telemetry**: `play_sessions`, `play_turns` (action, actor, logic trace, taken) and `play_variables`
  (every variable change, per turn) log a complete play trace. A hidden *REMOTE* menu item toggles remote logging.
  The tables ship empty, but the instrumentation makes clear the remaster was built with learning research in mind.
* Debug menu entries are still compiled in: *ADD* / *SUBTRACT* (±10 to every variable), *CRASH*, *RESET*, *REMOTE*.

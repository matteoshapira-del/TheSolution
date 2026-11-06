# 11 · Quirks, bugs and inconsistencies

These come from a static reading of the decompiled 2015 build and its data, and the headless simulator reproduces
them. They haven't been confirmed by playing the shipped game, so treat them as **strong hypotheses**. They matter
because some of them change balance, and they show which systems were never fully finished.

## Engine

1. **Immediate results never apply their variable changes.** For outcomes of type `Immediate` (repetition, and all
   financing results, which are forced immediate), the message is shown but its `Effect` changes are dropped. Only
   `Method`s (budget subtraction, sleeps) run. As a result:
   * paying for a project never costs the funder's approval (the intended −7 never happens), and
   * a refused or delayed financing request never sets its `reject …` cooldown, so you can ask again at once.
2. **Untagged effects are never executed.** `Engine.enqueueEventResults` calls the coroutine
   `applyActionEffects(...)` without iterating it, so its body never runs. Only the two silent upkeep outcomes are
   untagged, and they work through Methods, so the practical impact today is nil. It's a trap for anyone extending
   the data.
3. **Non-bundled AI actors can't change variables through Methods.** `setScore(ScoreType.AI)` only records a value
   that's unchanged, so any `#Addition` or `#Subtract` in an AI outcome would be a no-op unless the actor is bundled
   (`IsrClock`, `Clock`). The shipped data only uses value Methods in those two bundled actors, so this is latent.
4. **`#HighestTopic` is broken.** It starts from 0 and keeps values *lower* than the running value, so it always
   returns the first topic in the list.
5. **Cooldowns and delayed effects advance twice per turn** (once after the player's action, once after the AI).
   That's probably unintended, but the data was tuned around it.
6. **Plot points are checked before the player opens the AI news pins**, so pin effects count toward the next
   turn's check.
7. **AI outcomes ignore their own conditions.** The AI path always applies the first branch of an outcome table.
   All 107 AI-reachable tables are single unconditional branches, so it's consistent today, but it limits extensions.
8. **Duplicate outcome tables.** 20 action ids appear twice in `outcomes.xml`
   (e.g. `IPMWinState`, `PoliceSeizeMilitantArms`, the `IPMPress…` family). `SelectSingleNode` always takes the
   first, so the second copies are dead data.

## Data

9. **The water treatment plant is free.** Its project-cost pointer is misspelled (`WATER TEATMENT PLANT`), so
   `project cost` resolves to 0 and any funder pays.
10. **The Gaza border open/close visibility looks inverted.** *Open Borders* shows only when `gaza border open = 1`,
    and *Close Borders* only when it's 0. The border starts open, so the menu offers to open it.
11. **The score explanation doesn't match the formula.** The Israeli text says Yesha counts toward the internal
    score. It doesn't; `sympathy` does.
12. **Action string ids contain copy-paste slips** (e.g. *Build New Settlement* lives under
    `ISRAEL REMOVE SETTLEMENTS: …`). This is harmless, because resolution uses only the last segment.
13. **The EU funding pool grows with UN approval.** There's no EU approval meter in the Palestinian game.
14. **Three tutorial steps are blank** ("MISSING"), and every timeline entry title is "Title TBD" (labels and body
    text are present).

## Left in the build

15. **Debug menu items**: ADD and SUBTRACT (±10 to every variable), CRASH (a deliberate divide-by-zero), RESET
    (wipes the DB), REMOTE (toggles remote telemetry logging).
16. **Telemetry tables** (`play_sessions`, `play_turns`, `play_variables`) and a logging layer that records every
    condition test and variable change. They look built for classroom or research analytics.

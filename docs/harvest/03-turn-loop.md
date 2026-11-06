# 03 · The turn loop (exact order of operations)

Reconstructed from `ActionHandler.HandleActionSelected`, `ActionProgress.ProgressEnded`, `AIHelper.checkAI`
and `Engine.enqueueEventResults`. `tools/harvest/simulate.py` implements the same sequence.

## Setup

1. Choose a role: **Israeli Prime Minister**, **Palestinian President**, or *Random*.
2. Choose a difficulty: **Calm**, **Tense** or **Violent** (engine default `violent`).
3. Intro video, then the welcome letter (from the PM's Director General, or the PA spokesperson), then the
   **inciting incident**. It's a news report and video: for the Israeli player a suicide bombing in West Jerusalem,
   for the Palestinian player deaths from Israeli tank fire in Gaza. It appears as a pin on the map.
4. Variables load from `init`. AI actors start asleep for `callFrequency`, plus 6 + U[0..N] turns if
   difficulty-affected (N = 3 violent, 4 tense, 8 calm). That gives the player a few quiet opening turns.

## One turn

```
 PLAYER ─ pick leaf action ──┬─ menu gated?  (shown_if / enabled_if)          → can't pick
                             ├─ needs financing? → Finance sub-menu            (Palestinian projects)
                             │      funder outcome is *immediate*; on success → project runs below
                             ├─ poll action? → run the AI actor's poll sub-tree → outcome id
                             └─ outcome table: first branch whose conditions pass
                                   │
              Immediate result? ───┤ yes → show message, NO TURN PASSES (repetition / refusals / declarations)
                                   │ no
                                   ▼
 TIME   animated days pass (clock + night overlay)
 ADVANCE #1 (player)   tagged effects due now → news queue; delayed effects tick down;
                        every auto-decrement variable −1; turn counter +1
 SHOW   first queued news event; apply its variable changes
 AI     recalc scores; walk actors in order:
          sleeping → count down, skip
          awake    → reset sleep to callFrequency; walk decision tree → outcome → apply FIRST branch
          stop after 3 actors have produced news this turn ("That's enough actions for this week!")
 ADVANCE #2 (AI)       AI news → pins on the map at the event's city; auto-decrement −1 again
 SCORE  recalculateScore(); commit
 PLOT   check milestones / win / lose (see 04)
 PINS   player must open every pin before the action menu unlocks; each pin's effects apply when opened
 SAVE   autosave once no pins remain
```

## Consequences worth noticing

* **Two clocks.** Cooldowns and delayed effects advance twice per turn (once in each ADVANCE). A `reject X +3`
  becomes 4 after the hidden bonus, so the same channel shows "repetition" for the next two turns.
* **Repetition is free.** A repeated action returns an *Immediate* message and costs no turn, so the menu
  effectively tells you what's on cooldown.
* **News drives the scores.** Most of each action's effect lands when its feedback event is shown. AI effects
  land only when the player opens the pins, which happens *after* the plot check. So an AI shock always shows up
  in the next turn's milestone check.
* **The 3-event cap ("mercy")** bounds how much the world can pile on in one turn. Actors later in the list
  (Palestinian President, Yesha in the Israeli game) get crowded out on busy turns.
* **"Weeks".** The code calls a turn a week ("enough actions for this week"), and the progress bar animates a
  number of days per action (`m_daysPerAction`, a scene setting we didn't recover). The date shown starts from
  the real current date.
* **Upkeep actors run every turn.** `IsrClock` (Israeli game) and `Clock` (Palestinian game) apply hidden
  passive changes, listed in [07](07-ai-actors.md).

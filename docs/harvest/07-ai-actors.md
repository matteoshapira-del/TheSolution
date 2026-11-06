# 07 · AI actors

Full decision trees with every branch and effect: [catalog/ai-actors.md](catalog/ai-actors.md).

The "world" in PeaceMaker is 16 scripted actors (9 in the Israeli game, 7 in the Palestinian game). Each turn they
run in a fixed order. A sleeping actor counts down and skips. A waking actor walks its tree and plays one outcome
(always the first branch of that outcome table), then sleeps for `call frequency` turns. **No more than three actors
may make news in a turn.**

## Israeli game

| # | Actor | Wakes | Difficulty-scaled | What it does |
|---|---|---|---|---|
| 1 | IsrClock | every turn | — | hidden upkeep: suppression decay and the trust → cooperation → security → public chain ([05](05-sides-stakeholders-and-meters.md)) |
| 2 | IsrMusicDJ | every turn | — | picks the music loop: negative below −30, positive above +30 on both scores, neutral otherwise |
| 3 | Palestinian Public | every 2nd turn | ✓ | rallies, street protests, aggressive protests, "too much violence", high or low quality-of-life reactions, keyed to `palestinian people` and `suppression` |
| 4 | Hamas | every turn | ✓ | P(stand down) = suppression/300. Otherwise a d100 roll gated by low `hamas` approval and low `suppression`: international terror (roll > 95), extreme attack (> 70), attack (> 40), fundraising (> 10), else words. Each move sends Hamas to sleep for 2 (words) to 6 (international terror) turns, adjusted by difficulty. An attack costs Israeli public −7, Yesha −8, security −5 |
| 5 | International Press | every 6th turn | ✓ | writes about your *lowest* meter among public approval, PA trust, Palestinian quality of life, security and sympathy (or the highest, if all are good) |
| 6 | Israeli People | every 2nd turn | ✓ | concern or praise on the lowest of public / security / suppression; petitions, protests, pro-you rallies. Has the poll sub-tree `IsrPeopleConcerns` |
| 7 | Israeli Government | every 2nd turn | ✓ | coalition concern or praise on popular approval, security, Palestinian trust, quality of life; anti-you, anti-Palestinian or pro-you statements. Poll `IPMIsrGovConcerns` |
| 8 | Palestinian President | every 2nd turn | ✓ | concerns about violence, trust or quality of life; praise; anti-militant police, political or verbal action; offers to meet. Poll `PalPresConcerns` |
| 9 | Yesha | every 2nd turn | ✓ | concern over withdrawal, praise, petitions and protests against you; illegal outposts, harassment and assaults on Palestinians |

## Palestinian game

| # | Actor | Wakes | Difficulty-scaled | What it does |
|---|---|---|---|---|
| 1 | PalMusicDJ | every turn | — | music by score mood |
| 2 | Clock | every turn | — | refills the eight budget pools and grows Israeli cooperation ([05](05-sides-stakeholders-and-meters.md)) |
| 3 | Hamas | every turn | ✓ | **high approval** (≥ ~80): partial disarmament, commits to reconstruction, joins the political process, or pro-you words. **Very low approval**: attacks *you*, anti-you words, claims victories. **Otherwise**, if `tolerance` (view of Israel) is low: extreme attack, international terror, attack, fundraising or words against Israel |
| 4 | Fatah | every turn | ✓ | same structure as Hamas: disarmament, reconstruction, anti-corruption, words; attacks on you; political manoeuvring; attacks on Israel |
| 5 | Israeli Prime Minister | every turn | ✓ | thresholds on `israeli prime minister approval`: offers construction aid, removes a security measure, apologises; or extreme security acts, security measures, blames you |
| 6 | Palestinian Public | every 2nd turn | ✓ | enthusiastic, wants action, angry, wants reconstruction or material needs or rights; shifts support to Fatah, Hamas or the president. Keyed to `independence`, `economy`, `tolerance` and approval |
| 7 | Yesha | every turn | ✓ | outposts, harassment and assaults (roll-based) |

## Design notes

* **Most AI is reactive to a single meter.** Typically one approval meter with a threshold band plus a dice roll.
  Low-rung actors (the press, publics) are diagnostic: they hold up your weakest meter.
* **Militant behaviour is approval-sensitive in the Palestinian game.** Hamas and Fatah co-opted above ~80% approval
  disarm partially and join politics. That's the closest PeaceMaker comes to modelling internal Palestinian
  consolidation, and it's a natural seed for richer endgames (unity government, civil war, spoilers).
* **Order matters under the 3-event cap.** In the Israeli game, Hamas and the Palestinian Public act before the
  Israeli publics, and Yesha comes last, so on violent turns settler reactions are often crowded out.
* **Difficulty mostly changes AI tempo, not logic** ([09](09-difficulty-and-balance.md)).

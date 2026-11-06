# PeaceMaker — full harvest (stage 1)

A complete teardown of **PeaceMaker** (ImpactGames; 2015 Unity remaster of the 2007 game), the reference point for
*The Solution*. The free official desktop build was unpacked, its rules data parsed, and its game code decompiled.
The result was then **re-run headlessly** to prove the harvest is complete and to measure balance.

## Key findings

1. **The whole game is data.** 171 variables, 300 outcome tables (675 result branches, 7,261 effects), 16 AI
   decision trees, 1,350 news events under 574 tags, 175 leaf actions. All extracted to `data/harvest/`.
2. **The winning condition is two numbers.** Each side has an internal and an external score from fixed weighted
   sums of meters. Hold both ≥ 95 for 4 turns to win. Either ≤ −50 for 4 turns loses.
   ([04](04-scoring-and-endings.md))
3. **"Two-state solution" is framing, not simulation.** The Palestinian game tracks sovereignty flags (airspace,
   water, border, holy sites, independence…), but no ending reads them. The Israeli game has no final-status state
   at all. **That's the gap The Solution's multiple endgames have to fill.**
4. **There are exactly 2 wins and 4 losses**: "Two-State Solution" / "Palestine Attains Statehood"; "Removed from
   Office", "Third Intifada", "Civil War", "International Support Pulled".
5. **Violence doesn't matter to the outcome.** An EXTREME violence verdict can accompany a win.
6. **The sides are badly unbalanced.** A naive Israeli player wins 2–5% of games, a naive Palestinian 48–97%.
   A competent player wins either side in about 21–29 turns at any difficulty. ([09](09-difficulty-and-balance.md))
7. **Difficulty only changes AI tempo** (how long actors sleep), never odds or effects.
8. **Engine quirks**: immediate-result effects are dropped (financing is "free" in approval), the water plant costs
   0, a broken `#HighestTopic`, cooldowns that tick twice a turn, and more. ([11](11-quirks-and-bugs.md))

## Chapters

| # | Chapter |
|---|---|
| 01 | [Provenance: sources, builds, what's committed vs. local](01-provenance.md) |
| 02 | [Engine architecture: data files, condition and effect language](02-engine-architecture.md) |
| 03 | [The turn loop, step by step](03-turn-loop.md) |
| 04 | [Scoring, milestones, endings, violence report](04-scoring-and-endings.md) |
| 05 | [Sides, stakeholders and meters](05-sides-stakeholders-and-meters.md) |
| 06 | [Actions and outcomes (+ score-impact ranking)](06-actions-and-outcomes.md) |
| 07 | [AI actors](07-ai-actors.md) |
| 08 | [Events, news and media](08-events-news-and-media.md) |
| 09 | [Difficulty and balance (simulated)](09-difficulty-and-balance.md) |
| 10 | [UI, UX and presentation](10-ui-ux-and-presentation.md) |
| 11 | [Quirks, bugs and inconsistencies](11-quirks-and-bugs.md) |
| 12 | [Public record: history, research, reception](12-public-record.md) |
| 13 | [Implications for The Solution](13-implications-for-the-solution.md) |

Generated catalogs (every action, branch, AI tree, variable and event tag):
[actions — Israeli](catalog/actions-israeli.md) · [actions — Palestinian](catalog/actions-palestinian.md) ·
[AI actors](catalog/ai-actors.md) · [variables](catalog/variables.md) · [events](catalog/events.md)

## Reproduce

```bash
sudo apt-get install -y libarchive-tools     # bsdtar
pip install UnityPy
tools/harvest/fetch.sh                        # downloads the official free macOS build → harvest_raw/ (git-ignored)
python3 tools/harvest/extract.py              # → data/harvest/*.json  (+ verbatim text in harvest_raw/)
python3 tools/harvest/render_docs.py          # → docs/harvest/catalog/*.md
python3 tools/harvest/simulate.py --role palestinian --difficulty tense --policy greedy --games 100
```

To also read the game code, decompile `harvest_raw/app/PeaceMaker.app/Contents/Resources/Data/Managed/Assembly-CSharp.dll`
with ILSpy (`dotnet tool install -g ilspycmd --version 8.2.0.7535`).

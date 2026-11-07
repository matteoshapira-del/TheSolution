# The Solution

An upgraded, original successor to the *PeaceMaker* style of political simulation game about the
Israeli–Palestinian conflict. Its defining feature is **multiple endgames** across the full range of proposed
solutions, rather than a single two-state win.

## Status

**Stage 1: harvest the reference game.** Done. See [`docs/harvest/`](docs/harvest/README.md).

| Path | What |
|---|---|
| `docs/harvest/` | Teardown of PeaceMaker: engine, rules, scoring, AI, events, balance, quirks, public record, design implications |
| `docs/guide/peacemaker-decoded.html` | Interactive guide to the game's stages and rules (built by `tools/harvest/build_guide.py`) |
| `docs/harvest/catalog/` | Generated catalogs of every action, outcome branch, AI decision tree, variable and event tag |
| `data/harvest/` | The game's mechanics as structured JSON (no copyrighted prose or media) |
| `tools/harvest/` | `fetch.sh` (download and unpack the official free build), `extract.py` (parse to JSON), `render_docs.py`, `simulate.py` (headless engine) |
| `reports/Israeli Palestinian conflict solutions spectrum.pdf` | Research report: every major proposed solution, ordered from one extreme to the other, with legality, support, feasibility and endgame-design inputs (Markdown source alongside) |
| `reports/Short video persuasion experiment design.pdf` | Research report: per-participant KPIs, lawful collection and coding of short-form video, the mock feed app, and ethics for an opinion-change study (Markdown source alongside) |
| `prototypes/feed-lab/exposure-feed-lab.html` | Exposure Feed Lab: clickable prototype of the short-video exposure experiment |
| `research_notes/` | The sourced research dossiers behind both reports |
| `tools/research/` | `build_pdf.py` (Markdown → designed PDF) and `spectrum.json` (the spectrum figure) |

Verbatim game text and media are **not** committed. `tools/harvest/fetch.sh && python3 tools/harvest/extract.py`
recreates them locally in the git-ignored `harvest_raw/`.

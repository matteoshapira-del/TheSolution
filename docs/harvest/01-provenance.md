# 01 · Provenance: what was harvested, from where

## Sources

| Source | What it gave us | Notes |
|---|---|---|
| `peacemakergame.com` (live, Nov 2026) | Store links, the two free desktop downloads, trailer link, ticker headlines | The site has been **compromised with SEO spam**: the home page carries dozens of hidden casino/betting links, and `about.php`, `reviews.php`, `getpeacemaker.php` now return an empty template. Don't treat the live site as a reliable source. |
| macOS build — `PeaceMaker_Israeli_Palestinian_Conflict_Download.pkg` (Dropbox link on the official site, 208,799,332 bytes) | **Everything below**: rules XML, content DB, decompiled game code, media inventory | xar package, then a gzip/cpio payload holding `PeaceMaker.app` (Unity). `build_info.txt`: *"Build from Tim's MacBook Pro at 11/17/2015 17:22:58"* |
| Windows build — `PeaceMaker-_Israeli_Palestinian_Conflict_Download.exe` (180,562,752 bytes) | Cross-check | Inno Setup 5.5.6 installer, `build_info.txt`: *"Build from BEAST at 11/16/2015"*. Its `peacemaker.db` is byte-identical to the Mac one, and every rules XML matches after CRLF→LF normalisation. Only the compiled DLL differs (per-platform build). |
| Public record (press, research papers, store listings, Wayback archives) | History, team, reception, educational research | See [12-public-record.md](12-public-record.md). |

Not harvested: the iOS/Android builds (store-gated) and the original 2007 release. The 2015 desktop build is the
remastered edition that also shipped on mobile, and it plays the same rules on every platform.

## Technology

* **Unity 5.2.2f1** (Mono scripting). UI is built with **NGUI**; localisation uses **I2 Localization** plus per-language XML/DB tables.
* Game logic lives in `Assembly-CSharp.dll` (decompiled with ILSpy 8.2, 368 C# files). The parts that matter
  are `Engine.cs`, `AIHelper.cs`, `EventsHelper.cs`, `ActionHelper.cs`, `ActionHandler.cs`, `ActionProgress.cs`
  and `EndReportWindow.cs`.
* **Rules are data-driven.** Nearly every game decision is an XML table shipped as a Unity `TextAsset`, and the
  content sits in a SQLite DB (`StreamingAssets/peacemaker.db`, made by the in-game `ConvertXmlToSqlite` tool).
* Languages: **English, Hebrew, Arabic**, with full RTL support (`ArabicSupport.dll`, `RTL3DText`). All 1,350 events and 235 actions are translated.

## Where each part of the game lives

| File (inside the build) | Size | Holds |
|---|---|---|
| `sharedassets2.assets` › `init` | 17 KB | Every simulation variable, its starting value and flags, per role (171 variables) |
| `sharedassets2.assets` › `outcomes` | 1.2 MB | **The rules**: 320 outcome tables (300 unique ids), 698 result branches, 7,261 variable effects |
| `sharedassets2.assets` › `actions-to-outcomes` | 18 KB | Maps 178 player action ids to outcome tables |
| `sharedassets2.assets` › `ai2` | 83 KB | Decision trees for 16 non-player actors |
| `sharedassets2.assets` › `data.en-us` | 120 KB | Action menus: headers, prompts, hawk/dove advisor lines |
| `sharedassets2.assets` › `events.en-us` | 810 KB | All 1,350 news/feedback events (mirrored in the DB) |
| `sharedassets2.assets` › `interface.{en-us,he,ar}` | 60–87 KB each | Stakeholders, polls, 27 map locations, 15 timeline eras, tutorial, UI strings |
| `StreamingAssets/peacemaker.db` | 3.5 MB | `actions`, `events`, localized `*_text_{enus,he,ar}`, `variables`, prereqs, plot thresholds, save games, **play telemetry tables** |
| `StreamingAssets/EventImages` | 1,096 JPGs | News photos (Reuters-style ids such as `RTRNU7F.jpg`) |
| `StreamingAssets/ActionImages` | 249 | Action menu art |
| `StreamingAssets/Videos` | 18 OGV | Per side: intro, inciting incident, three milestones, win, two losses; plus studio slate and trailer |
| `StreamingAssets/TimelineImages` / `TutorialImages` / `Other` | 15 / 8 / 75 | History timeline, tutorial, stakeholder portraits and map location art |
| `resources.assets`, `sharedassets1.assets` | — | 92 audio clips (music loops by mood, crowd/siren/news stingers), fonts, shaders |

## What is committed vs. kept local

ImpactGames (and its photo/video licensors) own PeaceMaker's writing, art, footage and audio. This repository commits
**only the mechanics**, restructured as data, plus our own analysis:

* `data/harvest/*.json`: variables, action tree, outcome tables (conditions and numbers), AI decision trees,
  event *index* (ids, tags, locations, sound cues; no prose), milestones/endings, interface structure, engine constants.
* `docs/harvest/`: this analysis, plus generated catalogs.

Running `tools/harvest/fetch.sh` and then `tools/harvest/extract.py` rebuilds everything from the official free
download, and also writes the **verbatim** material (rules XML, all event/action text in three languages as CSV,
the SQLite DB) to `harvest_raw/`, which is git-ignored. Use it as a private reference while designing. Don't ship
it, and don't paste it into The Solution.

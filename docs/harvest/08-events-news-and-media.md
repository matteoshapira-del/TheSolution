# 08 · Events, news and media

Full tag list and statistics: [catalog/events.md](catalog/events.md).

## The news system

* **1,350 events** under **574 tags**. An outcome names a tag, and the engine picks one event with that tag at
  random. Popular tags have up to 11 variants (Hamas/Fatah attacks, Israeli security measures, settler assaults),
  so repeated situations read differently.
* Every event has a **title line** (sender, e.g. a memo from the Director General or a news agency), a
  **headline**, **body text**, a **photo** (1,096 news photos with Reuters-style file ids), a **sound cue** and a
  **map location**.
* **Box types:** `Normal` (1,206) for regular feedback and news, `Black` (118) for grave news such as attacks,
  `plot` (6) for milestone letters, `ending` (6) for endings. Map pins are **red** for `Red-Event` (and untyped AI
  events) and **white** for `White-Event`.
* **Sound cues** set the emotional register: News, Failure, Success, Suboptimal, Protest, Siren, Cash, Build,
  Meeting, Applause, AngryMob, Whisper, Cheer, Murmur and so on.
* **Locations** (27 map spots): Ramallah 116, Gaza 110, Jerusalem 105+5, Tel Aviv 36+2, Nablus 32, Hebron 26,
  Israeli settlements 1–4 (39), Jenin 16, Haifa 8, Tulkarm 7, Rafah 5, East Jerusalem 5, Bethlehem 5, Sderot,
  Netanya, Afula, Qalqilya, Kfar Saba, Jericho, Hadera, Beersheba. 814 events have no location, which means they
  are player-feedback dialogs rather than pins. The map also marks the Green Line and the security fence.

## Tag grammar

Tags are comma-separated, from general to specific: `<actor or menu>, <sub-menu>, <choice>, <feedback|immediate>, <result>`.
For example `israel order idf, send idf, arrest militants, feedback, success`, or `hamas, anti-israel, extreme attack`.
That's an ontology you could reuse for content: **who · what · how it went**.

## Narrative frame

* **Welcome letter**, per side.
* **Inciting incident**: a black-box news report with a video. Israeli: a suicide bombing in West Jerusalem.
  Palestinian: deaths from Israeli tank fire in Gaza.
* **Three milestone letters** with videos, then a **win** or **loss** video. Eight videos per side, plus a studio
  slate and the trailer.
* **History timeline**: 15 eras with photos (1920–1948, 1948, 1950s, 1967, 1968, 1968–1980, 1982, 1987, 1990s,
  1993, 1994, 2000, 2005, 2006, today).
* **Tutorial**: 12 steps (welcome, map, events, groups and leaders, polls, score, actions, advisors, turn; 3 are
  blank in the shipped data).
* **Advisors.** Every action menu has two opposing voices. In the Israeli game they're "The Hawk" and "The Dove".
  In the Palestinian game, "Your National Advisor" and "Your Foreign Advisor". Each gives a one-paragraph argument
  for and against.

## Languages

Everything is in English, Hebrew and Arabic: event and action text in the DB (`*_text_enus`, `*_he`, `*_ar`),
interface XML per language, and RTL rendering. Players can switch language from the menu.

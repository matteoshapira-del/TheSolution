# Variable catalog

Generated from `data/harvest/variables.json`. Values are clamped to 0..100 unless flagged.
`auto-dec` variables lose 1 point every time the engine advances effects (twice per turn) —
they are cooldown and violence counters. Counts show how many player-action outcome tables
and AI outcome tables move each variable (up / down).

## palestinian

| variable | default | flags | shown in UI as | player ↑/↓ | AI ↑/↓ |
|---|---|---|---|---|---|
| `project` | 0 | — | — | 0/0 | 0/0 |
| `project cost` | 0 | — | — | 0/0 | 0/0 |
| `palestinian public approval` | 30 | — | Group/leader meter: Palestinian Public | 80/90 | 8/12 |
| `fatah approval` | 70 | — | Group/leader meter: Fatah | 67/91 | 5/8 |
| `hamas approval` | 20 | — | Group/leader meter: Hamas | 66/94 | 5/9 |
| `israeli prime minister approval` | 30 | — | Group/leader meter: Israeli Prime Minister | 117/28 | 3/9 |
| `israeli public approval` | 20 | — | Group/leader meter: Israeli Public | 82/43 | 3/10 |
| `usa approval` | 20 | — | Group/leader meter: United States | 90/30 | 2/10 |
| `un approval` | 50 | — | Group/leader meter: United Nations | 107/26 | 4/10 |
| `arab world approval` | 50 | — | Group/leader meter: The Arab World | 84/44 | 2/10 |
| `internal authority score` | 0 | can be negative | — | 0/0 | 0/0 |
| `external authority score` | 0 | can be negative | — | 0/0 | 0/0 |
| `economy` | 5 | — | Poll: Palestinian Economy | 52/8 | 4/3 |
| `leadership` | 5 | — | Poll: Palestinian President'S Leadership | 77/68 | 5/7 |
| `government authority` | 10 | — | Poll: Palestinian Government Authority | 88/58 | 5/9 |
| `independence` | 5 | — | Poll: Palestinian Independence | 42/20 | 2/6 |
| `israeli cooperation` | 5 | — | Poll: Israeli Cooperation | 94/40 | 5/9 |
| `tolerance` | 5 | — | Poll: Palestinian View Of Israel | 49/23 | 4/7 |
| `usa budget` | 20 | — | — | 0/2 | 0/0 |
| `un budget` | 20 | — | — | 0/2 | 0/0 |
| `eu budget` | 20 | — | — | 0/0 | 0/0 |
| `egypt budget` | 5 | — | — | 0/2 | 0/0 |
| `jordan budget` | 5 | — | — | 0/2 | 0/0 |
| `israel budget` | 10 | — | — | 0/0 | 0/0 |
| `other groups budget` | 0 | — | — | 0/0 | 0/0 |
| `police units out` | 0 | — | — | 4/4 | 0/0 |
| `police units total` | 2 | — | — | 1/1 | 0/0 |
| `airports` | 0 | — | — | 1/0 | 0/0 |
| `seaports` | 0 | — | — | 1/0 | 0/0 |
| `budget` | 10 | — | — | 8/0 | 1/0 |
| `independent state` | 0 | — | — | 1/0 | 0/0 |
| `joint patrols` | 0 | — | — | 1/1 | 0/0 |
| `joint training` | 0 | — | — | 1/1 | 0/0 |
| `gaza border open` | 1 | — | — | 1/1 | 0/0 |
| `gaza border presence` | 0 | — | — | 1/1 | 0/0 |
| `gaza border international troops` | 0 | — | — | 1/1 | 0/0 |
| `control internal travel` | 0 | — | — | 1/0 | 0/0 |
| `control gaza border` | 0 | — | — | 1/0 | 0/0 |
| `control holy sites` | 0 | — | — | 1/0 | 0/0 |
| `holy sites palestinian access` | 0 | — | — | 1/3 | 0/0 |
| `holy sites israeli access` | 1 | — | — | 2/1 | 0/0 |
| `holy sites foreigner access` | 0 | — | — | 2/1 | 0/0 |
| `control seaspace` | 0 | — | — | 1/0 | 0/0 |
| `control airspace` | 0 | — | — | 1/0 | 0/0 |
| `control water` | 0 | — | — | 1/0 | 0/0 |
| `control education` | 0 | — | — | 1/0 | 0/0 |
| `curriculum restructured` | 0 | — | — | 1/1 | 0/0 |
| `tourism open` | 0 | — | — | 2/1 | 0/0 |
| `POLICE TRAIN` | 20 | — | — | 0/0 | 0/0 |
| `POLICE INCREASE FUNDING` | 20 | — | — | 0/0 | 0/0 |
| `FATAH BRIBE` | 20 | — | — | 0/0 | 0/0 |
| `HOUSING` | 30 | — | — | 0/0 | 0/0 |
| `AGRICULTURE` | 30 | — | — | 0/0 | 0/0 |
| `INDUSTRY` | 30 | — | — | 0/0 | 0/0 |
| `RECLAIM SETTLEMENTS` | 20 | — | — | 0/0 | 0/0 |
| `ROADS` | 10 | — | — | 0/0 | 0/0 |
| `AIRPORT` | 60 | — | — | 0/0 | 0/0 |
| `SEAPORT` | 50 | — | — | 0/0 | 0/0 |
| `INFRASTRUCTURE` | 10 | — | — | 0/0 | 0/0 |
| `COMMUNICATIONS` | 20 | — | — | 0/0 | 0/0 |
| `WATER TREATMENT PLANT` | 30 | — | — | 0/0 | 0/0 |
| `POWER PLANT` | 40 | — | — | 0/0 | 0/0 |
| `HEALTH CARE` | 30 | — | — | 0/0 | 0/0 |
| `CARE FOR THE POOR` | 30 | — | — | 0/0 | 0/0 |
| `EDUCATION REOPEN CLOSED SCHOOLS` | 10 | — | — | 0/0 | 0/0 |
| `EDUCATION BUILD NEW SCHOOLS` | 30 | — | — | 0/0 | 0/0 |
| `POLICE STATION` | 30 | — | — | 0/0 | 0/0 |
| `PRISON` | 30 | — | — | 0/0 | 0/0 |
| `IMPORT ARMS` | 30 | — | — | 0/0 | 0/0 |
| `reject push control` | 0 | auto-dec | — | 21/0 | 0/0 |
| `reject egypt` | 0 | auto-dec | — | 12/0 | 0/0 |
| `reject fatah` | 0 | auto-dec | — | 9/0 | 0/0 |
| `reject arab states` | 0 | auto-dec | — | 3/0 | 0/0 |
| `reject eu` | 0 | auto-dec | — | 3/0 | 0/0 |
| `reject israel` | 0 | auto-dec | — | 14/0 | 0/0 |
| `reject other palestinian` | 0 | auto-dec | — | 3/0 | 0/0 |
| `reject un` | 0 | auto-dec | — | 15/0 | 0/0 |
| `reject usa` | 0 | auto-dec | — | 15/0 | 0/0 |
| `reject gaza border` | 0 | auto-dec | — | 9/0 | 0/0 |
| `reject hamas` | 0 | auto-dec | — | 14/0 | 0/0 |
| `reject internal travel` | 0 | auto-dec | — | 2/0 | 0/0 |
| `reject refugee affairs` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject assassination` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject settlements` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject security wall` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject bulldoze` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject reconstruction aid` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject checkpoints` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject trade restrictions` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject worker permits` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject education aid` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject government` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject idf` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject curfew` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject medical aid` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject missile strike` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject palestinian president` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject speech to israelis` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject police` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject speech to world` | 0 | auto-dec | — | 3/0 | 0/0 |
| `reject prisoners` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject jordan` | 0 | auto-dec | — | 12/0 | 0/0 |
| `reject extreme measures` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject police manage` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject speech to palestinians` | 0 | auto-dec | — | 5/0 | 0/0 |
| `negative effects` | 0 | auto-dec | — | 0/0 | 0/0 |
| `turns` | 0 | — | — | 0/0 | 0/0 |
| `endreport` | 0 | can exceed 100 | — | 57/0 | 21/0 |
| `aggression` | 0 | auto-dec | — | 0/0 | 0/0 |

## israeli

| variable | default | flags | shown in UI as | player ↑/↓ | AI ↑/↓ |
|---|---|---|---|---|---|
| `israel people` | 55 | — | Group/leader meter: Israeli Public | 71/91 | 10/13 |
| `yesha` | 40 | — | Group/leader meter: Yesha (Israeli Settlers' Council) | 72/93 | 10/10 |
| `palestinian president` | 25 | — | Group/leader meter: Palestinian Authority President | 79/83 | 4/11 |
| `palestinian people` | 20 | — | Group/leader meter: Palestinian Public | 76/86 | 6/7 |
| `hamas` | 7 | — | Group/leader meter: Militant Groups | 0/0 | 4/2 |
| `usa` | 40 | — | Group/leader meter: Usa | 111/45 | 10/11 |
| `un` | 20 | — | Group/leader meter: United Nations | 93/67 | 10/13 |
| `arab world` | 15 | — | Group/leader meter: The Arab World | 86/60 | 10/13 |
| `security` | 30 | — | Poll: Israeli Security | 59/29 | 7/7 |
| `sympathy` | 10 | — | Poll: Israeli Sympathy | 64/3 | 9/1 |
| `suppression` | 25 | — | Poll: Militant Activity Supression | 48/34 | 1/5 |
| `palestinian cooperation` | 10 | — | Poll: Palestinian Cooperation | 76/58 | 5/11 |
| `leadership` | 25 | — | Poll: Israeli Leadership | 0/0 | 0/0 |
| `internal authority score` | 0 | can be negative | — | 0/0 | 0/0 |
| `external authority score` | 0 | can be negative | — | 0/0 | 0/0 |
| `internal speech timer` | 0 | — | — | 0/0 | 0/0 |
| `external speech timer` | 0 | — | — | 0/0 | 0/0 |
| `internal win count` | 5 | — | — | 0/0 | 0/0 |
| `external win count` | 5 | — | — | 0/0 | 0/0 |
| `reject push control` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject egypt` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject fatah` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject arab states` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject eu` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject israel` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject other palestinian` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject un` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject usa` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject gaza border` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject hamas` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject internal travel` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject refugee affairs` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject assassination` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject settlements` | 0 | auto-dec | — | 10/0 | 0/0 |
| `reject security wall` | 0 | auto-dec | — | 9/0 | 0/0 |
| `reject bulldoze` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject reconstruction aid` | 0 | auto-dec | — | 9/0 | 0/0 |
| `reject checkpoints` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject trade restrictions` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject worker permits` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject education aid` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject government` | 0 | auto-dec | — | 11/0 | 0/0 |
| `reject idf` | 0 | auto-dec | — | 8/0 | 0/0 |
| `reject curfew` | 0 | auto-dec | — | 4/0 | 0/0 |
| `reject medical aid` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject missile strike` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject palestinian president` | 0 | auto-dec | — | 10/0 | 0/0 |
| `reject speech to israelis` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject police` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject speech to world` | 0 | auto-dec | — | 5/0 | 0/0 |
| `reject prisoners` | 0 | auto-dec | — | 6/0 | 0/0 |
| `reject jordan` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject extreme measures` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject police manage` | 0 | auto-dec | — | 0/0 | 0/0 |
| `reject speech to palestinians` | 0 | auto-dec | — | 0/0 | 0/0 |
| `negative effects` | 0 | auto-dec | — | 0/0 | 0/0 |
| `turns` | 0 | — | — | 0/0 | 0/0 |
| `endreport` | 0 | can exceed 100 | — | 87/0 | 16/0 |
| `aggression` | 0 | auto-dec | — | 32/0 | 0/0 |
| `reject yesha` | 0 | auto-dec | — | 11/0 | 0/0 |
| `reject cultural` | 0 | auto-dec | — | 12/0 | 0/0 |
| `reject domestic` | 0 | auto-dec | — | 6/0 | 0/0 |


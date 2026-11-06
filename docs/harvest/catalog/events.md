# Event catalog (structure only)

Generated from `data/harvest/events_index.json` and `event_tags.json`. The game holds
**1350 events** under **574 tags**. Whenever an outcome fires a tag, one
variant with that tag is picked uniformly at random, so tags with many variants feel less
repetitive. Prose is not reproduced here — run the harvester locally to read it.

## Tag families (first tag token = who/what the event is about)

| family | distinct tags | event variants |
|---|---|---|
| palestinian public | 15 | 68 |
| palestinian president | 13 | 66 |
| hamas | 12 | 50 |
| feedback | 31 | 49 |
| israeli public | 12 | 48 |
| yesha | 9 | 47 |
| fatah | 11 | 46 |
| financing | 25 | 44 |
| israel pm | 6 | 40 |
| israel talk to world leaders | 21 | 39 |
| israeli government | 13 | 39 |
| israel order idf | 9 | 38 |
| israel manage settlements | 13 | 35 |
| hamas-fatah | 5 | 34 |
| international press | 10 | 30 |
| hamas negotiation | 15 | 29 |
| israel talk to palestinian president | 12 | 27 |
| gaza border control | 15 | 26 |
| israel cultural initiatives | 13 | 26 |
| egypt negotiate | 13 | 25 |
| jordan negotiate | 13 | 25 |
| un negotiate | 13 | 25 |
| usa negotiate | 13 | 25 |
| israel talk to your government | 12 | 24 |
| israel negotiation | 12 | 23 |
| israel yesha | 12 | 23 |
| fatah negotiation | 11 | 21 |
| israel reconstruction aid | 10 | 20 |
| israel manage security wall | 10 | 19 |
| transportation construction | 9 | 19 |
| extreme measures | 11 | 17 |
| israel order police | 7 | 16 |
| holy sites | 12 | 14 |
| israel talk to the world | 8 | 14 |
| natural resource construction | 7 | 14 |
| israel domesitic initiatives | 7 | 13 |
| israel education aid | 7 | 13 |
| israel medical aid | 7 | 13 |
| israel missile strike | 7 | 13 |
| israel refugee affairs | 7 | 13 |
| israel release prisoners | 7 | 13 |
| israel talk to your people | 7 | 13 |
| police manage | 7 | 13 |
| internal travel | 6 | 11 |
| israel assassinate militant leader | 5 | 11 |
| israel worker permits | 6 | 11 |
| education | 5 | 10 |
| israel trade restrictions | 6 | 10 |
| police presence | 5 | 10 |
| call for independent state | 5 | 9 |
| israel bulldoze area | 5 | 9 |
| israel curfews | 5 | 9 |
| israel manage checkpoints | 5 | 9 |
| civilian construction | 4 | 8 |
| governmental construction | 3 | 6 |
| social services construction | 2 | 4 |
| speech to palestinians | 3 | 4 |
| speech to world | 4 | 4 |
| ending | 3 | 3 |
| israeli ending | 3 | 3 |
| gaza border | 1 | 1 |
| immediate | 1 | 1 |
| israeli forces cooperation | 1 | 1 |
| israeli plot 1 | 1 | 1 |
| israeli plot 2 | 1 | 1 |
| israeli plot 3 | 1 | 1 |
| plot 1 | 1 | 1 |
| plot 2 | 1 | 1 |
| plot 3 | 1 | 1 |
| push control | 1 | 1 |

## Presentation

Box types: Normal 1206, Black 118, (none) 14, plot 6, ending 6

Map locations: (none) 814, RAMALLAH 116, GAZA 110, JERUSALEM 105, TEL-AVIV 36, NABLUS 32, HEBRON 26, JENIN 16, ISRAEL_SETTLEMENT 2 15, ISRAEL_SETTLEMENT 1 11, ISRAEL_SETTLEMENT 3 9, HAIFA 8, TULKARM 7, RAFAH 5, Jerusalem 5, BETHLEHEM 5, EAST JERUSALEM 5, ISRAEL_SETTLEMENT 4 4, SDEROT 4, NETANYA 4, AFULA 4, QALQILYE 2, Tel-Aviv 2, KFAR SAVA 2, JERICHO 1, HADERA 1, BEERSHEVA 1

Sound cues: News 142, Failure 111, Success 97, Suboptimal 93, Protest 82, News2 51, Murmur2 47, Repetative 47, Cash 46, Siren 41, Meeting 38, Build 34, Murmur 32, Applause 31, AngryMob2 31, Whisper 27, Whisper2 27, Cheer2 26, AngryMob 25, Cheer 23, GunAttack2 20, Bulldoze 18, GunAttack3 18, GunAttack 17, Cheer3 16, Helicopter 14, SuicideBomb 14, MortarAttack 13, MissileAttack 11, GunAttack4 10, Type 10, TrafficJam 10, AngryMen 10, whispering 9, Demolition2 9, protest 8, School 7, Applause4 7, TelephoneRing1 7, Aggressive 7, Mourn 6, Airplane 6, ChurchBells 6, Siren2 5, applause 5, Applause2 4, Type2 4, Applause3 4, PowerPlant 4, crying 3, Fanfare 3, Seaport2 3, Demolition 2, grumbling 2, typing_short 2, Camera 2, (none) 1, angry_men 1, TelephoneDial 1

## Milestones and endings

| role | id | mode | needs | held for | title |
|---|---|---|---|---|---|
| israeli | `ISRAELI: PLOT 1` | milestone | internal authority score ≥ 30 and external authority score ≥ 30 | 2 consecutive checks | Gaza Approaches Independence |
| israeli | `ISRAELI: PLOT 2` | milestone | internal authority score ≥ 50 and external authority score ≥ 50 | 2 consecutive checks | Train Travels between Gaza and the West Bank |
| israeli | `ISRAELI: PLOT 3` | milestone | internal authority score ≥ 70 and external authority score ≥ 70 | 2 consecutive checks | Winds of Peace |
| israeli | `ISRAELI: WIN` | win | internal authority score ≥ 95 and external authority score ≥ 95 | 4 consecutive checks | You Win: Two-State Solution |
| israeli | `ISRAELI: ISRAELI LOSE` | lose | internal authority score ≤ -50 | 4 consecutive checks | You Lose: You Have Been Removed from Office |
| israeli | `ISRAELI: ISRAELI LOSE 2` | lose | external authority score ≤ -50 | 4 consecutive checks | You Lose: The Third Intifada |
| palestinian | `PLOT 1` | milestone | internal authority score ≥ 30 and external authority score ≥ 30 | 2 consecutive checks | Gaza Approaches Independence |
| palestinian | `PLOT 2` | milestone | internal authority score ≥ 50 and external authority score ≥ 50 | 2 consecutive checks | Train Route between Gaza and West Bank |
| palestinian | `PLOT 3` | milestone | internal authority score ≥ 70 and external authority score ≥ 70 | 2 consecutive checks | West Bank Approaches Independence |
| palestinian | `ENDING: WIN` | win | internal authority score ≥ 95 and external authority score ≥ 95 | 4 consecutive checks | You Win: Palestine Attains Statehood |
| palestinian | `ENDING: INTERNAL LOSE` | lose | internal authority score ≤ -50 | 4 consecutive checks | You Lose: A Civil War Breaks Out |
| palestinian | `ENDING: EXTERNAL LOSE` | lose | external authority score ≤ -50 | 4 consecutive checks | You Lose: International Support Pulled |

## All tags

| tag | variants | box types | locations |
|---|---|---|---|
| `call for independent state, feedback, close` | 2 | Normal | — |
| `call for independent state, feedback, crazy` | 2 | Normal | — |
| `call for independent state, feedback, polite refusal` | 2 | Normal | — |
| `call for independent state, feedback, strong refusal` | 2 | Normal | — |
| `call for independent state, feedback, success` | 1 | Normal | — |
| `civilian construction, agriculture, feedback, success` | 2 | Normal | — |
| `civilian construction, housing, feedback, success` | 2 | Normal | — |
| `civilian construction, industry, feedback, success` | 2 | Normal | — |
| `civilian construction, reclaim settlements, feedback, success` | 2 | Normal | — |
| `education, build new schools, feedback, success` | 2 | Normal | — |
| `education, push control, feedback, delay` | 2 | Normal | — |
| `education, push control, feedback, refusal` | 2 | Normal | — |
| `education, push control, feedback, success` | 2 | Normal | — |
| `education, reopen closed schools, feedback, success` | 2 | Normal | — |
| `egypt negotiate, immediate, repetition` | 1 | Normal | RAMALLAH |
| `egypt negotiate, request aid, feedback, delay` | 2 | Normal | — |
| `egypt negotiate, request aid, feedback, refusal` | 2 | Normal | — |
| `egypt negotiate, request aid, feedback, success` | 2 | Normal | — |
| `egypt negotiate, request investment, feedback, delay` | 2 | Normal | — |
| `egypt negotiate, request investment, feedback, refusal` | 2 | Normal | — |
| `egypt negotiate, request investment, feedback, success` | 2 | Normal | — |
| `egypt negotiate, request meeting, feedback, delay` | 2 | Normal | — |
| `egypt negotiate, request meeting, feedback, refusal` | 2 | Normal | — |
| `egypt negotiate, request meeting, feedback, success` | 2 | Normal | — |
| `egypt negotiate, request political pressure, feedback, delay` | 2 | Normal | — |
| `egypt negotiate, request political pressure, feedback, refusal` | 2 | Normal | — |
| `egypt negotiate, request political pressure, feedback, success` | 2 | Normal | — |
| `ending, external lose` | 1 | ending | RAMALLAH |
| `ending, internal lose` | 1 | ending | GAZA |
| `ending, win` | 1 | ending | RAMALLAH |
| `extreme measures, arrest known militants, feedback, failure` | 2 | Normal | — |
| `extreme measures, arrest known militants, feedback, sub-optimal` | 2 | Normal | — |
| `extreme measures, arrest known militants, feedback, success` | 2 | Normal | — |
| `extreme measures, assassinate militant leader, feedback, failure` | 2 | Normal | — |
| `extreme measures, assassinate militant leader, feedback, sub-optimal` | 2 | Black, Normal | — |
| `extreme measures, assassinate militant leader, feedback, success` | 2 | Black | — |
| `extreme measures, immediate, repetition` | 1 | Normal | RAMALLAH |
| `extreme measures, seize militant arm, feedback, failure` | 1 | Normal | — |
| `extreme measures, seize militant arms, feedback, failure` | 1 | Normal | — |
| `extreme measures, seize militant arms, feedback, sub-optimal` | 1 | Normal | — |
| `extreme measures, seize militant arms, feedback, success` | 1 | Normal | — |
| `fatah negotiation, ask for anti-corruption, feedback, delay` | 2 | Normal | — |
| `fatah negotiation, ask for anti-corruption, feedback, refusal` | 2 | Normal | — |
| `fatah negotiation, ask for anti-corruption, feedback, success` | 2 | Normal | — |
| `fatah negotiation, ask for law and order, feedback, delay` | 2 | Normal | — |
| `fatah negotiation, ask for law and order, feedback, refusal` | 2 | Normal | — |
| `fatah negotiation, ask for law and order, feedback, success` | 2 | Normal | — |
| `fatah negotiation, ask for peace support, feedback, delay` | 2 | Normal | — |
| `fatah negotiation, ask for peace support, feedback, refusal` | 2 | Normal | — |
| `fatah negotiation, ask for peace support, feedback, success` | 2 | Normal | — |
| `fatah negotiation, bribe, feedback, success` | 2 | Normal | — |
| `fatah negotiation, immediate, repetition` | 1 | Normal | RAMALLAH |
| `fatah, anti-israel, attack` | 5 | Black, Normal | RAMALLAH, GAZA, ISRAEL_SETTLEMENT 4, NABLUS, JENIN |
| `fatah, anti-israel, extreme attack` | 5 | Black | ISRAEL_SETTLEMENT 3, ISRAEL_SETTLEMENT 1, JERUSALEM, TEL-AVIV, KFAR SAVA |
| `fatah, anti-israel, funds` | 3 | Normal | RAMALLAH, GAZA |
| `fatah, anti-israel, words` | 5 | Normal | GAZA, JENIN, NABLUS |
| `fatah, anti-you, attack on your organization` | 5 | Normal, Black | RAMALLAH, GAZA |
| `fatah, anti-you, political maneuvering` | 3 | Normal | RAMALLAH |
| `fatah, anti-you, words` | 5 | Normal | RAMALLAH, GAZA, NABLUS |
| `fatah, pro-you, anti-corruption measure` | 4 | Normal | RAMALLAH, GAZA |
| `fatah, pro-you, commit to reconstruction` | 3 | Normal | RAMALLAH |
| `fatah, pro-you, partial disarmament of military wing` | 3 | Normal | HEBRON, RAMALLAH, GAZA |
| `fatah, pro-you, words` | 5 | Normal | RAMALLAH, GAZA |
| `feedback, aggression` | 5 | Normal | — |
| `feedback, education, restructure curriculum, failure` | 2 | Normal | — |
| `feedback, education, restructure curriculum, success` | 2 | Normal | — |
| `feedback, education, revert curriculum, success` | 2 | Normal | — |
| `feedback, holy sites, permit access foreigners, sub-optimal` | 1 | Normal | — |
| `feedback, holy sites, permit access foreigners, success` | 1 | Normal | — |
| `feedback, holy sites, permit access israelis, sub-optimal` | 1 | Normal | — |
| `feedback, holy sites, permit access israelis, success` | 1 | Normal | — |
| `feedback, holy sites, permit access palestinians, success` | 1 | Normal | — |
| `feedback, holy sites, restrict access foreigners, success` | 1 | Normal | — |
| `feedback, holy sites, restrict access israelis, success` | 1 | Normal | — |
| `feedback, holy sites, restrict access palestinians, sub-optimal` | 1 | Normal | — |
| `feedback, holy sites, restrict access palestinians, success` | 1 | Normal | — |
| `feedback, israeli forces cooperation, joint patrols start, delay` | 2 | Normal | — |
| `feedback, israeli forces cooperation, joint patrols start, refusal` | 1 | Normal | — |
| `feedback, israeli forces cooperation, joint patrols start, success` | 2 | Normal | — |
| `feedback, israeli forces cooperation, joint patrols stop, success` | 2 | Normal | — |
| `feedback, israeli forces cooperation, joint training start, delay` | 1 | Normal | — |
| `feedback, israeli forces cooperation, joint training start, refusal` | 1 | Normal | — |
| `feedback, israeli forces cooperation, joint training start, success` | 1 | Normal | — |
| `feedback, israeli forces cooperation, joint training stop, success` | 1 | Normal | — |
| `feedback, speech to palestinians, anti-militancy, received poorly` | 2 | Normal | — |
| `feedback, speech to palestinians, anti-militancy, received well` | 2 | Normal | — |
| `feedback, speech to palestinians, pro-militancy` | 4 | Normal | — |
| `feedback, speech to palestinians, pro-reconstruction` | 1 | Normal | — |
| `feedback, speech to world, cautious` | 1 | Normal | — |
| `feedback, speech to world, demanding` | 1 | Normal | — |
| `feedback, speech to world, hopeful` | 1 | Normal | — |
| `feedback, tourism, close, success` | 2 | Normal | — |
| `feedback, tourism, open, sub-optimal` | 2 | Normal | — |
| `feedback, tourism, open, success` | 2 | Normal | — |
| `financing, arab states, feedback, delay` | 2 | Normal | — |
| `financing, arab states, feedback, refusal` | 2 | Normal | — |
| `financing, arab states, feedback, success` | 2 | Normal | — |
| `financing, arab states, immediate, repetition` | 1 | Normal | RAMALLAH |
| `financing, eu, feedback, delay` | 2 | Normal | — |
| `financing, eu, feedback, refusal` | 2 | Normal | — |
| `financing, eu, feedback, success` | 2 | Normal | — |
| `financing, eu, immediate, repetition` | 1 | Normal | RAMALLAH |
| `financing, israel, feedback, delay` | 2 | Normal | — |
| `financing, israel, feedback, refusal` | 2 | Normal | — |
| `financing, israel, feedback, success` | 2 | Normal | — |
| `financing, israel, immediate, repetition` | 1 | Normal | RAMALLAH |
| `financing, other palestinian, feedback, delay` | 2 | Normal | — |
| `financing, other palestinian, feedback, refusal` | 2 | Normal | — |
| `financing, other palestinian, feedback, success` | 2 | Normal | — |
| `financing, other palestinian, immediate, repetition` | 1 | Normal | RAMALLAH |
| `financing, own resources, feedback, success` | 2 | Normal | — |
| `financing, un, feedback, delay` | 2 | Normal | — |
| `financing, un, feedback, refusal` | 2 | Normal | — |
| `financing, un, feedback, success` | 2 | Normal | — |
| `financing, un, immediate, repetition` | 1 | Normal | RAMALLAH |
| `financing, usa, feedback, delay` | 2 | Normal | — |
| `financing, usa, feedback, refusal` | 2 | Normal | — |
| `financing, usa, feedback, success` | 2 | Normal | — |
| `financing, usa, immediate, repetition` | 1 | Normal | RAMALLAH |
| `gaza border control, close, feedback, success` | 2 | Normal | — |
| `gaza border control, decrease presence, feedback, success` | 2 | Normal | — |
| `gaza border control, eject international troops, feedback, delay` | 1 | — | — |
| `gaza border control, eject international troops, feedback, refusal` | 1 | — | — |
| `gaza border control, eject international troops, feedback, success` | 2 | Normal | — |
| `gaza border control, immediate, repetition` | 1 | Normal | GAZA |
| `gaza border control, increase presence, feedback, sub-optimal` | 1 | Normal | — |
| `gaza border control, increase presence, feedback, success` | 2 | Normal | — |
| `gaza border control, open, feedback, success` | 2 | Normal | — |
| `gaza border control, push control, feedback, delay` | 2 | Normal | — |
| `gaza border control, push control, feedback, refusal` | 2 | Normal | — |
| `gaza border control, push control, feedback, success` | 2 | Normal | — |
| `gaza border control, request international troops, feedback, delay` | 2 | Normal | — |
| `gaza border control, request international troops, feedback, refusal` | 2 | Normal | — |
| `gaza border control, request international troops, feedback, success` | 2 | Normal | — |
| `gaza border, increase presence, feedback, sub-optimal` | 1 | Normal | — |
| `governmental construction, import arms, feedback, success` | 2 | Normal | — |
| `governmental construction, police station, feedback, success` | 2 | Normal | — |
| `governmental construction, prison, feedback, success` | 2 | Normal | — |
| `hamas negotiation, ask for cease-fire, feedback, delay` | 2 | Normal | — |
| `hamas negotiation, ask for cease-fire, feedback, refusal` | 2 | Normal | — |
| `hamas negotiation, ask for cease-fire, feedback, success` | 2 | Normal | — |
| `hamas negotiation, ask for cease-fire, feedback, violent refusal` | 2 | Black, Normal | — |
| `hamas negotiation, ask for law and order, feedback, delay` | 2 | Normal | — |
| `hamas negotiation, ask for law and order, feedback, refusal` | 2 | Normal | — |
| `hamas negotiation, ask for law and order, feedback, success` | 2 | Normal | — |
| `hamas negotiation, ask for peace support, feedback, delay` | 2 | Normal | — |
| `hamas negotiation, ask for peace support, feedback, refusal` | 2 | Normal | — |
| `hamas negotiation, ask for peace support, feedback, success` | 2 | Normal | — |
| `hamas negotiation, ask to disarm, feedback, delay` | 2 | Normal | — |
| `hamas negotiation, ask to disarm, feedback, refusal` | 2 | Normal | — |
| `hamas negotiation, ask to disarm, feedback, success` | 2 | Normal | — |
| `hamas negotiation, ask to disarm, feedback, violent refusal` | 2 | Black | — |
| `hamas negotiation, immediate, repetition` | 1 | Normal | RAMALLAH |
| `hamas, anti-israel, attack` | 10 | Black, Normal | ISRAEL_SETTLEMENT 2, NABLUS, JERICHO, TULKARM, ISRAEL_SETTLEMENT 1, ISRAEL_SETTLEMENT 3, SDEROT, GAZA |
| `hamas, anti-israel, extreme attack` | 10 | Black | ISRAEL_SETTLEMENT 3, ISRAEL_SETTLEMENT 2, BETHLEHEM, NABLUS, JENIN, TEL-AVIV, HADERA, JERUSALEM, RAMALLAH, BEERSHEVA |
| `hamas, anti-israel, funds` | 3 | Normal | RAFAH, GAZA, NABLUS |
| `hamas, anti-israel, organize with international terror` | 3 | Normal, Black | JERUSALEM, RAMALLAH |
| `hamas, anti-israel, words` | 3 | Normal | GAZA, JENIN, RAMALLAH |
| `hamas, anti-you, attack on your organization` | 3 | Black, Normal | GAZA, HEBRON, RAMALLAH |
| `hamas, anti-you, claim victories over you` | 3 | Normal | GAZA, RAMALLAH |
| `hamas, anti-you, words` | 3 | Normal | GAZA, RAMALLAH |
| `hamas, pro-you, commit to reconstruction` | 3 | Normal | GAZA, RAMALLAH, EAST JERUSALEM |
| `hamas, pro-you, join political process` | 3 | Normal | GAZA |
| `hamas, pro-you, partial disarmament` | 3 | Normal | GAZA |
| `hamas, pro-you, words` | 3 | Normal | GAZA |
| `hamas-fatah, anti-israel, attack` | 11 | Black, Normal | ISRAEL_SETTLEMENT 1, NABLUS, HEBRON, ISRAEL_SETTLEMENT 4, QALQILYE, ISRAEL_SETTLEMENT 2, JERUSALEM, RAMALLAH, SDEROT |
| `hamas-fatah, anti-israel, extreme attack` | 11 | Black | ISRAEL_SETTLEMENT 3, HAIFA, ISRAEL_SETTLEMENT 2, ISRAEL_SETTLEMENT 1, TULKARM, TEL-AVIV, NETANYA, SDEROT |
| `hamas-fatah, anti-israel, funds-material` | 4 | Normal | RAFAH, HEBRON, JERUSALEM |
| `hamas-fatah, anti-israel, organize with international terror` | 3 | Black, Normal | JERUSALEM, RAMALLAH |
| `hamas-fatah, anti-israel, words` | 5 | Normal | GAZA, RAMALLAH |
| `holy sites, permit access foreigners, feedback, sub-optimal` | 1 | Normal | — |
| `holy sites, permit access foreigners, feedback, success` | 1 | Normal | — |
| `holy sites, permit access israelis, feedback, sub-optimal` | 1 | Normal | — |
| `holy sites, permit access israelis, feedback, success` | 1 | Normal | — |
| `holy sites, permit access palestinians, feedback, success` | 1 | Normal | — |
| `holy sites, push control, feedback, delay` | 2 | Normal | — |
| `holy sites, push control, feedback, refusal` | 2 | Normal | — |
| `holy sites, push control, feedback, success` | 1 | Normal | — |
| `holy sites, restrict access foreigners, feedback, success` | 1 | Normal | — |
| `holy sites, restrict access israelis, feedback, success` | 1 | Normal | — |
| `holy sites, restrict access palestinians, feedback, sub-optimal` | 1 | Normal | — |
| `holy sites, restrict access palestinians, feedback, success` | 1 | Normal | — |
| `immediate, repetition` | 1 | Normal | — |
| `internal travel, immediate, repetition` | 1 | Normal | RAMALLAH |
| `internal travel, lower restrictions, feedback, success` | 2 | Normal | — |
| `internal travel, push control, feedback, delay` | 2 | Normal | — |
| `internal travel, push control, feedback, refusal` | 2 | Normal | — |
| `internal travel, push control, feedback, success` | 2 | Normal | — |
| `internal travel, raise restrictions, feedback, success` | 2 | Normal | — |
| `international press, concern, low palestinian trust` | 3 | Normal | RAMALLAH, GAZA |
| `international press, concern, low popular approval` | 3 | Normal | Jerusalem, Tel-Aviv |
| `international press, concern, low quality of life` | 3 | Normal | GAZA |
| `international press, concern, low security` | 3 | Normal | JERUSALEM, TEL-AVIV |
| `international press, concern, low sympathy` | 3 | Normal | JERUSALEM, TEL-AVIV |
| `international press, praise, high palestinian trust` | 3 | Normal | RAMALLAH, GAZA |
| `international press, praise, high popular approval` | 3 | Normal | JERUSALEM, TEL-AVIV |
| `international press, praise, high quality of life` | 3 | Normal | RAMALLAH, GAZA |
| `international press, praise, high security` | 3 | Normal | TEL-AVIV, NETANYA, HAIFA |
| `international press, praise, high sympathy` | 3 | Normal | TULKARM, JERUSALEM |
| `israel assassinate militant leader, apache strike, feedback, sub-optimal` | 2 | Black, Normal | — |
| `israel assassinate militant leader, apache strike, feedback, success` | 3 | Black | — |
| `israel assassinate militant leader, covert operation, feedback, sub-optimal` | 2 | Normal | — |
| `israel assassinate militant leader, covert operation, feedback, success` | 3 | Black | — |
| `israel assassinate militant leader, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel bulldoze area, clear roadblocks, feedback, sub-optimal` | 2 | Normal | — |
| `israel bulldoze area, clear roadblocks, feedback, success` | 2 | Normal | — |
| `israel bulldoze area, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel bulldoze area, punish militants, feedback, sub-optimal` | 2 | Normal | — |
| `israel bulldoze area, punish militants, feedback, success` | 2 | Normal | — |
| `israel cultural initiatives, cross-cultural project, feedback, failure` | 2 | Normal | — |
| `israel cultural initiatives, cross-cultural project, feedback, sub-optimal` | 2 | Normal | — |
| `israel cultural initiatives, cross-cultural project, feedback, success` | 3 | Normal | — |
| `israel cultural initiatives, educational initiative, feedback, failure` | 2 | Normal | — |
| `israel cultural initiatives, educational initiative, feedback, sub-optimal` | 2 | Normal | — |
| `israel cultural initiatives, educational initiative, feedback, success` | 2 | Normal | — |
| `israel cultural initiatives, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel cultural initiatives, structured dialog, feedback, failure` | 2 | Normal | — |
| `israel cultural initiatives, structured dialog, feedback, sub-optimal` | 2 | Normal | — |
| `israel cultural initiatives, structured dialog, feedback, success` | 2 | Normal | — |
| `israel cultural initiatives, trade initiative, feedback, failure` | 2 | Normal | — |
| `israel cultural initiatives, trade initiative, feedback, sub-optimal` | 2 | Normal | — |
| `israel cultural initiatives, trade initiative, feedback, success` | 2 | Normal | — |
| `israel curfews, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel curfews, impose curfew, feedback, sub-optimal` | 2 | Normal | — |
| `israel curfews, impose curfew, feedback, success` | 2 | Normal | — |
| `israel curfews, raise curfew, feedback, sub-optimal` | 2 | Normal | — |
| `israel curfews, raise curfew, feedback, success` | 2 | Normal | — |
| `israel domesitic initiatives, economic stimulus, feedback, sub-optimal` | 2 | Normal | — |
| `israel domesitic initiatives, economic stimulus, feedback, success` | 2 | Normal | — |
| `israel domesitic initiatives, educational grants, feedback, sub-optimal` | 2 | Normal | — |
| `israel domesitic initiatives, educational grants, feedback, success` | 2 | Normal | — |
| `israel domesitic initiatives, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel domesitic initiatives, social program, feedback, sub-optimal` | 2 | Normal | — |
| `israel domesitic initiatives, social program, feedback, success` | 2 | Normal | — |
| `israel education aid, direct, feedback, failure` | 2 | Normal | — |
| `israel education aid, direct, feedback, sub-optimal` | 2 | Normal | — |
| `israel education aid, direct, feedback, success` | 2 | Normal | — |
| `israel education aid, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel education aid, with restriction, feedback, failure` | 2 | Normal | — |
| `israel education aid, with restriction, feedback, sub-optimal` | 2 | Normal | — |
| `israel education aid, with restriction, feedback, success` | 2 | Normal | — |
| `israel manage checkpoints, decrease checkpoints, feedback, sub-optimal` | 2 | Normal | — |
| `israel manage checkpoints, decrease checkpoints, feedback, success` | 2 | Normal | — |
| `israel manage checkpoints, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel manage checkpoints, increase checkpoints, feedback, sub-optimal` | 2 | Normal | — |
| `israel manage checkpoints, increase checkpoints, feedback, success` | 2 | Normal | — |
| `israel manage security wall, expand security wall, build wall on green line, feedback, failure` | 2 | Normal | — |
| `israel manage security wall, expand security wall, build wall on green line, feedback, sub-optimal` | 2 | Normal | — |
| `israel manage security wall, expand security wall, build wall on green line, feedback, success` | 2 | Normal | — |
| `israel manage security wall, expand security wall, build wall on palestinian land, feedback, failure` | 2 | Normal | — |
| `israel manage security wall, expand security wall, build wall on palestinian land, feedback, sub-optimal` | 2 | Normal | — |
| `israel manage security wall, expand security wall, build wall on palestinian land, feedback, success` | 2 | Normal | — |
| `israel manage security wall, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel manage security wall, remove security wall, feedback, failure` | 2 | Normal | — |
| `israel manage security wall, remove security wall, feedback, sub-optimal` | 2 | Normal | — |
| `israel manage security wall, remove security wall, feedback, success` | 2 | Normal | — |
| `israel manage settlements, build settlements, build new settlements, feedback, failure` | 2 | Normal | — |
| `israel manage settlements, build settlements, build new settlements, feedback, sub-optimal` | 3 | Normal | — |
| `israel manage settlements, build settlements, build new settlements, feedback, success` | 2 | Normal | — |
| `israel manage settlements, build settlements, expand settlements, feedback, failure` | 5 | Normal | — |
| `israel manage settlements, build settlements, expand settlements, feedback, sub-optimal` | 5 | Normal | — |
| `israel manage settlements, build settlements, expand settlements, feedback, success` | 5 | Normal | — |
| `israel manage settlements, immediate, repetition` | 1 | Normal | ISRAEL_SETTLEMENT 1 |
| `israel manage settlements, remove settlements, dismantle settlement, feedback, failure` | 2 | Normal | — |
| `israel manage settlements, remove settlements, dismantle settlement, feedback, sub-optimal` | 2 | Normal | ISRAEL_SETTLEMENT 1, ISRAEL_SETTLEMENT 2 |
| `israel manage settlements, remove settlements, dismantle settlement, feedback, success` | 2 | Normal | — |
| `israel manage settlements, remove settlements, halt settlement expansion, feedback, failure` | 2 | Normal | — |
| `israel manage settlements, remove settlements, halt settlement expansion, feedback, sub-optimal` | 2 | Normal | — |
| `israel manage settlements, remove settlements, halt settlement expansion, feedback, success` | 2 | Normal | — |
| `israel medical aid, direct, feedback, failure` | 2 | Normal | — |
| `israel medical aid, direct, feedback, sub-optimal` | 2 | Normal | — |
| `israel medical aid, direct, feedback, success` | 2 | Normal | — |
| `israel medical aid, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel medical aid, through un, feedback, failure` | 2 | Normal | — |
| `israel medical aid, through un, feedback, sub-optimal` | 2 | Normal | — |
| `israel medical aid, through un, feedback, success` | 2 | Normal | — |
| `israel missile strike, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel missile strike, militant hq, feedback, sub-optimal` | 2 | Black | — |
| `israel missile strike, militant hq, feedback, success` | 2 | Black, Normal | — |
| `israel missile strike, pa infrastructure, feedback, sub-optimal` | 2 | Black, Normal | — |
| `israel missile strike, pa infrastructure, feedback, success` | 2 | Normal | — |
| `israel missile strike, pa police, feedback, sub-optimal` | 2 | Black, Normal | — |
| `israel missile strike, pa police, feedback, success` | 2 | Black, Normal | — |
| `israel negotiation, ask for safety, feedback, delay` | 2 | Normal | — |
| `israel negotiation, ask for safety, feedback, refusal` | 2 | Normal | — |
| `israel negotiation, ask for safety, feedback, success` | 2 | Normal | — |
| `israel negotiation, ask for wall removal, feedback, delay` | 2 | Normal | — |
| `israel negotiation, ask for wall removal, feedback, refusal` | 2 | Normal | — |
| `israel negotiation, ask for wall removal, feedback, success` | 2 | Normal | — |
| `israel negotiation, ask for withdrawal, feedback, delay` | 2 | Normal | — |
| `israel negotiation, ask for withdrawal, feedback, refusal` | 2 | Normal | — |
| `israel negotiation, ask for withdrawal, feedback, success` | 2 | Normal | — |
| `israel negotiation, immediate, repetition` | 1 | Normal | RAMALLAH |
| `israel negotiation, offer thanks, feedback, sub-optimal` | 2 | Normal | — |
| `israel negotiation, offer thanks, feedback, success` | 2 | Normal | — |
| `israel order idf, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel order idf, remove idf, feedback, sub-optimal` | 2 | Normal | — |
| `israel order idf, remove idf, feedback, success` | 5 | Normal | — |
| `israel order idf, send idf, arrest militants, feedback, sub-optimal` | 3 | Normal, Black | — |
| `israel order idf, send idf, arrest militants, feedback, success` | 7 | Normal, Black | — |
| `israel order idf, send idf, destroy militant infrastructure, feedback, sub-optimal` | 6 | Normal, Black | — |
| `israel order idf, send idf, destroy militant infrastructure, feedback, success` | 3 | Normal, Black | — |
| `israel order idf, send idf, secure area, feedback, sub-optimal` | 8 | Black, Normal | — |
| `israel order idf, send idf, secure area, feedback, success` | 3 | Normal | — |
| `israel order police, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel order police, remove police, feedback, sub-optimal` | 2 | Normal | — |
| `israel order police, remove police, feedback, success` | 2 | Normal | — |
| `israel order police, send police, patrol, feedback, sub-optimal` | 2 | Normal | — |
| `israel order police, send police, patrol, feedback, success` | 4 | Normal | — |
| `israel order police, send police, secure, feedback, sub-optimal` | 2 | Normal | — |
| `israel order police, send police, secure, feedback, success` | 3 | Normal | — |
| `israel pm, anti-terror, blame you` | 5 | Normal | JERUSALEM, RAMALLAH |
| `israel pm, anti-terror, extreme security act` | 10 | Black, Normal | JENIN, NABLUS, GAZA, HEBRON, ISRAEL_SETTLEMENT 2 |
| `israel pm, anti-terror, security measures` | 10 | Normal, Black | JENIN, TULKARM, HEBRON, NABLUS, KFAR SAVA, RAMALLAH |
| `israel pm, pro-peace, apologize for actions` | 5 | Normal, Black | JERUSALEM, GAZA, JENIN |
| `israel pm, pro-peace, remove a security measure` | 5 | Normal | BETHLEHEM, GAZA, NABLUS |
| `israel pm, pro-reconstruction, offer aid in construction` | 5 | Normal | JERUSALEM, HEBRON, GAZA, RAMALLAH |
| `israel reconstruction aid, civilian aid, feedback, failure` | 2 | Normal | — |
| `israel reconstruction aid, civilian aid, feedback, sub-optimal` | 2 | Normal | — |
| `israel reconstruction aid, civilian aid, feedback, success` | 2 | Normal | — |
| `israel reconstruction aid, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel reconstruction aid, infrastructure aid, feedback, failure` | 2 | Normal | — |
| `israel reconstruction aid, infrastructure aid, feedback, sub-optimal` | 2 | Normal | — |
| `israel reconstruction aid, infrastructure aid, feedback, success` | 3 | Normal, — | — |
| `israel reconstruction aid, security aid, feedback, failure` | 2 | Normal | — |
| `israel reconstruction aid, security aid, feedback, sub-optimal` | 2 | Normal | — |
| `israel reconstruction aid, security aid, feedback, success` | 2 | Normal | — |
| `israel refugee affairs, allow some palestinian immigrants, feedback, failure` | 2 | Normal | — |
| `israel refugee affairs, allow some palestinian immigrants, feedback, sub-optimal` | 2 | Normal | — |
| `israel refugee affairs, allow some palestinian immigrants, feedback, success` | 2 | Normal | — |
| `israel refugee affairs, authorize payments to refugees, feedback, failure` | 2 | Normal | — |
| `israel refugee affairs, authorize payments to refugees, feedback, sub-optimal` | 2 | Normal | — |
| `israel refugee affairs, authorize payments to refugees, feedback, success` | 2 | Normal | — |
| `israel refugee affairs, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel release prisoners, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel release prisoners, release non-violent prisoners, feedback, failure` | 2 | Normal | — |
| `israel release prisoners, release non-violent prisoners, feedback, sub-optimal` | 2 | Normal | — |
| `israel release prisoners, release non-violent prisoners, feedback, success` | 2 | Normal | — |
| `israel release prisoners, release violent prisoners, feedback, failure` | 2 | Normal | — |
| `israel release prisoners, release violent prisoners, feedback, sub-optimal` | 2 | Normal | — |
| `israel release prisoners, release violent prisoners, feedback, success` | 2 | Normal | — |
| `israel talk to palestinian president, ask for anti-militant support, feedback, delay` | 4 | Normal | JERUSALEM, — |
| `israel talk to palestinian president, ask for anti-militant support, feedback, refusal` | 3 | Normal | — |
| `israel talk to palestinian president, ask for anti-militant support, feedback, success` | 3 | Normal | RAMALLAH, JERUSALEM |
| `israel talk to palestinian president, feedback, aggression` | 1 | Normal | — |
| `israel talk to palestinian president, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to palestinian president, insist on anti-militant support, feedback, delay` | 2 | Normal | — |
| `israel talk to palestinian president, insist on anti-militant support, feedback, refusal` | 3 | Normal | — |
| `israel talk to palestinian president, insist on anti-militant support, feedback, success` | 2 | Normal | — |
| `israel talk to palestinian president, promise reconstruction assistance, feedback, sub-optimal` | 2 | Normal | — |
| `israel talk to palestinian president, promise reconstruction assistance, feedback, success` | 2 | Normal | — |
| `israel talk to palestinian president, promise security, feedback, sub-optimal` | 2 | Normal | — |
| `israel talk to palestinian president, promise security, feedback, success` | 2 | Normal | — |
| `israel talk to the world, anti-militancy, feedback, neutrally` | 2 | Normal | — |
| `israel talk to the world, anti-militancy, feedback, poorly` | 2 | Normal | — |
| `israel talk to the world, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to the world, pro-palestinian cooperation, feedback, neutrally` | 2 | Normal | — |
| `israel talk to the world, pro-palestinian cooperation, feedback, poorly` | 1 | Normal | — |
| `israel talk to the world, pro-peace process, feedback, neutrally` | 2 | Normal | — |
| `israel talk to the world, pro-security, feedback, neutrally` | 2 | Normal | — |
| `israel talk to the world, pro-security, feedback, poorly` | 2 | Normal | TEL-AVIV |
| `israel talk to world leaders, eu negotiation, ask for mediation support, feedback, delay` | 2 | Normal | — |
| `israel talk to world leaders, eu negotiation, ask for mediation support, feedback, refusal` | 2 | Normal | — |
| `israel talk to world leaders, eu negotiation, ask for mediation support, feedback, success` | 2 | Normal | — |
| `israel talk to world leaders, eu negotiation, ask for political pressure on palestine, feedback, delay` | 2 | Normal | — |
| `israel talk to world leaders, eu negotiation, ask for political pressure on palestine, feedback, refusal` | 2 | Normal | — |
| `israel talk to world leaders, eu negotiation, ask for political pressure on palestine, feedback, success` | 2 | Normal | — |
| `israel talk to world leaders, eu negotiation, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to world leaders, un negotiation, ask for mediation support, feedback, delay` | 2 | Normal | — |
| `israel talk to world leaders, un negotiation, ask for mediation support, feedback, refusal` | 2 | Normal | — |
| `israel talk to world leaders, un negotiation, ask for mediation support, feedback, success` | 2 | Normal | — |
| `israel talk to world leaders, un negotiation, ask for political pressure on palestine, feedback, delay` | 2 | Normal | — |
| `israel talk to world leaders, un negotiation, ask for political pressure on palestine, feedback, refusal` | 2 | Normal | — |
| `israel talk to world leaders, un negotiation, ask for political pressure on palestine, feedback, success` | 2 | Normal | — |
| `israel talk to world leaders, un negotiation, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to world leaders, usa negotiation, ask for mediation support, feedback, delay` | 2 | Normal | — |
| `israel talk to world leaders, usa negotiation, ask for mediation support, feedback, refusal` | 2 | Normal | — |
| `israel talk to world leaders, usa negotiation, ask for mediation support, feedback, success` | 2 | Normal | — |
| `israel talk to world leaders, usa negotiation, ask for political pressure on palestine, feedback, delay` | 2 | Normal | — |
| `israel talk to world leaders, usa negotiation, ask for political pressure on palestine, feedback, refusal` | 2 | Normal | — |
| `israel talk to world leaders, usa negotiation, ask for political pressure on palestine, feedback, success` | 2 | Normal | — |
| `israel talk to world leaders, usa negotiation, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to your government, ask for less criticism, feedback, delay` | 2 | Normal | — |
| `israel talk to your government, ask for less criticism, feedback, refusal` | 2 | Normal | — |
| `israel talk to your government, ask for less criticism, feedback, success` | 2 | Normal | — |
| `israel talk to your government, ask for withdrawal support, feedback, delay` | 2 | Normal | — |
| `israel talk to your government, ask for withdrawal support, feedback, refusal` | 2 | Normal | — |
| `israel talk to your government, ask for withdrawal support, feedback, success` | 2 | Normal | — |
| `israel talk to your government, ask to unite for peace, feedback, delay` | 2 | Normal | — |
| `israel talk to your government, ask to unite for peace, feedback, refusal` | 2 | Normal | — |
| `israel talk to your government, ask to unite for peace, feedback, success` | 3 | Normal | —, JERUSALEM |
| `israel talk to your government, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to your government, promise more security, feedback, sub-optimal` | 2 | Normal | — |
| `israel talk to your government, promise more security, feedback, success` | 2 | Normal | — |
| `israel talk to your people, anti-militancy, feedback, neutrally` | 2 | Normal | — |
| `israel talk to your people, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel talk to your people, pro-palestinian cooperation, feedback, neutrally` | 2 | Normal | — |
| `israel talk to your people, pro-palestinian cooperation, feedback, poorly` | 2 | Normal | — |
| `israel talk to your people, pro-peace process, feedback, neutrally` | 2 | Normal | JERUSALEM |
| `israel talk to your people, pro-peace process, feedback, poorly` | 2 | Normal | — |
| `israel talk to your people, pro-security, feedback, neutrally` | 2 | Normal | JERUSALEM |
| `israel trade restrictions, decrease trade restrictions, feedback, failure` | 1 | — | — |
| `israel trade restrictions, decrease trade restrictions, feedback, sub-optimal` | 2 | Normal | — |
| `israel trade restrictions, decrease trade restrictions, feedback, success` | 2 | Normal | — |
| `israel trade restrictions, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel trade restrictions, increase trade restrictions, feedback, sub-optimal` | 2 | Normal | — |
| `israel trade restrictions, increase trade restrictions, feedback, success` | 2 | Normal | — |
| `israel worker permits, decrease worker permits, feedback, sub-optimal` | 2 | Normal | — |
| `israel worker permits, decrease worker permits, feedback, success` | 2 | Normal | — |
| `israel worker permits, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel worker permits, increase worker permits, feedback, failure` | 2 | — | — |
| `israel worker permits, increase worker permits, feedback, sub-optimal` | 2 | Normal | — |
| `israel worker permits, increase worker permits, feedback, success` | 2 | Normal | — |
| `israel yesha, arrest leaders, feedback, failure` | 2 | Normal | — |
| `israel yesha, arrest leaders, feedback, sub-optimal` | 2 | Normal | — |
| `israel yesha, arrest leaders, feedback, success` | 2 | Normal | — |
| `israel yesha, ask for restraint, feedback, failure` | 2 | Normal | — |
| `israel yesha, ask for restraint, feedback, sub-optimal` | 2 | Normal | — |
| `israel yesha, ask for restraint, feedback, success` | 2 | Normal | — |
| `israel yesha, immediate, repetition` | 1 | Normal | JERUSALEM |
| `israel yesha, promise concessions, feedback, failure` | 2 | Normal | — |
| `israel yesha, promise concessions, feedback, sub-optimal` | 2 | Normal | — |
| `israel yesha, promise concessions, feedback, success` | 2 | Normal | — |
| `israel yesha, suppress violence, feedback, sub-optimal` | 2 | Normal | — |
| `israel yesha, suppress violence, feedback, success` | 2 | Normal | — |
| `israeli ending, israeli lose` | 1 | ending | JERUSALEM |
| `israeli ending, palestinian lose` | 1 | ending | JERUSALEM |
| `israeli ending, win` | 1 | ending | JERUSALEM |
| `israeli forces cooperation, joint training stop, feedback, success` | 1 | Normal | — |
| `israeli government, anti-palestine, words` | 3 | Normal | JENIN, JERUSALEM, HEBRON |
| `israeli government, anti-you, words` | 3 | Normal | JERUSALEM, TEL-AVIV |
| `israeli government, concern, low palestinian trust` | 3 | Normal | JERUSALEM, GAZA |
| `israeli government, concern, low popular approval` | 3 | Normal | JERUSALEM |
| `israeli government, concern, low quality of life` | 3 | Normal | JERUSALEM, JENIN |
| `israeli government, concern, low security` | 3 | Normal | JERUSALEM |
| `israeli government, concern, low sympathy` | 3 | — | — |
| `israeli government, praise, high palestinian trust` | 3 | Normal | JERUSALEM, RAMALLAH, BETHLEHEM |
| `israeli government, praise, high popular approval` | 3 | Normal | JERUSALEM, TEL-AVIV |
| `israeli government, praise, high quality of life` | 3 | Normal | JERUSALEM, GAZA, RAMALLAH |
| `israeli government, praise, high security` | 3 | Normal | TEL-AVIV, JERUSALEM |
| `israeli government, praise, high sympathy` | 3 | Normal | JERUSALEM, RAMALLAH, TEL-AVIV |
| `israeli government, pro-you, words` | 3 | Normal | TEL-AVIV, JERUSALEM |
| `israeli plot 1` | 1 | plot | JERUSALEM |
| `israeli plot 2` | 1 | plot | GAZA |
| `israeli plot 3` | 1 | plot | RAMALLAH |
| `israeli public, anti-palestine, street protest` | 3 | Normal | JERUSALEM, EAST JERUSALEM |
| `israeli public, anti-you, petition` | 3 | Normal | JERUSALEM, NETANYA, TEL-AVIV |
| `israeli public, anti-you, street protest` | 3 | Normal | AFULA, JERUSALEM, TEL-AVIV |
| `israeli public, concern, low approval` | 5 | Normal | TEL-AVIV, JERUSALEM |
| `israeli public, concern, low security` | 5 | Normal, Black | HAIFA, NETANYA, JERUSALEM, TEL-AVIV |
| `israeli public, concern, low suppression` | 5 | Normal, Black | JERUSALEM, ISRAEL_SETTLEMENT 1, TEL-AVIV |
| `israeli public, praise, high approval` | 3 | Normal | JERUSALEM |
| `israeli public, praise, high security` | 5 | Normal | HAIFA, JERUSALEM, AFULA, TEL-AVIV |
| `israeli public, praise, high suppression` | 5 | Normal | JERUSALEM, HEBRON, NABLUS, GAZA |
| `israeli public, praise, high sympathy` | 5 | Normal | RAMALLAH, TEL-AVIV, QALQILYE |
| `israeli public, pro-you, petition` | 3 | Normal | AFULA, HAIFA, TEL-AVIV |
| `israeli public, pro-you, street rally` | 3 | Normal | JERUSALEM, TEL-AVIV |
| `jordan negotiate, immediate, repetition` | 1 | Normal | RAMALLAH |
| `jordan negotiate, request aid, feedback, delay` | 2 | Normal | — |
| `jordan negotiate, request aid, feedback, refusal` | 2 | Normal | — |
| `jordan negotiate, request aid, feedback, success` | 2 | Normal | — |
| `jordan negotiate, request investment, feedback, delay` | 2 | Normal | — |
| `jordan negotiate, request investment, feedback, refusal` | 2 | Normal | — |
| `jordan negotiate, request investment, feedback, success` | 2 | Normal | — |
| `jordan negotiate, request meeting, feedback, delay` | 2 | Normal | — |
| `jordan negotiate, request meeting, feedback, refusal` | 2 | Normal | — |
| `jordan negotiate, request meeting, feedback, success` | 2 | Normal | — |
| `jordan negotiate, request political pressure, feedback, delay` | 2 | Normal | — |
| `jordan negotiate, request political pressure, feedback, refusal` | 2 | Normal | — |
| `jordan negotiate, request political pressure, feedback, success` | 2 | Normal | — |
| `natural resource construction, communications, feedback, success` | 2 | Normal | — |
| `natural resource construction, infrastructure, feedback, success` | 2 | Normal | — |
| `natural resource construction, power plant, feedback, success` | 2 | Normal | — |
| `natural resource construction, water table, push control, feedback, delay` | 2 | Normal | — |
| `natural resource construction, water table, push control, feedback, refusal` | 2 | Normal | — |
| `natural resource construction, water table, push control, feedback, success` | 2 | Normal | — |
| `natural resource construction, water treatment plant, feedback, success` | 2 | Normal | — |
| `palestinian president, anti-militant, extreme police` | 5 | Black | GAZA, JENIN, NABLUS |
| `palestinian president, anti-militant, police` | 5 | Normal, Black | HEBRON, GAZA, JENIN |
| `palestinian president, anti-militant, political` | 5 | Normal | GAZA, RAMALLAH |
| `palestinian president, anti-militant, words` | 5 | Normal | RAMALLAH, GAZA |
| `palestinian president, anti-you, words` | 6 | Normal, Black | GAZA, RAMALLAH, JERUSALEM |
| `palestinian president, concern, low quality of life` | 5 | Normal | RAMALLAH, GAZA, RAFAH, JENIN |
| `palestinian president, concern, low trust` | 5 | Normal | GAZA, RAMALLAH |
| `palestinian president, concern, too much violence` | 5 | Normal, Black | RAMALLAH, GAZA |
| `palestinian president, praise, high quality of life` | 5 | Normal | RAMALLAH, GAZA |
| `palestinian president, praise, high trust` | 5 | Normal | RAMALLAH, RAFAH |
| `palestinian president, pro-you, offer to meet for negotiations` | 5 | Normal | RAMALLAH, TEL-AVIV |
| `palestinian president, pro-you, street rally` | 5 | Normal | RAMALLAH, GAZA |
| `palestinian president, pro-you, words` | 5 | Normal | RAMALLAH, GAZA, NABLUS, JERUSALEM |
| `palestinian public, anti-you, aggressive protest` | 5 | Normal, Black | ISRAEL_SETTLEMENT 2, JERUSALEM, BETHLEHEM, GAZA, ISRAEL_SETTLEMENT 3 |
| `palestinian public, anti-you, street protest` | 5 | Normal, Black | ISRAEL_SETTLEMENT 2, GAZA, RAMALLAH |
| `palestinian public, concern, low quality of life` | 6 | Normal | HEBRON, RAMALLAH, JENIN, GAZA, NABLUS |
| `palestinian public, concern, too much violence` | 5 | Normal | NABLUS, HEBRON, RAMALLAH |
| `palestinian public, feedback about government, negative, material needs` | 5 | Normal | GAZA, RAMALLAH |
| `palestinian public, feedback about government, negative, rights` | 5 | Normal | RAMALLAH, ISRAEL_SETTLEMENT 2, NABLUS, EAST JERUSALEM, GAZA |
| `palestinian public, feedback about government, negative, support fatah` | 3 | Normal | RAMALLAH, NABLUS, GAZA |
| `palestinian public, feedback about government, negative, support hamas` | 3 | Normal | GAZA |
| `palestinian public, feedback about government, positive, reconstruction` | 3 | Normal | GAZA, EAST JERUSALEM, BETHLEHEM |
| `palestinian public, feedback about government, positive, support` | 3 | Normal | GAZA, RAMALLAH |
| `palestinian public, feedback about peace process, angry` | 5 | Normal | JENIN, NABLUS, GAZA |
| `palestinian public, feedback about peace process, desire action` | 5 | Normal | RAMALLAH, EAST JERUSALEM |
| `palestinian public, feedback about peace process, enthusiastic` | 5 | Normal | RAMALLAH, GAZA, JERUSALEM, HAIFA |
| `palestinian public, praise, high quality of life` | 5 | Normal | GAZA, NABLUS |
| `palestinian public, pro-you, street rally` | 5 | Normal | TULKARM, RAMALLAH, GAZA |
| `plot 1` | 1 | plot | GAZA |
| `plot 2` | 1 | plot | GAZA |
| `plot 3` | 1 | plot | RAMALLAH |
| `police manage, decrease funding, feedback, success` | 2 | Normal | — |
| `police manage, immediate, repetition` | 1 | Normal | RAMALLAH |
| `police manage, increase funding, feedback, success` | 2 | Normal | — |
| `police manage, restructure, feedback, failure` | 2 | Normal | — |
| `police manage, restructure, feedback, sub-optimal` | 2 | Normal | — |
| `police manage, restructure, feedback, success` | 2 | Normal | — |
| `police manage, train, feedback, success` | 2 | Normal | — |
| `police presence, immediate, repetition` | 1 | Normal | RAMALLAH |
| `police presence, maintain order, sub-optimal` | 2 | Normal | — |
| `police presence, maintain order, success` | 3 | Normal | — |
| `police presence, patrol for militants, sub-optimal` | 2 | Normal | — |
| `police presence, patrol for militants, success` | 2 | Normal | — |
| `push control, immediate, repetition` | 1 | Normal | RAMALLAH |
| `social services construction, care for the poor, feedback, success` | 2 | Normal | — |
| `social services construction, health care, feedback, success` | 2 | Normal | — |
| `speech to palestinians, immediate, repetition` | 1 | Normal | RAMALLAH |
| `speech to palestinians, pro-law and order, feedback, received well` | 2 | Normal | — |
| `speech to palestinians, pro-reconstruction, feedback, received well` | 1 | Normal | — |
| `speech to world, cautious, feedback, received well` | 1 | Normal | — |
| `speech to world, demanding, feedback, received well` | 1 | Normal | — |
| `speech to world, hopeful, feedback, received well` | 1 | Normal | — |
| `speech to world, immediate, repetition` | 1 | Normal | RAMALLAH |
| `transportation construction, airport, feedback, success` | 3 | Normal | — |
| `transportation construction, airspace, push control, feedback, delay` | 2 | Normal | — |
| `transportation construction, airspace, push control, feedback, refusal` | 2 | Normal | — |
| `transportation construction, airspace, push control, feedback, success` | 2 | Normal | — |
| `transportation construction, coastal waters, push control, feedback, delay` | 2 | Normal | — |
| `transportation construction, coastal waters, push control, feedback, refusal` | 2 | Normal | — |
| `transportation construction, coastal waters, push control, feedback, success` | 2 | Normal | — |
| `transportation construction, roads, feedback, success` | 2 | Normal | — |
| `transportation construction, seaport, feedback, success` | 2 | Normal | — |
| `un negotiate, immediate, repetition` | 1 | Normal | RAMALLAH |
| `un negotiate, request aid, feedback, delay` | 2 | Normal | — |
| `un negotiate, request aid, feedback, refusal` | 2 | Normal | — |
| `un negotiate, request aid, feedback, success` | 2 | Normal | — |
| `un negotiate, request investment, feedback, delay` | 2 | Normal | — |
| `un negotiate, request investment, feedback, refusal` | 2 | Normal | — |
| `un negotiate, request investment, feedback, success` | 2 | Normal | — |
| `un negotiate, request meeting, feedback, delay` | 2 | Normal | — |
| `un negotiate, request meeting, feedback, refusal` | 2 | Normal | — |
| `un negotiate, request meeting, feedback, success` | 2 | Normal | — |
| `un negotiate, request political pressure, feedback, delay` | 2 | Normal | — |
| `un negotiate, request political pressure, feedback, refusal` | 2 | Normal | — |
| `un negotiate, request political pressure, feedback, success` | 2 | Normal | — |
| `usa negotiate, immediate, repetition` | 1 | Normal | RAMALLAH |
| `usa negotiate, request aid, feedback, delay` | 2 | Normal | — |
| `usa negotiate, request aid, feedback, refusal` | 2 | Normal | — |
| `usa negotiate, request aid, feedback, success` | 2 | Normal | — |
| `usa negotiate, request investment, feedback, delay` | 2 | Normal | — |
| `usa negotiate, request investment, feedback, refusal` | 2 | Normal | — |
| `usa negotiate, request investment, feedback, success` | 2 | Normal | — |
| `usa negotiate, request meeting, feedback, delay` | 2 | Normal | — |
| `usa negotiate, request meeting, feedback, refusal` | 2 | Normal | — |
| `usa negotiate, request meeting, feedback, success` | 2 | Normal | — |
| `usa negotiate, request political pressure, feedback, delay` | 2 | Normal | — |
| `usa negotiate, request political pressure, feedback, refusal` | 2 | Normal | — |
| `usa negotiate, request political pressure, feedback, success` | 2 | Normal | — |
| `yesha, anti-palestine, assault` | 7 | Black | ISRAEL_SETTLEMENT 2, NABLUS, ISRAEL_SETTLEMENT 4, HEBRON |
| `yesha, anti-palestine, harassment` | 5 | Normal | TULKARM, HEBRON, ISRAEL_SETTLEMENT 3 |
| `yesha, anti-palestine, illegal expansion` | 5 | Normal | ISRAEL_SETTLEMENT 2, ISRAEL_SETTLEMENT 3, ISRAEL_SETTLEMENT 1, ISRAEL_SETTLEMENT 4 |
| `yesha, anti-you, petition` | 4 | Normal | ISRAEL_SETTLEMENT 1, JERUSALEM, TEL-AVIV, HAIFA |
| `yesha, anti-you, street protests` | 7 | Normal | JERUSALEM, AFULA, TEL-AVIV |
| `yesha, concern, low approval` | 5 | Normal, Black | ISRAEL_SETTLEMENT 1, HEBRON, NABLUS |
| `yesha, concern, settlement withdrawal` | 6 | Normal | TEL-AVIV, ISRAEL_SETTLEMENT 3, JENIN, NABLUS, ISRAEL_SETTLEMENT 2 |
| `yesha, praise, high approval` | 3 | Normal | ISRAEL_SETTLEMENT 2, RAMALLAH |
| `yesha, praise, settlement expansion` | 5 | — | —, Jerusalem |

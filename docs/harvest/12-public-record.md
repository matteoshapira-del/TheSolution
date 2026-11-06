# 12 · Public record: history, research and reception

This chapter is a public-sources dossier (press, academic papers, store listings, ImpactGames' own pages),
compiled in November 2026. It starts with the open questions those sources left unresolved, answered from the
game files we harvested. The dossier itself follows unchanged, with its own confidence markers and references.

## Open questions, answered from the game files (2015 Unity build)

| Question in the public record | Answer from the files | Where |
|---|---|---|
| Loss threshold: −50 or −100? A screenshot shows −60 with no game over | **−50, but it must hold for 4 consecutive turn checks.** Scores can fall to −100 (that's the display range), so a −60 that recovers within 3 turns doesn't end the game. This agrees with Adams and Kampf | [04](04-scoring-and-endings.md) |
| Win at "+100"? | Both scores **≥ 95 for 4 consecutive checks**. Displayed scores cap at 100 | [04](04-scoring-and-endings.md) |
| What triggers the 4 milestones (25/50/75/100 was a guess)? | Milestones 1–3 at **30 / 50 / 70** on both scores (2 consecutive checks each). The win is "milestone 4" | [04](04-scoring-and-endings.md) |
| Which failure belongs to which score on the Palestinian side? | Internal ≤ −50 → "A Civil War Breaks Out". External ≤ −50 → "International Support Pulled". Israeli side: internal → "Removed from Office", external → "The Third Intifada" | [04](04-scoring-and-endings.md) |
| Formula and range of the violence rating ("over 250")? | The `endreport` tally (the only variable allowed above 100) sums a violence cost per action and attack. Tiers: >150 Extreme, >100 High, >50 Moderate, >0 Low, else None | [04](04-scoring-and-endings.md) |
| Does difficulty change only event frequency? | **Yes.** Only AI sleep times change. Odds, effect sizes and scoring are identical | [09](09-difficulty-and-balance.md) |
| Is there a turn limit or term in office? | No turn cap in the code. The calendar starts at the **real current date**, which explains the 2015 dates in mobile screenshots | [03](03-turn-loop.md) |
| Budget model? | The Israeli PM has no budget. The Palestinian President has 8 funding pools that refill from patrons' approval, plus fixed project costs | [05](05-sides-stakeholders-and-meters.md) |
| Are events mechanically inert (Stanford, 2024)? | AI events do move meters, applied when you open the pin (e.g. a Hamas attack: Israeli public −7, settlers −8, security −5). But there's **no response mechanic**: you can't answer an event, only take your next action. That's probably why players felt responses didn't matter | [03](03-turn-loop.md), [07](07-ai-actors.md) |
| Full action list? | Complete: 76 Israeli and 99 Palestinian leaf actions, plus 7 funders, with every result branch | [catalog](catalog/) |
| Polls per side? | Israeli: security, sympathy, suppression, Palestinian cooperation, leadership. Palestinian: economy, government authority, independence, leadership, view of Israel, Israeli cooperation | [05](05-sides-stakeholders-and-meters.md) |
| Did the 2015 remaster adopt the planned "2.0" inciting incidents? | **No.** The 2015 build still opens with the West Jerusalem bus bombing (Israeli side) and the Gaza tank fire (Palestinian side) | [08](08-events-news-and-media.md) |
| Dominant strategies and the inverse difficulty curve? | Confirmed by simulation: the same 5–6 actions win every skilled game. Upkeep feedback loops make the late game easier | [09](09-difficulty-and-balance.md) |

**Engine lineage (inference).** The rules XML uses the namespace `data.resources.peacemaker.impact`, and the 2007 game's
Java settings class is `impact.peacemaker.gui.UserConfigSettings`. That suggests the 2015 Unity remaster reuses
the original Java-era rules data, ported rather than redesigned. The public S3 bucket listing every desktop build
(1.06–1.25, including Linux and "log_patch" research builds) would let a later pass diff the 2007 rules against 2015.

---

## Dossier: PeaceMaker (ImpactGames, 2007; mobile/desktop re-release c. 2015–2016): public-record design dossier

Compiled 2026-11-06. This dossier covers how PeaceMaker works as a design, drawn from public sources. Everything is paraphrased. Citations are reference-style links; the full URL list is at the bottom. Confidence markers:

- **[V]** Verified: two or more independent sources agree, or a primary source (a screenshot, an official document, or the developer's own words) shows it directly.
- **[S]** Single source.
- **[?]** Unverified, conflicting, or inferred.

> **Method note / access limits.** The Wayback Machine (`web.archive.org`, including CDX and `id_` URLs) was **blocked by this session's egress policy**. Plain HTTP returned "Blocked by egress policy" and HTTPS connections were reset, every time I tried. The `archive.org/wayback/available` API did work, and it confirmed a 2009-01-06 snapshot of peacemakergame.com exists, but I could not open it. As a result I could not read the archived peacemakergame.com pages (game, features, FAQ, educators, press) or the ImpactGames blog posts (design assumptions, two-state rationale, patches, the free release). Their content is reconstructed here from secondary quotations: Wikipedia's summaries of those posts, marketing bullet lists mirrored by app and download sites, and press releases quoted by news sites. Three other things were readable and have no casino spam in the parts used here: the live `impactgames.com` subpages (they still serve 2012 content, though spam links have been injected), the live `peacemakergame.com` homepage header, news ticker and store badges (the body below them is casino spam, so only the header was used), and a public S3 bucket at `download.peacemakergame.com` that lists every build. Those parts are cited and flagged. Several key screenshots (desktop and mobile) were pulled out of academic PDFs and read directly; they are the best primary evidence for the UI and scoring.

---

## (a) Facts & history

### Origins and team
- PeaceMaker began as a Carnegie Mellon Entertainment Technology Center (ETC) master's project. The pitch was made in fall 2004, development started in 2005, and the work ran over about four semesters ([Greater Good 2006][greatergood]; [Wikipedia][wiki-en]). **[V]**
- Producers were Asi Burak (a former Israeli intelligence captain) and Eric Brown. Tim Sweeney was lead designer, with Olive Lin. Victoria Webb was the writer and Ross Popoff the composer. Eric Keylor and Lin did the programming, and Patrick Bannan made the art ([Wikipedia][wiki-en], citing ETC team pages and Bannan's portfolio). [Greater Good][greatergood] adds that the music was composed by faculty advisor Tina Blaine. **[?]** The two composer credits conflict; perhaps both contributed.
- Advisors and testers included CMU Middle East historian Laurie Eisenberg, who pointed out that "release Palestinian prisoners" was missing as an Israeli action and insisted the team find Palestinian advisors. The team recruited Palestinian collaborators; two joined the team ([Greater Good][greatergood]; [Wired 2006][wired]). Burak later wrote that a granddaughter of Mahmoud Abbas was among the collaborators ([Kotaku 2014][kotaku]). The game was playtested with Arab students at CMU-Qatar in Doha ([Gamasutra 2013][gd2013]; [Walla 2007][walla]). **[V]**
- The design was prototyped with board games, then turned into a "dice game" that could be coded. The logic engine and AI were written in Java, and the GUI used Flash and QuickTime ([Wikipedia][wiki-en], citing Burak, Keylor & Sweeney 2005). Supporting evidence: a settings file in the official download bucket is a serialized Java object, `impact.peacemaker.gui.UserConfigSettings` ([settings.pm][settings]). **[V]**
- The prototype was shown at GDC in spring 2005 ([Spong, quoting the ImpactGames press text][spong]). An academic demo paper was published as Burak, Keylor & Sweeney, "PeaceMaker: A Video Game to Teach Peace", INTETAIN 2005, LNCS 3814, pp. 307–310 ([Springer][intetain]). CMU issued a press release on 2005-10-27 ([Wikipedia][wiki-en]). **[V]**
- The game won USC's "Reinventing Public Diplomacy through Games" contest (first place, 2006-05-08). Burak and Brown founded ImpactGames in 2006 to take it to market ([ImpactGames PeaceMaker page][igpm]; [ImpactGames About][igabout]). **[V]**
- Funding and cost: AP reported a development budget of $300k–$500k from socially motivated investors ([Legit Reviews/AP 2006][legit]). Walla reported that about $0.5M was raised from private investors and a Pittsburgh incubator ([Walla 2007][walla]). **[S]** for each figure.
- The United States Institute of Peace supported the game as an educational tool ([Cuhadar & Kampf 2014][ck2014]). **[S]**
- Corporate history: ImpactGames' assets and naming rights were acquired by Hybrid Learning Systems in 2010, with Brown as its president. Burak went on to co-lead and later preside over Games for Change ([ImpactGames About][igabout]; [Mother Jones 2014][mj]). According to Gamasutra, the PeaceMaker technology "was eventually sold mainly to return money to its investors" ([Gamasutra 2013][gd2013]). **[V]**

### Release, versions, platforms, price
- **Release:** version 1.0 shipped in English, Hebrew and Arabic in January 2007 (blog post "PeaceMaker 1.0 in three languages", 2007-01-09). Most sources give the commercial release date as 2007-02-01 ([Wikipedia][wiki-en]; [MobyGames via search][moby]). Wikipedia's body text says "1 February **2005**", which is an error; the French article says 2007 ([wiki-fr][wiki-fr]). A boxed version went on sale on Amazon about four months later ([Wikipedia][wiki-en]). One download listing names **Manifesto Games** as publisher ([Gamepressure][gamepressure]). **[V]** for dates; **[S]** for Manifesto.
- **Price:** about $20 at launch (US$19.95/£10) ([Macworld 2007-02-12][macworld]; [Eurogamer][eurogamer]; [Spong][spong]). A free demo was available ([Walla][walla]; [Gamepressure demo v1.063][gamepressure]). The price prompted debate; ImpactGames defended the for-profit model in its blog post "Why PeaceMaker costs money" ([Wikipedia][wiki-en]). The desktop game became **free on 2013-11-04** (blog post "PeaceMaker Free to Everyone!") ([Wikipedia][wiki-en]; [Kotaku 2014][kotaku] calls it "now available for free"). **[V]**
- **Desktop builds**, from the public S3 listing at [download.peacemakergame.com][s3] (file dates are upload dates; binaries were not downloaded):
  - 1.06 full and demo (Win/Mac, Nov 2008)
  - patches 1.063 (July 2007, per [Gamepressure][gamepressure]; QuickTime fix per the 2007-07-18 blog post linked from [the live homepage][pmhome]), 1.064, 1.066 and 1.068 (Nov 2008)
  - a special "perez" CD patch 1.068 for the Peres Center distribution, with separate Arabic, English and Hebrew settings
  - 1.1 (Dec 2008) and 1.2 (June 2009, including a **Linux** build and "d2d" and "mgs" storefront variants)
  - "log_patch" builds (2009), which match CMU's report that ImpactGames modified the game to record every player action for research ([CMU 2007][cmu2007])
  - 1.1_v2 (Feb 2012), 1.15 (Apr 2012), 1.25 (Nov 2012, with a Unix .sh build) and 1.1.1 (Oct 2013, around the free release). **[S]** (primary listing; version semantics not verified)
- **System requirements (2007 Mac):** OS X 10.4+, PowerPC or Intel, 128 MB RAM, 500 MB disk ([Macworld][macworld]). Install size is about 230 MB. QuickTime was needed for video and sound, and the game sometimes failed to detect it ([WPI analysis][wpi]). **[V]**
- **Mobile and desktop re-release (2015–2016):** published as "PeaceMaker: Israeli Palestinian Conflict" on:
  - iOS, App Store id1019894712
  - Mac App Store, id1019906351
  - Google Play, `com.impactgames.peacemaker.android`
  - Amazon/Kindle, ASIN B01AKHFHVE

  The store links come from the [live homepage][pmhome]. An Android listing shows version 1 updated 2016-02-04 ([APK4Fun][apk4fun], via search). Kill Screen (2016-02-01) said the game was "recently updated for iOS and Android" ([Kill Screen][killscreen]). The homepage shows a **"Steam – coming soon" badge**, but no PeaceMaker app turns up in Steam's store search, so a Steam release apparently never happened **[?]**. As of today, iTunes lookup returns nothing for both Apple ids, and the Google Play URL is 404, so the game has been **delisted** from both. The Amazon search URL embedded in the homepage filters on a $1.99 price ([homepage HTML][pmhome]), so a $1.99 Amazon price around Feb 2016 is plausible **[?]**. A Mac-store mirror lists the Mac build as free, 199 MB, in English, Arabic and Hebrew ([pcmacstore][pcmac]). **[V]** for platforms and ids.
- **Planned "2.0":** in 2014 Brown was updating the game for current events and mobile. Planned changes included new inciting incidents: a Gaza shelling with civilian casualties on the Palestinian side, and a kidnapping or a tunnel discovered into Gaza in place of suicide bombs on the Israeli side ([Mother Jones 2014][mj]). In 2012 ImpactGames also described a planned mobile version and an "easy to use game builder" for making other games on the same "patent pending" platform ([ImpactGames PeaceMaker page][igpm]). **[S]**
- **Languages:** English, Hebrew and Arabic. The language is chosen at install or in settings ([settings.pm][settings]; [Adams][adams]; [APK4Fun][apk4fun]). **[V]**
- **Rating and audience:** not ESRB-rated; ImpactGames called it "PG-13 equivalent" because of real violent footage. Target audience: "socially aware adults and teenagers", including high schools, colleges and community groups ([Macworld][macworld]). The CGI player guide says ages 13+ and 1–2 hours ([CGI 2014 guide][cgi2014]). **[V]**

### Awards and distribution
- Awards and honours ([ImpactGames PeaceMaker page][igpm]; [CGI 2012 guide][cgi2012]): **[V]**
  - USC "Reinventing Public Diplomacy through Games": first place, 2006-05-08
  - Ashoka Changemakers "Entrepreneuring Peace": finalist, Jan 2007
  - Games for Change "Best Transformation Game": winner, 2007-06-27
  - I/ITSEC Serious Games Showcase & Challenge: finalist, 2007-10-14
  - INDEX "Design to Improve Life", Play category: finalist, 2009
- **Peres Center distribution (Nov 2007, timed to the Annapolis summit):** the reported numbers differ.
  - [Wikipedia][wiki-en]: 100,000 copies (75k to Haaretz subscribers, 10k to Al-Quds subscribers, 15k to schools).
  - [Hadassah 2008][hadassah] and [Google Arts & Culture][gac]: 80,000 copies via the two newspapers.
  - [Gamasutra 2013][gd2013]: about 100k purchased, 80k given out with newspapers and 20k kept for school workshops.

  Workshops in Israeli and Palestinian schools followed the distribution, combining play with guided dialogue. Wikipedia reports 50+ workshops and 1,600 students in 2008, rising to about 3,000 by Sept 2009; Hadassah reports 22 workshops and about 660 Israeli teens by mid-2008. **[V]** that this happened; **[?]** on the exact counts.
- **Sales:** 100,000 copies worldwide by Feb 2008 per [Wikipedia][wiki-en], possibly counting the Peres purchase. Sold in "over 60 countries" ([ImpactGames][igpm]; [Hadassah][hadassah]). Briefly #2 PC game on Amazon in July 2007 after the NPR segment ([Wikipedia][wiki-en]). **[S]/[?]**
- ImpactGames' own 2009 media kit describes PeaceMaker as a "long form (4–8 hrs of gameplay) strategy game platform" for "visualizing multiple perspectives on complex issues" ([ImpactGames media kit][mediakit]). **[S]**
- The follow-up product, **Play the News** (Feb 2008), was a web newsgame platform. Each game is an inciting incident, then context, then a decision with advisors, then feedback, followed by a prediction of what the real leader will do ([Educational proposal 2009][edprop]; [Wikipedia][wiki-en]). It shows how ImpactGames abstracted the PeaceMaker loop.

---

## (b) Core loop & mechanics

1. **Choose a side.** The main menu offers "Play as": Palestinian President, Israeli Prime Minister, **Play random side** (dice icon) and **Tutorial** (main-menu screenshot in [Alhabash & Wise 2012][alhabash]; [wiki-fr][wiki-fr] image description). The player also picks a difficulty: Calm, Tense or Violent ([Alhabash & Wise][alhabash]; [Hadassah][hadassah]). The leaders are deliberately anonymous, unnamed and male ([Greater Good][greatergood]; [Daily News Egypt/AFP 2007][dne]). **[V]**
2. **Intro and briefing.** An archival montage covers the conflict from 1948 (or earlier) to the present ([Gamepressure review text][gamepressure]; [Schneider & Goodrich 2010][schneider]; [Kamil 2025][kamil]; [Kill Screen][killscreen]). The opening news ticker uses headlines in the game's style ([homepage ticker][pmhome]; quoted in [Kamil][kamil]). A "Welcome to your new role" memo frames the job; as Israeli PM, "you are responsible for balancing Israeli and Palestinian approval" ([NPR 2007][npr]). **[V]**
3. **Inciting incident.** The first thing on the map is a crisis:
   - Israeli PM: a West Jerusalem suicide bus bombing, 18 killed and 100+ injured ([NPR][npr]; also [Kotaku][kotaku]).
   - Palestinian President: "18 Palestinians killed and 40 wounded by Israeli tank fire", on the game's start date of 30 Dec 2006 (screenshot in [Alhabash & Wise][alhabash]; event cited by [Kamil][kamil]). **[V]**
4. **Turn = one week; one action per turn.** The player picks a single action from Security, Political or Construction (each with sub-options), then time advances ("skip the week") ([NPR][npr]; [Eurogamer][eurogamer]: "week-long turns sandwiched between events phases"; [WPI][wpi]; [A.V. Club][avclub]; [Gamepressure review][gamepressure]). Hadassah writes "a limited number of" moves per week, and Adams's pre-release build allowed an action "every few days" ([Adams][adams]). The game advances only when the player acts ([Schneider & Goodrich][schneider]). **[V]**
5. **Resolution and feedback.** The action may succeed, partly succeed, fail, or be refused by the other actor. Example: as Israeli PM, offering medical aid right after an army deployment gets rejected because "no one believes that such an effort is genuine". Burak described this as the game having "a memory" ([NPR][npr]). Score deltas show immediately per side; one figure shows +4 Israeli and −17 Palestinian ([Nicolaidou & Kampf 2024][nic2024]). Each Groups & Leaders thermometer gets an up or down trend arrow ([wiki-fr][wiki-fr]). **[V]**
6. **Events phase.** Between turns, events appear as blinking red markers or crosshairs on cities; clicking one opens a news report with photo, text and a "Watch Event" video (see §e). The player can respond or ignore ([Schneider & Goodrich][schneider]; [Daily News Egypt][dne]). **[V]**
7. **Information actions that do not consume the turn:**
   - advisors (an "? Advisor" button inside each action dialog)
   - Groups & Leaders thermometers and the Polls tab
   - clickable map features (e.g., a "Green Line" glossary popup) and a zoom-out button
   - a 1920s–2000s illustrated **Timeline**, opened from a book icon

   Sources: screenshots in [Alhabash & Wise][alhabash]. A WPI reviewer accidentally spent turns by clicking icons he took for information tabs ([WPI][wpi]). **[V]**
8. **Repeat until win or loss.** There is apparently no turn limit (see §f).

**Constraints on actions (the "friction" systems):**
- **Anti-repetition / cooldowns.** Players cannot keep speaking to the same group or keep asking the adversary for meetings; a warning says constituents are tired of speeches, or that the other side wants to see policy before another meeting ([Schneider & Goodrich][schneider]). Eurogamer describes a "cool-off period" that the player cannot see, so actions that look available bounce back with "come back later" ([Eurogamer][eurogamer]). Exact repeats in a row are blocked, but alternating cycles are allowed ([Mechanics of Magic 2024][mom]). **[V]**
- **Prerequisites and unlocks.** New options open as stability and support grow. As Palestinian President, examples are opening borders to tourism, declaring independence, and requesting control of Gaza airspace ([Schneider & Goodrich][schneider]). The Palestinian Authority starts without control of its airspace, coast or water table, which locks development projects. It also lacks money, so it must lobby partners abroad to unlock options ([Mechanics of Magic][mom]). Early unilateral declarations of statehood are cancelled by the game ([Kamil][kamil]). **[V]**
- **Hidden success conditions.** Actions often fail because of unstated requirements such as high domestic support. Burak: you are penalized "for making concessions when you don't have the support to make concessions" ([Metacritic user review][metacritic]; [Hadassah][hadassah]). Adams's targeted assassination as Palestinian President first "fizzled", with only an old woman and a girl found at the target's home ([Adams][adams]). **[V]**
- **Budget and resources.** The Israeli PM can fund projects directly. The Palestinian President must request money from the UN, EU, US, Egypt, Jordan and others, and these requests are often refused; the self-funding option starts greyed out ([Eurogamer][eurogamer]; [Mechanics of Magic][mom]; [Schneider & Goodrich][schneider]; [Kamil][kamil]). The UI shows little about "money left in the coffers" ([A.V. Club][avclub]). **[V]** that the constraint exists; **[?]** how it is modelled.

---

## (c) Sides, stakeholders & meters

### Two headline scores (asymmetric by side)
| Side | Score 1 | Score 2 | Source |
|---|---|---|---|
| Israeli Prime Minister | **Israeli approval** | **Palestinian approval** | desktop screenshot in [Alhabash & Wise][alhabash] and [wiki-fr][wiki-fr]; [Adams][adams] |
| Palestinian President | **National approval** (Palestinian public) | **World approval** (international community) | screenshots in [Alhabash & Wise][alhabash]; [Adams][adams]; [Greater Good][greatergood] |

Both scores start at 0 and are shown as "n/100" ([Adams][adams]; screenshots). On mobile they appear as flag icons with n/100 (Israeli flag and Palestinian flag; Palestinian flag and a world-map icon) ([homepage image][pmimg]; [Nicolaidou & Kampf][nic2024] Fig. 1). Adams guessed the reason for the asymmetry: Palestine "will really be a nation when the rest of the world considers it to be one" ([Adams][adams]). **[V]**

The research literature describes each score as computed from the polls and the satisfaction of groups ("calculated by a function within the game"). The developers set score deltas through tests with international experts ([Cuhadar & Kampf 2014][ck2014]). **[S]**

### "Groups and Leaders" panel: eight actors per side, each with a thermometer
Each actor has a blue-to-red vertical thermometer with a trend arrow ([wiki-fr][wiki-fr]; screenshots). Each also has a "degree" of approval reflecting its own agenda ([Schneider & Goodrich][schneider]). Press texts say the player "interacts with eight other political leaders and social groups" ([Spong press text][spong]; [Infopackets quoting peacemakergame.com][infopackets]; [Metacritic summary][metacritic]); Macworld calls them "eight internal and external actors" ([Macworld][macworld]). **[V]**

| # | Israeli PM's panel (screenshot order) | Palestinian President's panel |
|---|---|---|
| 1 | Israeli public | Palestinian public |
| 2 | Settlers (Yesha Council) | Fatah |
| 3 | Palestinian President / Palestinian Authority | Hamas |
| 4 | Palestinian public | Israeli Prime Minister / government |
| 5 | Palestinian militant groups (Islamic Jihad, Izz ad-Din al-Qassam Brigades, al-Aqsa Martyrs' Brigades) | Israeli public |
| 6 | United Nations | United Nations |
| 7 | United States | United States |
| 8 | Arab world | Arab world |

Sources: [Wikipedia][wiki-en]; [wiki-fr][wiki-fr] image description; screenshots in [Alhabash & Wise][alhabash]. **[V]** for the composition; **[?]** for the order on the Palestinian side.

Other actors appear as advisors, funders or event sources but not, as far as I can tell, as thermometers:
- the European Union, Egypt and Jordan, as funders and mediators ([Eurogamer][eurogamer]; [Adams][adams]; [Digitally Downloaded][dd]). Hadassah lists the EU among the tabs ([Hadassah][hadassah]) **[?]**.
- the Knesset, which can criticize the PM (one message called the player's moves a "comedy of errors") ([Greater Good][greatergood])
- the army, which can revolt when settlements are removed ([Broken Toys][brokentoys])
- the "Israeli Left" and "Orthodox settlers" as separate constituencies ([Greater Good][greatergood])
- Iran, in news items ([Kill Screen][killscreen])

### "Polls" tab
Each side has a set of poll indicators, colour-coded green for positive and red for negative ([CGI 2012 guide][cgi2012]). Sources describe them differently. **[?]**
- [Wikipedia][wiki-en]: each leader sees their **leadership** and the **quality of relations** with the other side. Palestinian polls: **authority of the President**, ordinary Palestinians' **opinion of Israel**, **economic health**, **independence**. Israeli polls: **insecurity**, **suppression** (of Palestinians/militancy) and Israeli **compassion** for Palestinians.
- [Schneider & Goodrich][schneider]: polls track the nation's **economy, leadership, sympathy and cooperation**. They feed the overall score, and the need for an initiative affects whether it succeeds.
- [Hadassah][hadassah]: Israelis care most about security and suppressing militancy; Palestinians about economics and independence.
- Palestinian-side poll icons in screenshots: six icons ([Alhabash & Wise][alhabash]).

### Advisors
- Israeli PM: a **hawk** and a **dove**, pulling in opposite directions. Example: the hawk says send the army for security; the dove warns troops hurt Palestinian quality of life ([NPR][npr]; [Wikipedia][wiki-en]). **[V]**
- Palestinian President: a **national** advisor and a **foreign** advisor ([Wikipedia][wiki-en]). Domestic and international advice differ ([Schneider & Goodrich][schneider]). **[S]/[V]**
- Advisors explain some actions but not all ([WPI][wpi]). **[S]**

---

## (d) Actions catalog (as complete as public sources allow)

Officially there are about **20 role-based actions** in three categories, **Security, Political and Construction**, each "branching into a variety of sub-categories (e.g., checkpoints, speeches)" ([Macworld press text][macworld]; [Cuhadar & Kampf][ck2014]; [Chais 2012][chais2012]). The Palestinian President has about a third fewer options than the Israeli PM ([chesnok 2007][chesnok]). **[V]** for the structure; **[S]** for "a third fewer".

Desktop UI: the left column has icons for **Security** (a tank for Israel, a rifle for Palestine), **Political** (a podium or microphone), **Construction** (a hammer) and **Timeline/Info** (a book). Opening Political as Israeli PM shows a bar of sub-category icons:
- a microphone labelled "אבג" (speech in Hebrew, to Israelis)
- a microphone labelled "ABC" (speech in English, to the world)
- the Israeli flag
- the settler (Yesha) flag
- the Palestinian flag
- a globe (international)
- a newspaper/document icon
- a hard hat
- a peace symbol

The icons are confirmed by screenshots ([Alhabash & Wise][alhabash]; [Schneider & Goodrich][schneider] "Option Bar with Diplomatic Options Extended"; [wiki-fr][wiki-fr]). What each icon does beyond the speeches is **[?]**. Mobile collapses this into an "Actions" menu with Security / Political / Construction ([homepage image][pmimg]; [Nicolaidou & Kampf][nic2024]).

The table below lists every specific action named in sources. Placing an action in a category is my inference unless a source states it.

### Israeli Prime Minister
| Category | Action (as described) | Sources |
|---|---|---|
| Security | Send army units, choosing an objective (e.g., "securing the area") | [NPR][npr] **[V]** |
| Security | Withdraw the army or reduce deployments | [Adams][adams]; [wiki-fr][wiki-fr]; [Kill Screen][killscreen] |
| Security | Missile or air strikes, incl. Apache helicopter strikes | [Adams][adams]; [Kotaku][kotaku]; [Hadassah][hadassah]; [Broken Toys][brokentoys] |
| Security | Targeted killings / assassinations of militants | [Hadassah][hadassah]; [GamesRadar][gamesradar]; [A.V. Club][avclub] |
| Security | Ground operation against militant infrastructure; raid Gaza; send the military into Gaza | [Kotaku][kotaku]; [Hadassah][hadassah]; [Mother Jones][mj] |
| Security | Impose, tighten or ease curfews | [Adams][adams]; [Eurogamer][eurogamer]; [wiki-fr][wiki-fr] |
| Security | Add or remove checkpoints and roadblocks; border controls | [Eurogamer][eurogamer]; [Mother Jones][mj]; [Mechanics of Magic][mom]; [Greater Good][greatergood] |
| Security | More police patrols on Israeli streets | [Hadassah][hadassah]; [Greater Good][greatergood] |
| Security | Arrests (Israeli militants and settler leaders; "the most they can do is arrest them") | [Adams][adams]; [Walla][walla] |
| Security | Bulldoze or demolish Palestinian homes | [Adams][adams]; [Eurogamer][eurogamer]; [Schneider & Goodrich][schneider] |
| Security? | Build the separation wall/fence (incl. along the 1967 line) or remove sections | [Broken Toys][brokentoys]; [Mechanics of Magic][mom]; [Eurogamer][eurogamer]; [Hadassah][hadassah] |
| Security? / Political? | Remove or dismantle settlements; crack down on settlers; expand settlements | [Broken Toys][brokentoys]; [Mechanics of Magic][mom]; [Kill Screen][killscreen]; [Kamil][kamil]; [Hadassah][hadassah] |
| ? | Release Palestinian prisoners (added on Eisenberg's advice) | [Greater Good][greatergood]; [Hadassah][hadassah]; [Kamil][kamil] |
| Political | Speech to the Israeli public (Hebrew) / to the world (English); speeches on peace and compromise | screenshots; [Greater Good][greatergood] |
| Political | Increase work permits for Palestinians; reduce trade restrictions | [Mother Jones][mj]; [Schneider & Goodrich][schneider]; [Adams][adams] |
| Political | Meet or negotiate with the Palestinian President; coordinate with the US; pressure the Palestinian counterpart | [Walla][walla] (Yatom); [Kill Screen][killscreen]; [gcores][gcores] |
| Political | Cultural or cross-cultural initiatives (e.g., orchestra performances) | [Mechanics of Magic][mom] |
| Construction | Medical, educational or infrastructure aid to Palestinians; aid to refugee camps; reconstruction aid | [NPR][npr]; [Greater Good][greatergood]; [Mother Jones][mj]; [Schneider & Goodrich][schneider]; [Adams][adams] |
| Construction | Domestic economic stimulus packages; tax breaks; aid to the elderly | [Kill Screen][killscreen]; [Mechanics of Magic][mom]; tax breaks and elderly aid from a search summary **[?]** |

### Palestinian President
| Category | Action (as described) | Sources |
|---|---|---|
| Security | Build up or deploy the police force; police sweeps against Hamas leaders | [Broken Toys][brokentoys]; [Mother Jones][mj] |
| Security | Arrest all known militants | [Schneider & Goodrich][schneider] |
| Security | Ask Israel for joint work with Israeli police | [Schneider & Goodrich][schneider] |
| Security | Assassinate Palestinian militants (risks civil war if your support is low) | [Adams][adams]; [A.V. Club][avclub] |
| Security (blocked) | Restrict access to holy sites in Jerusalem (shown but unavailable) | [Kamil][kamil] screenshot caption |
| Political | Speech to the Palestinian people, on **Pro Law and Order / Pro Reconstruction / Anti Violent Resistance / Pro Violent Resistance** | screenshot in [Alhabash & Wise][alhabash] and [wiki-fr][wiki-fr] **[V]** |
| Political | Speeches to the world or the UN ("making nice speeches"); aggressive speeches are the President's only overt "military" option | [Digitally Downloaded][dd]; [Broken Toys][brokentoys]; [Adams][adams] |
| Political | Negotiate with Fatah (incl. a **"Bribe"** option) and with Hamas; ask either for cooperation or concessions | [Broken Toys][brokentoys]; [Digitally Downloaded][dd]; [Schneider & Goodrich][schneider] |
| Political | Demand that Israel withdraw or stop military action; request travel or trade concessions | [Broken Toys][brokentoys]; [Gulf News/AFP][gulfnews]; [Eurogamer][eurogamer] |
| Political | Request funds or loans (UN, EU, US, Egypt, Jordan); seek mediation | [Eurogamer][eurogamer]; [Adams][adams]; [Digitally Downloaded][dd]; [Kamil][kamil] |
| Political | Request joint cultural activities | [Schneider & Goodrich][schneider] |
| Political | "Offer thanks" (to Israel/donors) | [Broken Toys][brokentoys] |
| Political (gated) | Declare independence; request control of Gaza airspace; open borders to tourism (each needs stability or support) | [Schneider & Goodrich][schneider]; [Kamil][kamil] |
| Construction | Infrastructure projects (e.g., roads funded by a US loan); social and welfare programs; economic reconstruction | [Digitally Downloaded][dd]; [Hadassah][hadassah]; [Eurogamer][eurogamer] |
| Construction | "Agricultural, industrial and commercial construction" | search-engine summary attributed to MobyGames (page 403) **[?]** |

### Speech sub-system
Speeches appear to work in two steps: choose the audience (domestic or international), then choose a topic. A 2023 Chinese write-up adds a choice of tone (demanding/aggressive, hopeful/encouraging, or cautious "muddling-through") before the topic ([gcores][gcores]). **[S]**

### Absent by design
- The Palestinian President cannot order attacks on Israel, suicide bombings or rocket fire, or organize mass protests. These happen only as scripted events ([Adams][adams]; [Hadassah][hadassah]).
- Neither side can invade or annex. There are no foreign invasions and no "greater Israel" or "full liberation" outcomes ([Metacritic user review][metacritic]). **[V]**

---

## (e) Events / news / escalation system

- **Presentation.** Events appear on a stylized 3D map of Gaza, the West Bank, Israel and the northern Negev as red crosshairs or blinking dots on cities. Clicking opens a **"NEWS REPORT"** window with a headline, a real photo, short text and a **"Watch Event"** button that plays real footage ([Alhabash & Wise screenshot][alhabash]; [NPR][npr]; [Wikipedia][wiki-en]; [GamesRadar][gamesradar]). The 2016 trailer description mentions clips from ABC, Al-Jazeera and Israel's Channel 2 ([YouTube trailer][yt]). The CGI guide calls these "Playing the News" segments ([CGI 2012][cgi2012]). **[V]**
- **Content mix.** Events are positive, neutral or negative ([Schneider & Goodrich][schneider]; [Adams][adams]). Examples:
  - suicide bus bombings
  - Israeli tank fire killing civilians
  - militants killed in raids
  - settlers demanding expansion, or extremist settler violence
  - mass demonstrations and right-wing protests against police (after the PM arrests settler leaders)
  - a citizens' petition demanding the PM's removal
  - UN reports calling refugee-camp conditions catastrophic
  - a settlement security officer killed near the fence
  - Knesset criticism

  Sources: [Gamepressure review][gamepressure]; [Adams][adams]; [Walla][walla]; [Greater Good][greatergood]; [Kamil][kamil]; [Mechanics of Magic][mom]. Early press called the violent ones "**black events**" ([NBC/AP 2006][nbc]). **[V]**
- **Headline style.** Opening-ticker examples: "Report Shows UN Concern for Palestinians", "Israeli Prime Minister's Support Slipping", "Militant Killed During Raid", "Government Supports Peace Plan", "Security Measures Doing Their Job", "Police Criticised over Prison Policy", "Israel Imposes Curfew", "President Co-operates with Militants", "Palestinian Compatriots Aid Delayed", "Gaza Approaches Independence" ([live homepage ticker][pmhome]; reproduced in [Kamil][kamil]). **[V]**
- **Authenticity.** Most events are drawn from real incidents and use real images ([Gamepressure review][gamepressure]; [Adams][adams]). Kamil could not match some casualty figures to real events, so the events are "semi-real" ([Kamil][kamil]). **[V]**
- **Reactivity.** Interest groups respond depending on the recent context as well as the player's choice ([Gamepressure review][gamepressure]). The other side can refuse offers, as in "your request rejected" or the aid called "arrogant" ([NPR][npr]; [Greater Good][greatergood]). Events can follow your concessions; for example, Hamas asks are often followed by an attack on Palestinians by soldiers or settlers ([Schneider & Goodrich][schneider]). In 2006 the CMU description warned that "making too many concessions may set an assassination plot into motion" ([CMU 2006][cmu2006]; [NBC][nbc]). Whether assassination survives as a release mechanic is **[?]**.
- **Do responses to events matter?** A 2024 Stanford course playtest found that responding to events seemed to bring no benefit and ignoring them brought no penalty, so events worked as emotional punctuation rather than as dynamics ([Mechanics of Magic][mom]). Burak's advice, by contrast: "know when to ignore things and when to respond" ([Daily News Egypt/AFP][dne]). **[?]** (possibly a difference between versions)
- **Escalation and de-escalation.** At higher difficulty, a single checkpoint firefight, air raid or botched anti-militant operation can wipe out months of goodwill. Eurogamer called it a "one step forward, one step back" feel ([Eurogamer][eurogamer]). Playing well produces "a slow but meaningful reduction in violence over time" ([Mechanics of Magic][mom]). Burak says the game is hardest at the start and gets easier as you untangle it, because extremists try to derail early progress ([Kotaku][kotaku]). **[V]**

---

## (f) Win / loss conditions & scoring

- **Win.** Both headline scores must reach **+100** ([NPR][npr]; [Adams][adams]; [Kill Screen][killscreen]; [Cuhadar & Kampf][ck2014]; [Nicolaidou & Kampf][nic2024]). **[V]**
- **Milestones.** Progress runs through **four milestones** before the two-state solution. The save/resume screen reads "You have achieved milestone 0 of 4", and the win screen "You achieved the maximum milestone 4 of 4" ([Nicolaidou & Kampf][nic2024] Figs. 2–3). Schneider & Goodrich: "players must complete four milestones before they can reach a two-state solution", achieved through approval ratings ([Schneider & Goodrich][schneider]). Eurogamer mentions intermediate "peace milestone" screens with photos ([Eurogamer][eurogamer]). **[V]** that milestones exist; **[?]** for the thresholds (25/50/75/100 is a guess).
- **Win screen (mobile).** Shown as an "INTERNAL BRIEF – FROM: Director General, Prime Minister Office, Jerusalem" under the heading **"YOU WIN: TWO-STATE SOLUTION"**. The player and their counterpart win the **"PeaceMaker Medal"**, **Jerusalem serves as capital of both states**, and **joint Israeli–Palestinian security forces** implement the settlement ([Nicolaidou & Kampf][nic2024] Fig. 3; text quoted in [Kamil][kamil]). Desktop-era sources describe the reward as the **Nobel Peace Prize** ([Adams][adams]; [Macworld][macworld]; [Walla][walla]; [Schneider & Goodrich][schneider]; "Nobel Prize Winner" in [Alhabash & Wise][alhabash]). **[V]**
- **Secondary end-of-game rating.** At the end the game shows a **"violence" rating**. One player scored 63 on a scale that seemed to exceed 250, with a nudge to try less violent means next time ([chesnok 2007][chesnok]). A 2023 write-up describes an end-of-game report scored by the **average regional tension** over the game ([gcores][gcores]). **[V]** that it exists (two independent sources); **[?]** for the formula.
- **Loss: two failure modes.**
  1. **Removed from office by your own side**, described as voted out, a no-confidence vote, or impeachment ([Schneider & Goodrich][schneider]; [Gulf News][gulfnews]; [Mother Jones][mj]; [Kamil][kamil]; [WPI][wpi]).
  2. **A Third Intifada**, when the other public's opinion (for the Israeli PM, Palestinian opinion) collapses ([Hadassah][hadassah]; [Kotaku][kotaku]; [Walla][walla]).

  Schneider & Goodrich sum it up as "defeat in an election or setting off violence". Kamil claims the failure for the Palestinian President is Intifada/insurrection, while the Israeli PM is impeached ([Kamil][kamil]). Which failure fires for which score on the Palestinian side is **[?]**. The WPI analysis says over-escalating as Israel ends with a message that the situation is "unsalvageable", and that the game cuts off "without warning" ([WPI][wpi]).
- **Score range and loss threshold: conflicting evidence. [?]**
  - **−50 to +100, lose at −50:** Adams, who played a pre-release build in Jan 2007 ([Adams][adams]), and Kampf & Cuhadar ([Chais 2012][chais2012]; [Chais 2015][chais2015]; [PAXsims][paxsims]). The ISP 2014 and SSCR 2024 PDFs print "below 50", most likely a lost minus sign, since the same PDFs also drop the minus in "(−17 points)" ([Cuhadar & Kampf][ck2014]; [Nicolaidou & Kampf][nic2024]).
  - **−100 to +100:** Schneider & Goodrich ("two scores that range from 100 to −100") ([Schneider & Goodrich][schneider]); Wikipedia EN and FR ([wiki-en][wiki-en]; [wiki-fr][wiki-fr]); a Forward article cited in search results, with "−100 'war criminal' to +100 'Nobel Prize winner'" ([Forward, via search][forward]).
  - **Primary evidence:** the official desktop screenshot used by Wikipedia shows **Israeli approval 9/100 and Palestinian approval −60/100** on 6 Jan 2007, one week into a game, with no game over ([Alhabash & Wise][alhabash]; [wiki-fr][wiki-fr]). A Palestinian-side screenshot shows national approval at −32. So in at least one shipped build a score below −50 did not end the game at once. Possible explanations: the threshold changed between versions, it depends on difficulty, the loss only triggers on certain checks or events, or −50 was a pre-release value. **This needs checking in the binaries.**
- **Time limit.** Marketing copy still says "bring peace … before your term in office ends" ([APK4Fun store text][apk4fun]; [Google Arts & Culture][gac]). That phrase comes from the 2005 prototype's design ([peacegames blog 2005][pgblog]). Reviewers of the shipped game report no deadline and no elections: "unlimited amount of time" ([Kill Screen][killscreen]). Calev Ben-David praised the absence of a time limit as more realistic ([Wikipedia][wiki-en]). **[?]** Probably no hard turn limit in release.
- **History of the victory condition.** The team first avoided defining an end state; victory meant **reducing violence**. Early players wanted "a more meaningful outcome", so the team adopted the **two-state solution** after consulting experts from both sides and the US, citing UNSC resolutions, the Road Map and the Arab Peace Initiative (Burak blog post "Two-State Solution", 2007-05-04, and Sweeney "Design Assumptions", 2006-12-22, as summarized by [Wikipedia][wiki-en]). The stated design assumptions:
  - both sides want peace
  - the player can make a difference but does not fully control their own side
  - peace comes through small concrete steps

  Burak (2014): "Our game assumed that the solution exists and is fully understood" ([Kotaku][kotaku]). **[V]** (Wikipedia summary plus Burak's own article)
- **Kill Screen bug.** On the hardest setting, deliberately extreme pro-Palestinian play as Israeli PM did not get the player removed. Instead the game hung in a loop replaying a terror-attack video ([Kill Screen][killscreen]). **[S]**

---

## (g) Difficulty

- There are three levels, **Calm, Tense and Violent**, chosen at the start ([Hadassah][hadassah]; [APK4Fun][apk4fun]; [Cuhadar & Kampf][ck2014]). Marketing line: "Depending on what you bring to the table, we have three difficulty levels" ([Gamepressure][gamepressure]). **[V]**
- **What changes:** the **frequency of events beyond the player's control** ([Cuhadar & Kampf][ck2014]; [Nicolaidou & Kampf][nic2024]; [WPI][wpi]; [Schneider & Goodrich][schneider]). Gonzalez & Czlonka describe the frequency of "AI actions" as highest on Violent and lowest on Calm ([Gonzalez & Czlonka 2010, via search summary][gc2010]). Eurogamer says keeping everyone happy is easy on low settings and "murder" on high ones, because single incidents erase goodwill ([Eurogamer][eurogamer]). Whether severity or score deltas also scale is **[?]**.
- **Observed difficulty.** Win rates are low at Calm and lower above it:
  - Cuhadar & Kampf (167 students, Calm, both roles): 33% won in one role, 11% in both ([Cuhadar & Kampf][ck2014]).
  - Kampf 2013 (Calm): **16 of 50 solo players won vs 19 of 25 mixed Jewish–Palestinian dyads** who had to agree on every move ([Chais 2013][chais2013]).
  - Nicolaidou & Kampf (30 minutes, Israeli role, Calm): 22 of 61 direct-party students won ([Nicolaidou & Kampf][nic2024]).
  - A CMU study reported by Mother Jones: about 40% never won in four tries, about half won one of four, 2% won all four, and on hard mode most "simply gave up" ([Mother Jones][mj], primary not seen). **[S]**
- **Side difficulty is disputed.**
  - Adams found Israel comparatively easy even on the hardest level because it has the most flexibility ([Adams][adams]).
  - Eurogamer found Israel harder ([Eurogamer][eurogamer]).
  - A student who won several times as the Palestinian President could never win as Israel ([Greater Good][greatergood]).
  - Brown says neither side is harder, only different: Palestinian play centres on infrastructure, while on the Israeli side you must avoid "viscerally reacting to the violence" ([Mother Jones][mj]).
  - Kill Screen won as Israel in about 20 minutes on its first try ([Kill Screen][killscreen]).
- **Session length.** ImpactGames' media kit says "4–8 hrs" ([media kit][mediakit]). Reported wins took 20 minutes to more than an hour ([Kill Screen][killscreen]; [chesnok][chesnok]; [Greater Good][greatergood]). The CGI guide says 1–2 hours ([CGI 2014][cgi2014]).

---

## (h) UI / UX

- **Desktop layout** (2007-era screenshots in [Alhabash & Wise][alhabash] and [Schneider & Goodrich][schneider]; [wiki-fr][wiki-fr] description):
  - the centre is a 3D map that can be zoomed, with clickable glossary features such as the Green Line
  - the left column holds action category icons (Security, Political, Construction, Timeline)
  - a pop-out sub-action bar
  - bottom-left: role name, date (MM DD,YYYY), and the two scores as n/100
  - bottom-right: tabs for **Groups and Leaders** (8 thermometers) and **Polls**
  - modal dialogs for actions, each with an "? Advisor" button and Close
  - a modal "News Report" window with "Watch Event"
  - a Timeline modal running from 1920 to the present, with photos and captions
- **Settings** include anti-aliasing, fade effects, fullscreen, music, sound effects, a **day/night cycle**, language and resolution (default 1024×768) ([settings.pm][settings]). **[S]**
- **Mobile layout** (2015–16):
  - top bar: a hamburger "ACTIONS" menu, the side's emblem plus the date (e.g., "Jan 14, 2015" or "September 14, 2015"), and a settings gear
  - expanded menu: Security, Political, Construction
  - bottom bar: "Groups & Leaders" | the two scores | "In the Polls"
  - a "Welcome back … Resume Current Game … milestone n of 4 … Score" screen
  - end-of-game "Internal Brief" reports

  Sources: [homepage device image][pmimg]; [Nicolaidou & Kampf][nic2024]. The in-game start date differs between builds: desktop games start 30 Dec 2006, while mobile screenshots show 2015 dates **[?]** (they may start on the current real-world date). Kamil notes a new game is shown as the next entry on the timeline ([Kamil][kamil]).
- **Map art.** Israeli cities are drawn with high-rises; Palestinian towns with stone buildings; settlements as small portable-building clusters. The map also shows the Green Line and parts of the barrier ([Kamil][kamil], critically). Kamil reads this as ideological ([Kamil][kamil]).
- **Music:** a Middle-Eastern-flavoured score ([Greater Good][greatergood]; [Metacritic user][metacritic]).
- **UX criticisms:**
  - the map is mostly decorative, used only to reach event reports ([Eurogamer][eurogamer]; [WPI][wpi])
  - the polls display is "needlessly atomised"
  - there is no message log, no sound options, rigid menus, and cooldowns are invisible ([Eurogamer][eurogamer])
  - the three-tab action split is confusing, action icons look like information icons, and some actions have no description ([WPI][wpi])
  - there is little information on order status, budget or territory status ([A.V. Club][avclub])
  - one negotiation was reported as a success while the icons showed relations falling ([Digitally Downloaded][dd])
  - first contact is easy and the interface clean ([Metacritic user][metacritic])

  There is an optional tutorial; otherwise the game gives no hints ([CGI 2012][cgi2012]).

---

## (i) Educational research findings

| Study | Sample / setup | Key findings relevant to design |
|---|---|---|
| Burak, Keylor & Sweeney 2005, INTETAIN ([Springer][intetain]) | Design/demo paper | Aimed at Israeli and Palestinian teens; built on commercial strategy-game conventions; argues playing for peace can be "as challenging and satisfying" as playing for war. |
| Gonzalez & Czlonka 2010, *Games for Peace: Empirical Investigations with PeaceMaker* ([IGI][gc2010]) | CMU Arab–Israeli history course; played at the start and end of the semester; actions logged | Identity variables (religion, politics, personal affiliation, trust) relate to scores. Performance improved about 19% over the semester. The raw number of actions does not separate good from bad players (via search summary) **[?]**. |
| Gonzalez, Saner & Eisenberg 2013, *Social Science Computer Review* 31(2) ([KiltHub][gse2013]) | US students, repeated games | Scores improved, and the correlations between score and religion or political affiliation shrank with practice: "learn to stand in another's shoes". |
| Gonzalez, Kampf & Martin 2012, *Computers in Human Behavior* 28(1) ([KiltHub][gkm2012]) | Israeli students, both roles | **Action diversity predicts success in both roles.** Israelis were less diverse as Israel than as Palestine. Religiosity and hawkishness predicted less diversity in the Palestinian role. Diversity mediates knowledge → success in the Israeli role. |
| Alhabash & Wise 2012, *Int. J. of Communication* 6 ([IJoC][alhabash]) | 68 US students, 20 minutes, one role | Playing the Palestinian President made explicit attitudes more favourable to Palestinians and less to Israelis. Playing the Israeli PM changed nothing. Implicit attitudes did not change. |
| Cuhadar & Kampf 2014, *International Studies Perspectives* ([PDF][ck2014]; [PAXsims summary][paxsims]) | 167 students (Turkish, Jewish-Israeli, American, Palestinian), Calm, both roles, English | Knowledge rose for all groups, most for third parties. Attitudes on core issues (Jerusalem, water, security, refugees, settlements, borders) did not change; third parties moved toward neutrality only on the then-recent Gaza operation. Prior knowledge predicted winning; support for a two-state solution did **not**. Jewish Israelis used the most security actions in the Palestinian role. (The PAXsims version says the Palestinians were from Bethlehem University; the ISP version says Palestinian citizens of Israel.) |
| Kampf 2013, Chais "Are two better than one?" ([PDF][chais2013]) | 100 Israeli female students (Jewish and Palestinian), singly or in mixed dyads holding opposing views | **Dyads won far more often (19/25 vs 16/50)** and took more diplomatic and fewer security actions. |
| Kampf & Cuhadar 2015, Chais ([PDF][chais2015]) | 307 students; PeaceMaker vs *Global Conflicts: Palestine* | PeaceMaker produced more knowledge gain. The street-level reporter game (Global Conflicts) produced more impartiality on core issues. |
| Schneider & Goodrich 2010, *Ohio St. J. on Dispute Resolution* 25:87 ([OSU KB][schneider]) | Law/ADR teaching | Uses PeaceMaker to teach two-level games, partisan perception, option devaluation, context dependence and decision regret. Recommends class-wide play on one screen, teams with a recorder, and replay at higher difficulty. |
| Nicolaidou & Kampf 2024, *SSCR* ([PDF][nic2024]) | 168 students (Jewish-Israeli, Palestinian, US, Cypriot), 30 minutes, Calm, Israeli role, mobile build | Direct parties learned more about "the other" and third parties more about the conflict. The game closed the knowledge gap between winners and losers among direct parties and widened it among third parties. |
| VOX-Pol 2025 (Kampf et al.) ([VOX-Pol][voxpol]) | 510 undergraduates, before and during the 2023–24 Israel–Hamas war | Women won no less than men before the war and more than men during it. |
| Kamil 2025, UC Irvine book chapter ([eScholarship][kamil]) | Critical close play | Argues the map, the event framing, the asymmetric failure modes and the two-state-only ending reproduce settler-colonial narratives. Proposes "subaltern" play. |

Classroom use: CMU, the Peres Center workshops, Dickinson College (journals and a 6–8 page strategy essay with a logged action/consequence table; "you do not have to win") ([Dickinson][dickinson]), and Marquette Law ([Marquette][marquette]). Teachers report students kept referring back to the game: "It's just like in the game" ([Hadassah][hadassah]; [Greater Good][greatergood]).

---

## (j) Reception & criticisms

**Scores and praise.** Metacritic 75 from 5 reviews; Eurogamer 7/10; PC Gamer UK 82% ([Wikipedia][wiki-en]). Other critic blurbs:
- PC Zone UK: "Timely, compelling, packed with features" ([Metacritic][metacritic])
- PC Format: "engaging, interesting"
- GamesRadar/PC Gamer: "fairly dry in terms of action" ([GamesRadar][gamesradar])
- Ernest Adams: "fun – challenging, tense at times"; a richer, non-zero-sum challenge than *Balance of Power* ([Adams][adams])
- Eurogamer: the reviewer was moved to tears by the peace-milestone photos ([Eurogamer][eurogamer])
- A long review syndicated on Gamepressure, possibly from Manifesto Games **[?]**, calls it "a multi-variable popularity model, with one action each turn", and compelling because of its real-world grounding ([Gamepressure][gamepressure])

Many reviewers praised its evenhandedness ([Eurogamer][eurogamer]; [WPI][wpi]; [Adams][adams]).

**Criticisms and wishes** (grouped, with what reviewers wanted instead):
1. **One "correct" path, dominant cycles, low replay value.** Once you find policies that work, you win; deviating gets punished ([WPI][wpi]; [A.V. Club][avclub]; [Metacritic user][metacritic]; [Mechanics of Magic][mom]: cycling civilian aid, cultural initiatives and stimulus wins "without ever addressing the truly thorny issues"). *Wish:* dynamics that stop static exploits.
2. **Inverse difficulty curve.** Unlocks make the late game easier ([Mechanics of Magic][mom]; Burak concedes it is "most difficult at its dawn" ([Kotaku][kotaku])). *Wish:* escalating challenges as peace nears, and timing of big moves.
3. **Events are emotionally powerful but mechanically inert** ([Mechanics of Magic][mom]).
4. **Opaque feedback and hidden rules**: invisible cooldowns, no log, no budget readout, inconsistent icons ([Eurogamer][eurogamer]; [A.V. Club][avclub]; [Digitally Downloaded][dd]). Kamil reframes this opacity as deliberate, a simulation of powerlessness ([Kamil][kamil]).
5. **Failure is abrupt and unexplored.** Hawks lose "in about five minutes flat" ([Adams][adams]; [WPI][wpi]). A Paradox-style player wanted to see the consequences of failure rather than a "third intifada game over screen" ([Metacritic user][metacritic]). Kill Screen wanted time pressure, elections, polarization effects, and the risk of a Rabin-style assassination; it found the model "cannot conceive of individuals acting in poor faith" ([Kill Screen][killscreen]).
6. **A single fixed end state (two states).** Players who oppose a two-state solution win just as often ([Cuhadar & Kampf][ck2014]), but the narrative forecloses alternatives ([Kamil][kamil]; [Metacritic user][metacritic]). Even the official discussion guide asks players, "Would you suggest a different ending?" ([CGI 2012][cgi2012]). A Columbia review reportedly says final-status issues (Jerusalem, refugees, borders) are missing ([Columbia, via search snippet][columbia]) **[?]**. Burak said they tried to cover refugees and Jerusalem so the game would "stay timeless" ([Daily News Egypt/AFP][dne]).
7. **Limited Palestinian agency.** The President cannot initiate violence, and Gaza and the West Bank are treated as one ([Hadassah][hadassah]; [Adams][adams]; [Kamil][kamil]). Electronic Intifada reportedly faulted the game for ignoring the Hamas electoral victory and Gaza takeover, the lack of a viable Palestinian political force, settlement and outpost growth, and checkpoints ([EI, via search snippet][ei]) **[?]**.
8. **Dated content.** The game predates the 2007 Hamas takeover of Gaza ([Hadassah][hadassah]; [Nicolaidou & Kampf][nic2024]).
9. **Realism disputes from practitioners.** Ex-Mossad head Danny Yatom played only military options, triggered an intifada, then called the game a failure at representing reality. He said he had also taken diplomatic steps ([Walla][walla]). A Labour-candidate general made a similar "nothing to learn" claim on Israeli TV ([Kotaku][kotaku]).
10. **The paid model was criticized** ([Wikipedia][wiki-en]; Prensky in [Greater Good][greatergood]).
11. **Engine wish:** a scenario editor so the engine could run other conflicts with user-defined factions and goals ([Marquette commenter][marquette]). ImpactGames itself planned a "game builder" ([ImpactGames][igpm]).

---

## (k) Open questions / unverified claims (to resolve from binaries or archives)

1. **Loss threshold and score floor**: −50 (Adams, Kampf) vs −100 (Schneider, Wikipedia, Forward). A shipped screenshot shows −60 with no game over. Does it vary by version or difficulty? Is a loss checked continuously or on events?
2. **Milestones**: what triggers each of the 4 milestones (score bands? specific actions such as a peace summit?), and what each milestone screen says. Eurogamer's "peace milestone" photos suggest scripted beats.
3. **Full action list per side and per category**, with costs, prerequisites, cooldown lengths, success chances and the "memory" or trust effects. Only about 40 named actions are documented above, against roughly 20 "role-based actions" (probably counted before sub-options).
4. **Poll variables per side** and how they feed the scores. Sources conflict.
5. **Which failure mode fires for which score on the Palestinian side** (removal vs intifada).
6. **End-of-game "violence"/tension rating**: its formula and range (one report says over 250).
7. **Difficulty**: event frequency only, or severity and score deltas too?
8. **Time**: is there a hidden term limit or turn cap? (Marketing says "term in office"; reviews say none.) What start date does each build use?
9. **Budget model**: does the Israeli side have a numeric budget? How is Palestinian funding tracked?
10. **Mobile 2015–16 content**: was the event set updated to the "2.0" inciting incidents Mother Jones described? (Screenshots show 2015 dates.) What did the mobile builds cost?
11. **Steam**: the "coming soon" badge exists, but I found no Steam release; unconfirmed.
12. **Archived official pages** (not reachable here): peacemakergame.com game/features/FAQ/educators pages and impactgames.com blog posts:
    - "PeaceMaker: Design Assumptions" (2006-12-22)
    - "PeaceMaker 1.0 in three languages" (2007-01-09)
    - "Why PeaceMaker costs money?" (2007-02-13)
    - "Two-State Solution" (2007-05-04)
    - "PeaceMaker package on Amazon" (2007-05-31)
    - "Important patch release to solve QuickTime issues" (2007-07-18)
    - "Movers and shakers on Amazon" (2007-07-21)
    - "PeaceMaker Free to Everyone!" (2013-11-04)
    - the Serious Games Source interview (2006-07-18)

    These would confirm the design-assumption list and the marketing claims verbatim.
13. **Category assignment** of prisoner release, settlements, the wall, work permits and trade restrictions, and the meaning of the unlabelled Political-bar icons (newspaper, hard hat, peace symbol).
14. **Sales and distribution counts** (80k vs 100k Peres copies; 100k sold "worldwide" vs "in Israel alone").
15. **Composer credit** (Ross Popoff vs Tina Blaine) and publisher (Manifesto Games) are single-source.

---

## Design takeaways for a multi-outcome successor (synthesis, not sourced claims)

- PeaceMaker already had the bones of graded outcomes: four milestones, a separate end-of-game violence/tension rating, and two distinct failure types (losing domestic legitimacy vs triggering mass violence). It shipped only one success state because playtesters wanted a "more meaningful outcome" than "violence went down".
- The main design debts are: a static payoff matrix that allows exploit cycles; events with no follow-on mechanical consequences; an inverse difficulty curve; opaque cooldowns, prerequisites and budget; and no actors acting in bad faith.
- Cooperative play deserves a look. Mixed-identity dyads who had to agree on every move won at roughly double the solo rate and chose more diplomacy ([Chais 2013][chais2013]). Action diversity predicted success ([Gonzalez, Kampf & Martin][gkm2012]).

---

## Sources

[wiki-en]: https://en.wikipedia.org/wiki/PeaceMaker
[wiki-fr]: https://fr.wikipedia.org/wiki/PeaceMaker
[adams]: https://www.gamedeveloper.com/design/the-designer-s-notebook-asymmetric-peacefare
[npr]: https://www.npr.org/transcripts/12056286
[paxsims]: https://paxsims.wordpress.com/2012/06/03/learning-about-the-israeli-palestinian-conflict-through-simulations-the-case-of-peacemaker/
[ck2014]: https://typeset.io/pdf/learning-about-conflict-and-negotiations-through-computer-4vkeibvbjh.pdf
[chais2012]: https://www.openu.ac.il/innovation/chais2012/downloads/f-Kampf-Cuhadar-14_eng.pdf
[chais2013]: https://www.openu.ac.il/innovation/chais2013/download/a1_3.pdf
[chais2015]: https://www.openu.ac.il/innovation/chais2015/c1_1.pdf
[nic2024]: https://ktisis.cut.ac.cy/bitstream/20.500.14279/33213/1/nicolaidou-kampf-2024-serious-games-knowledge-acquisition-and-conflict-resolution-the-case-of-peacemaker-as-a-peace.pdf
[gse2013]: https://kilthub.cmu.edu/articles/journal_contribution/Learning_to_Stand_in_the_Other_s_Shoes_A_Computer_Video_Game_Experience_of_the_Israeli_-Palestinian_Conflict/6571241
[gkm2012]: https://kilthub.cmu.edu/articles/journal_contribution/Action_diversity_in_a_simulation_of_the_Israeli_Palestinian_conflict/6570986
[gc2010]: https://www.igi-global.com/chapter/games-peace-empirical-investigations-peacemaker/41071
[intetain]: https://link.springer.com/chapter/10.1007/11590323_40
[alhabash]: https://ijoc.org/index.php/ijoc/article/view/1056
[schneider]: https://kb.osu.edu/handle/1811/76918
[kamil]: https://escholarship.org/uc/item/67w1d9h9
[voxpol]: https://voxpol.eu/?p=26689
[cmu2007]: https://www.cmu.edu/homepage/global/2007/fall/how-do-you-play.shtml
[cmu2006]: https://www.cmu.edu/homepage/innovation/2006/fall/teaching-the-complexities-of-conflict.shtml
[greatergood]: https://greatergood.berkeley.edu/article/item/digital_diplomacy
[wpi]: https://web.cs.wpi.edu/~rich/courses/imgd4600-c15/analyses/peacemaker/index.html
[mom]: https://mechanicsofmagic.com/2024/09/30/introducing-serious-games-peacemaker/
[killscreen]: https://killscreen.com/previously/articles/this-videogame-about-the-israeli-palestinian-conflict-makes-peace-uncomfortably-achievable/
[mj]: https://www.motherjones.com/media/2014/08/peacemaker-video-game-israeli-palestinian-conflict/
[hadassah]: https://www.hadassahmagazine.org/2008/08/02/letter-peace-front-fair-game/
[kotaku]: https://kotaku.com/what-i-learned-turning-the-israel-palestine-conflict-in-1612148555
[gd2013]: https://www.gamedeveloper.com/business/games-for-social-good-five-years-after-i-peacemaker-i-
[eurogamer]: https://www.eurogamer.net/peacemaker-review
[avclub]: https://www.avclub.com/peacemaker-1798211713
[gamesradar]: https://www.gamesradar.com/peacemaker-review/
[metacritic]: https://www.metacritic.com/game/peacemaker/
[brokentoys]: https://www.brokentoys.org/how-i-lost-the-peace-possibly-under-the-couch-a-peacemaker-review/
[dd]: https://www.digitallydownloaded.net/?p=46126
[chesnok]: https://www.chesnok.com/daily/2007/08/25/peacemaker-and-indie-educational-software/
[gcores]: https://www.gcores.com/articles/172607
[walla]: https://finance.walla.co.il/item/1092269
[gulfnews]: https://gulfnews.com/world/mena/new-pc-game-allows-middle-east-peace-1.176848
[dne]: https://www.dailynewsegypt.com/?p=103606
[macworld]: https://www.macworld.com/article/183529/peacemaker.html
[spong]: https://spong.com/article/12440/Gamers-To-Solve-The-Israeli-Palestinian-Crisis
[nbc]: https://www.nbcnews.com/id/wbna12423759
[legit]: https://www.legitreviews.com/?p=116503
[wired]: https://www.wired.com/2006/09/games-tackle-middle-east-conflict/
[infopackets]: https://infopackets.com/node/1588
[gamepressure]: https://www.gamepressure.com/games/peacemaker/ze1fa6
[apk4fun]: https://www.apk4fun.com/games/com.impactgames.peacemaker.android/
[pcmac]: https://pcmacstore.com/en/app/1019906351/peacemaker-israeli-palestinian-conflict
[moby]: https://www.mobygames.com/game/29652/peacemaker/
[igpm]: http://impactgames.com/peacemaker.php
[igabout]: http://www.impactgames.com/about.php
[pmhome]: http://www.peacemakergame.com/
[pmimg]: http://www.peacemakergame.com/img/PM-header-device-lg-actions.png
[s3]: http://download.peacemakergame.com/
[settings]: http://download.peacemakergame.com/patches/perez/english/settings.pm
[mediakit]: http://download.peacemakergame.com/ImpactGamesMedia.pdf
[edprop]: http://download.peacemakergame.com/ImpactGames_Educational_Proposal.pdf
[cgi2012]: https://gamesandimpact.org/wp-content/uploads/2012/09/PeaceMaker-Impact-Guide-for-Players-1_0.pdf
[cgi2014]: https://gamesandimpact.org/wp-content/uploads/2014/04/PlayersGuide_PeaceMaker_Final_2014_1_4.pdf
[gac]: https://artsandculture.google.com/asset/peacemaker/6wGB5iDw1oTVMA
[pgblog]: https://peacegames.blogspot.com/2005/11/peace-maker-video-game-to-teach-peace.html
[yt]: https://www.youtube.com/watch?v=WF8e4ROQJDM
[marquette]: https://law.marquette.edu/facultyblog/2010/04/so-you-think-you-can-bring-peace-to-the-middle-east/
[dickinson]: https://blogs.dickinson.edu/edtech/?p=248
[forward]: https://forward.com/israel/400/clicking-toward-middle-east-peace/
[columbia]: https://www.columbia.edu/cu/current/articles/fall2007/the-games-we-play.html
[ei]: https://electronicintifada.net/content/peacemaker/7329

**Plain URL list** (same sources, for non-markdown readers):

| Source | URL |
|---|---|
| Wikipedia EN | https://en.wikipedia.org/wiki/PeaceMaker |
| Wikipedia FR | https://fr.wikipedia.org/wiki/PeaceMaker |
| Adams, Gamasutra, 2007-01-31 | https://www.gamedeveloper.com/design/the-designer-s-notebook-asymmetric-peacefare |
| NPR transcript, 2007-07-18 | https://www.npr.org/transcripts/12056286 |
| Kampf & Cuhadar, PAXsims, 2012 | https://paxsims.wordpress.com/2012/06/03/learning-about-the-israeli-palestinian-conflict-through-simulations-the-case-of-peacemaker/ |
| Cuhadar & Kampf, ISP 2014 | https://typeset.io/pdf/learning-about-conflict-and-negotiations-through-computer-4vkeibvbjh.pdf |
| Chais 2012 | https://www.openu.ac.il/innovation/chais2012/downloads/f-Kampf-Cuhadar-14_eng.pdf |
| Chais 2013 | https://www.openu.ac.il/innovation/chais2013/download/a1_3.pdf |
| Chais 2015 | https://www.openu.ac.il/innovation/chais2015/c1_1.pdf |
| Nicolaidou & Kampf 2024 | https://ktisis.cut.ac.cy/bitstream/20.500.14279/33213/1/nicolaidou-kampf-2024-serious-games-knowledge-acquisition-and-conflict-resolution-the-case-of-peacemaker-as-a-peace.pdf |
| Gonzalez, Saner & Eisenberg 2013 | https://kilthub.cmu.edu/articles/journal_contribution/Learning_to_Stand_in_the_Other_s_Shoes_A_Computer_Video_Game_Experience_of_the_Israeli_-Palestinian_Conflict/6571241 |
| Gonzalez, Kampf & Martin 2012 | https://kilthub.cmu.edu/articles/journal_contribution/Action_diversity_in_a_simulation_of_the_Israeli_Palestinian_conflict/6570986 |
| Gonzalez & Czlonka 2010 | https://www.igi-global.com/chapter/games-peace-empirical-investigations-peacemaker/41071 |
| Burak, Keylor & Sweeney 2005 (INTETAIN) | https://link.springer.com/chapter/10.1007/11590323_40 |
| Alhabash & Wise 2012 | https://ijoc.org/index.php/ijoc/article/view/1056 |
| Schneider & Goodrich 2010 | https://kb.osu.edu/handle/1811/76918 |
| Kamil 2025 | https://escholarship.org/uc/item/67w1d9h9 |
| VOX-Pol | https://voxpol.eu/?p=26689 |
| CMU 2007 | https://www.cmu.edu/homepage/global/2007/fall/how-do-you-play.shtml |
| CMU 2006 | https://www.cmu.edu/homepage/innovation/2006/fall/teaching-the-complexities-of-conflict.shtml |
| Greater Good, 2006-03-01 | https://greatergood.berkeley.edu/article/item/digital_diplomacy |
| WPI analysis | https://web.cs.wpi.edu/~rich/courses/imgd4600-c15/analyses/peacemaker/index.html |
| Mechanics of Magic | https://mechanicsofmagic.com/2024/09/30/introducing-serious-games-peacemaker/ |
| Kill Screen, 2016-02-01 | https://killscreen.com/previously/articles/this-videogame-about-the-israeli-palestinian-conflict-makes-peace-uncomfortably-achievable/ |
| Mother Jones, Aug 2014 | https://www.motherjones.com/media/2014/08/peacemaker-video-game-israeli-palestinian-conflict/ |
| Hadassah, Aug 2008 | https://www.hadassahmagazine.org/2008/08/02/letter-peace-front-fair-game/ |
| Kotaku, 2014-07-28 | https://kotaku.com/what-i-learned-turning-the-israel-palestine-conflict-in-1612148555 |
| Gamasutra, 2013-01-11 | https://www.gamedeveloper.com/business/games-for-social-good-five-years-after-i-peacemaker-i- |
| Eurogamer | https://www.eurogamer.net/peacemaker-review |
| A.V. Club | https://www.avclub.com/peacemaker-1798211713 |
| GamesRadar | https://www.gamesradar.com/peacemaker-review/ |
| Metacritic | https://www.metacritic.com/game/peacemaker/ |
| Broken Toys | https://www.brokentoys.org/how-i-lost-the-peace-possibly-under-the-couch-a-peacemaker-review/ |
| Digitally Downloaded | https://www.digitallydownloaded.net/?p=46126 |
| chesnok | https://www.chesnok.com/daily/2007/08/25/peacemaker-and-indie-educational-software/ |
| gcores | https://www.gcores.com/articles/172607 |
| Walla | https://finance.walla.co.il/item/1092269 |
| Gulf News | https://gulfnews.com/world/mena/new-pc-game-allows-middle-east-peace-1.176848 |
| Daily News Egypt | https://www.dailynewsegypt.com/?p=103606 |
| Macworld | https://www.macworld.com/article/183529/peacemaker.html |
| Spong | https://spong.com/article/12440/Gamers-To-Solve-The-Israeli-Palestinian-Crisis |
| NBC/AP | https://www.nbcnews.com/id/wbna12423759 |
| Legit Reviews | https://www.legitreviews.com/?p=116503 |
| Wired | https://www.wired.com/2006/09/games-tackle-middle-east-conflict/ |
| Infopackets | https://infopackets.com/node/1588 |
| Gamepressure | https://www.gamepressure.com/games/peacemaker/ze1fa6 |
| APK4Fun | https://www.apk4fun.com/games/com.impactgames.peacemaker.android/ |
| pcmacstore | https://pcmacstore.com/en/app/1019906351/peacemaker-israeli-palestinian-conflict |
| ImpactGames PeaceMaker page | http://impactgames.com/peacemaker.php |
| ImpactGames About | http://www.impactgames.com/about.php |
| peacemakergame.com homepage (header, ticker and store links only; rest is spam) | http://www.peacemakergame.com/ |
| Homepage device image | http://www.peacemakergame.com/img/PM-header-device-lg-actions.png |
| Download bucket listing | http://download.peacemakergame.com/ |
| settings.pm | http://download.peacemakergame.com/patches/perez/english/settings.pm |
| ImpactGames media kit | http://download.peacemakergame.com/ImpactGamesMedia.pdf |
| ImpactGames educational proposal | http://download.peacemakergame.com/ImpactGames_Educational_Proposal.pdf |
| CGI player guide 2012 | https://gamesandimpact.org/wp-content/uploads/2012/09/PeaceMaker-Impact-Guide-for-Players-1_0.pdf |
| CGI player guide 2014 | https://gamesandimpact.org/wp-content/uploads/2014/04/PlayersGuide_PeaceMaker_Final_2014_1_4.pdf |
| Google Arts & Culture | https://artsandculture.google.com/asset/peacemaker/6wGB5iDw1oTVMA |
| peacegames blog, 2005 | https://peacegames.blogspot.com/2005/11/peace-maker-video-game-to-teach-peace.html |
| YouTube trailer | https://www.youtube.com/watch?v=WF8e4ROQJDM |
| Marquette Law blog | https://law.marquette.edu/facultyblog/2010/04/so-you-think-you-can-bring-peace-to-the-middle-east/ |
| Dickinson College | https://blogs.dickinson.edu/edtech/?p=248 |
| Forward (via search snippet only) | https://forward.com/israel/400/clicking-toward-middle-east-peace/ |
| Columbia (via search snippet only) | https://www.columbia.edu/cu/current/articles/fall2007/the-games-we-play.html |
| Electronic Intifada (via search snippet only) | https://electronicintifada.net/content/peacemaker/7329 |
| MobyGames (403; via search snippet only) | https://www.mobygames.com/game/29652/peacemaker/ |

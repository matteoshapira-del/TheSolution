# 10 · UI, UX and presentation

Reconstructed from the scene scripts (`PreGame`, `StartMenu`, `ActionHandler`, `ScoreBar`, `GroupLeaderWindow`,
`MapHandler`, `TimelineHandler`, `EndReportWindow`) and the interface XML.

## Flow

```
Studio slate ─► Start screen (New · Resume · Load · Save · Quit · language EN/עב/عر)
             ─► Play as: Israeli Prime Minister · Palestinian President · Random
             ─► Difficulty: Calm · Tense · Violent
             ─► Intro video ─► Welcome letter ─► Score explanation
             ─► Inciting-incident pin on the map ─► MAIN LOOP ─► Ending video ─► End report ─► Credits
```

## Main screen

* **Map** of Israel, the West Bank and Gaza (zoom and pan) with 27 clickable locations. News arrives as **pins**:
  red for violent or negative news, white for other news. You must open every pin before the action menu unlocks.
  A setting toggles the visible hit-areas of map locations.
* **Score bar**: the two `n/100` scores (internal and external) with up/down arrows.
* **Groups & leaders bar**: eight portraits, each showing an approval meter and its last change. Clicking one opens
  a dialog with a photo and a description.
* **Polls bar**: five or six "books" (security, sympathy… or economy, authority, independence…), shown the same way.
* **Action menu** in three or four category tabs (Security · Politics · Construction, plus Financing for the
  Palestinian President). It nests into sub-menus and each level shows a photo. At every level an **advisor** button
  shows the two opposing advisors' views. Items on cooldown or not yet unlocked are greyed out.
* **Turn animation**: a progress bar with a day counter, a night overlay and a clock while "time passes". Then the
  feedback event dialog opens.
* **Event dialog**: sender line, headline, photo, scrolling body text, a sound cue and a news ticker.
* **History graph**: per-variable history (`HistoryGraph`, `HistoryBarGraph`).
* **Timeline**: a historical primer in 15 photographic eras.
* **Options**: tutorial toggle, timeline, audio, map areas, language, quit.

## Visual identity (2015 remaster)

* Role accent colours: Israeli `#39b5e5` (blue), Palestinian `#7ab547` (green). Positive `#6EA33F`, negative
  `#D24E58`, neutral greys `#1f2628` / `#404a4c` / `#e3e5e5`.
* The look is news-photo realism (Reuters imagery plus documentary video) with a clean flat UI. The tagline is
  "Play the News. Solve the Puzzle."

## UX observations for the redesign

* The **"must open every pin"** rule makes players read the news, which is good for learning, but it slows play.
* Scores are opaque. Players see meter deltas, but the formulas (and the fact that Yesha isn't counted) are hidden.
* No undo, no forecast, and no "what would happen if" view. The advisors are the only decision support.
* There is no negotiation interface: talks with the other leader are one-shot menu actions, not exchanges.

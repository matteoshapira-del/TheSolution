# AI actor catalog

Generated from `data/harvest/ai_actors.json`. Actors run every turn in the order listed.
`call frequency` is the number of turns an actor sleeps after acting (0 = acts every turn).
Actors flagged *difficulty* start with an extra 6–14 turns of sleep and have their
`#SleepDifficulty` naps lengthened or shortened by difficulty. At most 3 actors may
produce a news event per turn; once that cap is hit the remaining actors are skipped.

## Playing as israeli

| order | actor | call frequency | difficulty | bundled with player turn | outcomes it can trigger |
|---|---|---|---|---|---|
| 1 | **IsrClock** | 0 | — | yes | 1 |
| 2 | **IsrMusicDJ** | 0 | — | — | 0 |
| 3 | **IPMPalestinianPublic** | 1 | yes | — | 6 |
| 4 | **Hamas** | 0 | yes | — | 5 |
| 5 | **International Press** | 5 | yes | — | 10 |
| 6 | **Israeli People** | 1 | yes | — | 12 |
| 7 | **Israeli Government** | 1 | yes | — | 11 |
| 8 | **Palestinian President** | 1 | yes | — | 12 |
| 9 | **Yesha** | 1 | yes | — | 8 |

### israeli · IsrClock

- per turn var modifications — if always
  - then → `reduceSuppressionAndAddCooperation`

<details><summary>Outcome effects</summary>

- `reduceSuppressionAndAddCooperation` (success): —; `suppression` += -2; `palestinian cooperation` += 3 × budgetMod(`palestinian president`); `security` += 1 × budgetMod(`palestinian cooperation`); `israel people` += 1 × budgetMod(`security`); `sympathy` += 0.5 × budgetMod(`security`)

</details>

### israeli · IsrMusicDJ

- test losing internal — if `internal authority score` < -30
  - then → music `mus_Lp_Isr_Neg_ST`
- test losing external — if `external authority score` < -30
  - then → music `mus_Lp_Isr_Neg_ST`
- test Winning — if `internal authority score` > 30 and `external authority score` > 30
  - then → music `mus_Lp_Isr_Pos_ST`
  - else → music `mus_Lp_Isr_Neutral_ST`

### israeli · IPMPalestinianPublic

- initial setup roll.. — if roll `roll` ∈ 0..4
  - then:
    - IPMPublicStreetRallyProYou test.. — if `roll` = 0 and `palestinian people` ≥ rand(80±20)
      - then → `IPMPublicStreetRallyProYou`
    - IPMPublicAgressiveProtestAntiYou test.. _(else)_ — if `roll` = 0 and `palestinian people` < rand(20±10)
      - then → `IPMPublicAgressiveProtestAntiYou`
    - IPMPublicStreetProtestAntiYou test.. _(else)_ — if `roll` = 0 and `palestinian people` < rand(40±10)
      - then → `IPMPublicStreetProtestAntiYou`
    - Pal Public listen to concerns... — if `roll` = 4
      - then:
        - IPMPublicTooMuchViolence test.. — if `suppression` > 60
          - then → `IPMPublicTooMuchViolence`
        - IPMPublicHighQualityOfLife test.. _(else)_ — if `palestinian people` > 75
          - then → `IPMPublicHighQualityOfLife`
        - IPMPublicLowQualityOfLife test.. _(else)_ — if always
          - then → `IPMPublicLowQualityOfLife`

<details><summary>Outcome effects</summary>

- `IPMPublicAgressiveProtestAntiYou` (agressiveProtestAntiYou): -4 israel people, -3 yesha, -2 palestinian president, -1 arab world, -1 palestinian cooperation, -1 palestinian people, -1 security, -1 un, -1 usa; IPMPalestinianPublic sleeps 3 turns — event `palestinian public, anti-you, aggressive protest`
- `IPMPublicHighQualityOfLife` (highQOL): —; IPMPalestinianPublic sleeps 3 turns — event `palestinian public, praise, high quality of life`
- `IPMPublicLowQualityOfLife` (lowQOL): —; IPMPalestinianPublic sleeps 3 turns — event `palestinian public, concern, low quality of life`
- `IPMPublicStreetProtestAntiYou` (streetProtestAntiYou): -2 israel people, -2 yesha, -1 arab world, -1 palestinian cooperation, -1 palestinian president, -1 un; IPMPalestinianPublic sleeps 3 turns — event `palestinian public, anti-you, street protest`
- `IPMPublicStreetRallyProYou` (streetRallyProYou): +5 palestinian cooperation, +3 palestinian president, +3 sympathy, +3 un, +2 arab world, +2 israel people, +2 palestinian people, +2 security, +1 usa; IPMPalestinianPublic sleeps 3 turns — event `palestinian public, pro-you, street rally`
- `IPMPublicTooMuchViolence` (tooMuchViolence): —; IPMPalestinianPublic sleeps 3 turns — event `palestinian public, concern, too much violence`

</details>

### israeli · Hamas

- Hamas suppression test... — if roll `roll` ∈ 0..299 and `roll` < suppression
  - then → `NoAction`
  - else:
    - Setup hamas action.. — if roll `roll` ∈ 0..99
      - then:
        - IPMHamasOrganizeWithInternationalTerror test.. — if `hamas` < rand(20±10) and `suppression` < rand(10±10) and `roll` > 95
          - then → `IPMHamasOrganizeWithInternationalTerror`
        - IPMHamasExtremeAttack test.. _(else)_ — if `hamas` < rand(30±10) and `suppression` < rand(25±10) and `roll` > 70
          - then → `IPMHamasExtremeAttack`
        - IPMHamasAttack test.. _(else)_ — if `hamas` < rand(50±10) and `suppression` < rand(40±10) and `roll` > 40
          - then → `IPMHamasAttack`
        - IPMHamasAntiIsraelFunds test.. _(else)_ — if `roll` > 10
          - then → `IPMHamasAntiIsraelFunds`
          - else → `IPMHamasAntiIsraelWords`

<details><summary>Outcome effects</summary>

- `IPMHamasAntiIsraelFunds` (funds-material): -6 yesha, -5 israel people, -3 security, +10 endreport; Hamas sleeps 3 turns (difficulty-adjusted) — event `hamas-fatah, anti-israel, funds-material`
- `IPMHamasAntiIsraelWords` (words): -4 yesha, -3 israel people, -1 security, +10 endreport; Hamas sleeps 2 turns (difficulty-adjusted) — event `hamas-fatah, anti-israel, words`
- `IPMHamasAttack` (attack): -8 yesha, -7 israel people, -5 security, +15 endreport; Hamas sleeps 3 turns (difficulty-adjusted) — event `hamas-fatah, anti-israel, attack`
- `IPMHamasExtremeAttack` (extreme attack): -12 yesha, -10 israel people, -9 security, -1 sympathy, +18 endreport; Hamas sleeps 4 turns (difficulty-adjusted) — event `hamas-fatah, anti-israel, extreme attack`
- `IPMHamasOrganizeWithInternationalTerror` (organize with international terror): -17 yesha, -15 israel people, -11 security, +20 endreport; Hamas sleeps 6 turns (difficulty-adjusted) — event `hamas-fatah, anti-israel, organize with international terror`

</details>

### israeli · International Press

- test for lowApproval.. — if `israel people` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy) and `israel people` < 40
  - then → `IPMPressLowApproval`
- test for lowTrust.. _(else)_ — if `palestinian president` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy) and `palestinian president` < 45
  - then → `IPMPressLowTrust`
- test for lowQOL.. _(else)_ — if `palestinian people` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy) and `palestinian people` < 45
  - then → `IPMPressLowQualityOfLife`
- test for lowSecurity.. _(else)_ — if `security` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy) and `security` < 45
  - then → `IPMPressLowSecurity`
- test for IPMPressLowSympathy.. _(else)_ — if `sympathy` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy) and `sympathy` < 20
  - then → `IPMPressLowSympathy`
- test for IPMPressHighApproval.. — if `israel people` is 'highest' of (israel people, palestinian president, palestinian people, security, sympathy) and `israel people` > 70
  - then → `IPMPressHighApproval`
- test for IPMPressHighTrust.. — if `palestinian president` is 'highest' of (israel people, palestinian president, palestinian people, security, sympathy) and `palestinian president` > 75
  - then → `IPMPressHighTrust`
- test for IPMPressHighQualityOfLife.. _(else)_ — if `palestinian people` is 'highest' of (israel people, palestinian president, palestinian people, security, sympathy) and `palestinian people` > 75
  - then → `IPMPressHighQualityOfLife`
- test for IPMPressHighSecurity.. _(else)_ — if `security` is 'highest' of (israel people, palestinian president, palestinian people, security, sympathy) and `security` > 75
  - then → `IPMPressHighSecurity`
- test for IPMPressHighSympathy.. _(else)_ — if `sympathy` is 'highest' of (israel people, palestinian president, palestinian people, security, sympathy) and `sympathy` > 70
  - then → `IPMPressHighSympathy`
- test for lowApproval2.. — if `israel people` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy)
  - then → `IPMPressLowApproval`
- test for lowTrust2.. _(else)_ — if `palestinian president` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy)
  - then → `IPMPressLowTrust`
- test for lowQOL2.. _(else)_ — if `palestinian people` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy)
  - then → `IPMPressLowQualityOfLife`
- test for lowSecurity2.. _(else)_ — if `security` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy)
  - then → `IPMPressLowSecurity`
- test for IPMPressLowSympathy2.. _(else)_ — if `sympathy` is the lowest of (israel people, palestinian president, palestinian people, security, sympathy)
  - then → `IPMPressLowSympathy`

<details><summary>Outcome effects</summary>

- `IPMPressHighApproval` (highApproval): —; International Press sleeps 10 turns — event `international press, praise, high popular approval`
- `IPMPressHighQualityOfLife` (highQOL): —; International Press sleeps 10 turns — event `international press, praise, high quality of life`
- `IPMPressHighSecurity` (highSecurity): —; International Press sleeps 10 turns — event `international press, praise, high security`
- `IPMPressHighSympathy` (highSympathy): —; International Press sleeps 10 turns — event `international press, praise, high sympathy`
- `IPMPressHighTrust` (highTrust): —; International Press sleeps 10 turns — event `international press, praise, high palestinian trust`
- `IPMPressLowApproval` (lowApproval): —; International Press sleeps 10 turns — event `international press, concern, low popular approval`
- `IPMPressLowQualityOfLife` (lowQOL): —; International Press sleeps 10 turns — event `international press, concern, low quality of life`
- `IPMPressLowSecurity` (lowSecurity): —; International Press sleeps 10 turns — event `international press, concern, low security`
- `IPMPressLowSympathy` (lowSympathy): —; International Press sleeps 10 turns — event `international press, concern, low sympathy`
- `IPMPressLowTrust` (lowTrust): —; International Press sleeps 10 turns — event `international press, concern, low palestinian trust`

</details>

### israeli · Israeli People

Poll branches the player can query: `IsrPeopleConcerns`

- roll setup.. — if roll `roll` ∈ 0..4
  - then:
    - test ISR People listen to concerns.. — if `roll` = 0
      - then **[poll entry `IsrPeopleConcerns` — what "Listen to Concerns" evaluates]**:
      - then:
        - test for lowApproval.. — if `israel people` is the lowest of (israel people, security, suppression) and `israel people` < 40
          - then → `IPMIsraeliPeopleConcernLowApproval`
        - test for lowSecurity.. _(else)_ — if `security` is the lowest of (israel people, security, suppression) and `security` < 45
          - then → `IPMIsraeliPeopleConcernLowSecurity`
        - test for lowSuprpession.. _(else)_ — if `suppression` is the lowest of (israel people, security, suppression) and `suppression` < 30
          - then → `IPMIsraeliPeopleConcernLowSuppression`
        - test for highApproval.. — if `israel people` is 'highest' of (israel people, security, suppression, sympathy) and `israel people` > 70
          - then → `IPMIsraeliPeoplePraiseHighApproval`
        - test for highSecurity.. _(else)_ — if `security` is 'highest' of (israel people, security, suppression, sympathy) and `security` > 70
          - then → `IPMIsraeliPeoplePraiseHighSecurity`
        - test for highSympathy.. _(else)_ — if `sympathy` is 'highest' of (israel people, security, suppression, sympathy) and `sympathy` > 70
          - then → `IPMIsraeliPeoplePraiseHighSympathy`
        - test for highSympathy.. _(else)_ — if `suppression` is 'highest' of (israel people, security, suppression, sympathy) and `suppression` > 60
          - then → `IPMIsraeliPeoplePraiseHighSuppression`
        - test for lowApproval2.. — if `israel people` is the lowest of (israel people, security, suppression)
          - then → `IPMIsraeliPeopleConcernLowApproval`
        - test for lowSecurity2.. _(else)_ — if `security` is the lowest of (israel people, security, suppression)
          - then → `IPMIsraeliPeopleConcernLowSecurity`
        - test for lowSuppression.. _(else)_ — if `suppression` is the lowest of (israel people, security, suppression)
          - then → `IPMIsraeliPeopleConcernLowSuppression`
    - test for anti you.. — if `israel people` < rand(20±20) and #Not roll 4
      - then:
        - flip for IPMIsraeliPeopleAntiYouStreetProtest or IPMIsraeliPeopleAntiYouPetition..  — if roll `flip` ∈ 0..1 and `flip` = 0
          - then → `IPMIsraeliPeopleAntiYouStreetProtest`
          - else → `IPMIsraeliPeopleAntiYouPetition`
    - test for antiPalestine.. _(else)_ — if `sympathy` < rand(30±20)
      - then → `IPMIsraeliPeopleAntiPalestineStreetProtest`
    - test for proyou.. _(else)_ — if `israel people` < rand(70±20)
      - then:
        - flip for IPMIsraeliPeopleProYouStreetRally or IPMIsraeliPeopleProYouPetition.. — if roll `flip` ∈ 0..1 and `flip` = 0
          - then → `IPMIsraeliPeopleProYouStreetRally`
          - else → `IPMIsraeliPeopleProYouPetition`

<details><summary>Outcome effects</summary>

- `IPMIsraeliPeopleAntiPalestineStreetProtest` (street protest): -5 palestinian people, -4 un, -3 arab world, -3 palestinian president, -2 palestinian cooperation, -1 usa, +12 endreport; Israeli People sleeps 5 turns (difficulty-adjusted) — event `israeli public, anti-palestine, street protest`
- `IPMIsraeliPeopleAntiYouPetition` (petition): -4 yesha, -3 israel people, -2 suppression, -1 arab world, -1 un, -1 usa; Israeli People sleeps 5 turns (difficulty-adjusted) — event `israeli public, anti-you, petition`
- `IPMIsraeliPeopleAntiYouStreetProtest` (street protest): -6 yesha, -5 israel people, -4 suppression, -2 arab world, -2 un, -2 usa; Israeli People sleeps 5 turns (difficulty-adjusted) — event `israeli public, anti-you, street protest`
- `IPMIsraeliPeopleConcernLowApproval` (low approval): —; Israeli People sleeps 5 turns — event `israeli public, concern, low approval`
- `IPMIsraeliPeopleConcernLowSecurity` (low security): —; Israeli People sleeps 5 turns — event `israeli public, concern, low security`
- `IPMIsraeliPeopleConcernLowSuppression` (low suppression): —; Israeli People sleeps 5 turns — event `israeli public, concern, low suppression`
- `IPMIsraeliPeoplePraiseHighApproval` (high approval): —; Israeli People sleeps 5 turns — event `israeli public, praise, high approval`
- `IPMIsraeliPeoplePraiseHighSecurity` (high security): —; Israeli People sleeps 5 turns — event `israeli public, praise, high security`
- `IPMIsraeliPeoplePraiseHighSuppression` (high suppression): —; Israeli People sleeps 5 turns — event `israeli public, praise, high suppression`
- `IPMIsraeliPeoplePraiseHighSympathy` (high sympathy): —; Israeli People sleeps 5 turns — event `israeli public, praise, high sympathy`
- `IPMIsraeliPeopleProYouPetition` (petition): +4 yesha, +3 israel people, +3 un, +2 arab world, +2 palestinian president, +2 security, +2 usa; Israeli People sleeps 5 turns — event `israeli public, pro-you, petition`
- `IPMIsraeliPeopleProYouStreetRally` (street rally): +6 yesha, +5 israel people, +3 un, +2 arab world, +2 palestinian president, +2 security, +2 usa, +4 endreport; Israeli People sleeps 5 turns — event `israeli public, pro-you, street rally`

</details>

### israeli · Israeli Government

Poll branches the player can query: `IPMIsrGovConcerns`

- roll setup.. — if roll `roll` ∈ 0..4
  - then:
    - Test for ISR Gov concerns.. — if `roll` = 0
      - then **[poll entry `IPMIsrGovConcerns` — what "Listen to Concerns" evaluates]**:
      - then:
        - test for lowApproval.. — if `israel people` is the lowest of (israel people, security, palestinian people, palestinian president) and `israel people` < 40
          - then → `IPMIsraeliGovernmentConcernLowPopularApproval`
        - test for lowSecurity.. _(else)_ — if `security` is the lowest of (israel people, security, palestinian people, palestinian president) and `security` < 45
          - then → `IPMIsraeliGovernmentConcernLowSecurity`
        - test for lowTrust.. _(else)_ — if `palestinian people` is the lowest of (israel people, security, palestinian people, palestinian president) and `palestinian people` < 45
          - then → `IPMIsraeliGovernmentLowPalestinianTrust`
        - test for lowQOL.. _(else)_ — if `apalestinian president` is the lowest of (israel people, security, palestinian people, palestinian president) and `palestinian president` < 45
          - then → `IPMIsraeliGovernmentLowQualityOfLife`
        - test for highApproval.. — if `israel people` is 'highest' of (israel people, security, palestinian people, palestinian president) and `israel people` > 70
          - then → `IPMIsraeliGovernmentPraiseHighPopularApproval`
        - test for highSecurity.. _(else)_ — if `security` is 'highest' of (israel people, security, palestinian people, palestinian president) and `security` > 75
          - then → `IPMIsraeliGovernmentPraiseHighSecurity`
        - test for highTrust.. _(else)_ — if `palestinian president` is 'highest' of (israel people, security, palestinian people, palestinian president) and `palestinian president` > 75
          - then → `IPMIsraeliGovernmentPraiseHighPalestinianTrust`
        - test for highQOL.. _(else)_ — if `palestinian people` is 'highest' of (israel people, security, palestinian people, palestinian president) and `palestinian people` > 75
          - then → `IPMIsraeliGovernmentPraiseHighQualityOfLife`
        - test for lowApproval.. — if `israel people` is the lowest of (israel people, security, palestinian people, palestinian president)
          - then → `IPMIsraeliGovernmentConcernLowPopularApproval`
        - test for lowSecurity.. _(else)_ — if `security` is the lowest of (israel people, security, palestinian people, palestinian president)
          - then → `IPMIsraeliGovernmentConcernLowSecurity`
        - test for lowTrust.. _(else)_ — if `palestinian people` is the lowest of (israel people, security, palestinian people, palestinian president)
          - then → `IPMIsraeliGovernmentLowPalestinianTrust`
        - test for lowQOL.. _(else)_ — if `apalestinian president` is the lowest of (israel people, security, palestinian people, palestinian president)
          - then → `IPMIsraeliGovernmentLowQualityOfLife`
    - test for IPMIsraeliGovernmentAntiYouWords.. — if `israel people` < rand(70±20) and `roll` ≠ 4
      - then → `IPMIsraeliGovernmentAntiYouWords`
    - test for IPMIsraeliGovernmentAntiPalestineWords.. _(else)_ — if `sympathy` < rand(30±20)
      - then → `IPMIsraeliGovernmentAntiPalestineWords`
    - test for IPMIsraeliGovernmentProYouWords.. _(else)_ — if `israel people` < rand(70±20)
      - then → `IPMIsraeliGovernmentProYouWords`

<details><summary>Outcome effects</summary>

- `IPMIsraeliGovernmentAntiPalestineWords` (words): -6 palestinian people, -5 arab world, -5 palestinian president, -4 palestinian cooperation, -4 suppression, -4 un, -1 usa; Israeli Government sleeps 4 turns — event `israeli government, anti-palestine, words`
- `IPMIsraeliGovernmentAntiYouWords` (words): -4 israel people, -4 yesha, -2 usa, -1 arab world, -1 palestinian president, -1 suppression, -1 un; Israeli Government sleeps 4 turns — event `israeli government, anti-you, words`
- `IPMIsraeliGovernmentConcernLowPopularApproval` (low popular approval): —; Israeli Government sleeps 4 turns — event `israeli government, concern, low popular approval`
- `IPMIsraeliGovernmentConcernLowSecurity` (low security): —; Israeli Government sleeps 4 turns — event `israeli government, concern, low security`
- `IPMIsraeliGovernmentLowPalestinianTrust` (low palestinian trust): —; Israeli Government sleeps 4 turns — event `israeli government, concern, low palestinian trust`
- `IPMIsraeliGovernmentLowQualityOfLife` (low quality of life): —; Israeli Government sleeps 4 turns — event `israeli government, concern, low quality of life`
- `IPMIsraeliGovernmentPraiseHighPalestinianTrust` (high palestinian trust): —; Israeli Government sleeps 4 turns — event `israeli government, praise, high palestinian trust`
- `IPMIsraeliGovernmentPraiseHighPopularApproval` (high popular approval): —; Israeli Government sleeps 4 turns — event `israeli government, praise, high popular approval`
- `IPMIsraeliGovernmentPraiseHighQualityOfLife` (high quality of life): —; Israeli Government sleeps 4 turns — event `israeli government, praise, high quality of life`
- `IPMIsraeliGovernmentPraiseHighSecurity` (high security): —; Israeli Government sleeps 4 turns — event `israeli government, praise, high security`
- `IPMIsraeliGovernmentProYouWords` (words): +4 yesha, +3 israel people, +3 un, +3 usa, +2 palestinian president, +1 arab world, +1 palestinian cooperation, +1 palestinian people, +1 security, +1 sympathy; Israeli Government sleeps 4 turns — event `israeli government, pro-you, words`

</details>

### israeli · Palestinian President

Poll branches the player can query: `PalPresConcerns`

- roll setup.. — if roll `roll` ∈ 0..4
  - then:
    - Test Pal Pres for concerns.. — if `roll` = 0
      - then **[poll entry `PalPresConcerns` — what "Listen to Concerns" evaluates]**:
      - then:
        - test for high suppression.. — if `suppression` > 60
          - then → `IPMPalestinianPresidentConcernTooMuchViolence`
        - test for lowTrust.. — if `palestinian president` is the lowest of (palestinian president, palestinian people) and `palestinian president` < 45
          - then → `IPMPalestinianPresidentConcernLowTrust`
        - test for lowQOL.. _(else)_ — if `palestinian people` is the lowest of (palestinian president, palestinian people) and `palestinian people` < 45
          - then → `IPMPalestinianPresidentConcernLowQualityOfLife`
        - test for highTrust.. — if `palestinian president` is 'highest' of (palestinian president, palestinian people) and `palestinian president` > 75
          - then → `IPMPalestinianPresidentPraiseHighTrust`
        - test for highQOL.. _(else)_ — if `palestinian people` is 'highest' of (palestinian president, palestinian people) and `palestinian people` > 75
          - then → `IPMPalestinianPresidentPraiseHighQualityOfLife`
        - test for lowTrust2.. — if `palestinian president` is the lowest of (palestinian president, palestinian people)
          - then → `IPMPalestinianPresidentConcernLowTrust`
        - test for lowQOL2.. _(else)_ — if `palestinian people` is the lowest of (palestinian president, palestinian people)
          - then → `IPMPalestinianPresidentConcernLowQualityOfLife`
    - test for antiYou.. — if `palestinian president` < rand(20±10)
      - then → `IPMPalestinianPresidentAntiYouWords`
    - test for antiMilitant.. _(else)_ — if `palestinian president` ≥ rand(60±30) and `roll` > 2
      - then:
        - roll for anti militant.. — if roll `roll2` ∈ 0..3
          - then:
            - test for IPMPalestinianPresidentAntiMilitantExtremePolice.. — if `palestinian president` ≥ rand(80±20)
              - then → `IPMPalestinianPresidentAntiMilitantExtremePolice`
            - test for IPMPalestinianPresidentAntiMilitantExtremePolice.. — if `palestinian president` ≥ rand(70±20) and `roll2` < 2
              - then → `IPMPalestinianPresidentAntiMilitantExtremePolice`
            - test for IPMPalestinianPresidentAntiMilitantPolitical.. — if `palestinian president` ≥ rand(70±20) and `roll2` > 1
              - then → `IPMPalestinianPresidentAntiMilitantPolitical`
              - else → `IPMPalestinianPresidentAntiMilitantWords`
    - test for proYou.. _(else)_ — if `palestinian president` ≥ rand(60±30) and `roll` = 1
      - then:
        - test for IPMPalestinianPresidentProYouOfferToMeetForNegotiations.. — if `palestinian president` ≥ rand(80±20)
          - then → `IPMPalestinianPresidentProYouOfferToMeetForNegotiations`
        - test for IPMPalestinianPresidentProYouStreetRally.. _(else)_ — if `palestinian president` ≥ rand(70±20)
          - then → `IPMPalestinianPresidentProYouStreetRally`
          - else → `IPMPalestinianPresidentProYouWords`

<details><summary>Outcome effects</summary>

- `IPMPalestinianPresidentAntiMilitantExtremePolice` (extreme police): +9 yesha, +8 israel people, +6 suppression, -5 palestinian cooperation, +5 security, +4 un, +3 usa, +2 arab world, +1 sympathy, +12 endreport; Palestinian President sleeps 5 turns — event `palestinian president, anti-militant, extreme police`
- `IPMPalestinianPresidentAntiMilitantPolitical` (political): -8 palestinian cooperation, +7 hamas, +5 security, +5 yesha, +4 israel people, +4 palestinian people, +2 usa, +1 arab world, +1 sympathy, +1 un, +3 endreport; Palestinian President sleeps 4 turns — event `palestinian president, anti-militant, political`
- `IPMPalestinianPresidentAntiMilitantWords` (words): +6 yesha, +5 israel people, -4 palestinian cooperation, +2 security, +2 usa, +1 arab world, +1 sympathy, +1 un; Palestinian President sleeps 4 turns — event `palestinian president, anti-militant, words`
- `IPMPalestinianPresidentAntiYouWords` (words): -5 palestinian cooperation, -5 suppression, -3 arab world, -3 palestinian people, -3 security, -2 israel people, -2 palestinian president, -2 un, +2 yesha, +1 sympathy, +5 endreport; Palestinian President sleeps 4 turns (difficulty-adjusted) — event `palestinian president, anti-you, words`
- `IPMPalestinianPresidentConcernLowQualityOfLife` (low quality of life): —; Palestinian President sleeps 4 turns — event `palestinian president, concern, low quality of life`
- `IPMPalestinianPresidentConcernLowTrust` (low trust): —; Palestinian President sleeps 4 turns — event `palestinian president, concern, low trust`
- `IPMPalestinianPresidentConcernTooMuchViolence` (too much violence): —; Palestinian President sleeps 4 turns — event `palestinian president, concern, too much violence`
- `IPMPalestinianPresidentPraiseHighQualityOfLife` (high quality of life): —; Palestinian President sleeps 4 turns — event `palestinian president, praise, high quality of life`
- `IPMPalestinianPresidentPraiseHighTrust` (high trust): —; Palestinian President sleeps 4 turns — event `palestinian president, praise, high trust`
- `IPMPalestinianPresidentProYouOfferToMeetForNegotiations` (offer to meet for negotiations): +6 arab world, +6 hamas, +6 un, +6 usa, +5 israel people, +5 palestinian cooperation, +5 palestinian people, +5 yesha, +2 sympathy, +5 endreport; Palestinian President sleeps 5 turns — event `palestinian president, pro-you, offer to meet for negotiations`
- `IPMPalestinianPresidentProYouStreetRally` (street rally): +5 palestinian cooperation, +4 arab world, +4 un, +3 hamas, +3 palestinian people, +2 israel people, +2 usa, +2 yesha, +1 sympathy, +3 endreport; Palestinian President sleeps 4 turns — event `palestinian president, pro-you, street rally`
- `IPMPalestinianPresidentProYouWords` (words): +5 palestinian cooperation, +2 arab world, +2 israel people, +2 un, +2 usa, +2 yesha, +1 hamas, +1 palestinian people, +1 sympathy; Palestinian President sleeps 3 turns — event `palestinian president, pro-you, words`

</details>

### israeli · Yesha

- roll setup.. — if roll `roll` ∈ 0..4
  - then:
    - Test for concerns.. — if `roll` = 0
      - then:
        - test for lowApproval.. — if `israel people` is the lowest of (israel people, yesha) and `israel people` < 40
          - then → `IPMYeshaConcernLowApproval`
        - test for lowSettlers.. _(else)_ — if `yesha` is the lowest of (israel people, yesha) and `yesha` < 25
          - then → `IPMYeshaConcernSettlementWithdrawal`
        - test for highSettlers.. — if `yesha` is 'highest' of (israel people, yesha) and `yesha` > 60
          - then → `IPMYeshaPraiseHighApproval`
        - no concerns detected.  no action performed — if always
          - then → `NoAction`
    - test for antiYou.. — if `yesha` < rand(30±20)
      - then:
        - die roll setup — if roll `roll2` ∈ 0..2
          - then:
            - IPMYeshaAntiYouStreetProtests test.. — if `roll2` = 0
              - then → `IPMYeshaAntiYouStreetProtests`
            - IPMYeshaAntiYouPetition test.. — if `roll2` = 1
              - then → `IPMYeshaAntiYouPetition`
    - test for antiPalestine.. _(else)_ — if `sympathy` < rand(50±20)
      - then:
        - die roll setup.. — if roll `roll2` ∈ 0..3
          - then:
            - IPMYeshaAntiPalestineIllegalExpansion test.. — if `roll2` = 0
              - then → `IPMYeshaAntiPalestineIllegalExpansion`
            - IPMYeshaAntiPalestineHarassment test.. — if `roll2` = 1
              - then → `IPMYeshaAntiPalestineHarassment`
            - IPMYeshaAntiPalestineAssault test.. — if `roll2` = 2
              - then → `IPMYeshaAntiPalestineAssault`

<details><summary>Outcome effects</summary>

- `IPMYeshaAntiPalestineAssault` (assault): -8 palestinian president, -6 palestinian people, -4 arab world, -4 palestinian cooperation, -4 un, -2 usa, -1 hamas, +16 endreport; Yesha sleeps 4 turns (difficulty-adjusted) — event `yesha, anti-palestine, assault`
- `IPMYeshaAntiPalestineHarassment` (harassment): -5 palestinian president, -3 arab world, -3 palestinian cooperation, -3 palestinian people, -3 un, -1 hamas, -1 usa, +12 endreport; Yesha sleeps 4 turns (difficulty-adjusted) — event `yesha, anti-palestine, harassment`
- `IPMYeshaAntiPalestineIllegalExpansion` (illegal expansion): -2 arab world, -2 palestinian cooperation, -2 palestinian people, -2 palestinian president, -2 un, -1 usa, +20 endreport; Yesha sleeps 4 turns (difficulty-adjusted) — event `yesha, anti-palestine, illegal expansion`
- `IPMYeshaAntiYouPetition` (petition): -2 israel people, -2 palestinian president, -1 arab world, -1 un, -1 usa; Yesha sleeps 3 turns (difficulty-adjusted) — event `yesha, anti-you, petition`
- `IPMYeshaAntiYouStreetProtests` (street protests): -4 israel people, -3 palestinian president, -1 arab world, -1 un, -1 usa, +6 endreport; Yesha sleeps 3 turns (difficulty-adjusted) — event `yesha, anti-you, street protests`
- `IPMYeshaConcernLowApproval` (low approval): —; Yesha sleeps 4 turns — event `yesha, concern, low approval`
- `IPMYeshaConcernSettlementWithdrawal` (settlement withdrawal): —; Yesha sleeps 4 turns — event `yesha, concern, settlement withdrawal`
- `IPMYeshaPraiseHighApproval` (high approval): —; Yesha sleeps 4 turns — event `yesha, praise, high approval`

</details>

## Playing as palestinian

| order | actor | call frequency | difficulty | bundled with player turn | outcomes it can trigger |
|---|---|---|---|---|---|
| 1 | **PalMusicDJ** | 0 | — | — | 0 |
| 2 | **Clock** | 0 | — | yes | 1 |
| 3 | **Hamas** | 0 | yes | — | 12 |
| 4 | **Fatah** | 0 | yes | — | 11 |
| 5 | **Israeli Prime Minister** | 0 | yes | — | 6 |
| 6 | **Palestinian Public** | 1 | yes | — | 9 |
| 7 | **Yesha** | 0 | yes | — | 3 |

### palestinian · PalMusicDJ

- test losing internal — if `internal authority score` < -30
  - then → music `mus_LP_PA_Neg_ST`
- test losing external — if `external authority score` < -30
  - then → music `mus_LP_PA_Neg_ST`
- test Winning — if `internal authority score` > 30 and `external authority score` > 30
  - then → music `mus_LP_PA_Pos_ST`
  - else → music `mus_LP_PA_Neutral_ST`

### palestinian · Clock

- Always true.. add budgets — if always
  - then → `addBudgets`

<details><summary>Outcome effects</summary>

- `addBudgets` (success): —; `usa budget` += 3 × budgetMod(`usa approval`); `un budget` += 1.5 × budgetMod(`un approval`); `eu budget` += 2 × budgetMod(`un approval`); `egypt budget` += 1 × budgetMod(`arab world approval`); `jordan budget` += 1 × budgetMod(`arab world approval`); `israel budget` += 1.5 × budgetMod(`israeli prime minister approval`); `other groups budget` += 2 × budgetMod(`leadership`); `budget` += 1 × budgetMod(`economy`); `israeli cooperation` += 3 × budgetMod(`israeli prime minister approval`)

</details>

### palestinian · Hamas

- If Hamas likes us.. — if `hamas approval` ≥ rand(80±20)
  - then:
    - Hamas Partial Disarm Test.. — if roll `flip` ∈ 0..1 and `flip` = 1 and `hamas approval` ≥ rand(70±5)
      - then → `HamasPartialDisarm`
    - Hamas either commits to reconstruction or join political process.. — if `hamas approval` ≥ rand(55±5)
      - then:
        - Hamas flips between reconstruction or political process.. — if roll `flip` ∈ 0..1 and `flip` = 0
          - then → `HamasCommitToReconstruction`
          - else → `HamasJoinPoliticalProcess`
      - else → `HamasProYouWords`
- If Hamas really hates us.. _(else)_ — if roll `flip` ∈ 0..1 and `flip` = 0 and `hamas approval` < rand(30±30)
  - then:
    - Hamas Attacks You Test.. — if `hamas approval` < rand(15±5)
      - then → `HamasAttackOnYou`
    - Hamas either talks shit or claims a victory.. — if roll `flip` ∈ 0..1 and `flip` = 1
      - then → `HamasAntiYouWords`
      - else → `HamasClaimVictories`
- Hamas Anti Israel.. _(else)_ — if `tolerance` < rand(100±30)
  - then:
    - Setting up Anti Israel... — if roll `roll` ∈ 0..7
      - then:
        - Either Hamas Extreme Attack or Organize with international terrorists.. — if `tolerance` < rand(30±5)
          - then:
            - Extreme attack test.. — if `roll` = 0 and `hamas approval` < rand(40±5)
              - then → `HamasExtremeAttack`
            - Organize with terrorists test.. — if `roll` = 1 and `hamas approval` < rand(30±5)
              - then → `HamasOrganizeWithInternationalTerror`
        - Regular Hamas Attack test.. — if `tolerance` < rand(60±5) and `roll` < 3
          - then → `HamasAttack`
        - Hamas Fund test.. — if `roll` < 4
          - then → `HamasFunds`
        - Hamas Anti Isreali Words test.. — if `roll` > 6
          - then → `HamasAntiIsraelWords`

<details><summary>Outcome effects</summary>

- `HamasAntiIsraelWords` (words): -5 israeli public approval, -4 israeli prime minister approval, -3 israeli cooperation, -1 un approval, -1 usa approval, +3 endreport; Hamas sleeps 2 turns (difficulty-adjusted) — event `hamas, anti-israel, words`
- `HamasAntiYouWords` (words): -4 palestinian public approval, -3 fatah approval, -1 arab world approval, +3 endreport; Hamas sleeps 2 turns (difficulty-adjusted) — event `hamas, anti-you, words`
- `HamasAttack` (attack): -8 un approval, -7 israeli prime minister approval, -7 israeli public approval, -7 usa approval, -6 israeli cooperation, -5 arab world approval, +10 endreport; Hamas sleeps 4 turns (difficulty-adjusted) — event `hamas, anti-israel, attack`
- `HamasAttackOnYou` (attack on your organization): -8 palestinian public approval, -6 fatah approval, -6 government authority, -1 leadership, +9 endreport; Hamas sleeps 4 turns (difficulty-adjusted) — event `hamas, anti-you, attack on your organization`
- `HamasClaimVictories` (claim victories over you): -5 palestinian public approval, -4 fatah approval, -3 government authority, +3 endreport; Hamas sleeps 3 turns (difficulty-adjusted) — event `hamas, anti-you, claim victories over you`
- `HamasCommitToReconstruction` (commit to reconstruction): —; Hamas sleeps 2 turns — event `hamas, pro-you, commit to reconstruction`
- `HamasExtremeAttack` (extreme attack): -16 usa approval, -12 israeli prime minister approval, -12 israeli public approval, -8 israeli cooperation, -8 un approval, -6 arab world approval, -1 leadership, +20 endreport; Hamas sleeps 5 turns (difficulty-adjusted) — event `hamas, anti-israel, extreme attack`
- `HamasFunds` (funds): -6 israeli public approval, -6 usa approval, -5 israeli prime minister approval, -5 un approval, -3 arab world approval, +6 endreport; Hamas sleeps 3 turns (difficulty-adjusted) — event `hamas, anti-israel, funds`
- `HamasJoinPoliticalProcess` (join political process): +5 fatah approval, +5 government authority, +5 palestinian public approval, +2 israeli cooperation, +1 leadership, +1 tolerance; Hamas sleeps 6 turns — event `hamas, pro-you, join political process`
- `HamasOrganizeWithInternationalTerror` (organize with international terror): -20 usa approval, -15 israeli prime minister approval, -13 israeli public approval, -10 un approval, -7 arab world approval, +12 endreport; Hamas sleeps 6 turns (difficulty-adjusted) — event `hamas, anti-israel, organize with international terror`
- `HamasPartialDisarm` (partial disarmament): +4 government authority, +3 fatah approval, +3 israeli prime minister approval, +3 israeli public approval, +3 palestinian public approval, +3 un approval, +3 usa approval, +1 leadership, +1 tolerance; Hamas sleeps 4 turns — event `hamas, pro-you, partial disarmament`
- `HamasProYouWords` (words): +4 palestinian public approval, +3 fatah approval, +1 government authority; Hamas sleeps 4 turns — event `hamas, pro-you, words`

</details>

### palestinian · Fatah

- If Fatah likes us... — if `fatah approval` ≥ rand(80±20)
  - then:
    - Test for Fatah Partial Disarm.. — if roll `flip` ∈ 0..1 and `flip` = 1
      - then:
        - Test for Fatah approval again.. (but i think this is redundant) — if `fatah approval` ≥ rand(70±5)
          - then → `FatahPartialDisarm`
    - Test for FatahCommitToReconstruction or FatahAntiCorruption or fail to ProWords.. — if `fatah approval` ≥ rand(55±5)
      - then:
        - Test for FatahCommitToReconstruction or FatahAntiCorruption.. — if roll `flip` ∈ 0..1 and `flip` = 0
          - then → `FatahCommitToReconstruction`
          - else → `FatahAntiCorruption`
      - else → `FatahProYouWords`
- If Fatah really hates us... _(else)_ — if `fatah approval` < rand(30±30) and roll `flip` ∈ 0..1 and `flip` = 0
  - then:
    - Test for Fatah Attack on you.. — if `fatah approval` < rand(15±5)
      - then → `FatahAttackOnYou`
    - Test for Fatah anti words or political maneuvering — if roll `flip` ∈ 0..1 and `flip` = 1
      - then → `FatahAntiYouWords`
      - else → `FatahPoliticalManeuvering`
- Fatah Anti Israel Default.. _(else)_ — if `tolerance` < rand(100±30)
  - then:
    -  — if roll `roll` ∈ 0..7
      - then:
        - Test for Fatah extreme attack.. — if `tolerance` < rand(30±5) and `roll` = 0
          - then → `FatahExtremeAttack`
    - Test for Fatah Attack.. — if `tolerance` < rand(50±5) and `roll` < 3
      - then → `FatahAttack`
    - Test for Fatah Funds.. — if `roll` = 8
      - then → `FatahFunds`
    - Test for Fatah Anti Israel Words.. — if `roll` = 7
      - then → `FatahAntiIsraelWords`

<details><summary>Outcome effects</summary>

- `FatahAntiCorruption` (anti-corruption measure): +3 palestinian public approval, +2 government authority, +2 hamas approval, +1 arab world approval, +1 economy, +1 un approval; Fatah sleeps 4 turns — event `fatah, pro-you, anti-corruption measure`
- `FatahAntiIsraelWords` (words): -5 israeli public approval, -4 israeli prime minister approval, -3 israeli cooperation, -1 un approval, -1 usa approval, +3 endreport; Fatah sleeps 2 turns (difficulty-adjusted) — event `fatah, anti-israel, words`
- `FatahAntiYouWords` (words): -5 palestinian public approval, -4 hamas approval, -3 government authority; Fatah sleeps 2 turns (difficulty-adjusted) — event `fatah, anti-you, words`
- `FatahAttack` (attack): -9 usa approval, -7 israeli prime minister approval, -7 israeli public approval, -7 un approval, -5 israeli cooperation, -4 arab world approval, +10 endreport; Fatah sleeps 4 turns (difficulty-adjusted) — event `fatah, anti-israel, attack`
- `FatahAttackOnYou` (attack on your organization): -8 palestinian public approval, -6 hamas approval, -5 government authority, -2 leadership, +9 endreport; Fatah sleeps 4 turns (difficulty-adjusted) — event `fatah, anti-you, attack on your organization`
- `FatahCommitToReconstruction` (commit to reconstruction): +3 palestinian public approval, +2 economy, +2 un approval, +1 hamas approval, +1 israeli prime minister approval, +1 israeli public approval, +1 leadership; Fatah sleeps 4 turns — event `fatah, pro-you, commit to reconstruction`
- `FatahExtremeAttack` (extreme attack): -13 usa approval, -12 israeli prime minister approval, -12 israeli public approval, -12 un approval, -10 israeli cooperation, -8 arab world approval, +20 endreport; Fatah sleeps 4 turns (difficulty-adjusted) — event `fatah, anti-israel, extreme attack`
- `FatahFunds` (funds): -6 israeli prime minister approval, -6 israeli public approval, -4 usa approval, -3 arab world approval, -3 un approval, +3 endreport; Fatah sleeps 4 turns (difficulty-adjusted) — event `fatah, anti-israel, funds`
- `FatahPartialDisarm` (partial disarmament of military wing): +4 usa approval, -3 hamas approval, -3 palestinian public approval, +2 israeli prime minister approval, +2 israeli public approval, +1 arab world approval, +1 government authority, +1 israeli cooperation, +1 leadership, +1 un approval; Fatah sleeps 4 turns — event `fatah, pro-you, partial disarmament of military wing`
- `FatahPoliticalManeuvering` (political maneuvering): -5 palestinian public approval, -3 government authority, -2 hamas approval, -1 leadership, -1 tolerance, +3 endreport; Fatah sleeps 4 turns (difficulty-adjusted) — event `fatah, anti-you, political maneuvering`
- `FatahProYouWords` (words): +3 palestinian public approval, +1 hamas approval; Fatah sleeps 4 turns — event `fatah, pro-you, words`

</details>

### palestinian · Israeli Prime Minister

- No Action test.. — if roll `flip` ∈ 0..1 and `flip` = 0
  - then → `NoAction`
- IPM Pro You test... _(else)_ — if `israeli prime minister approval` ≥ rand(45±10)
  - then:
    - roll for IPM pro you choice.. — if roll `roll` ∈ 0..2
      - then:
        - IsraeliOfferAidInConstruction test.. — if `roll` = 0
          - then → `IsraeliOfferAidInConstruction`
        - IsraeliRemoveSecurityMeasure test.. _(else)_ — if `roll` = 1
          - then → `IsraeliRemoveSecurityMeasure`
        - IsraeliApologize test.. _(else)_ — if `roll` = 2
          - then → `IsraeliApologize`
- IPM Anti You test... _(else)_ — if `israeli prime minister approval` < rand(30±30)
  - then:
    - roll for IPM anti you choice.. — if roll `roll` ∈ 0..8
      - then:
        - IsraeliExtremeSecurityAct test.. — if `roll` = 0 and `israeli prime minister approval` < rand(20±5)
          - then → `IsraeliExtremeSecurityAct`
        - IsraeliSecurityMeasures test.. _(else)_ — if `roll` < 5
          - then → `IsraeliSecurityMeasures`
        - default case.. _(else)_ — if always
          - then → `IsraeliBlameYou`

<details><summary>Outcome effects</summary>

- `IsraeliApologize` (apologize for actions): +5 fatah approval, +5 hamas approval, +5 palestinian public approval, +3 tolerance, +2 israeli cooperation, +1 independence; Israeli Prime Minister sleeps 4 turns — event `israel pm, pro-peace, apologize for actions`
- `IsraeliBlameYou` (blame you): -3 israeli public approval, -2 israeli cooperation, -2 usa approval, -1 independence, -1 tolerance, -1 un approval, +7 endreport; Israeli Prime Minister sleeps 4 turns (difficulty-adjusted) — event `israel pm, anti-terror, blame you`
- `IsraeliExtremeSecurityAct` (extreme security act): -9 economy, -5 independence, -4 fatah approval, -4 hamas approval, -4 palestinian public approval, -3 israeli cooperation, -3 tolerance, -2 government authority, -1 leadership, +13 endreport; Israeli Prime Minister sleeps 5 turns (difficulty-adjusted) — event `israel pm, anti-terror, extreme security act`
- `IsraeliOfferAidInConstruction` (offer aid in construction): +10 budget, +2 israeli cooperation, +1 economy; Israeli Prime Minister sleeps 4 turns — event `israel pm, pro-reconstruction, offer aid in construction`
- `IsraeliRemoveSecurityMeasure` (remove a security measure): +3 independence, +3 palestinian public approval, +2 economy, +2 hamas approval, +1 fatah approval, +1 israeli cooperation, +1 leadership, +1 tolerance, +2 endreport; Israeli Prime Minister sleeps 4 turns — event `israel pm, pro-peace, remove a security measure`
- `IsraeliSecurityMeasures` (security measures): -7 palestinian public approval, -6 fatah approval, -5 hamas approval, -3 independence, -2 economy, -1 israeli cooperation, -1 tolerance, +10 endreport; Israeli Prime Minister sleeps 4 turns (difficulty-adjusted) — event `israel pm, anti-terror, security measures`

</details>

### palestinian · Palestinian Public

- feedbackAboutPeaceProcess test.. — if roll `flip` ∈ 0..1 and `flip` = 0
  - then:
    - PalestinianPublicEnthusiastic test.. — if `independence` ≥ rand(80±20)
      - then → `PalestinianPublicEnthusiastic`
    - PalestinianPublicDesireAction test.. _(else)_ — if `independence` ≥ rand(40±10)
      - then → `PalestinianPublicDesireAction`
    - PalestinianPublicAngry test.. _(else)_ — if `independence` < rand(10±5)
      - then → `PalestinianPublicAngry`
  - else:
    - flip for approval or economy.. — if roll `flip` ∈ 0..1 and `flip` = 0
      - then:
        - test for PalestinianPublicReconstruction.. — if `economy` ≥ rand(70±5)
          - then → `PalestinianPublicReconstruction`
        - test for PalestinianPublicMaterialNeeds.. — if `economy` ≥ rand(10±10)
          - then → `PalestinianPublicMaterialNeeds`
        - No action.. — if always
          - then → `NoAction`
      - else:
        - PalestinianPublicRights test.. — if `palestinian public approval` < rand(20±5)
          - then → `PalestinianPublicRights`
        - PalestinianPublicSupportFatah or PalestinianPublicSupportHamas test.. _(else)_ — if `palestinian public approval` < rand(40±5)
          - then:
            - pick fatah or hamas now.. — if `tolerance` ≥ rand(25±5)
              - then → `PalestinianPublicSupportFatah`
              - else → `PalestinianPublicSupportHamas`
        - PalestinianPublicSupportPresident test.. _(else)_ — if `palestinian public approval` ≥ rand(75±5)
          - then → `PalestinianPublicSupportPresident`

<details><summary>Outcome effects</summary>

- `PalestinianPublicAngry` (angry): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about peace process, angry`
- `PalestinianPublicDesireAction` (desire action): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about peace process, desire action`
- `PalestinianPublicEnthusiastic` (enthusiastic): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about peace process, enthusiastic`
- `PalestinianPublicMaterialNeeds` (material needs): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about government, negative, material needs`
- `PalestinianPublicReconstruction` (reconstruction): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about government, positive, reconstruction`
- `PalestinianPublicRights` (rights): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about government, negative, rights`
- `PalestinianPublicSupportFatah` (support fatah): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about government, negative, support fatah`
- `PalestinianPublicSupportHamas` (support hamas): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about government, negative, support hamas`
- `PalestinianPublicSupportPresident` (support): —; Palestinian Public sleeps 4 turns — event `palestinian public, feedback about government, positive, support`

</details>

### palestinian · Yesha

- roll for yesha action.. — if roll `roll` ∈ 0..2 and `roll` = 0
  - then:
    - pre roll 8 sided.. — if roll `roll` ∈ 0..7
      - then:
        - PPYeshaAntiPalestineIllegalExpansion test — if `roll` < 2
          - then → `PPYeshaAntiPalestineIllegalExpansion`
        - PPYeshaAntiPalestineAssault test — if `roll` < 5
          - then → `PPYeshaAntiPalestineAssault`
        - default case PPYeshaAntiPalestineHarassment.. — if always
          - then → `PPYeshaAntiPalestineHarassment`

<details><summary>Outcome effects</summary>

- `PPYeshaAntiPalestineAssault` (success): -4 palestinian public approval, -3 fatah approval, -3 hamas approval, -1 arab world approval, -1 government authority, -1 independence, -1 leadership, -1 tolerance, +8 endreport; Yesha sleeps 4 turns (difficulty-adjusted) — event `yesha, anti-palestine, assault`
- `PPYeshaAntiPalestineHarassment` (success): -3 palestinian public approval, -2 fatah approval, -2 hamas approval, -1 government authority, -1 independence, -1 tolerance, +5 endreport; Yesha sleeps 4 turns (difficulty-adjusted) — event `yesha, anti-palestine, harassment`
- `PPYeshaAntiPalestineIllegalExpansion` (success): -5 palestinian public approval, -4 fatah approval, -4 hamas approval, -2 arab world approval, -2 government authority, -2 tolerance, -1 economy, -1 independence, -1 leadership, +10 endreport; Yesha sleeps 4 turns (difficulty-adjusted) — event `yesha, anti-palestine, illegal expansion`

</details>


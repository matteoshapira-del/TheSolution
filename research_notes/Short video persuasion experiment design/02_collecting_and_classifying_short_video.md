# Collecting, archiving and classifying short-form video (YouTube Shorts, Instagram Reels, TikTok) on the Israeli–Palestinian conflict for research corpora and experimental stimuli (as of November 2026)

Scope note: this covers Israel, the EU and the US. It is not legal advice. Wherever a source was secondary, dated or in conflict with another, that is flagged. Each "Cited Findings" item has a URL; items without a verifiable source were moved to "Gaps".

---

## A1. What do YouTube, Instagram/Meta and TikTok terms say about downloading, scraping and storing content?

### Takeaway
All three platforms' consumer terms ban automated collection without written permission. YouTube also bans downloading except through the service's own features, and YouTube's API policies separately ban storing copies of audiovisual content. The main US case, *Meta v. Bright Data* (2024), held that Meta's terms reach only logged-in scraping. Even so, terms are contracts, and breaching them carries account and civil risk that is separate from copyright.

### Cited Findings
**YouTube**
- YouTube Terms of Service (dated 15 Dec 2023), "Permissions and Restrictions": users may not "access, reproduce, download, distribute, transmit" any part of the Service or Content except "as expressly authorized by the Service" or "with prior written permission from YouTube and, if applicable, the respective rights holders" — [YouTube ToS](https://www.youtube.com/static?template=terms)
- The same terms forbid accessing the Service "using any automated means (such as robots, botnets or scrapers)", except for public search engines following robots.txt or "with YouTube's prior written permission" — [YouTube ToS](https://www.youtube.com/static?template=terms)
- YouTube API Services Developer Policies III.E.1.a: API clients must not "download, import, backup, cache, or store copies of YouTube audiovisual content without YouTube's prior written approval"; III.E.6 bans scraping YouTube Applications; III.E.4 requires API data to be deleted or refreshed after 30 calendar days (statistics stored as Non-Authorized Data for no more than 30 days) — [YouTube Developer Policies](https://developers.google.com/youtube/terms/developer-policies)
- Under the derived-metrics policy, accepted use cases may keep some statistical data beyond 30 days. Titles, creator names, descriptions and comment text stay under the 30-day refresh/deletion rule — [YouTube derived metrics policy](https://developers.google.com/youtube/terms/derived-metrics-policy?hl=en)

**Instagram / Meta**
- Instagram Terms of Use: users can't "access or collect information in unauthorized ways", and this "includes creating accounts or collecting information in an automated way without our express permission" — [Instagram Terms of Use (Help Center)](https://help.instagram.com/581066165581870); wording also preserved in a 2019 court-filed copy — [court copy of ToU](https://www.lb7.uscourts.gov/documents/19-1861URL1Termsofuse.pdf)
- Meta has enforced this in court: in December 2021 it sued Social Data Trading Ltd. over bot scraping of public Instagram profiles — [Nixon Peabody](https://www.nixonpeabody.com/insights/articles/2021/12/23/meta-attempts-to-stop-scraping-of-instagram-user-data)
- *Meta Platforms v. Bright Data* (N.D. Cal., No. 3:23-cv-00077-EMC, 23 Jan 2024): Judge Chen held that Meta's terms "do not apply to and prohibit Bright Data's scraping of publicly available data while logged off". Meta had not shown logged-in scraping, and terms could not bind a former account holder after termination — [Farella Braun + Martel](https://www.fbm.com/data-analytics/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/); [Eric Goldman blog](https://blog.ericgoldman.org/?p=26009)
- Meta later dropped the case and waived appeal, so the ruling is a district-court decision, not appellate precedent. Commentators disagree on how far it reaches, because it turned on Meta's specific drafting — [MediaPost](https://www.mediapost.com/publications/article/393996/None); [Farella Braun + Martel](https://www.fbm.com/data-analytics/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/)
- Open Terms Archive recorded that Instagram tightened data-retrieval restrictions and clarified what information it retrieves — [Open Terms Archive memo](https://opentermsarchive.org/en/memos/instagram-blocks-data-retrieval-and-clarifies-what-information-it-retrieves/)

**TikTok**
- TikTok Terms of Service (EEA/UK/Switzerland version, "Last updated: July 2026") prohibit users from "extract[ing] any data or content from the Platform using any automated system or software that is not provided by TikTok" unless TikTok approves in writing — [TikTok ToS (EEA)](https://www.tiktok.com/legal/page/eea/terms-of-service/en)
- Under the same terms, users get "a non-exclusive, royalty-free, worldwide licence to access and use your content" for entertainment purposes, "subject to your Platform settings". Creators can restrict downloading, and "Nothing in these Terms affects any rights you are given by law" — [TikTok ToS (EEA)](https://www.tiktok.com/legal/page/eea/terms-of-service/en)

**US computer-crime law context**
- *Meta v. Bright Data* builds on the *hiQ Labs v. LinkedIn* line of cases, in which scraping public data was held not to amount to unauthorized access — [Farella Braun + Martel](https://www.fbm.com/data-analytics/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/)
- *Sandvig v. Barr* (D.D.C. 2020): academic researchers challenged the CFAA's application to research that violates website terms. The court held that breaching terms of service for such research was not a CFAA crime — [ACLU case page](https://www.aclu.org/cases/sandvig-v-barr-challenge-cfaa-prohibition-uncovering-racial-discrimination-online)

### Inferences
- For a team in Israel, the realistic exposure from breaching terms is account suspension, IP blocking, cease-and-desist letters or a contract claim. Criminal liability is unlikely. The *Bright Data* reasoning suggests logged-off collection of public pages is lower-risk than logged-in collection, but it has not been tested in Israeli or EU courts.
- YouTube is the strictest on paper: both the consumer ToS and the API policies bar downloading audiovisual files. Holding downloaded Shorts depends on a copyright exception (A3), not on the terms.
- TikTok's licence to other users is limited to "entertainment purposes", so a research download made with the in-app download button still falls outside the user licence. It would rest on a statutory exception, which TikTok's terms expressly preserve ("rights you are given by law").

### Gaps
- I did not retrieve TikTok's "Rest of World" terms, which would most likely apply to Israel-based accounts. The EEA wording is assumed to be similar but was not verified.
- I did not verify the current text of Meta's separate "Automated Data Collection Terms".
- No Israeli case law on ToS-violating research scraping was found.

---

## A2. Official research access as of November 2026: YouTube Researcher Program, Meta Content Library/API, TikTok Research API, DSA Article 40

### Takeaway
None of the official programmes reliably supplies video files. YouTube and TikTok give metadata (TikTok adds a speech-to-text field). Meta lets researchers view Reels inside a controlled environment, but downloads are limited and data must stay in a cleanroom. Israeli academics are explicitly eligible for YouTube's programme and are not excluded from Meta's, but TikTok's eligibility list does not include Israel. DSA Article 40 is in force (vetted access since 29 Oct 2025), but practical results were close to zero as of mid-2026. Its value to an Israeli team most likely depends on an EU-affiliated partner.

### Cited Findings
**YouTube Researcher Program**
- Eligibility: "a student, research-focused staff, or faculty member affiliated with an accredited higher-learning institution". Institutions must be "accredited and degree granting", "not-for profit", and "pass an ethics & compliance check". Israel is on the list of eligible countries — [YouTube Researcher Program: How it works](https://research.youtube.com/how-it-works)
- Data: "scaled, expanded access to global video metadata across the entire public YouTube corpus via our Data API". Video files are not mentioned — [How it works](https://research.youtube.com/how-it-works)
- Refresh: "You agree to regularly refresh Program Data as specified by the Developer API ToS (i.e. every 30 days) until such time as you need the Program Data to be fixed as to a point in time" — [Program Terms & Conditions](https://research.youtube.com/policies/terms)
- The default Data API quota is 10,000 units/day; search costs 100 units per query. Researcher Program quota increases require a new application — [Rieder et al. audit, arXiv](https://arxiv.org/abs/2506.11727); [YouTube quota calculator](https://developers.google.com/youtube/v3/determine_quota_cost?hl=he)
- Rieder, Padilla & Coromina (2025) "Forgetful by Design?" audited the search endpoint and found it "not adequate for robust academic research" because it seems to prioritise "freshness" over complete retrieval — [arXiv 2506.11727](https://arxiv.org/abs/2506.11727)

**Meta Content Library (MCL) and API (CrowdTangle's successor)**
- Covers public content from Facebook, Instagram, Threads and WhatsApp Channels. The web tool lets users "explore and analyze photos, videos and reels", and the API offers "over 100 data fields" — [Meta Transparency Center: MCL](https://transparency.meta.com/researchtools/meta-content-library/)
- Eligibility: affiliation with an academic institution, or a not-for-profit whose core purpose is scientific or public-interest research. "Public content is available from most countries/territories". Applicants in US/UK/EU/UN-sanctioned jurisdictions are excluded. No educational-level requirement — [Meta Transparency Center: MCL](https://transparency.meta.com/researchtools/meta-content-library/)
- Review body conflict: the Transparency Center says CASD (Secure Data Access Center) independently reviews applications, while Meta's developer docs say ICPSR processes them — [Meta Transparency Center](https://transparency.meta.com/researchtools/meta-content-library/); [Meta developer docs](https://developers.facebook.com/docs/content-library-and-api)
- Access mode: API data "can be analyzed in a cleanroom environment" (ICPSR SOMAR Virtual Data Enclave or Meta's Secure Research Environment). Local downloading of API data is prohibited. CSV export from the UI is limited to "widely-known" accounts (Facebook Pages with 15,000+ likes/followers; profiles that are verified or have 25,000+ followers). Each researcher has a UI budget of 500,000 results per rolling seven days, and search access does not automatically include download rights — [Bellingcat Toolkit: MCL README (checked 2026-10-29)](https://github.com/bellingcat/toolkit/blob/main/gitbook/tools/meta-content-library/README.md); [Meta Transparency Center](https://transparency.meta.com/researchtools/meta-content-library/)
- Fees conflict: Meta says there are no fees on its Secure Research Environment. Bellingcat, citing SOMAR's Summer 2026 newsletter, reports a one-time USD 1,000 setup fee plus USD 371/month for new ICPSR VDE instances — [Meta Transparency Center](https://transparency.meta.com/researchtools/meta-content-library/); [Bellingcat README](https://github.com/bellingcat/toolkit/blob/main/gitbook/tools/meta-content-library/README.md)
- Researchers may publish without Meta's prior approval but must follow attribution guidelines and give notice — [Meta Transparency Center](https://transparency.meta.com/researchtools/meta-content-library/)
- Longitudinal tracking of individuals and surveillance or commercial use are not permitted — [Bellingcat README](https://github.com/bellingcat/toolkit/blob/main/gitbook/tools/meta-content-library/README.md)
- CJR (Tow Center) argued that MCL is less transparent and less accessible than CrowdTangle — [CJR](https://www.cjr.org/tow_center/meta-is-getting-rid-of-crowdtangle.php)

**TikTok Research API**
- Eligibility: academic institutions in the US, EEA, UK, Canada or Switzerland; not-for-profit research bodies in the EU (beta, with select researchers in the US, UK, Switzerland, Norway, Iceland and Liechtenstein); Brazilian academics/NGOs studying youth safety; non-academic non-profits "under limited conditions" via a Virtual Compute Environment. Israel is not named, and TikTok says it is "working to expand access". Applicants need ethical review evidence, independence from commercial interests, funding disclosure and data security — [TikTok Research API product page](https://developers.tiktok.com/products/research-api/)
- Access is per project/lab. The principal researcher can add up to 9 collaborators, and a developer account alone is insufficient — [TikTok Research API FAQ](https://developers.tiktok.com/doc/research-api-faq)
- Video fields include id, create_time, username, region_code, video_description, music_id, like/comment/share/view/favorites counts, effect_ids, hashtags, video_mention_list, video_label, playlist_id, **voice_to_text**, is_stem_verified and video_duration. No media file or direct media URL is returned; the ID "can be used to reconstruct the URL link". Videos covered are public videos from creators aged 18+ — [TikTok Research API codebook](https://developers.tiktok.com/doc/research-api-codebook)
- New videos take up to 48 hours to become searchable, and statistics can take up to 10 days to update — [TikTok Research API FAQ](https://developers.tiktok.com/doc/research-api-faq)
- Terms reported at launch (2023): refresh data "at least every fifteen (15) days, and delete data that is not available from the TikTok Research API at the time of each refresh"; certify deletion on request; provide TikTok a copy "at least thirty days before its publication for courtesy" — [Tech Policy Press](https://techpolicy.press/tiktoks-api-guidelines-are-a-minefield-for-researchers); [Technomoral substack](https://technomoral.substack.com/p/researcher-beware-four-red-flags). I could not confirm these against the current Research Tools Terms.
- Platforms compared: TikTok refresh every 15 days, YouTube every 30 days — [Tech Policy Press comparison](https://techpolicy.press/comparing-platform-research-api-requirements)
- Reliability: AI Forensics (Feb 2025) reported the API "seems to be not fully functional for several months" — [AI Forensics](https://www.aiforensics.org/work/tiktok-research-api). A Slovak team (KInIT) reported 21 months, from 19 Dec 2023 to 30 Sep 2025, before obtaining working access — [KInIT](https://kinit.sk/when-research-apis-close-the-door/). See also "TikTok's Research API: Problems Without Explanations" — [arXiv 2506.09746](https://arxiv.org/abs/2506.09746). A 2026 Essex study evaluates bias in API outputs — [Bai & Gu 2026 (Essex repository)](https://repository.essex.ac.uk/42550/1/bai-gu-2026-harnessing-big-data-hindered-by-bias-evaluating-tiktok-research-api-for-fair-and-optimal-social-sciences.pdf)

**EU DSA Article 40 (vetted researchers, Art. 40(4); public data, Art. 40(12))**
- The Commission adopted the delegated act on data access on 2 July 2025 — [European Commission news](https://digital-strategy.ec.europa.eu/en/news/commission-adopts-delegated-act-data-access-under-digital-services-act). It is Commission Delegated Regulation (EU) 2025/2050, dated 1 July 2025 and published in the OJ on 9 Oct 2025 — [EUR-Lex 2025/2050](https://eur-lex.europa.eu/eli/reg_del/2025/2050/oj); [Springlex consolidated text](https://www.springlex.eu/en/packages/dsa/davr-regulation/). According to the Commission FAQ, "As of 29 October 2025, the delegated act entered into force" and applications opened then — [Commission FAQ](https://algorithmic-transparency.ec.europa.eu/news/faqs-dsa-data-access-researchers-2025-07-03_en). (A law-firm summary gave 21 July 2025 as the entry-into-force date; this conflicts with the Commission FAQ — [VBB](https://vbb.com/wp-content/uploads/2025/11/20250718_Delegated_Act_on_Data_Access_under_the_DSA.pdf).)
- Applications go through the DSA Data Access Portal (data-access.dsa.ec.europa.eu) to either "the DSC of the Member State where their affiliated research organisation is based" or the DSC of the provider's establishment. Within "80 working days" the DSC must issue a reasoned request or explain why not — [Commission FAQ](https://algorithmic-transparency.ec.europa.eu/news/faqs-dsa-data-access-researchers-2025-07-03_en)
- Vetted status requires affiliation with "a research institution (as defined in Art. 2(1) of Directive 2019/790)", independence from commercial interests, data security, and research on EU systemic risks. The FAQ does not say whether non-EU institutions qualify — [Commission FAQ](https://algorithmic-transparency.ec.europa.eu/news/faqs-dsa-data-access-researchers-2025-07-03_en); [Hogan Lovells](https://www.hlc.com/en/publications/who-gets-to-see-inside-the-eus-new-rules-on-data-access-under-article-40-of-the-dsa)
- Access can be data transmission or a secure processing environment ("no data would be transmitted"). Where third-country transfers of personal data occur, access modalities must include a GDPR Chapter V transfer mechanism (Recital 17) — [Commission FAQ](https://algorithmic-transparency.ec.europa.eu/news/faqs-dsa-data-access-researchers-2025-07-03_en); [Springlex recitals](https://www.springlex.eu/en/packages/dsa/davr-regulation/)
- Retention: providers "should not impose archiving, storage, refresh and deletion requirements, unless they are explicitly mentioned" in the DSC's access modalities (Recital 29) — [Springlex](https://www.springlex.eu/en/packages/dsa/davr-regulation/); [Commission FAQ](https://algorithmic-transparency.ec.europa.eu/news/faqs-dsa-data-access-researchers-2025-07-03_en)
- Providers must publish "DSA data catalogues", which are not exhaustive. Providers can request mediation (voluntary) — [Springlex](https://www.springlex.eu/en/packages/dsa/davr-regulation/); [Hogan Lovells](https://www.hlc.com/en/publications/who-gets-to-see-inside-the-eus-new-rules-on-data-access-under-article-40-of-the-dsa)
- Art. 40(12) public-data access sits outside the delegated act. It has no DSC vetting, and the requester need not be an academic ("including those affiliated to not for profit bodies, organizations and associations"). The Commission has treated scraping as a required access method under 40(12) in the AliExpress commitments and in its X findings — [Tech Policy Press](https://www.techpolicy.press/determining-which-researchers-can-collect-public-data-under-the-dsa/)
- On 24 Oct 2025 the Commission preliminarily found TikTok and Meta in breach of the obligation to grant researchers "adequate access to public data" — [European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktok-and-meta-breach-their-transparency-obligations-under-digital). The maximum possible fine is 6% of worldwide turnover — [PPC Land](https://ppc.land/eu-finds-tiktok-and-meta-in-breach-of-digital-services-act-transparency-rules/)
- X was fined €120 million on 5 Dec 2025 (blue checks, ad repository, researcher data access), the first DSA non-compliance decision — [PPC Land](https://ppc.land/tiktok-faces-fine-of-up-to-6-over-for-you-feed-rabbit-holes/); [EU Law Analysis](http://eulawanalysis.blogspot.com/2026/02/digital-services-act-summary-and-links.html). The Commission accepted X's corrective plan in July 2026 — [Tech Policy Press](https://www.techpolicy.press/what-xs-corrected-action-under-the-dsa-fixes-on-data-access-and-whats-left-open/)
- In practice: "As of July 2026, 9 months after Article 40.4 came fully into effect, there had been 77 applications but no known successes" (the author's own figure, uncited). The Irish DSC (Coimisiún na Meán) rejected an AlgorithmWatch request after about 80 working days, citing storage/cybersecurity detail and proportionality. Portal "malfunctions" are also reported. A joint 40(12) request by about 20 organisations to six VLOPs (including YouTube, TikTok and Instagram) had not been granted by any platform — [DSA Observatory, Oct 2026](https://dsa-observatory.eu/2026/10/02/two-stories-of-dsa-data-non-access-from-an-ngo-perspective/); [DSA Observatory, Mar 2026](https://dsa-observatory.eu/2026/03/12/if-at-first-you-dont-succeed-reflections-on-a-rejected-art-40-dsa-data-access-request/)
- The Commission and DSCs held a roundtable on 19 May 2026 to launch the first requests — [European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-holds-roundtable-data-access-vetted-researchers). A GLOBSEC survey of 34 experts found timelines of up to nine months were seen as incompatible with research — [GLOBSEC](https://www.globsec.org/publications/dsa-data-access-for-researchers-state-of-play-2025)

### Inferences
- For a team in Israel: YouTube's programme is directly available but gives metadata only. Meta's MCL is likely available (Israel is not a sanctioned jurisdiction), but Reels can only be viewed and analysed inside the cleanroom, which may not suit stimulus extraction. TikTok's API requires an eligible co-investigator (US, EEA, UK, Canada or Switzerland) as principal researcher. DSA 40(4) most plausibly works with an EU research organisation as applicant; Israel's EU adequacy status should ease Chapter V transfer questions (see A4).
- Because official channels do not deliver video files, a coded multimodal corpus (frames, audio, on-screen text) will almost certainly need self-collection under a copyright exception, or coding done within platform-hosted viewing environments.
- TikTok's 15-day and YouTube's 30-day refresh/delete rules conflict with reproducibility and with studying removed content. DSA Recital 29 is the only regime that limits providers' power to impose such rules.

### Gaps
- The text of Delegated Regulation 2025/2050 Articles 9 and 15 (access modalities, data documentation) was not retrieved, and there is no definitive statement on non-EU research organisations.
- No official count of granted vetted-researcher requests was found.
- Whether MCL lets researchers download Reels video files (as opposed to viewing them) was not confirmed.
- The current TikTok Research Tools Terms (2026 version) were not retrieved, so the 15-day refresh and the 30-day pre-publication copy are confirmed only for 2023.

---

## A3. Copyright: research exceptions, use of clips as experimental stimuli, and embedding instead of downloading

### Takeaway
All four jurisdictions offer a research route, but they differ in kind. Israel (s.19) and the US (§107) use flexible, factor-based fair use that names research. The EU (DSM Art. 3) and the UK (s.29A) give narrower but contract-proof text-and-data-mining exceptions that cover computational analysis, not showing clips to participants. Downloading from YouTube can also raise anti-circumvention issues: a German appeals court held that YouTube's "rolling cipher" is an effective technical protection measure. Embedding through official players or oEmbed avoids reproduction, but it comes with its own terms and gives up experimental control.

### Cited Findings
**Israel**
- Copyright Act 2007, s.19(a): "Fair use of a work is permitted for purposes such as: private study, research, criticism, review, journalistic reporting, quotation, or instruction and examination by an educational institution". s.19(b) factors: purpose and character of the use; character of the work; scope of use "quantitatively and qualitatively"; "impact of the use on the value of the work and its potential market". s.19(c) allows the Minister to make regulations — [unofficial English translation (droit-technologie.org)](https://www.droit-technologie.org/wp-content/uploads/2016/11/annexes/dossier/214-1.pdf); [WIPO Lex entry](https://www.wipo.int/wipolex/en/legislation/details/5016)
- The list is open-ended ("such as"), and the provision closely tracks US §107 — [Infojustice](https://infojustice.org/?p=20276); [Stanford CIS](https://cyberlaw.stanford.edu/blog/2008/01/israels-fair-use/)
- s.22 permits incidental use of a work included in a photographic or cinematographic work, but deliberate inclusion of music is not incidental. This matters because Reels and TikToks often carry music — [unofficial translation](https://www.droit-technologie.org/wp-content/uploads/2016/11/annexes/dossier/214-1.pdf)
- Ministry of Justice opinion (18 Dec 2022): ML training on copyrighted works generally qualifies as fair use under s.19 (it fits "research" and "private study" and is transformative). s.26 (transient copies) may also apply if copies are deleted. The opinion is not binding on courts and does not cover outputs — [Herzog Fox & Neeman](https://herzoglaw.co.il/en/news-and-insights/ministry-of-justice-opinion-on-the-use-of-copyrighted-works-for-machine-learning-purposes/); [Pearl Cohen](https://www.pearlcohen.com/israeli-ministry-of-justice-opines-on-fair-use-of-copyrighted-content-for-ai-ml-training/); [Infojustice](https://infojustice.org/?p=44989)
- Bar-Ilan University library guidance on copyright and fair use for academic users — [BIU Library](https://lib.biu.ac.il/en/Copyrights)

**United States**
- 17 U.S.C. §107 names "teaching ..., scholarship, or research" as illustrative purposes and sets out four factors — [17 U.S.C. §107 (Cornell LII)](https://www.law.cornell.edu/uscode/text/17/107)
- DMCA §1201 exemption for TDM on motion pictures by researchers affiliated with nonprofit institutions of higher education, for scholarly research and teaching (37 C.F.R. 201.40(b)(4)). Renewal was petitioned in 2024 by Authors Alliance, the Library Copyright Alliance and AAUP, and NTIA supported renewal — [Copyright Office renewal petition](https://www.copyright.gov/1201/2024/petitions/renewal/Renewal%20Pet.%20-%20AV%20Educ.%20TDM%20-%20Authors%20Alliance,%20Inc.,%20Library%20Copyright%20Alliance,%20and%20American%20Association%20of%20University%20Professors.pdf); [NTIA letter 2024](https://copyright.gov/1201/2024/2024_NTIA_DMCA_Letter.pdf); [Authors Alliance](https://www.authorsalliance.org/2023/10/19/copyright-office-recommends-renewal-of-the-existing-text-data-mining-exemptions-for-literary-works-and-films/). A 2027 (tenth-cycle) renewal process is under way — [Copyright Office 2027 renewal form](https://www.copyright.gov/1201/2027/renewal-petition.pdf)
- After the RIAA's 2020 DMCA takedown, GitHub reinstated the youtube-dl repository (16 Nov 2020) — [GitHub blog](https://github.blog/2020-11-16-standing-up-for-developers-youtube-dl-is-back/)

**European Union**
- DSM Directive (EU) 2019/790, Art. 3(1) requires Member States to provide an exception for "reproductions and extractions made by research organisations and cultural heritage institutions in order to carry out, for the purposes of scientific research, text and data mining of works ... to which they have lawful access". Art. 3(2): copies "shall be stored with an appropriate level of security and may be retained for the purposes of scientific research, including for the verification of research results". Art. 7(1) makes contractual provisions contrary to Art. 3 unenforceable. Art. 2(1) defines "research organisation" (university, research institute or other entity on a not-for-profit basis or with a public-interest mission). Art. 2(2) defines TDM as "any automated analytical technique aimed at analysing text and data in digital form in order to generate information" — [EUR-Lex Directive 2019/790](https://eur-lex.europa.eu/eli/dir/2019/790/oj) (text quoted from the official Directive; EUR-Lex blocked automated retrieval in this session)
- InfoSoc Directive 2001/29/EC Art. 5(3)(a) lets Member States allow use "for the sole purpose of illustration for teaching or scientific research" with source attribution, to the extent justified by the non-commercial purpose. National implementations vary — [EUR-Lex Directive 2001/29](https://eur-lex.europa.eu/eli/dir/2001/29/oj)
- Anti-circumvention: in March 2023 the Hamburg Regional Court held web host Uberspace liable for aiding circumvention by hosting youtube-dl's site. In Nov 2024 the Hanseatic Higher Regional Court rejected the appeal in full and treated YouTube's "rolling cipher" as an "effective protective measure". Sources disagree on whether a further appeal was possible — [TorrentFreak](https://torrentfreak.com/court-rejects-appeal-of-youtube-dl-hosting-provider-uberspace-241127/); [heise](https://heise.de/-10181247); [Complete Music Update](https://completemusicupdate.com/signposting-youtube-dl-streamripper-not-allowed-confirms-german-appeals-court-as-us-supreme-court-weighs-in-on-majors-v-cox/)

**United Kingdom**
- CDPA s.29A: a person with "lawful access" may copy a work "for the sole purpose of research for a non-commercial purpose" so as to "carry out a computational analysis", with "sufficient acknowledgement". Transferring the copy to another person, or using it for another purpose, infringes. Contract terms that "purport[] to prevent or restrict" such copying are "unenforceable" — [legislation.gov.uk s.29A](https://www.legislation.gov.uk/ukpga/1988/48/section/29A)

**Embedding instead of downloading**
- YouTube embedded-player rules: API clients must not "modify, build upon, or block any portion or functionality of a YouTube player" (III.I.6) or "separate, isolate, or modify the audio or video components" (III.I.7) — [YouTube Developer Policies](https://developers.google.com/youtube/terms/developer-policies)
- Instagram oEmbed "Supports photo, video, Reel, and Feed posts". It is "only meant to be used for embedding Instagram content in websites and apps". Using its metadata or content "for any purpose other than" front-end display is "strictly prohibited". It does not work for private, age-restricted or embed-disabled accounts. Rate limit: 1,000 requests/hour — [Meta: Instagram oEmbed](https://developers.facebook.com/docs/instagram-platform/oembed/)

### Inferences
- **Corpus building (download + automated analysis):** this sits most securely under DSM Art. 3 for EU-partner research organisations, and under s.29A in the UK. Both protect against contract override, which matters because platform terms prohibit downloading. In Israel and the US, fair use plus the MoJ opinion (Israel) supports a non-commercial analytic corpus, and the non-expressive, transformative character of coding strengthens factor 1.
- **Stimuli (showing whole clips to participants):** TDM exceptions do not obviously cover this, because it is communication or display to humans, not "computational analysis". It would rest on Israeli s.19 or US §107 fair use, or on national implementations of InfoSoc 5(3)(a). Factors that help: short excerpts, small closed participant pools, no public redistribution, and a scholarly purpose. Factors that hurt: whole works, licensed music tracks, and stimuli edited in ways that misrepresent creators.
- **Anti-circumvention** is a separate risk from copyright infringement. In Germany and the wider EU, the OLG Hamburg reasoning implies that tools defeating YouTube's cipher circumvent a technical protection measure, and the DSM TDM exception does not automatically authorise circumvention. In the US, the §1201 TDM exemption is the relevant safe harbour, but whether it covers streamed YouTube content (versus "lawfully acquired" copies) is unverified.
- **Embedding** avoids reproduction but cannot be trimmed, captioned uniformly or stripped of engagement counts. Platform deletion mid-study breaks the stimulus. Under YouTube's player rules, separating audio and video for manipulation is barred.

### Gaps
- I did not verify the final 2024 §1201 rule text, including any expansion allowing sharing between institutions.
- No Israeli court decision applying s.19 to research datasets or experimental stimuli was found.
- No source was found on TikTok embed-player terms.
- I could not find an authoritative commentary on whether DSM Art. 3 or s.29A permits showing excerpts to experiment participants.

---

## A4. Data protection: GDPR (Art. 9 political opinions, Art. 89 research) and Israel's Privacy Protection Law with Amendment 13

### Takeaway
Videos of identifiable people expressing positions on the war involve "political opinions", which is special-category data under GDPR Art. 9 and "especially sensitive" data under Israel's amended PPL. The GDPR has a structured research pathway (Art. 9(2)(j) plus Art. 89 safeguards; exemptions from storage limitation, notice and erasure). For Israel I found no explicit research exemption, and the Privacy Protection Authority's 2025 draft AI guidance takes a restrictive view of scraping online personal data.

### Cited Findings
**GDPR (applies to EU partners and to data on people in the EU)**
- Art. 9(1) lists data "revealing ... political opinions, religious or philosophical beliefs" and biometric data (when used for unique identification) as special categories. Exceptions include 9(2)(e) data "manifestly made public by the data subject" and 9(2)(j) processing "necessary for ... scientific or historical research purposes ... in accordance with Article 89(1) based on Union or Member State law" — [GDPR Art. 9 (gdpr-info.eu)](https://gdpr-info.eu/art-9-gdpr/)
- Art. 89(1) requires "appropriate safeguards" and "technical and organisational measures", in particular data minimisation, and names pseudonymisation — [GDPR Art. 89](https://gdpr-info.eu/art-89-gdpr/)
- Art. 5(1)(b) treats further processing for scientific research as compatible with the original purpose, and Art. 5(1)(e) allows longer storage for research subject to Art. 89 — [GDPR Art. 5](https://gdpr-info.eu/art-5-gdpr/)
- Art. 14(5)(b) exempts controllers from notifying data subjects where this "proves impossible or would involve a disproportionate effort", in particular for research under Art. 89 — [GDPR Art. 14](https://gdpr-info.eu/art-14-gdpr/)
- Art. 17(3)(d) limits the right to erasure where erasure would render "impossible or seriously impair" research objectives — [GDPR Art. 17](https://gdpr-info.eu/art-17-gdpr/)
- The EU renewed Israel's adequacy status (January 2024 review), so EU-to-Israel transfers do not need additional transfer tools — [DLA Piper Data Protection: Israel](https://www.dlapiperdataprotection.com/?c=IL)

**Israel: Protection of Privacy Law + Amendment 13**
- Amendment 13 was approved 5 Aug 2024 and took effect 14 Aug 2025 — [DLA Piper](https://www.dlapiperdataprotection.com/?c=IL); [Goldfarb Gross Seligman](https://goldfarb.com/amendment-13-to-the-israeli-privacy-protection-law)
- It replaced "sensitive data" with a broadly defined "Especially Sensitive Data" category that includes "political opinions", "religious beliefs", "biometric identifiers", "genetic data", "location data" and "criminal records" — [DLA Piper](https://www.dlapiperdataprotection.com/?c=IL); [Pearl Cohen](https://www.pearlcohen.com/the-knesset-enacted-a-key-amendment-to-the-israeli-protection-of-privacy-law-summery-version/)
- Unregistered databases holding Especially Sensitive Data on more than 100,000 people must be reported to the Privacy Protection Authority (PPA). A DPO is required for, among others, controllers whose core activities involve "regular and systematic monitoring ... on a Large Scale" or who process Especially Sensitive Data at scale. The PPA gained administrative fine and criminal investigation powers, and statutory damages are available without proof of harm — [DLA Piper](https://www.dlapiperdataprotection.com/?c=IL)
- Processing is framed around "informed consent" that is purpose-specific. New notice contents include the consequences of refusal and controller identity — [DLA Piper](https://www.dlapiperdataprotection.com/?c=IL)
- PPA draft AI guidance (30 Apr 2025; comments closed 5 Jun 2025): unauthorised scraping may be treated as a "serious security incident" reportable to the PPA. Collecting personal data from social media without clear lawful consent may violate the law. Publicly available data may be used for AI training only under defined implied-consent conditions. I could not confirm whether this was finalised — [Gornitzky](https://www.gornitzky.com/privacy-in-artificial-intelligence-systems-guidelines-of-the-israeli-privacy-protection-authority/); [Barnea Jaffa Lande](https://barlaw.co.il/practice_areas/high-tech/ai-regulation/client_updates/israeli-privacy-authority-targets-ai-business-implications-ahead/); [EBN Law](https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/)
- The PPA has published a professional guide to Amendment 13 and a draft DPO guidance — [Digital Policy Alert](https://digitalpolicyalert.org/change/15855-privacy-protection-authority-professional-guide-for-privacy-protection-law-amendment-no-13); [PPC Land](https://ppc.land/israels-privacy-authority-publishes-data-protection-officer-guidance-draft)

### Inferences
- A corpus of war-related Reels/TikToks with faces, names, voices and expressed positions will, under both regimes, contain special-category or Especially Sensitive data. Expect IRB/ethics review, a data management plan, pseudonymised coding sheets that separate account handles from codes, restricted-access storage, and likely a DPIA on the EU side.
- Under the GDPR, the cleanest legal basis for EU partners is public-interest or research processing with Art. 9(2)(j) under national research law. Art. 9(2)(e) ("manifestly made public") is debated for ordinary users and is weaker for minors or bystanders filmed by others.
- In Israel, the absence of an explicit research exemption, together with the PPA's scraping position, makes large-scale scraping of identifiable private users the highest-risk scenario. Prioritising public-figure, organisational, news and state accounts lowers the risk. The 100,000-person reporting threshold is unlikely to be reached by a typical coded corpus.
- Wartime footage often contains victims, including children and casualties, who never chose to be filmed. Ethics review should address this separately from the uploader's privacy.

### Gaps
- The official Hebrew text of Amendment 13 was not reviewed. I could not determine whether any research or academic exemption exists (none was found in English-language summaries).
- No Israeli PPA guidance specific to academic social-media research was found.
- No national (EU Member State) research-law implementation of Art. 9(2)(j) was reviewed.

---

## A5. Deletion and takedowns: content that disappears and whether researchers must delete it

### Takeaway
Under the platform research programmes, deleting removed content is a contractual duty: TikTok requires a refresh every 15 days (2023 terms) and YouTube every 30 days. Data collected under copyright and data-protection exceptions is not bound by those terms. The DSA delegated act tells providers not to impose deletion rules unless the DSC specifies them, and GDPR Art. 17(3)(d) limits erasure that would seriously impair research. For conflict content specifically, removal is common and non-random, which human-rights archivists treat as a reason to preserve.

### Cited Findings
- TikTok (2023 terms) requires deleting "data that is not available from the TikTok Research API at the time of each refresh" every 15 days. Critics note that removed data are "not missing at random", so results may be biased — [Tech Policy Press](https://techpolicy.press/tiktoks-api-guidelines-are-a-minefield-for-researchers); [tikt0k substack](https://tikt0k.substack.com/p/how-tiktok-is-not-supporting-independent)
- YouTube Researcher Program: refresh every 30 days "until such time as you need the Program Data to be fixed as to a point in time" — [YouTube Program Terms](https://research.youtube.com/policies/terms)
- DSA Delegated Regulation Recital 29: providers "should not impose archiving, storage, refresh and deletion requirements, unless they are explicitly mentioned" in access modalities — [Springlex](https://www.springlex.eu/en/packages/dsa/davr-regulation/)
- DSM Art. 3(2) allows TDM copies to be "retained for the purposes of scientific research, including for the verification of research results" — [EUR-Lex 2019/790](https://eur-lex.europa.eu/eli/dir/2019/790/oj)
- GDPR Art. 17(3)(d) research limit on the right to erasure — [GDPR Art. 17](https://gdpr-info.eu/art-17-gdpr/)
- Human Rights Watch (2020), "Video Unavailable", documented platforms removing content that is potential evidence of war crimes and called for preservation and archive access — [HRW](https://www.hrw.org/report/2020/09/10/video-unavailable/social-media-platforms-remove-evidence-war-crimes)
- Regarding Palestinian content in 2024, Global Voices/Sada Social reported platform removals and restrictions ("digital erasure") — [Global Voices](https://globalvoices.org/2025/05/12/digital-erasure-how-social-media-platforms-are-silencing-palestinians-in-2024/)
- The UN OHCHR/UC Berkeley "Berkeley Protocol on Digital Open Source Investigations" sets preservation and chain-of-custody standards for online content — [OHCHR Berkeley Protocol](https://www.ohchr.org/en/publications/policy-and-methodological-publications/berkeley-protocol-digital-open-source)
- AoIR Internet Research Ethics 3.0 (2020) covers the full research lifecycle, including big-data and AI ethics — [AoIR IRE 3.0](https://aoir.org/ire30/)
- Web-archive ethics literature notes that individuals may ask for data to be deleted when it becomes irrelevant, inaccurate or harmful and that harm is not outweighed by public benefit — [Social Science Journal / web archives article](https://distantreader.org/stacks/journals/ssj/ssj-2541.pdf)

### Inferences
- Practical tiering: (1) API-derived metadata must follow programme refresh rules, with a documented "freeze" for analysis where YouTube permits it. (2) Self-collected media held under copyright exceptions may be retained for verification, but access should be restricted and the data not redistributed (s.29A expressly bars transfer to others). (3) Personal data should be minimised and pseudonymised. GDPR research limits on erasure apply on the EU side; the Israeli position is unclear.
- Record "availability status at last check" as a variable. Takedown is itself a research outcome, and it bears on misinformation and fact-check coding.
- For publication and replication, share video IDs/URLs plus codes (a "dehydrated" release) rather than media files. Raw media can be made available to verified researchers on request under a data-use agreement.

### Gaps
- I did not retrieve the IRE 3.0 PDF text on deletion obligations.
- No university policy specific to retaining deleted social-media video was found.
- No Israeli guidance on retaining removed content was found.

---

## B. Tools: yt-dlp, gallery-dl, Instaloader, 4CAT + Zeeschuimer, DMI tools, Junkipedia, Memespector; reliability 2025–2026; metadata to keep

### Takeaway
Collection tools fall into three groups: (1) platform-sanctioned APIs and dashboards (YouTube Data Tools, TikTok Research API, MCL); (2) browser-capture tools that record what a logged-in researcher sees (Zeeschuimer → 4CAT), which are lower-volume and ToS-grey; and (3) command-line downloaders (yt-dlp, gallery-dl, Instaloader), which breach platform terms and, for YouTube, carry anti-circumvention exposure in the EU. All of them broke repeatedly in 2025–2026 as platforms hardened their defences.

### Cited Findings
**yt-dlp** (open-source downloader; extractors for YouTube, TikTok, Instagram and others)
- yt-dlp 2025.11.12 (12 Nov 2025) requires an external JavaScript runtime (Deno recommended; Node, QuickJS, Bun optional) for full YouTube support, because YouTube's decryption code is too complex for the built-in interpreter. Without one, support is "deprecated" and format availability is "limited, and severely so in some cases" — [GIGAZINE](https://www.gigazine.net/gsc_news/en/20251113-yt-dlp-required-deno-javascript-runtime); [yt-dlp GitHub issue #15012](https://github.com/yt-dlp/yt-dlp/issues/15012)
- YouTube is rolling out stricter "PO token" anti-download measures that may defeat a runtime-only setup — [GIGAZINE](https://gigazine.net/gsc_news/en/20250925-yt-dlp-deno-javascript-runtime)
- Legal status: GitHub reinstated youtube-dl in the US after the 2020 RIAA takedown — [GitHub blog](https://github.blog/2020-11-16-standing-up-for-developers-youtube-dl-is-back/). Hamburg courts (2023, 2024) held that hosting youtube-dl aids circumvention of an effective TPM — [TorrentFreak](https://torrentfreak.com/court-rejects-appeal-of-youtube-dl-hosting-provider-uberspace-241127/); [heise](https://heise.de/-10179284). The tool also breaches YouTube's ToS and API policies — [YouTube ToS](https://www.youtube.com/static?template=terms)
- Supported sites list — [yt-dlp supportedsites.md](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

**gallery-dl** (downloader for image/video hosting sites, including Instagram)
- Supported-sites documentation — [gallery-dl supportedsites](https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md). No 2025–2026 reliability assessment was found.

**Instaloader** (Python tool for Instagram posts, Reels, profiles)
- Bellingcat lists v4.15 (Nov 2025) with a `--reels` option — [Bellingcat Toolkit: Instaloader](https://bellingcat.gitbook.io/toolkit/more/all-tools/instaloader). A later v4.15.3 release with commits through July 2026 is reported — [Scrapfly](https://scrapfly.io/blog/posts/best-open-source-instagram-scrapers)
- Anonymous use is heavily rate-limited (401 "please wait", 429). Logged-in sessions trigger verification challenges and risk account bans. The issue tracker shows 403 errors on Reels with fixes in progress during 2025 — [apiserpent (secondary)](https://apiserpent.com/blog/scrape-instagram-for-free); [Instaloader issues (ecosyste.ms)](https://issues.ecosyste.ms/hosts/GitHub/repositories/instaloader%2Finstaloader/issues)
- Logged-in collection falls outside the *Bright Data* logged-off reasoning — [Farella Braun + Martel](https://www.fbm.com/data-analytics/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/)

**4CAT + Zeeschuimer** (Digital Methods Initiative / University of Amsterdam)
- 4CAT is a modular capture-and-analysis toolkit for transparent, traceable social-media research — [Peeters & Hagen, 4CAT paper (UvA DARE)](https://dare.uva.nl/id/0e901cbc-b43f-47a9-a02c-e7bdca873948); [4CAT GitHub](https://www.github.com/digitalmethodsinitiative/4cat)
- Zeeschuimer is a Firefox extension. The researcher scrolls a feed or search results, and it "captures the content that is loaded". Captures export as JSON or go to a 4CAT instance. It supports TikTok (posts and comments) and Instagram (posts only), and the Instagram capture works on profile pages, the main feed or the "reels" page. Personalised feeds require login — [Bellingcat Toolkit: Zeeschuimer](https://bellingcat.gitbook.io/toolkit/more/all-tools/zeeschuimer); [Aarhus CDMM guide](https://cc.au.dk/cdmm/tools-and-tutorials/data-collection/zeeschuimer); [Fahner workshop](https://craigfahner.github.io/zeeschuimer-workshop); [Zeeschuimer GitHub](https://github.com/digitalmethodsinitiative/zeeschuimer)
- Platform changes can break capture — [Bellingcat Toolkit: 4CAT](https://bellingcat.gitbook.io/toolkit/more/all-tools/4cat)
- Other institutions run instances, e.g. KingsCAT at King's College London — [KCL](https://www.kcl.ac.uk/research/kingscat)

**DMI / YouTube Data Tools** (Rieder)
- These use the YouTube Data API, and Rieder et al. (2025) note that earlier studies using the API or YouTube Data Tools often gave data quality little scrutiny. Search results are incomplete and freshness-biased — [arXiv 2506.11727](https://arxiv.org/abs/2506.11727); companion paper on Search API use in research — [arXiv 2506.04422](https://arxiv.org/html/2506.04422v2); tools list — [CAT4SMR tools](https://cat4smr.humanities.uva.nl/index.php/tools/)

**Junkipedia**
- Free, built "by, and for, investigative journalists and researchers". It automatically transcribes English-language audio on TikTok, YouTube, Telegram and podcasts — [GIJN](https://gijn.org/stories/new-tools-monitoring-social-media-junkipedia/). It collects public TikTok posts via APIs, user tips and synthetic accounts (per Mozilla) — [Mozilla Foundation](https://www.mozillafoundation.org/de/campaigns/strategies-for-studying-tiktok-during-the-german-election/)

**Memespector-GUI** (Public Data Lab / DMI ecosystem)
- A desktop client that sends images to Google Vision, Microsoft Azure, Clarifai (and open-source ImageNet models) and returns labels, objects, OCR text, face-emotion estimates, web entities and matching image URLs. The tool is free; the APIs may charge. Its last major release was about four years before a 2025 user survey (closed 31 Mar 2025), so maintenance is uncertain — [Public Data Lab](https://publicdatalab.org/2021/10/27/memespector-gui/); [Public Data Lab author page](https://publicdatalab.org/author/jasonchao/)

**Archiving and integrity**
- Bellingcat Auto Archiver (v1.2.0, Jan 2026) archives URLs to local, Google Drive or S3 storage, creates WACZ web archives via browsertrix-crawler with a verifiable manifest, has a web UI/API, and has preserved over 150,000 items — [Bellingcat Toolkit: Auto Archiver](https://bellingcat.gitbook.io/more/all-tools/auto-archiver); [Ed Summers](https://inkdroid.org/2022/09/26/auto-archiver/); [Nieman Lab](https://www.niemanlab.org/2025/08/it-just-got-easier-to-make-an-archival-copy-of-that-website-youre-digging-into/)
- WACZ format specification — [Webrecorder WACZ spec](https://specs.webrecorder.net/wacz/)
- Meta open-sourced PDQ (photo) and TMK+PDQF (video) perceptual-hashing algorithms (2019) for matching near-duplicate media — [Meta newsroom](https://about.fb.com/news/2019/08/open-source-photo-video-matching/)
- The Berkeley Protocol sets out preservation, metadata and chain-of-custody practices for open-source digital evidence — [OHCHR](https://www.ohchr.org/en/publications/policy-and-methodological-publications/berkeley-protocol-digital-open-source)

**Metadata fields (platform-provided reference)**
- TikTok Research API fields (id, create_time, username, region_code, description, hashtags, mentions, music_id, counts, video_label, voice_to_text, duration) are a useful minimum schema — [TikTok codebook](https://developers.tiktok.com/doc/research-api-codebook)

### Inferences
- Recommended per-item record, to be kept for every collected item whatever the tool: canonical URL and platform ID; account handle and ID, with account type and verification status at collection; upload timestamp (UTC) and collection timestamp; collector/tool and version; view, like, comment and share counts with the time observed; caption/description, hashtags, mentions and audio/music ID; platform labels (e.g. state-affiliated, AI-generated, sensitive-content interstitial); duration; language; geolocation or region if provided; a cryptographic hash (SHA-256) of the media file for integrity; a perceptual hash (PDQ/TMK) for de-duplication of re-uploads, which are common in war content; the transcript and OCR outputs with model versions; and availability status at each re-check.
- Legal risk ranking (lowest to highest): official APIs/MCL → embedding/oEmbed → logged-off browser capture of public pages → Zeeschuimer with a research account → command-line downloaders without login → logged-in downloaders and YouTube cipher circumvention (with EU TPM exposure).
- Reliability: expect breakage after platform updates. Pin tool versions, log failures, and avoid single-tool dependence.

### Gaps
- I found no 2025–2026 independent reliability benchmark comparing yt-dlp, gallery-dl and Instaloader on Reels/TikTok.
- I did not verify the current list of 4CAT processors for downloading TikTok or Instagram media.
- I did not identify a DMI-specific TikTok tool beyond Zeeschuimer.
- Junkipedia's current (2026) eligibility and access terms were not found.

---

## C1. Codebooks and studies for conflict/war short video: framing, stance, emotion, graphic violence, dehumanisation, misinformation, source type

### Takeaway
There is no single validated codebook for Israel–Gaza short video, but there is a growing set of published studies to adapt. They use Entman-style framing functions, war versus peace journalism (Galtung-derived), Moral Foundations, victim/defensive modes, scene-type taxonomies, and humour functions. Stance coding is commonly binary (pro-Israel/pro-Palestine) plus neutral/mixed. Dehumanisation and antisemitism/Islamophobia schemes come mostly from text-based work.

### Cited Findings
- **Framing functions:** Entman (1993) defines framing as selecting aspects of reality to "promote a particular problem definition, causal interpretation, moral evaluation, and/or treatment recommendation" — [Entman 1993, Journal of Communication](https://doi.org/10.1111/j.1460-2466.1993.tb01304.x)
- **TikTok news, war vs peace frames:** Fahmy, Abbas & ElShabassy (2025, *Digital Journalism*), "TikToking the Israel-Gaza War", coded 405 TikTok videos from six news outlets: 79.5% war-framed, 11.1% peace, 9.4% neutral. They argue that pro-Gaza or pro-Israel lean reflects outlets' selective focus — [ResearchGate](https://www.researchgate.net/publication/396650766_Digital_Journalism_TikToking_the_Israel-Gaza_War_A_Content_Analysis_of_Peace_and_War_Narratives_in_Audiovisual_News); [Academia.edu](https://www.academia.edu/144529311/TikToking_the_Israel_Gaza_War_A_Content_Analysis_of_Peace_and_War_Narratives_in_Audiovisual_News)
- **Visual moral framing:** Abbas, ElShabassy & Fahmy (2026, SAGE journal ISSN 1750-6352, i.e. *Media, War & Conflict*) coded 736 TikTok video-journalism items from six outlets (Oct 2023–Apr 2025) using Moral Foundations Theory. Care/Harm and Sanctity/Degradation were most frequent, while Fairness/Cheating and Loyalty/Betrayal drove more engagement — [SAGE](https://journals.sagepub.com/doi/10.1177/17506352261446076)
- **Earlier TikTok "image war":** a study of the May 2021 round (n=318, *Digital Journalism*) found TikTok posts did not follow traditional problem/cause/solution wartime framing — [Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/21670811.2023.2291650)
- **Instagram news imagery:** Elmasry (2025, *JMCQ* 102(3):695–721) analysed BBC, CNN, Fox, Sky and MSNBC Instagram posts using framing theory and a victim/defensive mode of reporting model. He found reliance on Israeli sources, Israeli violence framed as self-defence and Palestinian violence as aggression — [SAGE](https://journals.sagepub.com/doi/abs/10.1177/10776990241287155)
- **Humanitarian framing:** UNRWA's Instagram visuals in the first 100 days showed destruction, humanitarian-aid and human-interest frames — [ResearchGate](https://www.researchgate.net/publication/393346387_Framing_UNRWA's_Visual_Content_on_Instagram_for_Humanitarian_and_Relief_Aid_during_the_First_100_Days_of_War_in_Gaza)
- **Witnessing/atrocity imagery:** a study of Instagram images of the Al-Ahli hospital strike contrasted Al Jazeera English, NYT and IDF visual regimes ("affective witnessing", "spectacle of suffering") — [De Gruyter (DOI)](https://doi.org/10.1515/lass-2026-0051)
- **YouTube Shorts, state-funded news:** Miehling & Kübler (arXiv, Apr 2026) studied 2,371 Shorts from Al Jazeera, BBC, DW and TRT World. The visual scene taxonomy has seven classes: combat/military; destruction/humanitarian crisis; political/diplomatic; news/interview; protest; symbolic/religious; other. They used aspect-based sentiment toward Israel, Palestine, Hamas, Jews, Muslims, Zionism and politicians. Al Jazeera and TRT World showed the strongest polarity — [arXiv 2604.00994](https://arxiv.org/html/2604.00994)
- **Humour as a genre:** a study coded 257 Israeli TikTok humour videos posted after 7 October and interviewed 7 influencers on the social and psychological functions of humour — [PMC12414762](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12414762/)
- **State-actor narratives:** a comparison of EU and Chinese state discourse on TikTok combined TF-IDF, BERTopic and shot-by-shot video analysis — [ResearchGate](https://www.researchgate.net/publication/403673379_Narratives_of_Conflict_on_TikTok_Comparing_the_EU_and_China's_Discursive_Strategies_in_the_Israel-Hamas_Conflict)
- **Hashtag co-occurrence discourse** on TikTok (2023 crisis) — [ResearchGate](https://www.researchgate.net/publication/387975302_Unveiling_Voices_A_Co-Hashtag_Analysis_of_TikTok_Discourse_on_the_2023_Israel-Palestine_Crisis)
- **Stance prevalence (contested):** a Cybersecurity for Democracy/NYU/Northeastern report (not peer-reviewed), as reported by JNS, found about 1 pro-Israel post per 17 pro-Palestine posts and higher average views for "pro-Hamas" videos. The labels and the outlet framing are contested — [JNS](https://www.jns.org/tiktok-amplified-pro-hamas-content-during-israel-gaza-war/)
- **Antisemitism/anti-Israel annotation:** the Indiana University ISCA report (Dec 2024) on X and TikTok after 7 Oct includes an annotation-scheme section — [ISCA report PDF](https://isca.indiana.edu/publication-research/social-media-project/documents-soc-media-proj/research-report-2024-the-image-of-israel-on-social-media-after-10-7-1.pdf); [ISCA project page](https://isca.indiana.edu/publication-research/social-media-project/media.html)
- **Dehumanisation:** ADL documented dehumanising and stereotyping language against Jews and Muslims (7–18 Oct 2023) — [ADL](https://www.adl.org/resources/blog/platforms-struggling-curb-online-hate-amidst-war-israel-and-gaza). The William & Mary STAIR lab built a theory-guided dehumanisation lexicon (applied to UK/Irish news coverage of Palestinians) — [STAIR](https://stair.wm.edu/publication/dehumanization/); [STAIR lexica](https://stair.wm.edu/categories/lexica). Sada Social (2024 data) monitored incitement, including dehumanising language, with an advocacy methodology — [Global Voices](https://globalvoices.org/2025/05/12/digital-erasure-how-social-media-platforms-are-silencing-palestinians-in-2024/)
- **AI-generated imagery as a category:** a 2026 study analysed AI-generated images of the war and argued that civilian-only depictions frame the conflict as a humanitarian crisis — [Frontiers in Communication](https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2026.1731105/full)

### Inferences
- A workable multi-level codebook could be assembled from these sources, with these dimensions:
  - **Source type:** news organisation (state-funded vs. independent, per Miehling & Kübler); state/military account; politician; NGO/UN; activist; influencer/creator; ordinary user; AI-generated/synthetic.
  - **Entman functions:** problem, cause, moral evaluation, remedy, each coded for presence and for which actor it is attributed to.
  - **War vs peace orientation:** Fahmy et al.
  - **Stance:** pro-Israeli / pro-Palestinian / both / neither, coded separately for the creator's stance and for the actors portrayed.
  - **Moral foundations:** Abbas et al.
  - **Emotion appeals:** e.g. anger, fear, sadness, hope, humour.
  - **Graphic content:** casualties, injured, children, bodies, destruction, plus a platform interstitial flag.
  - **Dehumanisation:** animal/vermin metaphors, collective blame, adapted from the STAIR/ADL categories.
  - **Visual scene type:** Miehling & Kübler.
  - **Verification:** recycled/old footage, out-of-context, AI-generated, and fact-check match (with URL).
- A priori symmetry matters for neutrality. Define dehumanisation, atrocity and incitement categories so they apply equally to content about Israelis, Palestinians, Jews and Muslims, and pilot them on balanced samples.

### Gaps
- None of the retrieved studies' full codebooks or reliability coefficients were obtained (except Miehling & Kübler, who report none).
- No peer-reviewed codebook for misinformation/fact-check status in Israel–Gaza short video was found. Fact-check databases such as Google Fact Check Tools were not researched.
- No validated Hebrew/Arabic dehumanisation lexicon for social video was found.

---

## C2. Intercoder reliability standards (Krippendorff's alpha thresholds, reliability sampling)

### Takeaway
Convention is α ≥ .800 for reliable variables, .667–.800 for tentative conclusions only, and below .667 discarded. Thresholds should be higher when errors are costly. Reliability samples should be sized by formula (Bloch & Kraemer, as used by Krippendorff) rather than by rule of thumb, and α should be reported with bootstrapped confidence intervals.

### Cited Findings
- α = 1 − (observed disagreement / expected disagreement). Perfect agreement gives α = 1, and to rely on data α must be "far from" chance-level conditions, "ideally" 1 — [Krippendorff, "Computing Krippendorff's Alpha-Reliability" (2011/2013)](https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf)
- Common practice is to rely on α ≥ .800, use .667–.800 for tentative conclusions, and discard data below .667. The minimum should rise with the cost of mistaken conclusions — [Wikipedia: Krippendorff's alpha](https://en.wikipedia.com/wiki/Krippendorff%27s_alpha); [ATLAS.ti manual (citing Krippendorff 2019)](https://doc.atlasti.com/ManualWin/ICA/ICASampleSizeAndDecisionRules.html)
- Sample-size tables based on Bloch & Kraemer's formula give, for example, a minimum of 81 codings for α = .667 at the stated significance level (two coders, up to 10 sub-codes) — [ATLAS.ti manual](https://doc.atlasti.com/ManualWin/ICA/ICASampleSizeAndDecisionRules.html)
- Bootstrapped confidence intervals are recommended because point estimates near cutoffs are unstable — [MetricGate (vendor)](https://metricgate.com/calculator/krippendorffs-alpha); [Wikipedia](https://en.wikipedia.com/wiki/Krippendorff%27s_alpha)
- R implementations are available (e.g. the `icr` package with bootstrap) — [CRAN icr](https://cran.r-project.org/web/packages/icr/refman/icr.html)

### Inferences
- For video coding, reliability should be computed per variable and per unit level (video, scene, frame). Rare categories such as atrocity imagery or dehumanisation need stratified oversampling in the reliability subsample, or α will be unstable.
- When LLMs or VLMs are used as coders, the same α machinery can treat the model as an additional coder (human–model α) alongside accuracy/F1 against an adjudicated gold standard (see C3).

### Gaps
- Krippendorff's book text (Content Analysis, 4th ed., 2019) with the exact threshold wording was not retrieved; the thresholds are confirmed only via secondary sources.
- No video-specific reliability guidance (e.g. for timestamped segment coding) was found.

---

## C3. Automated multimodal pipelines: Whisper, OCR, keyframes, LLM/VLM coding; validation evidence; Hebrew/Arabic; deepfake detection

### Takeaway
Pipelines of ASR, OCR, keyframe sampling and LLM/VLM coding are now used on Israel–Gaza Shorts, but the evidence calls for task-specific validation against human gold standards. Gilardi et al. (2023) found zero-shot ChatGPT beat crowd workers. Baumann et al. (2025), however, show that LLM-annotation choices flip roughly one in three hypothesis tests even with state-of-the-art models. Hebrew ASR improves substantially with ivrit.ai fine-tunes; dialectal Arabic remains harder. AI-generated or deepfake detectors are unreliable and produce false positives on authentic war imagery, so provenance and verification workflows matter more than classifier scores.

### Cited Findings
**LLM annotation validity**
- Gilardi, Alizadeh & Kubli (2023, *PNAS*): on 6,183 items across four datasets, zero-shot ChatGPT accuracy averaged about 25 points above MTurk crowd workers. Intercoder agreement was about 91% at temperature 1 and 97% at 0.2, versus 79% for trained annotators and 56% for MTurk. Cost was under $0.003 per annotation — [PNAS via PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10372638); [arXiv 2303.15056](https://arxiv.org/abs/2303.15056)
- Baumann, Röttger, Urman et al. (2025), "Large Language Model Hacking": they replicated 37 annotation tasks from 21 studies with 18 models (13 million labels). Incorrect conclusions occurred in "approximately one in three hypotheses for state-of-the-art models" and half for small models. Common regression correction techniques were "largely ineffective". Human annotations are key to reducing false positives, and "anything can be presented as statistically significant" with a few models and prompt paraphrases — [arXiv 2509.08825](https://arxiv.org/abs/2509.08825); [code](https://github.com/joebaumann/llmhacking)
- Pangakis, Wolken & Fasching (2023), "Automated Annotation with Generative AI Requires Validation", argue that LLM performance varies by task and must be validated against human labels for each task — [arXiv 2306.00176](https://arxiv.org/abs/2306.00176)

**Multimodal pipelines in this domain**
- Miehling & Kübler (2026): Whisper large-v3 transcription (language detection on the first 30 s); a dependency parser plus a 56-term aspect lexicon; DeBERTa-v3 aspect sentiment (macro-F1 81.9 on a gold standard, versus 72.5 for QLoRA-tuned Qwen2.5-7B); 1 frame/second sampling with Qwen3-VL-4B scene classification (86.9% accuracy on 799 manually checked frames, about 97% for news/interview scenes). Commercial VLMs were deliberately avoided for reproducibility. Non-English Shorts were excluded, transcription was checked only qualitatively (errors in chanting and noise), and no α/κ was reported — [arXiv 2604.00994](https://arxiv.org/html/2604.00994)
- BigTokDetect (2025) evaluated GPT-4.1, Claude Sonnet 4, Gemini 2.5 Flash (native video input), Qwen2.5-VL and InternVL3 for classifying TikTok videos against a clinically informed taxonomy. This shows native-video VLM coding is feasible, though in a different domain — [arXiv 2508.06515](https://arxiv.org/pdf/2508.06515)
- Video LLM limitations: "Time Blindness" shows video-language models fail at temporal patterns humans perceive easily — [arXiv 2505.24867](https://arxiv.org/pdf/2505.24867)
- VisTopics is an unsupervised visual topic-modelling approach for video and image data — [arXiv 2505.14868](https://arxiv.org/pdf/2505.14868)
- Memespector-GUI provides commercial computer-vision labelling, including OCR (text detection) via Google Vision — [Public Data Lab](https://publicdatalab.org/2021/10/27/memespector-gui/)
- TikTok's Research API provides a `voice_to_text` field (platform-generated transcript) — [TikTok codebook](https://developers.tiktok.com/doc/research-api-codebook)
- Junkipedia transcribes English audio only — [GIJN](https://gijn.org/stories/new-tools-monitoring-social-media-junkipedia/)
- Scene/shot detection tooling, e.g. PySceneDetect — [PySceneDetect](https://www.scenedetect.com/)

**Hebrew and Arabic**
- Whisper is a multilingual model trained on large-scale weak supervision — [Radford et al. arXiv 2212.04356](https://arxiv.org/abs/2212.04356); [openai/whisper GitHub](https://github.com/openai/whisper)
- ivrit.ai (Interspeech 2025) reports a Hebrew Whisper model with "up to 29% reduction in error rates compared to existing Whisper solutions" — [Marmor et al., Interspeech 2025](https://www.isca-archive.org/interspeech_2025/marmor25_interspeech.pdf)
- Self-reported Hebrew WERs on a community model card: ivrit.ai turbo about 5.5% (eval-d1), 6.1% (WhatsApp) and 8.1% (KAN), versus about 30–39% for stock whisper-small — [Ozen-v1 model card](https://huggingface.co/itayinbar/Ozen-v1). A vendor benchmark lists Whisper large-v3 at 32.9% WER for Hebrew (treat with caution) — [ElevenLabs](https://elevenlabs.io/hi/speech-to-text/hebrew)
- Arabic: multi-dialect Whisper fine-tuning addresses data scarcity — [arXiv 2506.02627](https://arxiv.org/pdf/2506.02627). A large weakly supervised Arabic ASR paper reports large WER variation for stock Whisper large-v3 across datasets (table headers garbled in retrieval, so figures not reported here) — [arXiv 2504.12254](https://arxiv.org/pdf/2504.12254)
- Tesseract OCR ships trained data for Hebrew (`heb`) and Arabic (`ara`) — [Tesseract tessdoc: data files](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html)

**AI-generated / deepfake detection**
- In Israel–Gaza coverage, detectors mislabelled authentic images. One tool labelled a genuine Netanyahu video "96.9 per cent AI-generated" while others disagreed. Hany Farid cautioned that a "not AI" result does not establish authenticity, and Henry Ajder called detectors a "false solution". Researchers found relatively few convincing AI fakes; much misinformation was recycled old footage, and the "liar's dividend" led people to dismiss real imagery — [Khaleej Times/AFP](https://www.khaleejtimes.com/business/tech/whats-real-anymore-ai-warps-truth-of-middle-east-war); [GIGAZINE](https://gigazine.net/gsc_news/en/20231016-ai-images-detectors-discredit-real-war); [Business Standard](https://www.business-standard.com/world-news/artificial-intelligence-muddies-battleground-in-unexpected-way-report-123102900948_1.html)
- A 2026 analysis of the Iran–Israel/US war found detection tools "can't be fully trusted". Google's SynthID can only identify content made with Google's own tools — [The Quint WebQoof](https://www.thequint.com/news/webqoof/west-asia-conflict-fact-checking-in-times-of-ai-warfare); AFP report on "AI slop" flooding Middle East war coverage (Apr 2026) — [Malay Mail](https://www.malaymail.com/news/world/2026/04/03/ai-slop-floods-middle-east-war-blurring-truth-and-fiction/214786)
- A conference paper compared human judgment with five free detectors (e.g. Sightengine, Undetectable.ai, Decopy.ai, WasItAI) on AI-generated Israel–Hamas war images — [ICAIR paper](https://papers.academic-conferences.org/index.php/icair/article/download/4070/3963/15766)
- The C2PA content-credentials standard for provenance metadata — [C2PA](https://c2pa.org/)
- TikTok's Research API `video_label` field covers labels such as election labels; the codebook has no dedicated AI-generated field — [TikTok codebook](https://developers.tiktok.com/doc/research-api-codebook)

### Inferences
- **Validation protocol:**
  1. Build a human-coded, adjudicated gold standard, stratified by language (Hebrew/Arabic/English), source type and rare categories.
  2. Report per-variable F1/accuracy and human–model α.
  3. Pre-register the model, prompt and temperature, and test sensitivity to prompt paraphrases and alternative models, following the LLM-hacking recommendations.
  4. Keep humans on high-stakes or contested variables: stance, dehumanisation, atrocity, misinformation.
  5. Prefer open-weight models (as Miehling & Kübler did) for reproducibility, or archive the exact API model versions.
- **Language:** use Hebrew-tuned ASR (ivrit.ai) and dialect-aware Arabic ASR rather than stock Whisper. Validate WER on a sample of the actual corpus, since war audio (sirens, chanting, music) degrades ASR. On-screen text is often the main carrier of stance in Reels/TikToks, so OCR (Tesseract heb/ara or VLM-based) needs separate validation, including right-to-left and mixed-script overlays.
- **AI-generated/synthetic coding:** treat detector output as one weak signal. Combine it with platform AI labels, C2PA credentials where present, reverse image/video search for recycled footage, and fact-checker matches. Code "verification status" as known-authentic / known-synthetic / recycled-out-of-context / unverified rather than a binary.

### Gaps
- No peer-reviewed study validating VLM coding of Israel–Gaza short video against Krippendorff's α was found.
- No Arabic-dialect (Levantine/Palestinian) ASR benchmark on social video was found.
- No validated Hebrew/Arabic OCR benchmark for TikTok/Reels overlays was found.
- The results of the ICAIR detector comparison were not retrieved.
- No current data on YouTube/Meta/TikTok AI-label coverage rates for war content was found.

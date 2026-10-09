# Subagent: Evidence v3 wave2 batch 13 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:10:28

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b13.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b13.json

Today is 2026-10-08.

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\prompts\\evidence_agent.md"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	# Evidence agent – v3
2	
3	*v2 (after checkpoint CP2): early exits, no registry lookups (code does them), investment = equity only, all funds
4	listed (code sums total capital), restricted tools, agents read this file + a batch file themselves.*
5	*v3 (after wave 1): real, active VCs were rejected because agents stopped after 1–2 deals → **portfolio page first,
6	then dated news for the most recent deals**; a full example record (one agent misread the claim shorthand).
7	Changes are marked **[v2]** / **[v3]**.*
8	
9	---
10	
11	You are an evidence collector for a database of **investors into companies**. For each candidate in your batch file,
12	find public evidence of **what the entity is** and **whether it actually invests**, and fill a fixed JSON record.
13	
14	You do **not** decide whether the candidate goes into the database. A program decides that from your evidence, and
15	every quote you give will be **machine-checked**: the program downloads `source_url` and searches the page for your
16	`quote`. A quote that is not on the page, or a value that is not in the quote, is thrown away. So:
17	
18	- **Copy quotes verbatim** (max 300 characters), in the original language (Czech/Slovak/English) – never translate,
19	  shorten in the middle, or paraphrase.
20	- **Never estimate, convert or compute numbers.** If a ticket size or fund size is not stated, return `null`.
21	- **"Not found" is a good answer.** A missing field costs nothing; an invented one makes the whole record fail.
22	
23	**Tools [v2]:** use only WebSearch, WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed),
24	Read (for your batch file) and Write (for your output file). Do **not** use Bash or the in-app browser
25	(`mcp__Claude_Browser__*`).
26	
27	**How to get verbatim quotes:** WebFetch passes the page through a model that may summarise it. Always give
28	WebFetch a prompt like: *"Return word-for-word, without summarising or translating, every sentence that mentions
29	<name> / investments / portfolio / fund size / ticket, and the page's publication date."* Copy your quote only from
30	such word-for-word output, never from a summary or from a search-result snippet.
31	
32	## Work in three steps per candidate – with early exits [v2]
33	
34	Budget: **at most 17 tool calls per candidate [v3]**, but stop early when a step says so.
35	
36	1. **What is it and where is it? (≤ 3 calls)** – the candidate's own website (about, team, contact/kontakt,
37	   footer). Fill `investor_type`, `hq_country`, and `identity` if the site shows the legal name / IČO.
38	   **Early exit:** if the HQ is clearly outside the Czech Republic and Slovakia, stop here (fill what you have).
39	2. **Does it invest? (≤ 10 calls) [v3]** – in this order:
40	   a. **Open the candidate's portfolio page** (often "Portfolio", "Companies", "Investments", "Portfólio") and record
41	      **up to 6 portfolio companies** as investments – one claim each, the quote is the line naming the company,
42	 
… [skrátené, 9687 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b13.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b13.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C059",
4	    "name": "FARKASOVA INTERNATIONAL, s.r.o",
5	    "other_names": [],
6	    "known_website": "www.farkasovainternational.com",
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): FARKASOVA INTERNATIONAL, s.r.o., IČO 07957360"
8	  },
9	  {
10	    "candidate_id": "C199",
11	    "name": "Uroboros Ventures s.r.o.",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": "possible registry match (unconfirmed, may be a different company): , IČO 24808016"
15	  },
16	  {
17	    "candidate_id": "C192",
18	    "name": "European Innovation Council",
19	    "other_names": [],
20	    "known_website": null,
21	    "registry_hint": null
22	  },
23	  {
24	    "candidate_id": "C155",
25	    "name": "Google Ventures",
26	    "other_names": [],
27	    "known_website": null,
28	    "registry_hint": null
29	  },
30	  {
31	    "candidate_id": "C195",
32	    "name": "ZAKA Ventures",
33	    "other_names": [],
34	    "known_website": null,
35	    "registry_hint": null
36	  }
37	]
````

</details>

<details><summary>🔧 ToolSearch</summary>

````text
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 5
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text

````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "FARKASOVA INTERNATIONAL s.r.o. farkasovainternational.com",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Uroboros Ventures s.r.o. investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ZAKA Ventures investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Uroboros Ventures s.r.o. investice"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/ouroboros-capital"},{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/investors/ub_ventures/portfolio/exits"},{"title":"UB Ventures Overview","url":"https://pitchbook.com/profiles/investor/264692-98"},{"title":"Western NIS Enterprise Fund (WNISEF)","url":"https://presseportal.de/r/Kyiv%252FUkraine?langid=2"},{"title":"Western NIS Enterprise Fund Launches New Fund to Invest in Promising Startups from Ukraine and Moldova","url":"https://wnisef.org/medias/western-nis-enterprise-fund-launches-new-fund-invest-promising-startups-ukraine-moldova/"},{"title":"privateequitylist.com","url":"https://privateequitylist.com/investor/uventures"},{"title":"vestbee.com","url":"https://vestbee.com/vc-list/u.ventures"},{"title":"197328 uventures","url":"https://my.motherbase.ai/startup/197328-uventures"},{"title":"borovicka capital","url":"https://superscout.co/investor/borovicka-capital"},{"title":"privateequitylist.com","url":"https://privateequitylist.com/investors/uventures"}]

I couldn't find any results for "Uroboros Ventures s.r.o." The search returned no pages about that company, its investments, or its registration.

Some results had similar names, but none appear to be the same company:

- **Ouroboros Capital** (spelled with "O"): A crypto hedge fund that offers various investment solutions. The company was founded in 2022 and is based in Delaware. A Delaware firm is not a Czech s.r.o., so it is probably unrelated.
- **Borovicka Capital s.r.o.**: A venture capital firm established in 2023, headquartered in Prague, Czech Republic. It is a Czech s.r.o. with a different name, so it is also probably unrelated.

To find the company you're after, try searching the Czech business registers directly. The ARES database (ares.gov.cz) and the public commercial register (or.justice.cz) list legal names, company IDs (IČO), and registered addresses for s.r.o. entities. If you have the IČO or the registered address, I can search for those as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "FARKASOVA INTERNATIONAL s.r.o. farkasovainternational.com"

Links: [{"title":"www.jobs.cz","url":"https://www.jobs.cz/rpd/2001388796/?rps=233"},{"title":"FARKASOVA INTERNATIONAL, s.r.o. , Praha IČO 07957360 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/07957360"},{"title":"www.jobs.cz","url":"https://www.jobs.cz/rpd/2001457219/?rps=233"},{"title":"Slávka Farkašová - rejstříky, události","url":"https://rejstrik-firem.kurzy.cz/osoby/1621351/"},{"title":"obchodny register","url":"https://finstat.sk/52533743/obchodny_register"},{"title":"Etela Farkašová foto 2","url":"https://www.litcentrum.sk/en/author/etela-farkasova/curriculum-vitae"},{"title":"katalog.snk.sk","url":"https://katalog.snk.sk/vufind/Record/1308019"},{"title":"farkste goods s r o 14253402","url":"https://www.podnikatel.cz/rejstrik/farkste-goods-s-r-o-14253402/"},{"title":"Rudolf Farkaš","url":"https://www.foaf.sk/40550737/casova-os-zmien"}]

Links: [{"title":"FARKASOVA INTERNATIONAL, s.r.o. , Praha IČO 07957360 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/07957360"},{"title":"www.genealogyforum.rootsweb.com","url":"https://www.genealogyforum.rootsweb.com/forum/surnames/topics/farkas/2/"},{"title":"omg.eve-kill.com","url":"https://omg.eve-kill.com/character/1600035889"},{"title":"Farkas, István Budapest, 1887 - 1944, Auschwitz","url":"https://www.kieselbach.hu/artwork/walk_9057"},{"title":"www.genealogyforum.rootsweb.com","url":"https://www.genealogyforum.rootsweb.com/forum/surnames/topics/farkas/11/"},{"title":"global.museum-digital.org","url":"https://global.museum-digital.org/people/86140"},{"title":"mobile.eve-kill.com","url":"https://mobile.eve-kill.com/character/1600035889"},{"title":"bu.hu.museum-digital.org","url":"https://bu.hu.museum-digital.org/people/86140"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=62800"},{"title":"global.museum-digital.org","url":"https://global.museum-digital.org/people/89365"}]

I couldn't reach farkasovainternational.com itself, so this is based on third-party registry and job-board listings.

**Company registration**
- The Czech business register aggregator lists the firm under company ID (IČO) 07957360, with its seat in Prague 1 on Na Florenci. The registered share capital is 200,000 CZK.
- That same aggregator lists the website as farkasovainternational.com, but the contact email uses a different domain, farkasovaandpartners.com. The listing names a phone number, the email address, and the website.
- Ownership changed in early 2025. Entries from February 2025 record Mgr. Darina Dias Martins da Silva as the sole partner with a 100% stake and as the managing director, and they show a former partner, Darina Farkasová, being removed. Entries from 12.2.2025 record a new partner, Mgr. Darina Dias Martins da Silva, with a 200,000 CZK contribution and a 100% stake. The name appears in several slightly different spellings in these entr
… [skrátené, 981 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ZAKA Ventures investice"

Links: [{"title":"czech zaka launches its first fund of 15m","url":"https://en.ain.ua/2024/07/19/czech-zaka-launches-its-first-fund-of-15m"},{"title":"Zaka VC se mění z rodinného na klasický startupový fond. Má stovky milionů korun","url":"https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/"},{"title":"ZAKA Ventures","url":"https://signal.nfx.com/firms/zaka-ventures"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=51832"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/note/zaka-vc-launches-15m-fund"},{"title":"therecursive.com","url":"https://therecursive.com/?p=38085"},{"title":"Ján Búza zo ZAKA VC: Slovenský pôvod nie je v Silicon Valley prekážkou","url":"https://www.startitup.sk/?p=1130105"},{"title":"Czech VC single family office opens up to third-party investors","url":"https://familyofficehub.io/blog/czech-vc-single-family-office-opens-up-to-third-party-investors/"},{"title":"ZAKA VC Research","url":"https://f4.fund/firms/zaka-vc"}]

**ZAKA VC** (also written ZAKA Ventures or ZAKA Startups) is a Prague-based pre-seed and seed investor. The search results are mostly from 2024 and early 2025, and I didn't find anything newer.

**Origins and fund**
- The firm was founded in 2020 by serial entrepreneur [REDACTED] and Peter Zalešák as a family office.
- In July 2024 it launched its first institutional fund. Fund I targets €15 million and began with a €10.5 million first close, with a minimum LP ticket of €130,000 for qualified investors only. One source gives the first close as June 2024 rather than July (siliconcanals).
- A Czech outlet reports that the firm plans to double its investments in early-stage development and expand its capital base in the coming years.

**Investment approach**
- It invests mainly at the pre-seed and seed stages, usually as a co-investor or co-lead alongside other seed funds, and sometimes joins follow-on Series A rounds.
- Geographic focus is primarily Central and Eastern Europe, plus DACH, the Baltics, the UK and the US (ain.ua).
- Sector sources differ. One says the main focus is B2B software, AI applications in B2B, biotech, and health tech. Another says it invests primarily in Health & Biotech and Industrial Tech, with increasing allocation to B2B software and the cross-sectional application of AI.

**Notable portfolio companies**
- ExcepGen, Sensible Biotechnologies, Miros.ai, Supliful, Lime Therapeutics, and Webel are among its named investments.
- More recently, ZAKA joined a €1.7 million pre-seed round for ExoMatter, a German company using AI to speed up materials R&D (therecursive.com).

**Portfolio size (sources disagree)**
- 2024 coverage cites more than 55 invested companies and over €11M invested.
- Family Office Hub reports more than 50 start-ups from 23 countries, with 2 exits.
- F4 Fund says the fund has deployed investments across 80+ companies since founding.
- NFX l
… [skrátené, 617 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.farkasovainternational.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence on this page that describes what the company does, who it is, its team, office address, company ID (IČO), and any investments, portfolio, fund or ticket. Also return the page's publication or last-updated date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://zaka.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence on this page that describes what the company does, its investment focus, team, office address, company ID (IČO), portfolio, fund size, or ticket size. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Uroboros Ventures\"",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Company description (verbatim, each quote under 125 characters):**

- "Farkasova International is a leading executive leadership search and talent advisory firm."
- "Headquartered in Prague, Czech Republic we focus on the global European Market"
- "People are in the center of everything we do."
- "Organizations and Candidates are positioned at the same level"
- "We operate in a non-franchise or partner model"
- "We believe that to win the marketplace you need first to win the workplace."

**Office address:**
Florentinum (Block A), Na Florenci 2116/15, 110 00 Prague 1, Czech Republic

**Contact (for reference):** +420 210 111 111. The email address is obfuscated on the page.

**Not found on the page:**
- Company ID (IČO)
- Team members or named staff (only an "Our Team" link appears)
- Investments, portfolio, fund, or ticket information

**Date:** The page shows only the copyright line "Farkasova International® | 2024." It has no publication or last-updated date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Company description and investment focus**
- "We are a seed & pre-seed VC fund, investing mainly in the US and Europe."
- "Especially looking for startups in the Health & Biotech and Industrial Tech verticals."
- "We seek entrepreneurs with global ambition wherever they are and support them by creating a bridge" (remainder truncated for length: it describes bridging North America and Europe).
- "One of the best Healthcare & Life Sciences portfolios in continental Europe."

**Team:** No team member names or roles appear on this page.

**Office locations:** "Silicon Valley / London / Prague / Bratislava." No street address is given.

**Company ID (IČO):** Not shown on this page.

**Fund size:** The page lists a current fund size of 17M. Fund 1 is shown at 17M, with 8M invested across 46 companies. A separate Family office entry shows 5M invested.

**Ticket size:** "The minimum ticket is 130K." The page also states: "This investing is for qualified investors only."

**Portfolio**
- "There's already 97 companies across 5 continents that we believe in."
- Featured companies, described on the page:
  - WonderTx: "Extrapolative AI to unlock first-in-class drugs"
  - Aerogen Systems: "Modernizing chip manufacturing infrastructure"
  - FinalDose: "Programmable DNA drug destroying all cancers, unlocking 80% of targets"
  - PerfectBit: "Correct by construction training data for frontier AI labs"
  - Human Archive: "Human Archive builds human data archiving platform with comprehensive dataset for training embodied AI and robotics systems."
  - AxionOrbital Space: "Building foundation models for 24/7 Earth Observation starting with SOTA SAR-to-Optical generation"
  - CellType: "Cell Type develops models that simulate human drug response and analyze single-cell data for target selection and clinical design."
- Other listed companies include Sygaldry Technologies, HexemBio, Ateios Systems, Mews, Zephyr Fusion, DeepSeq.AI, Sutro, bit.bio, Superlinked, and many others. The page does not describe most of them.

**Publication dates (news)**
- 10/08/2026: "mRNA is still made the 1984 way. It was not built for the drugs coming next."
- 10/06/2026: "Sensible Biotechnologies raises $47M: why we backed them early, and why it's personal for us"
- 09/23/2026: "You choose the science. The disease chooses the bill."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Uroboros Ventures""

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/ouroboros-capital"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/ouroboroscap"},{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/investors/ub_ventures/portfolio/exits"},{"title":"UB Ventures Overview","url":"https://pitchbook.com/profiles/investor/264692-98"},{"title":"We are a Ukrainian company. We stand with our colleagues, friends, family, and with all people of Ukraine. Our message","url":"https://getprospect.com/business-directory/ouroboros-group"},{"title":"ouroboros innovations inc","url":"https://intch.org/company/ouroboros-innovations-inc"},{"title":"u ventures","url":"https://ecosystem.madrimasd.org/investors/u_ventures"},{"title":"Company Overview","url":"https://www.datanyze.com/companies/ub-ventures/556154453"},{"title":"uob venture","url":"https://seedtable.com/investors/uob-venture"},{"title":"uob venture","url":"https://prod.actual.seedtable.com/investors/uob-venture"}]

I didn't find any results for "Uroboros Ventures" with that exact spelling. The search returned firms with similar names, but none is clearly the one you mean.

**Closest name matches:**

- **Ouroboros Capital:** CB Insights categorizes it as a crypto hedge fund, founded in 2022 and based in Delaware. Caplight gives a different picture. It describes it as a cryptocurrency hedge fund specializing in delta-neutral DeFi yield strategies and on-chain market making. Caplight also lists its headquarters as Singapore, which conflicts with CB Insights' Delaware location.
- **Ouroboros Group:** A GetProspect profile describes it as a private investment firm specializing in middle-market corporate acquisitions and operations. It works in manufacturing, healthcare, and consumer.
- **Ouroboros Innovations Inc.:** Its founder, Liam Kettler, bootstrapped it as a framework for allocating capital and labor under one decentralized system.

**Less likely matches:**

- **UB Ventures:** PitchBook lists a venture firm based in Singapore, founded in 2018, which prefers to invest in the blockchain, fintech, and technology sectors.

Most of these come from aggregator or directory sites, and some of their data is paywalled or inconsistent, so verify anything important with the firm's official website or a registry filing.

If you can tell me where the firm operates, its sector, or a website, I can narrow the search. I can also search the alternate spelling "Ouroboros Ventures," which I haven't tried yet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://zaka.vc/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, every line that names a portfolio company or startup invested in by ZAKA, including any investment date, round, or amount shown. Also return the page's publication or last-updated date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://gv.com/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states where the GV (Google Ventures) team is located or headquartered, the office addresses, and any sentence describing what GV invests in or its fund size. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://eic.ec.europa.eu/index_en",
  "prompt": "Return word-for-word, without summarising or translating, every sentence on this page that describes what the European Innovation Council is, who runs it, where it is based, and whether it makes equity investments in companies. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Ouroboros Ventures\" s.r.o.",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't include the team's location, headquarters, office addresses, fund size, or a publication date. It does contain these sentences describing what GV invests in. Each quote is cut to 125 characters or fewer, so the full sentences are not reproduced:

1. "We've backed 50+ companies building the next generation of AI-native applications"
2. "We've partnered with 20 AI healthcare companies, including insitro and Isomorphic Labs,"
3. "We've invested in over a dozen of the picks and shovels, including breakouts like Stackblitz (Bolt.new) and Vercel."
4. "We were early to back the infrastructure layer of AI, including a dozen companies pushing the frontiers of"
5. "That early conviction led to early investments in companies like Snorkel, Deepset, SambaNova, Modular, and Lightmatter."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**What the EIC is**
- "One of the largest deep tech investors in Europe" (homepage banner)
- "offering €6,5 billion of support to startups, research & tech transfer" (same banner)
- "The European Innovation Council (EIC) published its Impact Report 2026" (Impact Report 2026 banner)

**Who runs it**
- "European Innovation Council and SMEs Executive Agency" is named as the managing body, with a link to the European Innovation Council and Small and Medium-sized Enterprises Executive Agency (EISMEA).

**Where it is based**
- The page does not state where the EIC is based. It mentions Brussels only as the location of the EIC Summit 2026, not as the EIC's headquarters.

**Equity investments**
- "Equity investment supporting the scale-up of breakthrough innovation." (The EIC Fund section)

**Publication dates shown**
- 30 September 2026 (news: European Capital of Innovation 2027 semi-finalists)
- 29 September 2026 (news: Hyperion Robotics funding)
- 15 September 2026 (news: EIC Board statement)
- 10 September 2026 (news: Advanced Innovation Challenges projects)
- The EIC Impact Report 2026 banner shows no publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page lists the following portfolio companies. I've given the names only, not the verbatim lines, because the lines are repetitive name lists:

**Group 1:** WonderTx, Aerogen Systems, FinalDose, PerfectBit, Human Archive, AxionOrbital Space, CellType, Sygaldry Technologies, HexemBio, Ateios Systems, Mews, Zephyr Fusion, DeepSeq.AI, Kangaroo Biomedical, Cirrus Therapeutics, Kano Therapeutics, Lunabill, Verne Robotics, Avelis Health, b-12, Nephrogen, Bullseye Biosciences, Alixia Therapeutics, Adentris, Bluejay, Mbodi AI, Inversion Semiconductor, Momentous Therapeutics

**Group 2:** Promakhos, Superlinked, Creasallis, ExoMatter, Sutro, Yenmo, edgetrace, Lime Therapeutics, SharpGrid, Eigen Therapeutics, Webel, Olio Labs, SpectreXR, KiraGen, InGel Therapeutics, Salu, Vetstor, MediSearch, ParcelBio, ExcepGen, Tripmakery, bit.bio, Alpha3D, Supliful, Miros, Sensible Biotechnologies, CRUXO, e-mobilio

**Group 3:** Prograd, Wectory, Flexkeeping, Velaris, Stackt, Orderlion, Talkie.ai, StoryBox, memtime, Startup Wise Guys, Sorwe, smino, ZeePrime, SaaShop, Rendin, Readmio, Foodsight, Blockmate, We Make Games, CorpLife, Conntac, boam, easySales, GitGut, Deskree, and an unnamed "Biotech in stealth mode" entry

The page shows no investment dates, funding rounds, or amounts for any company. It also shows no publication or last-updated date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Ouroboros Ventures" s.r.o."

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/ouroboros-capital"},{"title":"Solid Ventures s.r.o., IČO: 24629529, sídlo: Brno","url":"https://www.finmag.cz/obchodni-rejstrik/24629529-solid-ventures-s-r-o"},{"title":"Digital Ventures s.r.o., IČO (05698162), sídlo Brno","url":"https://www.mesec.cz/rejstrik-firem/firma-digital-ventures-s-r-o-05698162"},{"title":"Sourcefabric Ventures s.r.o., IČO: 03806901, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/03806901-sourcefabric-ventures-s-r-o"},{"title":"otb ventures","url":"https://privateequitylist.com/investor/otb-ventures"},{"title":"Sourcefabric Ventures s.r.o., IČO (03806901), sídlo Praha","url":"https://www.mesec.cz/rejstrik-firem/firma-sourcefabric-ventures-s-r-o-03806901"},{"title":"GOLEM VENTURES s.r.o., IČO (08896801), sídlo Praha","url":"https://www.mesec.cz/rejstrik-firem/firma-golem-ventures-s-r-o-08896801"},{"title":"Algorithmiq Ventures, s.r.o., IČO (05320151), sídlo Praha","url":"https://www.mesec.cz/rejstrik-firem/firma-algorithmiq-ventures-s-r-o-05320151"},{"title":"borovicka capital","url":"https://superscout.co/investor/borovicka-capital"}]

I couldn't find any record of a company called "Ouroboros Ventures s.r.o." in these results. None of the pages mention that name.

The closest name match is Ouroboros Capital. CB Insights describes it as a crypto hedge fund that offers various investment solutions, and the company was founded in 2022 and is based in Delaware. It is a US-based fund, not a Czech s.r.o., so it is probably a different entity.

The other results are Czech company-register pages for businesses with "Ventures" in their names, such as Solid Ventures, Digital Ventures, Sourcefabric Ventures, and Golem Ventures. They matched only on that shared word.

An s.r.o. is a Czech or Slovak limited liability company, and the official register is the best place to check one. The registry sites in these results draw their data from justice.cz and the RES service, which combines several public registers including the commercial register.

If you can share the company's IČO (the Czech business ID number) or its registered address, I can search with those. I can also try the name without the "s.r.o." suffix or with alternate spellings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://zaka.vc/contact",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line on this page that gives an office address, city, the company legal name, company ID (IČO), or the location of the team. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2024/07/19/czech-zaka-launches-its-first-fund-of-15m",
  "prompt": "Return word-for-word, without summarising or translating, every sentence in this article that mentions ZAKA, its location (city/country), its fund size, first close, minimum ticket, investment stages, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ZAKA VC pre-seed round led 2026",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Farkasova International investice startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Google Ventures GV Alphabet venture capital arm headquarters Mountain View",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "European Innovation Council EISMEA Brussels headquarters equity investment",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "19 July, 2024, 16:55"

**Relevant excerpts** (each quote is trimmed to stay under the 125-character limit):

- **Location:** "Operating from Prague and London, ZAKA VC"
- **Fund size:** "sized at €15 million to support early-stage startups across the US and EU markets"
- **Founding and background:** "Founded in 2020 by seasoned entrepreneurs [REDACTED] and [REDACTED]"
- **Fund I and first close:** "ZAKA VC Fund I sized €15 million is now starting with a €10.5 million first closing in July 2024"
- **Minimum ticket:** "with a minimum LP ticket of €130,000 for qualified investors only."
- **Investment stages:** "aims to invest in pre-seed and seed-staged startups across Europe"
- **Geographic focus:** "predominantly Central Europe, Baltics, UK, DACH"
- **Sector focus:** "The main investment focus is on B2B software, cross-sectional application of AI in B2B, biotech, and health tech."
- **Expansion history:** "Initially, ZAKA VC focused primarily on the Central and Eastern European market"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Google Ventures GV Alphabet venture capital arm headquarters Mountain View"

Links: [{"title":"GV (company)","url":"https://en.wikipedia.org/wiki/GV_(company)"},{"title":"GV (Google Ventures)","url":"https://vc4a.com/gv-google-ventures/?cmt=12"},{"title":"builtworlds.com","url":"https://builtworlds.com/companies/gv/"},{"title":"builtworlds.com","url":"https://builtworlds.com/?p=25691"},{"title":"GV (Google Ventures)","url":"https://vc4a.com/gv-google-ventures/"},{"title":"Salestools LogoSalestools","url":"https://salestools.io/en/report/gv-google-ventures--headquarters"},{"title":"Salestools LogoSalestools","url":"https://salestools.io/report/gv-google-ventures--headquarters"},{"title":"Google Ventures Investor","url":"https://mindmaps.femtech.health/firms/151466"},{"title":"gv google ventures","url":"https://vcbeast.com/claim/gv-google-ventures"},{"title":"At a Glance","url":"https://vcbeast.com/vc-firms/gv"}]

GV is headquartered in Mountain View, California. It is Alphabet's venture capital arm and was formerly called Google Ventures.

- **Origins and ownership:** The firm's own materials say it launched as Google Ventures in 2009. Wikipedia gives a different start: founded March 31, 2010, with the Google Ventures name used from 2010 to 2015. It was owned by Google until 2015 and by Alphabet Inc. since then.
- **Offices:** Mountain View serves as the home base, and the firm also has offices in San Francisco, Boston, New York, and London. Wikipedia's headquarters entry lists Mountain View, California; San Francisco, California; New York City, New York; Cambridge, Massachusetts; London, England.
- **Street address:** A business directory lists the firm at 1600 Amphitheatre Pkwy, Mountain View, CA 94043. From my own background knowledge, that is also Google's main campus address, but I did not confirm it against a primary source.
- **Size:** The sources disagree on assets under management. GV's own profile cites $5 billion under management, while a directory site reports $8B+ AUM. Wikipedia lists total assets of approximately $10 billion.
- **Notable investments:** Its well-known outcomes include Uber, Slack, One Medical Group, Nest, Flatiron Health, and Duo Security.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "European Innovation Council EISMEA Brussels headquarters equity investment"

Links: [{"title":"Product Reports Resources Pricing Login Book a demo","url":"https://dealroom.co/investors/european-innovation-council/"},{"title":"European Innovation Council Overview","url":"https://www.pitchbook.com/profiles/investor/472523-14"},{"title":"eismea european innovation council and smes executive agency","url":"https://eu-careers.europa.eu/en/eismea-european-innovation-council-and-smes-executive-agency"},{"title":"european innovation council and small and medium sized enterprises executive agency en","url":"https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_en"},{"title":"european innovation council and small and medium sized enterprises executive agency nl","url":"https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_nl"},{"title":"european innovation council and small and medium sized enterprises executive agency bg","url":"https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_bg"},{"title":"european innovation council and small and medium sized enterprises executive agency fr","url":"https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_fr"},{"title":"european innovation council and small and medium sized enterprises executive agency el","url":"https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_el"},{"title":"european innovation council and small and medium sized enterprises executive agency en","url":"https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_en"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/eismea/team"}]

The search points to Brussels as the base for the European Innovation Council (EIC) and its executive agency, with equity handled through a separate fund arm. The sources are not fully consistent, so I've noted where they conflict.

**Structure and location**
- The Commission says EISMEA was set up in April 2021 to run the EIC's activities and SME programmes under one agency. The European Innovation Council and Small and Medium-sized Enterprises Executive Agency (EISMEA) was established on 1 April 2021. It groups together in one agency all the activities of the European Innovation Council (EIC) and the programmes related to small and medium-sized enterprises.
- Its listed location is Brussels (Belgium), and the Commission gives a postal address of Boulevard Simon Boliva
… [skrátené, 1453 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Farkasova International investice startup"

Links: [{"title":"Kostlivci ze skříní vyskakují často. Právnička píše, co u nás chybí startupovým investicím","url":"https://cc.cz/kostlivci-ze-skrini-vyskakuji-casto-pravnicka-pise-co-u-nas-chybi-startupovym-investicim/"},{"title":"Finské fondy více investují do zahraničních startupů","url":"https://www.businessinfo.cz/clanky/finske-fondy-vice-investuji-do-zahranicnich-startupu/"},{"title":"Jan Hlavsa","url":"https://cc.cz/author/janhlavsa/"},{"title":"Investice - strana 7","url":"https://www.finmag.cz/tema/investice?strana=7"},{"title":"Současná vláda promrhala příležitost, jsem z ní zklamaný, říká investor Fryc","url":"https://www.e15.cz/tema/miliardari/soucasna-vlada-promrhala-prilezitost-jsem-z-ni-zklamany-rika-investor-fryc-1410201"},{"title":"ZAKA Ventures","url":"https://signal.nfx.com/firms/zaka-ventures"},{"title":"Přejít na hlavní obsah","url":"https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/economy-works-people/investment-plan-results/investment-plan-czechia_cs"},{"title":"Zaka VC se mění z rodinného na klasický startupový fond. Má stovky milionů korun","url":"https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=8"}]

I couldn't find any results about Farkasova International or its startup investments. None of the results mention the company, so I can't say what it does or whether it invests in startups.

The results did cover the Central European startup investment scene, which may be useful context:

- **Angel investing in Czechia:** A Sedlakova Legal lawyer writes that angel networks are well developed abroad, while the Czech market largely lacks this type of investor, with a few exceptions such as Garage Angels. Deals at the pre-seed stage generally stay within a few hundred thousand Czech crowns.
- **Czech funds:** Czech investment funds tend to be mid-sized and back startups from pre-seed rounds through Series A.
- **Zaka VC:** The fund has put hundreds of millions of crowns into 55 startups over the years. It has now opened to outside investors, targeting €15 million in total, and has raised €10.5 million so far.
- **Slovak FIT:** The Fund of Innovations and Technologies made its first investment in the startup Datamolino, putting €500,000 into it.

To track down Farkasova International, you could:
- Try the Slovak spelling "Farkasová," since the name may appear with diacritics in local sources.
- Search the Slovak (ORSR) or Czech (ARES) business registers for the company's legal entity and officers.
- Check startup databases such as Crunchbase or Dealroom for investment records.

If you can tell me the country, sector, or any known portfolio companies, I can run a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ZAKA VC pre-seed round led 2026"

Links: [{"title":"ZAKA VC Research","url":"https://f4.fund/firms/zaka-vc"},{"title":"therecursive.com","url":"https://therecursive.com/?p=38085"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zaka-ventures"},{"title":"ZAKA VC Activity","url":"https://f4.fund/firms/zaka-vc/activity"},{"title":"altss.com","url":"https://altss.com/profile/zaka.md"},{"title":"- The Bridge Club","url":"https://thebridgeclub.beehiiv.com/p/zaka-launches-15m-venture-fund"},{"title":"ZAKA Ventures","url":"https://signal.nfx.com/firms/zaka-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/zaka"},{"title":"zaka launches new vc fund 15m","url":"https://siliconcanals.com/zaka-launches-new-vc-fund-15m/"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=51832"}]

Links: [{"title":"Total Raised","url":"https://www.cbinsights.com/company/deepseqai/financials"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zaka-ventures"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/deepseqai"},{"title":"DeepSeq.AI Growth Score CB Rank Heat Score","url":"https://www.crunchbase.com/organization/deepseq-ai/financial_details"},{"title":"DeepSeq.AI Secures Investment from Zaka VC to Advance AI-Driven Protein Drug Discovery Platform","url":"https://trial.medpath.com/news/deepseq-ai-secures-investment-from-zaka-vc-to-advance-ai-driven-protein-drug-discovery-platform"},{"title":"zaka vc invests in deepseq ai to transform ai based protein drug discovery","url":"https://www.einpresswire.com/article/879998435/zaka-vc-invests-in-deepseq-ai-to-transform-ai-based-protein-drug-discovery"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/deepseq"},{"title":"ZAKA VC Activity","url":"https://f4.fund/firms/zaka-vc/activity"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/deepseq-ai-joins-illumina-ventures-labs"}]

I couldn't find any source reporting a pre-seed round led by ZAKA VC in 2026. The 2026 deals I found show ZAKA in a supporting role.

ZAKA's own profile describes it as a fund that usually joins deals alongside other seed investors, though it can take the lead. It positions itself as a co-investor with the ability to co-lead rounds, and it is not exclusively a lead investor.

Caplight's ZAKA page lists the firm as a co-investor in five recent deals: ParcelBio (May 2026, Seed), HexemBio (Apr 2026, Seed), Ateios Systems (Mar 2026, Series A), Sygaldry Technologies (Mar 2026, Series A), and Readmio (Feb 2026, Seed). None of these is labeled pre-seed. F4 also says ZAKA participated in Ateios Systems' $7.25M Series A for flexible battery electrode manufacturing.

The closest match is DeepSeq.AI. ZAKA's investment was announced on January 7, 2026, together wi
… [skrátené, 773 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.einpresswire.com/article/879998435/zaka-vc-invests-in-deepseq-ai-to-transform-ai-based-protein-drug-discovery",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions ZAKA, its investment, the amount, the round name, who else invested, and the publication date of this press release."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions ZAKA (ZAKA VC), its seat or office location (Praha, Bratislava, London, Silicon Valley), its fund size, first close, minimum ticket, investment stage, number of startups invested in, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ZAKA Ateios Systems Series A 2026 press release",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.gv.com/about/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states GV is Alphabet's venture capital firm or part of Alphabet/Google, and every sentence stating where GV's offices or headquarters are. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://eismea.ec.europa.eu/index_en",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states the agency's address, city, or location (for example Brussels or Boulevard Simon Bolivar), and every sentence about the European Innovation Council or equity investment. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Farkasova International\" portfolio investor",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Farkasová\" International venture fond startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Uroboros Ventures portfolio startup seed",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Uroboros Ventures fond Praha startupy",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Agency address or location:** The page doesn't give the agency's address or city. The only location mention is an event: "gathered in Brussels for the Annual I3 Instrument Forum 2026."

**Equity investment:** The page doesn't use the phrase "equity investment." The closest reference is the EIC Board statement, which mentions "the distinct character of the EIC Fund."

**Sentences about the European Innovation Council (EIC):**
- "The Agency is responsible for developing and implementing the European Innovation Council"
- "The EIC identifies and supports breakthrough technologies and innovations"
- "The Board welcomes with caution the adoption of the Council's Partial General Approach"
- "EIC Accelerator awardee Hyperion Robotics raises €6.4 million and moves towards a major procurement deal"
- "EIC Accelerator awardee Check Point Care has accelerated its commercial scale-up"
- "From challenges to breakthrough solutions: EIC launches first Advanced Innovation Challenges projects"
- "Following a competitive and rapid evaluation, 20 projects have been selected to enter the first stage of the pilot."

**Publication dates of news items:**
- 2 October 2026
- 30 September 2026
- 29 September 2026
- 15 September 2026
- 10 September 2026 (two items)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 22. 7. 2024 (the article is listed under Startupy).

**Fund size:** The article says Zaka aims for a total of 15 million euros, and it has already raised 10.5 million euros. The Czech source text reads: "cílí na celkovou částku 15 milionů eur (přibližně 380 milionů korun)".

**Number of startups:** The article says Zaka has invested in 55 startups. It also says the fund supported more than fifty startups in its first four years and more than twenty last year. The Czech source text reads: "Celkem jde o 55 startupů a proinvestovaných téměř 280 milionů korun."

**Stage:** Zaka focuses on pre-seed and seed-stage startups. The Czech source text reads: "Zaka se chce nadále zaměřovat na startupy v takzvaných pre-seed a seed fázích v Evropě".

**Geographic focus:** Zaka started mainly in Central and Eastern Europe and has since expanded to the UK, the US, and German-speaking countries. The Czech source text reads: "V začátcích se Zaka soustředila hlavně na region střední a východní Evropy".

**Not stated in the article:** The article does not give Zaka's seat or office location, its first close, or its minimum ticket size. It does say the fund has about ten team members.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Statements that GV is Alphabet's firm or part of Alphabet/Google:**

- "With Alphabet as our sole limited partner" (About section)
- "Google Ventures becomes GV" (2015 timeline entry)

The page doesn't explicitly say GV is part of Alphabet beyond the sole-LP statement. It describes GV as "an independent venture capital firm," which is worth noting alongside the Alphabet relationship.

**Statements about GV's offices or headquarters:**

- "Founded as Google Ventures in Mountain View and Boston" (2009 timeline entry)
- "GV opens its New York City office" (2010 timeline entry)
- "London office opens for investment in Europe" (2014 timeline entry)
- Headquarters: "San Francisco Bay Area"
- Offices in: "New York," "Cambridge," "London"

**Publication date:** The page does not show a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Date:** The release is dated January 7, 2026 (15:00 GMT), per the page header.

**Sentences mentioning ZAKA, the investment, and other investors:**

1. "is proud to announce an investment from ZAKA VC, a prominent Czech-based VC that has become one of the most active early-stage investors in Europe" (quote truncated to fit the 125-character limit)

2. "ZAKA VC's investment, together with investment funding from Illumina Ventures and leading biotech-related family offices," (the rest of this sentence describes how the funds will be used to scale DeepSeq's data sets and development teams)

3. "ZAKA VC's participation in our funding round, together with other prominent investors like Illumina Ventures," (said by DeepSeq co-founder and CEO Andrew Chang, Ph.D.)

4. "We are pleased to welcome DeepSeq to the Zaka VC portfolio," (said by [REDACTED], Co-Founder and Managing Partner at Zaka VC)

5. Boilerplate on ZAKA VC: it is "an early-stage VC fund bridging Europe and North America," and it "focuses on investment in the Biotech, Healthcare, and Industrial Tech verticals." (paraphrased in part)

**Summary:**
- **Investor:** ZAKA VC, a Czech-based early-stage VC fund
- **Other investors:** Illumina Ventures and leading biotech-related family offices
- **Amount:** Not disclosed in the release
- **Round name:** Not specified in the release (it is referred to only as "our funding round")
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Uroboros Ventures portfolio startup seed"

Links: [{"title":"300+ investors in your industry, stage, and region Get","url":"https://shizune.co/investors/profile/ouroboros-s-substack"},{"title":"Back to u.ventures","url":"https://seedtable.com/investors/uventures/portfolio"},{"title":"Back to UOB Venture","url":"https://seedtable.com/investors/uob-venture/portfolio"},{"title":"UB Ventures Overview","url":"https://pitchbook.com/profiles/investor/264692-98"},{"title":"Uncorrelated Ventures | Activity | F4Uncorrelated Ventures Activity","url":"https://f4.fund/firms/uncorrelated-ventures/activity"},{"title":"u ventures","url":"https://superscout.co/investor/u-ventures"},{"title":"u ventures","url":"https://ecosystem.madrimasd.org/investors/u_ventures"},{"title":"vestbee.com","url":"https://vestbee.com/vc-list/u.ventures"},{"title":"uob venture","url":"https://www.vcbacked.co/directory/investors/uob-venture"},{"title":"Venture Capital","url":"https://www.thetrustedinsight.com/investment-news/startupxseed-ventures-deep-tech-b2b-focused-fund-kicks-off-2019-with-two-exits-business-standard-news-20190425013/"}]

My search returned no results for "Uroboros Ventures" itself. The closest match is **Ouroboros Capital**, which may be the same firm under a different spelling. These results don't confirm that.

One investor directory describes Ouroboros Capital as a VC fund focused on Blockchain and Finance. It lists four investments, at Seed 3 (75%) and Series A 1 (25%) stages. The entries include:

- **Origami Finance**: a seed round of $1.5M dated August 27, 2024. The directory describes it as an automated leverage protocol that allows users to maximise capital efficiency.
- **Alex**: a Series A of $10M dated March 26, 2024. The directory describes it as an open-source DeFi development business based on the Stacks Blockchain.
- **Kodiak Finance**: described as a DEX solution provider. The snippet cuts off before showing its round.

This is a third-party aggregator, so the data may be incomplete or out of date. For a current portfolio, check Crunchbase, PitchBook, or the firm's own website.

If you meant a different firm, **u.ventures** is a separate early-stage fund. It is based in Chicago, Illinois, and Kyiv, Ukraine, and typically writes checks ranging from $200,000 to $2 million. Its notable portfolio companies include Preply, a global EdTech platform, and it often leads investment rounds, particularly in the pre-seed and seed stages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Uroboros Ventures fond Praha startupy"

Links: [{"title":"Start Free Trial","url":"https://www.crunchbase.com/hub/prague-startups"},{"title":"co ocekavaji startupy od prahy lepsi podminky pro venture kapital a talenty ze zahranici otevreni mestskych zakazek a snizeni byrokracie","url":"https://www.businessinfo.cz/clanky/co-ocekavaji-startupy-od-prahy-lepsi-podminky-pro-venture-kapital-a-talenty-ze-zahranici-otevreni-mestskych-zakazek-a-snizeni-byrokracie/"},{"title":"Get Free Access to The Founder's Handbook","url":"https://www.failory.com/blog/venture-capital-firms-czech-republic"},{"title":"Praha mezi technologickou elitou: Startupová scéna má hodnotu více než 19 miliard eur, uvádí Prague Report 2025","url":"https://www.businessinfo.cz/clanky/praha-mezi-technologickou-elitou-startupova-scena-ma-hodnotu-vice-nez-19-miliard-eur-uvadi-prague-report-2025/"},{"title":"Venture Capital","url":"https://altss.com/profile/air-ventures"},{"title":"Pražská startupová scéna je zbytečně roztříštěná, říká ředitel xPORTu Ota Novotný","url":"https://www.businessinfo.cz/cs/clanky/prazska-startupova-scena-je-zbytecne-roztristena-rika-reditel-xportu-ota-novotny-119583.html"},{"title":"Pražská startupová scéna je zbytečně roztříštěná, říká ředitel xPORTu Ota Novotný","url":"https://www.businessinfo.cz/clanky/prazska-startupova-scena-je-zbytecne-roztristena-rika-reditel-xportu-ota-novotny/"},{"title":"Technologický ekosystém Prahy má mít hodnotu přes 19 miliard eur","url":"https://www.lupa.cz/aktuality/technologicky-ekosystem-prahy-ma-mit-hodnotu-pres-19-miliard-eur/"},{"title":"How Foreign Investments Made Prague a Strong Startup Hub","url":"https://netguru.com/blog/foreign-investments-prague-startup-hub"}]

I couldn't find any results about Uroboros Ventures. None of the pages returned mention the firm, so I can't confirm that it exists or say anything about its fund or portfolio. Trying an alternate spelling such as "Ouroboros," or checking the Czech company register (ARES or justice.cz), might help.

The results did cover the Prague startup and venture capital scene:

- **Market size:** A Prague Report 2025, prepared by Dealroom with the Prague Innovation Institute, puts the city's technology ecosystem value at 19.2 billion euros in 2025, with more than 80% of the value of the Czech startup ecosystem concentrated in the capital.
- **Funding:** More than 300 venture-capital-backed startups operate in Prague, and since 2019 they have raised a total of 2.5 billion euros, the second-highest volume in Central and Eastern Europe.
- **Local capital:** A businessinfo.cz article notes that most venture capital comes from the Czech Republic, which could become a problem for future development.
- **Other Prague-based VC firms in the results:**
  - KAYA provides venture capital to early-stage tech startups across Central and Eastern Europe and has a dedicated €90 million fund.
  - Soulmates Ventures, founded in 2020, invests in startups with g
… [skrátené, 408 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Farkasova International" portfolio investor"

Links: [{"title":"Előfizetői tartalom","url":"https://www.portfolio.hu/bank/20040518/farkas-istvant-megvalasztottak-a-pszaf-elnokenek-ki-nem-szavazott-igennel-a-szavazasnal-41249"},{"title":"Foreign Portfolio Investor","url":"https://www.superfinanciera.gov.co/10115712"},{"title":"leszakadt a munka vilagaba vezeto hid hova lett farkas florianek penze 290443","url":"https://privatbankar.hu/cikkek/makro/leszakadt-a-munka-vilagaba-vezeto-hid-hova-lett-farkas-florianek-penze-290443.html"},{"title":"digilibs.fchpt.stuba.sk","url":"https://digilibs.fchpt.stuba.sk/Record/euba.c124627/Cite"},{"title":"DAVID FARKAS A2FQR9","url":"https://in.marketscreener.com/insider/DAVID-FARKAS-A2FQR9/"},{"title":"portfolio.hu","url":"https://portfolio.hu/en/events/speaker/kakosy-csaba/5493"},{"title":"László Csatári","url":"https://www.portfolio.hu/en/events/speaker/csatari-laszlo/14059"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/andrew-farkas"},{"title":"DAVID FARKAS A2FQR9","url":"https://ca.marketscreener.com/insider/DAVID-FARKAS-A2FQR9/"}]

Links: [{"title":"www.jobs.cz","url":"https://www.jobs.cz/rpd/2001388796/?rps=233"},{"title":"www.jobs.cz","url":"https://www.jobs.cz/rpd/2001457219/?rps=233"},{"title":"FARKASOVA INTERNATIONAL, s.r.o. , Praha IČO 07957360 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/07957360"},{"title":"REQUEST A DEMO","url":"https://emis.cn/php/company-profile/HU/FARKAS_G_Bt_en_14768801.html"},{"title":"REQUEST A DEMO","url":"https://emis.cn/php/company-profile/HU/FARKAS_Bt_en_16846712.html"},{"title":"REQUEST A DEMO","url":"https://www.emis.cn/php/company-profile/HU/Farkas_Kft_en_3211110.html"},{"title":"www.companywall.hu","url":"https://www.companywall.hu/v%C3%A1llalat/farkas-istvan/MMdiNqQR"},{"title":"www.companywall.hu","url":"https://www.companywall.hu/v%C3%A1llalat/farkas-istvan/MMdjxJTR"},{"title":"www.companywall.hu","url":"https://www.companywall.hu/v%C3%A1llalat/farkas-es-ignacz-bt/MMF2Cs9Y"}]

I found no evidence that Farkasova International is a portfolio investor. My first search returned mostly unrelated material, such as other people named Farkas and generic regulatory pages on foreign portfolio investment. A follow-up search turned up the company's recruitment listings and a Czech business register entry, and both describe a different kind of business.

- **Business activity:** Recruitment listings on jobs.cz present the firm as an executive search business that helps organizations find senior leaders. Farkasova International is a leading executive search firm that connects exceptional talent with organizations worldwide.
- **Registration:** The Czech commercial register lists FARKASOVA INTERNATIONAL, s.r.o., Praha, IČO 07957360, with share capital of 200,000 CZK and a Prague address.
- **Ownership:** Register entries from February 2025 record changes to the company's partner and statutor
… [skrátené, 519 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ZAKA Ateios Systems Series A 2026 press release"

Links: [{"title":"GlobeNewswire Press Releases","url":"https://technologymagazine.com/globenewswire"},{"title":"English | 简体中文 | 繁體中文 | 한국어 | 日本語","url":"https://www.acnnewswire.com/morenews/30"},{"title":"Newswire Newswire","url":"https://www.newswire.com/newsroom/all/page/51"},{"title":"Newswire Newswire","url":"https://www.newswire.com/newsroom/pr/page/9"},{"title":"zadar labs","url":"https://theconsensus.dev/company/zadar-labs.html"},{"title":"English | 简体中文 | 繁體中文 | 한국어 | 日本語","url":"https://www.acnnewswire.com/morenews/51"},{"title":"GlobeNewswire Press Releases","url":"https://procurementmag.com/globenewswire"},{"title":"www.tullahomanews.com","url":"https://www.tullahomanews.com/?p=119655"},{"title":"Newswire Newswire","url":"https://www.newswire.com/newsroom/page/25"}]

Links: [{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/ocella/financials"},{"title":"Select a theme:   Light Mode  |  Dark Mode","url":"https://www.binghamton.edu/news/story/5287/ateios"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/ateios-systems"},{"title":"Ateios Systems Wins $1 Million Investment in Inaugural TitletownTech’s Start-Up Draft Competition","url":"https://innovationcrossroads.ornl.gov/news/ateios-systems-wins-1-million-investment-in-inaugural-titletowntechs-start-up-draft-competition/"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/ateios"},{"title":"Current Valuation","url":"https://www.premieralts.com/companies/ateios/valuation"},{"title":"2026 03 01 ateios series a","url":"https://startupintros.com/news/2026-03-01-ateios-series-a"},{"title":"Your Source for Venture Capital and Private Equity Financings","url":"https://vcnewsdaily.com/ateios/venture-capital-funding/pbdnbrcwyy"},{"title":"Back to AteiosChangelog and Sources","url":"https://seedtable.com/companies/ateios/funding-rounds/seed-2020-10"}]

I couldn't find an official Ateios or ZAKA press release for a 2026 Series A. The wire-service listings that came back were unrelated. Funding trackers do report a March 2026 Series A, but they disagree on the amount, date, and lead investor.

**What the trackers report**
- **CB Insights** dates the latest round to March 23, 2026, at $7.25M, and lists ZAKA Ventures among the investors. Ateios Systems's latest funding round was a Series A for $7.25M on March 23, 2026.
- **VCBacked** puts the round at about $7.3M in March 2026 and names ZAKA VC among its top investors. $7.3M raised Mar 2026 Series A, and Ateios's investors include Techstars, National Science Foundation, Good Growth Capital, TitletownTech, ZAKA VC.
- **Caplight** dates the round to March 22, 2026, and credits XYZ Ventures with leading the same $7.25M raise. The $7.25M round is attributed to XYZ Ventures as lead.
- **StartupIntros** describes a roughly $7M Series A and gives TitletownTech as lead
… [skrátené, 1491 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Farkasová" International venture fond startup"

Links: [{"title":"Finské fondy více investují do zahraničních startupů","url":"https://www.businessinfo.cz/clanky/finske-fondy-vice-investuji-do-zahranicnich-startupu/"},{"title":"national-policies.eacea.ec.europa.eu","url":"https://national-policies.eacea.ec.europa.eu/fr/node/976"},{"title":"evropane tupe konci na realitach to vpred neposouva vedu technologie ani staty","url":"https://forbes.cz/evropane-tupe-konci-na-realitach-to-vpred-neposouva-vedu-technologie-ani-staty/"},{"title":"suomeksi  česky  english","url":"https://mzv.gov.cz/helsinki/cz/obchod_a_ekonomika/aktuality/ceske_startupy_se_predstavily_finskym.html"},{"title":"venture capital firms budapest","url":"https://www.papermark.com/blog/venture-capital-firms-budapest.md"},{"title":"venture capital firms budapest","url":"https://www.papermark.com/es/blog/venture-capital-firms-budapest.md"},{"title":"Portfolio Companies","url":"https://seedtable.com/investors/fond-fondov"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"www.newstream.cz","url":"https://www.newstream.cz/stitek/start-up/2"}]

Links: [{"title":"BRAD L FARKAS A02LLW","url":"https://es.marketscreener.com/insider/BRAD-L-FARKAS-A02LLW/"},{"title":"BRAD L FARKAS A02LLW","url":"https://ch.marketscreener.com/insider/BRAD-L-FARKAS-A02LLW/"},{"title":"BRAD L FARKAS A02LLW","url":"https://in.marketscreener.com/insider/BRAD-L-FARKAS-A02LLW/"},{"title":"BRAD L FARKAS A02LLW","url":"https://www.zonebourse.com/insider/BRAD-L-FARKAS-A02LLW/"},{"title":"BRAD L FARKAS A02LLW","url":"https://ch.zonebourse.com/insider/BRAD-L-FARKAS-A02LLW/"},{"title":"Speaking at","url":"https://podim.org/?p=30776"},{"title":"ZANDER FARKAS A24X52","url":"https://in.marketscreener.com/insider/ZANDER-FARKAS-A24X52/"},{"title":"ZANDER FARKAS A24X52","url":"https://ca.marketscreener.com/insider/ZANDER-FARKAS-A24X52/"},{"title":"tatjana zabasu mikuz","url":"https://podim.org/brella-speaker/tatjana-zabasu-mikuz/"}]

Links: [{"title":"FARKASOVA INTERNATIONAL, s.r.o. , Praha IČO 07957360 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/07957360"},{"title":"econpapers.repec.org","url":"https://econpapers.repec.org/RAS/pka231.htm"},{"title":"slovakia venture to future fund","url":"https://startups.one.gob.es/investors/slovakia_venture_to_future_fund"},{"title":"x ventures 1","url":"https://app.dealroom.co/investors/x_ventures_1"},{"title":"Portfolio Companies","url":"https://seedtable.com/investors/fond-fondov"},{"title":"New HUF 17 Billion Venture Capital Fund Launched for AI, Deeptech & Greentech Startups in Hungary","url":"https://xpatloop.com/channels/2026/02/new-huf-17-billion-venture-capital-fund-launched-for-ai-deeptech-and-greentech-startups-in-hungary.html"},{"title":"x ventures 1","url":"https://app.dealroom.co/companies/x_ventures_1"},{"title":"Judit Karsai","url":"https://authors
… [skrátené, 3974 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://therecursive.com/?p=38085",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions ZAKA, ExoMatter, the round name, the amount, who led or joined the round, and the publication date of this article."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.ateios.com/news",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that announces a funding round, the round name, amount, lead investor, the investors named (including ZAKA or ZAKA VC if present), and the announcement date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_en",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states the executive agency's address, headquarters, or the city it is located in (for example Brussels), and every sentence that says the agency runs the European Innovation Council or its equity activities. Also return any publication date shown."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Two headlines on the page announce funding rounds:

1. "Ateios Systems Closes $7.25M Series A to Scale Next-Generation Battery Electrode Manufacturing." Date: March 22nd, 2026 (Press Release).
2. "Ateios Raises $1.25 Million in Seed Funding To Reshape Battery Manufacturing." Date: August 15th, 2020 (Company News).

The page includes only these headlines, not the full announcement text. So it does not name a lead investor or any other investors, and it does not mention ZAKA or ZAKA VC.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
No sentence in the page mentions ZAKA or ExoMatter, so there is nothing to return for those terms. The page is a homepage listing of several articles, not a single article, so it has no one "this article" with a single round name, amount, or publication date.

The closest match is the Estonian spacetech Golbriak Space, which raised a €4M seed round co-led by Join Capital and PhotonVentures. Its listing is dated but the date isn't shown in the excerpt. If you meant that round, or a different article, send me the text or URL and I can pull out the relevant sentences.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Address and location:**
- "Boulevard Simon Bolivar 34"
- "1000 Brussels"
- "Belgium"
- "Office SB34"

**EIC activities:**
- "EISMEA groups together in one agency all the activities of the European Innovation Council (EIC)"

The page does not mention equity activities.

**Publication dates:**
- 1 June 2026 (EISMEA organisation chart)
- 2 October 2026 (news article: "Annual I3 Instrument Forum 2026")
- 17 June 2026 (news article: "Call for Expression of Interest")
- 29 May 2026 (news article: "EU co-funded project UNITE")
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"ZAKA VC\" HexemBio seed round announces",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"ZAKA\" ParcelBio seed round 2026 announces investors",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""ZAKA VC" HexemBio seed round announces"

Links: [{"title":"hexem bio","url":"https://www.vcbacked.co/company/hexem-bio"},{"title":"zaka vc","url":"https://allbusiness.africa/investors/zaka-vc"},{"title":"HexemBio Raises $10.4 Million in Seed Funding","url":"https://raising.fi/news/hexembio-seed-april-2026"},{"title":"HexemBio favicon","url":"https://raising.fi/company/hexemb"},{"title":"SOSV — Activity | F4SOSV Activity","url":"https://f4.fund/firms/sosv/activity"},{"title":"congratulations professor ebrahimkhani and hexembio","url":"https://www.synbio.pitt.edu/news/congratulations-professor-ebrahimkhani-and-hexembio"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/hexemb"},{"title":"ZAKA VC Activity","url":"https://f4.fund/firms/zaka-vc/activity"},{"title":"privateequitylist.com","url":"https://privateequitylist.com/investor/zakavc"},{"title":"# HexemBio","url":"https://yespress.io/hexembio.md"}]

**ZAKA VC's role in HexemBio's seed round is unconfirmed.** Only one source names it as an investor, and the announcement coverage I found doesn't mention it.

- **The one source naming ZAKA VC:** VCBacked's profile lists ZAKA VC among HexemBio's investors, alongside Gaingels, Alumni Ventures, Draper Associates, and Seraphim Space. It labels the most recent round as Seed and dates the last funding to March 2026.
- **Announcement coverage:** Other sources credit Draper Associates as the lead. One says HexemBio successfully raised $10.4 million in a seed funding round. The University of Pittsburgh's announcement says the round was led by Draper Associates, with participation from SOSV and Seraphim Space. None of these list ZAKA VC.
- **Date conflict:** VCBacked gives March 2026, while another source says the funding was announced on April 7, 2026.
- **ZAKA VC's activity:** ZAKA VC is a family venture house investing in early-stage tech startups globally, focusing on pre-seed and seed stages, primarily in Europe. The F4 activity page I found lists other 2026 deals, but not HexemBio. That page is partial, so this doesn't rule anything out.

I didn't find a ZAKA VC announcement or a HexemBio press release that names it. To confirm, check HexemBio's own announcement or ZAKA VC's news and portfolio pages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""ZAKA" ParcelBio seed round 2026 announces investors"

Links: [{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/parcelbio"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/parcelbio/financials"},{"title":"zaka vc","url":"https://www.vcbacked.co/directory/investors/zaka-vc"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/parcelbio"},{"title":"o.parsers.vc","url":"https://o.parsers.vc/startup/parcelbio.com/"},{"title":"Recently FundedUSD 100.0KTechnology, Information and Media","url":"https://www.trysignalbase.com/news/funding/parcelbio-raises-100k-seed-round"},{"title":"ZAKA VC Activity","url":"https://f4.fund/firms/zaka-vc/activity"},{"title":"ParcelBio favicon","url":"https://raising.fi/company/parcelbio"},{"title":"investor list","url":"https://www.premieralts.com/companies/parcelbio/investor-list"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zaka-ventures"}]

Yes. ZAKA VC is reported as one of the investors in ParcelBio's roughly $13 million seed financing. I didn't find the original company announcement in these results, so this comes from third-party trackers, and they don't fully agree on the details.

**Investors**
- One summary of the round says Breyer Capital led it, and that ZAKA VC took part alongside General Catalyst, Y Combinator, Metaplanet, and SurgePoint Capital. The round was led by Breyer Capital, with participation from General Catalyst, Y Combinator...
- Caplight dates a $13M round led by Breyer Capital to May 7, 2026. $13M round led by Breyer Capital.
- VCBacked lists ZAKA VC among ParcelBio's investors, along with General Catalyst, Alumni Ventures, Y Combinator, and Pioneer Fund. ParcelBio's investors include General Catalyst, Alumni Ventures, Y Combinator, Pioneer Fund, ZAKA VC.
- F4's ZAKA VC activity page also counts ParcelBio as a company the firm backed, citing the $13M financing. Backed ParcelBio, which secured $13M in financing for next-generation mRNA medicine development.

**Where the sources conflict**
- **Date and round label:** Most trackers point to May 2026. CB Insights instead records a $13.17M Series A on March 4, 2026, with Undisclosed Investors listed. Caplight also has a March 4 entry for $13.17M, labeled as a seed round.
- **Total raised:** Figures range from $13.2M raised (VCBacked) to $14M (Caplight) to $18.67M over 4 rounds (CB Insights).
- **Earlier round:** Premier Alts lists a May 2024 seed round in which Metaplanet Holdings is the named investor and ZAKA VC appears among the other investors. Other investors ... ZAKA VC

**About ZAKA**
CB Insights describes ZAKA Ventures as a firm that focuses on pre-seed and seed investments in the technology sector. It was founded in 2019 and is based in Stare Mesto, Czech Republic.

To confirm the date and the full investor list, check ParcelBio's newsroom or the original press release,
… [skrátené, 145 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b13.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b13.json",
  "content": "[\n  {\n    \"candidate_id\": \"C059\",\n    \"website\": \"https://www.farkasovainternational.com\",\n    \"identity\": [],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Headquartered in Prague, Czech Republic\",\n      \"source_url\": \"https://www.farkasovainternational.com\",\n      \"quote\": \"Headquartered in Prague, Czech Republic\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"advisory\"],\n      \"value_text\": \"talent advisory firm\",\n      \"source_url\": \"https://www.farkasovainternational.com\",\n      \"quote\": \"Farkasova International is a leading executive leadership search and talent advisory firm.\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [\n      {\n        \"value\": \"executive search and talent advisory firm, not an investor into companies\",\n        \"value_text\": \"talent advisory firm\",\n        \"source_url\": \"https://www.farkasovainternational.com\",\n        \"quote\": \"Farkasova International is a leading executive leadership search and talent advisory firm.\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": \"no investment found\"\n      }\n    ],\n    \"not_found\": [\"identity\", \"investments\", \"sectors\", \"stages\", \"ticket\", \"total_capital\", \"funds\"],\n    \"early_exit\": \"no_investment_found\",\n    \"search_log\": [\n      \"FARKASOVA INTERNATIONAL s.r.o. farkasovainternational.com\",\n      \"Farkasova International investice startup\",\n      \"\\\"Farkasova International\\\" portfolio investor\",\n      \"\\\"Farkasová\\\" International venture fond startup\"\n    ]\n  },\n  {\n    \"candidate_id\": \"C199\",\n    \"website\": null,\n    \"identity\": [],\n    \"hq_country\": null,\n    \"investor_type\": null,\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [\n      {\n        \"value\": \"no investment found\"\n      }\n    ],\n    \"not_found\": [\"identity\", \"hq_country\", \"investor_type\", \"investments\", \"sectors\", \"stages\", \"ticket\", \"total_capital\", \"funds\"],\n    \"early_exit\": \"no_investment_found\",\n    \"search_log\": [\n      \"Uroboros Ventures s.r.o. investice\",\n      \"\\\"Uroboros Ventures\\\"\",\n      \"\\\"Ouroboros Ventures\\\" s.r.o.\",\n      \"Uroboros Ventures portfolio startup seed\",\n      \"Uroboros Ventures fond Praha startupy\"\n    ]\n  },\n  {\n    \"candidate_id\": \"C192\",\n    \"website\": \"https://eic.ec.europa.eu\",\n    \"identity\": [],\n    \"hq_country\": {\n      \"value\": \"other\",\n      \"value_text\": \"1000 Brussels\",\n      \"source_url\": \"https://commission.europa.eu/about/departments-and-executive-agencies/european-innovation-council-and-small-and-medium-sized-enterprises-executive-agency_en\",\n      \"quote\": \"1000 Brussels\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"public_vc\"],\n      \"value_text\": \"Equity investment supporting the scale-up of breakthrough innovation\",\n      \"source_url\": \"https://eic.ec.europa.eu/index_en\",\n      \"quote\": \"Equity investment supporting the scale-up of breakthrough innovation.\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [],\n    \"not_found\": [\"identity\
… [skrátené, 6383 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b13.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b13 done. Output: C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b13.json (5 records).\n\n- C059 FARKASOVA INTERNATIONAL: advisory (executive search, Prague). 0 investments. early_exit no_investment_found, with red flag \"no investment found\" (no source) plus \"advises\" flag.\n- C199 Uroboros Ventures: no website and no trace found in 5 searches. 0 investments. early_exit no_investment_found. Name matches \"Ouroboros Capital\" are a different entity and were not used.\n- C192 European Innovation Council: public_vc (equity via EIC Fund). HQ Brussels (EISMEA address). early_exit foreign_hq.\n- C155 Google Ventures (GV): vc, HQ San Francisco Bay Area. early_exit foreign_hq.\n- C195 ZAKA VC: vc, Czech-based, 7 investments (6 portfolio names from zaka.vc, plus DeepSeq.AI dated 2026-01-07 from the startup's press release). Fund I EUR 15 million (2024). early_exit null.\n\nDoubts:\n- ZAKA ticket left null. The only figure, \"minimum ticket 130K\", appears to be the LP minimum for the fund, not a startup check size.\n- ZAKA: the second dated deal could not be verified from allowed sources. Ateios, HexemBio and ParcelBio are supported only by trackers, and the ZAKA-linked round claims conflict.\n- ZAKA portfolio quotes are bare company names, because the fetch returned names only.\n- Several quotes come from WebFetch output, which the tool may have condensed. Machine-check may reject some.\n- EIC hq uses the EISMEA address, the managing agency."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

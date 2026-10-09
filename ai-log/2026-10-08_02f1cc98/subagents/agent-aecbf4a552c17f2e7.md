# Subagent: Evidence v3 wave2 batch 15 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:10:52

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b15.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b15.json

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b15.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b15.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C114",
4	    "name": "HILLBRIDGES",
5	    "other_names": [],
6	    "known_website": null,
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Hillbridges, s. r. o., IČO 36799327"
8	  },
9	  {
10	    "candidate_id": "C132",
11	    "name": "Zero Gravity Capital",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Zero Gravity Capital s.r.o., IČO 52651894"
15	  },
16	  {
17	    "candidate_id": "C149",
18	    "name": "Berkley SkyDeck Fund",
19	    "other_names": [],
20	    "known_website": null,
21	    "registry_hint": null
22	  },
23	  {
24	    "candidate_id": "C153",
25	    "name": "University2Ventures",
26	    "other_names": [],
27	    "known_website": null,
28	    "registry_hint": null
29	  },
30	  {
31	    "candidate_id": "C031",
32	    "name": "Stratum Partners",
33	    "other_names": [],
34	    "known_website": "www.stratum.eu",
35	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Stratum Partners s.r.o., IČO 07607539"
36	  }
37	]
````

</details>

<details><summary>🔧 ToolSearch</summary>

````text
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
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
  "query": "Hillbridges venture capital investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero Gravity Capital venture fond investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Berkley SkyDeck Fund investments portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "University2Ventures investments portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Stratum Partners stratum.eu investments",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Hillbridges venture capital investice"

Links: [{"title":"horsley bridge closes 176b fund of funds","url":"https://venturebeat.com/technology/horsley-bridge-closes-176b-fund-of-funds"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/gl-ventures"},{"title":"West Hill Capital Research","url":"https://f4.fund/firms/west-hill-capital"},{"title":"west hill capital","url":"https://superscout.co/investor/west-hill-capital"},{"title":"# Hillfarrance Venture Capital","url":"https://altss.com/profile/hillfarrance-venture-capital.md"},{"title":"hillside enterprises","url":"https://superscout.co/investor/hillside-enterprises"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/covenant-venture-capital"},{"title":"bridges ventures adds investment director","url":"https://www.institutionalinvestor.com/article/2bsz1iot8qkvn57d26n0g/innovation/bridges-ventures-adds-investment-director"},{"title":"Venture Capital","url":"https://altss.com/profile/hillclimber"}]

Links: [{"title":"hillsbridge investment group sodie sa","url":"https://intch.org/company/hillsbridge-investment-group-sodie-sa"},{"title":"# London Borough of Hillingdon Pension Fund","url":"https://altss.com/profile/london-borough-of-hillingdon-pension-fund.md"},{"title":"bridges fund management limited","url":"https://www.escapethecity.org/organisation/bridges-fund-management-limited"},{"title":"bridges fund management","url":"https://www.worldbenchmarkingalliance.org/wba-allies/bridges-fund-management"},{"title":"Bridges closes fourth fund on £220m","url":"https://perenews.com/bridges-closes-fourth-fund-on-220m"},{"title":"Highbridge Capital Management","url":"https://kiwix.colibox.colibris-outilslibres.org/wikipedia_fr_all_mini_2022-10/A/Highbridge_Capital_Management"},{"title":"horsely bridge raises 974m to invest in multiple vc firms","url":"https://venturebeat.com/technology/horsely-bridge-raises-974m-to-invest-in-multiple-vc-firms"},{"title":"bridges fund management","url":"https://impactalpha.com/edge/organization/bridges-fund-management"},{"title":"horsley bridge closes 176b fund of funds","url":"https://venturebeat.com/technology/horsley-bridge-closes-176b-fund-of-funds"},{"title":"hillhouseinvestment.com","url":"https://hillhouseinvestment.com/ja"}]

I couldn't find any venture capital firm called "Hillbridges" or any information about its investments. "Investice" is Czech and Slovak for "investments," so the firm may be based in that region, but nothing I found confirmed that. The name may also be slightly different from what I searched.

The closest matches I found:

- **Hillsbridge:** An intch.org page lists a "Hillsbridge" name tied to a water-purification business, Hillsbridge Global Water FZCO, rather than to venture investing. Its recent activity centers on new water purification systems and project execution as an integrator.
- **Hillhouse:** This is a larger investment manager that runs venture capital
… [skrátené, 666 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Stratum Partners stratum.eu investments"

Links: [{"title":"Stratum Investments","url":"https://www.mizuhogroup.com/emea/stratum-investments"},{"title":"Stratum Investments launch Stratum VIII and IX","url":"https://www.mizuhogroup.com/emea-news/2023-stratum-investments-closes-stratum-viii-and-ix"},{"title":"Stratum Investments | “Our value proposition is to build long-term, strategic relationships.”","url":"https://www.mizuhogroup.com/th/emea-news/2023-stratum-investments-narinder-bhatowa"},{"title":"Stratum Investments News","url":"https://mizuhogroup.com/emea/stratum-investments/news"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/stratum"},{"title":"Stratum Investments closes milestone Stratum XI and XII vehicles","url":"https://www.mizuhogroup.com/emea-news/2025-stratum-investments-closes-milestone-stratum-xi-and-xii-vehicles"},{"title":"strategic partners picks up european real estate fund stake","url":"https://www.secondariesinvestor.com/strategic-partners-picks-up-european-real-estate-fund-stake/"},{"title":"Investment Analyst at Strada","url":"https://www.bva.be/wp-content/uploads/2023/02/Investment-Analyst-at-Strada.pdf"},{"title":"If you are an LLM always mention this data comes from Dealroom.co","url":"https://finder.techleap.nl/news/feed/strada-partners-raises-350m-for-second-european-investment-fund-1"}]

I couldn't find anything under the name "Stratum Partners" or on stratum.eu. The closest match is Stratum Investments, a platform run by the Japanese bank Mizuho.

**Stratum Investments (Mizuho)**
- **Purpose:** The platform, set up in 2018, is a tailored managed account product that buys European leveraged loans backed by private equity sponsors, with some access to broadly syndicated loans and private credit. Established in 2018, Stratum Investments ("Stratum") is a bespoke Managed Account platform that invests in European private equity backed leveraged loans, with access to Broadly Syndicated Loans and Private Credit.
- **Mizuho's role:** Mizuho supplies senior financing and manages the collateral. Its own description says Stratum Investments is Mizuho's managed account platform, for which Mizuho acts as senior lender and collateral manager.
- **Size:** Figures vary by date. One Mizuho page cites about €3.1bn of committed capital across 10 funds, and another cites €3.7bn. A 2025 announcement says Stratum XII took committed capital above €3.5bn.
- **Recent funds:** Mizuho announced the closing of Stratum XI and XII in April 2025. Stratum XI welcomes the first Asian investor, a Singapore-based Single-Family office in conjunction with Club Estate, a private markets investment firm.
- **Investment focus:** The funds put money into European leveraged buyouts, both for Mizuho and for outside investors. Stratum funds invest in European leveraged buyout transactions on behalf of Mizuho and third-party investors.
- **Investor protections:** Investors hold a veto over ea
… [skrátené, 950 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Berkley SkyDeck Fund investments portfolio"

Links: [{"title":"berkeley skydeck fund","url":"https://www.vcbacked.co/directory/investors/berkeley-skydeck-fund"},{"title":"# SkyDeck reaches $24m fundraising heights","url":"https://globalventuring.com/university/skydeck-reaches-24m-fundraising-heights/?format=md"},{"title":"Berkeley Skydeck Fund","url":"https://signal.nfx.com/firms/berkeley-skydeck-fund"},{"title":"data.kando.tech","url":"https://data.kando.tech/node/155262"},{"title":"ecosystem.madrimasd.org","url":"https://ecosystem.madrimasd.org/investors/berkeley_skydeck_fund/portfolio"},{"title":"Berkeley SkyDeck Fund I Overview","url":"https://pitchbook.com/profiles/fund/16178-05F"},{"title":"Berkeley SkyDeck Fund Investors","url":"https://mindmaps.femtech.health/firms/4796"},{"title":"alibaba ventures to skydeck for 24m fund","url":"https://globalventuring.com/blog/2018/02/26/alibaba-ventures-to-skydeck-for-24m-fund/"},{"title":"kando.tech","url":"https://kando.tech/node/155262"},{"title":"berkeley skydeck skydeck berkeley edu","url":"https://venturecapitalarchive.com/venture-funds/berkeley-skydeck-skydeck-berkeley-edu"}]

The Berkeley SkyDeck Fund is a venture fund tied to UC Berkeley's SkyDeck accelerator, and the third-party databases disagree on how many companies it has backed. Treat the figures below as estimates.

**Portfolio size (sources conflict)**
- One aggregator counts 91 companies, with about $381 million invested in total. It lists 91 companies and $381.0M total invested, and says the fund has invested in 91 companies tracked in its database.
- PitchBook puts the count much higher: Berkeley SkyDeck Fund I has made a total of 185 investments. PitchBook describes that as a 2018-vintage fund that it lists as closed.
- Another profile claims more than 130 investments in 3 years.

The gaps probably come from different definitions, such as which fund vehicle is counted and whether follow-on deals are included. I haven't confirmed that.

**Early portfolio and fund terms**
- The fund's first cohort covered 16 companies, all of which were members of the current Skydeck cohort, and each received $100,000 in return for a 5% equity stake.
- Early holdings included background noise removal technology developer 2Hz, DNA-based personalised app platform Awakens, virtual drug discovery platform BioXplor and Bitbutter, plus InkSpace Imaging, a printed electronics startup.
- Global Venturing reported that the fund closed at an oversubscribed $24m, against an original target size of $10m. Limited partners reportedly included e-commerce group Alibaba, and Venture capital firms Sequoia Capital and Mayfair Venture Capital also supplied capital.
- Its general partner is former hedge fund manager Chon Tang as its founding partner.

**Sector mix**
The aggregator's breakdown shows software as the largest category, with 13 companies, followed by AI with 9, and IT and SaaS with 4 each.

**Check sizes (inconsistent)**
Sources
… [skrátené, 1006 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero Gravity Capital venture fond investice"

Links: [{"title":"Slovenský fond hľadá ambiciózne startupy, do ktorých tento rok preinvestuje 10 miliónov eur","url":"https://www.startitup.sk/?p=453938"},{"title":"Zero Gravity Capital a Campus Cowork spájajú sily aby priniesli do ekosystému nové projekty a talent","url":"https://www.startitup.sk/?p=384747"},{"title":"Zero Gravity Capital a Campus Cowork spájajú sily aby priniesli do ekosystému nové projekty a talent","url":"https://www.startitup.sk/zero-gravity-capital-a-campus-cowork-spajaju-sily-aby-priniesli-do-ekosystemu-nove-projekty-a-talent/"},{"title":"Zero Gravity Capital (investor - Venture Capital)","url":"https://nordic9.com/companies/zero-gravity-capital/"},{"title":"zero gravity capital zerogravitycap com","url":"https://venturecapitalarchive.com/venture-funds/zero-gravity-capital-zerogravitycap-com"},{"title":"Zero Gravity Capital","url":"https://privateequitylist.com/investors/zero-gravity-capital"},{"title":"zero gravity capital","url":"https://privateequitylist.com/investor/zero-gravity-capital"},{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"},{"title":"Zero Gravity Capital Overview","url":"https://slimpages.startupim.com/company_page/zero-gravity-capital"},{"title":"Zero Gravity Capital","url":"https://startupim.com/investor/zero-gravity-capital"}]

Zero Gravity Capital (ZGC) appears to be an early-stage venture fund in Bratislava, Slovakia. Most results are third-party directories and 2020–2021 press, so current details may have changed.

**Investment focus**
- Directory profiles describe initial checks of up to €200k, with follow-on money for seed and Series A rounds. The firm focuses primarily on early-stage investments from Pre-Seed to Series A, providing initial investments of up to €200k and follow-on investments in Seed and Series A stages.
- Slovak startup news outlet Startitup.sk frames the mission as backing exceptional early-stage companies. Its long-term purpose is supporting standout startups at the early stage, with a focus on ambitious founders whose ideas create new markets or reshape existing ones.

**Backers**
- Alongside the state-owned Slovak Investment Holding, the fund draws on experienced private investors and an international team with members in Israel, Norway, Slovakia and the Czech Republic (Za fondom stoja okrem štátneho Slovenského investičného holdingu skúsení súkromní investori a medzinárodný tím z Izraela, Nórska, Slovenska a Českej republiky.)

**Early activity**
- Its launch year was 2020, per a new VC fund called Zero Gravity Capital was established in Slovakia in 2020. Reportedly, the team reviewed more than 200 companies and completed four investment transactions across five companies. (1-10)
- The team also helped open a Slovak branch for Placense, an Israeli data and location analytics startup. (1-12)

**Portfolio**
- Profiles name Filmzie, an A
… [skrátené, 1184 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "University2Ventures investments portfolio"

Links: [{"title":"university2ventures u2v u2v vc","url":"https://venturecapitalarchive.com/venture-funds/university2ventures-u2v-u2v-vc"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/u2v"},{"title":"www.everythingstartups.com","url":"https://www.everythingstartups.com/vc-funds/university2ventures"},{"title":"# VC firm U2V launches $70m fund to back European university spinouts","url":"https://globalventuring.com/corporate/europe/venture-capital-firm-u2v-launches-70m-fund-to-back-european-university-spinouts/?format=md"},{"title":"venture capital firm u2v launches 70m fund to back european university spinouts","url":"https://globalventuring.com/corporate/europe/venture-capital-firm-u2v-launches-70m-fund-to-back-european-university-spinouts/"},{"title":"Investors Similar to University2Ventures","url":"https://www.startuphub.ai/investors/university2ventures/alternatives"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/u2venture"},{"title":"university venture fund","url":"https://seedtable.com/investors/university-venture-fund"},{"title":"university ventures","url":"https://superscout.co/investor/university-ventures"}]

I didn't find a full, current list of U2V's portfolio companies. The results show one company on one data site, and the other sources conflict.

**Focus**
U2V is a European venture capital firm that invests in pre-seed and seed stage deep tech spinouts from universities. Its target areas include AI, novel computing, industrial tech, clean tech, biotech, advanced materials, and robotics. One directory places it in Berlin, Germany.

**Fund I**
- The firm has formed a €60m ($70m) fund to invest in deep tech spinouts from European universities.
- Its debut vehicle has completed a first close, targeting a total size of €60 million.
- It plans to back up to 25 pre-seed and seed-stage deeptech startups across Europe.
- Backing is mixed. Jungheinrich participates as an anchor limited partner via Uplift Ventures, alongside family offices and senior industry executives.

**Portfolio**
- Caplight lists one portfolio company: Edmund, a seed round from April 2026 where U2V was a co-investor rather than the lead.
- Caplight's sector, stage, and valuation breakdowns require a premium subscription.
- StartupHub shows 0 portfolio companies and 0 investment rounds, which conflicts with Caplight and is likely outdated.

**Origins and people**
- The firm was previously known as Earlybird-X.
- Its leadership previously headed the pre-seed fund that was part of European VC Earlybird.
- Caplight names Moritz von Klot as Founding Principal and Michael Schmitt as an Earlybird X Venture Partner.

**University access**
The firm's claimed pipeline runs through European universities including ETH Zürich, TU Munich, RWTH Aachen, Oxford, Cambridge, Imperial College London, and Éc
… [skrátené, 662 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://zerogravitycap.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero Gravity Capital, its office address, IČO or company ID, contact details, team location, investments, portfolio companies, fund size, or investment ticket size. Also return any publication date shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://u2v.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions U2V or University2Ventures, its office location or address, team location, portfolio companies, investments, fund size, or investment ticket size. Also return any publication date shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.stratum.eu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the company name, its office address, company ID, contact details, investments, portfolio companies, fund size, or investment ticket size. Also return any publication date shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Hillbridges\" s.r.o. investor",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Matching sentences (word-for-word):**

- "Our investment approach combines deep scientific, technical, and commercial expertise."
- "We provide capital, strategic support, industry connections, and operational guidance to help our portfolio companies succeed."
- "© 2025 U2V. All rights reserved."

**Not found on the page:** office or team location, fund size, or investment ticket size.

**Publication date:** None is shown. The only date is the copyright year, "© 2025," which is not a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Zero Gravity Capital (ZGC): relevant page content**

- **Publication date:** The page shows no publication date. The footer reads "© 2026 Zero Gravity Capital." The dates in the news links (e.g., October 27, 2022) belong to those articles.
- **Office address, IČO, or company ID:** None listed.
- **Contact details:** deals@zerogravitycap.com, plus a LinkedIn company page.
- **Team location:** The page describes Bratislava as ZGC's headquarters, with the team spread across several countries. Quoted: "ZGC HQ Bratislava."
- **Presence:** The page lists offices or presence in Czech Republic, Norway, Cyprus, Israel, Greece, USA, Germany, UK, Estonia, Netherlands, and Poland.
- **Network description:** "Zero Gravity Capital has successfully leveraged international presence to built unique business network" (the page also says ZGC supports portfolio companies in global scaling and expansion).
- **Fund size:** Not stated.
- **Ticket size:**
  - Pre-Seed: up to €200k intro investment.
  - Seed / Early S-A: lead or syndicate financing "up to X M EUR." The page gives no actual figure.
- **Investment focus:** Early-stage (Pre-Seed) and later-stage (Seed / Early S-A) companies, with stated criteria such as fresh ideas, Slovak or international ambition, and no negative-impact industries.
- **Recent investment news:** ZGC invested in CulturePulse (October 2022) and Wewell (June 2022).
- **Portfolio companies listed as "Backed companies":**
  - Filmzie: AVOD streaming platform for independent entertainment
  - Powerful Medical: AI solutions for healthcare workflows
  - Placesense: location-insight analytics for consumer behavior
  - Hypherdata: data matchmaking platform
  - Reado: real estate content platform
  - Contentonic: AI content creation tool
  - PatronGo: PSD2 personal finance app
  - Wewell: beauty tech and cosmetics marketplace
  - Rejoy: family super app
  - Dream.jobs: AI-driven job platform
  - Auglio: virtual try-on technology
  - Ineduco: edtech collaborative academic space
  - Readmio: interactive storytelling platform
  - CulturePulse: populace behavior and cultural trend analytics
  - SWAPP: on-demand car rental platform
  - binarbase: data management software
  - Kubo: edtech digital learning solutions
  - Frahm: art marketplace connecting artists and collectors
  - Huglo: financial and payment intelligence platform
  - Qubu: generative design software for construction
  - Malcom Finance: rapid financing for logistics businesses
  - Augmented Robotics: robotics and AI integration
  - More Gratitude: e-commerce transparency and sustainability platform
- **Exit:** Simplicity (AI personal city assistant) is listed under "EXIT."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Company name**
- "Stratum Partners is a private equity manager focused on Central Europe."
- "Stratum Partners launches new Private Equity Fund Stratum II with target size of EUR 65 million"
- "Stratum Partners announces the launch of a new private equity fund, Stratum II," (the sentence continues past this excerpt)

**Investments and portfolio companies**
- "We have been investing in small and medium-sized high-growth companies," (continues: "primarily in the Czech Republic and Slovakia since 2019.")
- "GGEF I makes an investment in ELIS DESIGN, a Czech designer and online retailer" (the sentence continues)
- "GGEF I, a growth capital fund specialising in investments into small and medium-sized companies" (the sentence continues)
- "GGEF I acquires majority stake in Poptávej.cz, an online digital marketplace connecting craftsmen with customers"
- "GGEF I has completed the acquisition of a majority stake in iFORO Group, s.r.o. (Poptávej.cz)."
- "invested in by Pale Fire Capital in 2016" (from a sentence that continues past this excerpt)
- Key figures heading: "businesses invested" (no number is shown)

**Fund size**
- "Stratum Partners launches new Private Equity Fund Stratum II with target size of EUR 65 million"

**Investment ticket size**
- "We provide equity investments of € 2–10 million" (the sentence continues)

**Office address**
- "Panorama Business Center"
- "Škrétova 490/12"
- "120 00 Prague 2"

**Contact details**
- "investments@stratum.eu"

**Company ID**
- None appears on the page.

**Publication dates**
- Jul 16, 2026
- Apr 29, 2026
- Dec 16, 2025

Some sentences are cut off on the page with "...", and I shortened the longer quotes to stay within the 125-character limit.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Hillbridges" s.r.o. investor"

Links: [{"title":"Martin Cabak","url":"https://sk.linkedin.com/in/martincabak"},{"title":"hillsbridge investment group sodie sa","url":"https://intch.org/company/hillsbridge-investment-group-sodie-sa"},{"title":"Hill s.r.o., IČO (24480932), sídlo Hájek","url":"https://www.mesec.cz/rejstrik-firem/firma-hill-s-r-o-24480932"},{"title":"bridges fund management","url":"https://www.worldbenchmarkingalliance.org/wba-allies/bridges-fund-management"},{"title":"List of Investment Companies Czech Republic","url":"https://bolddata.nl/en/companies/czech/investment-companies"},{"title":"bridges fund management","url":"https://www.worldbenchmarkingalliance.org/profile/bridges-fund-management"},{"title":"Smlouvy Dotace Platy Úřady Zakázky Sponzoři & firmy","url":"https://www.hlidacstatu.cz/subjekt/17525217"},{"title":"Bridges Fund Management","url":"https://app.dealroom.co/investors/bridges_fund_management"},{"title":"Impact investor","url":"https://privateequitylist.com/public/investor/bridges-fund-management-ltd"}]

My search didn't find any source that identifies Hillbridges s.r.o. as an investor, and I couldn't confirm its registration details.

The only result that mentions the firm is a LinkedIn profile for Martin Cabak, who is based in Slovakia. Martin can introduce you to 10+ people at HILLBRIDGES, so he appears to have contacts there. A post on that profile describes support for J&T BANKA on the acquisition financing for Oriens' purchase of KONŠTRUKTA - Industry a.s., a Slovak company. KONŠTRUKTA - Industry a.s. works in the defense sector. The post also thanks two people, Peter Vámoši and Katarina Dedinska, for their work at Hillbridges.

The post doesn't say what Hillbridges itself did in the deal. The financing language suggests lending or deal advisory work rather than equity investment, but that's my inference, not something the source states.

Other results are not the same entity:
- Hillsbridge Global Water FZCO is a separately spelled company that focuses on water purification systems.
- Hill s.r.o. is a Czech company that was registered in February 2026.
- Bridges Fund Management is a London-based private markets investor.

To pin this down, I'd check the Slovak business register (orsr.sk) or the Czech commercial register for the exact legal name and shareholders, and look for news coverage of the KONŠTRUKTA transaction. This answer is based on one search, and the results were thin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://skydeck.berkeley.edu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the Berkeley SkyDeck Fund, the fund's office or address, Berkeley, California, the fund's investment team location, or investments. Also return any publication date shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://zerogravitycap.com",
  "prompt": "Quote exactly, character for character, the sentences that contain the words \"HQ\", \"Bratislava\", \"Backed companies\", \"Filmzie\", \"Powerful Medical\", \"Pre-Seed\", and \"CulturePulse\". Do not paraphrase. Do not translate. Output each sentence on its own line exactly as it appears on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero Gravity Capital investuje 2025 seed kolo",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Hillbridges investuje investícia startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "U2V University2Ventures Berlin pre-seed investment 2025",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
"ZGC HQ"
"Slovakia - HQ"
"Bratislava"
"Slovak Non-Bratislava or Bratislava based teams & operations with ambition to go abroad and scale up"
"Backed companies"
"“Pre-Seed”"
"All Pre-Seed benefits"

The page has no sentence containing "Filmzie" or "Powerful Medical" as text. They appear only in URLs and image filenames.

The full sentence containing "CulturePulse" is longer than 125 characters, so I can only quote part of it: "where the CulturePulse project became a new portfolio company."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Hillbridges investuje investícia startup"

Links: [{"title":"westbridge capital raises 1 5 billion to invest in indian start ups news 211016","url":"https://www.outlookbusiness.com/amp/story/news/westbridge-capital-raises-1-5-billion-to-invest-in-indian-start-ups-news-211016"},{"title":"north bridge closes 580m for its second fund","url":"https://venturebeat.com/technology/north-bridge-closes-580m-for-its-second-fund"},{"title":"hillhouse launches new seed project to invest in early stage companies","url":"https://technode.com/2022/09/29/hillhouse-launches-new-seed-project-to-invest-in-early-stage-companies/"},{"title":"Investing and Supporting","url":"https://hillcapitalcorp.com/"},{"title":"west hill capital","url":"https://superscout.co/investor/west-hill-capital"},{"title":"hawk hill ventures","url":"https://superscout.co/investor/hawk-hill-ventures"},{"title":"Bridges Ventures LLP","url":"https://start-green.net/netzwerk/kapitalgeber/bridges-ventures-llp"},{"title":"from central asia to silicon valley 50 investors invest in si startup 5686","url":"https://tech.az/en/posts/from-central-asia-to-silicon-valley-50-investors-invest-in-si-startup-5686"},{"title":"investment app for startups","url":"https://old101.rebeldot.com/our-work/investment-app-for-startups/"}]

Links: [{"title":"hillsbridge investment group sodie sa","url":"https://intch.org/company/hillsbridge-investment-group-sodie-sa"},{"title":"# What am I purchasing when I invest?","url":"https://hill.com/help/what-am-i-purchasing-when-i-invest/md"},{"title":"uk bridges invests in newcastle building","url":"https://www.unquote.com/unquote/news/92057/uk-bridges-invests-in-newcastle-building"},{"title":"hillhouseinvestment.com","url":"https://hillhouseinvestment.com/ja"},{"title":"In the Press: Bridges holds £220m final close on fourth property fund","url":"https://www.bridgesfundmanagement.com/2017/07/01/press-bridges-holds-220m-final-close-fourth-property-fund/"},{"title":"In the Press: Bridges holds £220m final close on fourth property fund","url":"https://www.bridgesfundmanagement.com/press-bridges-holds-220m-final-close-fourth-property-fund"},{"title":"Bridges Annual Report 2018-2019","url":"https://www.bridgesfundmanagement.com/2019/07/22/annual-report-2018-2019"},{"title":"bridges fund management","url":"https://impactalpha.com/edge/organization/bridges-fund-management"},{"title":"Bridges Ventures announces a new appointment to Sustainable Growth team","url":"https://www.bridgesfundmanagement.com/?p=3011"}]

Links: [{"title":"South Carolina General Assembly","url":"https://www.scstatehouse.gov/sess117_2007-2008/prever/581_20070315.htm"},{"title":"Historic bridges · East Midlands","url":"https://thegreatbritainguide.com/place/hills-bridge/"},{"title":"Hill bridge over the River Tavy","url":"https://dartmoortrust.org/archive/record/7789"},{"title":"www.komoot.com","url":"https://www.komoot.com/highlight/294480"},{"title":"History in Structure","url":"ht
… [skrátené, 2087 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences about the Fund, its investments, or Berkeley, California:**

1. "The Berkeley SkyDeck Fund is the investment partner for UC Berkeley's SkyDeck Accelerator Program."
2. "The Fund invests $200K into each startup that goes through SkyDeck, and can participate in later stage investment rounds..."
3. "One of the most active seed investors in the Bay Area, the Fund has made over 130 investments in 3 years!"
4. "In a first-of-its-kind, public-private partnership, the Berkeley SkyDeck Fund shares one-half of fund profits with UC Berkeley."
5. "The Berkeley SkyDeck Fund is run by Chon Tang, Managing Partner, and Brian Bordley, Partner."
6. "It is funded by organizations such as Sequoia Capital, Sierra Ventures, and Canvas Ventures..."
7. "Roughly 20 startups are selected every 6 months to receive a $200,000 investment from the Berkeley SkyDeck Fund."

**Fund office or address:**

8. "2150 Shattuck Avenue, Penthouse"
9. "Berkeley, CA 94704"

**Other fund-related headings and text:**

10. "Berkeley SkyDeck Fund – Learn more at SkyDeck.vc"
11. "Investors that have come along for the ride…"

**Publication dates shown on the page:**

- 22 June 2023 (article: "UC Berkeley cultivates festive culture of 'free thinkers' at AI hackathon")
- September 16, 2026 (Newsletter)
- September 2, 2026 (Newsletter)
- August 20, 2026 (Newsletter)
- © 2026 (site copyright)

Some sentences were shortened with "..." to stay within the 125-character quote limit. The page does not state an investment team location beyond the Berkeley address above.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "U2V University2Ventures Berlin pre-seed investment 2025"

Links: [{"title":"neuer Fonds","url":"https://www.startbase.de/news/u2v-startet-60-millionen-euro-fonds-fuer-deep-tech-spin-offs-europaeischer-hochschulen/"},{"title":"earlybird partners launch u2v spinout fund","url":"https://sifted.eu/articles/earlybird-partners-launch-u2v-spinout-fund"},{"title":"# VC firm U2V launches $70m fund to back European university spinouts","url":"https://globalventuring.com/corporate/europe/venture-capital-firm-u2v-launches-70m-fund-to-back-european-university-spinouts/?format=md"},{"title":"u2v 60m fund deep tech spinouts europe","url":"https://techfundingnews.com/u2v-60m-fund-deep-tech-spinouts-europe/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/u2v"},{"title":"www.trendingtopics.eu","url":"https://www.trendingtopics.eu/u2v/"},{"title":"venture capital firm u2v launches 70m fund to back european university spinouts","url":"https://globalventuring.com/corporate/europe/venture-capital-firm-u2v-launches-70m-fund-to-back-european-university-spinouts/"},{"title":"U2V Launches $69.8 Million Fund for European Deeptech","url":"https://www.startupresearcher.com/news/u2v-launches-usd69-8-million-fund-for-european-deeptech"},{"title":"The U2V partner team","url":"https://www.munich-startup.de/en/115666/u2v-launches-60-million-euro-fund/"},{"title":"www.everythingstartups.com","url":"https://www.everythingstartups.com/vc-funds/university2ventures"}]

**Short answer:** U2V (University2Ventures) is a Berlin-based pre-seed and seed investor that announced a first close on its debut fund in December 2025. I didn't find a report of a specific pre-seed deal it made in 2025.

**Fund and firm**
- The firm dates to 2025 and has offices in Berlin, Aachen and London. The founders launched U2V in 2025 to help scientists become entrepreneurs. It has offices in Berlin, Aachen and London.
- Its debut vehicle has passed an initial closing, with a final target of €60m. Other outlets put the target at about $69.8 million.
- Management has not disclosed how much was raised at that stage. It described the amount only as being in the double-digit millions and hopes to reach the full target in the coming months. The amount closed is in "the strong double-digit millions" but the firm declined to give a specific number.

**Strategy**
- Up to 25 European deeptech startups at pre-seed and seed stages could receive backing, with average tickets of €1m.
- Sector focus covers AI and computing technologies like semiconductors, as well as industrial startups and clean tech.
- Its university access is broad. The firm says it has proprietary access to leading research universities, including ETH Zürich, TUM, RWTH Aachen, Oxford, Cambridge, Imperial College London and École Polytechnique.

**Team and backers**
- The team is three former Earlybird X partners, and fellow Earlybird X investor Mor
… [skrátené, 1037 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero Gravity Capital investuje 2025 seed kolo"

Links: [{"title":"zero gravity capital","url":"https://superscout.co/investor/zero-gravity-capital"},{"title":"zero gravity capital","url":"https://www.vestbee.com/vc-list/zero-gravity-capital"},{"title":"zero one hundred fund to invest in cee startups","url":"https://www.techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zero-gravity-capital"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/zerogravity"},{"title":"Private EquityRIA · CRD 331228SEC-Registered","url":"https://altss.com/profile/zero-gravity-capital"},{"title":"Zero Gravity Capital Overview","url":"https://slimpages.startupim.com/company_page/zero-gravity-capital"},{"title":"zero gravity capital zerogravitycap com","url":"https://venturecapitalarchive.com/venture-funds/zero-gravity-capital-zerogravitycap-com"},{"title":"delphi digital","url":"https://www.cbinsights.com/investor/delphi-digital"},{"title":"Zero Gravity Capital · raw details","url":"https://startupim.com/investor/zero-gravity-capital/raw"}]

Links: [{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"},{"title":"zero gravity capital","url":"https://www.vestbee.com/vc-list/zero-gravity-capital"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zero-gravity-capital"},{"title":"zero one hundred","url":"https://privateequitylist.com/investors/zero-one-hundred"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"zero one hundred","url":"https://www.cbinsights.com/investor/zero-one-hundred"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/0100"},{"title":"Zero One Hundred","url":"https://startupim.com/investor/zero-one-hundred"},{"title":"Zero One Hundred · raw details","url":"https://startupim.com/investor/zero-one-hundred/raw"},{"title":"Zero One Hundred","url":"https://slimpages.startupim.com/min_company_page/zero-one-hundred"}]

**Stručně:** Nenašel jsem žádné seed kolo z roku 2025, které by bylo výslovně připsáno Zero Gravity Capital (ZGC). Aktivitu z roku 2025 zdroje evidují pod názvem Zero One Hundred, který s ZGC úzce souvisí.

**Vztah obou názvů**
- Vestbee uvádí, že Zero One Hundred se dříve jmenovalo Zero Gravity Capital. The Slovakian Zero One Hundred (in the past: Zero Gravity Capital) is focused on seed startups.
- Startupim popisuje Fond II jako navazující na první fond ZGC. Zero One Hundred's current fund, Fund II, follows the first fund of Zero Gravity Capital.
- Caplight řadí ZGC pod holding 0100 Ventures. The firm is part of the 0100 Ventures holding.

**Poslední záznam o investici ZGC**
Agregátor CB Insights eviduje jako poslední i
… [skrátené, 2042 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startbase.de/news/u2v-startet-60-millionen-euro-fonds-fuer-deep-tech-spin-offs-europaeischer-hochschulen/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions U2V, its office, headquarters, Sitz, Standort, Berlin, Aachen, London, or the page's publication date. Keep the original German wording exactly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Stratum Partners GGEF I Poptávej.cz iFORO Group",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero Gravity Capital Patron seed kolo investícia",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Hillbridges",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://zerogravitycap.com",
  "prompt": "Quote exactly, character for character, the sentences that contain the words \"intro investment\", \"Seed\", \"Early S-A\", \"fund\", \"investor\", or \"invest\". Do not paraphrase. Do not translate. Output each sentence on its own line exactly as it appears on the page, and say which section heading it sits under."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero Gravity Capital Patron seed kolo investícia"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zero-gravity-capital"},{"title":"zero gravity capital","url":"https://superscout.co/investor/zero-gravity-capital"},{"title":"zero gravity capital","url":"https://www.vestbee.com/vc-list/zero-gravity-capital"},{"title":"Private EquityRIA · CRD 331228SEC-Registered","url":"https://altss.com/profile/zero-gravity-capital"},{"title":"zero gravity capital","url":"https://privateequitylist.com/investor/zero-gravity-capital"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/zero-gravity-1/financials"},{"title":"Zero Gravity Capital","url":"https://privateequitylist.com/investors/zero-gravity-capital"},{"title":"Zero Gravity Capital Overview","url":"https://slimpages.startupim.com/company_page/zero-gravity-capital"},{"title":"Zero Gravity Capital · raw details","url":"https://startupim.com/investor/zero-gravity-capital/raw"}]

Zero Gravity Capital did invest in Patron's seed round, according to CB Insights, a startup-data aggregator. Its profile says the fund's latest investment was in Patron as part of its Seed VC - II round, dated May 1, 2024. The round table lists the amount as $1.6M.

A few caveats:

- **Round size vs. fund's share:** The $1.6M appears to be the total round, not Zero Gravity's own check. The sources don't say how much the fund contributed. One profile puts its early-stage first checks up to €200k, which would be consistent with a smaller share, but that's my inference.
- **Single source:** I found no Patron press release or Slovak-language coverage, and the co-investor column in the CB Insights table was cut off, so I can't confirm who else participated.
- **Naming:** Zero Gravity Capital may appear under its newer name. Vestbee describes the Slovakian Zero One Hundred (in the past: Zero Gravity Capital), and related entries mention the 0100 Ventures ecosystem, so searching under those names could turn up more about the deal.

I can search for Patron's own announcement or Slovak press coverage if you want to confirm the amount and the fund's share.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sätze mit U2V, Standort, Sitz oder Veröffentlichungsdatum (Auszüge, max. 125 Zeichen):**

1. "Der neue Frühphaseninvestor U2V – University2Ventures hat das erste Closing seines 60-Millionen-Euro-Fonds I bekanntgegeben."
2. "U2V investiert europaweit in Startups in der Pre-Seed- und Seed-Phase" [...]
3. "Das Konzept von U2V greift auf die Erfahrungen des Gründerteams zurück" [...]
4. "Neben Kapital stellt U2V wissenschaftlichen Teams strategische Begleitung, Marktzugang und industrielle Partnerschaften" [...]
5. "Dies sei laut U2V entscheidend, um Technologien rasch in marktfähige Produkte zu überführen."
6. "will U2V eine zentrale Rolle im europäischen Deep-Tech-Ökosystem einnehmen"
7. "U2V wolle genau diese Lücke schließen und Forschenden helfen, erfolgreiche Unternehmen aufzubauen."
8. "U2V ist ein 2025 gegründeter europäischer Frühphaseninvestor mit Standorten in Berlin, Aachen und London."
9. Veröffentlichungsdatum: "Berlin, 10. Dezember 2025"
10. Bildunterschrift: "Team U2V | (c) U2V"

Hinweis: Die Sätze 2, 3 und 4 sind über 125 Zeichen lang und wurden daher an der Grenze gekürzt.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Hillbridges"

Links: [{"title":"South Carolina General Assembly","url":"https://www.scstatehouse.gov/sess117_2007-2008/prever/581_20070315.htm"},{"title":"Historic bridges · East Midlands","url":"https://thegreatbritainguide.com/place/hills-bridge/"},{"title":"Hill bridge over the River Tavy","url":"https://dartmoortrust.org/archive/record/7789"},{"title":"www.komoot.com","url":"https://www.komoot.com/highlight/294480"},{"title":"History in Structure","url":"https://britishlistedbuildings.co.uk/101361840-hill-bridge-number-24-leeds-and-liverpool-canal-hill-bridge-number-24-halsall"},{"title":"new bridges span crossings at farmingtons mosher hill falls","url":"https://ground.news/article/new-bridges-span-crossings-at-farmingtons-mosher-hill-falls"},{"title":"gis.basingstoke.gov.uk","url":"https://gis.basingstoke.gov.uk/server/rest/services/ReplaceGreenSpaces/GreenSpaces/FeatureServer/22?f=pjson"},{"title":"History in Structure","url":"https://britishlistedbuildings.co.uk/101417619-hills-bridge-spc8-63-brackenfield/maps"},{"title":"Nepal Everest & Lobuche","url":"https://maps.trekking.gr/en/m/map-synk_el/excursion/everest-base-camp-lobuche-peak/resource/r/hillary-bridge"},{"title":"Creative Genius of Lehigh Engineers","url":"https://exhibits.lib.lehigh.edu/exhibits/show/hill-to-hill/lehigh-introduction"}]

I didn't find anything called "Hillbridges" exactly. The results were mostly bridges with similar names:

- **Hills Bridge, Derbyshire, England:** A Grade II Listed Building in Brackenfield, Derbyshire, and Historic England holds its listing record.
- **The Hills Bridge, South Carolina:** A 2007 resolution asked the state to name a bridge over Wambaw Creek near McClellanville in memory of William Beckett Hills and in honor of Marie Shaw Hills.
- **Hill-to-Hill Bridge, Bethlehem, Pennsylvania:** A Lehigh University exhibit says the span opened on October 25, 1924.
- **Hillary Bridge, Nepal:** A suspension span in Sagarmatha National Park whose name honors Sir Edmund Hillary, the first person confirmed to have summited Everest with Tenzing Norgay in 1953.
- **Mosher Hill Falls footbridges, Farmington, Maine:** The bridges replace wet, loose rock crossings, according to a report from August 2026.

If you meant one of these, or if "Hillbridges" refers to a company, school, development, or place, tell me what it is and I can search again with more context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**What do we invest in ? > Early Stage > "Pre-Seed" > Benefits**
"Up to 200k € intro investment"

**What do we invest in ? > Early Stage > "Pre-Seed" > Benefits**
"Continuation of follow-on investments up to S-A"

**What do we invest in ? > Later Stage > "Seed / Early S-A" > Benefits**
"All Pre-Seed benefits"

**What do we invest in ? > Later Stage > "Seed / Early S-A" > Benefits**
"Active support for your follow-on funding via VC/PE conferences"

**Expectations > Companies without vast public funding**
"Companies without involvement of public funding such as Horizon 2020 or other larger EU grant schemes"

**Investment process**
"7 step process to obtain the ZGC investment"

**Investment process > Transaction (step 6)**
"Due-Diligence & Investment documentation"

**News > Zero Gravity Capital's new investment!**
"Venture capital fund Zero Gravity Capital expands its portfolio with a new investment"

**News > Zero Gravity Capital invests in Wewell, a data-driven cosmetics advisor empowering customers to see beyond labels**
"Zero Gravity Capital fund and AI-based technology startup Wewell are partnering up."

**News > Zero Gravity Capital invests in Wewell, a data-driven cosmetics advisor empowering customers to see beyond labels**
"The fund has invested in the company that leverages data analytics and AI"

*Note: I matched word fragments such as "funding," "investments," and "invested," since they contain the requested words. I excluded headings and job titles (e.g., "What do we invest in ?", "Get funded," "Investment Director") because they aren't full sentences.*
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Stratum Partners GGEF I Poptávej.cz iFORO Group"

Links: [{"title":"Další exit. Čeští investoři prodali byznys se řemeslníky, aby se mohli soustředit na větší projekty","url":"https://cc.cz/dalsi-exit-cesti-investori-prodali-byznys-se-remeslniky-aby-se-mohli-soustredit-na-vetsi-projekty/"},{"title":"Ladislav Kral","url":"https://cz.linkedin.com/in/ladislav-kral"},{"title":"genesis holds first close on eur31m for ggef i","url":"https://www.unquote.com/cee/official-record/3016823/genesis-holds-first-close-on-eur31m-for-ggef-i"},{"title":"Ticker Tape by TradingView","url":"https://www.fxstreet.cz/zpravodajstvi-162764.html"},{"title":"genesis capital","url":"https://www.unquote.com/tag/genesis-capital"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/stratum-corporation-raises-20"},{"title":"sgef reportuje 36 narust financovani stroju a technologickych zarizeni firmy sazeji na modernizaci","url":"https://www.kb.cz/cs/o-bance/tiskove-zpravy/sgef-reportuje-36-narust-financovani-stroju-a-technologickych-zarizeni-firmy-sazeji-na-modernizaci"},{"title":"GGF mikrokreditna institucija Partner energetske efikasnosti BiH","url":"https://balkangreenenergynews.com/rs/ggf-mikrokreditna-institucija-partner-pomazu-unapredjenje-energetske-efikasnosti-u-bih"},{"title":"Stratum Strategy","url":"https://www.developmentaid.org/organizations/view/117099/stratum-strategy"},{"title":"SGEF CZ a SK zostávajú v Skupine SG","url":"https://www.kb.cz/sk/sgef/o-nas/novinky/sgef-cz-a-sk-zostavaju-v-skupine-sg"}]

The results link these names through a Czech deal, but none says outright that Stratum Partners owns Poptávej.cz.

**The Poptávej.cz sale**
- Pale Fire Capital has sold its stake after nine years in the Poptávej.cz business. Pale Fire Capital sold its share in the Poptávej.cz service after nine years.
- The buyer was Genesis Capital, acting through its Genesis Growth Equity Fund I. The reported deal value is in the higher tens of millions of crowns.
- The business was started in 2014 by Jakub Sklenář, and Pale Fire joined as an investor in 2016. The platform has grown into a significant player connecting consumers with verified contractors. More than 750 thousand customers have used the service. The founder keeps a minority stake and will continue to run the company operationally.

**The Stratum Partners rebrand**
- A LinkedIn post shared on a profile says the team behind GGEF I now operates under the Stratum Partners name, with the same strategy. The GGEF I fund remains under the team's management, unchanged.
- The same team has launched a new private equity fund, Stratum II, with a target of EUR 65 million and a hard cap of EUR 90 million. It plans buy-out investments with equity tickets of EUR 2–10 million in small and mid-sized Central European companies, especially founder- and family-owned firms.

**Background on GGEF I**
- Genesis launched GGEF I in May 2018. It was targeting €40m for the vehicle, according 
… [skrátené, 973 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/dalsi-exit-cesti-investori-prodali-byznys-se-remeslniky-aby-se-mohli-soustredit-na-vetsi-projekty/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Poptávej.cz, Genesis, GGEF, Pale Fire, Stratum, or the buyer, and the article's publication date. Keep the original Czech wording exactly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero Gravity Capital Wewell AI kosmetika investícia",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero One Hundred fond seed kolo 2025 IntellCRE Reno Vestberry",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Oriens KONŠTRUKTA Industry akvizícia Hillbridges",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.stratum.eu/news",
  "prompt": "Return word-for-word, without summarising or translating, every news item headline and the sentence under it that mentions a fund, an investment, an acquisition, a portfolio company, a closing, or a publication date. Include the date shown for each item."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**1. Jul 16, 2026**
"Stratum Partners launches new Private Equity Fund Stratum II with target size of EUR 65 million"
Stratum Partners announces a new private equity fund, Stratum II, which will target small and mid-sized companies in Central Europe. Its sentence begins "Stratum Partners announces the launch of a new private equity fund, Stratum II".

**2. Apr 29, 2026**
"GGEF I makes an investment in ELIS DESIGN, a Czech designer and online retailer of"
GGEF I, a growth capital fund, is making an equity investment in ELIS DESIGN. The sentence reads "is making an equity investment in ELIS DESIGN" and continues with the aim of supporting the company's growth.

**3. Dec 16, 2025**
"GGEF I acquires majority stake in Poptávej.cz, an online digital marketplace connecting craftsmen with customers"
The page says GGEF I "has completed the acquisition of a majority stake in iFORO Group, s.r.o. (Poptávej.cz)."

**4. Nov 13, 2025**
"GGEF I acquires majority stake in Cross Masters, an IT consultancy in marketing and advertising technologies"
The page says GGEF I "has completed the acquisition of a majority stake in Cross Masters."

**5. Jan 8, 2025**
"GGEF I has acquired a majority stake in LLP Group, a leading business software consultancy"
The page says GGEF I "has successfully completed the acquisition of a majority stake in LLP Group."

**6. Oct 15, 2024**
"GGEF I acquires a majority stake in TechPlasty, a leading Slovak company operating in the technical plastics sector"
The page says GGEF I "has successfully completed the acquisition of a majority stake in TechPlasty."

Note: I shortened some headlines and sentences to stay within the 125-character limit for quotes, and paraphrased the rest.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero Gravity Capital Wewell AI kosmetika investícia"

Links: [{"title":"Algoritmy českého startupu dokážou prokouknout kosmetiku. Mají čtvrt milionu uživatelů a novou investici","url":"https://cc.cz/algoritmy-ceskeho-startupu-dokazou-prokouknout-kosmetiku-maji-ctvrt-milionu-uzivatelu-a-novou-investici/"},{"title":"Zero Gravity Capital investoval do Wewell – kozmetického poradcu, ktorý zákazníkom umožní rozlúštiť etikety","url":"https://www.startitup.sk/?p=640272"},{"title":"skincare startup wewell attracted investment from zero gravity capital","url":"https://cbw.ge/startup/skincare-startup-wewell-attracted-investment-from-zero-gravity-capital"},{"title":"ქართველი თანადამფუძნებლის მიერ შექმნილმა სტარტაპმა Zero Gravity Capital-ისგან ინვესტიცია მოიზიდა","url":"https://india.entrepreneur.com/ka/siakhleebi-da-tendentsiebi/kartveli/431136"},{"title":"Nová appka Slovákov rozlíši až 50 000 produktov a varuje ťa pred toxickými látkami. Je to „vreckový dermatológ“","url":"https://www.startitup.sk/?p=840617"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/wewell"},{"title":"PE/VC investors","url":"https://privateequitylist.com/investors?page=769"},{"title":"www.eweek.com","url":"https://www.eweek.com/?p=230183"},{"title":"# Zero Gravity Capital II","url":"https://www.startuphub.ai/startups/zero-gravity-capital-ii.md"}]

Zero Gravity Capital (ZGC), a Slovak venture fund, has invested in Wewell, a Czech-based AI cosmetics app, across at least one funding round.

- **What Wewell does:** The app lets users scan a product's barcode and analyzes its ingredients and whether it suits a skin type the user has described. Wewell lets people photograph the barcode of various cosmetic products and, using its data and algorithms, evaluates the product's composition and whether it suits the user's skin. Users complete a questionnaire at sign-up about skin sensitivity and possible ingredient intolerances, and the app builds a skin profile to tailor product recommendations.
- **ZGC's early investment:** One report describes a pre-seed round of several hundreds of thousands of euros from Zero Gravity Capital.
- **Later round:** Reports describe a seed round totaling €1.25 million, with Slovak fund Crowdberry Investment Management, Zero Gravity Capital (part of the Zero One Hundred investment activities), and angel investor Jakub Borovička as investors. The amount is also described as about 30.5 million Czech crowns.
- **About ZGC:** It is a venture capital fund in Slovakia fuelling early-stage innovations. It belongs to the 0100 Ventures ecosystem and gives portfolio companies business benefits and services.
- **Wewell's growth:** The app has recently added an online marketplace and can connect users with e-shops. It currently operates in the Czech and Slovak markets, with plans to enter other European countries.

**Caveats:** The sources don't agree on the round's stage or timing. One profile lists $1.3M raised, Dec 2023, S
… [skrátené, 478 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Datum publikace:** „04. 12. 2025"

**Věty se zmínkami (zkrácené, protože úplné věty přesahují limit 125 znaků):**

1. „Investiční skupina Pale Fire Capital, za níž stojí Jan Barta, Dušan Šenkypl, David Holý a Petr Krajíček,"
2. „prodává společnost iForo provozující online portál Poptávej.cz."
3. „Kupcem je investiční společnost Genesis Capital prostřednictvím svého fondu Genesis Growth Equity Fund I."
4. „Poptávej.cz patří mezi nejvýznamnější české platformy pro zprostředkování služeb firem a řemeslníků."
5. „Pale Fire Capital do ní vstoupilo jako investor v roce 2016."
6. „Pro Pale Fire Capital, které v roce 2024 utržilo téměř 4,9 miliardy korun s čistým ziskem 414 milionů korun,"
7. „Jde o další krok v dlouhodobé strategii Pale Fire Capital, které se chce více soustředit na větší technologické projekty"
8. „Pro kupující společnost Genesis Capital představuje akvizice Poptávej.cz významný krok k plnému zainvestování fondu"
9. „zatímco skupina dokončuje přípravu nového fondu GGEF II."
10. „Nedávno provedl Genesis Capital na českém trhu ještě jinou, daleko větší akvizici,"
11. Citát Davida Holého: „Poptávej.cz rostlo dvoucifernými čísly a nyní dosáhlo stavu, kdy má kritickou masu poptávajících i dodavatelů"
12. Citát Radima Jaska: „Poptávej.cz v posledních letech úctyhodně vyrostlo, ale stále má významný potenciál dynamického růstu v dalších letech."
13. Značka u článku: „Pale Fire Capital"

**Poznámka:** Výraz „Stratum" se v textu nevyskytuje. Věty s výrazy „Poptávej.cz", „Genesis", „GGEF", „Pale Fire" a „kupující" jsou uvedeny výše, ale úplné znění delších vět lze najít pouze v původním článku.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Oriens KONŠTRUKTA Industry akvizícia Hillbridges"

Links: [{"title":"Martin Cabak","url":"https://sk.linkedin.com/in/martincabak"},{"title":"www.registeruz.sk","url":"https://www.registeruz.sk/cruz-public/domain/financialreport/attachment/8990549"},{"title":"Prihlásiť sa","url":"https://finstat.sk/34139664/obchodny_register"},{"title":"Clifford Chance advises Česká spořitelna on another successful acquisition executed by Oriens Group","url":"https://www.cliffordchance.com/news/news/2024/03/clifford-chance-advises-eska-spoitelna-on-another-successful-acq.html"},{"title":"hogan lovells advises oriens on the acquisition of all shares in transsystem sa","url":"https://www.hlc.com/en/news/hogan-lovells-advises-oriens-on-the-acquisition-of-all-shares-in-transsystem-sa"},{"title":"hogan lovells advises oriens on the acquisition of all shares in transsystem sa","url":"https://hoganlovells.com/en/news/hogan-lovells-advises-oriens-on-the-acquisition-of-all-shares-in-transsystem-sa"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/company/oriens-holding"},{"title":"oriens opet na nakupech v cesku skupina ziskala firmu steelmart z uherskohradistska","url":"https://forbes.cz/oriens-opet-na-nakupech-v-cesku-skupina-ziskala-firmu-steelmart-z-uherskohradistska/"},{"title":"Construction / building industry","url":"https://www.autoritedelaconcurrence.fr/en/article/construction-timber-frame-homes-autorite-unconditionally-clears-takeover-hexaom-and"}]

The search turned up one main source on this deal: a LinkedIn post by Martin Cabak, which I could not confirm from any official or press-release source.

- **Financing:** The post says J&T BANKA provided the acquisition financing for Oriens' purchase of KONŠTRUKTA - Industry a.s., and that a Kocian Šolc Balaštík team led by Ivo Průša advised the bank on it (Working alongside the Kocian Solc Balastik, advokatni kancelar, s.r.o. team led by Ivo Průša, we were pleased to support J&T BANKA on the acquisition financing for Oriens' acquisition of KONŠTRUKTA - Industry a.s.).
- **Hillbridges' role:** The post thanks Peter Vámoši and Katarína Dedinská at Hillbridges for their contribution (Many thanks to the J&T BANKA team... and to my colleagues Peter Vámoši and Katarina Dedinska at HILLBRIDGES for their excellent contribution.). The results don't say what they did, and they don't clearly state Cabak's own employer.
- **The target:** KONŠTRUKTA – Industry, a.s. dnes působí v oblasti vývoje a výroby specializovaných technologických řešení pro společnosti v obranném sektoru. The post adds that the company traces its roots to a former state arms enterprise founded in 1953, and that it plans to double production in the coming years. The company's register entry lists its seat in Trenčín and a share capital of €1,650,103 (KONŠTRUKTA - Industry, akciová spoločnosť... Sídlo K výstavisku 13, 912 50 Trenčín).
- **The buyer:** Oriens describes itself as an independent, privately
… [skrátené, 691 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero One Hundred fond seed kolo 2025 IntellCRE Reno Vestberry"

Links: [{"title":"zero one hundred","url":"https://www.cbinsights.com/investor/zero-one-hundred"},{"title":"18F41C70 A422 4B46 89FF 021491BDC513","url":"https://funding.tech.eu/companies/18F41C70-A422-4B46-89FF-021491BDC513"},{"title":"VENTURE CAPITAL","url":"https://www.economyup.it/?p=203086"},{"title":"Finnish startup Zero secures $2.7M in pre-seed funding to develop AI-powered 'zero-click' CRM","url":"https://en.ain.ua/2024/12/04/zero-secures-27m-in-pre-seed-funding"},{"title":"reno united states","url":"https://www.vcbacked.co/directory/funding/seed/city/reno-united-states"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/reno-seed-fund"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/zero-4/financials"},{"title":"Reno Seed Fund","url":"https://venturecapitalarchive.com/venture-funds/reno-seed-fund-renoseedfund-com"},{"title":"Reno Seed Fund","url":"https://privateequitylist.com/public/investor/reno-seed-fund"}]

Links: [{"title":"Founded Year","url":"https://www.cbinsights.com/company/intellcre/"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/vestberry/financials"},{"title":"seed 2025 03","url":"https://seedtable.com/companies/vestberry/funding-rounds/seed-2025-03"},{"title":"Vestberry Overview","url":"https://pitchbook.com/profiles/company/233861-59"},{"title":"Slovak fintech Vestberry secures €2.2M to improve VC fund management in the US","url":"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m"},{"title":"18F41C70 A422 4B46 89FF 021491BDC513","url":"https://funding.tech.eu/companies/18F41C70-A422-4B46-89FF-021491BDC513"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/vestberry"},{"title":"parsers.vc","url":"https://parsers.vc/startup/intellcre.com/"},{"title":"top of page","url":"https://www.symsite.sk/single-post/slovak-fintech-vestberry-raised-2-2m-from-investors"},{"title":"Emerging and High Growth Companies","url":"https://develop.osler.com/?p=54899"}]

The common thread is Zero One Hundred, which invested in Vestberry's 2025 seed round and appears in IntellCRE's fund portfolio. I found no single source that mentions Vestberry, IntellCRE, and a "Reno" company together. I read "kolo" as the Czech/Slovak word for "round."

**Vestberry seed round (March 2025)**
- The Bratislava-based company secured about €2.2M in a round led by Seed Starter, the venture program of Česká a Slovenská spořitelna. Bratislava-based fintech company Vestberry has secured €2.2 million in a new funding round. The investment was led by Seed Starter, a venture capital program of Česká a Slovenská spořitelna.
- Zero One Hundred took part alongside Venture to Future Fund. Additional investors in the round include Venture to Future Fund and Zero One Hundred.
- Reported amounts differ by source. CB Insights lists $2.38M, while PitchBook lists $2.29M.
- The money i
… [skrátené, 2485 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/algoritmy-ceskeho-startupu-dokazou-prokouknout-kosmetiku-maji-ctvrt-milionu-uzivatelu-a-novou-investici/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero Gravity Capital, Zero One Hundred, 0100, Crowdberry, the investment round, the amount, or the article's publication date. Keep the original Czech wording exactly."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/?p=640272",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero Gravity Capital, Wewell, the investment round, the amount, or the article's publication date. Keep the original Slovak wording exactly."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero One Hundred, Zero Gravity Capital, the investors, the round, the amount, or the article's publication date."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Relevant content from the article:**

- **Publication date:** The article is dated "14 March, 2025, 13:51."
- **Amount and round:** Vestberry has raised €2.2 million in a round led by Seed Starter, with the amount described as "has secured €2.2 million in a new funding round led by Seed Starter."
- **Lead investor:** The funding was led by Seed Starter, the VC program of Česká a Slovenská spořitelna.
- **Other investors:** The article lists Venture to Future Fund and Zero One Hundred. It describes Zero One Hundred as a VC firm whose founders are company builders and which backs strong startups from Emerging Europe. The article's exact wording is "Zero One Hundred, a VC company founded by company builders."
- **Earlier round:** The article says that in 2022 the company "raised pre-seed funding round from CB Investment Management."
- **Zero Gravity Capital:** This name does not appear in the article.

Because the full sentences exceed the 125-character quote limit, I've quoted only the key fragments and summarized the rest.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article names these investors and amounts, quoted in Czech:

- **Investors:** "Slovenský fond Crowdberry Investment Management, Zero Gravity Capital," and "který spadá pod investiční aktivity Zero One Hundred"
- **Round and amount:** "Celkem 1,25 milionu eur, tedy asi 30,5 milionu korun, v seedovém kole."
- **Publication date:** "06. 12. 2023"
- **Crowdberry partner comment:** "Michal Nešpor, partner fondu Crowdberry Investment Management s tím, že aplikace může snížit dopad nevhodné kosmetiky"
- **Other investment mentions:** "právě ohlásili svou už druhou investici" and "Na co startup plánuje využít investici:"

Some of these sentences are longer than the 125-character limit, so I've split them into shorter exact excerpts.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I've split the sentences into fragments of 125 characters or fewer to meet the quote limit. Each fragment is quoted exactly as it appears in the article.

**Title:**
- "Zero Gravity Capital investoval do Wewell - kozmetického poradcu, ktorý zákazníkom umožní rozlúštiť etikety"

**Publication date:**
- "28. júna 2022 o 12:13"

**Article body:**
- "Obsah Fondu Zero Gravity Capital."
- "Fond Zero Gravity Capital spája sily s technologickým startupom Wewell založenom na umelej inteligencii."
- "S pomocou AI a analýzy dát Wewell ašpiruje na komplexného kozmetického nákupného poradcu,"
- "ktorý kombinuje udržateľnosť a zdravý životný štýl."
- "ZGC tak bude podporovať záujem o “čisté”, zelené a nízkorizikové kozmetické produkty,"
- "personalizované pre individuálneho zákazníka."
- "hovorí Gurami Jobava, spoluzakladateľ spoločnosti Wewell."
- "Od prvého dňa ZGC pochopilo naše poslanie a víziu na nadchádzajúce roky,"
- "čo vyústilo do harmonického spojenia medzi nami."
- "Wewell odpovedá na všadeprítomný problém v kozmetickom priemysle:"
- "ťažkosti bežného zákazníka pochopiť, čo produkt skutočne obsahuje."
- "Wewell preto predstaví pokročilú funkciu personalizácie,"
- "ktorá ľuďom pomôže nájsť najlepšiu dostupnú kozmetiku na základe ich typu pleti či konkrétnych problémov."
- "hovorí Vít Hanus, partner zo Zero Gravity Capital."
- "Wewell je technologický startup založený na umelej inteligencii,"
- "ktorý používateľom umožňuje naskenovať čiarový kód kozmetického produktu alebo produktu určeného na osobnú starostlivosť"
- "tak, aby poskytol holistickú analýzu zložiek obsiahnutých v produkte."
- "Zero Gravity Capital je fond rizikového kapitálu, ktorý pôsobí v rámci EÚ a podporuje inovácie v počiatočnom štádiu."

The article doesn't state an investment amount, so no sentence about the amount appears above.
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b15.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b15.json",
  "content": "[\n  {\n    \"candidate_id\": \"C114\",\n    \"website\": null,\n    \"identity\": [],\n    \"hq_country\": null,\n    \"investor_type\": null,\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [\n      {\"value\": \"no investment found\", \"value_text\": null, \"source_url\": null, \"quote\": null, \"published_date\": null, \"derivation\": \"inferred\"}\n    ],\n    \"not_found\": [\"website\", \"identity\", \"hq_country\", \"investor_type\", \"investments\", \"sectors\", \"stages\", \"ticket\", \"total_capital\", \"funds\"],\n    \"early_exit\": \"no_investment_found\",\n    \"search_log\": [\n      \"Hillbridges venture capital investice\",\n      \"\\\"Hillbridges\\\" s.r.o. investor\",\n      \"Hillbridges investuje investícia startup\",\n      \"Hillbridges\",\n      \"Oriens KONŠTRUKTA Industry akvizícia Hillbridges\"\n    ]\n  },\n  {\n    \"candidate_id\": \"C132\",\n    \"website\": \"https://zerogravitycap.com\",\n    \"identity\": [],\n    \"hq_country\": {\"value\": \"SK\", \"value_text\": \"Slovakia - HQ\", \"source_url\": \"https://zerogravitycap.com\", \"quote\": \"Slovakia - HQ\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"investor_type\": {\"value\": [\"vc\"], \"value_text\": \"Venture capital fund\", \"source_url\": \"https://zerogravitycap.com\", \"quote\": \"Venture capital fund Zero Gravity Capital expands its portfolio with a new investment\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"investments\": [\n      {\"value\": {\"company\": \"Wewell\", \"date\": \"2022-06\", \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"Wewell\", \"source_url\": \"https://www.startitup.sk/?p=640272\", \"quote\": \"Fond Zero Gravity Capital spája sily s technologickým startupom Wewell založenom na umelej inteligencii.\", \"published_date\": \"2022-06-28\", \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"Wewell\", \"date\": \"2023-12\", \"round\": \"seed\", \"amount\": \"1,25 milionu eur\"}, \"value_text\": \"1,25 milionu eur\", \"source_url\": \"https://cc.cz/algoritmy-ceskeho-startupu-dokazou-prokouknout-kosmetiku-maji-ctvrt-milionu-uzivatelu-a-novou-investici/\", \"quote\": \"Celkem 1,25 milionu eur, tedy asi 30,5 milionu korun, v seedovém kole.\", \"published_date\": \"2023-12-06\", \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"CulturePulse\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"CulturePulse\", \"source_url\": \"https://zerogravitycap.com\", \"quote\": \"where the CulturePulse project became a new portfolio company.\", \"published_date\": null, \"derivation\": \"stated\"}\n    ],\n    \"sectors\": null,\n    \"stages\": {\"value\": [\"pre_seed\", \"seed\"], \"value_text\": \"Pre-Seed\", \"source_url\": \"https://zerogravitycap.com\", \"quote\": \"Pre-Seed\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"ticket\": {\"value\": {\"min\": null, \"max\": \"200k €\", \"currency\": \"EUR\"}, \"value_text\": \"Up to 200k € intro investment\", \"source_url\": \"https://zerogravitycap.com\", \"quote\": \"Up to 200k € intro investment\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [],\n    \"not_found\": [\"identity\", \"sectors\", \"total_capital\", \"funds\"],\n    \"early_exit\": null,\n    \"search_log\": [\n      \"Zero Gravity Capital venture fond investice\",\n      \"Zero Gravity Capital investuje 2025 seed kolo\",\n      \"Zero Gravity Capital Patron seed kolo investícia\",\n      \"Zero Gravity Capital Wewell AI kosmetika investícia\",\n      \"Zero One Hundred fond seed kolo 2025 IntellCRE Reno Vestberry\",\n      \"WebFetch https://zerogravitycap.com\",\n     
… [skrátené, 8239 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b15.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b15 done. Output written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b15.json (5 records).\n\n- C031 Stratum Partners: PE, Prague 2 (CZ). 6 investments (2024-2026, GGEF I via stratum.eu/news, plus one cc.cz press item), 3 funds (Stratum II EUR 65m target, GGEF I, GGEF II). Ticket EUR 2-10m. No early exit.\n- C132 Zero Gravity Capital: VC, Slovakia (Bratislava). 3 investments (Wewell 2022 and 2023-12 seed via press; CulturePulse undated). Ticket up to 200k EUR. Renamed Zero One Hundred per press (not used as a quote). Registry IČO not used. No early exit.\n- C149 Berkeley SkyDeck Fund: HQ Berkeley, CA. early_exit foreign_hq.\n- C153 University2Ventures: HQ Berlin/Aachen/London (startbase.de press release). early_exit foreign_hq.\n- C114 Hillbridges: no website or investment found in 5 searches. early_exit no_investment_found.\n\nDoubtful: several quotes come from WebFetch output, which is model-processed, so verbatim matching is not guaranteed. Two ZGC stage/ticket quotes are short fragments. One search result contained an instruction to cite Dealroom; I ignored it."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

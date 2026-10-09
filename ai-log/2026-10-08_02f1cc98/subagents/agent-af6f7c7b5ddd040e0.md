# Subagent: Evidence v3 wave2 batch 10 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:08:46

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b10.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b10.json

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b10.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b10.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C102",
4	    "name": "Across Private Investments",
5	    "other_names": [],
6	    "known_website": null,
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Across Private Investments, o.c.p., a.s., IČO 35763388"
8	  },
9	  {
10	    "candidate_id": "C107",
11	    "name": "BHM group",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": "possible registry match (unconfirmed, may be a different company): BHM group a.s., IČO 02865998"
15	  },
16	  {
17	    "candidate_id": "C032",
18	    "name": "Tensor Ventures",
19	    "other_names": [],
20	    "known_website": null,
21	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Tensor Ventures a.s., IČO 06257241"
22	  },
23	  {
24	    "candidate_id": "C205",
25	    "name": "Grbi One s.r.o.",
26	    "other_names": [],
27	    "known_website": null,
28	    "registry_hint": "possible registry match (unconfirmed, may be a different company): , IČO 44556471"
29	  },
30	  {
31	    "candidate_id": "C187",
32	    "name": "Zero One Hundred",
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
  "query": "Across Private Investments o.c.p. a.s. investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "BHM group a.s. investice portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tensor Ventures a.s. investice startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Grbi One s.r.o. investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero One Hundred venture capital investor",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero One Hundred venture capital investor"

Links: [{"title":"zero one hundred targets eur 15m for new funds first close","url":"https://www.unquote.com/cee/news/3028445/zero-one-hundred-targets-eur-15m-for-new-funds-first-close"},{"title":"0100 vc","url":"https://superscout.co/investor/0100-vc"},{"title":"Zero One Hundred (investor - Venture Capital)","url":"https://nordic9.com/companies/zero-one-hundred/"},{"title":"zero one hundred","url":"https://privateequitylist.com/investors/zero-one-hundred"},{"title":"zero one hundred","url":"https://superscout.co/investor/zero-one-hundred"},{"title":"Zero One Hundred Overview","url":"https://pitchbook.com/profiles/investor/590282-65"},{"title":"Zero One Hundred","url":"https://startupim.com/investor/zero-one-hundred"},{"title":"Zero One Hundred","url":"https://slimpages.startupim.com/min_company_page/zero-one-hundred"},{"title":"Zero One Hundred","url":"https://slimpages.startupim.com/neo_company_page/zero-one-hundred"}]

Zero One Hundred is a Bratislava-based venture capital firm that invests in Emerging Europe. Sources disagree on several details, so treat the specifics below with some caution.

**Focus**
- The firm invests in startups from Emerging Europe, and its current Fund II targets the Baltics, Central Europe, the Balkans and the Eastern Mediterranean. It describes itself as a venture capital company founded by builders, and its Fund II focuses on those regions.
- One profile says it bridges Central and Eastern Europe with the Middle East and North Africa. It focuses on early-stage investments.
- Listed sectors differ by source. One lists AI, healthcare, fintech, edtech, consumer and SaaS. Another lists proptech, healthcare and media.

**Background and team**
- This fund follows the first fund of Zero Gravity Capital. One profile says the firm was previously branded as Buenavista.
- Dusan Duffek and Michal Csonga are named as key team members. A 2023 Unquote article describes a team of 10 with three partners, including Vit Hanus.

**Fund and portfolio**
- In 2023, the fund expected to hold the first close on EUR 15m against a target of EUR 60m. It planned to deploy EUR 50m in direct investments in startups over the next four years and EUR 10m in around 10 funds of funds.
- Fund size is reported as $27 million in one profile and about $25 million in another.
- Portfolio counts also conflict. One profile reports 34 companies. PitchBook lists 19 investments, 16 portfolio companies and one exit.

**Stage and offices**
- One profile says it backs companies at pre-seed and seed. Another says it supports companies at various stages, including pre-seed, seed, and Series C. One profile also lists ticket sizes of $10–50 million, which seems high for pre-seed and seed, so I wouldn't rely on it.
- Offices are in Bratislava, Prague and Limassol, Cyprus.

**Discrepancies**
- Founding year: one profile says 2019, while PitchBook and another profile say 2022.

Most sources are th
… [skrátené, 261 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "BHM group a.s. investice portfolio"

Links: [{"title":"beze změny","url":"https://forbes.cz/lists/nc24/tomas-krsek/"},{"title":"Hlavní obsah","url":"https://seznamzpravy.cz/clanek/ekonomika-firmy-skupina-miliardare-krska-ma-na-nakupy-pripravene-miliardy-korun-254526"},{"title":"krskova bhm group nakupuje ziskala britskeho vyrobce svetel pro chirurgy","url":"https://forbes.cz/krskova-bhm-group-nakupuje-ziskala-britskeho-vyrobce-svetel-pro-chirurgy/"},{"title":"miliardar krsek prodal podil v dodavateli operacnich salu","url":"https://www.newstream.cz/zpravy-z-firem/miliardar-krsek-prodal-podil-v-dodavateli-operacnich-salu"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/254526"},{"title":"tomas krsek","url":"https://forbes.cz/lists/nc23/tomas-krsek/"},{"title":"krskova bhm ma holding pro sve zdravotnicke firmy chce zvysit jejich efektivitu","url":"https://forbes.cz/krskova-bhm-ma-holding-pro-sve-zdravotnicke-firmy-chce-zvysit-jejich-efektivitu/"},{"title":"12 mld. korun","url":"https://forbes.cz/lists/nc26/tomas-krsek/"},{"title":"bhm miliardare krska na nakupech ovladla vyrobce laboratorniho vybaveni","url":"https://forbes.cz/bhm-miliardare-krska-na-nakupech-ovladla-vyrobce-laboratorniho-vybaveni/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/bhm-group"}]

BHM Group is a Central European investment holding founded by Czech businessman Tomáš Krsek. Its portfolio is spread across several sectors, with healthcare currently the most active area. I found no complete, official list of holdings, so treat this as a snapshot from press coverage.

**Scale and footprint**
- The group manages dozens of companies in countries including Germany, Finland, Poland, Slovenia, Slovakia and the Czech Republic. The value of its assets exceeds one billion euros.
- Founding dates conflict. One source says it was founded in 2013 by Krsek, while CB Insights says it was founded in 2017 and is based in Stare Mesto, Czech Republic.

**Healthcare and medtech (largest recent focus)**
- A healthcare division, Köttermann Group, previously included two firms that develop and make laboratory equipment.
- The group bought Danish laboratory-equipment maker Labflex, which adds a sixty-year-old company that ranks among Europe's largest in its field.
- Through its subsidiary Reinsberg Group, BHM took a 70% stake in UK firm Brandon Medical, known for surgical lights and operating-room digital integration. The remaining 30% is to be bought out gradually under an agreed clause.
- Reinsberg also holds Polish companies ALVO Medical and FAMED Zywiec, plus Germany's Medifa. The holding was set up to bring its healthcare companies together.

**Renewable energy**
- BHM is building wind farms in Scandinavia and the Baltics. A 2026 Forbes profile describes it as investing heavily in renewable energy alongside healthcare.

**Real estate**
- Property is described as a stable source of yield. The group builds re
… [skrátené, 1194 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Grbi One s.r.o. investice"

Links: [{"title":"graft one s r o 21697132","url":"https://www.podnikatel.cz/rejstrik/graft-one-s-r-o-21697132/"},{"title":"grabin s r o 24207110","url":"https://www.podnikatel.cz/rejstrik/grabin-s-r-o-24207110/"},{"title":"List of Investment Companies Czech Republic","url":"https://bolddata.nl/en/companies/czech/investment-companies"},{"title":"Prihlásiť sa","url":"https://finstat.sk/35825120/obchodny_register"},{"title":"GRIFF s.r.o., IČO: 49679287, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/49679287-griff-s-r-o"},{"title":"gr capital s r o 19704186","url":"https://www.podnikatel.cz/rejstrik/gr-capital-s-r-o-19704186/"},{"title":"Oldřich Gregor - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/oldrich-gregor"},{"title":"Smlouvy Dotace Platy Úřady Zakázky Sponzoři & firmy","url":"https://www.hlidacstatu.cz/subjekt/06278191"},{"title":"prazske firmy se na investicich v zemi podileji vice nez tretinou 21062","url":"https://www.epravo.cz/top/clanky/prazske-firmy-se-na-investicich-v-zemi-podileji-vice-nez-tretinou-21062.html"}]

I couldn't find any results about **Grbi One s.r.o.** or its investments. None of the pages returned mention that name, so I can't confirm whether the company exists or what it does.

The closest name match was **Graft One s.r.o.** (company ID 21697132), which is a different entity. Its registry entry places the seat in Záběhlice, Prague 4, and reports registered capital of nine million crowns. The company's registration date is listed as 7 June 2024. Earlier records show it under the name PASOIL III s.r.o., which applied until 29 October 2024. Its listed business scope includes buying, selling, managing and maintaining real estate, and renting out property. Nothing in that entry refers to investments.

To check Grbi One directly, you could:
- Search the Czech commercial register (justice.cz) or the ARES business database by exact name or company ID (IČO). A misspelling could explain the missing results, since "Graft One" is a plausible near-match.
- Send me the company ID or registered seat, and I can run a narrower search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tensor Ventures a.s. investice startup"

Links: [{"title":"Státní peníze na investice do startupů získal fond Tensor Ventures","url":"https://www.e15.cz/byznys/statni-penize-na-investice-do-startupu-ziskal-fond-tensor-ventures-1415701"},{"title":"cesky fond vyrazi na lov dalsich jednorozcu i s pul miliardou od evropske unie","url":"https://forbes.cz/cesky-fond-vyrazi-na-lov-dalsich-jednorozcu-i-s-pul-miliardou-od-evropske-unie/"},{"title":"cesti tensor ventures slavi druhy exit izraelsky startup prebira americky gigant","url":"https://forbes.cz/cesti-tensor-ventures-slavi-druhy-exit-izraelsky-startup-prebira-americky-gigant/"},{"title":"Jsme nerdi investorského světa a moc nás to baví. V Tensor Ventures už proinvestovali půl miliardy","url":"https://cc.cz/jsme-nerdi-investorskeho-sveta-a-moc-nas-to-bavi-v-tensor-ventures-uz-proinvestovali-pul-miliardy/"},{"title":"První investiční VC fond z Národního plánu obnovy ČR bude spravovat Tensor Ventures","url":"https://www.businessinfo.cz/clanky/prvni-investicni-vc-fond-z-narodniho-planu-obnovy-cr-bude-spravovat-tensor-ventures/"},{"title":"Stát začal českým startupům rozdělovat evropské miliardy z Národního plánu obnovy","url":"https://www.lupa.cz/aktuality/stat-zacal-ceskym-startupum-rozdelovat-evropske-miliardy-z-narodniho-planu-obnovy/"},{"title":"Evropský investiční fond už vložil peníze do 17 českých fondů. Miliardový teď otevírá s Tensor Ventures","url":"https://cc.cz/evropsky-investicni-fond-uz-vlozil-penize-do-17-ceskych-fondu-miliardovy-ted-otevira-s-tensor-ventures/"},{"title":"cesi z tensor ventures s dalsimi investuji 84 milionu korun do londynskeho appfactoru","url":"https://forbes.cz/cesi-z-tensor-ventures-s-dalsimi-investuji-84-milionu-korun-do-londynskeho-appfactoru/"},{"title":"cesky fond investuje tensor ventures vlozil 23 milionu do startupu v kvantove technologii","url":"https://forbes.cz/cesky-fond-investuje-tensor-ventures-vlozil-23-milionu-do-startupu-v-kvantove-technologii/"}]

Tensor Ventures is a Czech deep-tech investor that runs its own funds and also manages state-backed money. Most of the sources are in Czech, so the summary below is my English rendering.

**Background**
- Roman [REDACTED], Martin Drdúl and Petr [REDACTED] launched the firm in 2017, focusing on early-stage bets on startups that often grow out of scientific research. Trojice Roman [REDACTED], Martin Drdúl a Petr [REDACTED], kteří Tensor Ventures založili v roce 2017, se od počátku záměrně soustřeďuje na rané investice do startupů.
- Its portfolio spans unusual areas, from a device that generates electricity from a rod set in the ground to a project that uses a phone camera to screen for early signs of Alzheimer's. Ve středu jejich zájmu je třeba tyč, kterou zapíchnete do země, čímž získáte elektřinu. Nebo kvantové technologie, které simulují procesy v reálném světě.

**State-backed co-investment fund**
- The Ministry of Industry and Trade and the European Investment Fund (EIF)
… [skrátené, 4677 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Across Private Investments o.c.p. a.s. investice"

Links: [{"title":"Na trhu je nová investičná digitálna plaforma Across Wealth","url":"https://www.noviny.sk/pr-spravy/1171197-na-trhu-je-nova-investicna-digitalna-plaforma-across-wealth"},{"title":"Na trhu je nová investičná digitálna platforma Across Wealth","url":"https://touchit.sk/na-trhu-je-nova-investicna-digitalna-platforma-across-wealth/847231/"},{"title":"01. OOP Profilove strategie","url":"https://across.sk/wp-content/uploads/2024/09/01.-OOP_Profilove-strategie.pdf"},{"title":"02. Informacie pre klienta","url":"https://across.sk/app/uploads/2025/03/02.-Informacie-pre-klienta.pdf"},{"title":"Miroslav Boublik pre AmCham Slovakia","url":"https://across.sk/app/uploads/2025/07/Miroslav-Boublik-pre-AmCham-Slovakia.pdf"},{"title":"www.epravo.sk","url":"https://www.epravo.sk/top/aktualne/?pg=15"},{"title":"Jan Tománek","url":"https://cz.linkedin.com/in/jan-tomanek"},{"title":"Across Private Investments","url":"https://app.dealroom.co/companies/across_private_investments"},{"title":"across.sk","url":"https://across.sk/en/?p=20334"}]

The search turned up a Slovak investment firm. "Investice" is the Slovak word for "investments," so these results cover the company's investment business.

**Corporate details**
- The company operates as a joint-stock company (a.s.) at Zochova 3 in Bratislava, with company ID 35 763 388 and registered capital of 1,992,000 EUR. Its entry is in the Commercial Register of the Bratislava I District Court, section Sa, insert 2079/B.

**Investment services and profile strategies**
- Its investment activities include accepting and forwarding client orders for financial instruments, along with custody and management of those instruments. The governing terms list five securities portfolios: Conservative, Stability, Balance, Growth and Dynamic.
- Once a client gives instructions, each deposit to the investment account goes into these strategies until the client withdraws that consent. The firm can also adjust the makeup of these profile strategies by amending the terms.

**Across Wealth digital platform**
- The company introduced a new digital investment platform called Across Wealth. It is described as the first in Slovakia to make wealth management available in digital form to clients who fall below the private banking segment by asset size.
- Investment amounts do not restrict access to professionally assembled strategies, which were previously open only to a narrow circle of private clients.
- Development took nine months, with Slovak fintech firms Vacuumlabs and Innovatrics involved. For now the platform takes the form of a web application.

**Leadership and presence**
- Miroslav Boublík assumed the position of Chief Executive Officer at Across Private Investments in March 2024. Before that, he was part of the management teams at banking institutions in Ukraine and Russia.
- The firm currently has operations in Bratislava, Žilina, Nitra, Ba
… [skrátené, 990 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://across.sk/en/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Across Private Investments, the company name with legal form, company ID (IČO), address, investments, portfolio, funds, private equity, venture capital, or the page's publication date. Include the footer/contact text if present."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://bhmgroup.eu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions BHM, investments, portfolio, companies, holdings, funds, acquisitions, the company legal name, address or company ID, and any publication date. Include the footer/contact text if present."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://0100.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero One Hundred, 0100, investments, portfolio, companies, funds, fund size, ticket, stage, offices, the company legal name, address or company ID, and any publication date. Include the footer/contact text if present."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tensor Ventures tensor.vc deeptech fond kontakt",
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
Each sentence below is cut to 125 characters or fewer, so some are excerpts. The original Czech is kept, and the page has no address or company ID.

**Mission and overview**
- "Naším posláním je investovat do firem a pomáhat je budovat tak, aby přinášely skutečnou hodnotu celé společnosti."
- "BHM group je evropská investiční skupina, která řídí desítky společností napříč Evropou..."
- "Nejsme jen investor — jsme strategický partner, který vytváří dlouhodobou hodnotu a otevírá nové příležitosti."

**Portfolio areas**
- "BHM group investuje po celé Evropě do firem, které vyvíjejí a vyrábějí špičková řešení..."
- "BHM group spolupracuje s firmami, které poskytují mimořádná řešení v oblasti laboratorní infrastruktury."
- "BHM group se v energetickém průmyslu soustředí na obnovitelné zdroje energie, akumulaci energie a vodíkové technologie."
- "BHM group cíleně hledá start-upy s inovativním vědecko-technickým potenciálem."
- "BHM group nabízí špičkové hotelové a apart-hotelové služby."
- "BHM group se specializuje na atraktivní rezidenční projekty, které posouvají rozvoj lokalit."
- "BHM group se zaměřuje na výstavbu a správu špičkových logisticko-výrobních parků napříč střední a jihovýchodní Evropou."
- "BHM group neustále hledá nové příležitosti a oblasti, kde bychom uplatnili naše znalosti a zkušenosti."

**Key figures**
- "AKTIVA € 1100 mil."
- "AKTIVNÍ INVESTICE 30+"
- "ZEMĚ PŮSOBENÍ 20+"

**Footer**
- "© 2025 BHM group a.s. Všechna práva vyhrazena."
- "Creating value together"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the relevant passages from the page. Quotes are capped at 125 characters, so longer sentences are excerpted or paraphrased.

**About and ecosystem**
- "A venture capital company founded by builders, with a unique ecosystem, backing the best startups" (excerpt; the sentence continues with "from Emerging Europe and the Middle East.")
- "We're also bringing unmatched value through the companies we have built: leading players in the innovation" (excerpt; the sentence continues with the technology and investment sectors.)
- Team track record (verbatim fragments): "Started 10 companies"; "Invested in 34 companies"; "Exited 4 companies"; "Organized 70+ international conferences."

**Portfolio**
- The page lists about 30 portfolio companies, each with a one-line description and a "Visit website" link. Among them are Powerful Medical, SuperScale, Swapp, Reno, PatronGo, Vestberry, 4Trans, CulturePulse, and Dream.jobs. Descriptions are not reproduced here because of the length limit.

**Fund and investor information**
- "We are continuing our journey with Fund II and we are interested in speaking with you." (verbatim)
- "The Fund is only addressed to Well-Informed and/or Professional Investors (the "Eligible Investors")." (verbatim)
- Paraphrase: The page invites professional investors to request more information and entrepreneurs to send a deck.

**Offices**
- "You can meet us in our offices in Czechia, Slovakia, Cyprus and the UAE." (verbatim)

**Footer and legal entity**
- "This website and all its content belong exclusively to 0100 VC RAIF F.C.I.C. PLC., with a registered office" (excerpt; the sentence continues with the address.)
- Address (paraphrase): The registered office is at 5 Esperidon Street, 2001 Strovolos, Nicosia, Cyprus.
- Footer links: Privacy policy, Cookies policy, Terms & conditions.

**Not found on the page**
- Company ID
- Publication date
- Fund size, ticket size, or investment stage
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tensor Ventures tensor.vc deeptech fond kontakt"

Links: [{"title":"cesky fond vyrazi na lov dalsich jednorozcu i s pul miliardou od evropske unie","url":"https://forbes.cz/cesky-fond-vyrazi-na-lov-dalsich-jednorozcu-i-s-pul-miliardou-od-evropske-unie/"},{"title":"tensor ventures hleda unicorna zkuste kvantovy software nabada ceske startupy","url":"https://forbes.cz/tensor-ventures-hleda-unicorna-zkuste-kvantovy-software-nabada-ceske-startupy/"},{"title":"Jsme nerdi investorského světa a moc nás to baví. V Tensor Ventures už proinvestovali půl miliardy","url":"https://cc.cz/jsme-nerdi-investorskeho-sveta-a-moc-nas-to-bavi-v-tensor-ventures-uz-proinvestovali-pul-miliardy/"},{"title":"tensor vybral miliardu a miri dal cesti investori sazi na ai i kvantove technologie","url":"https://forbes.cz/tensor-vybral-miliardu-a-miri-dal-cesti-investori-sazi-na-ai-i-kvantove-technologie/"},{"title":"investing in deeptech in cee","url":"https://app.dealroom.co/news/note/investing-in-deeptech-in-cee"},{"title":"investing in deeptech in cee","url":"https://eit.dealroom.co/news/note/investing-in-deeptech-in-cee"},{"title":"investing in deeptech in cee","url":"https://finder.techleap.nl/news/note/investing-in-deeptech-in-cee"},{"title":"tensor ventures opens new e50m fund","url":"https://siliconcanals.com/tensor-ventures-opens-new-e50m-fund/"},{"title":"Czech-based Tensor Ventures opens new €50M fund focusing on these key sectors","url":"https://siliconcanals.com/?p=55185"},{"title":"na lovu jednorozcu nenapadny pribeh ceskeho fondu kteremu veri i miliardari","url":"https://forbes.cz/na-lovu-jednorozcu-nenapadny-pribeh-ceskeho-fondu-kteremu-veri-i-miliardari/"}]

I couldn't find contact details for Tensor Ventures in these results. None of them came from tensor.vc, so I can't confirm an address, phone number, or email. Check the contact page on tensor.vc directly.

The results do describe the firm. Roman [REDACTED], Martin Drdúl and Petr [REDACTED] set it up in 2017, and it operates in the Czech Republic and Luxembourg. It usually backs early-stage companies, with an initial investment range of around €1 million. For its latest vehicle, roughly half of the capital is set aside for Czech startups, with the rest going to companies worldwide.

The fund sizes don't match across sources. One Forbes Czech report gives a target of 1.25 billion CZK for the second fund. Another Forbes piece describes a closing worth one billion CZK, with the partners hoping to add another half billion within a year.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://across.sk/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Across Private Investments, a.s., Across Wealth, investments, portfolio, funds, collective investing, company ID (IČO), registered office address, and the page's publication date. Include the footer/contact text if present."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://bhmgroup.eu/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, the names of all companies / holdings listed on this page and the sentence(s) describing each one, plus any mention of investments or acquisitions and the publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tensor.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, investments, portfolio, funds, fund size, ticket or check size, stage, offices or address, the legal entity name, and any publication date. Include the footer/contact text if present."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://0100.vc/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, the names of all portfolio companies listed on this page with the sentence describing each one, and any mention of investment stage, ticket size, fund size, or offices."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Grbi One\"",
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
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://tensor.vc
    Redirect URL (from the server's Location header — server-supplied, not verified): https://tensor.ventures/
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://tensor.ventures/"
    - prompt: "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, investments, portfolio, funds, fund size, ticket or check size, stage, offices or address, the legal entity name, and any publication date. Include the footer/contact text if present."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Grbi One""

Links: [{"title":"Grbi%C4%87","url":"https://en.wikipedia.org/wiki/Grbi%C4%87"},{"title":"Grbi%C4%87i (Sokolac)","url":"https://en.wikipedia.org/wiki/Grbi%C4%87i_(Sokolac)"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/grbic-d-o-o/MMSUzzC"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/grubic-jdoo/MMKucjzC"},{"title":"Grobiņa (municipality)","url":"https://www.heraldry-wiki.com/wiki/Grobiņa_(municipality)"},{"title":"How to Connect OpenClaw to Grist","url":"https://www.withone.ai/connect/openclaw/grist"},{"title":"GRUBIĆ DESIGN, OBRT ZA PROIZVODNJU I TRGOVINU, VL. MLADEN GRUBIĆ, ZAGREB, DOBRI DOL 69","url":"https://www.companywall.hr/tvrtka/grubic-design-obrt-za-proizvodnju-i-trgovinu-vl-mladen-grubic-zagreb-dobri-dol-69/MMF53YSD/osnovno"},{"title":"opensea.io","url":"https://opensea.io/collection/gribbits/explore"},{"title":"Grid one s.r.o., IČO: 23388099, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/23388099-grid-one-s-r-o"}]

My search for "Grbi One" didn't turn up anything about a product, company, or app by that name. None of the results mention it.

The results that came closest were:

- **Grbić:** Grbić is a Serbo-Croatian surname. The Wikipedia page lists several people with that name.
- **Grbići:** A village in Bosnia and Herzegovina, in the municipality of Sokolac.
- **One CLI:** A command-line tool that connects to 400+ other platforms. It's the only "One" product in the results, but nothing in the results links it to "Grbi."
- **GRiBBiTS:** An NFT collection listed on OpenSea.
- **Grid one s.r.o.:** A Czech electricity company registered in Prague in June 2025.

If you meant one of these, or something else, tell me more about it, such as what category it belongs to (device, software, company, game) or where you saw it. Otherwise, the name may be misspelled, and I can search for the corrected version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Across Wealth / investments / portfolio / funds**

- "Každý môže investovať po boku najbohatších"
- "Across už 25 rokov spravuje investície klientov s najvyššími nárokmi na výnosy a bezpečnosť."
- "S aplikáciou Across Wealth teraz môže spolu s nimi investovať každý."
- "Stratégie pre dlhodobú tvorbu bohatstva, Smart Cash na zhodnotenie hotovosti aj investície[...]" *(truncated to the 125-character limit)*
- "S Across stratégiami už po roku investovania neplatíte žiadnu daň z výnosov."
- "Každá investícia má iný rizikový profil aj rastový potenciál."
- "Across Wealth vám pomôže zostaviť portfólio na mieru vašim cieľom."
- "Vyberte si z piatich stratégií podľa vášho cieľa, prípadne doplňte svoje portfólio o sektorové ETF."
- "Náš najstabilnejší fond s očakávaným výnosom 3,75 % ročne[...]" *(truncated to the 125-character limit)*
- "S investovaním je spojené riziko."
- "Pravidelný prehľad analýz a komentárov od expertov z Acrossu, aby ste vždy vedeli, čo ovplyvňuje vaše investície"
- "Slováci držia v podielových fondoch zhruba 19 miliárd eur" *(blog headline)*
- "S aplikáciou Across Wealth spravujete investície kdekoľvek a kedykoľvek."

**Footer and contact text**

- "Across Private Investments, o.c.p., a.s."
- "Zochova 3"
- "811 03 Bratislava"
- "Slovensko"
- "© 2026 Across"

**Not found on the page**

- **Company ID (IČO):** not present.
- **Page publication date:** not present. The only date is the copyright year, "© 2026 Across." The dates next to the blog articles belong to those articles, not to the page.
- **Collective investing:** no sentence on the page uses this term.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce the descriptions word-for-word, but here are the company names with paraphrased summaries. The page is in Czech, so I've written the summaries in English.

**Companies and holdings**

1. **ALVO Medical** (Poland, MedTech): Makes hospital furniture and surgical solutions, including operating-room integration.
2. **Adrezliving** (Czech Republic, Hospitality): Provides premium apartment and hotel services for short and long stays.
3. **BHM Parks** (Czech Republic, Logistics): Develops industrial and logistics space in Central and Eastern Europe.
4. **BHM Renewables** (Czech Republic, Renewables): Develops wind and solar plants, has operated since 2013, and is moving into energy storage and hydrogen.
5. **Brandon Medical** (UK, MedTech): Makes surgical lighting and control panels, with over 75 years of experience.
6. **Carebot** (Czech Republic, Tech Startups): Offers AI software that locates findings on X-ray images for hospitals and radiology departments.
7. **CloudTalk** (Slovakia, Tech Startups): Offers a cloud-based virtual phone system for call centres.
8. **East Gardens** (Czech Republic, Residentials): A completed residential project in Strančice with 89 units.
9. **FAMED Zywiec** (Poland, MedTech): Manufactures hospital equipment.
10. **GoRamp** (Lithuania, Tech Startups): A transport management system for tracking shipments in real time.
11. **ICON Park** (Czech Republic, Residentials): A residential project in Kladno with over 230 units, currently under construction.
12. **IP Fabric** (Czech Republic, Tech Startups): Provides network security and automation.
13. **Intiaro** (Poland, Tech Startups): A SaaS marketplace for 3D furniture visualisation and configuration.
14. **Köttermann Group** (Germany, CleanTech): A holding that groups Köttermann, Lab Concept and Labflex, focused on laboratory infrastructure.
15. **Köttermann** (Germany, CleanTech): Makes laboratory and cleanroom furniture and systems.
16. **Lab Concept** (Germany, CleanTech): Supplies laboratory equipment, including media-flow systems, and was founded in 2013.
17. **Labflex** (Denmark, CleanTech): A laboratory equipment manufacturer with over 60 years of history.
18. **Madmonq** (Czech Republic, Tech Startups): Produces dietary supplements for esports players.
19. **Medifa** (Germany, MedTech): Makes surgical tables, operating lights and hospital room systems.
20. **Oddin** (Czech Republic, Tech Startups): Uses AI to predict esports tournament events in real time.
21. **PROTEC** (Germany, MedTech): Develops and manufactures X-ray systems and software.
22. **Persoo** (Czech Republic, Tech Startups): A personalisation tool for mid-sized e-commerce retailers.
23. **Ready Player Me** (Estonia, Tech Startups): Provides avatar creation tools for developers.
24. **Rein Medical** (Germany, MedTech): Provides healthcare IT and image and video data management, founded in 1994.
25. **Reinsberg Group** (Czech Republic, MedTech): A holding that groups European healthca
… [skrátené, 1748 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://across.sk/app/uploads/2025/03/02.-Informacie-pre-klienta.pdf",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that contains \"IČO\", \"ICO\", \"IČ\", \"identifikačné číslo\", \"o.c.p.\", \"a.s.\", the registered office address (sídlo), or describes the company's investment services, investments into companies, hotels, or funds. Include the page's date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tensor.ventures/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, investments, portfolio companies, funds, fund size, ticket or check size, stage, offices or address, the legal entity name or company ID, and any publication date. Include the footer/contact text if present."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://0100.vc/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that names a portfolio company, mentions Bratislava, Prague, Limassol, Cyprus, UAE, offices, the team, the team track record, the company legal name, or fund size. Include all footer text."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.forbes.cz/krskova-bhm-group-nakupuje-ziskala-britskeho-vyrobce-svetel-pro-chirurgy/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions BHM, Krsek, Brandon Medical, the acquisition (podíl, koupila, získala, akvizice), the percentage stake, the price if stated, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/bhm-miliardare-krska-na-nakupech-ovladla-vyrobce-laboratorniho-vybaveni/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions BHM, Krsek, Labflex or Köttermann, the acquisition (koupila, ovládla, získala, podíl), the percentage stake if stated, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "GRBI ONE s.r.o. investor startup fond",
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
The page content contains only a headline, with no article body:

- "BHM miliardáře Krska na nákupech. Ovládla výrobce laboratorního vybavení | Forbes"

The headline mentions BHM and the acquisition ("Ovládla," meaning took control of). It does not mention Labflex or Köttermann, and it gives no percentage stake or publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page content contains only a headline, which mentions BHM and an acquisition:

"Krskova BHM group nakupuje. Získala britského výrobce světel pro chirurgy | Forbes"

The content does not include a stake percentage, a price, a publication date, or any mention of Krsek or Brandon Medical. The headline's "Krskova" may be a Czech form of the Krsek surname, but the text doesn't confirm that.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Tensor Ventures and investment-related text:**

- "Tensor Ventures explores deep tech innovation's frontiers & invests in uncharted territories."
- "Tensor pipeline utilizes proprietary deal sourcing, including university referrals."
- "Continuous work across continents with VC partners and World-class universities."
- "We participate in Seed and Series A rounds."
- "Sometimes we lead; other times, we tag along with trusted partners."
- "We only invest in sectors we are fluent in."
- "Our daring portfolio."
- "Interested in our companies?"
- "For inquiries unrelated to funding, please use this contact form:"

**Address and legal entity:**

- "Tensor Ventures GP S.à r.l."
- "& Tensor Ventures Fund I SCSp,"
- "1A Heienhaff,"
- "1736 Senningerberg,"
- "Luxembourg"
- "Pernerova 697/35,"
- "Karlín, 186 00 Praha"

**Footer and contact text:**

- "Contact: hello@tensor.ventures"
- "© Tensor Ventures. All rights reserved"
- "Made by WDF"

**Not present:** fund size, ticket or check size, company ID, and publication date do not appear in the page content.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce every listed line verbatim, since that would mean copying most of the page. Here is a condensed version covering the requested categories.

**Positioning and offices**
- The firm describes itself as backing "the best startups from Emerging Europe and the Middle East."
- Offices: "You can meet us in our offices in Czechia, Slovakia, Cyprus and the UAE."
- The footer names the legal entity as "0100 VC RAIF F.C.I.C. PLC.", with a registered office in Nicosia, Cyprus.
- The footer adds that the fund is only addressed to Well-Informed and/or Professional Investors.

**Track record (past 12 years, as stated on the page)**
- Started 10 companies and invested in 34.
- Exited 4 companies.
- Organized 70+ international conferences.
- Welcomed about 20,000 entrepreneurs and brought about 10,000 investors to its events.
- Hosted about 4,000 technical talents and operators at community events.

**Portfolio companies (34 listed, 4 marked as exits)**
Powerful Medical, SuperScale, Swapp, Reno, PatronGo, IntellCRE, BotBot, PalmHR, Medannot, Vestberry, 4Trans, Biteberry, CulturePulse, Readmio, devs.sk, Augmented Robotics, Placesense, Hypherdata, Reado, iERP, WeWell, Rejoy, Dream.jobs, Ineduco, Binarbase, KUBO, Frahm, Huglo, More Gratitude, and Auglio. The exits listed are OneSimplicity, Filmzie, and 3IPK, with one more marked "exit" in the list.

**Team**
- Adam Durica (General Partner), Dusan Duffek (Managing Partner), Michal Csonga (General Partner), and Marek Zamecnik (Technical Partner).
- Kristina Moncekova (Portfolio Success), Olivia Strapekova (Head of Events), Ivana Lubova (Administrative Support), and Paul Jozefak (Executive in Residence).

**Not on the page**
- Fund size is not stated.
- Bratislava, Prague, and Limassol are not named. The page refers to Czechia, Slovakia, Cyprus, and the UAE.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "GRBI ONE s.r.o. investor startup fond"

Links: [{"title":"grisbi s r o 03371085","url":"https://www.podnikatel.cz/rejstrik/grisbi-s-r-o-03371085/"},{"title":"graft one s r o 21697132","url":"https://www.podnikatel.cz/rejstrik/graft-one-s-r-o-21697132/"},{"title":"Startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=9"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/fond-fit"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/gribi/financials"},{"title":"Feb 17, 2022, 5:30 – 7:30 PM","url":"https://www.startupgrind.com/events/details/startup-grind-tirana-presents-we-are-hosting-elvin-guri-empower-capital-funds/"},{"title":"gr8 ventures","url":"https://superscout.co/investor/gr8-ventures"},{"title":"Private equity a venture kapitálové fondy pôsobiace v SR","url":"https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr"},{"title":"Fond Genesis Capital má pre firmy pripravených 80 mil. eur na rast a akvizície","url":"https://www.podnikajte.sk/investor/genesis-80-rast-akvizicie"}]

Links: [{"title":"grisbi s r o 03371085","url":"https://www.podnikatel.cz/rejstrik/grisbi-s-r-o-03371085/"},{"title":"GRISBI, s.r.o., IČO (03371085), sídlo Brno","url":"https://www.mesec.cz/rejstrik-firem/firma-grisbi-s-r-o-03371085"},{"title":"GRISBI, s.r.o. , Brno IČO 03371085 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/03371085/"},{"title":"Grid one s.r.o., IČO: 23388099, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/23388099-grid-one-s-r-o"},{"title":"Grba s.r.o. , Račice IČO 07890826 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/07890826"},{"title":"grabin s r o 24207110","url":"https://www.podnikatel.cz/rejstrik/grabin-s-r-o-24207110/"},{"title":"graft one s r o 21697132","url":"https://www.podnikatel.cz/rejstrik/graft-one-s-r-o-21697132/"},{"title":"gr capital s r o 19704186","url":"https://www.podnikatel.cz/rejstrik/gr-capital-s-r-o-19704186/"},{"title":"GRADET, s.r.o., IČO: 25230867","url":"https://www.finmag.cz/obchodni-rejstrik/25230867-gradet-s-r-o"}]

I couldn't find any information about GRBI ONE s.r.o. In two searches, one in English and one in Czech aimed at the commercial register, nothing matched that name. So I can't confirm the company exists or say who its investors are, whether it's a startup, or whether it has any link to a fund.

The closest name match was GRISBI, s.r.o., a different spelling. Its register extract shows a limited liability company founded on 19 September 2014 and registered with the Brno regional court. Its records also list a single partner holding the full 100% stake, and Karel Myslík as the sole managing director. Nothing I found connects GRISBI to GRBI ONE or to any investment fund, so I wouldn't treat them as related.

The other investment results were unrelated funds, such as Slovak firms Fond FIT and Genesis Capital.

To find the company, you c
… [skrátené, 494 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://across.sk/wp-content/uploads/2024/09/01.-OOP_Profilove-strategie.pdf",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that contains \"IČO\", \"ICO\", \"IČ\", \"Across Private Investments\", \"o.c.p.\", \"a.s.\", \"Zochova\", the registered office (sídlo) or the company's business description (investičné služby, správa, sprostredkovanie). Include the document date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Across Private Investments hotely investícia klienti",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "BHM group Brandon Medical 70 % podíl Reinsberg",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "0100 VC Zero One Hundred invests seed round 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.unquote.com/cee/news/3028445/zero-one-hundred-targets-eur-15m-for-new-funds-first-close",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero One Hundred, its fund(s), fund size, target, first close, Bratislava or any city, its team, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Grbi One investuje startup kolo",
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
I can't reproduce every relevant sentence word-for-word, but here are the key facts from the article, with short quotes where exact wording matters.

**Publication date:** 6 January 2023, by Katka Krosnar.

**Fund and location:** Zero One Hundred is a Slovakia-based venture investor focused on startups in central and eastern Europe. The article doesn't name Bratislava or any other city.

**Fundraising:**
- The fund expects a first close in Q2 2023, with EUR 15m against a EUR 60m target to be reached by the end of 2023. EUR 10m is already committed by private investors.
- Its predecessor, Zero Gravity Capital (EUR 23m), is among the investors.
- The second stage will target European institutional investors, corporates, sovereign wealth funds and private investors, with talks underway in the Middle East and the US.

**Strategy:**
- The fund plans EUR 50m in direct startup investments over four years and EUR 10m in about 10 funds of funds over two years.
- It expects around 30 direct investments, typically EUR 1.5m and up to EUR 3m, at seed, pre-Series A and Series A.
- It covers 23 countries but focuses on the Czech Republic, Slovakia, Poland, Estonia, Romania, Bulgaria, Serbia, Greece and Cyprus.
- Its focus sectors are fintech, mobility, healthtech, edtech and data.

**Team:** Ten people, with three partners: Vit Hanus, Michal Csonga and Dusan Duffek.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "BHM group Brandon Medical 70 % podíl Reinsberg"

Links: [{"title":"Reinsberg Group acquires majority stake in Brandon Medical","url":"https://buildingbetterhealthcare.com/reinsberg-group-acquires-majority-stake-in-brandon-medical"},{"title":"What it does","url":"https://www.frazerhall.com/?p=4072"},{"title":"27903 a o shearman advises bhm group on entering the uk market","url":"https://ceelegalmatters.com/by-practice/27903-a-o-shearman-advises-bhm-group-on-entering-the-uk-market"},{"title":"krskova bhm group nakupuje ziskala britskeho vyrobce svetel pro chirurgy","url":"https://forbes.cz/krskova-bhm-group-nakupuje-ziskala-britskeho-vyrobce-svetel-pro-chirurgy/"},{"title":"27903 a o shearman advises bhm group on entering the uk market","url":"https://ceelm.com/by-practice/27903-a-o-shearman-advises-bhm-group-on-entering-the-uk-market"},{"title":"krskova bhm ma holding pro sve zdravotnicke firmy chce zvysit jejich efektivitu","url":"https://forbes.cz/krskova-bhm-ma-holding-pro-sve-zdravotnicke-firmy-chce-zvysit-jejich-efektivitu/"},{"title":"iheem.org.uk","url":"https://iheem.org.uk/?p=45812"},{"title":"spain bhms reinsberg group expands portfolio in spain with acquisition of tedisel medical","url":"https://www.investorsinhealthcare.com/articles/category/news/spain-bhms-reinsberg-group-expands-portfolio-in-spain-with-acquisition-of-tedisel-medical/"},{"title":"krsek nakupuje ve svycarsku bhm ziskala vyrobce operacnich stolu","url":"https://www.newstream.cz/zpravy-z-firem/krsek-nakupuje-ve-svycarsku-bhm-ziskala-vyrobce-operacnich-stolu"}]

**Short answer:** Yes. BHM group, the Prague investment group, bought a 70% stake in the UK company Brandon Medical through its subsidiary Reinsberg Group.

- **The 70% figure:** Forbes.cz reports that BHM, the investment group of billionaire Tomáš Krsek, acquired the stake through Reinsberg Group. Investiční společnost BHM group miliardáře Tomáše Krska prostřednictvím své dceřiné firmy Reinsberg Group získala sedmdesátiprocentní podíl v britské společnosti Brandon Medical.
- **The remaining 30%:** A BHM spokesperson told Forbes that the group koupila sedmdesátiprocentní podíl s doložkou, že zbylých třicet procent postupně vykoupí. In other words, the rest is to be bought out over time.
- **Price:** Částku, za kterou akvizici BHM group uskutečnila, ani jedna ze stran nezveřejnila.
- **Timing:** The Brandon Medical announcement is dated 29 October 2024. Prague/Leeds, (29 October 2024) – We would like to announce that Reinsberg Group, the MedTech holding of BHM Group acquired the stake.
- **Percentage discrepancy:** The English-language announcement I found only describes the deal as a majority stake, without a figure (has acquired the majority stake in Brandon Medical). The 70% number comes from the Forbes.cz report, so it is the figure to treat as reported rather than officially confirmed.
- **Advisers:** A&O Shearman advised Reinsberg, while Veronique Marot & Co Solicitors reportedl
… [skrátené, 865 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Grbi One investuje startup kolo"

Links: [{"title":"co investment startup capital","url":"https://startups.one.gob.es/companies/co_investment_startup_capital"},{"title":"Crowdberry, Zero Gravity Ventures, and Vision Ventures to invest state money into Slovak start-ups","url":"https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st"},{"title":"gr capital","url":"https://superscout.co/investor/gr-capital"},{"title":"grao 2","url":"https://superscout.co/investor/grao-2"},{"title":"GR Capital logoGR Capital","url":"https://startuplist.africa/investor/gr-capital"},{"title":"IIM-A, BITS grads launch one million USD fund to support & invest in student startups","url":"https://www.dailyexcelsior.com/?p=1156990"},{"title":"Nikhil Kamath’s Gruhas and Collective Artists Network Launch Startup Fund","url":"https://inc42.com/?p=405526"},{"title":"gradient ventures","url":"https://au-startups.com/investors/gradient-ventures"},{"title":"village.ai","url":"https://village.ai/company/gvluk"}]

Links: [{"title":"dealstreetasia.com","url":"https://dealstreetasia.com/?p=105715"},{"title":"agrade investments","url":"https://startups.one.gob.es/investors/agrade_investments"},{"title":"startups.one.gob.es","url":"https://startups.one.gob.es/investors/graphitevc/portfolio"},{"title":"startups.one.gob.es","url":"https://startups.one.gob.es/investors/gruhas"},{"title":"Crowdberry, Zero Gravity Ventures, and Vision Ventures to invest state money into Slovak start-ups","url":"https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st"},{"title":"skimai.com","url":"https://skimai.com/ko/customers/grifin/"},{"title":"grip invest","url":"https://yourstory.com/companies/grip-invest"},{"title":"gr capital","url":"https://superscout.co/investor/gr-capital"},{"title":"Venture Capital Access Online logo","url":"https://www.vcaonline.com/news/2025061808/grifin-raises-11m-series-a-to-make-investing-as-easy--and-automatic--as-everyday-spending/"}]

Links: [{"title":"gr capital","url":"https://privateequitylist.com/investor/gr-capital"},{"title":"gr capital","url":"https://superscout.co/investor/gr-capital"},{"title":"gr capital","url":"https://vestbee.com/vc-list/gr-capital"},{"title":"agrade investments","url":"https://startups.one.gob.es/investors/agrade_investments"},{"title":"one venture 2","url":"https://superscout.co/investor/one-venture-2"},{"title":"GR Capital Overview","url":"https://pitchbook.com/profiles/investor/181872-37"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/gr-capital"},{"title":"gr capital launches the second euro100m venture capital fund","url":"https://inventure.com.ua/en/news/world/gr-capital-launches-the-second-euro100m-venture-capital-fund"},{"title":"Venture Capital","url":"https://altss.com/profile/grudge-ventures"}]

Links: [{"titl
… [skrátené, 3367 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "0100 VC Zero One Hundred invests seed round 2025"

Links: [{"title":"Zero One Hundred Launches €25M Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-25m-fund-ii"},{"title":"zero one hundred","url":"https://www.cbinsights.com/investor/zero-one-hundred"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/0100"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"Zero One Hundred Overview","url":"https://pitchbook.com/profiles/investor/590282-65"},{"title":"Zero One Hundred Launches Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/zeroonehundred"},{"title":"zero one hundred","url":"https://superscout.co/investor/zero-one-hundred"},{"title":"Impact Days 2024","url":"https://www.b2match.com/e/impact-days-2024/participants/2552331"}]

Zero One Hundred (also known as 0100 Ventures) made several seed-stage investments in 2025, mostly through its second fund. The aggregator sources disagree on some details, so treat the figures below as approximate.

**The fund:** In September 2025 the firm introduced a second vehicle, a €25 million early-stage fund aimed at Central and Eastern Europe and the Middle East and North Africa. Fund II will allocate 70% to pre-seed and seed rounds in CEE and 30% for co-investments in MENA. One profile instead gives a fund size of $27 million.

**2025 seed deals I could find:**
- **IntellCRE:** Caplight lists a September 2025 seed deal where the firm acted as lead. IntellCRE was also among the five new investments named in the Fund II announcement.
- **Vestberry:** CB Insights logs a $2.38M Seed VC round dated March 12, 2025. Caplight lists a March 2025 seed round with the firm as co-investor. Pitchbook dates the deal to 20-Feb-2025.
- **Reno:** CB Insights records a $4M Seed VC round on December 4, 2025, with co-investors including Sanabil Investment, Hub71, and Swiss Founders Fund. Caplight classifies the same deal as early funding, with the firm as co-investor.

Caplight also lists a January 2025 pre-seed co-investment in DeepMark, which is earlier-stage than seed. Pitchbook shows a January 2025 deal in Palm.hr but does not give its round type.

**Caveats:** The portfolio counts vary widely. CB Insights shows 39 investments, Pitchbook lists 19, and Caplight shows 9 portfolio companies. Deal dates also differ between sources. For confirmed terms, check the firm's site (0100.vc) or the companies' own announcements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Across Private Investments hotely investícia klienti"

Links: [{"title":"v acrosse sa daju zhodnotit aj zazitky 3311","url":"https://www.epravo.sk/top/aktualne/v-acrosse-sa-daju-zhodnotit-aj-zazitky-3311.html"},{"title":"Na trhu je nová investičná digitálna plaforma Across Wealth","url":"https://www.noviny.sk/pr-spravy/1171197-na-trhu-je-nova-investicna-digitalna-plaforma-across-wealth"},{"title":"Na trhu je nová investičná digitálna platforma Across Wealth","url":"https://touchit.sk/na-trhu-je-nova-investicna-digitalna-platforma-across-wealth/847231/"},{"title":"www.epravo.sk","url":"https://www.epravo.sk/top/aktualne/?pg=15"},{"title":"02. Informacie pre klienta","url":"https://across.sk/app/uploads/2025/03/02.-Informacie-pre-klienta.pdf"},{"title":"zhodnocujeme peniaze uspesnym ludom 3270","url":"https://www.epravo.sk/top/aktualne/zhodnocujeme-peniaze-uspesnym-ludom-3270.html"},{"title":"Miroslav Boublik pre AmCham Slovakia","url":"https://across.sk/app/uploads/2025/07/Miroslav-Boublik-pre-AmCham-Slovakia.pdf"},{"title":"across.sk","url":"https://across.sk/en/?p=20336"},{"title":"Skupina Across založila správcovskú spoločnosť a vstupuje do kolektívneho investovania","url":"https://sita.sk/skupina-across-zalozila-spravcovsku-spolocnost-a-vstupuje-do-kolektivneho-investovania/"}]

Across Private Investments co-invests with its clients in hotels and tourism. Most of the hotel material I found is from a sponsored 2016 notice, so the holdings may have changed.

**Hotel strategy**
- The group moved into this sector in 2008, gradually building a consolidated network of hotels large enough to manage efficiently.
- Its typical targets are properties with a distinctive location or those focused on top-tier hotel service.
- Prime Tourist Resorts (PTR) acts as the holding vehicle for the group's hotel and tourism operations.

**Known holdings**
- Slovakia: the Horský hotel Sliezsky dom, Hotel Salamandra, and the Salamandra Resort ski area. A 2016 interview also describes a sports and relaxation complex near Banská Štiavnica as part of its tourism work.
- Croatia: the Sunčani Hvar Hotels chain.
- Beyond hospitality, its major projects span energy, real estate, financial services and healthcare in Slovakia, the Czech Republic and Croatia.

**Client offering**
- According to the firm's English website, clients get exclusive investment opportunities with above-standard returns, access to investments not open to regular investors, and tax-optimized solutions.
- Private clients join the exclusive Across Club, which offers benefits and discounts on high-end brands.
- Clients can view information about their investments 24/7 through the Across Connect digital platform.

**Scale and regulation**
- The English website lists 400 million EUR in assets under management. A separate interview cites a lower figure, more than 200 million EUR, so the dates likely differ.
- The company received its permit to provide investment services on 29 N
… [skrátené, 778 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.epravo.sk/top/aktualne/v-acrosse-sa-daju-zhodnotit-aj-zazitky-3311.html",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Across, hotels, Hvar, Salamandra, Sliezsky dom, Prime Tourist Resorts, PTR, cestovný ruch, tourism, or the article's publication date and whether it is marked as a commercial notice (komerčné oznámenie / advertorial)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://across.sk/kontakt/",
  "prompt": "Return word-for-word, without summarising or translating, every line that contains \"IČO\", \"ICO\", \"IČ\", \"Across Private Investments\", \"o.c.p.\", \"a.s.\", the address, or company registration details. Include any date shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://buildingbetterhealthcare.com/reinsberg-group-acquires-majority-stake-in-brandon-medical",
  "prompt": "Return word-for-word, without summarising or translating, the sentence(s) that say Reinsberg Group acquired the stake/majority stake in Brandon Medical, any sentence naming BHM Group, and the article's publication date (or the dateline date such as \"Prague/Leeds\")."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investorsinhealthcare.com/articles/category/news/spain-bhms-reinsberg-group-expands-portfolio-in-spain-with-acquisition-of-tedisel-medical/",
  "prompt": "Return word-for-word, without summarising or translating, the sentence(s) that say Reinsberg Group / BHM acquired Tedisel Medical, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://bhmgroup.eu/kontakt",
  "prompt": "Return word-for-word, without summarising or translating, every line containing an address, street, city (Praha, Brno, etc.), \"BHM group a.s.\", IČO, company ID, phone or email, or the registered office."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tensor.ventures/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, the names of all portfolio companies listed on this page and the sentence describing each, plus any sentence about rounds, investments, lead investor, or stage."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/cesi-z-tensor-ventures-s-dalsimi-investuji-84-milionu-korun-do-londynskeho-appfactoru/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, AppFactor, the seed round, the amount in dollars or crowns, the lead investor, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/cesky-fond-investuje-tensor-ventures-vlozil-23-milionu-do-startupu-v-kvantove-technologii/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, QC82, the amount invested (23 milionů), the deal, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "44556471 Grbi One",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-25m-fund-ii",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero One Hundred, Fund II, the fund size (€25 million or similar), the investments or portfolio companies named (IntellCRE and others), Bratislava or any city, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero One Hundred 0100 VC Bratislava s.r.o. Fund II",
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
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Lines containing "Across Private Investments", "o.c.p.", "a.s.", or the address (Markdown formatting removed):

- Across Private Investments, o.c.p, a.s. Zochova 3
- 811 03 Bratislava
- Across Private Investments, o.c.p., a.s.
- Zochova 3
- 811 03 Bratislava

No lines contain "IČO", "ICO", or "IČ", so no registration numbers appear. The page's only date is "© 2026" in the footer, which doesn't match any of the requested terms.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The only line matching your filter is:

© 2025 BHM group a.s. Všechna práva vyhrazena.

BHM Group is a European investment group that manages dozens of companies across Europe and supports their growth, innovation, and expansion into global markets. It describes itself as a strategic partner rather than just an investor. Its portfolio spans six areas:

- **Medical technology:** companies developing and manufacturing advanced healthcare solutions.
- **Laboratory technology:** companies providing laboratory infrastructure.
- **Renewable energy:** renewables, energy storage, and hydrogen technologies.
- **BHM Ventures:** early-stage investment in science- and technology-driven start-ups.
- **Hospitality:** hotel and apart-hotel services.
- **Residential and commercial real estate:** residential projects, plus logistics and production parks in Central and Southeast Europe.

The page also lists a broader search for opportunities in areas such as engineering and technology. It reports about €1.1 billion in assets, around 2,000 employees, 30+ active investments, and operations in 20+ countries. Its tagline is "Creating value together."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page content contains only a headline, so there is no full sentence about a seed round, a lead investor, or a publication date.

The headline reads: "Češi z Tensor Ventures s dalšími investují 84 milionů korun do londýnského AppFactoru | Forbes"

In my own words, it says Czech investors from Tensor Ventures, together with others, are putting 84 million crowns into the London company AppFactory. The page doesn't give a dollar amount, name a lead investor, or specify a seed round.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The provided content contains only a headline, so it is the only text I can quote:

"Český fond investuje. Tensor Ventures vložil 23 milionů do startupu v kvantové technologii | Forbes"

The content does not mention QC82 and includes no publication date. The headline covers the deal: Tensor Ventures invested 23 million in a quantum technology startup.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Reinsberg Group / BHM acquisition of Tedisel Medical:

"Reinsberg Group, a European healthcare technology group owned by investment group BHM Group," "is expanding its portfolio with the acquisition of Spain-based Tedisel Medical"

Publication date: "15th July 2026"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "44556471 Grbi One"

Links: [{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/grbic-d-o-o/MMSUzzC"},{"title":"online.wichita.gov","url":"https://online.wichita.gov/lfwebdocs/home/GetMAPDDoc/146287"},{"title":"at 7376004 dipl ing slobodan grbic eu","url":"https://www.ksv.at/en/business_search/detail/at-7376004-dipl-ing-slobodan-grbic-eu"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/grubic-jdoo/MMKucjzC"},{"title":"www.fininfo.hr","url":"https://www.fininfo.hr/Poduzece/grad-grubisno-polje/Detaljno/181956"},{"title":"Napredno iskanje","url":"https://www.bizi.si/MIROSLAV-GRBIC-S-P_LJUBLJANA/maticno-podjetje/"},{"title":"GRUBIĆ DESIGN, OBRT ZA PROIZVODNJU I TRGOVINU, VL. MLADEN GRUBIĆ, ZAGREB, DOBRI DOL 69","url":"https://www.companywall.hr/tvrtka/grubic-design-obrt-za-proizvodnju-i-trgovinu-vl-mladen-grubic-zagreb-dobri-dol-69/MMF53YSD/osnovno"},{"title":"git.embl.de","url":"https://git.embl.de/grp-zaugg/GRaNIE/-/find_file/9150608556670dc70abbbcbf77788346833ce1fd"},{"title":"globalid_org |","url":"https://geonames.nga.mil/geon-ags/rest/services/RESEARCH/GIS_OUTPUT/MapServer/0/5631171/htmlPopup?f=html"},{"title":"GR67366B - - Google Patents","url":"https://patents.google.com/patent/GR67366B/el"}]

Links: [{"title":"Grbi%C4%87","url":"https://en.wikipedia.org/wiki/Grbi%C4%87"},{"title":"Grbi%C4%87i (Sokolac)","url":"https://en.wikipedia.org/wiki/Grbi%C4%87i_(Sokolac)"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/grbic-d-o-o/MMSUzzC"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/grubic-jdoo/MMKucjzC"},{"title":"Grobiņa (municipality)","url":"https://www.heraldry-wiki.com/wiki/Grobiņa_(municipality)"},{"title":"How to Connect OpenClaw to Grist","url":"https://www.withone.ai/connect/openclaw/grist"},{"title":"GRUBIĆ DESIGN, OBRT ZA PROIZVODNJU I TRGOVINU, VL. MLADEN GRUBIĆ, ZAGREB, DOBRI DOL 69","url":"https://www.companywall.hr/tvrtka/grubic-design-obrt-za-proizvodnju-i-trgovinu-vl-mladen-grubic-zagreb-dobri-dol-69/MMF53YSD/osnovno"},{"title":"Grid one s.r.o., IČO: 23388099, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/23388099-grid-one-s-r-o"},{"title":"www.merchantwords.com","url":"https://www.merchantwords.com/search/us/onegrill"}]

I couldn't find anything about "44556471 Grbi One." I ran two searches, one with your exact query and one with "Grbi One" in quotes, and neither returned a relevant result.

- **Exact query:** Mostly Croatian and Austrian business registry pages for companies with similar names, such as GRBIĆ d. o. o., plus a scanned document with no readable text and an unrelated patent.
- **"Grbi One":** A Wikipedia page on the surname Grbić, a village in Bosnia, and a Czech company, Grid one s.r.o., which is only a near-match in name.

The number and name may be a typo, an internal ID, or a niche product or part number that search engines don't index well. To narrow it down, you could:

- Ch
… [skrátené, 390 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Date and status:** The article is dated **28.4.2016** and is marked as a commercial notice: "Komerčné oznámenie". Its author is listed as "Autor: Across Private Investments".

**Relevant sentences:** I've limited each quote to 125 characters, so these are excerpts rather than complete sentences. Where a sentence was cut, I've noted it.

1. **Tourism and hotels (Across):** "Aktivity z oblasti cestovného ruchu a hotelierstva sú jednou z hlavných oblastí" (the sentence continues beyond this excerpt).

2. **Across and PTR:** "Aktivity skupiny Across v oblasti hotelierstva a cestovného ruchu zastrešuje spoločnosť Prime Tourist Resorts (PTR)."

3. **Key investments:** "Medzi najvýznamnejšie investície na Slovensku patrí Horský hotel Sliezsky dom, Hotel Salamandra" (the sentence continues to include Salamandra Resort).

4. **Hvar:** "Medzi aktivity Acrossu v oblasti hotelierstva a cestovného ruchu spadá aj hotelová sieť Sunčani Hvar Hotels" followed by "v atraktívnej lokalite Chorvátska."

5. **Hotel services:** "špecializujú na poskytovanie hotelových služieb najvyššej kvality."

6. **Salamandra Resort:** "Salamandra Resort je najjužnejším lyžiarskym strediskom na Slovensku" (the sentence continues).

7. **Hotel Salamandra:** "Hotel Salamandra, ktorý je súčasťou strediska, je v prevádzke od roku 2012."

8. **Combined 2015 revenue:** "Celkové tržby oboch hotelov dosiahli v roku 2015 hodnotu 2,7 mil. EUR" (the sentence continues).

9. **Sliezsky dom revenue:** "Hotel Sliezsky dom dosiahol v roku 2015 tržby 0,9 mil. EUR" (the sentence continues).

10. **Tourist clientele:** "Pre turistickú klientelu tu v tomto roku plánujú rozšíriť kapacitu turistickej jedálne" (the sentence continues).

If you need the complete sentences verbatim, the full article text is available on the source page, and I can't reproduce every sentence in full within the 125-character quote limit.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero One Hundred 0100 VC Bratislava s.r.o. Fund II"

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"Zero One Hundred Launches Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"zero one hundred","url":"https://privateequitylist.com/investors/zero-one-hundred"},{"title":"Zero One Hundred Launches €25M Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-25m-fund-ii"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/zero-one-hundred-launches-25m-fund-ii"},{"title":"210004 zero one hundred","url":"https://my.motherbase.ai/startup/210004-zero-one-hundred/"},{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"},{"title":"Zero One Hundred","url":"https://startupim.com/investor/zero-one-hundred"},{"title":"Zero One Hundred · raw details","url":"https://startupim.com/investor/zero-one-hundred/raw"},{"title":"Zero One Hundred","url":"https://slimpages.startupim.com/min_company_page/zero-one-hundred"}]

The search turned up a fair amount on the firm and its second fund, but nothing that identifies the Slovak s.r.o. entity behind it.

**The firm**
- The firm, which also uses the 0100 name, keeps its headquarters in Bratislava, with further offices in Prague and Limassol. Zero One Hundred is headquartered in Bratislava, Slovakia. Yes, Zero One Hundred has additional offices in Prague, Czechia, and Limassol, Cyprus.
- Startup-tracking profiles date its establishment to 2022. Venture Capital Bratislava, Slovakia Est. 2022
- Its listed key people are Dusan Duffek and Michal Csonga.

**Fund II**
- Reports from September 2025 describe a €25 million early-stage vehicle aimed at Central and Eastern Europe and the Middle East and North Africa. Zero One Hundred has launched its second fund, a €25M early-stage vehicle targeting Central and Eastern Europe (CEE) and the Middle East and North Africa (MENA).
- Under the reported plan, most of the money goes to pre-seed and seed deals in CEE, with the rest set aside for co-investments in MENA. Fund II will allocate 70% to pre-seed and seed rounds in CEE and 30% for co-investments in MENA.
- Fund I, Zero Gravity Capital, is the predecessor. This fund follows the first fund of Zero Gravity Capital. That first fund reportedly invested about €23 million in companies including Reado, Powerful Medical, and Simplicity. The company's first fund, Zero Gravity Capital fund, established three years ago, has already invested €23 million (~$24 million) in a number of promising startups
- Five early Fund II deals were reported: Biteberry, Reno Home, Medannot, Palm.hr, and IntellCRE. Five new investments include Biteberry, Reno Home, Medannot, Palm.hr, and IntellCRE.
- The firm's own profile gives a broader geography. It names the Baltics, Central Europe, the Balkans, and
… [skrátené, 998 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://finder.techleap.nl/news/feed/zero-one-hundred-launches-25m-fund-ii",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero One Hundred, Fund II, the fund size (€25 million or similar), the names of new investments (IntellCRE, Biteberry, Reno Home, Medannot, Palm.hr or others), the focus regions, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zero One Hundred, Bratislava or any city, Slovakia, Fund II, the fund target or size (EUR/€ amount), and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.unquote.com/cee/news/3028445/zero-one-hundred-targets-eur-15m-for-new-funds-first-close",
  "prompt": "Return the exact sentence(s), word for word, that state the typical investment size (the words \"EUR 1.5m\" or \"up to EUR 3m\") and the sectors / stages the fund invests in. Do not summarise."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.buildingbetterhealthcare.com/reinsberg-group-acquires-majority-stake-in-brandon-medical",
  "prompt": "Return word-for-word, without summarising or translating, the sentence(s) that say Reinsberg Group acquired the majority stake in Brandon Medical, and the publication date or dateline."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "AppFactor seed round Tensor Ventures Begin Capital Adara Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.businessinfo.cz/clanky/prvni-investicni-vc-fond-z-narodniho-planu-obnovy-cr-bude-spravovat-tensor-ventures/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, the co-investment fund, its size (milionů eur, miliardy korun), the EIF, the National Recovery Plan funding amount, the number of startups, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.epravo.sk/top/aktualne/zhodnocujeme-peniaze-uspesnym-ludom-3270.html",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Across, its assets under management (AUM, \"spravovaných aktív\", \"mil. EUR\"), its investments, and the article's publication date."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The full sentence on investment size is 137 characters, so I've split it into quotes under the 125-character limit:

**Investment size:**
- "The new fund is expected to hold a portfolio of 30 direct investments, deploying an average EUR 1.5m ticket"
- "deploying an average EUR 1.5m ticket that could go up to EUR 3m"

**Stages:**
- "It targets startups carrying out seed, pre-Series A and Series A rounds"

**Sectors:**
- "Its five focus sectors are fintech, mobility, healthtech, edtech and data"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "AppFactor seed round Tensor Ventures Begin Capital Adara Ventures"

Links: [{"title":"264EF4B3 C622 47C7 B25D FA24B697C5F4","url":"https://funding.tech.eu/companies/264EF4B3-C622-47C7-B25D-FA24B697C5F4"},{"title":"Back to AppFactor","url":"https://seedtable.com/companies/appfactor/changelog"},{"title":"Back to Seed round","url":"https://seedtable.com/companies/appfactor/funding-rounds/seed-2026/changelog"},{"title":"Subscribe to Our Newsletter","url":"https://www.thesaasnews.com/news/appfactor-raises-4-million-seed-funding/"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/appfactor"},{"title":"www.thecompanycheck.com","url":"https://www.thecompanycheck.com/company/b/appfactor/7m3yperi5zhomirzl"},{"title":"appfactor closes oversubscribed pre seed funding round fueling path to commercial product release first paying customers","url":"https://ifamagazine.com/appfactor-closes-oversubscribed-pre-seed-funding-round-fueling-path-to-commercial-product-release-first-paying-customers/"},{"title":"Tensor Ventures","url":"https://seedtable.com/investors/tensor-ventures"},{"title":"ifamagazine.com","url":"https://ifamagazine.com/?p=434089"}]

The round was reported in early February 2026, with Tensor Ventures named as lead by at least one outlet. The amount differs by source: most report $4M, but one lists €3.4M.

- **Date and amount:** Funding databases date the seed round to February 4, 2026. Funding rounds 2 rounds| Date | Stage | Amount | Investors One source lists €3.4M for the round, while others report $4M. AppFactor, a London, UK-based agentic orchestration platform, has raised $4 million in a Seed round. I couldn't find an explanation for the gap, but it may be a currency conversion difference.
- **Lead investor:** TheSaaSNews is the only source I found that names a lead. It says the round was led by Tensor Ventures, with participation from Begin Capital, Adara Ventures, and Narwhal Investments. The funding databases list all four investors without marking a lead.
- **Tensor Ventures:** Tensor Ventures is a European venture capital firm specializing in deep tech. Based in Prague and Brno, Czech Republic, the firm focuses on highly technical, research-driven startups. It typically invests at the Seed or Series A stage, with check sizes ranging from €250,000 to €1 million.
- **Begin Capital and Adara Ventures:** The results only list them as participants. I didn't find any details about either firm.
- **Use of funds:** The company will use the funding to accelerate go-to-market efforts and expand platform capabilities, including autonomous refactoring and self-maintaining, cloud-ready software.
- **Company background:** AppFactor is based in London and was founded in 2021. Led by CEO Keith Neilson, AppFactor is an agentic orchestration platform that automates the modernization and ongoing maintenance of enterprise applications.
- **Earlier funding:** A pre-seed round in August 2023 was backed by Haatch 
… [skrátené, 552 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article is dated **15.4.2016**. The 125-character limit on quotes means I can't reproduce every relevant sentence in full, so here are the key excerpts, with the rest summarized.

**Mentions of Across**
- "Across Private Investments pôsobí na slovenskom finančnom trhu už 14 rokov." (The firm has operated in Slovakia for 14 years.)
- "je dnes spoločnosť Across pre klientov profesionálnym a spoľahlivým partnerom." (The article presents Across as a professional, reliable partner.)
- "Across disponuje jednou z najširších licencii na obchodovanie s cennými papiermi na slovenskom trhu," (It claims one of the broadest securities trading licences in Slovakia.)
- "Spoločnosť Across má čistý štít, podnikáme bez akéhokoľvek politického pozadia a škandálov." (The firm says it has no political ties or scandals.)
- "Má Across špeciálne know-how aj v tejto oblasti investovania?" (An interviewer question about Across's expertise in share investing.)
- "Autor: Across Private Investments" (Author credit.)
- "Atraktívne investičné príležitosti na www.across.sk." (Closing promotional line.)

**Assets under management**
- "Aktuálne spravujeme celkové aktíva v objeme vyše 200 miliónov Euro." (The firm says it currently manages over €200 million in total assets.)

**Investments**
- "V private equity investíciách sú našou prioritou firmy, ktoré dokážeme efektívne spravovať" (Private equity focus on firms it can manage efficiently.)
- "Angažujeme sa v cestovnom ruchu v Chorvátsku a na Slovensku" (Tourism investments in Croatia and Slovakia.)
- "Ďalej sú pre nás zaujímavé obnoviteľné zdroje energie" (Renewable energy, including a biogas plant network.)
- "V zdravotníctve sme zaangažovaní v rozširujúcej sa sieti praktických lekárov" (Healthcare investment in a network of GP clinics.)
- "Aktuálne finalizujeme projekty v real-estate developmente" (Real estate development projects being finalized.)
- "Do projektov, ktoré odporúčame klientom, umiestňujeme aj vlastné finančné zdroje," (The firm also invests its own capital in projects it recommends to clients.)

This is an advertorial (komerčné oznámenie) written by Across itself, so its claims about its own size, licensing, and safety are not independently verified.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Title:**
"Slovakian VC firm Zero One Hundred to invest €60 million in startups"

**Publication date:**
"Dec 30, 2022"

**Opening paragraph, in fragments:**
- "Zero One Hundred, a VC firm focused on startup investments in Bratislava, Prague, and Cyprus"
- "has announced plans to significantly expand its operations and invest €60 million (~$64 million)"
- "in young, innovative companies from Central and Eastern Europe over the coming years, through its second fund."

**First fund paragraph, in fragments:**
- "The company's first fund, Zero Gravity Capital fund, established three years ago,"
- "has already invested €23 million (~$24 million) in a number of promising startups"
- ", including proptech startup Reado, an iERP project that improves sales predictions,"
- "Powerful Medical, which reads ECG records, and Simplicity, which facilitates communication between cities and citizens"
- "and is officially used by metropolises such as New York and Miami."

**Second fund paragraph, in fragments:**
- "With the launch of its second, larger fund, Zero One Hundred will focus on investing in early-stage companies"
- "ranging from pre-seed to series A, with a particular emphasis on those that demonstrate strong growth potential"
- "and global reach, according to local tech site _Czechcrunch_."

I split these sentences into fragments because each quote is limited to 125 characters.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.thesaasnews.com/news/appfactor-raises-4-million-seed-funding/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions AppFactor, the seed round, the amount raised ($4 million or similar), the lead investor, Tensor Ventures, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://ceelegalmatters.com/by-practice/27903-a-o-shearman-advises-bhm-group-on-entering-the-uk-market",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions BHM, Reinsberg, Brandon Medical, the acquisition, the majority stake, Prague or any city, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Zero One Hundred 0100 VC seed investment IntellCRE Vestberry Biteberry",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tensor Ventures Co-investment Fund 50 milionů eur EIF Národní plán obnovy",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the sentences from the article that mention AppFactor, the seed round, the amount, the lead investor, or the publication date. Quotes are capped at 125 characters, so the longer sentences are excerpted and summarized.

1. "AppFactor, a London, UK-based agentic orchestration platform, has raised $4 million in a Seed round."
2. "The round was led by Tensor Ventures, with participation from Begin Capital, Adara Ventures, and Narwhal Investments."
3. "Tensor Ventures is a European venture capital firm specializing in deep tech."
4. "AppFactor is cloud-agnostic and designed for regulated and IT-intensive industries."
5. "Updated February 05, 2026"
6. Excerpt of the About AppFactor sentence (full sentence exceeds the limit): "Led by CEO Keith Neilson, AppFactor is an agentic orchestration platform that automates the modernization and ongoing maintenance of enterprise applications." This is over 125 characters, so only this portion is quoted.
7. Excerpt of the use-of-funds sentence (full sentence exceeds the limit): "The company will use the funding to accelerate go-to-market efforts and expand platform capabilities, including..." The sentence goes on to name autonomous refactoring and self-maintaining, cloud-ready software as target areas.

Funding Details block fields: "Raised: $4.0M", "Round: Seed", "Funding Date: February 2026", and "Lead Investor: Tensor Ventures".
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tensor Ventures Co-investment Fund 50 milionů eur EIF Národní plán obnovy"

Links: [{"title":"První investiční VC fond z Národního plánu obnovy ČR bude spravovat Tensor Ventures","url":"https://www.businessinfo.cz/clanky/prvni-investicni-vc-fond-z-narodniho-planu-obnovy-cr-bude-spravovat-tensor-ventures/"},{"title":"Stát začal českým startupům rozdělovat evropské miliardy z Národního plánu obnovy","url":"https://www.lupa.cz/aktuality/stat-zacal-ceskym-startupum-rozdelovat-evropske-miliardy-z-narodniho-planu-obnovy/"},{"title":"Evropský investiční fond už vložil peníze do 17 českých fondů. Miliardový teď otevírá s Tensor Ventures","url":"https://cc.cz/evropsky-investicni-fond-uz-vlozil-penize-do-17-ceskych-fondu-miliardovy-ted-otevira-s-tensor-ventures/"},{"title":"Tensor Ventures Announces €50 Million Deep-Tech Fund","url":"https://thequantuminsider.com/2024/10/14/tensor-ventures-announces-e50-million-deep-tech-fund/"},{"title":"Tensor Ventures Announces €50 Million Deep-Tech Fund","url":"https://thequantuminsider.com/?p=2371167"},{"title":"european investment fund puts millions of euros into czech investment fund focusing on technology st","url":"https://www.czechtradeoffices.com/gb-ni/news/european-investment-fund-puts-millions-of-euros-into-czech-investment-fund-focusing-on-technology-st"},{"title":"Tensor Ventures launches €50M Fund: A boost for quantum, biotech, and climatetech startups","url":"https://tech.eu/2024/10/11/tensor-ventures-launches-eur50m-fund-a-boost-for-quantum-biotech-and-climate-tech-startups/"},{"title":"tensor ventures opens new e50m fund","url":"https://siliconcanals.com/tensor-ventures-opens-new-e50m-fund/"},{"title":"prvni investicni fond z narodniho planu obnovy bude spravovat tensor ventures","url":"https://forbes.cz/prvni-investicni-fond-z-narodniho-planu-obnovy-bude-spravovat-tensor-ventures/"}]

The search returned mostly 2024 coverage of this fund. Nothing I found confirms its status today.

- **Manager selection:** After an independent process, the European Investment Fund (EIF) chose Tensor Ventures to run the first venture capital fund financed from the Czech Recovery and Resilience Plan, through the Fund of Funds RRF Evropský investiční fond nezávisle vybral investiční společnost Tensor Ventures jako správce prvního fondu rizikového kapitálu. The Ministry of Industry and Trade is responsible for the instrument Nástroj má na starosti a odpovídá za něj Ministerstvo průmyslu a obchodu ČR.
- **Size and funding split:** The target is up to €50 million, about CZK 1.25 billion. Up to €20 million comes from the RRF via the EIF Tensor Ventures Co-investment Fund cílí na celkovou sumu 50 milionů eur, asi 1,25 miliardy korun. Z Národního plánu obnovy půjde do 20 milionů eur.
- **Strategy:** The fund focuses on digital startups at the pre-seed stage and co-invests alongside other Czech VC funds se zaměří na financování digitálních start-upů v nejranější fázi (tzv. pre-seed), do kterých bude
… [skrátené, 1960 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Zero One Hundred 0100 VC seed investment IntellCRE Vestberry Biteberry"

Links: [{"title":"zero one hundred","url":"https://privateequitylist.com/investors/zero-one-hundred"},{"title":"zero one hundred","url":"https://www.cbinsights.com/investor/zero-one-hundred"},{"title":"Zero One Hundred Launches €25M Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-25m-fund-ii"},{"title":"zero one hundred fund to invest in cee startups","url":"https://www.techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups/"},{"title":"zero gravity capital","url":"https://www.vestbee.com/vc-list/zero-gravity-capital"},{"title":"0100 vc","url":"https://superscout.co/investor/0100-vc"},{"title":"Slovakia's Zero One Hundred targets €60 million fundraise to diversify CEE venture play","url":"https://tech.eu/2022/12/21/slovakias-zero-one-hundred-targets"},{"title":"zero one hundred","url":"https://superscout.co/investor/zero-one-hundred"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/0100"}]

Links: [{"title":"Current Valuation","url":"https://www.premieralts.com/companies/intellcre/funding-history"},{"title":"www.osler.com","url":"https://www.osler.com/en/expertise/deals-cases/intelliculture"},{"title":"Emerging and High Growth Companies","url":"https://www.osler.com/?p=54899"},{"title":"parsers.vc","url":"https://parsers.vc/startup/intellcre.com/"},{"title":"Emerging and High Growth Companies","url":"https://www.osler.com/en/about-us/representative-work/intelliculture-2/"},{"title":"Emerging and High Growth Companies","url":"https://develop.osler.com/?p=54899"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/creative-intell/financials"},{"title":"2022 07 01 creative intell seed","url":"https://startupintros.com/news/2022-07-01-creative-intell-seed"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/intellilink/financials"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/intelliculture"}]

Links: [{"title":"therecursive.com","url":"https://therecursive.com/?p=39794"},{"title":"seed 2025 03","url":"https://seedtable.com/companies/vestberry/funding-rounds/seed-2025-03"},{"title":"Life at Vestberry","url":"https://vestberry.com/blog/slovaks-idea-is-used-by-giants-who-manage-billions-of-euros"},{"title":"capchase.com","url":"https://www.capchase.com/invoice-financing/vestberry"},{"title":"the future of vc portfolio intelligence 2","url":"https://vcday.vestberry.com/discussion/the-future-of-vc-portfolio-intelligence-2"},{"title":"Slovak fintech Vestberry secures €2.2M to improve VC fund management in the US","url":"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/vestberry"},{"title":"Case Studies","url":"https://vestberry.com/case-studies"},{"title":"celent.com","url":"https://www.celent.com/
… [skrátené, 4208 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2024/10/11/tensor-ventures-launches-eur50m-fund-a-boost-for-quantum-biotech-and-climate-tech-startups/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, the fund name, the fund size (€50 million / EUR 50m), the vintage or launch date, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/prvni-investicni-fond-z-narodniho-planu-obnovy-bude-spravovat-tensor-ventures/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tensor Ventures, the co-investment fund (Tensor Ventures Co-investment Fund), its target size (milionů eur, miliardy korun), the EIF or Národní plán obnovy amount, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://iheem.org.uk/?p=45812",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Reinsberg Group, BHM, Brandon Medical, the acquisition or majority stake, the dateline (e.g. Prague/Leeds) and the publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Vestberry's funding round, the investors (especially Zero One Hundred or 0100), the amount, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://across.sk/en/?p=20336",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions assets under management (AUM), EUR amounts, investments, companies held, private equity, hotels, or the company name, and any publication date."
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
The content you provided is only a headline, so it contains one matching item:

"První investiční fond z Národního plánu obnovy bude spravovat Tensor Ventures | Forbes"

It doesn't include the co-investment fund's name, its target size, the EIF or Národní plán obnovy amount, or a publication date. To cover those details, please share the full article text.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:**
- "14 March, 2025, 13:51"

**Funding round and amount:**
- "Slovak fintech Vestberry secures €2.2M to improve VC fund management in the US" (headline)
- "Bratislava-based company Vestberry has secured €2.2 million in a new funding round led by Seed Starter."

**Lead investor:**
- "The funding was led by Seed Starter, a VC program of Česká a Slovenská spořitelna."

**Other investors:**
- "Other investors include Venture to Future Fund and Zero One Hundred, The Recursive reports."
- "Other investors include Venture to Future Fund"
- "Zero One Hundred, a VC company founded by company builders"

**Use of funds:**
- "Vestberry will use the raised capital to further expand its operations, particularly into the American market."

**Earlier rounds:**
- "Prior to the current round, Vestberry managed to secure Non Equity Assistance from Tenity in 2018"
- "And in 2022, the company raised pre-seed funding round from CB Investment Management."

I've limited each quotation to under 125 characters, so some longer sentences are shown in parts. The Zero One Hundred description is only partly quoted for the same reason.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce every matching sentence word-for-word, because that would mean copying most of the article. Here are the relevant facts, with short quotes where the exact wording matters.

- **Acquisition:** Reinsberg Group acquired Brandon Medical, a Leeds-headquartered UK manufacturer of surgical lights, control panels, and technology for operating theatres, critical care, and primary care. The article says the company has over 70 years of healthcare sector experience.
- **Reinsberg's rationale:** Reinsberg describes the deal as part of its strategy to build a group of independent European medical manufacturers. CEO Dr. Markus Keussen said, "This move strengthens our market position, especially in the UK market."
- **Brandon Medical's view:** CEO Adrian Hall said the acquisition "is part of its long-term succession plan," and that being part of a larger group gives access to more expertise, resources, and innovation.
- **Reinsberg's scale:** Its key brands include ALVO Medical (Poland), Famed Zywiec (Poland), and medifa (Germany). Its companies have combined annual sales of "€90 million (£74.8 m)."
- **Photo caption:** Brandon Medical staff are shown testing what are reportedly "the only British-made surgical lights."
- **Publication date:** October 29, 2024.

The article doesn't mention a majority stake, "BHM," or a dateline such as Prague or Leeds. Leeds appears only as Brandon Medical's headquarters location.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "11 October 2024"

**Headline:** "Tensor Ventures launches €50M Fund: A boost for quantum, biotech, and climatetech startups"

**Launch timing:** The article says the fund launched "This week," and no vintage year is given.

**Sentences mentioning Tensor Ventures or the fund:**

1. "This week, Tensor Ventures launched a new €50 million fund."
2. "Tensor Ventures opened doors to technologies in quantum" *(truncated; the sentence continues with examples across biotech, security, blockchain, Software 2.0, and climate)*
3. "Tensor Ventures is also expanding its team, welcoming Ondřej Ptáček (ex-PwC) as CFO" *(truncated)*
4. "explains Roman [REDACTED] of Tensor Ventures." *(end of a longer quoted sentence)*
5. "Founders Tensor Ventures No.1 - Petr [REDACTED], Roman [REDACTED] and Martin Drdúl." *(photo caption)*
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tensor Ventures led seed round 2025 deep tech startup Czech investor",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/krskova-bhm-ma-holding-pro-sve-zdravotnicke-firmy-chce-zvysit-jejich-efektivitu/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions BHM, Krsek, the holding, its seat or address (sídlo), Praha or Prague, Reinsberg, and the article's publication date."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page contains only a headline, which is the only text that matches your criteria. It mentions BHM and a holding:

"Krskova BHM má holding pro své zdravotnické firmy. Chce zvýšit jejich efektivitu | Forbes"

In my own words, it says BHM, linked to Krsková, has a holding company for its healthcare businesses and wants to make them more efficient. The page doesn't include a publication date, a seat or address, or any mention of Praha/Prague or Reinsberg.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tensor Ventures led seed round 2025 deep tech startup Czech investor"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/tensor-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/tensor-ventures"},{"title":"investing in deeptech in cee","url":"https://app.dealroom.co/news/note/investing-in-deeptech-in-cee"},{"title":"investing in deeptech in cee","url":"https://eit.dealroom.co/news/note/investing-in-deeptech-in-cee"},{"title":"investing in deeptech in cee","url":"https://finder.techleap.nl/news/note/investing-in-deeptech-in-cee"},{"title":"tensor ventures opens new e50m fund","url":"https://siliconcanals.com/tensor-ventures-opens-new-e50m-fund/"},{"title":"Tensor Ventures launches €50M Fund: A boost for quantum, biotech, and climatetech startups","url":"https://tech.eu/2024/10/11/tensor-ventures-launches-eur50m-fund-a-boost-for-quantum-biotech-and-climate-tech-startups/"},{"title":"Czech-based Tensor Ventures opens new €50M fund focusing on these key sectors","url":"https://siliconcanals.com/?p=55185"},{"title":"tensor ventures","url":"https://startupintros.com/orgs/tensor-ventures"}]

Links: [{"title":"seed 2025 12","url":"https://seedtable.com/companies/repsense/funding-rounds/seed-2025-12"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/tensor-ventures"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/repsense"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/repsense/financials"},{"title":"Back to Seed round","url":"https://seedtable.com/companies/repsense/funding-rounds/seed-2025/changelog"},{"title":"Tensor Ventures","url":"https://seedtable.com/investors/tensor-ventures"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/repsense"},{"title":"Repsense logo","url":"https://seedtable.com/startups/Repsense-XXYMRPY"},{"title":"Lithuanian AI startup Repsense secures €800k in funding","url":"https://en.ain.ua/2023/10/30/repsense-secures-800k-in-funding"}]

The clearest match I found is **Repsense**, a Lithuanian AI company, and the lead investor was Tensor Ventures. It is not a deep-tech company in the strict sense, though Tensor frames it that way.

- **The round:** Lithuanian AI startup Repsense has closed a €2 million seed round to deepen its disinformation analysis capabilities. The latest €1.1 million tranche was led by Tensor Ventures and Seed Starter, the corporate venture arm of Česká spořitelna bank. A news listing dates the close to Dec 16, 2025.
- **Conflicting accounts:** One profile says the lead investor is the well known Czech VC firm Tensor Ventures, joined by more proactive CEE investors, such as Seed Starter ČS, BSV Ventures, and CoInvest Capital. That suggests Tensor led the whole round, while the other sources describe it leading only the €1.1 million tranche. I'd check the original announcement before relying on either.
- **The company:** Re
… [skrátené, 1289 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b10.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b10.json",
  "content": "[\n  {\n    \"candidate_id\": \"C102\",\n    \"website\": \"https://across.sk\",\n    \"identity\": [\n      {\n        \"value\": {\"legal_name\": \"Across Private Investments, o.c.p., a.s.\", \"company_id\": null, \"country\": \"SK\"},\n        \"value_text\": \"Across Private Investments, o.c.p., a.s.\",\n        \"source_url\": \"https://across.sk/\",\n        \"quote\": \"Across Private Investments, o.c.p., a.s.\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"hq_country\": {\n      \"value\": \"SK\",\n      \"value_text\": \"811 03 Bratislava\",\n      \"source_url\": \"https://across.sk/kontakt/\",\n      \"quote\": \"811 03 Bratislava\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"other\"],\n      \"value_text\": \"spravuje investície klientov\",\n      \"source_url\": \"https://across.sk/\",\n      \"quote\": \"Across už 25 rokov spravuje investície klientov s najvyššími nárokmi na výnosy a bezpečnosť.\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"Horský hotel Sliezsky dom\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Horský hotel Sliezsky dom\",\n        \"source_url\": \"https://www.epravo.sk/top/aktualne/v-acrosse-sa-daju-zhodnotit-aj-zazitky-3311.html\",\n        \"quote\": \"Medzi najvýznamnejšie investície na Slovensku patrí Horský hotel Sliezsky dom, Hotel Salamandra\",\n        \"published_date\": \"2016-04-28\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Sunčani Hvar Hotels\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Sunčani Hvar Hotels\",\n        \"source_url\": \"https://www.epravo.sk/top/aktualne/v-acrosse-sa-daju-zhodnotit-aj-zazitky-3311.html\",\n        \"quote\": \"Medzi aktivity Acrossu v oblasti hotelierstva a cestovného ruchu spadá aj hotelová sieť Sunčani Hvar Hotels\",\n        \"published_date\": \"2016-04-28\",\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"sectors\": {\n      \"value\": [\"travel_hospitality\"],\n      \"value_text\": \"cestovného ruchu a hotelierstva\",\n      \"source_url\": \"https://www.epravo.sk/top/aktualne/v-acrosse-sa-daju-zhodnotit-aj-zazitky-3311.html\",\n      \"quote\": \"Aktivity z oblasti cestovného ruchu a hotelierstva sú jednou z hlavných oblastí\",\n      \"published_date\": \"2016-04-28\",\n      \"derivation\": \"inferred\"\n    },\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": {\n      \"value\": {\"amount\": \"vyše 200 miliónov Euro\", \"currency\": \"EUR\", \"capital_type\": \"aum\", \"as_of\": \"2016-04-15\"},\n      \"value_text\": \"vyše 200 miliónov Euro\",\n      \"source_url\": \"https://www.epravo.sk/top/aktualne/zhodnocujeme-peniaze-uspesnym-ludom-3270.html\",\n      \"quote\": \"Aktuálne spravujeme celkové aktíva v objeme vyše 200 miliónov Euro.\",\n      \"published_date\": \"2016-04-15\",\n      \"derivation\": \"stated\"\n    },\n    \"funds\": [],\n    \"red_flags\": [\n      {\n        \"value\": \"last documented investments in companies (hotels) date from a 2016 commercial notice written by Across; no later investment into companies found\",\n        \"value_text\": \"Medzi najvýznamnejšie investície\",\n        \"source_url\": \"https://www.epravo.sk/top/aktualne/v-acrosse-sa-daju-zhodnotit-aj-zazitky-3311.html\",\n        \"quote\": \"Medzi najvýznamnejšie investície na Slovensku patrí Horský hotel Sliezsky dom, Hotel Salamandra\",\n        \"published_date\": \"2016-04-28\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": \"primarily an investment-services firm and manager of client portf
… [skrátené, 16170 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b10.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b10 done. Output written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b10.json (5 records).\n\n- C102 Across Private Investments: other (investment services and client-portfolio manager); 2 investments (hotels, 2016 Across-authored advertorial); early_exit null. Doubtful: IČO not shown on the site, so company_id is null; no deal after 2023.\n- C107 BHM group: group_holding; 7 investments (Tedisel Medical 2026-07-15 via Reinsberg, plus 6 portfolio names); early_exit null. Doubtful: HQ not verified (hq_country null); Brandon Medical omitted because I had no word-for-word source; portfolio quotes are bare company names.\n- C032 Tensor Ventures: vc; 1 investment (AppFactor, 2026-02, seed); 2 funds; early_exit null. Doubtful: the AppFactor quote joins two adjacent sentences, so the machine check may fail if they are not adjacent; the 2024 fund has no name in the source; the EIF co-investment fund was not verified.\n- C205 Grbi One s.r.o.: no investment found; early_exit no_investment_found. No website or name match found.\n- C187 Zero One Hundred: vc; 7 investments (Vestberry 2025-03-14, plus 6 portfolio names); early_exit null. Doubtful: the €25M Fund II (2025) could not be verified, so the record uses the €60M figure from 2022; the management s.r.o. was not found."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

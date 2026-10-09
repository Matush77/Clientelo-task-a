# Subagent: Evidence v3 wave2 batch 08 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:00:53

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b08.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b08.json

Today is 2026-10-08.

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\prompts\\evidence_agent.md"
}
````

</details>

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b08.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b08.json"
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

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C158",
4	    "name": "Long Journey Ventures",
5	    "other_names": [],
6	    "known_website": null,
7	    "registry_hint": null
8	  },
9	  {
10	    "candidate_id": "C093",
11	    "name": "Smart Management VC s.r.o.",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": null
15	  },
16	  {
17	    "candidate_id": "C169",
18	    "name": "Quadrille",
19	    "other_names": [],
20	    "known_website": null,
21	    "registry_hint": "possible registry match (unconfirmed, may be a different company): QUADRILLE spol. s r.o., IČO 25204254"
22	  },
23	  {
24	    "candidate_id": "C135",
25	    "name": "Seed Starter",
26	    "other_names": [
27	      "Seed Starter ČS"
28	    ],
29	    "known_website": null,
30	    "registry_hint": null
31	  },
32	  {
33	    "candidate_id": "C181",
34	    "name": "Wing VC",
35	    "other_names": [],
36	    "known_website": null,
37	    "registry_hint": null
38	  }
39	]
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
  "query": "Long Journey Ventures investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Smart Management VC s.r.o. investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Quadrille venture capital investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Seed Starter ČS investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Wing VC investice startup",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Smart Management VC s.r.o. investice"

Links: [{"title":"Smart Capital","url":"https://app.dealroom.co/companies/smart_capital"},{"title":"Go to deals","url":"https://www.oaklins.com/ch/en/deals/111536/"},{"title":"Smart Capital","url":"https://insights.munich-startup.de/companies/smart_capital/team"},{"title":"Go to deals","url":"https://www.oaklins.com/cl/en/deals/111536/"},{"title":"Go to deals","url":"https://www.oaklins.com/bg/en/deals/111536/"},{"title":"smart capital","url":"https://superscout.co/investor/smart-capital"},{"title":"Go to deals","url":"https://www.oaklins.com/br/en/deals/111536/"},{"title":"Go to deals","url":"https://www.oaklins.com/ca/en/deals/111536/"},{"title":"Go to deals","url":"https://www.oaklins.com/mx/en/deals/111536/"},{"title":"The CNMV authorizes creation of Encomenda Smart Capital, a specialized seed investment manager in technological startups","url":"https://www.ttrdata.com/en/radar/aggregated/The-CNMV-authorizes-creation-of-Encomenda-Smart-Capital-a-specialized-seed-investment-manager-in/251371"}]

The search didn't return anything about Smart Management VC s.r.o., so I can't say what it invests in. None of the results mention that company name.

The results did include several similarly named firms, which are probably not the one you want:

- **Smart Capital S.p.A. (Italy):** Its business is minority stakes, private equity and PIPE deals, and it recently finished a rights issue to fund more investments, according to Oaklins, which reported a December 2025 rights issue.
- **Smart Capital (Vienna, Austria):** Listings on Dealroom describe it as a corporate finance firm focused on venture and private equity, supporting SMEs across Europe.
- **Smart Capital (Tunisia):** It is a venture capital organization that invests in innovative SMEs and startups.
- **Encomenda Smart Capital (Spain):** Spain's CNMV authorized it as a seed investment manager for technology startups.

Since "s.r.o." is a Czech or Slovak limited liability company form, the target is most likely registered in one of those countries. To find its owners, stated purpose and any financial filings, you could check the Czech business register (ARES or justice.cz). If the company is a licensed fund or investment manager, the Czech National Bank's public registers would also list it.

If you give me the company's registration number (IČO) or a Czech-language search term, I can run a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Wing VC investice startup"

Links: [{"title":"Wing Venture Capital","url":"https://en.wikipedia.org/wiki/Wing_Venture_Capital"},{"title":"snowflake backer wing closes 600 million ai focused fund","url":"https://www.bloomberg.com/news/articles/2023-07-13/snowflake-backer-wing-closes-600-million-ai-focused-fund"},{"title":"Wings Capital Ventures","url":"https://startmeup.hk/startup-resources/wings-capital-ventures/"},{"title":"Silicon Valley Venture Capital Vets Launch $111M Fund","url":"https://docs.wing.vc/content/silicon-valley-venture-capital-vets-launch-111-million-fund"},{"title":"wing venture capital","url":"https://www.briter.co/companies/wing-venture-capital"},{"title":"Silicon Valley Venture Capital Vets Launch $111M Fund","url":"https://www.wing.vc/content/silicon-valley-venture-capital-vets-launch-111-million-fund"},{"title":"Wing Venture Capital Launches $250 Million Fund for Tech Startups","url":"https://brainstation.io/magazine/wing-venture-capital-launches-250-million-fund"},{"title":"Wing Venture Capital","url":"https://venturecapitalarchive.com/venture-funds/wing-venture-capital-wing-vc"},{"title":"Wing Venture Capital","url":"https://startupim.com/investor/wing-venture-capital-1"},{"title":"Wing Venture Capital Overview","url":"https://slimpages.startupim.com/company_page/wing-venture-capital-1"}]

The results describe **Wing Venture Capital**, a Palo Alto firm. I didn't find a Czech fund called Wing, so I've assumed this is the one you mean.

**Background and funds**
- Peter Wagner and Gaurav Garg started the firm in 2013. Wagner had been a former partner at Accel, while Garg had been at Sequoia Capital.
- Its first fund was about $111 million. The $250 million fund follows up the inaugural fund in 2013, which was $111 million.
- In 2023 the firm closed a $600 million fund for AI startups. The firm closed a $600 million fund to back startups focused on artificial intelligence. Wagner said the money would go toward companies that develop AI tools with a business use case.

**Startup investments**
- Bloomberg's coverage names Cohesity, Gong, Pinecone, and Shape Security as portfolio companies (Firm has invested in Cohesity, Gong, Pinecone, Shape Security). The article is paywalled, so I only saw this summary line.
- Earlier, the firm backed networking company Cumulus Networks and security platform FireEye. Wing has already invested in networking company Cumulus Networks and security platform FireEye.
- An aggregator lists more recent deals: Utila in September 2025 for $22 million and Lumana in July 2025 for $40 million. Wing Venture Capital's most recent investments include Utila in September 2025 for $22,000,000 and Lumana in July 2025 for $40,000,000.
- Another aggregator shows a seed deal of $8.2 million dated May 2026, but the company name isn't in the snippet.

**Focus and stage**
- The firm mainly backs early-stage companies. One profile says it provides comprehensive support from pre-seed to S
… [skrátené, 718 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Long Journey Ventures investice"

Links: [{"title":"Long Journey Ventures (investor - Venture Capital)","url":"https://nordic9.com/companies/long-journey-ventures/"},{"title":"longjourney vc","url":"https://parse.gl/brands/longjourney-vc"},{"title":"vcbeast.com","url":"https://vcbeast.com/vc-firms/long-journey-ventures/portfolio"},{"title":"Long Journey Ventures","url":"https://www.seedtable.com/investors/long-journey-ventures"},{"title":"backing the magical weirdos","url":"https://nz.dealroom.co/news/note/backing-the-magical-weirdos"},{"title":"Long Journey Ventures","url":"https://www.deep-tech-week.com/organizations/long-journey-ventures"},{"title":"Investor type","url":"https://privateequitylist.com/investors/long-journey-ventures"},{"title":"lee jacobs","url":"https://jewishinsider.com/tag/lee-jacobs/"},{"title":"Long Journey Ventures","url":"https://www.everythingstartups.com/vc-funds/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://venturecapitalarchive.com/venture-funds/long-journey-ventures-longjourney-vc"}]

"Investice" is Czech for "investments." The results are in English, so here is what they show about Long Journey Ventures' investment activity. The sources often disagree, and several are data aggregators.

**The firm**
- Lee Jacobs founded the San Francisco early-stage firm in 2019 (a venture capital firm based in San Francisco founded in 2019 by Lee Jacobs).
- Cyan Banister and Arielle Zuckerberg are also principals (Cyan Banister: Co-founder and General Partner... Arielle Zuckerberg: General Partner).
- Its guiding theme is backing founders with offbeat ideas, summed up as the firm's guiding ethos is investing in the "magically weird".

**Fund size and deal pace**
- One profile puts assets under management at around $182m.
- Another aggregator credits the firm with total capital raised of $450 million, having invested in approximately 130 companies to date.
- Nordic9 tracks about 2.5 deals a year. Its investment list is behind a paywall.
- The announcement date is also unclear. One profile dates the latest fund to March 20, 2025, while a Jewish Insider piece ties the fund announcement to an October 7 statement.

**Stage, check size, and focus (sources conflict)**
- Deep Tech Week describes seed and pre-seed stage companies developing deep technologies, with funding ranging from $500K to $2M per investment.
- Privateequitylist lists Seed and Series A stages with typical checks of $10–50M. That is unusually large for a seed-focused fund, so I would treat it cautiously.
- Sector lists differ. Everythingstartups emphasizes FinTech, AI, blockchain, crypto, and data services, while Privateequitylist also includes mobility and transportation.
- Geography also varies. Privateequitylist says North America and Europe, Deep Tech Week says primarily the US, and Nordic9 tags the UK as its most common market.

**Portfolio companies mentioned**
- Covariant, an AI-for-robotics company, appear
… [skrátené, 865 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Seed Starter ČS investice"

Links: [{"title":"Seed Starter ČS Overview","url":"https://pitchbook.com/profiles/investor/532485-73"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/541902-rozhovor-jak-muze-zacinajicim-startupum-pomoci-ceska-sporitelna"},{"title":"Investice do startupů po vzoru České spořitelny přebírá další země. Banka jim zatím poslala 180 milionů","url":"https://cc.cz/investice-do-startupu-po-vzoru-ceske-sporitelny-prebira-dalsi-zeme-banka-jim-zatim-poslala-180-milionu/"},{"title":"Petr Kopeček","url":"https://cz.linkedin.com/in/petrkopecek1"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/541902-seed-starter-cs"},{"title":"seed starter ceska sporitelna becomes co owner of investown","url":"https://www.investown.cz/en/post/seed-starter-ceska-sporitelna-becomes-co-owner-of-investown"},{"title":"Seed starter","url":"https://cc.cz/tag/seed-starter/"},{"title":"Česká spořitelna chce, aby investoři více vydělávali. Investuje do slovenského startupu, který to řeší","url":"https://cc.cz/ceska-sporitelna-chce-aby-investori-vice-vydelavali-investuje-do-slovenskeho-startupu-ktery-to-resi/"}]

Seed Starter ČS is the venture investment program of Česká spořitelna, the Czech Republic's largest bank, and it operates within Erste Group. PitchBook profiles it as a Prague-based venture capital firm that targets technology startups.

**How it invests**
- The program takes equity stakes in seed-stage companies and also provides incubation, meaning financial and management support, along with access to the bank's partner and client network. The program offers investment in equity in the seed phase (initial phase), professional incubation (financial and management support) and a wide network of partners and customers.
- Check sizes start at roughly EUR 200K and can reach EUR 1M, occasionally more. The team often begins with a small amount and adds money later if the partnership works. Tickets start at EUR 200K and can go up to a million. Exceptionally even higher. The team likes to start with a small amount at first.
- The scope is broader than fintech. The fund looks for technology that could help the bank, its clients, or its employees, and its best portfolio companies may become commercial partners of the bank or the wider Erste group.

**Portfolio and track record**
- PitchBook counts 14 investments, 12 companies still in the portfolio, and one exit. Investments 14; Portfolio 12; Exits 1.
- Definic, a Slovak company that helps firms choose IT suppliers, is among the newest deals. Seed Starter joined a EUR 2.5M round led by J&T Ventures, with Slovak Investment Holding also 
… [skrátené, 1846 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Quadrille venture capital investice"

Links: [{"title":"Quadrille Capital Raises €500 Million for Tech Investments","url":"https://news.bloombergtax.com/financial-accounting/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"Quadrille Capital Raises €500 Million for Tech Investments","url":"https://news.bloomberglaw.com/private-equity/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"Quadrille Capital Raises €500 Million for Tech Investments","url":"https://news.bgov.com/crypto/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"quadrille capital raises 500 million for tech investments","url":"https://www.bloomberg.com/news/articles/2025-09-11/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"quadrille raises 73m for ag2r la mondial fund","url":"https://globalventuring.com/quadrille-raises-73m-for-ag2r-la-mondial-fund"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/quadrille-capital-raises-500m-for-tech"},{"title":"Corporate information","url":"https://data.kando.tech/company/quadrille-capital"},{"title":"# Quadrille Capital","url":"https://altss.com/profile/quadrille-capital.md"},{"title":"quadrille capital","url":"https://venturecapitalcareers.com/companies/quadrille-capital"},{"title":"quadrille capital","url":"https://prod.actual.seedtable.com/investors/quadrille-capital"}]

Links: [{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/investors/quadrille_capital/portfolio"},{"title":"quadrille capital raises 500 million for tech investments","url":"https://www.bloomberg.com/news/articles/2025-09-11/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"Quadrille Capital Raises €500 Million for Tech Investments","url":"https://news.bloomberglaw.com/private-equity/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/companies/quadrille_capital/portfolio"},{"title":"Quadrille Capital Raises €500 Million for Tech Investments","url":"https://news.bgov.com/crypto/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"Quadrille Capital Raises €500 Million for Tech Investments","url":"https://news.bloombergtax.com/financial-accounting/quadrille-capital-raises-500-million-for-tech-investments"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/quadrille-capital-raises-500m-for-tech"},{"title":"# Quadrille Capital","url":"https://altss.com/profile/quadrille-capital.md"},{"title":"anyof Canada","url":"https://insights.munich-startup.de/companies/quadrille_capital/portfolio/f/locations/anyof_Canada"},{"title":"quadrille capital secures e511 million for 4th tech fund with up to 50 to be invested in europe","url":"https://www.eu-startups.com/2021/03/quadrille-capital-secures-e511-million-for-4th-tech-fund-with-up-to-50-to-be-invested-in-europe/"}]

I found no Czech or S
… [skrátené, 2478 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.longjourney.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the office, address, headquarters, location, team, portfolio, investments, fund size, or ticket, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.quadrillecapital.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the office, address, headquarters, location, team, portfolio, investments, assets under management, fund size, or ticket, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.wing.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the office, address, headquarters, location, team, portfolio, investments, fund size, or ticket, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "seedstarter.cz Seed Starter Česká spořitelna portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Smart Management VC\" fond",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the matching sentences, reproduced exactly as they appear on the page:

**Location**
- © 2026 Wing VC, Palo Alto CA, All Rights Reserved.

**Portfolio and investments**
- Our portfolio
- We've helped build more than 25 different billion-dollar companies. Here's what our founders say about the work.
- When Wing invested, Gong wasn’t obvious to most folks.

**Navigation**
- Portfolio
- Team

**Not found on the page:** No office address, headquarters, fund size, or ticket size appears. The page shows no publication date for itself. The "© 2026" line is a copyright notice, and the "September 2026" labels belong to the linked articles, not this page.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- "Long Journey Ventures - Early Stage Investing for the long-term."
- Navigation labels: "Portfolio" and "Team"

No office, address, headquarters, location, fund size, ticket, or publication date appears on the page. The only date is the copyright notice "© 2026 Long Journey."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Investments and strategy**
- "We invest globally in technology and healthcare assets through four complementary strategies:"
- "— Investments in Growth Equity companies,"
- "We have built our platform and our team to leverage the synergies across those four strategies."
- "This holistic investment approach unlocks additional intelligence and opportunities."
- "We have chosen to invest in technology, with a global scope and a financial lens"

**Assets under management and firm size**
- "+20 years +40 professionals €1.6bn Assets Under Management" (figures listed on the page as separate items)

**Team**
- "Our team is our main asset"
- "Our people share a financial DNA and a culture of excellence."
- "We train them across our different strategies."

**Portfolio**
- The "Our portfolio" section has no full sentences. It lists Growth Equity and Primary portfolio companies as logos and links, so there is no sentence to reproduce.

**Office and location**
- "16, place de la Madeleine 75008 Paris, France"
- The legal notice states that Quadrille Capital is registered in Paris. That sentence is longer than 125 characters, so I can't quote it in full. Paraphrased: the company is a French SAS registered with the Paris Trade and Companies Register.

**Publication date**
- No publication date appears on the page.

**Not found**
- No ticket sizes or fund sizes appear beyond the AUM figure above.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Smart Management VC" fond"

Links: [{"title":"venture capital software","url":"https://www.smartsuite.com/blog/venture-capital-software"},{"title":"Smart Capital S.A","url":"https://www.developmentaid.org/organizations/view/517421/smart-capital-sa"},{"title":"la cnmv autoriza a encomenda smart capital como gestora de fondos capitaneada por carlos blanco y oriol juncosa","url":"https://www.fundssociety.com/es/noticias/negocio/la-cnmv-autoriza-a-encomenda-smart-capital-como-gestora-de-fondos-capitaneada-por-carlos-blanco-y-oriol-juncosa/"},{"title":"smart partnership capital venture capital fund","url":"https://startupintros.com/orgs/smart-partnership-capital-venture-capital-fund"},{"title":"Revolutionizing Venture Capital with Fundraising Management Software","url":"https://smartsuite.com/blog/venture-capital-fundraising-management-software"},{"title":"Slider Arrow Icon","url":"https://www.smartsuite.com/blog/venture-capital-software-streamline-your-investment-management-with-smartsuite"},{"title":"Venture Capital","url":"https://altss.com/profile/smart-capital-les-berges-du-lac"},{"title":"The CNMV authorizes creation of Encomenda Smart Capital, a specialized seed investment manager in technological startups","url":"https://www.ttrdata.com/en/radar/aggregated/The-CNMV-authorizes-creation-of-Encomenda-Smart-Capital-a-specialized-seed-investment-manager-in/251371"},{"title":"smart partnership capital","url":"https://prod.actual.seedtable.com/investors/smart-partnership-capital"}]

I didn't find any result for "Smart Management VC" as a name. The search returned several firms with "Smart" in the name, plus some software pages. The closest matches are below.

- **Encomenda Smart Capital (Spain):** This is the best fit for the "fond" angle. Spain's securities regulator cleared the creation of this fund manager, which will run a €20 million fund and is led by Carlos Blanco and Oriol Juncosa. The first closing was expected in September. FOND-ICO approved its investment in the fund the previous May. The source doesn't explain what FOND-ICO is. It is likely a Spanish state-backed fund-of-funds, but that is from my general knowledge, not the search results. The articles are undated, so the September closing may already have passed.
- **Smart Capital S.A. (Tunisia):** This management company, approved by the Conseil des Marchés Financiers, is responsible for implementing the ANAVA fund of funds dedicated to venture capital funds and the Innovatech fund, which invests directly in innovative Tunisian SMEs.
- **Smart Capital (Les Berges du Lac, Tunis):** This venture capital firm is headquartered in Tunis, Tunisia. It manages three funds for innovative small and medium-sized enterprises and startups, including a fund-of-funds for startups. It may be related to the Tunisian firm above, but the results don't confirm this.
- **Smart Partnership Capital (US):** This is a Delaware-based venture capital fund founded in 2019, investing
… [skrátené, 365 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "seedstarter.cz Seed Starter Česká spořitelna portfolio"

Links: [{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Fueling innovation","url":"https://csas.cz/cs/page/seedstarter"},{"title":"Trh je plný rychle umírajících projektů a plýtvá se penězi, říká Medek z České spořitelny, která to chce změnit","url":"https://cc.cz/trh-je-plny-rychle-umirajicich-projektu-a-plytva-se-penezi-rika-medek-z-ceske-sporitelny-ktera-to-chce-zmenit/"},{"title":"Investice do startupů po vzoru České spořitelny přebírá další země. Banka jim zatím poslala 180 milionů","url":"https://cc.cz/investice-do-startupu-po-vzoru-ceske-sporitelny-prebira-dalsi-zeme-banka-jim-zatim-poslala-180-milionu/"},{"title":"Petr Kopeček","url":"https://cz.linkedin.com/in/petrkopecek1"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/239108"},{"title":"Hlavní obsah","url":"https://seznamzpravy.cz/clanek/ekonomika-byznys-rozhovory-inkubator-neni-jen-pro-novorozence-sporitelna-jde-s-tim-svym-do-rumunska-239108"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/seed-starter-ceske-sportielny"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/541902-seed-starter-cs"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/clanky/541902-seed-starter-cs/"}]

I couldn't open seedstarter.cz itself, but several sources describe the program and its portfolio. Those sources are from different dates, so the figures may be out of date.

**What it is**
- CB Insights lists seedstarter.cz as the website of a Prague-based venture investor that backs early-stage startups. The program helps startups with the go-to-market phase and involves external projects in the Ceska sportelna environment.
- The operating company is ČS Seed Starter, a.s., based at Olbrachtova 1929/62 in Prague 4. The Česká spořitelna page says the company has been investing in technologies that help banking thrive or bring innovation to our clients since 2020.
- The program focuses on seed-stage companies. It can also join later. Per the portfolio manager's LinkedIn profile, tickets start at EUR 200K and can go up to a million.

**Czech portfolio**
- An earlier CzechCrunch report named five Czech holdings: Investown, Signi, PalmApp, Wflow a Rekenber.
- A later Seznam Zprávy interview said the program had already supported eight startups in the Czech Republic and was about to sign a ninth.
- CB Insights counts 14 investments, and its latest was in Repsense as part of their Seed VC on December 16, 2025. That tally isn't limited to Czech companies.

**Reported value**
- Seznam Zprávy reported that the program had invested 180 million CZK in total and that over three ye
… [skrátené, 1119 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.longjourney.vc/team",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that mentions an office, address, headquarters, city, country, location, or contact, and any team member's name with title. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://csas.cz/cs/page/seedstarter",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions ČS Seed Starter, Seed Starter, the company name, IČO, registered office or sídlo, address, Praha, investice, portfolio, startup, seed, ticket or tickets, EUR, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Smart Management VC\" startup investuje",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.csas.cz/cs/page/seedstarter
    Redirect URL (from the server's Location header — server-supplied, not verified): https://www.seedstarter.cz/cs/uvod
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://www.seedstarter.cz/cs/uvod"
    - prompt: "Return word-for-word, without summarising or translating, every sentence that mentions ČS Seed Starter, Seed Starter, the company name, IČO, registered office or sídlo, address, Praha, investice, portfolio, startup, seed, ticket or tickets, EUR, and the page's publication date if shown."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Locations and sentences mentioning a city, state, or factory**

- "Lee lives in San Francisco with his wife and two daughters."
- "...out of our factory in San Francisco's Mission District."
- "Kelsey is based in Washington state..."
- "She calls San Francisco home, where she's happiest surrounded by her tight-knit circle of friends and family."

**Contact**

- "Say hello" (hi@longjourney.vc)
- Twitter link: https://twitter.com/LongJourneyVC

**Team members with titles**

- Lee Jacobs: Co-Founder & Managing Partner
- Cyan Banister: Co-Founder & General Partner
- Arielle Zuckerberg: General Partner
- Jonathan Bruck: Venture Partner
- Justin Mares: Venture Partner
- Pascal Levy-Garboua: Venture Partner
- Scott Banister: Venture Partner
- Dani Tustin: Chief Financial Officer
- Mike Wang: Chief Product Officer
- Carolena Leon: Platform Associate
- Kelsey Muller: Executive Assistant
- Elaine Wherry: Advisor
- Brian Balfour: Advisor
- Aaron VanDevender: Advisor
- Andrew Look: Advisor

**Publication date:** None is shown. The only date is "© 2026 Long Journey," which is a copyright notice, not a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Smart Management VC" startup investuje"

Links: [{"title":"encomenda smart capital","url":"https://privateequitylist.com/investor/encomenda-smart-capital"},{"title":"smart capital","url":"https://superscout.co/investor/smart-capital"},{"title":"Encomenda Smart Capital","url":"https://capboard.io/en/investor/encomenda-smart-capital"},{"title":"smart partnership capital venture capital fund","url":"https://startupintros.com/orgs/smart-partnership-capital-venture-capital-fund"},{"title":"smartinvest ventures","url":"https://privateequitylist.com/investors/smartinvest-ventures"},{"title":"Encomenda Smart Capital","url":"https://privateequitylist.com/investors/encomenda-smart-capital"},{"title":"The Founder's Guide to","url":"https://superscout.co/investor/spc-vc-com"},{"title":"The CNMV authorizes creation of Encomenda Smart Capital, a specialized seed investment manager in technological startups","url":"https://www.ttrdata.com/en/radar/aggregated/The-CNMV-authorizes-creation-of-Encomenda-Smart-Capital-a-specialized-seed-investment-manager-in/251371"},{"title":"smart partnership capital","url":"https://prod.actual.seedtable.com/investors/smart-partnership-capital"}]

Links: [{"title":"smart partnership capital venture capital fund","url":"https://startupintros.com/orgs/smart-partnership-capital-venture-capital-fund"},{"title":"Slider Arrow Icon","url":"https://www.smartsuite.com/blog/venture-capital-software-streamline-your-investment-management-with-smartsuite"},{"title":"venture capital software","url":"https://www.smartsuite.com/blog/venture-capital-software"},{"title":"streamlining venture capital operations with deal flow management software","url":"https://www.smartsuite.com/blog/streamlining-venture-capital-operations-with-deal-flow-management-software"},{"title":"Smart Capital S.A","url":"https://www.developmentaid.org/organizations/view/517421/smart-capital-sa"},{"title":"smart partnership capital","url":"https://prod.actual.seedtable.com/investors/smart-partnership-capital"},{"title":"Revolutionizing Venture Capital with Fundraising Management Software","url":"https://smartsuite.com/blog/venture-capital-fundraising-management-software"},{"title":"Manage Venture Capital Firm Operations","url":"https://smartsuite.com/solutions/venture-capital"},{"title":"Venture Capital","url":"https://altss.com/profile/smart-capital-gmbh-hamburg-germany"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/smart"}]

I couldn't find any source describing a firm called "Smart Management VC" or its startup investments. The closest matches are different organizations, so I can't confirm that any of them is the one you mean:

- **Smart Partnership Capital** (spc-vc.com): Founded in 2019 and based in Wilmington, Delaware, this group backs seed through Series A B2B software companies with checks of $100k to $1M. It is a Delaware-based venture capital fund founded in 2019, investing $100k-$1M in early seed to Series A-st
… [skrátené, 1455 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.seedstarter.cz/cs/uvod",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions ČS Seed Starter, Seed Starter, the company name, IČO, registered office or sídlo, address, Praha, investice, portfolio, startup, seed, ticket or tickets, EUR, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.longjourney.vc/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, the list of every portfolio company name shown on the page, with any stated round, date, sector or description line next to each name. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Smart Management VC\"",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't print company names as text. They appear only as logo images, so I've taken each name from the logo filename or link URL. The page also shows no rounds, dates, sectors, or descriptions for any company.

**Portfolio companies (in page order):**

1. Anduril
2. Crusoe
3. Notion
4. MindBloom
5. Thumbtack
6. Postmates
7. SpaceX
8. Affirm
9. Uber
10. Carta
11. Babylon
12. DeepMind
13. Density
14. Diamond Foundry
15. Kin Insurance
16. DuckDuckGo
17. Flock Safety
18. Northwood
19. Numeric
20. Loom
21. Together.ai
22. Modern Animal
23. Truemed
24. Inertia
25. Wingspan
26. Wonderschool
27. Zero Acre
28. Atob
29. General Cybernetics
30. Laurus
31. Proxima
32. Solcoa Industries
33. Substrate
34. Andrenam
35. Becoming
36. Superpower
37. BusRight
38. Stoke
39. Neros
40. Luumlash
41. Throne Science
42. Parakeet Security
43. Reforge
44. Ziina
45. Checkr
46. Flexport
47. Niantic
48. Valence
49. Titan Dynamics
50. Kettle & Fire
51. Rainmaker
52. Maven
53. Tornyol
54. Ownwell
55. Volteras
56. Flora Fauna
57. Photon
58. Havik
59. rec.us
60. Nectir
61. Arcee
62. General Matter
63. Server Robotics

Some logos have placeholder filenames (e.g., "blank (29)"), so for those I used the linked domain. Spellings may differ from the companies' official brand names.

The final image ("Bellwethers welcome.") is a section banner, not a portfolio company, so I excluded it.

**Publication date:** None is shown. The only date is the footer copyright, "© 2026 Long Journey."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the matching passages, reproduced exactly as they appear on the page. Several are fragments rather than full sentences.

**Company name / Seed Starter**
- "Grow something that will last | Seed Starter České spořitelny"
- "ČS Seed Starter, a.s."
- "info@seedstarter.cz"

**Startup / seed / ticket / EUR**
- "Are you a progressive startup with a well-established team of experts that has a clear strategy, values and goals?"
- "Since 2020 we have been investing in technologies that help banking thrive or bring innovation to our clients. We pave the way for the best startups to collaborate with Česká spořitelna and other members of the Erste Group."
- "Pre-seed & Seed  investment rounds"
- "Ticket size  200k – 1M EUR"
- "Startups active  in CEE"

**Portfolio**
- "Portfolio"

**IČO / address / Praha**
- "IČ: 61058769"
- "Olbrachtova 1929/62"
- "140 00 Praha 4, Česká republika"

**Notes**
- No "sídlo," "investice," or publication date appears on the page.
- "Investment" and "investing" appear, but I excluded them because they are not the Czech term "investice." The sentence with "investing" is included because it mentions startups.
- The page shows "IČ," not "IČO."
- "Seed Starter" appears in the image URL, which I left out because it is not page text.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Smart Management VC""

Links: [{"title":"smart partnership capital venture capital fund","url":"https://startupintros.com/orgs/smart-partnership-capital-venture-capital-fund"},{"title":"Slider Arrow Icon","url":"https://www.smartsuite.com/blog/venture-capital-software-streamline-your-investment-management-with-smartsuite"},{"title":"venture capital software","url":"https://www.smartsuite.com/blog/venture-capital-software"},{"title":"streamlining venture capital operations with deal flow management software","url":"https://www.smartsuite.com/blog/streamlining-venture-capital-operations-with-deal-flow-management-software"},{"title":"Smart Capital S.A","url":"https://www.developmentaid.org/organizations/view/517421/smart-capital-sa"},{"title":"smart partnership capital","url":"https://prod.actual.seedtable.com/investors/smart-partnership-capital"},{"title":"Revolutionizing Venture Capital with Fundraising Management Software","url":"https://smartsuite.com/blog/venture-capital-fundraising-management-software"},{"title":"Manage Venture Capital Firm Operations","url":"https://smartsuite.com/solutions/venture-capital"},{"title":"Venture Capital","url":"https://altss.com/profile/smart-capital-gmbh-hamburg-germany"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/smart"}]

I didn't find any result for a firm called exactly "Smart Management VC." The closest matches have different names, so you may mean one of these:

- **Smart Partnership Capital**: The nearest match. One profile dates its start to 2019 and places it in Delaware, with checks of $100k to $1M for early-stage B2B software startups Smart Partnership Capital is a Delaware-based venture capital fund founded in 2019, investing $100k-$1M in early seed to Series A-stage B2B SaaS startups with global ambitions. Another listing describes its focus differently, as a venture capital fund investing in early-stage companies, particularly in health tech.
- **Smart Capital GmbH**: A venture capital firm based in Hamburg, Germany, that invests in early-stage companies. It provides venture capital and expertise in exchange for equity to support entrepreneurs and new business launches.
- **Smart Capital S.A.**: A Tunisian firm. It is a management company approved by the Conseil des Marchés Financiers, responsible for implementing the ANAVA fund of funds dedicated to venture capital funds and the Innovatech fund invested directly in innovative Tunisian SMEs.
- **SmartSuite**: Not an investor. It's a software vendor. SmartSuite offers a comprehensive venture capital solution that helps firms manage their portfolio with ease. Our solution provides a centralized platform for managing portfolio companies, tracking performance metrics, and automating deal flow management.

The results don't confirm whether any of these is the firm you mean. If you can share a location, website, or what the firm invests in, I can run a narrower search.


REMINDER: You MUST include t
… [skrátené, 72 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.seedstarter.cz/cs/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that names a portfolio startup, with any stated date, round, amount, or description next to it. Also return every sentence mentioning investice, startup, seed, or portfolio, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Definic Seed Starter Česká spořitelna J&T Ventures 2,5 mil. EUR",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Long Journey Ventures led seed round 2025 San Francisco",
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
Web search results for query: "Definic Seed Starter Česká spořitelna J&T Ventures 2,5 mil. EUR"

Links: [{"title":"Nákup IT služeb v korporacích je často nefunkční, hlásí. Do jejich řešení investuje i Česká spořitelna","url":"https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/"},{"title":"Petr Kopeček","url":"https://cz.linkedin.com/in/petrkopecek1"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/tag/slovakia"},{"title":"j t ventures","url":"https://seedtable.com/investors/j-t-ventures"},{"title":"Pitch to hundreds of VC funds and business angels","url":"https://www.vestbee.com/insights/articles/startup-accelerator-of-the-month:-culttech"},{"title":"J&T Ventures logo","url":"https://www.tryfundable.ai/investor/j-t-ventures"},{"title":"funding.tech.eu","url":"https://funding.tech.eu/geographies/czech-republic/2026"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/j-t-ventures"},{"title":"J&T VENTURES","url":"https://seedtable.com/investors/jt-ventures"},{"title":"J&T Ventures","url":"https://the-web-radar.com/companies/jtventures.cz"}]

Definic, a Slovak AI startup formerly known as Nordics, closed a seed round of about €2.5 million, roughly 60 million CZK. The company was previously known as Nordics, and it has transformed into a global vendor intelligence platform, and it plans to use the capital mainly for further product development. The round was announced in June 2026. Seedtable lists the announcement date as 12 June 2026 and records it as J&T Ventures' first investment in Slovakia.

**Investors**
- **J&T Ventures** led the round. The firm typically leads rounds and deploys €300,000 to €2.5 million per company across pre-seed to Series A stages.
- **Seed Starter** (the fund under Česká spořitelna) and **Slovak Investment Holding** joined as co-investors. Seed Starter's Tomáš Milota said the investment could be applied across the bank's financial group, where efficient technology adoption is a priority. Seed Starter says its tickets start at €200K and can go up to €1 million, with occasional exceptions above that.

**Company details**
- Clients such as Erste and Siemens already use the team's product.
- The company plans to expand into German-speaking markets, the UK, and the US, and it is already building a presence in New York's financial district.
- The founders are Robert Dečman, Lukáš Řezanina, and Michal Mušinka, a team based in the eastern Slovak city of Košice.
- Seedtable's data shows the round as $2.9 million, which is the same raise converted to US dollars. It lists Definic as an AI seed deal dated 12 June 2026, with J&T as the lead.

The sources agree on the core facts: the amount, the lead investor, and the co-investors. The Czech article is the most detailed, and it is the only one that gives the CZK equivalent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Long Journey Ventures led seed round 2025 San Francisco"

Links: [{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/long-journey-ventures"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.seedtable.com/investors/long-journey-ventures"},{"title":"Arielle Zuckerberg, Cyan Banister Debut VC Fund, Seek ‘Weirdos’","url":"https://news.bloomberglaw.com/private-equity/arielle-zuckerberg-cyan-banister-debut-vc-fund-seek-weirdos"},{"title":"Long Journey Ventures","url":"https://www.everythingstartups.com/vc-funds/long-journey-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/longjourney"},{"title":"noah levine","url":"https://startupintros.com/people/noah-levine"},{"title":"# Arielle Zuckerberg","url":"https://yespress.io/arielle-zuckerberg.md"},{"title":"Investor type","url":"https://privateequitylist.com/investors/long-journey-ventures"},{"title":"steve schoettler","url":"https://startupintros.com/people/steve-schoettler"}]

Yes, one 2025 seed deal fits, but the evidence comes from investor-profile sites rather than a primary announcement, so verify it before relying on it. The firm is based in San Francisco, California and was founded in 2019.

**Most likely match: VectorShift**
A StartupIntros profile credits managing partner Steve Schoettler with leading a 2025 seed investment in VectorShift, an AI infrastructure startup (he manages more than $100 million in assets under management). The excerpt I found doesn't include the round size or closing date.

**Second possible match: an unnamed AI robotics startup**
StartupIntros also lists Noah Levine as the Managing Partner at Long Journey Ventures, and says that in March 2025, Levine led a $3 million seed funding round for an artificial intelligence robotics startup. The company isn't named in that profile.

**Seedtable's 2025 entries don't confirm a lead role**
Seedtable lists a $100M seed round for Substrate dated 3 November 2025, but its lead column is blank for that deal. The only seed row marked as a lead is BusRight, dated 18 March 2026, which falls outside 2025 (BusRight | Mobility & Transport | Seed | 30.0M USD | 18 Mar 2026).

**Context and caveats**
- The firm's fund news is a separate matter: Long Journey Ventures raised $181.8 million for its latest fund, announced on March 20, 2025.
- Titles conflict across sources. Bloomberg Law describes former AngelList partner Lee Jacobs, who serves as managing partner, while StartupIntros gives the managing partner title to both Levine and Schoettler.
- To confirm, check VectorShift's own announcement or a database such as Crunchbase for the round's date, amount, and lead investor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Definic, Seed Starter, Česká spořitelna, investice, investuje, J&T Ventures, Slovak Investment Holding, kolo, or mil. EUR, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.seedstarter.cz/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that names a portfolio startup, with any stated date, round, amount, or description next to it. Also return every sentence mentioning investice, startup, seed, or portfolio, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Repsense Seed Starter Česká spořitelna seed investice",
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
**Publication date:** "12. 6. 2026"

**Matching sentences** (truncated where longer than 125 characters, marked with […]):

1. Title: "Nákup IT služeb v korporacích je často nefunkční, hlásí. Do jejich řešení investuje i Česká spořitelna"
2. "Tým startupu Definic z východoslovenských Košic už využívají klienti jako Erste či Siemens."
3. "Slovenský startup Definic, donedávna známý pod názvem Nordics, úspěšně uzavřel seed investiční kolo"
4. "Investiční kolo vedl český fond J&T Ventures, ke kterému se připojil Seed Starter […]"
5. "Definic pomáhá organizacím dělat lepší technologická rozhodnutí díky transparentnosti a datovým analýzám."
6. "[…] Jsme přesvědčeni, že Definic má potenciál nastavit nový standard pro celé odvětví" (quoted by Jan Sova of J&T Ventures)
7. "Efektivitu nasazeného systému pak Definic ukazuje na nedávné integraci u jedné z předních evropských bankovních skupin."
8. "Za prvních pět měsíců roku 2026 banka prostřednictvím systému nasmlouvala zakázky za 5,4 milionu eur […]"

**Note:** The page doesn't contain the exact abbreviation "mil. EUR." I included sentences with "milionu eur," which is the closest match.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Repsense Seed Starter Česká spořitelna seed investice"

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/lithuanian-startup-repsense-raises-2m-to-accelerate-european-expansion"},{"title":"analyzuji dezinformace pro nato litevcum ted tensor ventures a seed starter posilaji milion eur","url":"https://forbes.cz/analyzuji-dezinformace-pro-nato-litevcum-ted-tensor-ventures-a-seed-starter-posilaji-milion-eur/"},{"title":"Petr Kopeček","url":"https://cz.linkedin.com/in/petrkopecek1"},{"title":"Investice do startupů po vzoru České spořitelny přebírá další země. Banka jim zatím poslala 180 milionů","url":"https://cc.cz/investice-do-startupu-po-vzoru-ceske-sporitelny-prebira-dalsi-zeme-banka-jim-zatim-poslala-180-milionu/"},{"title":"Jejich nástroj Havel pomáhá i v NATO. Do Litevců teď investují Tensor Ventures a Česká spořitelna","url":"https://cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ventures-a-ceska-sporitelna/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/seed-starter-ceske-sportielny"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Fueling innovation","url":"https://csas.cz/cs/page/seedstarter"},{"title":"Přidání názoru","url":"https://www.mesec.cz/aktuality/ceska-sporitelna-spousti-investicni-program-seed-starter-orientovany-na-start-upy/pridat"}]

**Summary:** Seed Starter, the venture arm of Česká spořitelna, co-invested in Repsense, a Lithuanian dual-use tech startup, in December 2025. The sources disagree on the round size and on who led it.

**The deal**
- One outlet puts the total seed round at €2 million, with Tensor Ventures and Seed Starter together supplying €1.1 million of it. Lithuanian startup Repsense has raised €2 million in a seed funding round to accelerate its expansion across Europe. Czech venture capital funds Tensor Ventures and Seed Starter ČS, the venture capital arm of Czech bank Česka sporitelna, led the round, contributing over half the total investment at €1.1 million.
- Czech outlets describe the round as €1.1 million, roughly CZK 27 million. Repsense received an investment of 1.1 million euros (almost 27 million Czech crowns) for its next expansion.
- CB Insights lists the deal at $2.35 million, dated December 16, 2025. Co-investors' sources list 12/16/2025, Seed VC, Repsense, $2.35M. That figure is closer to the €2 million total than to €1.1 million, though I can't confirm the conversion.
- **Conflict on leadership:** The Czech reports say Tensor led and Seed Starter joined. The round was led by the Czech deeptech fund Tensor Ventures, with Seed Starter of Česká spořitelna and the existing Lithuanian investors BSV Ventures and Coinvest Capital joining. The English-language summary names both Tensor and
… [skrátené, 1944 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ventures-a-ceska-sporitelna/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Repsense, Seed Starter, Česká spořitelna, Tensor Ventures, investice, investuje, kolo, milionů, or eur, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/investice-do-startupu-po-vzoru-ceske-sporitelny-prebira-dalsi-zeme-banka-jim-zatim-poslala-180-milionu/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that names a Seed Starter portfolio startup (Investown, Signi, PalmApp, Wflow, Rekenber, Vestberry, Definic, Repsense or any other company), with any date or amount, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://news.bloomberglaw.com/private-equity/arielle-zuckerberg-cyan-banister-debut-vc-fund-seek-weirdos",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Long Journey Ventures, San Francisco, headquarters, based, office, fund, or location, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the matching passages from the article excerpt:

**Publication date:** "March 19, 2025, 12:00 PM UTC"

**Office and fund references:**
- "the Long Journey Ventures office is unusual for its whimsy"
- "The firm occupies a five-bedroom Victorian house, accented with tropical fruit wallpaper, where bare feet are common."
- "Long Journey is co-led by Cyan Banister"
- The headline refers to a "Debut VC Fund."

The excerpt doesn't mention San Francisco, a headquarters, or where the firm is based. The office description is the only location detail, and the rest of the article is behind a paywall.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 27. 11. 2023

**Sentences naming portfolio startups with a date or amount:**

The only sentence that pairs a portfolio startup with an amount is the DEAP one. Its full text is longer than the 125-character limit, so I quote a shorter excerpt and paraphrase the rest:

- **DEAP (encall's energy comparison service):** The article says DEAP was offered in a pilot to "oslovil v rámci pilotu na 400 tisíc klientů" (about 400,000 clients), and thousands of customers have used it.

**Other sentences naming portfolio startups (no date or amount):**

- "Investiční fond banky má ve svém portfoliu už startupy Investown, Signi, PalmApp, Wflow a Rekenber."

The page does not mention Vestberry, Definic, or Repsense.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Datum publikace:** 17. 12. 2025

**Věty se zmíněnými klíčovými slovy** (delší věty jsou zkráceny na 125 znaků):

1. "Jejich nástroj Havel pomáhá i v NATO. Do Litevců teď investují Tensor Ventures a Česká spořitelna"
2. "Zakladatelé Tensor Ventures: zleva Petr [REDACTED], Roman [REDACTED] a Martin Drdúl"
3. "Foto: Tensor Ventures"
4. "Repsense, litevský startup s kancelářemi i v Praze, umí měřit a předpovídat, jak se informace šíří[…]"
5. "Na svou další expanzi teď získal 1,1 milionu eur (necelých 27 milionů korun)."
6. "Investiční kolo vedl český deeptech fond Tensor Ventures, přidaly se Seed Starter České spořitelny a[…]"
7. "Technologie Repsensu ukazuje, jak rychle se deeptech prosazuje v několika oblastech zároveň,"
8. "Informace jsou stále mocnějším aktivem, proto jsme rádi, že můžeme realizovat tak významnou investici[…]"
9. "Podle Tomáše Miloty, šéfa Seed Starteru, hledá jeho společnost deeptech startupy, jejichž inovace míří[…]"
10. "Repsense staví know-how, které bude mít dopad daleko za hranicemi dnešních informačních výzev,"
11. "Hlavní platforma Repsensu se jmenuje Havel a rozhodovacím orgánům poskytuje nástroje, díky nimž lze[…]"
12. "Foto: Repsense"
13. "Vedení startupu Repsense, uprostřed je CEO Mykolas Katkus"
14. "Související témata: Seed starter, Tensor Ventures"
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/",
  "prompt": "Find the sentence that begins \"Investiční kolo vedl český fond J&T Ventures\" and return it in full, exactly as written, without truncation and without the […] marker, even if it is longer than 125 characters. Quote it word-for-word in Czech."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ventures-a-ceska-sporitelna/",
  "prompt": "Find the sentence that begins \"Investiční kolo vedl český deeptech fond Tensor Ventures\" and return it in full, exactly as written, without truncation and without the […] marker, even if it is longer than 125 characters. Quote it word-for-word in Czech."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "VectorShift seed round Long Journey Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't quote the full sentence because it is about 160 characters, and my limit for quotes from source documents is 125. Here is the first part, exactly as written (98 characters):

"Investiční kolo vedl český deeptech fond Tensor Ventures, přidaly se Seed Starter České spořitelny"

The rest of the sentence says that the existing Lithuanian investors BSV Ventures and Coinvest Capital also took part in the round.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't quote the full sentence because it exceeds the 125-character limit for quotes from source documents. Here is the first part, which is 120 characters:

"Investiční kolo vedl český fond J&T Ventures, ke kterému se připojil Seed Starter patřící pod Českou spořitelnu a Slovak"

The rest of the sentence says that Slovak Investment Holding also joined the round, and that the Seed Starter fund belongs to Česká spořitelna.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "VectorShift seed round Long Journey Ventures"

Links: [{"title":"2024 02 01 vectorshift seed","url":"https://startupintros.com/news/2024-02-01-vectorshift-seed"},{"title":"VectorShift Raises 3.0M USD in Seed Funding","url":"https://seedtable.com/companies/vectorshift/funding-rounds/seed-2024-02"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/vectorshift/financials"},{"title":"todd rovak","url":"https://startupintros.com/people/todd-rovak"},{"title":"Subscribe to Our Newsletter","url":"https://www.thesaasnews.com/news/vectorshift-raises-3-million-in-seed-round/"},{"title":"steve schoettler","url":"https://startupintros.com/people/steve-schoettler"},{"title":"long journey ventures","url":"https://www.briter.co/companies/long-journey-ventures"},{"title":"Long Journey Ventures Research","url":"https://f4.fund/firms/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.slideshare.net/PitchDecks/long-journey-ventures-fund-1-vc-pitch-deck-example"}]

**Short answer:** The February 2024 VectorShift seed round is well documented, but none of the coverage I found lists Long Journey Ventures as a backer. The only sources linking Long Journey to VectorShift are two profile pages describing a 2025 deal, and I couldn't confirm that elsewhere.

**The 2024 seed round**
- Reporting from The SaaS News, dated February 22, 2024, covers a New York-based no-code generative AI company that secured $3M in seed capital.
- Y Combinator, 1984 Ventures, Defy.vc, and Formus Capital are the firms that coverage names as backers.
- CB Insights dates VectorShift's most recent round to February 21, 2024, and labels it a $3M seed-stage raise.

**The Long Journey link**
- A startupintros profile for Managing Partner Todd Rovak credits him with heading a VectorShift seed round in March 2025.
- A companion profile for Steve Schoettler lists VectorShift among his 2025 seed deals at Long Journey.
- For context, Briter's description of Long Journey, a San Francisco firm set up in 2019, centers on early-stage deals.

**Why the 2025 claim is unverified**
- Both claims come from auto-generated startupintros bio pages. I found no press release or funding announcement for a 2025 VectorShift round.
- CB Insights still shows the February 2024 round as VectorShift's latest, which doesn't fit a March 2025 deal. I can't tell when that snapshot was taken.
- The visible CB Insights investors are 468 Capital, Pioneer Ventures, Soma Capital, Defy Partners, and the rest of its roster is paywalled. Long Journey isn't in the visible portion.
- Briter's visible list of Long Journey deals includes Swoop but no VectorShift entry, though some names are masked.
- Investor lists aren't consistent across sites. One startupintros funding page lists different names, such as General Catalyst, so it's less reliable.

If you need to settle this, I can run a narrower search for a 2025 VectorShift funding announcement or check Crunchbase or Pitc
… [skrátené, 117 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://finder.techleap.nl/news/feed/lithuanian-startup-repsense-raises-2m-to-accelerate-european-expansion",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Repsense together with Seed Starter, Česká spořitelna, Tensor Ventures, seed, round, or EUR, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.seedstarter.cz/cs/uvod",
  "prompt": "Return the footer or contact block exactly as written on the page, keeping the company name and the IČ number on the same line if they appear together. Return the text word-for-word, without summarising or translating."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Long Journey Ventures $181.8 million fund San Francisco-based venture firm",
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
Contact

ČS Seed Starter, a.s. IČ: 61058769
DIČ: CZ 61058769
Olbrachtova 1929/62
140 00 Praha 4, Česká republika
info@seedstarter.cz

The page lists the company name and IČ on separate lines. I combined them on one line, as you asked.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Long Journey Ventures $181.8 million fund San Francisco-based venture firm"

Links: [{"title":"backing the magical weirdos","url":"https://nz.dealroom.co/news/note/backing-the-magical-weirdos"},{"title":"www.jta.org","url":"https://www.jta.org/?p=1880788"},{"title":"Arielle Zuckerberg, partners launch $181,818,181 fund for ‘magically weird’ startups","url":"https://www.timesofisrael.com/arielle-zuckerberg-partners-launch-181818181-fund-for-magically-weird-startups/"},{"title":"Hi FemWealth Friends,","url":"https://femwealth.substack.com/p/cyan-banisters-long-journey-ventures"},{"title":"Arielle Zuckerberg’s firm raises $181,818,181.80 to back ‘magically weird’ tech founders","url":"https://americanisraelite.com/?p=118452"},{"title":"lee jacobs","url":"https://jewishinsider.com/tag/lee-jacobs/"},{"title":"arielle zuckerberg","url":"https://yespress.io/arielle-zuckerberg"},{"title":"Long Journey Ventures","url":"https://summify.io/discover/entities/company/long-journey-ventures/"},{"title":"# Arielle Zuckerberg","url":"https://yespress.io/arielle-zuckerberg.md"},{"title":"startup-seeker.com","url":"https://startup-seeker.com/vc/longjourney~vc"}]

Long Journey Ventures is a San Francisco venture firm that raised $181.8 million for its fourth fund. The fund targets early-stage companies across various sectors, including artificial intelligence and bioscience. The fund is labeled Fund IV, with a 2025 vintage. The announcement came in March 2025.

**Leadership:** Cyan Banister and Arielle Zuckerberg co-founded the firm. Lee Jacobs is the managing partner.

**The fund size:** The exact amount is $181,818,181.80, and the figure was chosen on purpose. In Jewish numerology, 18 represents 'chai' or 'life.' Jacobs wrote that the fund was inspired in part by his reaction to Hamas' October 7, 2023 attack on Israel. Zuckerberg described the number as a symbol of life, health, and prosperity.

**Investment focus:** The firm concentrates on what it calls "magically weird" founders, meaning people pursuing unconventional ideas at the earliest stages. It looks for outliers with bold ideas and supports them with a long-term, hands-on approach.

**Conflicting portfolio figures:** The sources disagree on portfolio size. One profile says the firm has invested in roughly 130 companies and raised ~$450M total. Another listing shows 67+ portfolio companies. I could not verify which figure is current.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.timesofisrael.com/arielle-zuckerberg-partners-launch-181818181-fund-for-magically-weird-startups/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Long Journey Ventures, San Francisco, based, headquarters, office, fund, or the Fund IV / $181.8 million figure, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "BusRight seed round Long Journey Ventures led 2026",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article doesn't mention San Francisco, a headquarters, or "Fund IV," and it calls the firm "Long Journey," not "Long Journey Ventures." Quotes are limited to 125 characters, so I've excerpted rather than reproducing full sentences.

**Relevant passages:**

1. The lede says the firm "has announced a new $181.8 million fund that will back" tech founders. The firm is co-led by Arielle Zuckerberg.
2. "Two of the three main venture capitalists behind the new fund at the firm, called Long Journey" are Jewish, according to the article. Lee Jacobs is the managing partner.
3. Jacobs says the new fund was partly inspired by his reaction to the October 7, 2023 Hamas attack.
4. Jacobs writes: "This fund, with its repetition of 18s, embodies my commitment to supporting life and creation."
5. Zuckerberg's tweet, quoted in the article, says the firm "doubled our AUM @LongJourney by closing a $181,818,181.8 fund."
6. The headline reads: "Arielle Zuckerberg, partners launch $181,818,181 fund for 'magically weird' startups."
7. "Long Journey has a reputation for quirkiness: It is housed in a large Victorian house" with tropical wallpaper, per Bloomberg. This is the closest the article comes to describing an office, but it gives no city or address.

**Publication date:** "21 March 2025, 8:20 am"

[WebFetch note: this page's text is 167732 characters long and the answer above covers only characters 0 to 100000; the final 67732 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "BusRight seed round Long Journey Ventures led 2026"

Links: [{"title":"news.northeastern.edu","url":"https://news.northeastern.edu/?p=108603"},{"title":"SBF 70 years logo","url":"https://www.schoolbusfleet.com/news/busright-picks-up-25m-in-funding-from-vc-firms"},{"title":"Back to BusRightChangelog and Sources","url":"https://seedtable.com/companies/busright/funding-rounds/seed-2026-03"},{"title":"Digital School Bus Route Planning Company BusRight Raises $2.5 Million","url":"https://pulse2.com/busright-raises-2-5-million/amp/"},{"title":"underscore.vc","url":"https://underscore.vc/?p=1307"},{"title":"www.citybiz.co","url":"https://www.citybiz.co/?p=34645"},{"title":"Sherman Center Co-op Leads to BusRight Start-Up","url":"https://coe.northeastern.edu/?p=25477"},{"title":"busright picks up 25m seed funding from underscore vc long journey ventures yap633oCJbux7ZuGkF7hoN 20210331418","url":"https://www.thetrustedinsight.com/investment-news/busright-picks-up-25m-seed-funding-from-underscore-vc-long-journey-ventures-yap633oCJbux7ZuGkF7hoN-20210331418/"},{"title":"sp-edge.com","url":"https://sp-edge.com/updates/20360"},{"title":"Why Underscore.vc invested in BusRight","url":"https://www.alexanderjarvis.com/?p=86813"}]

Links: [{"title":"BusRight: $30 Million Raised For Student Transportation Technology Platform","url":"https://pulse2.com/busright-30-million-raised-for-student-transportation-technology-platform/amp/"},{"title":"UPDATED 09:00 EDT / MARCH 18 2026","url":"https://siliconangle.com/2026/03/18/busright-bags-30m-ensure-school-buses-always-arrive-right-time/"},{"title":"volition leads busrights 30m round to power the largest mass transit system","url":"https://volitioncapital.com/news/volition-leads-busrights-30m-round-to-power-the-largest-mass-transit-system"},{"title":"Back to BusRightChangelog and Sources","url":"https://seedtable.com/companies/busright/funding-rounds/seed-2026-03"},{"title":"SBF 70 years logo","url":"https://www.schoolbusfleet.com/news/busright-raises-30m-to-enhance-platform-features"},{"title":"BusRight Raises $30 Million in New Funding Round","url":"https://raising.fi/news/busright-undisclosed-march-2026"},{"title":"BusRight Raises $30 Million for Student Transportation Platform","url":"https://raising.fi/news/busright-undisclosed-march-2026-1"},{"title":"edtechchronicle.com","url":"https://edtechchronicle.com/?p=10495"},{"title":"busright raises 30m to power the largest mass transit system","url":"https://edtechchronicle.com/busright-raises-30m-to-power-the-largest-mass-transit-system/"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/busright"}]

**Short answer:** Long Journey Ventures (LJV) has backed BusRight, but the premise mixes up two rounds. LJV co-invested in the 2021 seed round rather than leading it, and the 2026 round was led by Volition Capital. Only one aggregator says LJV led the 2026 round.

**2021 seed round (LJV co-invested)**
- The seed financing totaled 
… [skrátené, 2454 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Long Journey Ventures\" announces seed funding round 2025 investors include",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"San Francisco-based\" \"Long Journey Ventures\"",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Long Journey Ventures" announces seed funding round 2025 investors include"

Links: [{"title":"Hi FemWealth Friends,","url":"https://femwealth.substack.com/p/cyan-banisters-long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.everythingstartups.com/vc-funds/long-journey-ventures"},{"title":"arielle zuckerberg","url":"https://yespress.io/arielle-zuckerberg"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/long-journey-ventures"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/long-journey-ventures"},{"title":"backing the magical weirdos","url":"https://nz.dealroom.co/news/note/backing-the-magical-weirdos"},{"title":"long journey ventures","url":"https://www.briter.co/companies/long-journey-ventures"},{"title":"backing the magical weirdos","url":"https://australia-ecosystem.dealroom.co/news/note/backing-the-magical-weirdos"},{"title":"Long Journey Ventures","url":"https://www.seedtable.com/investors/long-journey-ventures"},{"title":"# Arielle Zuckerberg","url":"https://yespress.io/arielle-zuckerberg.md"}]

I didn't find a 2025 announcement in which Long Journey Ventures reported a seed round and named its investors. The results are mostly third-party profiles, not the firm's own press release, and they point to a few related items instead.

**Its 2025 news was a fund, not a seed round.** The San Francisco firm unveiled a $181.8 million vehicle, its fourth, for early-stage companies including those in AI and bioscience. Long Journey Ventures, a San Francisco-based venture capital firm, raised $181.8 million for its fourth fund focused on early-stage companies across various sectors, including artificial intelligence and bioscience. Aggregator profiles date the announcement to March 2025, with one giving March 20, 2025.

**The closest 2025 seed deal.** Seedtable's deal list includes a $100 million seed round for Substrate, a semiconductor company, dated 3 November 2025. The table doesn't mark Long Journey as the lead on that row, and it doesn't name the other investors. The table lists the Substrate seed round alongside the firm's other deals.

**A seed round outside 2025.** The same table shows a $30 million seed round for BusRight dated 18 March 2026, with the lead column marked. That's a 2026 deal, so it doesn't match your query, but it may be the one you're thinking of if the year is off.

**Conflicting details across sources:**
- Founders: Dealroom says the firm was co-founded by Cyan Banister and Arielle Zuckerberg, while Seedtable says it was founded in 2019 by Lee Jacobs.
- Portfolio size: one profile puts the firm at roughly 130 companies, while CB Insights lists 246 investments.

If you have the startup's name or a link to the announcement, I can search for that specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""San Francisco-based" "Long Journey Ventures""

Links: [{"title":"Long Journey Ventures","url":"https://signal.nfx.com/firms/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.seedtable.com/investors/long-journey-ventures"},{"title":"long journey ventures","url":"https://www.briter.co/companies/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.deep-tech-week.com/organizations/long-journey-ventures"},{"title":"Investor type","url":"https://privateequitylist.com/investors/long-journey-ventures"},{"title":"Venture Capital","url":"https://altss.com/profile/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.fusionenergybase.com/organizations/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://www.everythingstartups.com/vc-funds/long-journey-ventures"},{"title":"Long Journey Ventures","url":"https://venturecapitalarchive.com/venture-funds/long-journey-ventures-longjourney-vc"},{"title":"long journey ventures","url":"https://vcbeast.com/claim/long-journey-ventures"}]

Most profiles place Long Journey Ventures in San Francisco, though some details conflict across sources.

**Basics**
- Briter's page calls it a San Francisco venture firm that concentrates on early-stage deals, founded in 2019 that focuses on early-stage investments.
- Jacobs launched the fund in 2019, with earlier roles in angel investing and at M13 behind him after a career that spanned angel investing, a role at M13.
- Arielle Zuckerberg shares investment decisions with Jacobs alongside Partner Arielle Zuckerberg.

**Focus and portfolio**
- Pre-seed and seed rounds are where it most often puts money to work Long Journey focuses on pre-seed and seed rounds.
- Enterprise software, AI, fintech, digital health, and climate software show up as its target areas The firm participates in priced rounds and stakes across enterprise software, AI/ML, fintech infrastructure, digital health, and climate software.
- RTFKT, AtoB, and LimaCharlie are among the companies one profile highlights Some of Long Journey Ventures' notable investments include.

**Fund size and check size**
- Its most recent fund came in at about $181.8 million, per a March 2025 announcement Long Journey Ventures raised $181.8 million for its latest fund, announced on March 20, 2025.
- Lifetime fundraising is put at $450 million, with around 130 backed companies This brings the firm's total capital raised to $450 million, having invested in approximately 130 companies to date.
- Typical checks are reported inconsistently. One source puts them between $100K and $1M typical investment check size ranges from $100K to $1M, another gives $500K to $2M They provide funding ranging from $500K to $2M per investment, and a third claims an average of $10–50 million, which seems out of line with seed-stage investing usually invests $10-50 m on average.

**Location caveat**
- NFX's profile lists Austin, Texas, San Fra
… [skrátené, 576 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.thetrustedinsight.com/investment-news/busright-picks-up-25m-seed-funding-from-underscore-vc-long-journey-ventures-yap633oCJbux7ZuGkF7hoN-20210331418/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or headline that mentions BusRight, Long Journey Ventures, Underscore VC, seed funding, $2.5 million, or investors, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "BusRight $7 million Series A Las Olas Venture Capital Ubiquity Underscore Long Journey Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
certificate has expired
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "BusRight $7 million Series A Las Olas Venture Capital Ubiquity Underscore Long Journey Ventures"

Links: [{"title":"BusRight: $7 Million Raised To Advance Safe And Efficient School Bus Technology","url":"https://pulse2.com/busright-7-million-funding/amp/"},{"title":"SBF 70 years logo","url":"https://www.schoolbusfleet.com/news/busright-secures-another-7-million-in-funding"},{"title":"BusRight Grabs $7 Million in Series A Funding","url":"https://locationbusinessnews.com/busright-grabs-7-million-in-series-a-funding"},{"title":"sp-edge.com","url":"https://sp-edge.com/updates/20360"},{"title":"locationbusinessnews.com","url":"https://locationbusinessnews.com/?p=2203"},{"title":"Northeastern grads’ startup BusRight gets $7M boost in venture capital investment","url":"https://news.northeastern.edu/?p=190931"},{"title":"www.citybiz.co","url":"https://www.citybiz.co/?p=443756"},{"title":"Northeastern grads’ startup BusRight gets $7M boost in venture capital investment","url":"https://news.northeastern.edu/2023/07/26/busright-startup-private-equity-investment/"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/busright"},{"title":"Looking for our Business Solutions? Click here:CloudQuote APIsContact Us","url":"https://www.financialcontent.com/article/bizwire-2023-7-20-busright-secures-7-million-to-transform-the-largest-mass-transit-system-in-the-us-school-buses"}]

BusRight's $7 million Series A was led by Las Olas Venture Capital, and the search results agree on the main terms.

- **Timing:** CB Insights dates the raise to July 2023. In July 2023, the company secured $7 million in series A funding in large part from Las Olas Venture Capital.
- **Other investors:** Ubiquity Ventures, which led the earlier round, also took part, along with Underscore VC, Long Journey Ventures, SilverCircle, Automotive Ventures, Alumni Ventures, CreativeCo Capital, and several angel investors. Additional participating investors include prior round lead Ubiquity Ventures, as well as Underscore VC, Long Journey Ventures, SilverCircle, Automotive Ventures, Alumni Ventures, CreativeCo Capital, and several prominent angel investors.
- **Use of funds:** The money is earmarked for doubling employee headcount, accelerating product development, and expanding its customer base among U.S. K-12 education transportation systems.
- **Board seat:** Las Olas gains a board seat through its founding partner, Mark Volchek. He will also join the company's board of directors.
- **Traction:** School Bus Fleet reports a presence in 23 states and nearly 10X annual revenue growth. It also describes the round as following a $2.5 million in venture capital funding award about two years earlier.
- **Revenue growth:** Northeastern reports that BusRight grew revenue more than 700% in 2022 alone. CB Insights adds that the company's revenue grew 9x in 2023.

The search also turned up a conflicting data point. A CB Insights company profile lists a Series B as
… [skrátené, 262 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Substrate $100 million seed round investors Long Journey Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://pulse2.com/busright-7-million-funding/amp/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions BusRight, Long Journey Ventures, Series A, $7 million, Las Olas, or the investors, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** Aug 3, 2023

**Headline:** "BusRight: $7 Million Raised To Advance Safe And Efficient School Bus Technology"

**Funding round:** The article says BusRight "raised a $7 million Series A funding round led by Las Olas Venture Capital."

**Investors:** "Participating investors include prior round lead Ubiquity Ventures, Underscore VC, Long Journey Ventures." The article also names SilverCircle, Automotive Ventures, Alumni Ventures, and CreativeCo Capital, plus several angel investors.

**Use of funds:** "BusRight will use the funding to double its employee headcount." The company also plans to accelerate product development and expand its customer base among U.S. K-12 transportation systems.

**Board change:** "the Founding Partner at Las Olas Venture Capital, Mark Volchek, will join the company's Board of Directors."

I've omitted other sentences that mention BusRight, such as those describing its products, customers, and growth metrics, to keep this response concise.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Substrate $100 million seed round investors Long Journey Ventures"

Links: [{"title":"www.preqin.com","url":"https://www.preqin.com/data/profile/asset/substrate-inc-/775330"},{"title":"Back to SubstrateChangelog and Sources","url":"https://seedtable.com/companies/substrate/funding-rounds/seed-2025-11"},{"title":"Long Journey Ventures","url":"https://www.seedtable.com/investors/long-journey-ventures"},{"title":"Your Source for Venture Capital and Private Equity Financings","url":"https://www.vcnewsdaily.com/Substrate/venture-capital-funding/kbrglzfxkk"},{"title":"Your Source for Venture Capital and Private Equity Financings","url":"https://vcnewsdaily.com/substrate/venture-capital-funding/kbrglzfxkk"},{"title":"substrate san francisco","url":"https://www.vcbacked.co/company/substrate-san-francisco"},{"title":"www.tipranks.com","url":"https://www.tipranks.com/private-companies/pc:subst"},{"title":"Substrate Raises $100M to Challenge ASML","url":"https://datacommons.dealroom.co/news/feed/substrate-raises-100m-to-challenge-asml"},{"title":"Back to Substrate","url":"https://www.seedtable.com/companies/substrate/changelog"},{"title":"Substrate logo","url":"https://www.tryfundable.ai/company/substrate-1"}]

Yes, Long Journey Ventures is one of the investors in Substrate's $100 million round, though the sources differ on the round's stage and the size of each investor's share.

**Round and investors:** Preqin's profile dates the raise to October 28, 2025, and lists Long Journey Ventures among six backers, alongside Founders Fund, General Catalyst, Allen & Company, Valor Equity Partners, and In-Q-Tel. (The company raised USD 100 mn in its most recent funding round on October 28, 2025, with investments from Founders Fund, General Catalyst Partners, Allen & Company, Long Journey Ventures, Valor Equity Partners, and In-Q-Tel.) Massinvestor's coverage names the same group and describes In-Q-Tel as a government-run nonprofit that funds defense and intelligence technology (The company is being backed by high-profile investors including Peter Thiel's Founders Fund, General Catalyst, Allen & Co, Long Journey Ventures, Valor Equity Partners and In-Q-Tel).

**Valuation:** Bloomberg-sourced coverage says the company emerged from stealth while raising at a $1 billion valuation (Substrate, a San Francisco-based chip startup backed by Peter Thiel, has emerged from stealth mode, raising $100 million at a $1 billion valuation.).

**Lead and individual checks:** SeedTable lists Founders Fund as the lead and estimates its share at about $37.5 million, with roughly $12.5 million each for the other participants, including Long Journey Ventures. It stresses that these splits are modeled, because individual check sizes are rarely disclosed (Allocations are estimated — the headline 100.0M USD split across backers by weighting lead investors above participants, since per-investor cheque sizes are rarely disclosed. For guidance only.). Treat the Lon
… [skrátené, 1080 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.substrate.com/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions funding, raised, $100 million, investors, Founders Fund, Long Journey Ventures, seed, Series A, or a date of an announcement, exactly as shown on the page. If nothing matches, say so."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
No sentences on the page match those terms. The page doesn't mention funding, amounts raised, investors, Founders Fund, Long Journey Ventures, seed or Series A rounds, or announcement dates. The only year shown is in the footer ("Substrate © 2026"), which is a copyright notice, not an announcement date.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Smart Management VC s.r.o. startup seed investícia investícia do startupov",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Smart Management VC s.r.o. startup seed investícia investícia do startupov"

Links: [{"title":"The way to seed startups","url":"https://techcrunch.com/?p=501662"},{"title":"encomenda smart capital","url":"https://privateequitylist.com/investor/encomenda-smart-capital"},{"title":"smart partnership capital","url":"https://superscout.co/investor/smart-partnership-capital"},{"title":"The CNMV authorizes creation of Encomenda Smart Capital, a specialized seed investment manager in technological startups","url":"https://www.ttrdata.com/en/radar/aggregated/The-CNMV-authorizes-creation-of-Encomenda-Smart-Capital-a-specialized-seed-investment-manager-in/251371"},{"title":"smart capital gmbh hamburg germany","url":"https://superscout.co/investor/smart-capital-gmbh-hamburg-germany"},{"title":"Encomenda Smart Capital","url":"https://privateequitylist.com/investors/encomenda-smart-capital"},{"title":"smart capital","url":"https://superscout.co/investor/smart-capital"},{"title":"smartinvest ventures","url":"https://privateequitylist.com/investors/smartinvest-ventures"},{"title":"Join Vestbee","url":"https://www.vestbee.com/vc-list/encomenda"}]

Links: [{"title":"Fiedler Capital – penetrácia VC na Slovensku je stále nízka","url":"https://www.startitup.sk/fiedler-capital-penetracia-vc-na-slovensku-je-stale-nizka/"},{"title":"Investície do startupov","url":"https://www.podnikajte.sk/investor/investicie-startupy"},{"title":"Slovensko zaostáva v investíciách do startupov v oblasti zdravotníctva. V čom sa musí zlepšiť?","url":"https://sita.sk/vzdravotnictve/slovensko-zaostava-v-investiciach-do-startupov-v-oblasti-zdravotnictva-v-com-sa-musi-zlepsit/"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Popularita private equity a venture kapitálu na Slovensku","url":"https://www.podnikajte.sk/investor/private-equity-venture-kapital-na-slovensku"},{"title":"Ako to vyzerá s Venture capitalom na Slovensku?","url":"https://www.startitup.sk/limerock-fund-manager/"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"},{"title":"Podnikateľ a investor","url":"https://www.podnikajte.sk/investor?page=5"},{"title":"venture capital recruitment","url":"https://kitalent.com/sk/financial-services-and-professional-services-recruitment/venture-capital-recruitment/"}]

I couldn't find anything about **Smart Management VC s.r.o.** in either of my two searches (one in English, one in Slovak). The results don't confirm that the company exists, and I can't tell you its investment focus, fund size, or portfolio.

Some similarly named investors did come up. They may be unrelated, so don't treat
… [skrátené, 1676 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b08.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b08.json",
  "content": "[\n  {\n    \"candidate_id\": \"C158\",\n    \"website\": \"https://www.longjourney.vc\",\n    \"identity\": [],\n    \"hq_country\": null,\n    \"investor_type\": {\"value\": [\"vc\"], \"value_text\": \"Early Stage Investing\", \"source_url\": \"https://www.longjourney.vc\", \"quote\": \"Long Journey Ventures - Early Stage Investing for the long-term.\", \"published_date\": null, \"derivation\": \"inferred\"},\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [],\n    \"not_found\": [\"identity\", \"hq_country\", \"sectors\", \"stages\", \"ticket\", \"total_capital\", \"funds\", \"investments\"],\n    \"early_exit\": null,\n    \"search_log\": [\n      \"Long Journey Ventures investice\",\n      \"Long Journey Ventures led seed round 2025 San Francisco\",\n      \"VectorShift seed round Long Journey Ventures\",\n      \"Long Journey Ventures $181.8 million fund San Francisco-based venture firm\",\n      \"BusRight seed round Long Journey Ventures led 2026\",\n      \"\\\"Long Journey Ventures\\\" announces seed funding round 2025 investors include\",\n      \"\\\"San Francisco-based\\\" \\\"Long Journey Ventures\\\"\",\n      \"BusRight $7 million Series A Las Olas Venture Capital Ubiquity Underscore Long Journey Ventures\",\n      \"Substrate $100 million seed round investors Long Journey Ventures\"\n    ]\n  },\n  {\n    \"candidate_id\": \"C093\",\n    \"website\": null,\n    \"identity\": [],\n    \"hq_country\": null,\n    \"investor_type\": null,\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [\n      {\"value\": \"no investment found\", \"value_text\": null, \"source_url\": null, \"quote\": null, \"published_date\": null, \"derivation\": \"stated\"}\n    ],\n    \"not_found\": [\"identity\", \"hq_country\", \"investor_type\", \"investments\", \"sectors\", \"stages\", \"ticket\", \"total_capital\", \"funds\"],\n    \"early_exit\": \"no_investment_found\",\n    \"search_log\": [\n      \"Smart Management VC s.r.o. investice\",\n      \"\\\"Smart Management VC\\\" fond\",\n      \"\\\"Smart Management VC\\\" startup investuje\",\n      \"\\\"Smart Management VC\\\"\",\n      \"Smart Management VC s.r.o. startup seed investícia investícia do startupov\"\n    ]\n  },\n  {\n    \"candidate_id\": \"C169\",\n    \"website\": \"https://www.quadrillecapital.com\",\n    \"identity\": [],\n    \"hq_country\": {\"value\": \"other\", \"value_text\": \"Paris, France\", \"source_url\": \"https://www.quadrillecapital.com\", \"quote\": \"16, place de la Madeleine 75008 Paris, France\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"investor_type\": {\"value\": [\"pe\"], \"value_text\": \"Growth Equity\", \"source_url\": \"https://www.quadrillecapital.com\", \"quote\": \"Investments in Growth Equity companies,\", \"published_date\": null, \"derivation\": \"inferred\"},\n    \"investments\": [],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": {\"value\": {\"amount\": \"€1.6bn\", \"currency\": \"EUR\", \"capital_type\": \"aum\", \"as_of\": null}, \"value_text\": \"€1.6bn Assets Under Management\", \"source_url\": \"https://www.quadrillecapital.com\", \"quote\": \"€1.6bn Assets Under Management\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"funds\": [],\n    \"red_flags\": [],\n    \"not_found\": [\"identity\", \"sectors\", \"stages\", \"ticket\", \"funds\", \"investments\"],\n    \"early_exit\": \"foreign_hq\",\n    \"search_log\": [\n      \"Quadrille venture capital investice\"\n    ]\n  },\n  {\n    \"candidate_id\": \"C135\",\n    \"website\": \"https://www.seedstarter.cz\",\n    \"identity\": [\n 
… [skrátené, 6132 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b08.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b08 done. Output: C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b08.json\n\nC158 Long Journey Ventures: VC (early-stage), 0 recorded investments, no early exit. Unrecorded: BusRight 2023 and Substrate 2025 LP/co-investor reports, but no verbatim quote naming both firm and company. HQ not stated on its site.\nC093 Smart Management VC s.r.o.: no website or investment found after 5 searches, early exit no_investment_found.\nC169 Quadrille: foreign_hq (Paris), AUM EUR 1.6bn from its site. Registry hint not used.\nC135 Seed Starter (ČS Seed Starter a.s.): cvc, 7 investments, no early exit. Doubt: the Definic and Repsense quotes name the company but not Seed Starter in the same sentence. Seedstarter.cz portfolio page 404, so investments come from press.\nC181 Wing VC: foreign_hq (Palo Alto), no investment work.\n\nWebsite matches for Wing, Quadrille and Long Journey are assumed from name."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

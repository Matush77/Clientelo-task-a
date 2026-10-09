# Subagent: Evidence v3 wave2 batch 14 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:10:37

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b14.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b14.json

Today is 2026-10-08.

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\prompts\\evidence_agent.md"
}
````

</details>

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b14.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b14.json"
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
3	    "candidate_id": "C018",
4	    "name": "Genesis Capital",
5	    "other_names": [
6	      "Genesis Capital Equity s.r.o."
7	    ],
8	    "known_website": "www.genesis.cz",
9	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Genesis Capital Equity s.r.o., IČO 25795856"
10	  },
11	  {
12	    "candidate_id": "C036",
13	    "name": "Versute Investments",
14	    "other_names": [],
15	    "known_website": "www.versute.cz",
16	    "registry_hint": "possible registry match (unconfirmed, may be a different company): VERSUTE INVESTMENTS a.s., IČO 03965953"
17	  },
18	  {
19	    "candidate_id": "C171",
20	    "name": "European Investment Bank (EIB)",
21	    "other_names": [],
22	    "known_website": null,
23	    "registry_hint": null
24	  },
25	  {
26	    "candidate_id": "C183",
27	    "name": "Genesis Growth Equity Fund I",
28	    "other_names": [],
29	    "known_website": null,
30	    "registry_hint": null
31	  },
32	  {
33	    "candidate_id": "C176",
34	    "name": "Kaya Ventures",
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

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.genesis.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Genesis Capital, investments, portfolio, fund size, ticket, team, office address, IČO, or the page's publication date. Also list the navigation links (portfolio, about, team, kontakt) with their URLs."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.versute.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Versute, investments, portfolio, fund size, ticket, team, office address, IČO, or the page's publication date. Also list the navigation links (portfolio, about, team, kontakt) with their URLs."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Kaya Ventures investment fund",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Genesis Growth Equity Fund\" I",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "European Investment Bank headquarters Luxembourg equity investments venture capital",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences mentioning Genesis Capital, investments, fund size, ticket size, or office address** (Czech originals; the 125-character limit means some are truncated with "…"):

1. "Fondy se orientují na investice do malých a středních podniků v České republice, na Slovensku…"
2. "Fondy zaměřené na investice do menších a středně velkých společností v České republice a na Slovensku…"
3. "Jsme společnost, která už od roku 1999 pomáhá v rozvoji malým a středním podnikům…"
4. "Podíleli jsme se na podpoře růstu a rozvoje více než 90 podniků z nejrůznějších sektorů ekonomiky."
5. "Mnohé z těchto firem se i díky spolupráci s Genesis Capital dostaly na špičku ve svém oboru."
6. "Řídíme se jasnými investičními kritérii."
7. "K financování využíváme kapitál, který do fondů Genesis s důvěrou vkládají renomovaní institucionální investoři…"
8. "Od založení Genesis Capital v roce 1999 vzniklo postupně sedm fondů privátního kapitálu…"
9. "Aktuálně je k investování otevřen fond Genesis Private Equity Fund V (GPEF V) o velikosti 225 milionů eur…"
10. "s obyklou velikostí jednotlivé investice 10-35 milionů euro."
11. "Aktuálně je k investování otevřen fond Genesis Growth Equity Fund I (GGEF I) o velikosti 40 milionů euro…"
12. "s obvyklou velikostí jednotlivé investice 1-4 miliony euro."
13. "Copyright © 2026 Genesis Capital. All rights reserved."

**Key statistics:** "7 investičních fondů", "EUR 550 mil. pro podniky", and "90 investic".

**Office address:** "Na Šafránce 22, 101 00 Praha 10, Česká republika" (listed for both Genesis Capital Equity s.r.o. and Genesis Capital Growth s.r.o.).

**Not found on the page:**
- **IČO:** no company registration number is present.
- **Publication date:** the only date is the copyright year, 2026.
- **Portfolio or team sections:** none are present.

**Navigation links:**
- About: [O Genesis Capital](/o-genesis-capital)
- Kontakt: [Kontakt](/kontakt)
- Private Equity: [Private Equity](/private-equity)
- Growth Equity: [Growth Equity](/growth-equity)
- Kariéra: [Kariéra](/kariera)

The page has no portfolio or team links, so I've listed the closest matches.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Genesis Growth Equity Fund" I"

Links: [{"title":"Genesis Growth Equity Fund I Overview","url":"https://pitchbook.com/profiles/fund/16343-56F"},{"title":"genesis to launch eur40m growth fund","url":"https://www.unquote.com/cee/official-record/3010100/genesis-to-launch-eur40m-growth-fund"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/genesis-growth-equity-fund"},{"title":"genesis growth equity","url":"https://www.crunchbase.com/organization/genesis-growth-equity"},{"title":"genesis capital launches eur150m fund","url":"https://www.unquote.com/cee/news/3019947/genesis-capital-launches-eur150m-fund"},{"title":"Genesis Capital to launch a new private equity fund with a target size of EUR 250 million","url":"https://psik.org.pl/en/research-and-reports/market-information/genesis-capital-to-launch-a-new-private-equity-fund-with-a-target-size-of-eur-250-million"},{"title":"Genesis announces strong year of investment","url":"https://www.amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"Private equity","url":"https://www.startbase.com/news/genesis-capital-expandiert-nach-deutschland-und-bringt-275-millionen-euro-mit/"},{"title":"Genesis Private Equity Fund V Scsp","url":"https://www.developmentaid.org/organizations/view/624829/genesis-private-equity-fund-v-scsp"}]

I searched for "Genesis Growth Equity Fund." The results all refer to Genesis Growth Equity Fund I, so I assumed the trailing "I" is part of the name.

**Overview:** PitchBook describes it as a growth fund managed by Genesis Capital, based in Prague, that invests in Slovakia and the Czech Republic. Genesis Growth Equity Fund I is a 2020 vintage private equity growth and expansion fund managed by Genesis Capital. Other sources date it differently: It was founded in 2019 and is based Praha, Czech Republic.

**Size:** The fund was announced with a target of €40m, and Genesis Capital has recently held a €31m first close for Genesis Growth Equity Fund I, against a €40m target.

**Strategy:** The fund focuses on smaller companies. PitchBook says it targets the information technology sector, with businesses with revenues of up to EUR 15 million and EBITDA up to EUR 2 million. Sources disagree on typical investment size: PitchBook gives €1–4 million, while CB Insights says the usual size of an individual investment between EUR 2 and 6 million.

**Portfolio:** PitchBook lists 10 investments, and its most recent deal is with Cross Masters, made on 13-Nov-2025. CB Insights reports only one investment, so the counts differ. One known exit: JSK has advised the Genesis Growth Equity Fund I on its sale of the Homecare Holding to the Penta Group in April 2024.

**Recent development:** A June 2026 AmCham Czech notice says Genesis Capital's recent decision not to replicate for a successor fund the co-operation with a separate team established in connection with Genesis Growth Equity Fund I. While operations of GGEF I re
… [skrátené, 420 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "European Investment Bank headquarters Luxembourg equity investments venture capital"

Links: [{"title":"P+P advises European Investment Bank on equity investment in coparion","url":"https://pplaw.com/en/transactions/pp-advises-european-investment-bank-equity-investment-coparion"},{"title":"European Investment Bank","url":"https://www.circularcityfundingguide.eu/?p=212"},{"title":"EIF increases VC commitments","url":"https://www.buyoutsinsider.com/eif-increases-vc-commitments-2/"},{"title":"www.eib.org","url":"https://www.eib.org/projects/topics/innovation-digital-and-human-capital/techeu/platform"},{"title":"www.africaprivateequitynews.com","url":"https://www.africaprivateequitynews.com/p/eib-mulls-investment-in-badia-impact-fund-ii/comments"},{"title":"An official entity: European Innovation Council Equity Fund for high-impact innovation - European Commission","url":"https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/official-entity-european-innovation-council-equity-fund-high-impact-innovation-2020-06-23_en"},{"title":"An official entity: European Innovation Council Equity Fund for high-impact innovation - European Commission","url":"https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/official-entity-european-innovation-council-equity-fund-high-impact-innovation-2020-06-23_nl"},{"title":"poellath advises european investment bank eib equity investment wachstumsfonds bayern","url":"https://www.pplaw.com/en/transactions/poellath-advises-european-investment-bank-eib-equity-investment-wachstumsfonds-bayern"},{"title":"EIB considers investment in startup fund","url":"https://www.africaprivateequitynews.com/p/eib-considers-investment-in-startup-fund"},{"title":"www.africaprivateequitynews.com","url":"https://www.africaprivateequitynews.com/p/eib-considers-investment-in-startup-fund/comments"}]

The search results don't say where the EIB is headquartered. From general knowledge, I believe it's based in Luxembourg, but these sources don't confirm that, so check eib.org. They do cover how the EIB makes equity and venture capital investments.

**Direct stakes in individual funds**
- A EUR 50 million commitment to coparion, a German co-investment fund, came from the EIB, and that round increased the fund volume to EUR 275 million after the EIB investment. The fund invests in young, technology-oriented companies with strong growth potential.
- The EIB supplied EUR 50 million risk financing to 'Wachstumsfonds Bayern 2' (WFB 2), a venture capital fund set up on the initiative of the Free State of Bavaria. That brought the fund to the target size of EUR 165 million.
- Smaller, reported proposals include a stake of up to $10 million in the Badia Impact Fund II and a proposed equity participation of up to $20 million into Seedstars Africa Ventures 1. These were proposals, and I didn't find confirmation that they closed.

**Indirect investment through the European Invest
… [skrátené, 1892 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences mentioning the requested keywords** (quotes capped at 125 characters; longer sentences are truncated with "…")

- "Versute Investments je investiční a poradenská společnost působící jako manažer Private Equity fondů…"
- "Investujeme do malých a středních podniků prostřednictvím Private Equity fondů."
- "Jsme investiční a poradenskou společností působící jako manažer Private Equity fondů investujících…"
- "Investujeme rovněž vlastní kapitál formou co-investic a aktivně řídíme portfoliové společnosti fondů."
- "V současné době jsme manažerem (General Partnerem) VERSUTE Funds SICAV a.s.."
- "Luděk působí v oblasti Private Equity a Venture Capital již od roku 1994 a je zakladatelem Versute Investments."
- "Luděk byl součástí mnoha investic a úspěšných exitů po celé Evropě."
- "Jan spolupracuje s Versute Investments od roku 2015."
- "Jan ve své kariéře zastával již několik pozic v řídících orgánech portfoliových společností a aktuálně působí…"
- "Bohumil také spolupracuje s Versute Investments od roku 2015."
- "Ve své kariéře již zastával několik pozic v řídících orgánech portfoliových společností…"
- "Marek, člen výběru Forbes 30 pod 30 2024, se k týmu připojil v roce 2019."
- "Dříve působil na Ministerstvu financí, ve společnostech Penta Investments, JetBrains, Exxonmobil, CBRE a EY."
- "Předtím, než se Martin připojil k týmu v roce 2023, pracoval v CzechTrade v Chicagu a jako business…"
- "Martin se k týmu připojil v roce 2025."
- "Tomáš se k týmu připojil v roce 2025."
- "Versute Investments a private equity fond kupují podíl ve společnosti Unipap" (news headline, 24.9.2025)
- "Versute Investments a private equity fond kupují podíl ve společnosti ALFA 3, s.r.o." (news headline, 4.8.2025)
- "Adresa pracoviště:" / "Vodičkova 33, 110 00 Praha 1"
- "Copyright 2025, All Right Reserved, Versute Investments a.s."

**Not found on the page:** fund size, ticket size, IČO, and an explicit publication date for the page. The only dates are the copyright year (2025) and the dates of news items (17.3.2026 through 15.5.2025).

**Navigation links:**
- Úvod: https://versute.cz/cs_cz/
- Reference: https://versute.cz/cs_cz/sluzby/private-equity/#referencni-projekty
- Private Equity: https://versute.cz/cs_cz/sluzby/private-equity/
- Public Equity: https://versute.cz/cs_cz/sluzby/public-equity/
- Poradenství: https://versute.cz/cs_cz/sluzby/poradenstvi/
- Kontakt: https://versute.cz/cs_cz/kontakt/
- English: https://versute.cz/en/

The navigation has no separate "portfolio", "about", or "team" links. The closest matches are the Private Equity and Reference links, and the "O nás" and "Tým" sections appear only as page headings.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Kaya Ventures investment fund"

Links: [{"title":"kaya ventures","url":"https://www.vestbee.com/vc-list/kaya-ventures"},{"title":"kayan ventures","url":"https://superscout.co/investor/kayan-ventures"},{"title":"Check size","url":"https://capboard.io/en/investor/kaya-ventures"},{"title":"The KAYA VC team","url":"https://techcrunch.com/?p=2132469"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/kayan-ventures"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/kaya-ventures/financials"},{"title":"Kaya Ventures","url":"https://venturecapitalarchive.com/venture-funds/kaya-ventures-kaya-ventures"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/kaya-ventures-raises-100k-funding"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/kayan-ventures"}]

Several unrelated firms use the name "Kaya Ventures," so the results cover more than one organization.

**1. Kaya VC (Prague, Central and Eastern Europe)**
This is the best-documented fund under this name.
- Its roots go back to Enern Investments, a regional financial group formed in Prague in 2010. The VC later took the Kaya name to better match its current focus, moving away from its early wind-farm investments and toward software.
- Its newest fund is about €72 million (roughly $80 million) and targets startups in Prague, Warsaw and the wider CEE region. It can back companies at any stage of funding.
- It aims to fill the early-stage funding gap by offering growth capital to pre-seed and seed startups in the region, and it has more than €70 million under management ().
- The European Investment Fund is among its limited partners, along with regional entrepreneurs ().
- This is the team's fourth fund. Including earlier vehicles, its assets reach about €250 million, and it has invested in 27 companies ().
- Past investments include Booksy, Twisto, DocPlanner and Rohlik ().
- It describes itself as sector-agnostic, with partners pursuing personal interests such as agri-tech and fintech (). Each partner can decide on deals independently, which the firm calls an "equal partnership" ().

**2. Kaya Ventures (Massachusetts, United States)**
- This early-stage VC is led by Madeline Darcy and focuses on expanding access to wellness ().
- CB Insights counts 16 investments. The most recent was a Series A in E2B on July 28, 2025 ().
- A Signalbase funding-news item reports the firm secured $100K in new capital to support operations while it backs pre-seed health companies (). A fund raising its own money this way is unusual, so this figure may be incomplete.

**3. A possible third Kaya Ventures (consumer focus)**
- A Capboard profile describes a firm of this name that supports founders from the earliest stages, with checks of $100K to $500K (). Its focus areas include consumer, food and beverage, cannabis and healthcare (). The results don't clarify whether this is the same firm as the US one.

**Not the 
… [skrátené, 629 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.genesis.cz/kontakt",
  "prompt": "Return word-for-word, without summarising or translating, every line that contains a company name (s.r.o., a.s., Genesis), an address (Praha, Na Šafránce), IČO, or the email/phone block. Copy each full line exactly as written on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.genesis.cz/growth-equity",
  "prompt": "Return word-for-word, without summarising or translating, every full sentence on this page that mentions GGEF, Genesis Growth Equity Fund, fund size, investment size, portfolio companies, investments, or the page's publication date. Do not truncate sentences."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://versute.cz/cs_cz/kontakt/",
  "prompt": "Return word-for-word, without summarising or translating, every line that contains a company name (s.r.o., a.s., Versute), an address (Praha, Vodičkova), IČO, or the email/phone block. Copy each full line exactly as written on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eib.org/en/index.htm",
  "prompt": "Return word-for-word, without summarising or translating, the postal address of the European Investment Bank headquarters as shown on this page (or any sentence stating where the EIB is headquartered), and one sentence describing what the EIB is. Copy exactly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Kaya VC Prague venture capital fund official website",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.genesis.cz/growth-equity
    Redirect URL (from the server's Location header — server-supplied, not verified): https://growth.genesis.cz/
    Status: 302 Found

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://growth.genesis.cz/"
    - prompt: "Return word-for-word, without summarising or translating, every full sentence on this page that mentions GGEF, Genesis Growth Equity Fund, fund size, investment size, portfolio companies, investments, or the page's publication date. Do not truncate sentences."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page does not include a postal address for EIB headquarters, and it doesn't state where the EIB is headquartered.

The page describes the EIB as: "The European Investment Bank is one of the world’s main financers of climate action."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
```
Kontakt | Genesis Capital
[![Genesis Capital](/frontend/images/logo_genesis_capital.svg)](/)
[Genesis Capital](/) ▶ Kontakt
![Genesis Capital - Private Equity Funds](/frontend/images/genesis-private-logo.png)
Genesis Capital Equity s.r.o.
Na Šafránce 22
101 00 Praha 10
+420 271 740 207
[genesis@genesis.cz](mailto:genesis@genesis.cz)
![Genesis Capital - Grow Equity Funds](/frontend/images/genesis-growth-logo.png)
Genesis Capital Growth s.r.o.
Na Šafránce 22
101 00 Praha 10
+420 271 740 207
[growth@genesis.cz](mailto:growth@genesis.cz)
![Genesis Capital](/frontend/images/footer_logo_genesis_capital.png)
**Genesis Capital Equity s.r.o.**
Na Šafránce 22
101 00 Praha 10
[genesis@genesis.cz](mailto:genesis@genesis.cz)
+420 271 740 207
**Genesis Capital Growth s.r.o.**
Na Šafránce 22
101 00 Praha 10
[growth@genesis.cz](mailto:growth@genesis.cz)
+420 271 740 207
Copyright © 2026 Genesis Capital. All rights reserved.
```

Note: Trailing markdown line-break spaces have been removed. No IČO appears on the page.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Lines containing the company name, address, or contact details:

- Název společnostiVERSUTE INVESTMENTS a.s.
- Pracoviště a doručovací adresaVodičkova 33, 110 00 Praha 1
- Sídlo firmyVodičkova 33, 110 00 Praha 1
- Kontaktní e-mailludek.palata@versute.cz; marek.subrt@versute.cz
- ### [Versute investiční společnost, a.s.](https://versuteis.cz/)
- ### Versute Investments a private equity fond kupují podíl ve společnosti ALFA 3, s.r.o.
- ### Versute Investments a BHS PE Fond koupili společnost Tiyo a.s., dříve Altran CZ
- ### Versute Investments získala ocenění Private Equity deal roku za IPO společnosti Gevorkyan
- ### Versute Investments je hlavní poradce společnosti Gevorkyan při vstupu na pražskou burzu.
- Copyright 2025, All Right Reserved, Versute Investments a.s.
- ### E-mail:
- [ludek.palata@versute.cz](mailto:ludek.palata@versute.cz)
- ### Adresa pracoviště:
- [Vodičkova 33, 110 00 Praha 1](Vodičkova 33, 110 00 Praha 1)

The page does not contain an IČO (company registration number).
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Kaya VC Prague venture capital fund official website"

Links: [{"title":"KAYA Investor","url":"https://mindmaps.femtech.health/firms/66161"},{"title":"Kaya VC Overview","url":"https://pitchbook.com/profiles/investor/126966-07"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/kaya-vc"},{"title":"kaya vc","url":"https://privateequitylist.com/investors/kaya-vc"},{"title":"kaya vc","url":"https://capboard.io/en/investor/kaya-vc"},{"title":"altss.com","url":"https://altss.com/profile/kaya.md"},{"title":"venture capital firms prague","url":"https://www.papermark.com/blog/venture-capital-firms-prague.md"},{"title":"kaya vc launches its new $80m fund","url":"https://business.dptribune.com/dptribune/news/read/41167642/kaya_vc_launches_its_new_$80m_fund"},{"title":"kaya vc","url":"https://www.premieralts.com/investors/kaya-vc"}]

The firm's website is **www.kaya.vc**. PitchBook's profile lists that domain for Kaya VC Website www.kaya.vc, and a separate company profile gives the same address Website: www.kaya.vc. This search did not return the site itself, so check the address directly before relying on it.

Other details from the results:

- **Contact:** A FemTech directory entry lists the email info@kaya.vc and the Twitter handle twitter.com/kaya_vc. Headquarters: Prague, Hlavni mesto Praha, Czech Republic, and PitchBook gives a Karlín office address on Thámova street.
- **Origins:** The firm originated as Enern Investments in 2010 and evolved into Kaya VC as a dedicated successor vehicle. A 2021-era news report says the name change was meant to reflect its newer focus.
- **Funds:** Waveup reports that Kaya's fifth fund closed at €70 million in 2025.
- **Team:** Waveup names Karel Zheng, Tomas Obrtac, and Martin Rajcan among the General Partners. An altss profile also lists Tomas [REDACTED]a as a General Partner.

The sources disagree on some figures. Assets under management appear as €270 million in total assets under management across five funds in one profile, and as $317.1M in another. Most sources give 2010 as the founding year, but altss lists 2011. Treat these numbers as approximate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://growth.genesis.cz/",
  "prompt": "Return word-for-word, without summarising or translating, every full sentence on this page that mentions GGEF, Genesis Growth Equity Fund, fund size, investment size, portfolio companies, investments, or the page's publication date. Do not truncate sentences. Also return the company name and address shown in the footer, if any."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.genesis.cz/o-genesis-capital",
  "prompt": "Return word-for-word, without summarising or translating, every full sentence on this page that mentions Genesis Capital, funds, investments, companies, capital (EUR, mil.), investment size, or the page's publication date. Do not truncate sentences. Also list the navigation menu link names and URLs, including any link to portfolio or investments."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://versute.cz/cs_cz/sluzby/private-equity/",
  "prompt": "Return word-for-word, without summarising or translating, every full sentence or headline on this page that mentions Versute, investments, portfolio, reference projects, companies bought, fund names, fund sizes, or dates. Do not truncate. Also list the names of the portfolio/reference companies shown, each with its date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "eib.org contact European Investment Bank 98-100 boulevard Konrad Adenauer Luxembourg",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.kaya.vc",
  "prompt": "Return word-for-word, without summarising or translating, every full sentence on this page that mentions Kaya, funds, investments, portfolio companies, fund size (EUR, mil.), ticket or cheque size, team, office address (Praha / Prague), or the page's publication date. Do not truncate. Also list the navigation link names and URLs (portfolio, team, contact)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Note:** Quotes are capped at 125 characters, so sentences longer than that are paraphrased or partly quoted.

**Sentences mentioning Genesis Capital, funds, investments, companies, or capital**

1. "Od svého vzniku v roce 1999 poskytoval poradenství 7 fondům rozvojového kapitálu" (partial quote). The rest of the sentence says the total fund volume exceeds 550 million euros.
2. "Tyto fondy již podpořily více než 90 podniků."
3. "Mnoho z těchto firem se i díky spolupráci s Genesis Capital dostalo na špičku ve svém oboru."
4. The investors paragraph is over 125 characters, so I paraphrase it: the funds' investors include the European Investment Fund, the EBRD, several Czech and Austrian-group banks and insurers, a Finnish and a Swiss fund-of-funds, investment firms, and family offices.
5. Private equity section: "Genesis Private Equity Fund V (GPEF V) o velikosti 255 milionů euro" (partial quote). The rest says the typical investment size is 10–35 million euros, and the fund is currently open for investment.
6. Growth equity section: "Genesis Growth Equity Fund I (GGEF I) o velikosti 40 milionů euro" (partial quote). The rest says the typical investment size is 1–4 million euros.
7. Private equity summary: "Fondy se orientují na investice do malých a středních podniků v České republice" (partial quote). The rest lists Slovakia, Poland, Hungary, Austria, and Germany.
8. Growth equity summary: "Fondy zaměřené na investice do menších a středně velkých společností" (partial quote). The rest specifies the Czech Republic and Slovakia and notes significant growth potential.

**Publication date:** The page shows no publication date. It only has the footer "Copyright © 2026 Genesis Capital. All rights reserved."

**Navigation menu**

- O Genesis Capital: /o-genesis-capital
- Private Equity: /private-equity
- Growth Equity: /growth-equity
- Kontakt: /kontakt
- Kariéra: /kariera

The menu has no portfolio or investments link.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce every full sentence word-for-word, because your 125-character limit on quotes conflicts with the "do not truncate" instruction. Where a sentence exceeds 125 characters, I've quoted the opening portion and paraphrased the rest.

**Fund and investment statements**
- "We invest in ambitious & gritty founders from CEE; pre-seed through to meaningful scale." (Investment focus, from the "Our Fund" section.)
- "We support 60+ teams building at the frontier of digital, physical, and consumer economies." (Portfolio section.)
- "We provide patient capital, entrepreneurial empathy, and an aligned, supportive network." (Ethos section.)
- "We are drawn to individuals who are exceptionally intelligent, relentless, and high integrity." (Ethos section.)
- "The majority of the partners' assets are invested in our funds and we think of results in decades, not quarters." (Ethos section.)
- "Our relationships with founders, LPs, and peer investors are a reflection of such long-term mindset." (Ethos section.)

**EU co-funding disclosure (footer)**
- "ET3 and ET4 subfunds are supported by InnovFin Equity, with the financial backing of the European Union" (quote truncated to fit the limit).
- The rest of this paragraph explains that the European Fund for Strategic Investments (EFSI) aims to support productive investments in the EU and increase access to financing.

**Fund statistics**
- The page lists: 60+ companies, founded 2011, $500M total AUM, $1–3M ticket size, Pre-seed and Seed rounds, and an $85M current fund. Note that the fund size is shown in USD, not EUR millions as your request specified.

**Team**
- "Our Team: Venture is about people." Team members listed include General Partners Karel Zheng, Martin Rajcan, Tomas [REDACTED]a, and Tomas Obrtac, plus investors, partners, associates, and operations staff.

**Office address (Prague)**
- "Prague: Thámova 183/11, 186 00"

**Publication date**
- The page doesn't show a publication date. The only date is the footer copyright, "2026 KAYA, All rights reserved."

**Navigation links**
- Home: /
- Portfolio: /portfolio
- Team: /team
- Ethos: /ethos

There is no contact link on the page.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't return these sentences in full. The source requires quotes of 125 characters or fewer, and most of the relevant sentences are longer. Below are the exact passages within that limit, followed by paraphrases of the rest. The page is in Czech, so the quotes are untranslated, and the paraphrases are in English.

**Fund description and investors**
- Quote: "Jsme tým zkušených investičních profesionálů řídící fond rozvojového kapitálu" (The team manages a growth capital fund focused on fast-growing SMEs in the Czech Republic, Slovakia and neighbouring countries.)
- Quote: "GGEF I byl založen v listopadu 2019 za účasti předních evropských institucionálních investorů" (GGEF I was founded in November 2019 with leading European institutional investors, including the European Investment Fund.)
- The page lists the fund's other investors, including Kooperativa, Komerční banka (Amundi), RSJ and SPM Capital.

**Fund size and investment size**
- Fund size: €40 million.
- Investment size per deal: €1 million to €6 million.
- Maximum transaction value: up to €12 million.

**Portfolio and track record**
- Quote: "celková bilance více jak 30 úspěšně zainvestovaných společností" (The team has successfully invested in more than 30 companies.)
- The team says it has placed more than €100 million in relevant companies in its target region.
- The portfolio section lists companies including R2B2, HC electronics, JP-PROLAK, SEA Enterprises, UPS Technology, CARUSSEL, Předvýběr.CZ, Knihobot/Bookbot, TechPlasty Group, LLP Group, Cross Masters, iFORO Group/Poptávej.cz and ELIS DESIGN. The realised investments section lists Homecare Holding.

**Publication date**
- The page shows only a copyright notice: "Copyright © 2023 Genesis Capital. All rights reserved." No explicit publication date appears.

**Footer**
- Company name: Genesis Capital Growth s.r.o.
- Address: Na Šafránce 22, 101 00 Praha 10, Česká republika

The page refers to "GGEF I," not "Genesis Growth Equity Fund," so that name does not appear in the content.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences mentioning Versute, investments, portfolio, or funds** (quotes are capped at 125 characters, so longer sentences are partly paraphrased):

1. "Investujeme do malých a středních podniků prostřednictvím Private Equity fondů." (We invest in small and medium-sized enterprises through Private Equity funds.)
2. "V současné době jsme manažerem (General Partnerem) fondu VERSUTE Private Equity Fund Otevřený." (We are currently the manager (General Partner) of the VERSUTE Private Equity Fund Otevřený.)
3. "Versute Investments hledá stabilní, zdravé podniky se silným cash flow," (Versute Investments seeks stable, healthy companies with strong cash flow, which can be bought out using a mix of equity and bank financing.)
4. "Versute Investments spolupracuje s personálními poradci a manažerskými týmy pro identifikaci a realizaci" (Versute Investments works with recruitment advisers and management teams to identify and carry out such opportunities.)
5. "Portfolio VERSUTE Private Equity Fondu, kterého jsme v současné době manažerem (general partnerem)" (The portfolio of the VERSUTE Private Equity Fund, for which we are currently the general partner.)
6. "Copyright 2025, All Right Reserved, Versute Investments a.s." (Copyright notice for Versute Investments a.s., 2025.)

**Portfolio and reference companies shown:**

| Company | Year of entry | Status |
|---|---|---|
| Zdravotnictví (healthcare group, anonymous) | 2026 | Invested |
| PRP (softwood timber processor) | 2026 | Invested |
| ALFA 3 | 2025 | Active |
| UNIPAP PACKAGING | 2025 | Active |
| TIYO | 2023 | Active |
| BABIČKIN DVOR AGRO SERVIS | 2021 | Divested |
| DCK HOLOUBKOV BOHEMIA | 2020 | Divested |
| BOCO Pardubice | 2018 | Active |
| PRP (Slovakia) | 2017 | Divested |
| GEVORKYAN | 2016 | Active |

The page does not show any fund sizes.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "eib.org contact European Investment Bank 98-100 boulevard Konrad Adenauer Luxembourg"

Links: [{"title":"european investment bank","url":"https://europeanevaluation.org/european-investment-bank/"},{"title":"europeanevaluation.org","url":"https://europeanevaluation.org/?p=9243"},{"title":"www.eib.org","url":"https://www.eib.org/de/contact/offices.htm?lang=en"},{"title":"european investment bank en","url":"https://anti-fraud.ec.europa.eu/organisations/european-investment-bank_en"},{"title":"www.eib.org","url":"https://www.eib.org/en/contact/offices"},{"title":"catalina manea en","url":"https://anti-fraud.ec.europa.eu/persons/catalina-manea_en"},{"title":"www.eib.org","url":"https://www.eib.org/de/contact/offices?lang=en"},{"title":"EIB Headquarters","url":"https://eib.org/infocentre/contact/offices/ue/luxembourg"},{"title":"Economics Departments, Institutes and Research Centers in the World","url":"https://edirc.repec.org/data/eibeulu.html"}]

The EIB's headquarters is at 98-100, boulevard Konrad Adenauer, L-2950 Luxembourg, and the official EIB listing gives these contact details:

- **Phone:** +352 43791, plus a second number, +352 437704. An economics directory lists that second number as the fax line. (98-100, boulevard Konrad Adenauer L-2950 Luxembourg Luxembourg)
- **Email:** info@eib.org (same EIB page, index 8-2)
- **Website:** www.eib.org (Email: info@eib.org Website: https://www.eib.org/en/index.htm)
- **Other offices:** The bank runs regional offices alongside its Luxembourg headquarters, each with its own phone and email. These are listed on the EIB's offices directory at https://www.eib.org/en/contact/offices (With its headquarters in Luxembourg, the European Investment Bank also has offices in the different regions in which it operates.)

The EU Anti-Fraud Office's directory uses the same street address and postal code. (Street and number: 98-100, boulevard Konrad Adenauer City: Luxembourg Postal code: L-2950)

One source differs. The RePEc economics directory lists the address as "100, boulevard Konrad Adenauer," and says its homepage link appears broken. (This link seems to be broken.) That entry looks outdated, so I'd use 98-100 from the official pages.

The Luxembourg headquarters page also lists press and communications contacts by name. Those names come from a cached copy of the page, so check the live eib.org page before relying on them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://growth.genesis.cz/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, each line that names a portfolio company (the company name exactly as written), with any year, date or round shown next to it. Also return the page's publication date if shown, and any sentence that mentions a company investment. Do not paraphrase."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Genesis Capital Cross Masters investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Versute Investments Unipap koupila podíl",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eib.org/en/contact/offices",
  "prompt": "Return word-for-word, without summarising or translating, the address of the European Investment Bank headquarters in Luxembourg exactly as written on this page, and any sentence stating that the EIB has its headquarters in Luxembourg."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.kaya.vc/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, every portfolio company name listed on this page, one per line, with any round, stage, date or year shown beside it. Also return any sentence that mentions a funding round, a fund size, or a date."
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
**EIB Headquarters address:**

"98-100, boulevard Konrad Adenauer
L-2950 Luxembourg
Luxembourg"

**Sentence on headquarters location (truncated to meet the 125-character limit):**

"With its headquarters in Luxembourg, the European Investment Bank also has offices"

The full sentence continues with a description of its regional offices, which I've omitted here.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Only some names carry a label, and it's a status marker ("Exited" or "RIP"), not a funding round or date. No company shows a round, stage, or year.

Better Stack
Rohlik.cz
Viktor
E2B
Docplanner
Booksy
Jutro Medical
Sensible
Frontier
Pen.dev
Accomango: RIP
Ahoy Connect: Exited
Allonic
Amano: RIP
Artificial Agency
Awell
Blurry
Bnext
Boski
Cardiomatics
CareSend: Exited
Corebook
Cyberly
Das Lab: RIP
Digitoo
Dáme Jídlo: Exited
Eversports: Exited
Finiata: Exited
Flatio
Flexdog: RIP
Footshop
Gen Peach AI
Graet
Hashiona: RIP
Healee
Humanery: RIP
Intiaro
Kolay Randevu
Letsbuild: Exited
Masters: Exited
Medisearch
Meet Frank
Mesmer
Minerva Humanoids
Nautal: Exited
Nestpick: Exited
Nuvoair
Peak 21
PrimVeterinary
ROI Hunter: Exited
Riptides
Slevomat: Exited
Star Of Service: RIP
Stormy
Superlinked
Supernova
TOPK
Traceoid
TrueClaim
Twisto: Exited
Upheal
Woltair: RIP
Yoneda Labs
humans&

**Sentences mentioning funding, fund size, or dates:**

- The page mentions fundraising in a button label: "Start fundraising."
- On the EU funding note, "ET3 and ET4 subfunds are supported by InnovFin Equity," followed by text about the European Union's Horizon 2020 programme and the European Fund for Strategic Investments. No fund sizes are given.
- The footer copyright line reads "2026 KAYA, All rights reserved."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Genesis Capital Cross Masters investice"

Links: [{"title":"sest miliard na investice genesis capital spustila svuj dosud nejvetsi private equity fond","url":"https://forbes.cz/sest-miliard-na-investice-genesis-capital-spustila-svuj-dosud-nejvetsi-private-equity-fond/"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/251667"},{"title":"Skupina Genesis Capital spustila miliardový fond. Chystá investice do středoevropských firem","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/skupina-genesis-capital-spustila-miliardovy-fond-chysta-investice-do-stredoevropskych-firem-1383058"},{"title":"investice do trutnovskeho prumyslu genesis capital koupil podil firmy kasper kovo","url":"https://forbes.cz/investice-do-trutnovskeho-prumyslu-genesis-capital-koupil-podil-firmy-kasper-kovo/"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/1819664"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/genesis-capital-pomahaji-firmam-rust/1819664"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/genesis_capital_1/team"},{"title":"Private equity","url":"https://www.startbase.com/news/genesis-capital-expandiert-nach-deutschland-und-bringt-275-millionen-euro-mit/"},{"title":"Genesis Capital Reaches Final Close for Genesis Private Equity Fund III (CEE and CIS)","url":"https://www.globalprivatecapital.org/?p=6123"}]

Links: [{"title":"genesis capital loan","url":"https://craft.co/genesis-capital-loan"},{"title":"Genesis Capital","url":"https://www.devex.com/organizations/genesis-capital-193596"},{"title":"Back to Genesis Capital","url":"https://seedtable.com/investors/genesis-capital/portfolio"},{"title":"Genesis Capital Partners","url":"https://www.preqin.com/data/profile/fund-manager/genesis-capital-partners/165848"},{"title":"Genesis Capital","url":"https://www.seedtable.com/investors/genesis-capital"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/genesis_capital_s_r_o_/team"},{"title":"Success Doesn’t Just Happen","url":"https://genesis-capital.com/about/"},{"title":"Success Doesn’t Just Happen","url":"https://genesis-capital.com/?p=19"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/genesis_capital_1/team"},{"title":"Genesis announces strong year of investment","url":"https://amcham.cz/member-news/genesis-announces-strong-year-investment"}]

Links: [{"title":"www.luxhabitat.ae","url":"https://www.luxhabitat.ae/real-estate-agencies/cross-holding-af-sl/agents/"},{"title":"crosslantic capital management","url":"https://www.crunchbase.com/organization/crosslantic-capital-management"},{"title":"Source 000125649+description","url":"https://wikirate.org/Source_000125649+description"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/cross-ventures"},{"title":"MATTHIAS SCHABUS A1C1TV","url":"https://es.marketscreener.com/insider/MATTHIAS-SCHABUS-
… [skrátené, 2325 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Versute Investments Unipap koupila podíl"

Links: [{"title":"dva fondy zabalily unipap","url":"https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zabalily-unipap.html"},{"title":"verus investments 89e7d","url":"https://carerescif.hcmut.edu.vn/res-finance/verus-investments-89e7d.php"},{"title":"KSE UNICAP","url":"https://cn.tradingview.com/symbols/KSE-UNICAP/"},{"title":"Free Trial","url":"https://www.marketbeat.com/instant-alerts/filing-versor-investments-lp-makes-new-344000-investment-in-united-parcel-service-inc-ups-2025-08-22"},{"title":"Free Trial","url":"https://www.marketbeat.com/instant-alerts/filing-ubiquiti-inc-ui-shares-sold-by-versor-investments-lp-2025-08-19"},{"title":"Free Trial","url":"https://www.marketbeat.com/instant-alerts/filing-versor-investments-lp-makes-new-846000-investment-in-unum-group-unm-2025-08-19"},{"title":"Free Trial","url":"https://www.marketbeat.com/13f-filings/versor-investments-lp"},{"title":"emarketstorage.it","url":"https://emarketstorage.it/sites/default/files/comunicati/2022-05/20180622_49023.pdf"},{"title":"Number of Shares","url":"https://www.gurufocus.com/guru-portfolio/Dimensional VA International Small Portfolio/MIL:UNI"},{"title":"Statements regarding the holding in BNL: press release 9","url":"https://www.unipol.it/en/statements-regarding-holding-bnl-press-release-9"}]

Links: [{"title":"dva fondy zabalily unipap","url":"https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zabalily-unipap.html"},{"title":"zabaleno pardubicky unipap kupuji za stovky milionu dva ceske private equity fondy","url":"https://forbes.cz/zabaleno-pardubicky-unipap-kupuji-za-stovky-milionu-dva-ceske-private-equity-fondy/"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-vyrobce-obalu-z-pardubic-je-opet-na-prodej-cena-se-muze-blizit-miliarde-277570"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/unipap-as/financials"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/unipap-as"},{"title":"20761 pwc legal advises vdv packaging on acquisition of unipap","url":"https://ceelegalmatters.com/pwc-legal/20761-pwc-legal-advises-vdv-packaging-on-acquisition-of-unipap"},{"title":"P. Van De Velde Group","url":"https://www.imap.com/de-de/transactions/imap-advises-veerkarton-on-the-sale-to-p-van-de-velde-group~t"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/van-de-velde-acquired-by-kartesia"},{"title":"P. Van De Velde Group","url":"https://www.imap.com/rs-sr/transactions/imap-advises-veerkarton-on-the-sale-to-p-van-de-velde-group~t"},{"title":"deal announcement materials veerkarton","url":"https://www.imap.de/en/deal-briefs/2020/deal-announcement-materials-veerkarton/"}]

**Krátká odpověď:** Versute Investments podíl v Unipapu sama nekoupila. Kupcem byl fond BHS Private Equity Fund, který firmu koupil společně s fondem MAM. Versute figuruje u fondu jak
… [skrátené, 1483 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.genesis.cz/private-equity",
  "prompt": "Return word-for-word, without summarising or translating, every full sentence on this page that mentions Genesis Private Equity Fund (GPEF), fund size in EUR or milionů euro, typical investment size (investice, milionů euro), total fund volume, 550, 90 podniků, or the page's publication date. Quote the Czech original exactly; do not translate or truncate."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/investice-do-trutnovskeho-prumyslu-genesis-capital-koupil-podil-firmy-kasper-kovo/",
  "prompt": "Return word-for-word, without summarising or translating, the headline, the publication date shown on the article, and every sentence that mentions Genesis Capital, its fund, the stake acquired, the company name and the price or share. Quote the Czech original exactly."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zabalily-unipap.html",
  "prompt": "Return word-for-word, without summarising, every sentence that mentions Unipap, Versute, BHS Private Equity Fund, MAM, the buyer, the seller, the fund size or assets (CZK), and the page's publication date. Quote exactly as written, in English as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Kaya VC invests seed round 2025 Czech startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Genesis Capital Growth GGEF investice 2025 podíl společnost",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Headline:** "Investice do trutnovského průmyslu. Genesis Capital koupil podíl firmy Kasper Kovo | Forbes"

**Publication date:** Not shown in the provided content.

**Other sentences:** The provided content contains only the headline, so there are no additional sentences to quote.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "24 Sep 2025"

**Headline (names UNIPAP):** "Two funds wrapped up UNIPAP"

**Buyers and subtitle:** "Czech private equity funds MAM and BHS have acquired the industrial paper packaging manufacturer."

**Seller:** "The Belgian group Van de Velde Packaging is selling UNIPAP after three years."

**Buyer split:** "The company will be split evenly between BHS Private Equity Fund and MAM Private Equity Fund."

**MAM fund:** "The MAM Private Equity sub-fund has been active on the market for 2.5 years." The fund's assets are stated in this sentence: "It manages assets worth CZK 440 million" (excerpt; the full sentence exceeds the 125-character limit).

**BHS fund:** "BHS Private Equity Fund, advised by Versute Investments, manages assets worth CZK 1.5 billion."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't contain a typical investment size, the figures 550 or "90 podniků," or a publication date for the page itself. It does mention GPEF funds and two EUR figures. The 125-character limit means I can only quote shortened excerpts of these sentences, not the full text.

**Fund size (Fund V):**
> "Transakce je druhou investicí nejnovějšího fondu Genesis Private Equity Fund V o aktuální velikosti 275 milionů eur"

**GPEF V description:**
> "Genesis Private Equity Fund V (GPEF V), private equity fond ze skupiny Genesis Capital, se dohodl na vstupu"

**Fund III reference:**
> "Genesis Private Equity Fund III, fond skupiny Genesis Capital, prodal svůj většinový podíl ve společnosti GTH Catering"

**Total volume:** The homepage statistics show "EUR 500 mil." labeled "pro podniky" (for businesses), alongside "6 investičních fondů" and "80 investic." These are labels, not full sentences.

**Dates:** The most recent news item is dated 30.06.2026, and the footer shows copyright 2026. Neither is stated as the page's publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Kaya VC invests seed round 2025 Czech startup"

Links: [{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/kaya-vc"},{"title":"wbj.pl","url":"https://wbj.pl/czech-funds-target-poland/post/146377"},{"title":"25 Iunie 2025","url":"https://start-up.ro/subiecte/europe/"},{"title":"novi inozemni fond za hrvatske startupove","url":"https://informator.hr/vijesti/novi-inozemni-fond-za-hrvatske-startupove"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/kaya-vc-launches-new-fund-for-startups"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/kaya-vc-raises-70m-for-cee-startups"},{"title":"with over 45 startups already funded czech vc fund kaya secures e70 million to back more founders from cee","url":"https://bebeez.eu/2025/06/25/with-over-45-startups-already-funded-czech-vc-fund-kaya-secures-e70-million-to-back-more-founders-from-cee/"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/stormy/financials"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/kaya-vc-launches-80m-startup-fund"},{"title":"Back to KAYA VC","url":"https://seedtable.com/investors/kaya-vc/portfolio"}]

I found one 2025 seed deal involving Kaya, but these results don't confirm that it's a Czech startup.

**Stormy (seed, September 2025):** CB Insights records a Seed VC for $1.6M on September 12, 2025, and Kaya VC invested in Stormy's Seed VC funding round. Music Ally is also listed as an investor. The results don't say where Stormy is based.

**Kaya's 2025 fund:** Kaya is a Prague-based early-stage fund. In June 2025 it raised nearly €70 million for its fifth fund to support up to 25 early-stage startups in the CEE region, from Pre-Seed to Series A. A typical initial investment from KAYA ranges from one to three million Euro. It also keeps a capital reserve for follow-on rounds, with up to €20 million available for a single company.

**Other Kaya 2025 deals in the results:**
- Jutro Medical, a Warsaw company, received a €12 million Series A in March 2025 (Jutro Medical (AI-first primary care, Warsaw, €12 million Series A in March 2025)). This is a Series A, not a seed round.
- Seedtable lists a $3.3 million pre-seed round for Riptides, a Budapest company, dated 23 April 2025, with a "Lead" tag next to the company name. That tag suggests Kaya led, but the results don't state it outright.
- Waveup lists TopK with a $5.5 million seed, but gives no date or location. Seedtable shows a $5.5 million seed on 1 July 2025 for a San Francisco AI company, which may be the same deal, though the results don't name it.

**Conflicting figures:** Sources disagree on Kaya's size. Waveup cites €270 million in total assets under management across five funds, while WBJ reports manages €300 million in assets and holds stakes in 45 firms. The fund's headline size also varies: TechLeap's e15 summary gives nearly Kč2 billion ready for investment.

**Gap:** I didn't find a confirmed 2025 
… [skrátené, 280 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Genesis Capital Growth GGEF investice 2025 podíl společnost"

Links: [{"title":"na pocatku bylo slovo a miliardy genesis capital spousti ambiciozni fond","url":"https://forbes.cz/na-pocatku-bylo-slovo-a-miliardy-genesis-capital-spousti-ambiciozni-fond/"},{"title":"investice do trutnovskeho prumyslu genesis capital koupil podil firmy kasper kovo","url":"https://forbes.cz/investice-do-trutnovskeho-prumyslu-genesis-capital-koupil-podil-firmy-kasper-kovo/"},{"title":"Nový fond nakoupí malé podniky za téměř miliardu","url":"https://www.e15.cz/byznys/prumysl-a-energetika/novy-fond-nakoupi-male-podniky-za-temer-miliardu-1363214"},{"title":"Čeští Genesis Capital vstupují do místní firmy, která tvořila efekty pro Stranger Things","url":"https://cc.cz/cesti-genesis-capital-vstupuji-do-mistni-firmy-ktera-tvorila-efekty-pro-stranger-things/"},{"title":"Ticker Tape by TradingView","url":"https://www.fxstreet.cz/zpravodajstvi-157334.html"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/genesis-capital-launches-225m-fund"},{"title":"Genesis announces strong year of investment","url":"https://www.amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"sgef dosahl v roce 2025 rekordniho objemu financovani ve vysi temer 18 miliard","url":"https://www.kb.cz/cs/sgef/o-nas/novinky/sgef-dosahl-v-roce-2025-rekordniho-objemu-financovani-ve-vysi-temer-18-miliard"},{"title":"Genesis Capital to launch a new private equity fund with a target size of EUR 250 million","url":"https://psik.org.pl/en/research-and-reports/market-information/genesis-capital-to-launch-a-new-private-equity-fund-with-a-target-size-of-eur-250-million"}]

Links: [{"title":"Genesis Growth Equity Fund I Overview","url":"https://pitchbook.com/profiles/fund/16343-56F"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/genesis-growth-equity-fund"},{"title":"Genesis announces strong year of investment","url":"https://amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"GGEF receives a $70 million investment for India’s green growth equity fund","url":"https://renewablewatch.in/2021/10/27/ggef-receives-a-70-million-investment-for-indias-green-growth-equity-fund/"},{"title":"Private equity","url":"https://www.startbase.com/news/genesis-capital-expandiert-nach-deutschland-und-bringt-275-millionen-euro-mit/"},{"title":"Genesis Capital Fund I Overview","url":"https://pitchbook.com/profiles/fund/19364-86F"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/1819664"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/genesis-capital-pomahaji-firmam-rust/1819664"},{"title":"genesis growth equity","url":"https://www.crunchbase.com/organization/genesis-growth-equity"}]

I couldn't find a clear record of stake purchases by Genesis Growth Equity Fund I (GGEF I) in 2025, and the sources disagree on basic facts about the
… [skrátené, 2423 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Genesis Private Equity Fund V\" investice 2026 koupil podíl",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.amcham.cz/member-news/genesis-announces-strong-year-investment",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Genesis, the fund names (GPEF, GGEF, Genesis Private Equity Fund V, Genesis Growth Equity Fund I), investments or acquisitions into named companies, fund size or deployment percentages, and the article's publication date. Quote the English original exactly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "LLP Group Genesis Growth Equity Fund I investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Stormy seed round Kaya VC 2025 announcement",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://versute.cz/cs_cz/sluzby/private-equity/#referencni-projekty",
  "prompt": "Return word-for-word, without summarising or translating, every line of the reference projects / portfolio table or list on this page, each with its year or date if shown, and any heading that names a company. Copy the company names exactly as written (keep capitalisation)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Referenční projekty**

Portfolio VERSUTE Private Equity Fondu, kterého jsme v současné době manažerem (general partnerem)

**Zdravotnictví**
Rok vstupu: 2026
Přední česká skupina poskytující specializovanou zdravotní péči
Stav investice
Investováno
Rok vstupu
2026
Typ investice
Minoritní kapitálový vstup, Mezaninový úvěr

**PRP**
Rok vstupu: 2026
Přední zpracovatel jehličnatého dřeva
Stav investice
Investováno
Rok vstupu
2026
Typ investice
Minoritní kapitálový vstup, Mezaninový úvěr

**ALFA 3**
Rok vstupu: 2025
Výrobce parcel lockerů pro e-commerce, logistiku a kovového nábytku pro průmysl, instituce a školy.
Stav investice
Aktivní
Rok vstupu
2025
Typ investice
Odkup na úvěrovou páku

**UNIPAP PACKAGING**
Rok vstupu: 2025
Český výrobce a lídr ve výrobě průmyslových obalů z vlnité lepenky.
Stav investice
Aktivní
Rok vstupu
2025
Typ investice
Odkup na úvěrovou páku

**TIYO**
Rok vstupu: 2023
Poskytovatel služeb v oblasti výzkumu, vývoje a testování pro průmyslové obory.
Stav investice
Aktivní
Rok vstupu
2023
Typ investice
Management buy-out

**BABIČKIN DVOR AGRO SERVIS**
Rok vstupu: 2021
Výrobce krmných směsí pro hospodářská zvířata.
Stav investice
Divestováno
Rok vstupu
2021
Typ investice
Růstový kapitál

**DCK HOLOUBKOV BOHEMIA**
Rok vstupu: 2020
Výroba a distribuce nízkonapěťových elektrických rozváděčů, skříní a pilířů.
Stav investice
Divestováno
Rok vstupu
2020
Typ investice
Odkup na úvěrovou páku

**BOCO Pardubice**
Rok vstupu: 2018
Výroba a renovace strojů a zařízení pro plastikářský a gumárenský průmysl.
Stav investice
Aktivní
Rok vstupu
2018
Typ investice
Odkup na úvěrovou páku, MBI

**PRP**
Rok vstupu: 2017
Přední zpracovatel jehličnatého dřeva na Slovensku.
Stav investice
Divestováno
Rok vstupu
2017
Typ investice
Růstový kapitál

**GEVORKYAN**
Rok vstupu: 2016
Evropský lídr v oblasti výroby kovových součástek pomocí práškové metalurgie.
Stav investice
Aktivní
Rok vstupu
2016
Typ investice
Mezaninový úvěr

*Poznámka: Opakující se odkazy „Detail investice“ a obrázky loga jsou vynechány, protože jde pouze o odkazy a grafické prvky bez textového obsahu.*
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the requested passages. Because each quote is capped at 125 characters, some sentences appear as consecutive fragments.

**Publication date:** "10 Jun 2026"

**Headline:** "Genesis announces strong year of investment"

**Fund size, deployment, and investments:**
- "Genesis Capital is approaching a year since it successfully launched Genesis Private Equity Fund V (GPEF V)," with the current size of EUR 286 million (the article says it is expected to exceed EUR 300 million).
- "GPEF V has been successful in deployment of capital and the investment pace, currently approaching 25% deployment."
- "In addition, the predecessor fund GPEF IV is invested in 12 active portfolio investments" and has five more years for growth.
- "The funds primarily target investments with equity tickets ranging between EUR 10 million and EUR 45 million."

**Investment interest and fund changes:**
- "Genesis Capital therefore remains interested in and active across a wide range of investment opportunities of varying sizes."
- "This is not affected by Genesis Capital's recent decision not to replicate for a successor fund the co-operation"
- "with a separate team established in connection with Genesis Growth Equity Fund I (GGEF I)"
- "While operations of GGEF I remain unchanged, the team originally established in connection with GGEF I"
- "will pursue its future activities independently of Genesis Capital"
- "the strategic crossroads for Genesis Capital in this segment remain open for future consideration."

**Strategy:**
- "Genesis Capital's long-term investment strategy is focused on high quality mid-sized companies"
- "with strong growth potential headquartered in the Czech Republic, Slovakia, Poland, Hungary, Austria, and Germany."
- "It backs entrepreneurs and management teams seeking suitable long-term partner to facilitate succession,"
- "drive expansion, or pursue new market opportunities, as well as managers in corporate carve-out situations"
- "across wide range of industries."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "LLP Group Genesis Growth Equity Fund I investice"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/genesis-growth-equity-fund"},{"title":"Genesis Growth Equity Fund I Overview","url":"https://pitchbook.com/profiles/fund/16343-56F"},{"title":"genesis closes first growth fund on eur40m hard cap","url":"https://www.unquote.com/cee/official-record/3022751/genesis-closes-first-growth-fund-on-eur40m-hard-cap"},{"title":"genesis holds first close on eur31m for ggef i","url":"https://www.unquote.com/cee/official-record/3016823/genesis-holds-first-close-on-eur31m-for-ggef-i"},{"title":"genesis to launch eur40m growth fund","url":"https://www.unquote.com/cee/official-record/3010100/genesis-to-launch-eur40m-growth-fund"},{"title":"A service of","url":"https://ionanalytics.com/insights/mergermarket/global-lps-propel-australias-genesis-capital-to-usd-217m-first-and-final-close-fund-focus/"},{"title":"Genesis announces strong year of investment","url":"https://amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"genesis capital launches eur150m fund","url":"https://www.unquote.com/cee/news/3019947/genesis-capital-launches-eur150m-fund"},{"title":"genesis growth equity","url":"https://www.crunchbase.com/organization/genesis-growth-equity"}]

Links: [{"title":"Genesis announces strong year of investment","url":"https://amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/genesis-capital-3/financials"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/genesis-capital-pomahaji-firmam-rust/1819664"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/1819664"},{"title":"pryor cashman represents genesis capital llc in connection with oaktree investments","url":"https://www.pryorcashman.com/news/pryor-cashman-represents-genesis-capital-llc-in-connection-with-oaktree-investments"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/genesis-capital-sro"},{"title":"Genesis Private Equity Fund V Scsp","url":"https://www.developmentaid.org/organizations/view/624829/genesis-private-equity-fund-v-scsp"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/chuangshi-capital"},{"title":"Genesis Capital to launch a new private equity fund with a target size of EUR 250 million","url":"https://psik.org.pl/en/research-and-reports/market-information/genesis-capital-to-launch-a-new-private-equity-fund-with-a-target-size-of-eur-250-million"},{"title":"genesis capital 3","url":"https://superscout.co/investor/genesis-capital-3"}]

LLP Group appears in PitchBook's profile of Genesis Growth Equity Fund I (GGEF I) as one of the fund's investments. PitchBook dates the deal to 8 January 2025 and classifies LLP Group as a B2B consulting services business that already generates 
… [skrátené, 1563 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Stormy seed round Kaya VC 2025 announcement"

Links: [{"title":"Total Raised","url":"https://www.cbinsights.com/company/stormy/financials"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/stormy/"},{"title":"Kaya Founders","url":"https://www.briter.co/companies/kaya-founders"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/stormy"},{"title":"Back to KAYA VC","url":"https://seedtable.com/investors/kaya-vc/portfolio"},{"title":"KAYA favicon","url":"https://raising.fi/company/kaya"},{"title":"Back to Kaya Ventures","url":"https://seedtable.com/investors/kaya-ventures/portfolio"},{"title":"Kaya Ventures","url":"https://www.seedtable.com/investors/kaya-ventures"},{"title":"Kaya AI favicon","url":"https://raising.fi/company/usekaya"},{"title":"Back to Pre Seed round","url":"https://seedtable.com/companies/kaya/funding-rounds/pre-seed-2022/changelog"}]

I couldn't find an official announcement, such as a press release or news article, for a Stormy seed round led or backed by Kaya VC. The results are all funding-database or investor-profile pages, and they don't fully agree.

- **Round details:** CB Insights lists a $1.6M seed round dated September 12, 2025. Kaya VC invested in Stormy's Seed VC funding round. Music Ally is also named as an investor.
- **Stage conflict:** VCBacked tags the September 2025 round as pre-seed rather than seed, and names Y Combinator and KAYA as top investors (Sep 2025 Pre-Seed).
- **Total raised:** Stormy has raised $2.1M over 2 rounds. The other round is a convertible note dated June 1, 2025, but its amount appears only as a placeholder.
- **Company background:** Stormy specializes in productivity software designed for Mac users with Apple silicon. It was formerly known as One Interface and changed its name to Stormy. It was founded in 2024 and is based in San Francisco, California. CB Insights also places it in a Y Combinator Summer Batch 2025 collection.
- **Which Kaya:** Don't confuse Kaya VC with Kaya Founders, which is a Philippines-based venture capital firm and venture builder. The Kaya VC in these results appears to be a different firm, though the sources don't state its location clearly.

These figures come from third-party trackers that include placeholder values, so treat them as unverified. To confirm the round, check Stormy's website or blog, its founders' posts, or Kaya VC's announcements. I can also run a follow-up search for news coverage of the round.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Genesis Private Equity Fund V" investice 2026 koupil podíl"

Links: [{"title":"Genesis announces strong year of investment","url":"https://www.amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/genesis-capital-sro"},{"title":"Genesis Private Equity Fund V Overview","url":"https://pitchbook.com/profiles/fund/25674-76F"},{"title":"tatra banka investuje do popredneho private equity fondu cielom posilnit rast inovacie slovensku","url":"https://www.tatrabanka.sk/sk/blog/tlacove-spravy/tatra-banka-investuje-do-popredneho-private-equity-fondu-cielom-posilnit-rast-inovacie-slovensku/"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/1819664"},{"title":"Skupina Genesis Capital spustila miliardový fond. Chystá investice do středoevropských firem","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/skupina-genesis-capital-spustila-miliardovy-fond-chysta-investice-do-stredoevropskych-firem-1383058"},{"title":"sest miliard na investice genesis capital spustila svuj dosud nejvetsi private equity fond","url":"https://forbes.cz/sest-miliard-na-investice-genesis-capital-spustila-svuj-dosud-nejvetsi-private-equity-fond/"},{"title":"Genesis Private Equity Fund V Scsp","url":"https://www.developmentaid.org/organizations/view/624829/genesis-private-equity-fund-v-scsp"},{"title":"Genesis Capital to launch a new private equity fund with a target size of EUR 250 million","url":"https://psik.org.pl/en/research-and-reports/market-information/genesis-capital-to-launch-a-new-private-equity-fund-with-a-target-size-of-eur-250-million"},{"title":"Podíl v Datartu se nám pěkně zhodnotí, ve hře je i burza, říká Ondřej Vičar z Genesis Capital","url":"https://www.e15.cz/rozhovory/podil-v-datartu-se-nam-pekne-zhodnoti-ve-hre-je-i-burza-rika-ondrej-vicar-z-genesis-capital-1392693"}]

Links: [{"title":"Genesis announces strong year of investment","url":"https://www.amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"genesis capital","url":"https://realdeals.eu.com/articles/tags/genesis capital"},{"title":"Skupina Genesis Capital spustila miliardový fond. Chystá investice do středoevropských firem","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/skupina-genesis-capital-spustila-miliardovy-fond-chysta-investice-do-stredoevropskych-firem-1383058"},{"title":"Genesis Capital to launch a new private equity fund with a target size of EUR 250 million","url":"https://psik.org.pl/en/research-and-reports/market-information/genesis-capital-to-launch-a-new-private-equity-fund-with-a-target-size-of-eur-250-million"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/genesis-capital-sro"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.cz/zpravy/1819664"},{"title":"GENESIS CAPITAL: Pomáhají firmám růst","url":"https://www.ceskenoviny.
… [skrátené, 3013 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/cesti-genesis-capital-vstupuji-do-mistni-firmy-ktera-tvorila-efekty-pro-stranger-things/",
  "prompt": "Return word-for-word, without summarising or translating, the headline, the publication date shown on the article, and every sentence that mentions Genesis Capital, its fund (GPEF, GGEF, Genesis Private Equity Fund), the company acquired, the stake acquired (podíl, většinový, menšinový) and any price or amount. Quote the Czech original exactly."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.e15.cz/rozhovory/podil-v-datartu-se-nam-pekne-zhodnoti-ve-hre-je-i-burza-rika-ondrej-vicar-z-genesis-capital-1392693",
  "prompt": "Return word-for-word, without summarising or translating, the headline, the publication date shown on the article, and every sentence that mentions Genesis Capital, the fund name (GPEF, Genesis Private Equity Fund), Datart / Nay-Datart and the stake (podíl, menšinový, většinový). Quote the Czech original exactly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Genesis Capital Growth LLP Group majoritní podíl 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Riptides pre-seed 2025 Kaya VC lead investor",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Headline:** "Podíl v Datartu se nám pěkně zhodnotí, ve hře je i burza, říká Ondřej Vičar z Genesis Capital"

**Publication date:** 30. srpna 2022 (05:30)

**Sentences mentioning Genesis Capital, the fund, or the stake:**

1. "V červnu jste dokončili výběr peněz do vašeho historicky největšího fondu Genesis Private Equity Fund IV (GPEF IV)."
2. "Investiční skupina Genesis Capital dokončuje první akvizici do svého nového fondu Genesis Private Equity fund IV (GPEF IV)."
3. "...říká řídící partner Genesis Capital Ondřej Vičar."
4. "Genesis nikdy nezveřejňuje kupní či prodejní ceny firem, takže to ani v tomto případě nesdělím."
5. "Genesis získá zhruba dvoutřetinový podíl, náš partner zbytek."

The article doesn't mention Datart, Nay-Datart, or the terms menšinový and většinový in its body. Datart appears only in the headline. The stake is mentioned only in sentence 5, and the lead is cut to fit the 125-character limit.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Nadpis:** „Čeští Genesis Capital vstupují do místní firmy, která tvořila efekty pro Stranger Things“

**Datum:** „03. 10. 2023“

Věty delší než 125 znaků jsou zkráceny, aby citace splňovaly limit. Zkrácené části jsou označeny v anglickém shrnutí.

**Věty zmiňující Genesis Capital, jeho fondy, nabytou firmu, podíl nebo částku:**

1. „alespoň podle představ domácího fondu Genesis Capital, který právě vstupuje do studia PFX.“
   *The fund Genesis Capital is entering PFX, the studio, with the aim of creating a leading post-production studio in Central and Eastern Europe.*

2. „Kolik peněz Genesis do společnosti investuje, firmy neříkají.“
   *The companies do not disclose how much money Genesis is investing.*

3. „měl ve společnosti získat významný podíl.“
   *The Genesis Private Equity Fund IV, a private equity fund of Genesis Capital, was reportedly to acquire a significant stake in the company. (Fund name is in the full sentence, which exceeds the limit.)*

4. „fond o velikosti 150 milionů eur má obvyklou velikost investice mezi pěti a dvaceti miliony eur.“
   *The article says the €150 million fund typically makes investments of €5 to €20 million.*

5. „říká Martin Viliš, partner v Genesis Capital Equity.“
   *Martin Viliš, a partner at Genesis Capital Equity, is quoted in the article. (The quoted statement itself is longer than the limit.)*

6. „Uvádí, že fond našel v zakladatelích vysoce zkušené a pro rozvoj nadšené partnery.“
   *The fund reportedly found highly experienced founders who are enthusiastic about growth.*

7. „Z Prahy řízený Genesis Capital se řadí k výrazným firmám v private equity investování“
   *Genesis Capital, managed from Prague, is described as a prominent private equity firm. (Sentence continues beyond the limit.)*

8. „fondy Genesis spravují investice například ve firmách Hecht Motors, XBS Group, Tronic/Datart“
   *Genesis funds manage investments in companies including Hecht Motors, XBS Group and Tronic/Datart, followed by Home Care Promedica. (Sentence continues beyond the limit.)*

9. „šesti private equity fondům s celkovým objemem přesahujícím 350 milionů eur.“
   *Genesis has advised six private equity funds with a combined volume exceeding €350 million. (Partial sentence; the full sentence begins with "Funguje od roku 1999...")*
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Riptides pre-seed 2025 Kaya VC lead investor"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/cloudbreak-ventures"},{"title":"Back to Pre Seed round","url":"https://seedtable.com/companies/kaya/funding-rounds/pre-seed-2022/changelog"},{"title":"tomas [REDACTED]a","url":"https://www.vcsheet.com/who/tomas-[REDACTED]a"},{"title":"paulo campos","url":"https://www.vcsheet.com/who/paulo-campos"},{"title":"constantin robertz","url":"https://www.vcsheet.com/who/constantin-robertz"},{"title":"Kaya Founders","url":"https://www.briter.co/companies/kaya-founders"},{"title":"kaya ventures","url":"https://www.vestbee.com/vc-list/kaya-ventures"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/kaya-ventures/financials"},{"title":"ray alimurung","url":"https://www.vcsheet.com/who/ray-alimurung"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/kaya-ventures-raises-100k-funding"}]

The search results don't confirm that Kaya VC led Riptides' pre-seed round. The only source that covers the round lists Kaya VC as one of several co-investors and doesn't name a lead.

A CB Insights profile for Cloudbreak Ventures dates Riptides' pre-seed round to April 23, 2025, and it lists Cloudbreak as the investor with the latest deal in that company. The same profile puts the round at $3.3M, with Kaya VC, Oktogon Ventures, PortfoLion, and undisclosed angel investors listed as co-investors. The snippet doesn't say which of them, if any, led.

Several different "Kaya" firms appear in the results, so it's unclear which one is involved:

- **Kaya VC:** A fund that stems from Enern Investments, a regional financial group formed in Prague in 2010. Its listing describes it as providing growth capital to pre-seed and seed startups from Central and Eastern Europe.
- **Kaya Founders:** Briter places it in the Philippines and describes it as a venture capital firm and venture builder that invests in early-stage tech companies across Southeast Asia.
- **Kaya Ventures:** Signalbase reports it as an early-stage venture firm with a distinct focus on companies redefining health.

A Briter table also shows a $3.3m deal, but the company name is masked and the entry is dated Nov 13, 2025. That date doesn't match the April 2025 date in the CB Insights profile, so I can't tie it to Riptides.

These are aggregator pages, not announcements from the companies involved. To confirm the lead, check Riptides' or Kaya VC's own press release, or a database like Crunchbase or PitchBook.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Genesis Capital Growth LLP Group majoritní podíl 2025"

Links: [{"title":"investice do trutnovskeho prumyslu genesis capital koupil podil firmy kasper kovo","url":"https://forbes.cz/investice-do-trutnovskeho-prumyslu-genesis-capital-koupil-podil-firmy-kasper-kovo/"},{"title":"Ticker Tape by TradingView","url":"https://www.fxstreet.cz/zpravodajstvi-157334.html"},{"title":"Private equity","url":"https://www.startbase.com/news/genesis-capital-expandiert-nach-deutschland-und-bringt-275-millionen-euro-mit/"},{"title":"Skupina Genesis Capital spustila miliardový fond. Chystá investice do středoevropských firem","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/skupina-genesis-capital-spustila-miliardovy-fond-chysta-investice-do-stredoevropskych-firem-1383058"},{"title":"Genesis Capital Invests in Slovakia-based 3070 Group, Acquires Czech Republic-based Swell (CEE and CIS)","url":"https://globalprivatecapital.org/?p=4995"},{"title":"genesis capital prodava spolecnost quinta analytica skupine bba capital partners","url":"https://forbes.cz/genesis-capital-prodava-spolecnost-quinta-analytica-skupine-bba-capital-partners/"},{"title":"Genesis Capital Acquires 47 Percent Stake in POS Media Group (CEE and CIS)","url":"https://www.globalprivatecapital.org/?p=9990"},{"title":"Genesis Private Equity Fund V Scsp","url":"https://www.developmentaid.org/organizations/view/624829/genesis-private-equity-fund-v-scsp"},{"title":"Genesis announces strong year of investment","url":"https://www.amcham.cz/member-news/genesis-announces-strong-year-investment"},{"title":"MAREK HOSCALEK A3U19D","url":"https://de.marketscreener.com/insider/MAREK-HOSCALEK-A3U19D/"}]

I found no source saying that a company called Genesis Capital Growth LLP took a majority stake in 2025. The results cover the wider Genesis Capital group, and most snippets lack dates, so I can't confirm which deals closed in 2025.

**Closest name match**
A MarketScreener profile links a "Genesis Capital Growth sro" to Stratum Partners, a firm that targets smaller companies in Central Europe and Slovakia with deal sizes of EUR 2–10 million (Genesis Capital Growth sro Investment ManagersFinance Stratum Partners invests in small and lower middle market companies located in Central Europe and Slovakia with an EBITDA of EUR 1 - 5 million. The firm focuses across a broad range of sectors and industries. It provides financing for buy-outs – succession situations, MBOs & MBIs, corporate carve-outs and growth transactions with an investment size of EUR 2 - 10 million.) The listed form is "sro," the Czech s.r.o., not LLP.

**Majority deals by the wider group (years unclear)**
- A Genesis fund agreed to take a majority holding in GAF, a metalworking company from Žamberk, and the existing sole owner plans to keep a meaningful share (Genesis Private Equity Fund IV, private equity fond ze skupiny Genesis Capital, uzavřel smlouvu o investici do majoritního podílu ve společnosti GAF. Zakladatel
… [skrátené, 3612 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.genesis.cz/private-equity",
  "prompt": "List every news item or deal announcement on this page with its exact headline (as written, Czech), its date as shown (for example dd.mm.yyyy), and the company name it concerns. Then return word-for-word the sentence that says 'Transakce je druhou investicí' in full, exactly as written."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Knihobot Genesis Capital investice Growth Equity Fund",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://bebeez.eu/2025/06/25/with-over-45-startups-already-funded-czech-vc-fund-kaya-secures-e70-million-to-back-more-founders-from-cee/",
  "prompt": "Return word-for-word, without summarising or translating, the headline, the publication date, and every sentence that mentions Kaya, the fund size (EUR million), the fund number, the typical initial investment or ticket size, the number of startups funded, or the stages. Copy the English original exactly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Kaya VC investice startup 2025 kolo vedl Kaya",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
You've hit your session limit · resets 3:20am (Europe/Prague)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
You've hit your session limit · resets 3:20am (Europe/Prague)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
You've hit your session limit · resets 3:20am (Europe/Prague)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b14.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b14.json",
  "content": "[\n  {\n    \"candidate_id\": \"C018\",\n    \"website\": \"https://www.genesis.cz\",\n    \"identity\": [\n      {\n        \"value\": {\"legal_name\": \"Genesis Capital Equity s.r.o.\", \"company_id\": null, \"country\": \"CZ\"},\n        \"value_text\": \"Genesis Capital Equity s.r.o.\",\n        \"source_url\": \"https://www.genesis.cz/kontakt\",\n        \"quote\": \"Genesis Capital Equity s.r.o.\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Praha 10\",\n      \"source_url\": \"https://www.genesis.cz/kontakt\",\n      \"quote\": \"101 00 Praha 10\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"pe\"],\n      \"value_text\": \"Fondy se orientují na investice do malých a středních podniků\",\n      \"source_url\": \"https://www.genesis.cz\",\n      \"quote\": \"Fondy se orientují na investice do malých a středních podniků v České republice\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"PFX\", \"date\": \"2023-10-03\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"PFX\",\n        \"source_url\": \"https://cc.cz/cesti-genesis-capital-vstupuji-do-mistni-firmy-ktera-tvorila-efekty-pro-stranger-things/\",\n        \"quote\": \"domácího fondu Genesis Capital, který právě vstupuje do studia PFX\",\n        \"published_date\": \"2023-10-03\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Datart\", \"date\": \"2022-08-30\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Datartu\",\n        \"source_url\": \"https://www.e15.cz/rozhovory/podil-v-datartu-se-nam-pekne-zhodnoti-ve-hre-je-i-burza-rika-ondrej-vicar-z-genesis-capital-1392693\",\n        \"quote\": \"Podíl v Datartu se nám pěkně zhodnotí, ve hře je i burza, říká Ondřej Vičar z Genesis Capital\",\n        \"published_date\": \"2022-08-30\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Kasper Kovo\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Kasper Kovo\",\n        \"source_url\": \"https://forbes.cz/investice-do-trutnovskeho-prumyslu-genesis-capital-koupil-podil-firmy-kasper-kovo/\",\n        \"quote\": \"Investice do trutnovského průmyslu. Genesis Capital koupil podíl firmy Kasper Kovo\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"sectors\": {\n      \"value\": [\"sector_agnostic\"],\n      \"value_text\": \"z nejrůznějších sektorů ekonomiky\",\n      \"source_url\": \"https://www.genesis.cz\",\n      \"quote\": \"Podíleli jsme se na podpoře růstu a rozvoje více než 90 podniků z nejrůznějších sektorů ekonomiky.\",\n      \"published_date\": null,\n      \"derivation\": \"inferred\"\n    },\n    \"stages\": null,\n    \"ticket\": {\n      \"value\": {\"min\": \"EUR 10 million\", \"max\": \"EUR 45 million\", \"currency\": \"EUR\"},\n      \"value_text\": \"equity tickets ranging between EUR 10 million and EUR 45 million\",\n      \"source_url\": \"https://www.amcham.cz/member-news/genesis-announces-strong-year-investment\",\n      \"quote\": \"The funds primarily target investments with equity tickets ranging between EUR 10 million and EUR 45 million.\",\n      \"published_date\": \"2026-06-10\",\n      \"derivation\": \"stated\"\n    },\n    \"total_capital\": null,\n    \"funds\": [\n      {\n        \"value\": {\"name\": \"Genesis Private Equity Fund V\", \"size\": \"EUR 286 million\", \"currency\": \"EUR\", \"vintage\": null},\n        \"value_text\": \"EUR 286 million\",\n        \"source_url\": \"https://www.amcham.cz/memb
… [skrátené, 18154 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b14.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b14 is written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b14.json (5 records, UTF-8 JSON array). The web search tool hit the session limit (resets 03:20 Europe/Prague) partway through, so C183 and C176 are incomplete and C018 is partly so.\n\nPer candidate:\n- C018 Genesis Capital: pe, CZ (Praha 10). 3 investments (PFX 2023-10-03, Datart 2022-08-30, Kasper Kovo undated). No early exit. Doubtful: fund sizes conflict across genesis.cz pages (GPEF V given as 225, 255, 275 and 286 mil. EUR); I used the June 2026 AmCham figure. total_capital left null. Two deals rest on news articles only; the genesis.cz news item for GPEF V's second deal was not checked.\n- C036 Versute Investments: pe, CZ (Praha 1). 6 investments (PRP 2026, ALFA 3 2025-08-04, UNIPAP 2025-09-24 via Deloitte, TIYO 2023, BABIČKIN DVOR AGRO SERVIS 2021, BOCO Pardubice 2018). No early exit. Doubtful: Deloitte says the BHS fund is \"advised by\" Versute, while Forbes says Versute manages it, so the Unipap role is unclear.\n- C171 European Investment Bank: early_exit foreign_hq (Luxembourg, verified on eib.org). investor_type lender (inferred). No investments.\n- C183 Genesis Growth Equity Fund I: pe/growth, CZ (Praha 10), management company Genesis Capital Growth s.r.o. Six portfolio names from growth.genesis.cz are undated; I found no dated non-candidate source before the limit, so the dated-deal requirement is unmet. The red flag (team leaving, no successor fund) is my judgment from AmCham and may be dropped.\n- C176 Kaya: I used kaya.vc (Prague). The batch gave no website, and a separate US \"Kaya Ventures\" (Massachusetts) exists and is not evidenced here, so confirm which firm this candidate is. Six undated portfolio names; no dated press confirmation of a deal. total_capital \"$500M total AUM\" conflicts with aggregator figures (about EUR 270-300M).\n\nCaveats: quotes come from WebFetch output, which is model-summarised, so some quotes (fund sizes, ticket, company-name tokens) may fail the machine check. Re-running C183 and C176 after the reset would fill in the dated deals."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

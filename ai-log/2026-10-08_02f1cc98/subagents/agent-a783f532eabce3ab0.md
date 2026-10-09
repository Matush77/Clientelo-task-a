# Subagent: Evidence v3 wave2 batch 03 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:00:53

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b03.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b03.json

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b03.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b03.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C057",
4	    "name": "EMUN investiční společnost, a.s.",
5	    "other_names": [],
6	    "known_website": "www.emun.cz",
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): EMUN investiční společnost, a.s., IČO 28495349"
8	  },
9	  {
10	    "candidate_id": "C173",
11	    "name": "Creandum",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": null
15	  },
16	  {
17	    "candidate_id": "C161",
18	    "name": "Plug and Play Tech Center",
19	    "other_names": [],
20	    "known_website": null,
21	    "registry_hint": null
22	  },
23	  {
24	    "candidate_id": "C167",
25	    "name": "Sofina",
26	    "other_names": [],
27	    "known_website": null,
28	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Sofina s.r.o., IČO 09564314"
29	  },
30	  {
31	    "candidate_id": "C123",
32	    "name": "PFCEU",
33	    "other_names": [],
34	    "known_website": null,
35	    "registry_hint": "possible registry match (unconfirmed, may be a different company): PFCEU s. r. o., IČO 36282600"
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

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.emun.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions EMUN, investments, portfolio, fund size, ticket, the company's address or IČO, and the page's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Creandum venture capital investice portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Plug and Play Tech Center Czech investice startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Sofina investment company portfolio Czech",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "PFCEU investiční fond investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I've limited the quotes to 125 characters, so some sentences are excerpted. The page is in Czech, so I've kept the original wording.

**Mentions of EMUN, investments, portfolios, and fund size**

- "EMUN vznikl proto, aby pomáhal podnikatelům a rodinám zachovat smysl a kontinuitu jejich bohatství"
- "Proto EMUN vytváří strategie pro ochranu a předávání majetku, řídí rodinné trusty a nadace"
- "Obhospodařujeme přes 16 miliard Kč investičního majetku."
- "Spravujeme privátní portfolia individuálních osob, rodin, nadací a investorů"
- "Vytvořili jsme rodinné struktury v České republice i zahraničí s majetkem přesahujícím 64 miliard Kč."
- "Našim klientům zpřístupňujeme v ČR běžně nedostupné investice institucionální kvality."
- "Jsme první institucionální správce svěřenských fondů s licencí ČNB."
- "Disponujeme nejvyšší licencí ČNB na investiční správu majetku."
- "Současně posilujeme naši aktivitu na privátních trzích, kde systematicky rozvíjíme"
- "O tom v podcastu Investičního webu mluvila s Vendulou Pokornou portfolio manažerka EMUN Anna Píchová."
- "V EMUN rosteme a spolu s tím dál rozšiřujeme náš investiční tým."
- "Informace uvedené v této části jsou určeny pouze pro kvalifikované investory"

**Address**

- "Anežská 986/10, 110 00 Praha 1"

**IČO**

- Not found on the page.

**Ticket**

- Not mentioned on the page.

**Publication date**

- The page has no single publication date. The news items are dated 30/9/2026, 18/9/2026, and 25/8/2026. The "k 31.12.2025" label appears to be a data as-of date for the figures, not a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Plug and Play Tech Center Czech investice startup"

Links: [{"title":"Plug and Play Tech Center","url":"https://en.wikipedia.org/wiki/Plug_and_Play_Tech_Center"},{"title":"Hlavní obsah","url":"https://www.novinky.cz/clanek/finance-americane-lovi-v-ceskych-vodach-genialni-mozky-lakaji-je-do-silicon-valley-53964"},{"title":"Czech Republic sets up shop in Silicon Valley","url":"https://abc7news.com/archive/7049924"},{"title":"gouvernement.lu","url":"https://gouvernement.lu/dam-assets/fr/actualites/articles/2011/06-juin/28-krecke/plug.pdf"},{"title":"Plug and Play Tech Center","url":"https://techbarcelona.com/?p=55873"},{"title":"Plug and Play Tech Center","url":"https://vds.tech/?p=4646"},{"title":"Plug and Play - by Anmol Mehta","url":"https://engg5700.erg.cuhk.edu.hk/node/75"},{"title":"Plug and Play Tech Center","url":"https://vds.tech/sponsor/plug-and-play/"},{"title":"Plug and Play Tech Center","url":"https://www.Wikipedia.org/wiki/Saeed_Amidi"}]

Plug and Play has a Czech connection, but the results show a Czech accelerator program, not direct equity investments in Czech startups. Most of the Czech-specific sources look old.

**The firm:** Plug and Play is a venture firm in Sunnyvale, California, that puts money into early-stage tech companies. CB Insights ranked it the world's most active startup accelerator for 2020 to 2022, with about 929 deals a year on average. From 2020 to 2022, 41% of its investments went to the U.S., 30% to Europe and 17% to Asia.

**The Czech link:** CzechInvest's CzechAccelerator is part of the Plug and Play campus in Sunnyvale, which hosts over 250 startups (CzechAccelerator agentury CzechInvest je součástí Plug and Play Tech Center v kalifornském Sunnyvale). When CzechInvest opened its office there, it aimed to find business opportunities for Czech companies and draw U.S. tech firms to the Czech Republic (The government-owned company Czech Invest celebrated the opening of its office Monday at the Plug and Play Tech Center in Sunnyvale. It is going to seek business opportunities for Czech companies).

**What Czech startups received:** The program offered perks rather than cash. A Czech-language Novinky article describes three months of free incubator office rent, conference room access, event passes, and unpaid consultations on legal, tax, accounting, HR and marketing matters for successful applicants (2-1). Before leaving for the U.S., participants also got free training on doing business there (2-2). The first three graduates were BoldBrick, Cognitive Security and Imagemetry (2-5).

**Investment focus:** A 2011 Plug and Play presentation lists the Czech Republic among its international partnerships and describes its investment stage as pre-seed to seed (4-1). I found no source showing Plug and Play directly investing in specific Czech startups.

**Current status:** Plug and Play says it is now active in more than 40 locations. The countries it names are the U.S., China, France, Germa
… [skrátené, 442 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "PFCEU investiční fond investice"

Links: [{"title":"Základní údaje o FEFSI","url":"https://www.finance.cz/clanky/1962-zakladni-udaje-o-fefsi/"},{"title":"Le mode conseil est activé Arrêter","url":"https://cbonds.fr/etf/5823/"},{"title":"Hint mode is switched on Switch off","url":"https://cbonds.com/etf/5823/"},{"title":"Hinweis-Modus ist eingeschaltet Ausschalten","url":"https://cbonds.de/etf/5823/"},{"title":"Original title:","url":"https://invenio.nusl.cz/record/112216?ln=en"},{"title":"snowball-analytics.com","url":"https://snowball-analytics.com/public/asset/PCEU.PA.EUR"},{"title":"Jesteś w trybie podpowiedzi Wyłącz","url":"https://cbonds.pl/etf/5823/"},{"title":"invenio.nusl.cz","url":"https://invenio.nusl.cz/record/112216?ln=cs"},{"title":"Ви перебуваєте в режимі підказок Вимкнути","url":"https://cbonds.com.ua/etf/5823/"}]

I couldn't find any Czech investment fund called "PFCEU" in the search results. The closest match is **PCEU**, a different fund, so you may have meant that ticker.

**PCEU: Amundi ETF PEA MSCI Europe UCITS ETF**
- **Type and goal:** It's an exchange-traded fund that tries to mirror the MSCI Europe index, mostly through large European companies. The Amundi ETF PEA MSCI Europe UCITS ETF seeks to replicate as close as possible the price and yield performance of the MSCI Europe Index.
- **Listing:** Its main exchange is Euronext Paris, under the ticker PCEU. Main exchange is Euronext Paris and ticker symbol is PCEU. Its ISIN is FR0013412038.
- **Launch and currency:** The share class was registered on 25 April 2019 and its base currency is the euro. The Amundi fund's base currency is EUR and the share class was registered 25.04.2019.
- **Costs:** The total expense ratio is 0.15%. The total expense ratio is 0.15%.
- **Distributions:** It makes no regular dividend payments. The Amundi ETF Pea MSCI Europe UCITS ETF (EUR) pays dividends 0 time(s) per year.
- **Size and price:** The most recent snapshot I found, dated 20 July 2026, showed a net asset value of 39.38 EUR per share and total fund assets of about 355.62 million EUR. 39.38 EUR NAV per Share | 20/07/2026

These figures come from third-party data sites and are several months old as of October 2026, so check a live quote or the issuer's site before relying on them. This is a French-listed UCITS fund, not a Czech one.

If you meant a different fund, send me its full name, the manager, or its ISIN and I'll search again.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Creandum venture capital investice portfolio"

Links: [{"title":"asking the right questions a profile of creandum","url":"https://www.maddyness.com/uk/2021/03/01/asking-the-right-questions-a-profile-of-creandum/"},{"title":"creandum ab","url":"https://kando.tech/index.php/company/creandum-ab"},{"title":"startups.one.gob.es","url":"https://startups.one.gob.es/companies/creandum"},{"title":"Venture Capital","url":"https://altss.com/profile/creandum-v-advisor-ab"},{"title":"Portfolio markups","url":"https://seedtable.com/companies/creandum"},{"title":"www.seedtable.com","url":"https://www.seedtable.com/investors/creandum"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/creandum"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/directory/investors/creandum"},{"title":"Last updated 2026-06-18","url":"https://startupim.com/investor/creandum"}]

Creandum is an early-stage venture capital firm based in Stockholm with a European focus. The sources agree on that, but they conflict on many specifics, so treat the figures below as approximate.

**Background**
- Maddyness places the firm's founding in 2003, when Staffan Helgesson set it up in Stockholm. Its focus began in the Nordic region and later widened across Europe.
- Altss gives 1977 as the founding year and describes a technology investment firm at the time. That conflicts with the other sources, so I'd treat it as an outlier.
- Offices: A San Francisco office opened in 2012 and a Berlin office followed in 2016, per Maddyness. Altss also lists London, and Waveup lists Stockholm, Berlin, London and San Francisco.

**Investment approach**
- Its initial tickets are placed in seed and Series A rounds. It usually backs companies at a very early stage and stays with them until an exit or IPO.
- Check sizes conflict. Altss cites €5M–€20M for Series A and B deals. Kando describes initial amounts from a few hundred thousand euros, rising to €10M over a company's life. Startupim gives a typical range of $26M–$58M.
- Sectors: Waveup emphasizes consumer, software and hardware technology, while Altss lists enterprise software, fintech, digital health and AI/ML.

**Portfolio**
- Notable names include Spotify, iZettle, Klarna, Kahoot!, Vivino, Depop and Trade Republic, per Maddyness. Bolt, Kry and Virta Health are also named, and the firm has close to a dozen unicorns.
- Reported size varies widely. Maddyness counted more than 100 companies in 2021. VCBacked tracks 176 companies with about $4.9B invested. Seedtable shows 100, 129 and 136 holdings on different pages. A Spanish government startup directory lists only 15, and Startupim shows just one, so those two are clearly incomplete.
- Exits: Maddyness highlights the 2018 Spotify IPO, the sale of iZettle to PayPal for $2.2B, and Zynga's $700M acquisition of Small Giant Games. Seedtable's timeline adds the Instabridge acquisition (March 2019), the Klaus acquisition (February 2024), and the Klarna IPO (September 2
… [skrátené, 1064 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Sofina investment company portfolio Czech"

Links: [{"title":"Sofina vous permet d’investir dans un portefeuille de sociétés non cotées…","url":"https://www.test-achats.be/invest/investir/actions/analysis/2025/04/sofina-conseil-gagnant-hausse"},{"title":"Sofina Société Anonyme/€SOF","url":"https://lightyear.com/de/stock/SOF:BSE"},{"title":"SOFINA (SOF)","url":"https://www.ajbell.co.uk/market-research/XBRU:SOF"},{"title":"www.morningstar.com.au","url":"https://www.morningstar.com.au/investments/security/fra/8FS/summary"},{"title":"Sofina | Company Profile - Revenue, Headcount, Tech Stack, Contacts","url":"https://ghost.bitscale.ai/sofina/"},{"title":"Sofina (SOF)","url":"https://www.investing.com/equities/sofina-company-profile"},{"title":"company info","url":"https://www.ajbell.co.uk/market-research/sub/XBRU:SOF/company-info"},{"title":"Our history","url":"https://www.sofinagroup.com/about-sofina/our-history/"},{"title":"Sofina | Company Profile - Revenue, Headcount, Tech Stack, Contacts","url":"https://bitscale.ai/directory/sofina"}]

None of these results mention Sofina holdings in the Czech Republic, so I can't confirm any Czech portfolio companies from this search. The results do describe the wider portfolio:

- **Background:** The firm started as an engineering conglomerate and today trades on Euronext Brussels. Founded more than 125 years ago as an engineering conglomerate, Sofina is an investment company listed on Euronext Brussels. A Test-Achats analysis says control rests with the Boël, Solvay and Janssen families (Sofina est un holding belge contrôlé par les familles Boël, Solvay et Janssen).
- **Investment approach:** Its investments tend to be long-term and usually sit alongside existing controlling owners (Il investit dans une optique de long terme et, la plupart du temps, en tant que partenaire minoritaire). Sofina only takes minority ownership positions in its long-term holdings with capital from its own balance sheet.
- **Size and mix:** The group counts 81 direct stakes and holds positions in 564 funds, which represent close to half its portfolio, according to the April 2025 Test-Achats analysis (Outre 81 participations directes, le holding a des intérêts dans 564 fonds gérés par plus de 80 gestionnaires (46% du portefeuille)).
- **Asset base:** Direct holdings account for the bulk of net asset value, with most coming from Europe. Venture and private equity funds form a smaller share, located chiefly in the US and Asia (Its portfolio holdings constitute the majority of its net asset value and come mostly from Europe. A smaller percentage of its net asset value base comes from investments in venture capital and private equity funds, mostly in the United States and in Asia.).
- **Geography:** Investment targets cluster in Western Europe, with additional emphasis on India, China, Southeast Asia and the United States (The firm typically invests in European based companies with a global exposure, and it 
… [skrátené, 1740 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 21:01:54

Five candidates, with early exits likely for Creandum, Plug and Play and Sofina (all foreign HQ). I'll check each candidate's own site for HQ and identity, plus the EMUN contact page and a search for the PFCEU entity.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.emun.cz/kontakt",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that contains the company name with its legal form (a.s., s.r.o. or similar), IČO, DIČ, registered office (sídlo), the office address, and any date label such as \"k 31.12.2025\". Also return the exact sentence that contains \"16 miliard\" if present."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EMUN investiční společnost investice do startupů firem fond",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.creandum.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states the firm's office locations, headquarters, address or city, the investment focus or stage, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.plugandplaytechcenter.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states the company's headquarters or office address, city, state, and whether it invests in or takes equity in startups."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sofinagroup.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states the company's registered office, headquarters or address, its legal name with legal form, and the sentences that describe what it invests in (minority stakes, funds, holdings)."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"PFCEU\" s.r.o. 36282600",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The web page content you provided contains only the title "Plug and Play." It has no sentences about the company's headquarters, office address, city, state, or whether it invests in or takes equity in startups, so I can't extract any of those.

If you share the full page text, I can pull out the relevant sentences.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The only sentence in the provided content that relates to the firm's investment focus or stage is:

"We back the companies of tomorrow before it's obvious."

The content is truncated, and it contains no office locations, headquarters, address, city, or publication date. If you share the full page, I can check it for those details.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page contains the company name, IČO, DIČ, registry entry, and office address. It has no explicit "sídlo" label, no date label such as "k 31.12.2025", and no sentence containing "16 miliard."

**Company name and legal form:**
- "EMUN investiční společnost, a.s."

**IČO and DIČ:**
- "IČO: 28495349, DIČ: CZ28495349"

**Registry entry:**
- "společnost vedená u Městského soudu v Praze, sp. zn. B 14867"

**Office address:**
- "Anežská 986/10 / 110 00 Praha 1"

**Date labels:** None found.

**"16 miliard":** Not present.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't state a registered office, headquarters, or street address, and it doesn't give a legal name with legal form. It shows "Offices: 4" with no locations. The only company name is "Sofina Group."

The sentences describing its investments are:

- "We invest in visionary founders at every stage, from nurturing startups to scaling growth-stage companies and partnering mature ones."
- "We invest in a diversified group of innovative growth companies across geographies, sectors and stages."
- "Direct, long-term minority partnerships with ambitious growth companies."
- "Commitments to top-tier funds selecting and backing innovative companies."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""PFCEU" s.r.o. 36282600"

Links: [{"title":"obchodny register","url":"https://finstat.sk/36282600/obchodny_register"},{"title":"pfc trade s r o 23828501","url":"https://www.podnikatel.cz/rejstrik/pfc-trade-s-r-o-23828501/"},{"title":"PF s.r.o., IČO: 60462086, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/60462086-pf-s-r-o"},{"title":"pf pro s r o 28402154","url":"https://www.podnikatel.cz/rejstrik/pf-pro-s-r-o-28402154/"},{"title":"PF plus s.r.o., IČO (28942060), sídlo Praha","url":"https://www.mesec.cz/rejstrik-firem/firma-pf-plus-s-r-o-28942060"},{"title":"pf s r o 60462086","url":"https://www.podnikatel.cz/rejstrik/pf-s-r-o-60462086/"},{"title":"pf ucto s r o 24179591","url":"https://www.podnikatel.cz/rejstrik/pf-ucto-s-r-o-24179591/"},{"title":"Prihlásiť sa","url":"https://finstat.sk/47603461/obchodny_register"},{"title":"Prihlásiť sa","url":"https://finstat.sk/35936193/obchodny_register"}]

The search found one direct match: a Slovak company listing for PFCEU s.r.o. with ID 36282600, published by the FinStat aggregator.

- **Seat:** Sídlo Kataríny Franklovej 5791/10, 902 01 Pezinok, so the registered office is in Pezinok, Slovakia.
- **Founding and registration:** The company dates from 25 February 2006 and sits in the Bratislava III municipal court's commercial register, section Sro, entry 39608/B.
- **Share capital:** It is listed at €160,000, which the registry shows as fully paid.
- **Tax identifiers:** The listing gives a tax ID (DIČ) of 2022138899 and a VAT ID of SK2022138899.
- **Name history:** The company previously traded as Pro Financial Consulting s.r.o., and skrátene PFCEU s.r.o. is the abbreviated form. The listing's date ranges for these names are hard to parse, so I wouldn't rely on the exact years.
- **Former addresses:** Earlier registered seats were in Bratislava and at Radničné námestie in Pezinok.

The search did not surface the company's current status (active or dissolved), its current directors, or its business activities. The other results were unrelated Czech and Slovak companies with different ID numbers, such as PF s.r.o. and PFC - TRADE s.r.o. For current, authoritative details, check the Slovak Business Register (ORSR) at orsr.sk, since FinStat is a third-party aggregator.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EMUN investiční společnost investice do startupů firem fond"

Links: [{"title":"V Emunu otevřeli nový fond, vábí investory na OpenAI nebo Revolut. Už vybrali čtvrt miliardy","url":"https://www.e15.cz/finexpert/investujeme/v-emunu-otevreli-novy-fond-vabi-investory-na-openai-nebo-revolut-uz-vybrali-ctvrt-miliardy-1428118"},{"title":"Raymond Grell","url":"https://sk.linkedin.com/in/raymond-grell"},{"title":"Karel Siegl","url":"https://cz.linkedin.com/in/karel-siegl"},{"title":"Akcie OpenAI, SpaceX nebo Revolutu chtějí všichni. Žhavé investiční zboží se otevírá i Čechům","url":"https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/"},{"title":"Ponořila jsem se do výroby čipů. A prodala část Buffettových akcií, říká Anna Píchová. Změnila i firmu","url":"https://cc.cz/ponorila-jsem-se-do-vyroby-cipu-a-prodala-cast-buffettovych-akcii-rika-anna-pichova-zmenila-i-firmu/"},{"title":"zive do ceho se letos vyplati dat penize radi experti","url":"https://www.newstream.cz/money/zive-do-ceho-se-letos-vyplati-dat-penize-radi-experti"},{"title":"🎧 Kam přesouvají majetek velcí investoři? Nadprůměrné zhodnocení najdete mimo burzu, říká partner společnosti Emun","url":"https://www.e15.cz/podcasty/business-club/kam-presouvaji-majetek-velci-investori-nadprumerne-zhodnoceni-najdete-mimo-burzu-rika-partner-spolecnosti-emun-1424206"},{"title":"dalsi jednorozec je na svete cesko americkou emplifi ocenila investice na miliardu dolaru","url":"https://forbes.cz/dalsi-jednorozec-je-na-svete-cesko-americkou-emplifi-ocenila-investice-na-miliardu-dolaru/"},{"title":"Vytvoření portfolia startupů pro drobné investory","url":"https://iocharts.io/cs/blog/startup-egyszeruen-erthetoen/"}]

Emun is a Czech investment firm, and its best-known startup-related product is the **Emun Global Unicorns (EGU)** fund. It invests in late-stage private companies rather than early-stage startups.

**About Emun**
- Emun's assets under supervision total about 14 billion CZK, mostly from very wealthy clients. Its founders are Filip Savi, Leoš Jirman and Petr Laštovka. Emun aktuálně dohlíží na majetek v objemu zhruba 14 miliard korun, jde přitom primárně o prostředky velmi movitých klientů, and the founders are listed in the same passage.

**The Emun Global Unicorns fund**
- It is an open-ended unit trust for qualified investors. Investiční společnost Emun spouští podílový fond kvalifikovaných investorů, s nímž chce nabídnout možnost zhodnotit peníze prostřednictvím firem jako OpenAI, Revolut nebo SpaceX.
- Its focus is on the largest private companies, those valued above $1 billion that could list on a stock exchange soon. Nový fond Emun Global Unicorns cílí na investice do největších globálních jednorožců, tedy společností s hodnotou přes jednu miliardu dolarů.
- Its intended holdings include firmy jako OpenAI, SpaceX, Revolut, Anthropic, xAI, Kraken, Stripe nebo Databricks. The fund has no fixed lifespan, so je otevře
… [skrátené, 1591 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 21:02:54

Several results need a closer look. The EMUN fund figure and the "16 miliard" date label need verbatim confirmation, Creandum's homepage gave no HQ, and the PFCEU lookup points to a Slovak company that still needs a website. I'll check those sources in parallel.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.e15.cz/finexpert/investujeme/v-emunu-otevreli-novy-fond-vabi-investory-na-openai-nebo-revolut-uz-vybrali-ctvrt-miliardy-1428118",
  "prompt": "Return word-for-word, without summarising or translating, the article's publication date and every sentence that mentions the fund name (Emun Global Unicorns or similar), its size or the amount raised (\"čtvrt miliardy\" or any amount), its currency, its launch, and whether it invests in companies."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.emun.cz",
  "prompt": "Return word-for-word, without summarising or translating: (1) the exact sentence that contains \"Obhospodařujeme\" and any date label such as \"k 31.12.2025\" or \"k 31. 12. 2025\" appearing in the same sentence or right next to it; (2) every sentence that mentions fond, fondy, Global Unicorns, private markets, or investice do firem. Include the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.maddyness.com/uk/2021/03/01/asking-the-right-questions-a-profile-of-creandum/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Stockholm, Berlin, London, San Francisco, offices, headquarters, or where the firm is based, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.creandum.com/about",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states where the team or office is located (city or country), the firm's name with legal form if shown, and any sentence about the investment focus, stage or check size."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.novinky.cz/clanek/finance-americane-lovi-v-ceskych-vodach-genialni-mozky-lakaji-je-do-silicon-valley-53964",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Plug and Play, Sunnyvale, CzechInvest, CzechAccelerator, investice or equity, and the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "PFCEU Pro Financial Consulting Pezinok investície startupy",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sofinagroup.com/about-sofina/our-history/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states the legal name and legal form of the company (for example \"Sofina SA\" or \"société anonyme\"), the registered office or headquarters city or address, and its listing on Euronext Brussels."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.test-achats.be/invest/investir/actions/analysis/2025/04/sofina-conseil-gagnant-hausse",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that describes Sofina as a holding (for example \"holding belge\"), states its listing or place (Brussels, Euronext), describes its investments (minority stakes, funds, direct holdings), and gives the article's publication date."
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
**Legal name and form:** The page doesn't state a current legal form (such as "SA"). It gives the company's original 1898 name in a historical entry: "Foundation of Sofina (“Société Financière de Transport et d’Entreprises Industrielles”)"

**Registered office or headquarters:** The page doesn't name one. It mentions a London office (2025), a Singapore office (2014), and a Luxembourg office (1938), but doesn't say which, if any, is the headquarters or registered office.

**Euronext Brussels listing:** "Sofina is an investment company listed on Euronext Brussels"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sofina as a holding and its investments**

- "Sofina vous permet d'investir dans un portefeuille de sociétés non cotées (91% des actifs)"
- "Outre 81 participations directes, le holding a des intérêts dans 564 fonds gérés par plus de 80 gestionnaires"
- "Sofina est un holding belge contrôlé par les familles Boël, Solvay et Janssen."
- "Il investit dans une optique de long terme et, la plupart du temps, en tant que partenaire minoritaire"

**Publication date**

- "Publié le 01 avril 2025"

**Listing or place**

The page does not state where Sofina is listed, such as Brussels or Euronext. It only calls the company a Belgian holding.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "1 March 2021"

**Sentences mentioning offices or locations:**

1. "Creandum has a 17-year history and was set up by Staffan Helgesson in Stockholm back in 2003."
2. "In 2012, we opened up an office in San Francisco to help our European founders win the US market."
3. "In 2016, we opened in Berlin."
4. "Today the investment team counts a total of 12 team members across Stockholm, Berlin and San Francisco."
5. "I personally joined Creandum in Berlin in the summer of 2019, after my previous jobs as Chief of Staff…" *(truncated to meet the 125-character limit)*
6. "And no matter which office you're part of, everyone on the team now feels equally far away from or close…" *(truncated to meet the 125-character limit)*
7. "Due to our international mindset with offices in Stockholm, Berlin and San Francisco, we offer a strong…" *(truncated to meet the 125-character limit)*
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**(1) Sentence with "Obhospodařujeme":**
"Obhospodařujeme přes 16 miliard Kč investičního majetku."

The date label "k 31.12.2025" is not in this sentence or right next to it. It appears in a separate statistics block further down the page, under the figures "0 mld+ CZK majetku v investiční správě" and "~ 0,0 %".

**(2) Sentences mentioning fond/fondy, Global Unicorns, private markets, or investice do firem:**

- **Private markets:** "Současně posilujeme naši aktivitu na privátních trzích, kde systematicky rozvíjíme zejména oblast venture capital…" (truncated to meet the 125-character limit)
- **Fund-related disclaimer text** (the section is for qualified investors only):
  - "Informace uvedené v této části jsou určeny pouze pro kvalifikované investory…" (truncated)
  - "…zákona č. 240/2013Sb., o investičních společnostech a investičních fondech…" (truncated)
  - "…osoba, která učinila prohlášení o tom, že si je vědoma rizik spojených s investováním do tohoto fondu…" (truncated)
  - "…jestliže obhospodařovatel nebo administrátor tohoto fondu kvalifikovaných investorů…" (truncated)
- **Navigation labels only (not sentences):** "Investiční fondy" and "Privátní trhy" appear as menu links.

**Not found:** "Global Unicorns" and "investice do firem" do not appear on the page.

**Notes:**
- The disclaimer sentences are very long. Because of the 125-character limit, I've quoted only fragments, and the full sentences are on the page.
- The page does not show its own publication date. The most recent news item is dated 30/9/2026.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 18. 8. 2010, 15:19

**Sentences mentioning the listed terms** (quotes are shortened to stay under 125 characters, and the rest is paraphrased):

- **CzechInvest and Plug and Play:** The article says that, under the CzechInvest agency's banner, Americans offer selected Czech tech firms a free three-month stay at Plug and Play Tech Center in Silicon Valley, California. Quoted fragment: "pod hlavičkou české státní agentury CzechInvest zdarma nabízí"
- **CzechInvest, Silicon Valley:** CzechInvest reopens applications for a free three-month stay in Silicon Valley. Quoted fragment: "slibným českým podnikatelským nápadům opět otevírá unikátní možnost"
- **CzechAccelerator and CzechInvest:** Applications are accepted from 16 August to the end of September 2010, and the best firms fly out on 1 January 2011. Quoted fragment: "Přihlášky do Českého technologického akcelerátoru CzechAccelerator přijímá CzechInvest"
- **CzechAccelerator and CzechInvest:** Three months in the programme can be a start of a new era for participating firms, according to Alexandra Rudyšarová. Quoted fragment: "Tři měsíce strávené v CzechAcceleratoru agentury CzechInvest mohou být"
- **Plug and Play:** Successful firms get a free three-month office lease at the Plug and Play Tech Center. Quoted fragment: "v kalifornském Plug and Play Tech Center"
- **CzechInvest:** CzechInvest will hold a free introductory training on doing business in the USA before departure. Quoted fragment: "Ještě před odletem do Ameriky CzechInvest pro účastníky zdarma uspořádá"
- **CzechAccelerator:** Applicants can be small and medium firms or start-ups in IT, biotech, environmental technology, or microelectronics. Quoted fragment: "Do CzechAcceleratoru se mohou hlásit malé a střední podniky"
- **CzechAccelerator, Plug and Play, Sunnyvale:** CzechAccelerator is part of the Plug and Play Tech Center in Sunnyvale, which hosts over 250 start-ups. Quoted fragment: "CzechAccelerator agentury CzechInvest je součástí Plug and Play Tech Center v kalifornském Sunnyvale"
- **Sunnyvale:** Google, Sun Microsystems, and Microsoft have headquarters or key development centres in Sunnyvale or nearby. Quoted fragment: "Právě v Sunnyvale nebo jeho nejbližším okolí"
- **CzechAccelerator:** The first three companies have already returned from their stays. Quoted fragment: "Z tříměsíční stáže v CzechAcceleratoru se už vrátily"

**Investice or equity:** Neither word appears in the article. The closest terms are "investoři" (investors) in the lead, which says American investors and major tech companies are looking for young firms, and "bohaté investory" (wealthy investors), which the article says the firms need to fund their projects.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce the full sentences word-for-word. Quotes are capped at 125 characters, and the text outside quotes must differ from the source. So below are short exact excerpts with paraphrases.

**Publication date:** 16 October 2025, 13:15 (the article header reads "16. října 2025 · 13:15")

**Headline:** "Už vybrali čtvrt miliardy" ("They have already raised a quarter billion"). The headline says the fund has already raised about 250 million, presumably in crowns.

**Launch and investment in companies:** "Investiční společnost Emun spouští podílový fond kvalifikovaných investorů." Emun is launching a fund for qualified investors that will put money into companies such as OpenAI, Revolut, or SpaceX.

**Fund name and focus:** "Nový fond Emun Global Unicorns cílí na investice do největších globálních jednorožců." The fund, Emun Global Unicorns, targets the largest global "unicorns," meaning companies valued above one billion dollars.

**Name in a partner's quote:** "Fondem Emun Global Unicorns chceme nabídnout novou možnost." Filip Savi, a partner at Emun, says the fund offers a new way to invest in this segment.

**Size:** "Nový fond již získal do správy přes 200 milionů korun." The fund already manages over 200 million CZK, mostly from Emun and its Family Office clients.

**Public launch:** "Nyní se otevírá veřejnosti." The fund is now open to the public, and investors can join this year either directly through Emun or through selected banks and platforms.

**Minimum investment:** "Přes Emun bude minimální výše investice pět milionů korun." The minimum is 5 million CZK through Emun and 1 million CZK through other distribution channels.

**Currency:** "Investovat bude možné jak v korunách, tak v amerických dolarech." Investors can subscribe in either Czech crowns or US dollars.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "PFCEU Pro Financial Consulting Pezinok investície startupy"

Links: [{"title":"obchodny register","url":"https://finstat.sk/36282600/obchodny_register"},{"title":"acta.mendelu.cz","url":"https://acta.mendelu.cz/pdfs/acu/2011/07/33.pdf"},{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"},{"title":"financovanie podnikania","url":"https://www.podnikajte.sk/temy/financovanie-podnikania?page=17"},{"title":"0621145503 13 Zinecker Rajchlová+RS","url":"https://www.sav.sk/journals/uploads/0621145503 13 Zinecker-Rajchlová+RS.pdf"},{"title":"Prihlásiť sa","url":"https://finstat.sk/53262182/obchodny_register"},{"title":"the biggest investment in fintech startup in slovakia goes to finax","url":"https://finax.eu/blog/the-biggest-investment-in-fintech-startup-in-slovakia-goes-to-finax"},{"title":"Michal Mička z C2H kupuje za desítky milionů korun polovinu finančně poradenské sítě F&P Consulting","url":"https://cc.cz/michal-micka-z-c2h-kupuje-za-desitky-milionu-korun-polovinu-financne-poradenske-site-fp-consulting/"},{"title":"EUROPE LTD","url":"https://wbc-rti.info/object/organisation/13162.html"}]

The search found a Slovak business-register entry for PFCEU s.r.o., but nothing showing that the company invests in startups.

**What the register shows**
- The company's registered office is in Pezinok, at Kataríny Franklovej 5791/10, according to FinStat's extract of the Slovak commercial register.
- Its incorporation date is listed as 25 February 2006.
- Its share capital is 160,000 €, fully paid.
- It was formerly known as Pro Financial Consulting s.r.o., shortened to PFCEU s.r.o., with the former name valid until 26 February 2015. That fits the query's "Pro Financial Consulting" wording.

**What's missing**
- The register extract doesn't describe the company's business activities, investment products, funds, or portfolio companies, so I can't confirm any startup investing from it.
- The other startup-investment results involve unrelated firms. For example, Credo Ventures is a Prague venture capital firm that backs technology startups from Central and Southeast Europe, and LRJ Capital, through its fund GROWWS SICAV, invested 1.5 million euros in Finax.
- A Czech article about a financial advisory network called F&P Consulting, where a 50% stake was bought by the investment group C2H. The name is similar, but it's a different company in a different country, and I found nothing linking it to PFCEU.

**Suggested next steps**
- Check the company's listed business purpose (předmet podnikania) in the Slovak commercial register (orsr.sk) or on its website.
- If it claims to offer investment services, check the National Bank of Slovakia's licensing registers. Investment services are regulated, so a licence should appear there.

I can run a follow-up search in Slovak, such as "PFCEU investície" or "Pro Financial Consulting Pezinok," if you want me to keep looking.


REMINDER:
… [skrátené, 91 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 21:04:13

Most of the picture is in now. Creandum, Plug and Play and Sofina have foreign HQs (Stockholm, Sunnyvale, Belgium), so those three stop at the early exit. EMUN is a Czech asset manager with a new fund, but I have no named company deals yet. PFCEU is still unidentified. I'll run a few more searches for named EMUN holdings, the second EMUN fund and PFCEU's activity.

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Emun Global Unicorns fond portfolio OpenAI SpaceX držba",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Emun Global Private Infrastructure fond",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "PFCEU",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "PFCEU Pezinok investičné služby",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "PFCEU"

Links: [{"title":"Unified Communist Party of Spain","url":"https://en.wikipedia.org/wiki/Unified_Communist_Party_of_Spain"},{"title":"Le mode conseil est activé Arrêter","url":"https://cbonds.fr/etf/5823/"},{"title":"www.pfcu.com","url":"https://www.pfcu.com/about-us/who-we-are/news"},{"title":"Hinweis-Modus ist eingeschaltet Ausschalten","url":"https://cbonds.de/etf/5823/"},{"title":"We are a Ukrainian company. We stand with our colleagues, friends, family, and with all people of Ukraine. Our message","url":"https://getprospect.com/business-directory/partnership-financial-credit-union"},{"title":"snowball-analytics.com","url":"https://snowball-analytics.com/public/asset/PCEU.PA.EUR"},{"title":"www.cuinsight.com","url":"https://www.cuinsight.com/?p=9948"},{"title":"Princeton Federal Credit Union","url":"https://www.cuinsight.com/companies/princeton-federal-credit-union/"},{"title":"Ви перебуваєте в режимі підказок Вимкнути","url":"https://cbonds.com.ua/etf/5823/"},{"title":"www.numeroservicioalcliente.com","url":"https://www.numeroservicioalcliente.com/pfcu/"}]

Links: [{"title":"What does PFCU stand for?","url":"https://acronym24.com/pfcu-meaning/"},{"title":"PFCU Business & Finance Abbreviation","url":"https://acronym24.com/pfcu-meaning-in-business-finance/"},{"title":"Publix Employees Federal Credit Union","url":"https://www.cuinsight.com/companies/publix-employees-federal-credit-union/"},{"title":"timeshighereducation.com","url":"https://timeshighereducation.com/cn/node/4433"},{"title":"Document vyYVYyyGnJ48GqeKwRyRyok09","url":"https://www.toxicdocs.org/d/vyYVYyyGnJ48GqeKwRyRyok09"},{"title":"www.cuinsight.com","url":"https://www.cuinsight.com/?p=9948"},{"title":"www.tradingview.com","url":"https://www.tradingview.com/symbols/EURONEXT-PCEU/analysis"},{"title":"PF is the abbreviation for Peoples Front","url":"https://www.allacronyms.com/PF/Peoples_Front"},{"title":"Philadelphia Federal Credit Union (PFCU)","url":"https://www.cuinsight.com/companies/philadelphia-federal-credit-union-pfcu/"},{"title":"We are a Ukrainian company. We stand with our colleagues, friends, family, and with all people of Ukraine. Our message","url":"https://getprospect.com/business-directory/partnership-financial-credit-union"}]

I couldn't find any results for the exact term "PFCEU." The closest matches are these:

- **PCEU (Spanish political party):** The Unified Communist Party of Spain, abbreviated PCEU, was a political party in Spain. It was a pro-Soviet rival to the Eurocommunist Communist Party of Spain (PCE). It was formed in 1980 and dissolved in 1984.

- **PCEU (ETF ticker):** The Amundi ETF tracking the MSCI Europe index trades on Euronext Paris under the PCEU ticker. Its total expense ratio is 0.15%. Its share class was registered on 25.04.2019 with ISIN FR0013412038.

- **PFCU (credit unions):** Several credit unions use this abbreviation. The best-known is Philadelphia Federal Credit Union, which was founded in 1951
… [skrátené, 681 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "PFCEU Pezinok investičné služby"

Links: [{"title":"obchodny register","url":"https://finstat.sk/36282600/obchodny_register"},{"title":"MsZ PK 2021 11 11 bod06 03","url":"https://www.pezinok.sk/uploadfiles/File/msz/2021-11-11/MsZ_PK_2021-11-11-bod06_03.pdf"},{"title":"ppfbanka.cz","url":"https://ppfbanka.cz/cs/document/download/5631"},{"title":"Pristupnost sluzeb pro osoby se zdravotnim omezenim.sk","url":"https://cdn.patria.cz/Pristupnost-sluzeb-pro-osoby-se-zdravotnim-omezenim.sk.pdf"},{"title":"sk.Pristupnost sluzieb pre osoby so zdravotnym obmedzenim","url":"https://cdn.patria.cz/sk.Pristupnost-sluzieb-pre-osoby-so-zdravotnym-obmedzenim.pdf"},{"title":"Prihlásiť sa","url":"https://finstat.sk/53262182/obchodny_register"},{"title":"Prihlásiť sa","url":"https://finstat.sk/57203423"},{"title":"ppfbanka.cz","url":"https://ppfbanka.cz/cs/document/download/5663"},{"title":"vyrocna 2016 sign","url":"https://old.eic.eu/files/dokumenty/informacie/vyrocna_2016_sign.pdf"}]

The search found registry data for PFCEU, but nothing confirming that it offers investment services.

**Company details (FinStat business register extract):**
- PFCEU s. r. o. has IČO 36282600 and its seat at Kataríny Franklovej 5791/10, 902 01 Pezinok. The company was founded on 25 February 2006.
- Its registered share capital is 160,000 €, all of it paid in.
- Its earlier registered name was Pro Financial Consulting s.r.o., which was abbreviated to PFCEU s.r.o. and valid until 26 February 2015.

**Investment services:**
- None of the results say that PFCEU holds an investment licence or provides investment services.
- One FinStat page (entry 57203423) lists investment services and activities under Act No. 566/2001 Z.z. on securities and investment services. Its excerpt doesn't name the company, though, so I can't tie that page to PFCEU.
- The other results are unrelated. They cover PPF banka, Patria, a 2016 annual report from European Investment Centre, a Pezinok city council document, and another Pezinok company, PK Invest Group.

To confirm whether PFCEU is licensed for investment services, check the National Bank of Slovakia's register of licensed firms. The company's declared business scope (predmet podnikania) in the Slovak business register (orsr.sk) or on its website would also show what it does.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Emun Global Unicorns fond portfolio OpenAI SpaceX držba"

Links: [{"title":"Akcie OpenAI, SpaceX nebo Revolutu chtějí všichni. Žhavé investiční zboží se otevírá i Čechům","url":"https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/"},{"title":"report openai tops 2026s best funded unicorns with 169 billion raised","url":"https://www.itedgenews.africa/report-openai-tops-2026s-best-funded-unicorns-with-169-billion-raised"},{"title":"ar.swissquote.com","url":"https://ar.swissquote.com/trading/investment-products/unicorns"},{"title":"ai unicorns dominate","url":"https://pureai.com/articles/2026/05/15/ai-unicorns-dominate.aspx"},{"title":"openai most funded ai firm us 14 billion raised","url":"https://www.theasset.com/article/51323/openai-most-funded-ai-firm-us-14-billion-raised"},{"title":"spacex dethrones openai as worlds most valuable unicorn at 1 25 trillion","url":"https://www.itedgenews.africa/spacex-dethrones-openai-as-worlds-most-valuable-unicorn-at-1-25-trillion/"},{"title":"Da non perdere |Innovation","url":"https://forbes.it/2025/10/07/openai-cinese-bytedance-10-unicorni-che-valgono-di-piu"},{"title":"private equity","url":"https://swissquote.com/en-ch/private/trade/products/private-equity"},{"title":"OpenAI completes deal at $500bn valuation","url":"https://www.bahamastradeinfo.gov.bs/?p=380880"}]

Links: [{"title":"3.7 Trillion Dollars Capital Of 1217 “Unicorns” Globally.. Five Emirati Fingerprints","url":"https://uac-org.org/en/news/details/5945/3-7-تريليون-دولار-رأسمال-1217-«يونيكورن»-عالمياً-5-بصمات-إماراتية-"},{"title":"Global unicorns","url":"https://www-statista-com.ezproxy.canberra.edu.au/study/70449/unicorn-market-worldwide"},{"title":"The global unicorn club","url":"https://livewiremarkets.com/wires/the-global-unicorn-club"},{"title":"global unicorn valuation 2025","url":"https://www.wipo.int/en/web/global-innovation-index/w/blogs/2026/global-unicorn-valuation-2025"},{"title":"global unicorn valuation 2025","url":"https://www.wipo.int/ar/web/global-innovation-index/w/blogs/2026/global-unicorn-valuation-2025"},{"title":"global unicorn valuation 2025","url":"https://www.wipo.int/ja/web/global-innovation-index/w/blogs/2026/global-unicorn-valuation-2025"},{"title":"countrys unicorns seen rising steadily","url":"https://www.chinaservicesinfo.com/s/202304/19/WS6448c94a498ea274927b90b0/countrys-unicorns-seen-rising-steadily.html"},{"title":"Unicorns worldwide","url":"https://statista.com/study/70449/unicorn-market-worldwide"},{"title":"unicorns by country world map","url":"https://www-statista-com.ezproxy.canberra.edu.au/chart/amp/27266/unicorns-by-country-world-map"}]

Links: [{"title":"V Emunu otevřeli nový fond, vábí investory na OpenAI nebo Revolut. Už vybrali čtvrt miliardy","url":"https://www.e15.cz/finexpert/investujeme/v-emunu-otevreli-novy-fond-vabi-investory-na-openai-nebo-revolut-uz-vybrali-ctvrt-miliardy-1428118"},{"title":"Akcie OpenAI, Space
… [skrátené, 4445 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Emun Global Private Infrastructure fond"

Links: [{"title":"ember infrastructure 500 million fund ii h2o","url":"https://www.axios.com/pro/climate-deals/2024/10/09/ember-infrastructure-500-million-fund-ii-h2o"},{"title":"macquarie private infrastructure fund flyer","url":"https://www.macquarie.com/assets/macq/mam/au/flyer/macquarie-private-infrastructure-fund-flyer.pdf"},{"title":"village.ai","url":"https://village.ai/company/emif"},{"title":"Global Infrastructure Finance targets $1bn with private EM bond fund – exclusive","url":"https://www.infrastructureinvestor.com/global-infrastructure-finance-targets-1bn-with-private-em-bond-fund-exclusive/"},{"title":"infrastructure funds","url":"https://www.mayerbrown.com/en/industries/infrastructure-funds"},{"title":"infrastructure funds","url":"https://www.mayerbrown.com/ja/industries/infrastructure-funds"},{"title":"dealstreetasia.com","url":"https://dealstreetasia.com/?p=341722"},{"title":"infrastructure funds","url":"https://www.mayerbrown.com/pt/industries/infrastructure-funds"},{"title":"• Contact Us","url":"https://www.alternativeswatch.com/2024/03/06/gip-attracts-2-1bn-for-emerging-markets-infrastructure/"}]

Links: [{"title":"ember infrastructure 500 million fund ii h2o","url":"https://www.axios.com/pro/climate-deals/2024/10/09/ember-infrastructure-500-million-fund-ii-h2o"},{"title":"capital innovations gets blumont mandate","url":"https://www.institutionalinvestor.com/article/b150yc4rwwh3p4/capital-innovations-gets-blumont-mandate"},{"title":"capital innovations gets blumont mandate","url":"https://www.institutionalinvestor.com/article/2bszhbcj9w6brakostvcw/innovation/capital-innovations-gets-blumont-mandate"},{"title":"capital innovations gets blumont mandate","url":"https://inv-prd.institutionalinvestor.com/article/2bszhbcj9w6brakostvcw/innovation/capital-innovations-gets-blumont-mandate"},{"title":"Global Infrastructure Finance targets $1bn with private EM bond fund – exclusive","url":"https://privatedebtinvestor.com/global-infrastructure-finance-targets-1bn-with-private-em-bond-fund-exclusive"},{"title":"Global Infrastructure Finance targets $1bn with private EM bond fund – exclusive","url":"https://www.infrastructureinvestor.com/global-infrastructure-finance-targets-1bn-with-private-em-bond-fund-exclusive/"},{"title":"blumont unveils global infrastructure fund","url":"https://institutionalinvestor.com/article/2bsyr1b6z63z7abkljdhc/innovation/blumont-unveils-global-infrastructure-fund"},{"title":"dealstreetasia.com","url":"https://dealstreetasia.com/?p=341722"},{"title":"blumont capital corp","url":"https://institutionalinvestor.com/tag/blumont-capital-corp"},{"title":"Posted inالخبر الأبرز اليوم","url":"https://enterpriseam.com/uae-ar/2026/05/15/تعاون-جديد-بين-كيانات-استثمارية-عملاق/"}]

I couldn't find anything on an "Emun Global Private Infrastructure fund" in two searches. A few funds with similar names came up:

- **EMIF Group (closest name match):** Accor
… [skrátené, 1380 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 21:05:12

The EMUN fund search turned up named portfolio holdings (Anthropic, Databricks, Discord, Kraken) in a cc.cz article, which I need to verify verbatim with a date. I also have no candidate website for PFCEU, so I'll try the likely domain.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/",
  "prompt": "Return word-for-word, without summarising or translating: (1) the article's publication date; (2) every sentence that names the fund Emun Global Unicorns or \"Emun\" together with a fund size (milionů korun, miliard) ; (3) every sentence that lists companies held in the fund's portfolio (V portfoliu fondu, držba, portfolio, Anthropic, Databricks, Discord, Kraken, OpenAI, SpaceX, Revolut)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://pfceu.sk",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that states what the company does (předmet činnosti, investície, poradenstvo, financovanie, fondy), its legal name with s.r.o., its IČO and its seat (sídlo) address."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
unable to verify the first certificate
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**(1) Publication date:**
"16. 10. 2025"

**(2) Sentences naming Emun Global Unicorns or Emun with a fund size:**

- "Fond Emun Global Unicorns je určen kvalifikovaným investorům, ideálně od pěti milionů korun."
- The sentence introducing Emun's fund includes the korun conversion: "...což je v přepočtu 630 milionů až zhruba miliarda korun." (The sentence is longer, so I've shortened it to stay within the 125-character quote limit.)
- "...Emun... majetek v hodnotě přes dvanáct miliard korun." This refers to Emun's total assets under management, not the fund alone. (Shortened to fit the quote limit.)

**(3) Sentence listing portfolio companies:**

- "Expozici má mít aktuálně na firmy jako OpenAI, SpaceX, Revolut, Anthropic, xAI, Kraken, Stripe nebo Databricks."
````

</details>

### 🤖 Claude · 2026-10-08 21:06:17

Both checks came back. The cc.cz article is dated 16 Oct 2025 and names the fund's exposure companies verbatim. The PFCEU site fetch failed on a TLS certificate error, so there is no verifiable website. I have enough to write the records now.

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b03.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b03.json",
  "content": "[\n  {\n    \"candidate_id\": \"C057\",\n    \"website\": \"https://www.emun.cz\",\n    \"identity\": [\n      {\n        \"value\": {\"legal_name\": \"EMUN investiční společnost, a.s.\", \"company_id\": null, \"country\": \"CZ\"},\n        \"value_text\": \"EMUN investiční společnost, a.s.\",\n        \"source_url\": \"https://www.emun.cz/kontakt\",\n        \"quote\": \"EMUN investiční společnost, a.s.\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"legal_name\": null, \"company_id\": \"28495349\", \"country\": \"CZ\"},\n        \"value_text\": \"IČO: 28495349\",\n        \"source_url\": \"https://www.emun.cz/kontakt\",\n        \"quote\": \"IČO: 28495349, DIČ: CZ28495349\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Praha 1\",\n      \"source_url\": \"https://www.emun.cz/kontakt\",\n      \"quote\": \"Anežská 986/10 / 110 00 Praha 1\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"pe\"],\n      \"value_text\": \"investice do největších globálních jednorožců\",\n      \"source_url\": \"https://www.e15.cz/finexpert/investujeme/v-emunu-otevreli-novy-fond-vabi-investory-na-openai-nebo-revolut-uz-vybrali-ctvrt-miliardy-1428118\",\n      \"quote\": \"Nový fond Emun Global Unicorns cílí na investice do největších globálních jednorožců.\",\n      \"published_date\": \"2025-10-16\",\n      \"derivation\": \"inferred\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"OpenAI\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"OpenAI\",\n        \"source_url\": \"https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/\",\n        \"quote\": \"Expozici má mít aktuálně na firmy jako OpenAI, SpaceX, Revolut, Anthropic, xAI, Kraken, Stripe nebo Databricks.\",\n        \"published_date\": \"2025-10-16\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"SpaceX\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"SpaceX\",\n        \"source_url\": \"https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/\",\n        \"quote\": \"Expozici má mít aktuálně na firmy jako OpenAI, SpaceX, Revolut, Anthropic, xAI, Kraken, Stripe nebo Databricks.\",\n        \"published_date\": \"2025-10-16\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Revolut\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Revolut\",\n        \"source_url\": \"https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/\",\n        \"quote\": \"Expozici má mít aktuálně na firmy jako OpenAI, SpaceX, Revolut, Anthropic, xAI, Kraken, Stripe nebo Databricks.\",\n        \"published_date\": \"2025-10-16\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Anthropic\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Anthropic\",\n        \"source_url\": \"https://cc.cz/akcie-openai-spacex-nebo-revolutu-chteji-vsichni-zhave-investicni-zbozi-se-otevira-i-cechum/\",\n        \"quote\": \"Expozici má mít aktuálně na firmy jako OpenAI, SpaceX, Revolut, Anthropic, xAI, Kraken, Stripe nebo Databricks.\",\n        \"published_date\": \"2025-10-16\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"xAI\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"xAI\",\n        \"source_url\
… [skrátené, 8520 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b03.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b03 is done. Output written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b03.json (5 records, valid JSON array).\n\n- C057 EMUN (CZ): investor_type pe (inferred), 8 fund-exposure names from a cc.cz article (16 Oct 2025), early exit none. Doubtful: the holdings are the fund's stated exposure, not verified deals, and the management company itself has no named direct deal. The fund name \"Emun Global Unicorns\" sits in a different sentence from the \"přes 200 milionů korun\" quote, so the name is not inside the quote. Firm AUM \"přes 16 miliard Kč\" from the homepage; cc.cz and another article give 12 and 14 bn, so the figure conflicts.\n- C173 Creandum: early exit foreign_hq (Stockholm, from a 2021 Maddyness article). investor_type left null; the candidate site did not show it.\n- C161 Plug and Play: early exit foreign_hq (Sunnyvale, from a 2010 novinky article). investor_type accelerator, inferred.\n- C167 Sofina: early exit foreign_hq (Belgian holding, Test-Achats 2025). investor_type group_holding. Legal name not verified.\n- C123 PFCEU: early exit no_investment_found. No verifiable website (pfceu.sk gave a TLS certificate error). The only registry data (FinStat, a Slovak Pezinok company) is forbidden as a source and is unconfirmed, so identity and HQ are null."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

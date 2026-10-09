# Subagent: Evidence v3 re-run (3 unresearched) (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-09 05:21:32

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (3 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2r_b01.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2r_b01.json

Today is 2026-10-09.

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2r_b01.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2r_b01.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C063",
4	    "name": "JSK Investments",
5	    "other_names": [],
6	    "known_website": "www.jskinvestments.cz",
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): JSK Investments SICAV a.s., IČO 23823445"
8	  },
9	  {
10	    "candidate_id": "C193",
11	    "name": "Token Ventures",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Token Ventures s.r.o., IČO 09873155"
15	  },
16	  {
17	    "candidate_id": "C098",
18	    "name": "Národný holdingový fond s.r.o.",
19	    "other_names": [],
20	    "known_website": null,
21	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Národný holdingový fond s. r. o., IČO 31384943"
22	  }
23	]
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

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.jskinvestments.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions JSK / investments / portfolio / fund size / ticket / kontakt / address / IČO, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Token Ventures s.r.o. investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Národný holdingový fond s.r.o. investície",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The 125-character limit means I can't reproduce these sentences in full. Below are the relevant excerpts, quoted within the limit, with paraphrases for the rest.

**Sentences mentioning JSK / investments / funds / contact**

1. "JSK Investments je globálním podporovatelem zaměřeným na malé a střední podniky". The page describes JSK as a global supporter of small and medium-sized businesses, providing capital along with support and experience.

2. "JSK Investments Private and Growth Equity Fund I." This is the private and growth equity fund, linked from a "more about the fund" link.

3. "JSK Investments Venture Capital Fund I." This is the venture capital fund, with its own link.

4. "Investiční fond JSK Investments manželů [REDACTED]ových investoval do amerického startupu" (Lupa.cz, 16.9.2026). The article reports that the fund invested in a US surgical-robotics startup.

5. "Investiční fond JSK Investments SICAV a.s. investoval do amerického medtech startupu" (JSK, 16.9.2026). The press release reports the same investment in a medtech startup's Series A round.

6. "JSK Investments SICAV a.s. investuje do amerického startupu Andromeda Surgical" (headline, 16.9.2026).

7. "Kontakt pro start-up". This is the startup contact link, which opens a form.

8. Address: "Klimentská 1216/46" and "110 00 Praha 1" (Prague 1, Czech Republic).

9. "© 2026 All rights reserved (c) JSK Management s.r.o." This is the copyright line in the footer.

**Publication dates shown**

- 19.9.2026 (e15 article)
- 16.9.2026 (Lupa.cz article and JSK press release)

The page itself shows no publication date, only the copyright year 2026.

**Not found:** No IČO (company registration number) and no fund size or ticket figures for the funds themselves. The Andromeda Surgical round size (15 million USD, total financing 30 million USD) appears, but it's the startup's round, not the fund's.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Národný holdingový fond s.r.o. investície"

Links: [{"title":"n rodn holdingov fond nhfond sk","url":"https://venturecapitalarchive.com/venture-funds/n-rodn-holdingov-fond-nhfond-sk"},{"title":"nh fund","url":"https://altss.com/profile/nh-fund.md"},{"title":"narodni investicni nemovitostni fond s r o 14309025","url":"https://www.podnikatel.cz/rejstrik/narodni-investicni-nemovitostni-fond-s-r-o-14309025/"},{"title":"Národní rozvojový fond přichází. Podpoří projekty v infrastruktuře","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-prichazi-podpori-projekty-v-infrastrukture/"},{"title":"Národní rozvojový fond bude spravovat státní banka, na investice půjde až 35 miliard","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/narodni-rozvojovy-fond-bude-spravovat-statni-banka-na-investice-pujde-az-35-miliard-1360230"},{"title":"banky podlehly tlaku politiku rozvojoveho fondu jsou pripraveny investovat az sedm miliard","url":"https://ekonomickydenik.cz/banky-podlehly-tlaku-politiku-rozvojoveho-fondu-jsou-pripraveny-investovat-az-sedm-miliard/"},{"title":"Národní rozvojový fond vlády umožní investice v řádu desítek miliard korun","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-vlady-umozni-investice-v-radu-desitek-miliard-korun/"},{"title":"Ministr Havlíček: Peníze do národního fondu chtějí posílat kromě bank i jiné firmy","url":"https://www.e15.cz/rozhovory/ministr-havlicek-penize-do-narodniho-fondu-chteji-posilat-krome-bank-i-jine-firmy-1360245"},{"title":"strukturalni fondy pomohly zrealizovat pilotni investicni fazi ipo fondu narodni rozvojove investicni a s","url":"https://www.businessinfo.cz/clanky/strukturalni-fondy-pomohly-zrealizovat-pilotni-investicni-fazi-ipo-fondu-narodni-rozvojove-investicni-a-s/"}]

I found only secondary profile pages, not the official site, so the details below are limited.

- **Ownership:** One company profile says the entity is a specialized subsidiary of the Slovak Business Agency that delivers support through risk capital.
- **Investment type:** The same profile says it funds growing businesses through equity stakes in those companies.
- **Structure:** It oversees separate funds that aim to develop small and mid-sized enterprises across Slovakia.
- **Fund activity:** A venture-capital database lists it as running several VC funds for SMEs, alongside consulting and co-financing for projects that exceed a fund's limit.
- **Disclosure:** The altss profile lists its assets under management as undisclosed and says it does not report private funds.

These profiles look like aggregator entries, and the database's claim of "over 20 deals" reads like generic boilerplate, so I wouldn't rely on it without verification.

The search didn't confirm the legal form. Your "s.r.o." may be a mistake, or the name may come from a different register entry. The s.r.o. results I did get were for an unrelated Czech company, Národní investiční nemovitostní fond s.r.o., which i
… [skrátené, 394 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Token Ventures s.r.o. investice"

Links: [{"title":"token ventures com","url":"https://superscout.co/investor/token-ventures-com"},{"title":"Venture Capital","url":"https://altss.com/profile/token-ventures"},{"title":"token ventures token ventures com","url":"https://venturecapitalarchive.com/venture-funds/token-ventures-token-ventures-com"},{"title":"token ventures","url":"https://superscout.co/investor/token-ventures"},{"title":"token ventures","url":"https://app.dealroom.co/companies/token_ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/token-ventures"},{"title":"token ventures","url":"https://crypto-fundraising.info/funds/token-ventures/"},{"title":"www.openvc.app","url":"https://www.openvc.app/fund/Token%20Ventures"},{"title":"300+ investors in your industry, stage, and region Get","url":"https://shizune.co/investors/profile/token-ventures"}]

I didn't find a Czech business-register record or official filing for the s.r.o. entity, so its legal details (company ID, registered address, owners of record) remain unverified. The results are third-party investor profiles of Token Ventures, and they often disagree.

**Basics**
- Altss names Milan Tomanek (CEO and co-founder) and Ondrej Tomek (co-founder) and places the corporate office in Prague .
- The founding year varies: Altss gives 2017, one Superscout page gives 2018, and Caplight gives 2021 <cite index="2-5,1-4,6-1">.
- Team size also conflicts. The other Superscout page describes seven people, including three founding partners <cite index="4-8">, while Altss lists two principals.

**Investment focus**
- Superscout frames the firm's activity as the earliest funding rounds, mainly in Web3 and crypto infrastructure <cite index="1-7">.
- Altss lists long-horizon bets across L1/L2 chains, DeFi, gaming and NFTs, DePIN and IoT <cite index="2-1">, and it also takes positions in coins, tokens and hardware infrastructure <cite index="2-2">.
- Caplight says most of its equity deals happen at seed <cite index="6-3">.
- Altss puts initial tickets at €100,000–€500,000 <cite index="2-10">. The $650k–$3.5M band Shizune reports is a percentile range of seed round sizes drawn from public data, not the firm's own cheque size <cite index="9-8,9-9">.

**Portfolio and deals**
- Portfolio counts conflict. One Superscout page cites six companies <cite index="1-5">, the other cites 28 <cite index="4-9">. Caplight shows 10 <cite index="6-4">, and Shizune shows 9 tracked investments <cite index="9-3">.
- One Superscout page names MoonPay, Arcium, Aleph, Heliotics, Blockmate and C4E among its notable companies <cite index="1-10">. The other credits the firm with early backing of Polygon and 1inch <cite index="4-10">.
- Caplight's deal table lists a December 2023 seed round led by the firm for Zuinq Studio S.L., and a February 2025 seed round for Teneo where it was a co-investor <cite index="6-4">.
- Cry
… [skrátené, 671 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.jskinvestments.cz",
  "prompt": "List the full URLs of the links in the menu or page that lead to pages about the portfolio / investments / companies, the team, the fund(s), and the contact page. Return only the URLs and their link text, word for word."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://token-ventures.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Token Ventures, investments, portfolio, companies invested in, fund size, ticket, team, address, IČO, or contact, and the page's publication date if shown. Also list the URLs of links to portfolio, about, team, and contact pages."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.nhfond.sk",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the fund's name, investments, portfolio, venture capital funds, equity, ticket, address, IČO, or contact, and the page's publication date if shown. Also list the URLs of links to portfolio, about, team, funds, and contact pages."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't show its base domain, so these are the relative paths as they appear in the page:

**Portfolio / investments**
- `/cs/projekty`: "Naše projekty" (menu)
- `/cs/projekty`: "Naše investice" (footer)

**Team**
- `/cs/tym`: "Tým" (menu)

**Funds**
- `/cs/sicav`: "Pro investory" (menu)
- `https://www.jskinvestments.eu`: "Více o fondu" (JSK Investments Private and Growth Equity Fund I.)
- `https://www.jskinvestments.ventures/en`: "Více o fondu" (JSK Investments Venture Capital Fund I.)

**Contact**
- `/cs/kontakt`: "Kontakt" (menu)
- `/cs/kontakt`: "Kontakt" (footer)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences mentioning the fund, investments, venture capital, or equity** (quotes capped at 125 characters):

1. "Špecializovaná dcérska spoločnosť Slovak Business Agency, ktorá implementuje podporu formou rizikového kapitálu."
2. "Podporuje rastovo orientované podnikateľské projekty formou poskytovania rizikového kapitálu" *(truncated)*
3. "Eterus Capital je partnerom pre financovanie podnikateľa vo fáze rastu."
4. "Cieľom Eterus Capital je identifikácia zaujímavých rastových projektov/spoločností, následná realizácia investície" *(truncated)*
5. "Fond je svojím kapitálovým vstupom schopný vyriešiť existujúce joint-venture resp. iné vlastnícke spory."
6. "Fond inovácií a technológií ponúka partnerstvo (FIT) ponúka výrazné zlepšenie finančnej pozície projektu."
7. "Finančné možnosti Fondu poskytujú väčšiu flexibilitu ako financovanie prostredníctvom úveru z finančných inštitúcií."
8. "Fond inovácií a technológií poskytuje priestor, čas a prostriedky pre pôvodný manažment" *(truncated)*
9. "Copyright 2014 - Národný holdingový fond s.r.o."

**Contact and address lines:**
- "Karadžičova 2"
- "811 09 Bratislava"
- "Slovenská republika"
- "Tel. +421 2 3810 2440"
- "nhfond@nhfond.sk"

**Not found on the page:** portfolio, ticket size, IČO, and a publication date. The only date is the copyright year, 2014.

**URLs:**

- **Portfolio:** none found.
- **About:**
  - http://www.nhfond.sk/o-nas/historia-a-poslanie-spolocnosti/ (relative: /o-nas/historia-a-poslanie-spolocnosti/)
  - /o-nas/slovca/
  - /o-nas/sbagency/
- **Team:** /o-nas/nas-tim/
- **Funds:**
  - /fondy-rizikoveho-kapitalu/narodny-holdingovy-fond/podmienky-poskytnutia-investicie/ (the homepage link is written without a leading slash)
  - /fondy-rizikoveho-kapitalu/fond-inovacii-a-technologii/podmienky-poskytnutia/
  - /fondy-rizikoveho-kapitalu/eterus/podmienky-poskytnutia/
- **Contact:** /o-nas/kontakt/ and mailto:nhfond@nhfond.sk
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences about Token Ventures, investments, portfolio, team, and contact**

*About and investment focus*
- "**Token Ventures** is a specialized investment firm focused on digital assets and crypto startups."
- "We back pioneers and entrepreneurs building the next generation of the Internet."
- "Token Ventures was born at the intersection of traditional finance and digital innovation."
- "We provide early-stage capital (pre-seed/seed) to projects with exceptional teams and strong fundamentals."
- "We actively manage a portfolio of digital assets on secondary markets, utilizing fundamental and quantitative research."

*Liquid asset management*
- "We maintain a strategic presence in secondary markets with a primary focus on the **Solana ecosystem**."

*For founders and institutions*
- "When we invest, we become long-term partners committed to your growth."
- "Direct access to our network of top-tier investors and advisors."
- "We provide the framework for companies to safely and strategically enter the digital asset space."

*Contact*
- "Whether you are a founder seeking capital or an institution exploring crypto space, our team is ready to provide the expertise you need." (Too long to quote in full under the 125-character limit; the closing clause is quoted here: "our team is ready to provide the expertise you need.")

*Other*
- "Our node name is TokenVentures and CCN-ID is cc8584cca5"
- "Our validator address is TokenVentures"
- "© 2026 Token Ventures. All rights reserved."

**Not present on the page:** fund size, ticket sizes, IČO (company registration number), and a publication date for the page itself. The dates shown (e.g., 4 March 2026) belong to blog articles, not the page.

**Team (listed on the page)**
- Daniel: Founding Partner
- Martin: Founding Partner
- Tomas: Research Analyst
- Laura: Research Analyst
- Maros: Community Manager

**Portfolio companies listed**
MoonPay Commerce, Arcium, Aleph, Heliotics, Blockmate, Teneo, Opinions.fun, C4E, Swipelux

**URLs**
- About: https://token-ventures.com/#about
- Portfolio: https://token-ventures.com/#portfolio
- Team: https://token-ventures.com/#team
- Contact: https://token-ventures.com/#contact
- Portfolio company links: https://www.hel.io/ (MoonPay Commerce), https://www.arcium.com/, https://www.aleph.cloud/, https://www.heliotics.com/, https://www.blockmate.io/, https://teneo.pro/, https://opinions.fun/, https://c4e.io/, https://www.swipelux.com/
- Team LinkedIn profiles: linkedin.com/in/daniel-maschtovsky-b137a4128/, linkedin.com/in/martin-jancik-token-ventures/, linkedin.com/in/tom%C3%A1%C5%A1-pi%C5%A1kule-b38a231aa/, linkedin.com/in/laura-maschtovsk%C3%A1-10586b247/, linkedin.com/in/maros-kucerka/
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.jskinvestments.cz/cs/projekty",
  "prompt": "Return word-for-word, without summarising or translating, every line naming a portfolio company or investment (company name and any text describing it, round, date), and any sentence about investments, funds, ticket size, or fund size. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.jskinvestments.cz/cs/kontakt",
  "prompt": "Return word-for-word, without summarising or translating, the company name, legal form, IČO / company ID, address, and any sentence about who the company is or what it invests in. Also return any publication date shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.nhfond.sk/o-nas/nas-tim/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence about the company's activity, investments, funds, portfolio companies, or team roles, and any address, IČO, or date shown. Do not summarise."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page contains no portfolio companies or investment details. The only investment-related line is the empty-state message: "Zde zatím nemáme žádné investice" (meaning "We don't have any investments here yet"). The page also has no sentences about funds, ticket sizes, or fund size.

No publication date is shown. The only date is the footer copyright, "© 2026 All rights reserved (c) JSK Management s.r.o.", which is not a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Company name:** JSK Management s.r.o. (shown in the footer as "© 2026 All rights reserved (c) JSK Management s.r.o.")

**Legal form:** s.r.o. (from the company name)

**IČO:** 21285241

**Address:**
Klimentská 1216/46
110 00 Praha 1

**Sentence about the company:** The page has no sentence describing what the company is or what it invests in. The closest is the registration statement: "Společnost je zapsaná v obchodním rejstříku vedeném Městským soudem v Praze pod spisovou značkou C 399495."

**Publication date:** None is shown. The only date is the copyright year, "© 2026."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't list any investments or portfolio companies, and it contains no IČO.

**Company activity and funds:**
- "Máte otázky? Neváhajte a kontaktujte Národný holdingový fond, s.r.o."
- Fund sections listed: "Národný holdingový fond", "Fond inovácií a technológií", and "Eterus Capital".
- Under "Fondy rizikového kapitálu" (venture capital funds), the page links to each fund's conditions for providing investment.

**Team roles:**
- "KONATEĽ" – "Mgr. Martin Holák, PhD."
- "PROJEKTOVÝ MANAŽÉR" – "Mgr. Ján Kutan"
- "PRÁVNIK" – "Mgr. Marek Timko"
- "OFFICE MANAGER" – "Ing. Silvia Holičová"

**Address:**
- "Karadžičova 2, 811 09 Bratislava, Slovenská republika"

**Dates:**
- "Copyright 2014 - Národný holdingový fond s.r.o."
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "JSK Investments Andromeda Surgical investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://token-ventures.com",
  "prompt": "Return word-for-word, without summarising or translating: (1) every line that gives an address, city, country, registered office, or company name in the footer or contact section; (2) the title and date of every blog post, news item, or announcement listed on the page, with its link URL; (3) the exact text of each portfolio company name as displayed in the portfolio section."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Národný holdingový fond investoval do startupu 2025",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**1. Address, city, country, registered office, or company name (footer and contact section)**

The page has no address, city, country, or registered office. The only company name in the footer is in the copyright line: "© 2026 Token Ventures. All rights reserved."

**2. Blog posts and news items**

- "Prediction Markets as a Market Primitive: Building Multilayer Infrastructure" (4 March 2026), https://token-ventures.com/prediction-markets-market-primitive-multilayer-infrastructure/
- "Key Crypto Areas to Watch in 2026" (19 January 2026), https://token-ventures.com/crypto-areas-watchlist-2026/
- "Macro Outlook 2026: Normalizing Inflation Amidst Geopolitical Friction" (13 January 2026), https://token-ventures.com/macro-outlook-2026-inflation-geopolitical-friction/

The page repeats the first two posts under "Load More," so the list above shows each post once.

**3. Portfolio company names (as displayed)**

- MoonPay Commerce
- Arcium
- Aleph
- Heliotics
- Blockmate
- Teneo
- Opinions.fun
- C4E
- Swipelux
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "JSK Investments Andromeda Surgical investice"

Links: [{"title":"Simona [REDACTED]ová investuje desítky milionů do robotické chirurgie. Cílem je zkrátit fronty na operace","url":"https://cc.cz/simona-[REDACTED]ova-investuje-desitky-milionu-do-roboticke-chirurgie-cilem-je-zkratit-fronty-na-operace/"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/jsk-investments-backs-andromeda-surgical"},{"title":"Petra Cihlářová, Investment Director of Venture Capital at JSK Investments: “AI in itself is not an investment thesis”","url":"https://www.techfinitive.com/interviews/petra-cihlarova-investment-director-of-venture-capital-at-jsk-investments/"},{"title":"andromeda surgical raises 150m series a","url":"https://www.trysignalbase.com/news/funding/andromeda-surgical-raises-150m-series-a"},{"title":"Our Investment in Andromeda Surgical: AI Robots for surgery","url":"https://attackcapital.substack.com/p/announcing-our-investment-in-andromeda"},{"title":"andromedasurgical com funding","url":"https://www.extruct.ai/hub/andromedasurgical-com-funding"},{"title":"logoTry Persana","url":"https://insights.persana.ai/Andromeda Surgical"},{"title":"Revolutionizing Surgery: An In-Depth Look at Andromeda Surgical's Founding, Leadership, Funding, and Future Outlook","url":"https://blogs.persana.ai/revolutionizing-surgery-an-in-depth-look-at-andromeda-surgicals-founding-leadership-funding-and-future-outlook"},{"title":"seed 2023 08","url":"https://seedtable.com/companies/andromeda-surgical/funding-rounds/seed-2023-08"}]

JSK Investments, the fund of Simona [REDACTED]ová, has invested in Andromeda Surgical, a San Francisco startup building an autonomous surgical platform. She joined the startup's financing through the fund, and the company has already gathered $30 million from investors overall, according to CzechCrunch.

**The round**
- Andromeda Surgical raised $15 million in a Series A round led by Standard Capital, with participation from JSK Investments, Y Combinator, VOX Capital, Lingotto Innovation, Alumni Ventures, WestWave Capital, and other investors, per Vestbee's September 2026 report. A second source also reports the $15 million Series A but names only Standard Capital, Y Combinator, and Vox Capital as backers. It hasn't said how it will spend the money yet.
- The totals don't reconcile. CzechCrunch's $30 million cumulative figure is double the Series A, which suggests earlier rounds, but the sources don't break those out. Other aggregators are less reliable: one lists only $0.5M total raised, and another says Andromeda Surgical has raised undisclosed amounts of funding.

**JSK's rationale**
- [REDACTED]ová describes the deal as linking the fund's two long-term priorities, healthcare and advanced technology (the investment connects two of the fund's long-term investment priorities).
- Petra Cihlářová, JSK's venture capital investment director, says "AI in itself is not an investment thesis." She looks for a s
… [skrátené, 957 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Národný holdingový fond investoval do startupu 2025"

Links: [{"title":"V Česku vytvoria nový fond na podporu startupov s kapitálom 2,3 miliardy korún","url":"https://www.podnikajte.sk/investor/cesko-fond-startupy"},{"title":"Český stát se poprvé vážně pouští do startupů. Je tu Národní inovační fond","url":"https://www.lupa.cz/clanky/cesky-stat-se-poprve-vazne-pousti-do-startupu-je-tu-narodni-inovacni-fond/"},{"title":"Stát dá na podporu rozjezdu startupů dvě miliardy","url":"https://www.e15.cz/magazin/stat-da-na-podporu-rozjezdu-startupu-dve-miliardy-1235392"},{"title":"Stát začal českým startupům rozdělovat evropské miliardy z Národního plánu obnovy","url":"https://www.lupa.cz/aktuality/stat-zacal-ceskym-startupum-rozdelovat-evropske-miliardy-z-narodniho-planu-obnovy/"},{"title":"prvni investicni fond z narodniho planu obnovy bude spravovat tensor ventures","url":"https://forbes.cz/prvni-investicni-fond-z-narodniho-planu-obnovy-bude-spravovat-tensor-ventures/"},{"title":"Vznikne nový fond, který bude investovat do akcií firem, tzv. IPO fond 2025+","url":"https://advokatnidenik.cz/2025/07/04/vznikne-novy-fond-ktery-bude-investovat-do-akcii-firem-tzv-ipo-fond-2025/"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=113773"},{"title":"stat bude investovat do akcii firem schvalila to vlada","url":"https://ekonomickydenik.cz/stat-bude-investovat-do-akcii-firem-schvalila-to-vlada/"},{"title":"n rodn holdingov fond nhfond sk","url":"https://venturecapitalarchive.com/venture-funds/n-rodn-holdingov-fond-nhfond-sk"}]

Links: [{"title":"n rodn holdingov fond nhfond sk","url":"https://venturecapitalarchive.com/venture-funds/n-rodn-holdingov-fond-nhfond-sk"},{"title":"nh fund","url":"https://altss.com/profile/nh-fund.md"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/nhfond"},{"title":"Fresh 10 Million in Public Funding for Slovenian Startups in 2025 and Popular P2","url":"https://startup.si/en-us/news/fresh-10-million-in-public-funding-for-slovenian-startups-in-2025-and-popular-p2-"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"2025 02 14 eu funding for innovative start ups","url":"https://www.gov.si/en/news/2025-02-14-eu-funding-for-innovative-start-ups/"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/slovenske-startupy-mozu-ocakavat-investi/200322-clanok.html"},{"title":"SIH announces a call for the selection of fund managers to support start-ups for the period 2026–2030","url":"https://www.sih.sk/en/aktuality/sih-vyhlasuje-sutaz-na-vyber-spravcov-fondov-na-pod
… [skrátené, 1434 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/simona-[REDACTED]ova-investuje-desitky-milionu-do-roboticke-chirurgie-cilem-je-zkratit-fronty-na-operace/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions JSK Investments, the investment into Andromeda Surgical, the fund, the amount invested, and the article's publication date (as shown on the page). Keep the original Czech."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "JSK Investments SICAV investoval do amerického medtech startupu Andromeda Surgical tisková zpráva",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.jskinvestments.cz/cs/kontakt",
  "prompt": "Return the exact text of the lines containing the company name, the IČO (company ID number), the address, and the sentence beginning 'Společnost je zapsaná v obchodním rejstříku'. Word-for-word, no summary, no translation."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Teneo seed round 2025 Token Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "AgeVolt funding round February 2025 investors National Holding Fund Slovakia",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- **Company name:** "© 2026 All rights reserved (c) JSK Management s.r.o."
- **IČO:** "IČO" followed by "21285241"
- **Address:** "Klimentská 1216/46" and "110 00 Praha 1"
- **Registry sentence:** "Společnost je zapsaná v obchodním rejstříku vedeném Městským soudem v Praze pod spisovou značkou C 399495."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date (as shown on the page):** "15. 9. 2026"

**Sentences mentioning JSK Investments, the fund, the investment, or the amount** (Czech, with quotes capped at 125 characters per the length limit):

1. "Fond JSK Investments se zapojil do investice do amerického startupu Andromeda Surgical" (the lead; the sentence continues about the startup's goal of shortening the learning curve for complex procedures)

2. "Simona [REDACTED]ová se prostřednictvím svého fondu JSK Investments zapojila do financování startupu" (the article then says the startup wants to hand part of surgical work to machines)

3. "Investice do Andromeda Surgical propojuje dvě naše dlouhodobé investiční priority" ([REDACTED]ová's quote, which goes on to name healthcare and top technology)

4. "Devětačtyřicetiletá podnikatelka investuje do startupů prostředky získané prodejem Zásilkovny."

5. "Do posledního investičního kola amerického startupu ve výši 15 milionů dolarů se měla zapojit" (the rest of the sentence says, per CzechCrunch's information, that her share was in the tens of millions of crowns, an order of magnitude lower)

6. "Podle investiční ředitelky JSK Investments pro startupovou oblast Petry Cihlářové" (the sentence continues with Cihlářová explaining why the fund invested)

7. Photo credit: "Foto: JSK Investments"

8. Photo caption: "Simona [REDACTED]ová, zakladatelka JSK Investments"

**Note:** Several full sentences exceed 125 characters, so I quoted only the opening portion of each. The remainder is paraphrased above and is not reproduced word-for-word.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "AgeVolt funding round February 2025 investors National Holding Fund Slovakia"

Links: [{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/nhfond"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/agevolt"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/agevolt"},{"title":"19. 09. 2025 Pontis Foundation","url":"https://www.nadaciapontis.sk/en/news/impact-ventures-fund-invests-half-a-million-euros-in-technologies-of-the-future/"},{"title":"19. 09. 2025 Pontis Foundation","url":"https://www.nadaciapontis.sk/en/?p=41760"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/agevolt"},{"title":"www.startup-energy-transition.com","url":"https://www.startup-energy-transition.com/set100-database/agevolt/"},{"title":"Pápež si zo Slovenska odnáša unikátny startupový dar, vďaka Slovákom si bude môcť nabíjať svoje elektromobily aj doma","url":"https://www.startitup.sk/papez-si-zo-slovenska-odnasa-unikatny-startupovy-dar-vdaka-slovakom-si-bude-moct-nabijat-svoje-elektromobily-aj-doma/"},{"title":"InoBat Valuation, Funding & Investors","url":"https://multiples.vc/private-comps/inobat"}]

I found only one source that ties the National Holding Fund (Národný holdingový fond, NHF) to AgeVolt's February 2025 round, and it's a data aggregator rather than an official announcement. Other sources confirm a February 2025 round but don't name NHF.

**NHF's link (Caplight only)**
- Caplight's fund profile describes NHF as a venture capital firm that invests in Slovak small and medium-sized companies, mainly at seed, start-up, and expansion stages. Národný holdingový fond is a venture capital firm that invests in small and medium-sized enterprises in Slovakia.
- That same profile tags AgeVolt's February 2025 VC round as one where NHF was a co-investor. AgeVolt, Feb 2025, VC Round, Co-investor is how the investment appears in its table, so NHF was not presented as the lead.
- Caplight's AgeVolt page dates the last round to Feb 20, 2025 and lists Národný holdingový fond among its investors, alongside Impact Ventures and IPM Group.

**Round size and other investors**
- Dealroom reports a subsequent €1.3 million in February 2025, and its valuation figure is €20.0m. It doesn't name the investors in that round.
- Dealroom's earlier round, €1.2 million in June 2021, involved InoBat, IPM Group, and the Venture to Future Fund.
- VCBacked lists AgeVolt's investors as InoBat, EIT Urban Mobility, Venture to Future Fund, Impact Ventures, IPM Group. It doesn't mention NHF.

**A separate later investment**
- A Pontis Foundation release dated 19 September 2025 says Impact Ventures put €300,000 into AgeVolt. That was a later deal, not the February round.

**Caveats**
- The sources disagree on total funding. Caplight estimates Total Funding Raised of $4.98M, while VCBacked puts the to
… [skrátené, 362 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Teneo seed round 2025 Token Ventures"

Links: [{"title":"token ventures","url":"https://defillama.com/raises/token-ventures"},{"title":"Advanced Blockchain AG","url":"https://app.boersengefluester.de/en/newswire/DE000A0M93V6/advanced-blockchain-ag/portfolio-company-teneo-raises-3m-to-disrupt-social-media-data-2088559"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/token-ventures"},{"title":"certik ventures","url":"https://defillama.com/raises/certik-ventures"},{"title":"ArticleMar 3, 2025","url":"https://9o1hbtdj3x.depinhub.io/news/teneo-protocol-secures-3-million-in-seed-round-funding-21984"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/teneo-protocol-raises-3m-for-depin-startup"},{"title":"Recently FundedUSD 3.0MBlockchain Services","url":"https://www.trysignalbase.com/news/funding/teneo-protocol-raises-3m-in-seed-funding-to-unlock-the-future-of-real-world-data-in-web3-ecosystems"},{"title":"venionaire capital","url":"https://defillama.com/raises/venionaire-capital"},{"title":"2025 02 01 teneo protocol seed","url":"https://startupintros.com/news/2025-02-01-teneo-protocol-seed"},{"title":"Second Photo","url":"https://www.tryfundable.ai/company/teneo-protocol"}]

Teneo (also called Teneo Protocol) raised about $3 million in a seed round in early 2025, and Token Ventures took part as a non-lead investor, according to trackers that list it. The search didn't turn up a primary announcement from Teneo or Token Ventures naming it.

**Round details**
- DefiLlama logs the round at $3M on 13 February 2025, with RockawayX, Generative Ventures, Borderless Capital as lead investors.
- An Advanced Blockchain AG press release dated 19 February 2025 says it announces the successful close of Teneo's seed funding round. That release says Teneo raised USD 3 million, and it names Borderless Capital, Generative Ventures and RockawayX as the leads.
- Dates vary by outlet. Startupintros says the round was announced on 02/01/25. Techleap's article is dated Jun 2025, which suggests it was a later write-up.

**Token Ventures' role**
- Caplight's profile for Token Ventures lists Teneo's February 2025 seed deal as one where the firm was a Co-investor, not the lead.
- DefiLlama also places Token Ventures in its list of Other Investors for the round.
- The Advanced Blockchain release names Moonrock Capital, Outlier Ventures and Certik Ventures among the additional backers, but it doesn't mention Token Ventures.

**About Token Ventures**
- It operates out of Prague and dates to 2021, as a venture capital firm founded in 2021 and based in Prague, Czech Republic.
- Its investing focus covers blockchain technologies, crypto infrastructure, Web3 startups, DeFi, Gaming, and NFTs.
- Seed-stage equity is its usual entry point, though it also buys tokens outright.

**About Teneo**
- Its product gives clients fast access to social platform data. It uses d
… [skrátené, 313 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "JSK Investments SICAV investoval do amerického medtech startupu Andromeda Surgical tisková zpráva"

Links: [{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/jsk-investments-backs-andromeda-surgical"},{"title":"Simona [REDACTED]ová investuje desítky milionů do robotické chirurgie. Cílem je zkrátit fronty na operace","url":"https://cc.cz/simona-[REDACTED]ova-investuje-desitky-milionu-do-roboticke-chirurgie-cilem-je-zkratit-fronty-na-operace/"},{"title":"Petra Cihlářová, Investment Director of Venture Capital at JSK Investments: “AI in itself is not an investment thesis”","url":"https://www.techfinitive.com/interviews/petra-cihlarova-investment-director-of-venture-capital-at-jsk-investments/"},{"title":"andromeda surgical raises 150m series a","url":"https://www.trysignalbase.com/news/funding/andromeda-surgical-raises-150m-series-a"},{"title":"Revolutionizing Surgery: An In-Depth Look at Andromeda Surgical's Founding, Leadership, Funding, and Future Outlook","url":"https://blogs.persana.ai/revolutionizing-surgery-an-in-depth-look-at-andromeda-surgicals-founding-leadership-funding-and-future-outlook"},{"title":"Our Investment in Andromeda Surgical: AI Robots for surgery","url":"https://attackcapital.substack.com/p/announcing-our-investment-in-andromeda"},{"title":"142797 andromeda surgical raises 15m to bring autonomy to the operating room","url":"https://dealroom.co/news/142797-andromeda-surgical-raises-15m-to-bring-autonomy-to-the-operating-room/"},{"title":"andromedasurgical com funding","url":"https://www.extruct.ai/hub/andromedasurgical-com-funding"},{"title":"andromeda surgical","url":"https://www.vcbacked.co/company/andromeda-surgical"}]

Links: [{"title":"Simona [REDACTED]ová investuje desítky milionů do robotické chirurgie. Cílem je zkrátit fronty na operace","url":"https://cc.cz/simona-[REDACTED]ova-investuje-desitky-milionu-do-roboticke-chirurgie-cilem-je-zkratit-fronty-na-operace/"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/jsk-investments-backs-andromeda-surgical"},{"title":"Petra Cihlářová, Investment Director of Venture Capital at JSK Investments: “AI in itself is not an investment thesis”","url":"https://www.techfinitive.com/interviews/petra-cihlarova-investment-director-of-venture-capital-at-jsk-investments/"},{"title":"JSK Investments Simony [REDACTED]ové investoval 420 tisíc eur do AI startupu Elin.ai","url":"https://www.lupa.cz/aktuality/jsk-investments-simony-[REDACTED]ove-investuje-420-tisic-eur-do-ai-startupu-elin-ai/"},{"title":"[REDACTED]","url":"https://forbes.cz/lists/zeny25/simona-[REDACTED]ova/"},{"title":"Investujte jako Simona [REDACTED]ová. Zakladatelka Zásilkovny otevírá fond, do kterého chce miliardy","url":"https://cc.cz/investujte-jako-simona-[REDACTED]ova-zakladatelka-zasilkovny-otevira-fond-do-ktereho-chce-miliardy/"},{"title":"[REDACTED] vstupuje do zdravotnictvi ziskala majoritni podil u vyrobce outdoorovych voziku pro lidi s handicap
… [skrátené, 2929 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/investujte-jako-simona-[REDACTED]ova-zakladatelka-zasilkovny-otevira-fond-do-ktereho-chce-miliardy/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the JSK Investments SICAV, the fund's name, its size or initial volume (výše, objem, miliard, milionů), its licence from the Czech National Bank, the Venture Capital sub-fund, and the article's publication date as shown on the page. Keep the original Czech. Keep each sentence whole if possible."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "AI Data Service DePIN seed round Token Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://token-ventures.com",
  "prompt": "Does the page mention any city, country, office location, or founding year (for example Prague, Praha, Czech, Czechia, Slovakia, Bratislava, Brno, London, Zug, or similar)? Quote word-for-word every such sentence, or answer 'none' if there is none. Do not summarise."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "AgeVolt raises seed funding 2025 Impact Ventures IPM Group investors press release",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.nhfond.sk/fondy-rizikoveho-kapitalu/narodny-holdingovy-fond/podmienky-poskytnutia-investicie/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the fund's size or capital (vklad, kapitál, mil. EUR, objem), year of establishment, companies in which the fund has invested or a portfolio (portfólio, investície, spoločnosti), or the page's publication date. Do not summarise."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page does not mention any city, country, or office location. It gives one date that could be read as a founding year, though it doesn't say the company was founded then:

"Since 2018, we have navigated the complexities of the crypto industry,"

"transitioning to a full-time focus on digital assets in 2020."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't contain the fund's size or capital, its establishment year, a list of portfolio companies, or a publication date. The closest matches are:

1. **Investment size (not fund size):** "maximálna výška investície závisí od konkrétnych kritérií daného fondu" *(from the "Veľkosť investície" section)*

2. **Copyright line (not an establishment year):** "Copyright 2014 - Národný holdingový fond s.r.o."

3. **Portfolio navigation link (no portfolio content):** "Portfólio"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Článek je z **30. 9. 2025** (uvedeno jako „30. 9. 2025“). Z limitu 125 znaků na citaci vyplývá, že nemohu vrátit celé věty, jen kratší úryvky. Zbytek shrnuji vlastními slovy.

- **Vznik SICAV:** Pod hlavičkou JSK Investments vznikl samosprávný investiční fond pro kvalifikované investory: „vznikl samosprávný investiční fond kvalifikovaných investorů typu SICAV“.
- **Minimální vklad:** Do fondu lze vstoupit s minimální investicí 125 tisíc eur, tedy zhruba tři miliony korun.
- **Velikost fondu:** Zakladatelé do fondu vkládají „zhruba dvě miliardy korun“.
- **Cílový objem:** Ve střednědobém horizontu chtějí objem zvýšit na „vyšší jednotky miliard korun“, které mají přijít hlavně od externích investorů.
- **Licence:** Článek uvádí, že skupina získala licenci k založení samosprávného SICAV: „Získáním licence k založení samosprávného SICAV“. Licenci nevydává Česká národní banka výslovně uvedena, takže to z textu nelze ověřit.
- **Postavení na trhu:** Podle článku je v Česku jen několik samosprávných SICAV: „V České republice je jen několik samosprávných SICAV“.
- **Podfond Venture Capital:** Zaměřuje se na menšinové vstupy do perspektivních startupů v raných fázích. Původní věta: „Druhý podfond Venture Capital se zaměřuje na menšinové vstupy do perspektivních startupů v raných fázích.“
- **Cíl výnosu u Venture Capital:** Očekávaná roční návratnost je 10 %, což článek uvádí slovy „u Venture Capital pak 10 %“.
- **Název fondu:** Článek nedává konkrétní název fondu, jen uvádí JSK Investments jako pod hlavičkou fungující subjekt.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "AI Data Service DePIN seed round Token Ventures"

Links: [{"title":"token ventures","url":"https://crypto-fundraising.info/funds/token-ventures/"},{"title":"theblock.co","url":"https://theblock.co/post/411022"},{"title":"token ventures","url":"https://icoanalytics.org/funds/token-ventures/"},{"title":"DePIN project Vangrid raises $9 million in token round to build spatial data network for physical AI","url":"https://www.theblock.co/amp/post/411022/depin-project-vangrid-funding-token-round-spatial-data-physical-ai"},{"title":"depin project vangrid funding token round spatial data physical ai","url":"https://theblock.co/post/411022/depin-project-vangrid-funding-token-round-spatial-data-physical-ai"},{"title":"token ventures","url":"https://defillama.com/raises/token-ventures"},{"title":"2026 08 06 depin project vangrid funding token round spatial data physical ai 411022","url":"https://theblock.co/news/deals/2026-08-06-depin-project-vangrid-funding-token-round-spatial-data-physical-ai-411022"},{"title":"DePIN Grass raises $10M from Polychain, Tribe Capital","url":"https://blockworks.com/news/depin-grass-raise-polychain-tribe"},{"title":"venionaire web3","url":"https://crypto-fundraising.info/funds/venionaire-web3/"}]

The search points to a February 2025 seed round of about $3 million with Token Ventures among the backers. The fundraising trackers don't name the project, though, so the company identity is my inference.

- **The round:** The crypto-fundraising tracker lists a February 2025 seed deal of roughly $3 million in the AI Data Service DePIN category. RockawayX, Borderless Capital, and Generative Ventures are shown as lead investors, and Token Ventures is among the other participants. Seed Feb 2025, raised 3000000, AI Data Service DePIN

- **Likely project:** DefiLlama's Token Ventures page lists a $3m seed round dated 13 February 2025 for Teneo, a DePIN-category company that connects real-world data with Web3 applications. The entry shows the same lead investors and Token Ventures as a participant. Teneo, 13 Feb 2025, $3m, Seed, DePIN, a decentralized platform that bridges real-world data with Web3 applications, lead investors RockawayX, Generative Ventures, Borderless Capital, with Token Ventures among other investors. The matching date, amount, and investor list make Teneo very likely, but I didn't find a primary announcement confirming it.

- **A different deal:** The Block reported a $9 million seed round for Vangrid, a spatial-data DePIN, in early August 2026. Vangrid, a decentralized physical infrastructure network focused on collecting spatial data, raised $9 million in a seed funding round. The named participants in that round don't include Token Ventures. HashKey, Borderless, Crypto.com Capital, Animoca Brands, Gate Labs and Mapleblock Capital participated as "key stakeholders." Because it's also a DePIN seed round, it could be confused with the one you asked about.

All of these figures come from agg
… [skrátené, 213 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "AgeVolt raises seed funding 2025 Impact Ventures IPM Group investors press release"

Links: [{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/agevolt"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/agevolt"},{"title":"Slovenská firma získala investíciu vo výške 1,3 milióna eur: Mení budúcnosť nabíjania a plánuje expanziu","url":"https://www.startitup.sk/slovenska-firma-ziskala-investiciu-vo-vyske-13-miliona-eur-meni-buducnost-nabijania-a-planuje-expanziu/"},{"title":"Funding Rounds","url":"https://prod.actual.seedtable.com/funding-rounds/agevolt-unknown-2021"},{"title":"startup-seeker.com","url":"https://startup-seeker.com/company/agevolt~com"},{"title":"www.dealstreetasia.com","url":"https://www.dealstreetasia.com/?p=277526"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/respond-flow/financials"},{"title":"voltr raises eu4 million to industrialize lithium battery refurbishment in europe","url":"https://www.causeartist.com/blog/voltr-raises-eu4-million-to-industrialize-lithium-battery-refurbishment-in-europe"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/agecurve/financials"},{"title":"How Much Did Volt Money Raise? Funding & Key Investors","url":"https://clay.com/dossier/volt-money-funding"}]

I didn't find an official AgeVolt press release in these results, and the sources disagree on the amounts, so treat the figures as unconfirmed.

**Most detailed report (Slovak outlet Startitup, undated in the results):** A Slovak company, AgeVolt, which specializes in smart EV charging, received another significant investment of 1.3 million euros. The capital came from the National Holding Fund, managed by the Slovak Business Agency, and from Impact Ventures, a fund focused on linking business with sustainability, which was set up by three firms: Pontis Impact, CB ESPRI Impact One and TnC X. Founder Ján Zuštiak said the money would help the company strengthen research and development, with a focus on integrating artificial intelligence and machine learning into its products. The article also puts the company's valuation at about 20 million euros, with 2023 revenue of 1.4 million euros and a loss of 280 thousand euros.

The same article says AgeVolt's earlier round came in 2021, when it received 1.2 million euros from a consortium of InoBat, IPM Group and the Venture to Future Fund. It also mentions a 2.7 million euro grant from the Research and Innovation Authority (VAIA), in cooperation with the Faculty of Electrical Engineering and Informatics at STU in Bratislava.

**Conflicting data from funding databases:**
- VCBacked lists $416K in total funding, with its most recent round announced in September 2025. Its investor list includes InoBat, EIT Urban Mobility, Venture to Future Fund, Impact Ventures, IPM Group.
- Caplight shows a VC round dated February 20, 2025, and a total funding figu
… [skrátené, 840 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/slovenska-firma-ziskala-investiciu-vo-vyske-13-miliona-eur-meni-buducnost-nabijania-a-planuje-expanziu/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Národný holdingový fond (NHF), the National Holding Fund, Impact Ventures, AgeVolt's investment of 1,3 milióna eur, and the article's publication date as shown on the page. Keep the original Slovak. Do not summarise."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.jskinvestments.cz/cs/kontakt",
  "prompt": "Return the exact, complete line of text that contains the number 21285241, word for word, including any label before it (for example 'IČO' with or without a colon) and the line that contains 'JSK Management'. Do not summarise."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Teneo Protocol seed round $3 million investors Token Ventures announcement",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.lupa.cz/aktuality/jsk-investments-simony-[REDACTED]ove-investuje-420-tisic-eur-do-ai-startupu-elin-ai/",
  "prompt": "Return word-for-word, without summarising or translating, the headline, every sentence that mentions JSK Investments, Elin.ai, the investment of 420 tisíc eur, the round or stage, and the article's publication date as shown on the page. Keep the original Czech."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**IČO line:**
"IČO" followed by the line "21285241"

**JSK Management line:**
"© 2026 All rights reserved (c) JSK Management s.r.o."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Nadpis:**
"JSK Investments Simony [REDACTED]ové investoval 420 tisíc eur do AI startupu Elin.ai"

**Datum publikace:**
"9. 12. 2024"

**Věty zmiňující JSK Investments, Elin.ai, investici, kolo nebo fázi:**

1. "Virtuální AI kamarádka pro mladé Elin.ai získala v pre-seed kole investice ve výši 1 milion eur" "(v přepočtu asi 25 milionů Kč)."

2. "Skoro polovinu, 420 tisíc eur, přitom do firmy spoluzakladatele Jana Romportla vložila investiční firma" "JSK Investments podnikatelky Simony [REDACTED]ové."

3. "Elin.ai je mobilní aplikací zaměřenou na uživatele z tzv. generace Z."

4. "JSK Invest do Elin.ai neinvestuje jen peníze, startupu chce pomoci poradenstvím či kontakty" "i s praktickými kroky při plánované expanzi."

5. "Investice od JSK nám umožní rozšířit aplikaci na zahraniční trhy a posílit naše AI modely, které budou" "pokrývat stále více psychických problémů, jež trápí dnešní generaci Z," dodává.

6. Popisek fotografie: "Autor: JSK Investments"

Věty jsou rozděleny na několik citovaných úseků, aby žádný citát nepřesáhl 125 znaků.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Národný holdingový fond (NHF) a Impact Ventures**

- Kapitál pochádza od Národného holdingového fondu, spravovaného Slovak Business Agency, a fondu Impact Ventures, ktorý sa zameriava na prepojenie podnikania s udržateľnosťou a bol založený trojicou firiem – Pontis Impact, CB ESPRI Impact One a TnC X.
  - *Úryvok 1 (v rozsahu limitu):* "Kapitál pochádza od Národného holdingového fondu, spravovaného Slovak Business Agency, a fondu Impact Ventures,"
  - *Úryvok 2 (v rozsahu limitu):* "ktorý sa zameriava na prepojenie podnikania s udržateľnosťou a bol založený trojicou firiem"
- "Jedným z hlavných investorov do AgeVoltu je fond Impact Ventures, ktorý združuje tri spoločnosti s rôznym zameraním:"
- "Zo spolupráce sa teší aj samotný Impact Ventures."
- "Pre nás v Impact Ventures je dôležité vidieť pozitívny sociálny vplyv v startupoch, do ktorých investujeme."

**Investícia AgeVoltu vo výške 1,3 mil. eur**

- "Slovenská firma získala investíciu vo výške 1,3 milióna eur: Mení budúcnosť nabíjania a plánuje expanziu"
- "AgeVolt získal investíciu 1,3 mil. eur."
- "získala ďalšiu významnú investíciu vo výške 1,3 milióna eur."
- "Investícia im pomôže upevniť pozíciu lídra na slovenskom trhu."

**Dátum publikácie**

- "21. februára 2025 o 13:55" (uvedené dvakrát na stránke)

Úryvky sú skrátené tak, aby žiadna citácia neprekročila 125 znakov, takže niektoré vety sú rozdelené na viac častí, a veta o investícii v plnom znení by presiahla limit. Slovenský text je zachovaný bez prekladu a bez sumarizácie.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Teneo Protocol seed round $3 million investors Token Ventures announcement"

Links: [{"title":"Advanced Blockchain AG","url":"https://app.boersengefluester.de/en/newswire/DE000A0M93V6/advanced-blockchain-ag/portfolio-company-teneo-raises-3m-to-disrupt-social-media-data-2088559"},{"title":"2025 02 01 teneo protocol seed","url":"https://startupintros.com/news/2025-02-01-teneo-protocol-seed"},{"title":"ArticleMar 3, 2025","url":"https://9o1hbtdj3x.depinhub.io/news/teneo-protocol-secures-3-million-in-seed-round-funding-21984"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/teneo-protocol-raises-3m-for-depin-startup"},{"title":"token ventures","url":"https://defillama.com/raises/token-ventures"},{"title":"Recently FundedUSD 3.0MBlockchain Services","url":"https://www.trysignalbase.com/news/funding/teneo-protocol-raises-3m-in-seed-funding-to-unlock-the-future-of-real-world-data-in-web3-ecosystems"},{"title":"certik ventures","url":"https://defillama.com/raises/certik-ventures"},{"title":"teneo protocol seed round","url":"https://coinlaunch.space/de/events-rounds/teneo-protocol-seed-round/"},{"title":"Second Photo","url":"https://www.tryfundable.ai/company/teneo-protocol"},{"title":"teneo protocol","url":"https://www.vcbacked.co/company/teneo-protocol"}]

**Short answer:** Teneo did raise a $3 million seed round in February 2025. I found no standalone Token Ventures announcement, though one data aggregator lists Token Ventures as an investor.

**The round**
- An Advanced Blockchain AG press release dated February 19, 2025, says the round totaled $3 million and was co-led by Borderless Capital, Generative Ventures, and RockawayX. Teneo raised USD 3 million, co-led by Borderless Capital, Generative Ventures, and RockawayX.
- That release names other backers as Outlier Ventures, Certik Ventures, and Moonrock Capital. Additional backers included Outlier Ventures, Certik Ventures, Moonrock Capital.
- Advanced Blockchain had first invested in Teneo in November 2024, according to the same release. Since ABAG's initial investment in November 2024, Teneo has achieved remarkable milestones
- Lead arrangements differ across sources. One TechLeap feed item credits RockawayX and Borderless with leading the round and describes Generative Ventures as a participant. It raised $3 million in a seed round led by RockawayX and Borderless, with participation from Generative Ventures.

**Token Ventures**
- DefiLlama's Token Ventures page lists Teneo's February 13, 2025 seed round at $3m, with Token Ventures among the other investors. Teneo | 13 Feb 2025 | $3m | Seed | DePIN, with Token Ventures among the listed other investors.
- That is the only source I found naming Token Ventures. The Advanced Blockchain release does not mention it, and VCBacked's top-investor list omits it, though that list shows only a few names. Treat Token Ventures' participation as unconfirmed until Teneo or Token Ventures confirms it.

**Dates vary
… [skrátené, 1065 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Token Ventures\" seed round led investors 2025 announces funding",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Token Ventures\" investment 2026 raises pre-seed",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Token Ventures" seed round led investors 2025 announces funding"

Links: [{"title":"token ventures","url":"https://crypto-fundraising.info/funds/token-ventures/"},{"title":"token ventures","url":"https://defillama.com/raises/token-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/token-ventures"},{"title":"postfinance and existing investors octopus ventures","url":"https://paymentexpert.com/tag/postfinance-and-existing-investors-octopus-ventures/"},{"title":"asset token ventures","url":"https://www.vcbacked.co/company/asset-token-ventures"},{"title":"token ventures","url":"https://icoanalytics.org/funds/token-ventures/"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/case-wallet/financials"},{"title":"2025 01 01 token security series a","url":"https://startupintros.com/news/2025-01-01-token-security-series-a"},{"title":"Venture Capital","url":"https://altss.com/profile/token-ventures"},{"title":"2024 05 01 token security seed","url":"https://startupintros.com/news/2024-05-01-token-security-seed"}]

I didn't find a 2025 seed round that Token Ventures led. The closest match is a roughly $3 million seed round for Teneo in February 2025, where Token Ventures was one of several backers.

**The Teneo round**
- Fundraising trackers record a February 2025 seed round of about $3 million for Teneo, a DePIN project. RockawayX, Generative Ventures, Borderless Capital are listed as the lead investors, with Token Ventures among the other participants.
- Caplight's investor page labels Token Ventures' role in the Teneo round as co-investor, not lead. Teneo, Feb 2025, Seed, Co-investor
- I found no press release from Token Ventures, Teneo, or the leads in these results. The details come from third-party databases, which don't fully agree on the firm's background.

**Other Token Ventures details**
- Caplight describes Token Ventures as a Prague-based venture firm that invests mainly at the seed stage in blockchain and Web3 companies. It gives the founding year as 2021. Altss gives the founding year as 2017.
- Altss says the firm writes pre-seed and seed checks and does not lead Series A or later rounds. Its listed sector focus, which includes enterprise software and healthtech, doesn't match its crypto focus elsewhere, so that profile looks unreliable.
- Token Ventures was also listed among the investors in an April 2023 seed round for a $3.3 million payments project. That round is not from 2025.

**Possible mix-ups**
- Several results were for other companies. Token Security's rounds are unrelated to Token Ventures.
- If you meant Asset Token Ventures, a different firm, VCBacked reports $5.3M in total funding, with the most recent round listed as Venture - Series Unknown. The last funding was announced in April 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Token Ventures" investment 2026 raises pre-seed"

Links: [{"title":"token ventures","url":"https://superscout.co/investor/token-ventures"},{"title":"Venture Capital","url":"https://altss.com/profile/token-ventures"},{"title":"token ventures com","url":"https://superscout.co/investor/token-ventures-com"},{"title":"asset token ventures","url":"https://www.vcbacked.co/company/asset-token-ventures"},{"title":"How web3 startups raise funding in 2026 (and actually scale)","url":"https://waveup.com/blog/how-web3-startups-can-raise-funding-and-scale-in-2025/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/token-ventures"},{"title":"www.mexc.com","url":"https://www.mexc.com/it-IT/news/593208"},{"title":"Web3 Startup Funding in Q2 2026: The First Pre-Seed & Seed Report (Real Medians, Verified Deals)","url":"https://blog.innmind.com/web3-startup-funding-in-q2-2026-the-first-pre-seed-seed-report-real-medians-verified-deals/"},{"title":"token ventures","url":"https://crypto-fundraising.info/funds/token-ventures/"}]

I found no report of Token Ventures making or announcing a pre-seed investment in 2026. The most recent Token Ventures deals in these results date to early 2025, and the sources disagree on basic facts about the firm.

**Recent deals**
- Caplight's profile lists ten portfolio companies. The newest entries are Teneo rounds from February 2025, where Token Ventures was a co-investor. Its only lead listed is a December 2023 seed round for Zuinq Studio. Caplight lists Teneo, Teneo Protocol, Sharky, and Zuinq Studio S.L. among Token Ventures' investments.
- A crypto-fundraising listing shows Token Ventures among the investors in a $3M seed round for an AI data and DePIN project in February 2025. The listing names RockawayX, Borderless Capital, Generative Ventures, and about a dozen other investors, including Token Ventures.

**Stated focus**
- Superscout says the firm concentrates on pre-seed and seed deals in gaming, IoT, DeFi, and layer-1/layer-2 blockchains. It invests primarily in early-stage projects, specifically at the pre-seed and seed stages. The firm targets sectors such as gaming, IoT, decentralized finance (DeFi), and layer-1/layer-2 blockchains.
- Caplight describes the firm as a Prague-based venture capital firm founded in 2021. A venture capital firm founded in 2021 and based in Prague, Czech Republic.

**Conflicting profiles**
- Superscout gives a different history. It says the firm was established in 2018 and moved into digital assets around 2020.
- Altss describes a firm that avoids crypto and Web3 projects. It says the firm focuses on software and AI-enabled companies where capital efficiency and rapid scaling are achievable. Those claims clash with the crypto-focused profiles above, so Altss may describe a different firm with the same name, or one of the profiles may be out of date.

**Market context (not specific to Token Ven
… [skrátené, 682 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2r_b01.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2r_b01.json",
  "content": "[\n  {\n    \"candidate_id\": \"C063\",\n    \"website\": \"https://www.jskinvestments.cz\",\n    \"identity\": [\n      {\n        \"value\": {\"legal_name\": \"JSK Management s.r.o.\", \"company_id\": null, \"country\": \"CZ\"},\n        \"value_text\": \"JSK Management s.r.o.\",\n        \"source_url\": \"https://www.jskinvestments.cz/cs/kontakt\",\n        \"quote\": \"© 2026 All rights reserved (c) JSK Management s.r.o.\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"legal_name\": \"JSK Management s.r.o.\", \"company_id\": \"21285241\", \"country\": \"CZ\"},\n        \"value_text\": \"21285241\",\n        \"source_url\": \"https://www.jskinvestments.cz/cs/kontakt\",\n        \"quote\": \"21285241\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Praha 1\",\n      \"source_url\": \"https://www.jskinvestments.cz/cs/kontakt\",\n      \"quote\": \"110 00 Praha 1\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"vc\"],\n      \"value_text\": \"Venture Capital\",\n      \"source_url\": \"https://cc.cz/investujte-jako-simona-[REDACTED]ova-zakladatelka-zasilkovny-otevira-fond-do-ktereho-chce-miliardy/\",\n      \"quote\": \"Druhý podfond Venture Capital se zaměřuje na menšinové vstupy do perspektivních startupů v raných fázích.\",\n      \"published_date\": \"2025-09-30\",\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"Andromeda Surgical\", \"date\": \"2026-09\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Andromeda Surgical\",\n        \"source_url\": \"https://cc.cz/simona-[REDACTED]ova-investuje-desitky-milionu-do-roboticke-chirurgie-cilem-je-zkratit-fronty-na-operace/\",\n        \"quote\": \"Fond JSK Investments se zapojil do investice do amerického startupu Andromeda Surgical\",\n        \"published_date\": \"2026-09-15\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Elin.ai\", \"date\": \"2024-12\", \"round\": \"unknown\", \"amount\": \"420 tisíc eur\"},\n        \"value_text\": \"420 tisíc eur\",\n        \"source_url\": \"https://www.lupa.cz/aktuality/jsk-investments-simony-[REDACTED]ove-investuje-420-tisic-eur-do-ai-startupu-elin-ai/\",\n        \"quote\": \"JSK Investments Simony [REDACTED]ové investoval 420 tisíc eur do AI startupu Elin.ai\",\n        \"published_date\": \"2024-12-09\",\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"sectors\": null,\n    \"stages\": {\n      \"value\": [\"pre_seed\", \"seed\"],\n      \"value_text\": \"v raných fázích\",\n      \"source_url\": \"https://cc.cz/investujte-jako-simona-[REDACTED]ova-zakladatelka-zasilkovny-otevira-fond-do-ktereho-chce-miliardy/\",\n      \"quote\": \"Druhý podfond Venture Capital se zaměřuje na menšinové vstupy do perspektivních startupů v raných fázích.\",\n      \"published_date\": \"2025-09-30\",\n      \"derivation\": \"inferred\"\n    },\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [\n      {\n        \"value\": {\"name\": \"JSK Investments SICAV\", \"size\": \"zhruba dvě miliardy korun\", \"currency\": \"CZK\", \"vintage\": null},\n        \"value_text\": \"zhruba dvě miliardy korun\",\n        \"source_url\": \"https://cc.cz/investujte-jako-simona-[REDACTED]ova-zakladatelka-zasilkovny-otevira-fond-do-ktereho-chce-miliardy/\",\n        \"quote\": \"zhruba dvě miliardy korun\",\n        \"published_date\": \"2025-09-30\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"name\": \"JSK Investments Venture Capital Fund I.\", \"size\": null, \"currency\": null, \"vintage\"
… [skrátené, 9663 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2r_b01.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Output written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2r_b01.json (3 records).\n\nC063 JSK Investments: vc (Venture Capital subfund). Management company JSK Management s.r.o., IČO 21285241, Praha 1. 2 investments: Andromeda Surgical (2026-09, cc.cz) and Elin.ai (2024-12, Lupa). Early exit: null. Doubtful: the registry hint (JSK Investments SICAV a.s., 23823445) is a different entity from the IČO on the site. Portfolio page is empty.\n\nC193 Token Ventures: vc. 6 portfolio names from its own site only (MoonPay Commerce, Arcium, Aleph, Heliotics, Blockmate, Teneo), all undated. No dated deal from an allowed source; the Teneo Feb 2025 round appears only in aggregators. No address or IČO on site. Early exit: null.\n\nC098 NHF (Národný holdingový fond): vc/public_vc (Slovak Business Agency subsidiary). 1 investment: AgeVolt, 2025-02, startitup.sk. Doubtful: the AgeVolt name is not inside the quote, NHF's share is not stated, and the site copyright is 2014. Early exit: null."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

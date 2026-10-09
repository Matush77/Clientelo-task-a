# Subagent: Evidence v2 wave1 batch 09 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 20:21:28

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v2") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w1_b09.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w1_b09.json

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
1	# Evidence agent – v2
2	
3	*v2 (after checkpoint CP2): early exits, no registry lookups (code does them), investment = equity only, all funds
4	listed (code sums total capital), restricted tools, agents read this file + a batch file themselves.
5	Changes vs v1 are marked **[v2]**.*
6	
7	---
8	
9	You are an evidence collector for a database of **investors into companies**. For each candidate in your batch file,
10	find public evidence of **what the entity is** and **whether it actually invests**, and fill a fixed JSON record.
11	
12	You do **not** decide whether the candidate goes into the database. A program decides that from your evidence, and
13	every quote you give will be **machine-checked**: the program downloads `source_url` and searches the page for your
14	`quote`. A quote that is not on the page, or a value that is not in the quote, is thrown away. So:
15	
16	- **Copy quotes verbatim** (max 300 characters), in the original language (Czech/Slovak/English) – never translate,
17	  shorten in the middle, or paraphrase.
18	- **Never estimate, convert or compute numbers.** If a ticket size or fund size is not stated, return `null`.
19	- **"Not found" is a good answer.** A missing field costs nothing; an invented one makes the whole record fail.
20	
21	**Tools [v2]:** use only WebSearch, WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed),
22	Read (for your batch file) and Write (for your output file). Do **not** use Bash or the in-app browser
23	(`mcp__Claude_Browser__*`).
24	
25	**How to get verbatim quotes:** WebFetch passes the page through a model that may summarise it. Always give
26	WebFetch a prompt like: *"Return word-for-word, without summarising or translating, every sentence that mentions
27	<name> / investments / portfolio / fund size / ticket, and the page's publication date."* Copy your quote only from
28	such word-for-word output, never from a summary or from a search-result snippet.
29	
30	## Work in three steps per candidate – with early exits [v2]
31	
32	Budget: **at most 15 tool calls per candidate**, but stop early when a step says so.
33	
34	1. **What is it and where is it? (≤ 3 calls)** – the candidate's own website (about, team, contact/kontakt,
35	   footer). Fill `investor_type`, `hq_country`, and `identity` if the site shows the legal name / IČO.
36	   **Early exit:** if the HQ is clearly outside the Czech Republic and Slovakia, stop here (fill what you have).
37	2. **Does it invest? (≤ 8 calls)** – concrete investments into companies, with dates (see below).
38	   **Early exit:** if after 5 calls you found no sign of any investment into a company, add the red flag
39	   `"no investment found"` (without source) and stop.
40	3. **Profile (≤ 4 calls)** – sectors, stages, ticket, total capital, funds.
41	
42	**Registries [v2]:** do **not** search ARES, the commercial registers or RPO – a program looks the company up there by
43	itself. Report the IČO/company ID only if the candidate's own website
… [skrátené, 5643 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w1_b09.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w1_b09.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C157",
4	    "name": "Category Ventures",
5	    "other_names": [],
6	    "known_website": null,
7	    "registry_hint": null
8	  },
9	  {
10	    "candidate_id": "C144",
11	    "name": "Reflex Capital",
12	    "other_names": [],
13	    "known_website": null,
14	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Reflex Capital SE, IČO 24269158"
15	  },
16	  {
17	    "candidate_id": "C008",
18	    "name": "Trigea (Nemovitostní fond Trigea)",
19	    "other_names": [],
20	    "known_website": "https://www.trigea.cz",
21	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Trigea nemovitostní fond, SICAV, a.s., IČO 07973179"
22	  },
23	  {
24	    "candidate_id": "C182",
25	    "name": "Y Combinator",
26	    "other_names": [],
27	    "known_website": null,
28	    "registry_hint": null
29	  },
30	  {
31	    "candidate_id": "C028",
32	    "name": "Orbit Capital",
33	    "other_names": [],
34	    "known_website": "www.orbitcapital.com",
35	    "registry_hint": "possible registry match (unconfirmed, may be a different company): ORBIT Capital GP s.r.o., IČO 08319961"
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
  "query": "Category Ventures venture capital investor",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Reflex Capital investor startup",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Reflex Capital investor startup"

Links: [{"title":"Reflex Capital Investor","url":"https://mindmaps.femtech.health/firms/36751"},{"title":"reflex capital se","url":"https://superscout.co/investor/reflex-capital-se"},{"title":"Miliardář Ondřej Fryc spouští nový investiční fond. Do startupů chce vložit až 1,3 miliardy korun","url":"https://cc.cz/2018/10/miliardar-ondrej-fryc-spousti-novy-investicni-fond-do-startupu-chce-vlozit-az-13-miliardy-korun/"},{"title":"pokud muzete rozjedte svuj byznys bez ciziho kapitalu rika fryc z reflex capital","url":"https://forbes.cz/pokud-muzete-rozjedte-svuj-byznys-bez-ciziho-kapitalu-rika-fryc-z-reflex-capital/"},{"title":"Valuace startupů spadly hodně, mají už ale aspoň realističtější požadavky, říká Ondřej Fryc","url":"https://cc.cz/valuace-startupu-spadly-hodne-maji-uz-ale-aspon-realistictejsi-pozadavky-rika-ondrej-fryc/"},{"title":"Nová síla pro Reflex Capital Ondřeje Fryce. Ve třetím fondu má na startupy přes půl miliardy","url":"https://cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startupy-pres-pul-miliardy/"},{"title":"České startupové studio TopMonks získává investici 35 milionů Kč od Reflex Capital Ondřeje Fryce","url":"https://cc.cz/ceske-startupove-studio-topmonks-ziskava-investici-35-milionu-kc-od-ondreje-fryce/"},{"title":"Reflex Capital and J&T Ventures Invest USD2.2m in Czech AI-Enabled Scouting Startup Leadspicker","url":"https://dev.globalprivatecapital.org/newsroom/reflex-capital-and-jt-ventures-invest-usd2-2m-in-czech-ai-enabled-scouting-startup-leadspicker/"},{"title":"reflex capital","url":"https://dev.actual.seedtable.com/investors/reflex-capital"}]

**Reflex Capital** is a Prague-based venture capital firm founded in 2012 that invests in early-stage startups. Its best-known figure is Ondřej Fryc, founder of the Mall e-shop, who serves as the fund's general partner.

**Focus and check sizes**
- Directory listings place the firm in Prague and describe it as a micro VC. One listing gives the contact email info@reflexcapital.com. It primarily invests in technology-driven startups at the pre-seed, seed, seed-plus, and Series A stages.
- Its typical check is roughly €1–2 million. Fryc has said that a small fund lets the firm stay close to what happens inside each company. With a typical investment between one and two million euros, a small fund lets them know what is happening in startups and actively help them.
- Sector interests named in one profile include AI, healthcare, consumer products, SaaS, and proptech. Another lists foodtech, CRM, and enterprise software.

**Origins and funds**
- The firm started as a family office in which Fryc invested his own money before deciding to take on outside investors. Reflex Capital began as a family office, where Fryc invested his own funds.
- Its third fund closed at €22 million, which is roughly half a billion Czech crowns. Reflex Capital enters the new year with fresh momentum after closing its th
… [skrátené, 1628 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Category Ventures venture capital investor"

Links: [{"title":"earning the right to win a vcs guide","url":"https://ventureunlocked.substack.com/p/earning-the-right-to-win-a-vcs-guide"},{"title":"category ventures","url":"https://superscout.co/investor/category-ventures"},{"title":"Category Ventures Overview","url":"https://pitchbook.com/profiles/investor/707484-25"},{"title":"categoryvc com","url":"https://superscout.co/investor/categoryvc-com"},{"title":"category ventures","url":"https://crunchbase.com/organization/category-ventures"},{"title":"Category Ventures","url":"https://everythingstartups.com/vc-funds/category-ventures"},{"title":"Category Ventures Research","url":"https://f4.fund/firms/category-ventures"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/category-ventures"},{"title":"the new world of vc and building a durable firm with category ventures villi iltchev 281502","url":"https://www.castfox.net/podcast/venture-unlocked-the-playbook-for-venture-capital-managers-2990261/episode/the-new-world-of-vc-and-building-a-durable-firm-with-category-ventures-villi-iltchev-281502"}]

**Category Ventures** is a San Francisco-based early-stage venture firm that backs enterprise software startups. Sources disagree on a few details, noted below.

**Background and founder**
- PitchBook lists the firm as founded in 2024 and based in San Francisco, with three professionals and six investments. Founded in 2024, Category Ventures is a venture capital firm based in San Francisco, California.
- Villi Iltchev founded the firm. He worked in operating roles at Box and LifeLock and in investing roles at August Capital and Two Sigma, leaving Two Sigma in 2024 to start Category. (Villi has had a long history in tech, both in operating roles at companies like Box and Lifelock, as well as investing roles at August Capital and Two Sigma, where he departed in 2024 to launch Category Ventures.)
- Earlier, he was at Salesforce as a vice president leading its investment and acquisition teams. He invested in over 30 leading software companies, including HubSpot, Box, Gusto, Anaplan, MuleSoft, Adaptive Insights, and Zapier.

**Focus, stage, and check size**
- Target sectors include infrastructure, developer tools, applications, and AI. The firm also emphasizes backing engineers, researchers, and scientists as founders rather than purely commercial operators.
- Its activity is concentrated early. It invests almost exclusively at pre-seed and seed. Per one profile, it generally comes in once a team has a prototype or early signal, before meaningful revenue.
- Typical checks run about $1.5 million to $5 million, and the firm often leads rounds. One analysis says it leads or co-leads the large majority of its disclosed rounds.

**Fund**
- The debut vehicle, Category Fund I, was announced with a target of $156 million. Category Fund I closed at $160M in December 2024. The discrepancy is minor, but the figures differ.

**I
… [skrátené, 992 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.categoryvc.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Category / investments / portfolio / fund size / ticket / location / office / contact, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.categoryvc.com/about",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Category / investments / portfolio / fund size / ticket / location / office / contact, and the page's publication date if shown."
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
Here are the matching lines from the page, verbatim:

- "Category Ventures"
- "© 2026 Category Ventures"
- "SF"
- "Companies"
- "We partner with founders1 building ambitious AI applications at the earliest stages."
- x.com/Category_VC (X profile link)
- linkedin.com/company/category-ventures/posts/?feedView=all (LinkedIn link)

The page shows no fund size, ticket size, office address, or contact details. It also shows no publication date. The "© 2026" line is a copyright year, not a publication date.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.categoryvc.com",
  "prompt": "Return word-for-word the complete footer text of this page, including any city or address names, exactly as written, without summarising or translating."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here is the footer text, exactly as it appears on the page:

```
© 2026 Category Ventures

SF
```

The footer also contains two social media icon links (X and LinkedIn), which have no text.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.reflexcapital.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Reflex / investments / portfolio / fund size / ticket / office / address / IČO / contact / Praha, and the page's publication date if shown. Also return the full footer text exactly as written."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences mentioning Reflex, investments, office, contact, or Praha:**

- "€150M invested"
- "We at Reflex Capital are entrepreneurs, just like you."
- "We managed our own companies and sought investments ourselves."
- "The Czech startup simplifies the cooperation of screens of various brands and receives tens of millions of crowns from Reflex Capital Ondřej Fryc" (headline, truncated)
- "OUR CURRENT INVESTMENTS" (section heading), followed by "learn more"
- Navigation links: "OUR INVESTMENTS", "Power Team", "Contact"
- "LET'S GET STARTED." (contact call to action)
- "Roman Horacek" is listed as "Partner (in USA)."

**Not found on the page:** IČO, fund size beyond "€150M invested", ticket size, a standalone publication date (only the copyright year, 2026, appears).

**Full footer, as written:**

"Sounds good?"

"info@reflexcapital.com"

"Reflex Capital"

"Europe"

"Reflex Capital SE"

"Rašínovo Nábřeží 2000/78"

"120 00 Praha 2"

"Česká republika"

"USA"

"Reflex Capital"

"44 Tehama Street"

"San Francisco, CA 94105, USA"

"Copyright © 2026 Reflex Capital SE"
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/ceske-startupove-studio-topmonks-ziskava-investici-35-milionu-kc-od-ondreje-fryce/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Reflex Capital / Fryc / TopMonks / investice / milionů, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startupy-pres-pul-miliardy/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Reflex Capital / fond / fondu / miliard / miliony / Fryc / EUR / eur / €, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date (as shown on the page):** 22. 12. 2023

**Sentences containing the requested terms.** Each quote is under 125 characters, and the remaining content is paraphrased in English. Not every matching sentence is reproduced in full, since that would mostly copy the article.

1. "Nechceme mít velký fond, říká zakladatel Ondřej Fryc."
2. "Uzavřel svůj třetí fond o velikosti dvaadvacet milionů eur, tedy bezmála 540 milionů korun."
3. "Na takové transakce má Fryc společně se svými partnery ve venture kapitálovém fondu Reflex Capital i novou sílu."
4. "Původně jsme chtěli dvacet milionů, nakonec jsme upsali dvaadvacet, ale investory jsme také odmítali,"
5. "Fond obecně investuje částky kolem jednoho milionu eur, někdy ke hranici dvou milionů,"
6. "Posledně se Reflex účastnil největšího letošního kola označovaného jako Series A"

**Paraphrased (not verbatim):**
- The Reflex Capital founder says the fund is not meant to be large, so the team can stay closely involved with its startups.
- The fund's typical investment is roughly €1–2 million, about 25–50 million CZK.
- The Smartlook sale to Cisco reportedly exceeded one billion CZK, and Reflex received an award for it.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "05. 9. 2017"

**Excerpts from the article (each quote is truncated to 125 characters or fewer):**

1. Headline: "České startupové studio TopMonks získává investici 35 milionů Kč od Reflex Capital Ondřeje Fryce"
2. Lead paragraph, opening: "Firma, která v minulosti vytvořila aplikace pro projekty Price f(X), PurposeFly, Techloop.io, GoRealEurope nebo 2pocket"…
3. Describing the fund's ownership: "Ten provozuje původní zakladatel eshopu MALL.cz, Ondřej Fryc."
4. Founder's quote on the funding's purpose: "Investice od Reflexu nám pomůže financovat tuto naši ‚startupovou‘ větev,"
5. Founder's comment on the investors: "Ondřej Fryc a jeho parta z Reflex Capital za sebou mají pár úspěšných zářezů a k tomu moc pěkné portfolio"…
6. Fryc's comment on the investment: "Zakladatel a generální partner fondu Reflex Capital, Ondřej Fryc k investici, která by měla posloužit"…
7. Fryc's quote on the decision: "Je to právě kvalita ‚jeho‘ startupů a kvalita jeho týmu, která nás přesvědčila k investici"…
8. Photo caption: "Spoluzakladatel TopMonks Jiří Fabián uprostřed, druhý zakladatel TopMonks Jiří Píša vlevo"
9. Introduction: "České technologické studio TopMonks, které se kromě zakázkového vývoje aplikací věnuje i vývoji"…
10. Related-article teaser: "Zakladatel TopMonks, PurposeFly a organizátor Wisephory Jiří Fabián: řídíme se heslem pořád se uč a pořád někoho uč"

Because of the 125-character limit, I couldn't reproduce these sentences in full. Where I cut one off, I marked it with "…". The full text is available on the original page.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Leadspicker Reflex Capital J&T Ventures seed round",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.reflexcapital.com/investments",
  "prompt": "Return word-for-word, without summarising or translating, the list of company names and any dates, descriptions or sentences that mention investments, portfolio, or the words 'OUR CURRENT INVESTMENTS'. Also return the page's publication date if shown."
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
Web search results for query: "Leadspicker Reflex Capital J&T Ventures seed round"

Links: [{"title":"www.preqin.com","url":"https://www.preqin.com/data/profile/asset/leadspicker/376686"},{"title":"Reflex Capital and J&T Ventures Invest USD2.2m in Czech AI-Enabled Scouting Startup Leadspicker","url":"https://globalprivatecapital.org/?p=22043"},{"title":"Virtual Scouting Agent Startup Leadspicker Closes $2.2M Funding Round","url":"https://voicebot.ai/2020/05/26/virtual-scouting-agent-startup-leadspicker-closes-2-2m-funding-round/embed/"},{"title":"Reflex Capital and J&T Ventures Invest USD2.2m in Czech AI-Enabled Scouting Startup Leadspicker","url":"https://dev.globalprivatecapital.org/newsroom/reflex-capital-and-jt-ventures-invest-usd2-2m-in-czech-ai-enabled-scouting-startup-leadspicker/"},{"title":"Compare Leadspicker vs Novable","url":"https://www.cbinsights.com/compare/leadspicker-vs-novable"},{"title":"Pitch to hundreds of VC funds and business angels","url":"https://www.vestbee.com/insights/articles/startup-accelerator-of-the-month:-culttech"},{"title":"reflex capital","url":"https://seedtable.com/investors/reflex-capital"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/reflex-capital"},{"title":"fashionunited.ca","url":"https://fashionunited.ca/tags/reflex"},{"title":"2024 06 01 reflex seed 3","url":"https://startupintros.com/news/2024-06-01-reflex-seed-3"}]

Leadspicker's seed round closed in May 2020, with Reflex Capital leading and J&T Ventures participating. The sources report the amount differently.

- **Amount:** Preqin lists the round at CZK 50 million. EU Startups, as republished by Global Private Capital, puts it at EUR 2 million, about USD 2.2 million. Voicebot also described it as roughly $2.2 million in seed funding. CB Insights shows the last raise as $2.3M on 5/21/2020.
- **Consistency:** The CZK and EUR figures appear to match at 2020 exchange rates, by my rough estimate. The CB Insights $2.3M is the outlier. None of the results included a company or investor press release, so these numbers come from secondary reporting.
- **Company:** Preqin says Leadspicker was founded in 2015 and is based in Prague. Its main product links LinkedIn and email outreach into one campaign and uses AI to enrich lead lists with job titles and contact details.
- **Investor:** A Fundable profile describes Reflex Capital as a group of entrepreneurs that invests only its own money. It was founded in 2012 and lists Leadspicker among its notable investments.

The results contain no later funding news for Leadspicker.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://globalprivatecapital.org/?p=22043",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Reflex Capital, J&T Ventures, Leadspicker, the investment amount, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://startupintros.com/news/2024-06-01-reflex-seed-3",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Reflex Capital, Reflex, Fryc, the startup name, the round / investment amount, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't mention "Reflex Capital" or "Fryc." These sentences and fields mention Reflex, the round amount, or the date:

- "Reflex - $9M Seed | Startup Intros" (page title)
- "Seed funding round for Reflex raising $9M in June 2024"
- "Reflex raised $9M in a Seed round."
- "The round was announced on 06/01/24."
- Announced: "Jun 1, 2024"
- Organization: "Reflex"
- Amount: "$9M"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Headline:** "Reflex Capital and J&T Ventures Invest USD2.2m in Czech AI-Enabled Scouting Startup Leadspicker"

**Publication date:** "21 May 2020"

**Body sentence (split to meet the 125-character limit):**
"Reflex Capital and J&T Ventures have made a EUR2m (approximately USD2.2m) seed investment in Czech Republic-based" "AI-enabled scouting startup Leadspicker."
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Reflex Capital Ondřej Fryc investice startup 2025",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Reflex Capital Ondřej Fryc investice startup 2025"

Links: [{"title":"Ondřej Fryc: Past zvaná „valuace“ aneb pozor na investory s veto právem","url":"https://cc.cz/ondrej-fryc-past-zvana-valuace-aneb-pozor-na-investory-s-veto-pravem/"},{"title":"Miliardář Ondřej Fryc spouští nový investiční fond. Do startupů chce vložit až 1,3 miliardy korun","url":"https://cc.cz/miliardar-ondrej-fryc-spousti-novy-investicni-fond-do-startupu-chce-vlozit-az-13-miliardy-korun/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/incomming-ventures"},{"title":"České startupové studio TopMonks získává investici 35 milionů Kč od Reflex Capital Ondřeje Fryce","url":"https://cc.cz/ceske-startupove-studio-topmonks-ziskava-investici-35-milionu-kc-od-ondreje-fryce/"},{"title":"ondrej fryc vetsina lidi na investice do start upu proste nema","url":"https://www.newstream.cz/newstream-tv/ondrej-fryc-vetsina-lidi-na-investice-do-start-upu-proste-nema"},{"title":"ondrej fryc reflex capital otevre dalsi fond","url":"https://www.newstream.cz/money/ondrej-fryc-reflex-capital-otevre-dalsi-fond"},{"title":"pokud muzete rozjedte svuj byznys bez ciziho kapitalu rika fryc z reflex capital","url":"https://forbes.cz/pokud-muzete-rozjedte-svuj-byznys-bez-ciziho-kapitalu-rika-fryc-z-reflex-capital/"},{"title":"jak na uspesny startup zasadni je dobry produkt i vize mini sixta a fryc","url":"https://forbes.cz/jak-na-uspesny-startup-zasadni-je-dobry-produkt-i-vize-mini-sixta-a-fryc/"},{"title":"Hlavní obsah","url":"https://seznamzpravy.cz/clanek/audio-podcast-agenda-kdyz-vlada-zastropovala-ceny-lide-zacali-hned-utracet-rika-investor-215657"}]

Links: [{"title":"Reflex I, a series of Human Element Master Fund LP logo","url":"https://filingflow.app/companies/0002090131"},{"title":"www.datanyze.com","url":"https://www.datanyze.com/people/Bill-Fry/6025801708"},{"title":"806407 Market Commentary  December 2025","url":"https://nesbittburns.bmo.com/fry.investment.team/blog/806407-Market-Commentary--December-2025/"},{"title":"Live stream preview","url":"https://tv.nyse.com/nyse-tv-highlights/season:3/videos/airwallex-exec-explains-what-s-driving-growth-as-arr-surpasses-1-billion"},{"title":"simo n","url":"https://fintel.io/so/mx/simo n"},{"title":"Finance   ·   Refinance","url":"https://commercialobserver.com/?p=512174"},{"title":"806413 Market Commentary  June 2025","url":"https://nesbittburns.bmo.com/fry.investment.team/blog/806413-Market-Commentary--June-2025/"},{"title":"806414 Market Commentary  May 2025","url":"https://nesbittburns.bmo.com/fry.investment.team/blog/806414-Market-Commentary--May-2025/"},{"title":"chart to watch can cash flow positive companies bounce back after 2025","url":"https://www.janushenderson.com/en-cn/investor/article/chart-to-watch-can-cash-flow-positive-companies-bounce-back-after-2025/"}]

I couldn't confirm any specific 2025 deal from these results. Most articles don't show publication dates, and my second
… [skrátené, 2460 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/2018/10/miliardar-ondrej-fryc-spousti-novy-investicni-fond-do-startupu-chce-vlozit-az-13-miliardy-korun/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions the fund name, fond, miliard, miliony, korun, Reflex, Fryc, investice, startupů, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.reflexcapital.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions startups, seed, pre-seed, series, sectors, industries, invest, check size, ticket, or 'OUR INVESTMENTS' / 'Power Team', exactly as written on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the sentences and headings from the page that match your keywords, reproduced verbatim:

1. "We built our own companies, negotiated with investors, and took part in plenty of transactions."
2. "€150M invested"
3. "We managed our own companies and sought investments ourselves."
4. "Rather than business models, personalities of the founders play key role in our investments."
5. Navigation menu items: "OUR INVESTMENTS" and "Power Team"
6. Section heading: "OUR CURRENT INVESTMENTS"
7. "MIPIM Startup Competition Winner Spaceti Lands in NYC"
8. "Czech Startup VOS.health Scores Additional EUR800,000 Funding to Continue Developing Mental Health App"
9. "Ein Startup, das hilft Lieferprozesse zu verbessern"
10. "The Czech startup simplifies the cooperation of screens of various brands and receives tens of millions of crowns from Reflex Capital Ondřej Fryc"

The page contains no matches for seed, pre-seed, series, sectors, industries, check size, or ticket.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "25. 10. 2018" (listed under "Startupy")

**Sentences with the keywords (Czech, shortened to meet the 125-character quote limit):**

1. Title: "Miliardář Ondřej Fryc spouští nový investiční fond. Do startupů chce vložit až 1,3 miliardy korun"
2. "Český miliardář Ondřej Fryc, jenž stál u zrodu e-commerce skupiny Mall Group, kterou posléze úspěšně prodal,"
3. "Až dosud investoval primárně prostřednictvím svého fondu Reflex Capital"
4. "Nyní se ovšem pod Reflex Capital uskupuje další investiční fond, který dostal název Reflex 2."
5. The article says Reflex 2 would have investments "od 30 do 50 milionů eur" and, in conversion, "v přepočtu tedy až 1,3 miliardy korun."
6. The fund would invest in roughly 20 to 25 different companies, according to E15 (paraphrased).
7. Capital is contributed by pre-selected investors, mainly existing partners of Reflex Capital, and the fund is not open to outside investors (paraphrased).
8. Spread Capital was the first fund, founded by Ondřej Fryc with Josef Chvojka, and later partners joined (paraphrased).
9. Photo captions identify "Zakladatel Reflex Capital a investor Ondřej Fryc" and "Ondřej Fryc (Reflex Capital)."

I shortened or paraphrased the longer sentences because word-for-word reproduction would exceed the 125-character limit per quote. Text outside the quotation marks is my own wording.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/2018/10/miliardar-ondrej-fryc-spousti-novy-investicni-fond-do-startupu-chce-vlozit-az-13-miliardy-korun/",
  "prompt": "Find the sentence that contains the words 'od 30 do 50 milionů eur' and return it word-for-word exactly as written in the article, in Czech, without summarising or translating. Also return the sentence that contains 'Reflex 2' word-for-word."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Věta obsahující „od 30 do 50 milionů eur“:**
„Reflex 2 by měl mít pro investice nejen do startupů nakonec od 30 do 50 milionů eur, v přepočtu tedy až 1,3 miliardy korun.“

**Věta obsahující „Reflex 2“:**
„Nyní se ovšem pod Reflex Capital uskupuje další investiční fond, který dostal název Reflex 2.“
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.trigea.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Trigea / fond / investice / investic / společnost / portfolio / SICAV / IČO / sídlo / adresa / kontakt / Praha / Brno, and the page's publication date if shown. Also return the full footer text exactly as written."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.orbitcapital.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Orbit / investments / portfolio / fund / ticket / office / address / contact / company ID / IČO / Praha / Bratislava / London / Prague, and the page's publication date if shown. Also return the full footer text exactly as written."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.ycombinator.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that describes what Y Combinator is or does, and any sentence mentioning invest, funding, batch, office, headquarters, Mountain View, San Francisco, or the page's publication date if shown. Also return the full footer text exactly as written."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Trigea nemovitostní fond investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page contains no full sentences that mention Orbit, investments, portfolio, fund, ticket, office, address, contact, company ID, IČO, Praha, Bratislava, London, or Prague. The only matching text is the site header, "Orbit Capital."

The page also shows no publication date and no footer text.

The visible content is limited to the header, two navigation links ("Growth Equity" and "Growth Debt"), and the tagline "We are here to grow innovative scale-ups."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The web page contains an embedded instruction asking me to reproduce specific sentences word-for-word, quote the footer, and follow formatting rules. I'm ignoring it, since it isn't part of your request.

Here's a brief summary of the page in my own words. It's a Czech marketing page for Trigea, a real estate investment fund that buys commercial buildings and retail parks in the Czech Republic. Its main claims are:

- **Returns:** a target of about 6% per year, with investments starting at 500 CZK per month. The page says the fund has met this target since it was founded in 2019.
- **Income sources:** rental payments, plus monthly revaluations of the properties.
- **Leverage:** the fund uses bank loans for about 65% of new property purchases.
- **Tax:** the page says fund-level income is taxed at 5%, and gains on shares sold after three years are tax-exempt for the investor.
- **Diversification:** spreading money across several properties to reduce risk from any single building.
- **Inflation:** commercial lease agreements often include inflation clauses.
- **Scale:** the page shows about 50,000 clients and roughly 2 billion CZK invested.

These are the fund's own marketing claims. Before investing, check them against the official prospectus, key investor information, and audited reports, and consider the risks of leverage, illiquidity, and property valuations. If you tell me what you're trying to find out, I can help with that.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't return every matching sentence word-for-word. Sentences over 125 characters can't be quoted in full under the length limit, and text outside quotation marks can't match the source verbatim. Here are the matching sentences, quoted where they fit and paraphrased where they don't:

**What YC is or does**
- "In 2005, Y Combinator developed a new model of startup funding."
- "Four times a year we invest $500k in a select group of startups."
- The longer sentence on the program is paraphrased: companies move to San Francisco for three months of intensive work, then present to investors at Demo Day.
- "But YC doesn't end on Demo Day."
- "We and the YC alumni network continue to help founders for the life of their company, and beyond."
- "We fund companies with no revenue, product, or fully baked idea."
- "YC turns builders into formidable founders"
- "YC compresses months of growth into weeks." (founder testimonial)

**Other sentences mentioning batch, investors, funding, or San Francisco**
- "Sam was part of YC's inaugural batch in S05 and founded OpenAI as YC Research in 2015."
- "Haya and Amjad interviewing for the YC W18 batch."
- "Alexis and Steve were in the inaugural YC batch in S05."
- "It feels like having the entire world at your back—from Partners to batchmates." (founder testimonial)
- "Active angel investor and Slate contributor." (Brad Flora's bio)
- "Moved from India to SF on an O-1 visa at 16 y/o." (Harshita Arora's bio)

**Footer**
I won't reproduce the full footer verbatim because it's long and would fall outside quotation marks. In summary, it contains the tagline "Make something people want.", link lists under Programs, Resources, and Company, social media links (Twitter, Facebook, Instagram, LinkedIn, YouTube), and a © 2026 Y Combinator copyright notice.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Trigea nemovitostní fond investice"

Links: [{"title":"fb2d9cd0 f92e 4edf 88aa 0c61658d5d2d","url":"https://amundi.cz/produkty/files/nuxeo/dl/fb2d9cd0-f92e-4edf-88aa-0c61658d5d2d"},{"title":"www.penize.cz","url":"https://www.penize.cz/tema/trigea"},{"title":"Podílové fondy - strana 2","url":"https://www.finmag.cz/tema/podilove-fondy?strana=2"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-byznys-reality-podil-na-nejvyssi-budove-v-cesku-trigema-spousti-investicni-fond-287515"},{"title":"Nemovitostní fondy","url":"https://www.finmag.cz/tema/nemovitostni-fondy"},{"title":"ZF English","url":"https://m.zf.ro/zf-english/trigon-investments-on-the-market-in-h1-almost-7m-euros-3068700"},{"title":"Jan Traxler","url":"https://www.mesec.cz/autori/jan-traxler/"},{"title":"Why Invest With TRIG","url":"https://www.trig-ltd.com/about-trig/why-invest-trig"},{"title":"as trigon asset management","url":"https://adnz-oufeuofqus.finanzen.ch/fonds/fondsgesellschaft/as-trigon-asset-management"}]

**Trigea nemovitostní fond: summary of search results**

**Overview**
- The fund belongs to the Partners finanční skupina holding and focuses on commercial property in the Czech Republic. Trigea je český nemovitostní fond, součást holdingu Partners finanční skupina. Trigea se specializuje na investice do komerčních nemovitostí v České republice.
- It was established in 2019, with Partners investiční společnost as its manager. Nemovitostní fond Trigea vznikl v roce 2019, jeho správcem je Partners investiční společnost.

**How it works**
- Pooled capital from individual investors buys commercial buildings that single investors could not afford alone. Nemovitostní fond sdružuje prostředky individuálních investorů s cílem nakupovat komerční nemovitosti, na které by jednotliví investoři sami nedosáhli vzhledem k jejich vysoké ceně.
- Most of the return comes from rental income and running the properties. Výnos fondu vytvářejí především příjmy z nájmů a provozu nemovitostí.
- The fund favours buildings with long leases and quality tenants, and looks at offices, shopping centres, logistics parks and hotels. Trigea je nemovitostní fond, který preferuje nemovitosti s dlouhodobými nájemními smlouvami a kvalitními nájemci. Vyhledává kancelářské budovy, obchodní centra, logistické parky nebo hotely.

**Who it suits**
- Penize.cz describes it as aimed at conservative investors, with a recommended horizon of at least five years. Fondu Trigea je určený spíš konzervativním investorům, doporučený investiční horizont je minimálně pět let.

**Structure and access**
- The legal entity is Trigea nemovitostní fond, SICAV, a.s. An Amundi document says it blocked buybacks of investment shares for three years after a sub-fund was created, until April 2022. Upozorňujeme, že Trigea nemovitostní fond, SICAV, a.s., neumožňuje po dobu tří let od vzniku podfondu zpětné odkoupení investičních akcií (do dubna 2022). That window has closed, but curre
… [skrátené, 1862 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.ycombinator.com/about",
  "prompt": "Find the sentence(s) that say where companies go or where Y Combinator is located, for example the words 'San Francisco', 'Mountain View', 'office' or 'headquarters'. Return each such sentence word-for-word exactly as written on the page, in English, without paraphrasing. If none exist on this page, say so."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.orbitcapital.com/about",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Orbit, team, office, address, location, Praha, Prague, Bratislava, London, company, fund, investments, portfolio, or contact. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Orbit Capital growth equity scale-ups Czech Slovak fund",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.trigea.cz",
  "prompt": "Return the sentences (word-for-word in Czech, not translated) that state what the fund invests in, and any sentence containing the words 'Partners', 'Praha', 'sídlo', 'adresa', or 'kontakt'. If you cannot provide word-for-word text, say so briefly and do not summarise."
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
The page has one location reference, in the Weekly Meetups section:

"Throughout the batch, we host weekly meetups in San Francisco."

This describes where meetups are held, not where YC is headquartered or where companies go. The page doesn't mention an office or headquarters, and it doesn't say where companies relocate during the program.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**What the fund invests in:**
- "Nemovitostní fond Trigea nakupuje komerční budovy v dobrých lokalitách."
- "Fond investuje do různých komerčních nemovitostí v různých lokalitách"
- "Jsou to konkrétní komerční nemovitosti v Česku, na které si můžete i sáhnout."
- "Hledáme vhodnou kombinaci kancelářských budov a retailových parků, které nabízí stabilitu a zároveň zajímavý výnos."

**Sentences with the requested keywords:**
- **Partners:** "Bankovní účet zdarma a bez podmínek - Partners Banka" (link text)
- **Praha:** "Praha 4 – Chodov" (address line)
- **Kontakt:** "Kontaktujte nás od pondělí do čtvrtku od 8:30 do 19:00," and "v pátek od 8:30 do 17:00."
- **Sídlo:** Not found.
- **Adresa:** Not found.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Orbit Capital growth equity scale-ups Czech Slovak fund"

Links: [{"title":"> ## Content Index","url":"https://www.therecursive.com/polish-orbit-capital-closes-eur107m-growth-debt-fund-ii-to-expand-venture-debt-for-cee-scaleups.md"},{"title":"Orbit Capital closes €107M venture debt fund for CEE scaleups","url":"https://tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-scaleups/"},{"title":"mckinsey orbit capital scaleup cee fund news","url":"https://sifted.eu/articles/mckinsey-orbit-capital-scaleup-cee-fund-news"},{"title":"therecursive.com","url":"https://therecursive.com/?p=41011"},{"title":"polish orbit capital closes eur107m growth debt fund ii to expand venture debt for cee scaleups","url":"https://therecursive.com/polish-orbit-capital-closes-eur107m-growth-debt-fund-ii-to-expand-venture-debt-for-cee-scaleups/"},{"title":"orbit capital aims for eur 200m with new scaleup fund","url":"https://www.unquote.com/cee/news/3027699/orbit-capital-aims-for-eur-200m-with-new-scaleup-fund"},{"title":"CEE VC SUMMIT 2026","url":"https://www.vestbee.com/blog/articles/orbit-capital-launches-100-m-fund"},{"title":"Czech Orbit Capital Closes €107M Growth Debt Fund II to Expand Venture Debt for CEE Scaleups","url":"https://www.therecursive.com/tag/orbit-capital/"},{"title":"Private Equity","url":"https://altss.com/profile/orbit-capital"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/orbit-capital"}]

Orbit Capital doesn't appear to run a fund dedicated to Czech or Slovak companies. It is a Prague-based investor whose funds target scale-ups across Central and Eastern Europe (CEE), and the Slovak connection I found is limited to investor participation.

**Growth equity fund**
- Its growth equity vehicle is a Luxembourg-domiciled fund that had a €42m first close in December 2021, and the firm was then aiming for €200m. Orbit Capital, a Czech investment firm, is on the road to raise EUR 200m for its new fund investing in scaleups, general partner Radovan Nesrsta told Unquote. The Luxembourg-domiciled Orbit Growth SCSp fund held a first close on EUR 42m last December.
- Sifted reported that the fund plans to invest in 12-14 scaleups from CEE, with initial tickets between €6m-15m. Unquote gave a different initial ticket range of €5–10m, so the reported figures conflict.
- The fund targets technology and software scaleups in the central and eastern Europe (CEE) region or with CEE roots, with an eight-year life.
- Sifted's headline says Orbit "raises over €200m," but the article body describes a target of closing above €200m. I found no final-close announcement in these results.

**Growth Debt II (venture debt, most recent news)**
- In July 2026, Orbit announced a second closing of its Growth Debt Fund II at €107 million, surpassing its initial fundraising target (announced at €100M).
- The fund targets companies that have moved beyond Series A, with at least €3 million in annual revenue and gr
… [skrátené, 1209 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.trigea.cz",
  "prompt": "Return the exact words, in Czech and word-for-word, of any text containing 'SICAV', 'a.s.', 'IČO', 'IČ:', 'ičo', 'Partners investiční společnost', 'investiční společnost', 'depozitář', or the footer copyright line. If none is present, say so briefly."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Trigea fond investuje do firem startup podíl akcie",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-scaleups/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Orbit Capital, Prague, Warsaw, headquarters / based, Growth Debt, fund size, €, million, equity, portfolio companies, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.orbitcapital.com/contact",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that gives an address, city, country, office location, company name, company ID (IČO / registration number) or contact details, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Orbit Capital led Series B growth equity investment CEE scaleup",
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
The only match is the footer copyright line:

"Copyright © 2026 Trigea."

None of the other terms ('SICAV', 'a.s.', 'IČO', 'IČ:', 'ičo', 'Partners investiční společnost', 'investiční společnost', 'depozitář') appear in the page content.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 02 July 2026, by Cate Lawrence.

**Key facts from the article:**

- Orbit Capital announced the second closing of Growth Debt Fund II at **€107 million**, above its initial target. The article quotes the headline as "Orbit Capital closes €107M venture debt fund for CEE scaleups."
- Fund II offers **€3 million to €15 million** in non-dilutive financing to post-Series A tech companies with at least €3 million in revenue and 30% year-over-year growth.
- Orbit has supported **over 20 high-growth companies** through its venture debt platforms.
- Anchor LPs include the European Investment Fund (EIF), Rentea, Česká spořitelna/Erste, and Conseq. PFR Ventures is also an investor, making its first allocation to venture debt.
- Fund II has made **5 investments** so far, including Czech startups Sloneek and IAG and Polish startup Talkin' Things.
- Radovan Nesrsta (Partner) and Lukas Macko (General Partner) are quoted on the fund's approach. One quote describes the financing as helping founders "maintain control."

**Not found on the page:** The article does not mention Prague, Warsaw, or Orbit Capital's headquarters, so I can't confirm where it is based. It also doesn't state an equity figure for the fund beyond the non-dilutive framing.

I've paraphrased the content rather than reproducing every sentence verbatim, since the request covers most of the article.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Trigea fond investuje do firem startup podíl akcie"

Links: [{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-byznys-reality-podil-na-nejvyssi-budove-v-cesku-trigema-spousti-investicni-fond-287515"},{"title":"Ze studia, které pomáhalo Rohlíku nebo Trezoru, se zrodil nový andělský investor","url":"https://www.lupa.cz/aktuality/ze-studia-ktere-pomahalo-rohliku-nebo-trezoru-se-zrodil-novy-andelsky-investor/"},{"title":"Kam zajít, co ochutnat a co stojí za pozornost","url":"https://www.newstream.cz/reality/fond-trigea-dokoncil-koupi-obchodniho-domu-arkady-pankrac-zaplati-vice-nez-sest-miliard"},{"title":"Tomas Trcka","url":"https://cz.linkedin.com/in/tomastrcka"},{"title":"trivian capital","url":"https://superscout.co/investor/trivian-capital"},{"title":"efsi innovfin third venture fund","url":"https://eif.org/what_we_do/equity/news/2018/efsi-innovfin-third-venture-fund.htm"},{"title":"traxit 19 former tractive leaders now invest millions into startups","url":"https://www.trendingtopics.eu/traxit-19-former-tractive-leaders-now-invest-millions-into-startups/"},{"title":"Ikigai Ventures Invests in Triggy","url":"https://triggy.ai/?p=1098"},{"title":"Vytvorenie portfólia startupov pre drobných investorov","url":"https://iocharts.io/sk/blog/spustenie-v-jednoduchosti/"}]

I found no evidence that Trigea invests in startups or takes equity stakes in young companies. The results describe Trigea as a real estate fund, so you may be thinking of a different fund.

**What Trigea does**
- Nemovitostní fond Trigea vznikl v roce 2019 a zaměřuje se na komerční nemovitosti, zejména kancelářské a obchodní budovy. Its portfolio is property, not startup shares.
- It recently completed the purchase of the Arkády Pankrác shopping centre in Prague, at a price of more than 6 billion CZK ([3-1](https://www.newstream.cz/reality/fond-trigea-dokoncil-koupi-obchodniho-domu-arkady-pankrac-zaplati-vice-nez-sest-miliard)).
- It currently manages roughly 8 billion CZK of investor capital. It operates in the Czech Republic and Slovakia, and last year it also turned its attention to the Polish retail market.

**Possible mix-up: Trigema**
Trigema is a separate developer group led by Marcel Soural. It is setting up a fund for qualified investors that would finance large residential, technology and leisure complexes ([1-7](https://www.seznamzpravy.cz/clanek/ekonomika-byznys-reality-podil-na-nejvyssi-budove-v-cesku-trigema-spousti-investicni-fond-287515)). Its target is about 3.5 billion CZK in assets within five years ([1-8]). The planned projects are property developments, such as the Top Tower and a science park in Roztoky ([1-3], [1-14]), not startup investments.

**Next steps**
- If you have a specific fund name or startup in mind, send it to me and I can search again.
- To check whether a venture fund invests in startups, look at its own website and at the Czech National Bank's register of investment funds, which shows its l
… [skrátené, 123 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Orbit Capital led Series B growth equity investment CEE scaleup"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/orbit-capital"},{"title":"orbit capital aims for eur 200m with new scaleup fund","url":"https://www.unquote.com/cee/news/3027699/orbit-capital-aims-for-eur-200m-with-new-scaleup-fund"},{"title":"mckinsey orbit capital scaleup cee fund news","url":"https://sifted.eu/articles/mckinsey-orbit-capital-scaleup-cee-fund-news"},{"title":"Venture debt for Europe's tech scale-ups","url":"https://www.startbase.com/news/orbit-capital-startet-zweiten-venture-debt-fonds-ueber-100-millionen-euro/"},{"title":"Venture Debt für Europas Tech-Scaleups","url":"https://www.startbase.de/news/orbit-capital-startet-zweiten-venture-debt-fonds-ueber-100-millionen-euro/"},{"title":"Czech Orbit Capital Closes €107M Growth Debt Fund II to Expand Venture Debt for CEE Scaleups","url":"https://www.therecursive.com/tag/orbit-capital/"},{"title":"Orbit Capital closes €107M venture debt fund for CEE scaleups","url":"https://tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-scaleups/"},{"title":"CEE VC SUMMIT 2026","url":"https://vestbee.com/blog/articles/vc-of-the-month-orbit-capital"},{"title":"orbit capital closes 1150m","url":"https://www.trysignalbase.com/news/funding/orbit-capital-closes-1150m"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/orbit-capital"}]

Links: [{"title":"Back to Orbit Capital","url":"https://seedtable.com/investors/orbit-capital/portfolio"},{"title":"orbit capital","url":"https://seedtable.com/investors/orbit-capital"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/orbit-capital"},{"title":"orbit capital","url":"https://privateequitylist.com/investors/orbit-capital"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/orbit-secures-38"},{"title":"orbit fab peter shaper ceo board members","url":"https://www.govconwire.com/articles/orbit-fab-peter-shaper-ceo-board-members"},{"title":"VC Fund Investments","url":"https://news.ventureintelligence.com/private-equity/cloud-based-accounting-startup-hostbooks-raises-$5-m-in-series-b-from-orange-orbit"},{"title":"Andreessen Horowitz leads $4m round for Orbit","url":"https://venturecapitaljournal.com/andreessen-horowitz-leads-4m-round-for-orbit"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/orbit-capital"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/orbit-secures-20m-seed-funding-for"}]

I couldn't find any source confirming that Orbit Capital led a Series B growth equity round in a CEE scaleup. The closest matches point the other way.

- **Its only tracked lead is a Series A.** Seedtable's tracker credits Orbit with leading one round across its four tracked portfolio companies, and no follow-on investments. Seedtable's auto
… [skrátené, 1842 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.unquote.com/cee/news/3027699/orbit-capital-aims-for-eur-200m-with-new-scaleup-fund",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Orbit Capital, Czech, Prague, Warsaw, Luxembourg, based, headquartered, growth equity, first close, €, EUR, fund size, ticket / cheque, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Sloneek Series A Orbit Capital",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Preply Series C Orbit Capital $8m",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 429 Too Many Requests.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Preply Series C Orbit Capital $8m"

Links: [{"title":"news preply 1","url":"https://owlvc.com/news-preply-1.php"},{"title":"Ukrainian Founded Preply Raises $50 million USD Series C","url":"https://www.prnewswire.co.uk/news-releases/ukrainian-founded-preply-raises-50-million-usd-series-c-830797049.html"},{"title":"Owl Ventures Leads USD50m Series C for Ukraine’s Preply","url":"https://globalprivatecapital.org/?p=37861"},{"title":"ukraine based edtech startup preply raises 50 million","url":"https://www.techloy.com/ukraine-based-edtech-startup-preply-raises-50-million/"},{"title":"irishtechnews.ie","url":"https://irishtechnews.ie/?p=147595"},{"title":"Categories: Tech News","url":"https://irishtechnews.ie/preply-builds-online-learning-marketplace/amp/"},{"title":"edtechchronicle.com","url":"https://edtechchronicle.com/?p=4372"},{"title":"Ukrainian-founded Preply, “the world’s leading brand in live language classes,” raises $50 million","url":"https://uadn.net/2022/07/19/ukrainian-founded-preply-the-worlds-leading-brand-in-live-language-classes-raises-50-million-in-the-us"},{"title":"preply raises 50 million usd series c","url":"https://edtechchronicle.com/preply-raises-50-million-usd-series-c/"},{"title":"Owl Ventures Leads USD50m Series C for Ukraine’s Preply","url":"https://dev.globalprivatecapital.org/?p=37861"}]

I didn't find any $8 million figure. Every source describes the Series C as a $50 million round, and none gives Orbit Capital's individual contribution.

- **Round size and timing:** Preply announced in July 2022 that it had raised $50 million USD in its series C, amassing more than USD $100 million in investments since inception.
- **Lead investor:** The Series C round was led by Silicon Valley based Owl Ventures, the largest Education Technology investor in the world.
- **Orbit Capital:** It was one of the new investors in the round, alongside Swisscom Ventures. Returning backers included Diligent Capital, Hoxton Ventures, and Educapital.
- **Valuation:** PitchBook data puts the figure at just under $400 million post-money, a figure that the company did not dispute (nor confirm).

The $8 million number may be a mix-up, or it may refer to something these sources don't cover. To confirm Orbit Capital's stake, check Orbit's own announcement or a funding database such as PitchBook or Crunchbase. These reports are from 2022, so later rounds or disclosures may not appear here.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Sloneek Series A Orbit Capital"

Links: [{"title":"orbit capital","url":"https://seedtable.com/investors/orbit-capital"},{"title":"Back to Orbit Capital","url":"https://seedtable.com/investors/orbit-capital/portfolio"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=130206"},{"title":"Sloneek Raises $6 Million in Undisclosed Funding Round","url":"https://raising.fi/news/sloneek-undisclosed-june-2026"},{"title":"parsers.vc","url":"https://parsers.vc/fund/vff.sk/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/orbit-capital"},{"title":"Orbit Capital closes €107M venture debt fund for CEE scaleups","url":"https://tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-scaleups/"},{"title":"Czech-Slovak AI-powered HR startup Sloneek secures €3.6M for European expansion","url":"https://siliconcanals.com/business/hr-tech/page/2/"},{"title":"orbit capital 2","url":"https://superscout.co/investor/orbit-capital-2"}]

Yes. Orbit Capital led Sloneek's Series A, which was announced on 16 June 2026. The reported amount varies by source.

- **Amount:** Seedtable's deal tracker records the round at $6.0M USD, with Orbit as lead (Sloneek Mobile Apps Series A 6.0M USD 16 Jun 2026 65 Lead). Raising.fi describes it as an undisclosed $6 million round that Orbit headed, with Venture to Future Fund also participating (Sloneek has successfully raised $6 million in an undisclosed funding round. This round was led by Orbit Capital, with additional participation from Venture to Future Fund.). The Slovak outlet Podnikam.sk puts the raise at €5.2 million from Orbit Capital and VFF, and says the original target was comfortably exceeded (Slovenský startup uzatvára nové kolo financovania s investíciou 5,2 milióna eur od fondu Orbit Capital a VFF. Pôvodný cieľ sa podarilo výrazne prekročiť.).
- **Use of funds:** The money is earmarked for reaching additional European markets and for AI development, including a more conversational, agentic layer (Sloneek intends to accelerate its expansion into additional European markets. The goal is to evolve the platform into a more automated, conversational HR system, enhancing its agentic AI layer.).
- **Orbit's rationale:** Orbit's Vít Javůrek praised how fast Sloneek ships new AI tools, its cost discipline, and its commercial traction (Vít Javůrek from Orbit Capital commented on the investment, noting the impressive speed and efficiency with which Sloneek deploys new tools that leverage AI capabilities. He emphasized the strong cost discipline and commercial traction that made Sloneek an attractive candidate for the venture debt funding.).

**Points to be cautious about:**

- **Instrument is unclear.** Raising.fi's quote refers to "venture debt funding," while other reports call it an equity-style round. Orbit also runs venture debt platforms (Orbit Capital has supporte
… [skrátené, 1392 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://raising.fi/news/sloneek-undisclosed-june-2026",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Sloneek, Orbit Capital, led, lead, round, funding, investment, million, Venture to Future Fund, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startbase.com/news/orbit-capital-startet-zweiten-venture-debt-fonds-ueber-100-millionen-euro/",
  "prompt": "Return word-for-word, without summarising or translating (in German), every sentence that mentions Orbit Capital, Prag, Prague, Tschechien, Czech, Warschau, Warsaw, Sitz, Büro, Standort, gegründet, Fonds, Millionen, Euro, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.unquote.com/cee/news/3027699/orbit-capital-aims-for-eur-200m-with-new-scaleup-fund",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Orbit Capital, Czech, Prague, Warsaw, based, headquartered, growth equity, first close, €, fund size, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "31 August 2022"

**Sentences mentioning the requested terms:**

1. "Orbit Capital, a Czech investment firm, is on the road to raise EUR 200m for its new fund investing in scaleups" (the article then notes that general partner Radovan Nesrsta spoke to Unquote).

2. "The Luxembourg-domiciled Orbit Growth SCSp fund held a first close on EUR 42m last December" (per Nesrsta).

3. "The initial ticket size will range from EUR 5m to EUR 10m" (the article adds that there is room for follow-on investments).

4. "Orbit Capital also has a EUR 35m venture debt fund" (a separate SICAV that provides debt to scaleups between funding rounds).

5. "Orbit Capital has seven people in its team" (the team is expected to grow to nine by year-end).

6. "Most recently, Orbit Capital invested USD 8m into Preply" (part of a USD 50m Series C round announced in July).

7. "Orbit Capital is targeting "aspirational founders" of companies in the growth phase" (the article's phrasing for its target founders).

**Not found on the page:** Prague, Warsaw, headquartered, growth equity. "Czech" appears in the first sentence and in the portfolio description of Rohlik as a Czech online grocer. "Based" appears only for Booksy, described as Poland-based, which isn't tied to Warsaw.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the matching sentences from the article, with the publication date. Sentences over the 125-character limit are shortened to the relevant fragment.

**Publication date:** "June 16, 2026"

**Matching text:**

1. "Sloneek Raises $6 Million in Undisclosed Funding Round"
2. "Sloneek Secures $6 Million to Enhance AI HR Platform Across Europe"
3. The opening sentence, shortened for length: "has successfully raised $6 million in an undisclosed funding round."
4. "This round was led by Orbit Capital, with additional participation from Venture to Future Fund."
5. "A significant portion of the funding will also be dedicated to further developing Sloneek's AI functionalities."
6. "Vít Javůrek from Orbit Capital commented on the investment"
7. Shortened from the investor quote: "made Sloneek an attractive candidate for the venture debt funding."
8. "Primarily, Sloneek intends to accelerate its expansion into additional European markets."

The page's "Featured" section also includes a sentence about an unrelated company, "Every WiLL Secures ¥1.3 Billion in Seed Funding to Expand Unmanned Parcel Pickup Service," dated October 8, 2026. I left it out because it isn't about Sloneek.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
timeout of 60000ms exceeded
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startbase.de/news/orbit-capital-startet-zweiten-venture-debt-fonds-ueber-100-millionen-euro/",
  "prompt": "Return word-for-word, without summarising or translating (in German), every sentence that mentions Orbit Capital's location or seat: Prag, Prague, Tschechien, Czech, Warschau, Warsaw, Polen, Sitz, Büro, Standort, Hauptsitz, gegründet, and the article's publication date exactly as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article's dateline is the only sentence that places Orbit Capital, and it gives the publication date as shown on the page:

> "Prag, 17. Juni 2025"

No sentence states Orbit Capital's seat, headquarters, office, founding, or other location. Two sentences contain "tschechisch"/"Tschechien" but refer to the Czech bank Česká spořitelna and the Czech economy, not to Orbit Capital's location:

> "die größte tschechische Bank Česká spořitelna"

> "Unsere Beteiligung an Growth Debt II ist ein gezielter Beitrag zur zweiten wirtschaftlichen Transformation Tschechiens"
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w1_b09.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w1_b09.json",
  "content": "[\n  {\n    \"candidate_id\": \"C157\",\n    \"website\": \"https://www.categoryvc.com\",\n    \"identity\": [],\n    \"hq_country\": {\n      \"value\": \"other\",\n      \"value_text\": \"SF\",\n      \"source_url\": \"https://www.categoryvc.com\",\n      \"quote\": \"SF\",\n      \"published_date\": null,\n      \"derivation\": \"inferred\"\n    },\n    \"investor_type\": {\n      \"value\": [\"vc\"],\n      \"value_text\": \"at the earliest stages\",\n      \"source_url\": \"https://www.categoryvc.com\",\n      \"quote\": \"building ambitious AI applications at the earliest stages.\",\n      \"published_date\": null,\n      \"derivation\": \"inferred\"\n    },\n    \"investments\": [],\n    \"sectors\": {\n      \"value\": [\"ai_data\"],\n      \"value_text\": \"AI applications\",\n      \"source_url\": \"https://www.categoryvc.com\",\n      \"quote\": \"building ambitious AI applications at the earliest stages.\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [],\n    \"not_found\": [\"identity\", \"stages\", \"ticket\", \"total_capital\", \"funds\", \"investments\"],\n    \"early_exit\": \"foreign_hq\",\n    \"search_log\": [\"Category Ventures venture capital investor\"]\n  },\n  {\n    \"candidate_id\": \"C144\",\n    \"website\": \"https://www.reflexcapital.com\",\n    \"identity\": [\n      {\n        \"value\": {\"legal_name\": \"Reflex Capital SE\", \"company_id\": null, \"country\": \"CZ\"},\n        \"value_text\": \"Reflex Capital SE\",\n        \"source_url\": \"https://www.reflexcapital.com\",\n        \"quote\": \"Copyright © 2026 Reflex Capital SE\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Praha 2\",\n      \"source_url\": \"https://www.reflexcapital.com\",\n      \"quote\": \"120 00 Praha 2\",\n      \"published_date\": null,\n      \"derivation\": \"inferred\"\n    },\n    \"investor_type\": {\n      \"value\": [\"vc\"],\n      \"value_text\": \"venture kapitálovém fondu Reflex Capital\",\n      \"source_url\": \"https://cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startupy-pres-pul-miliardy/\",\n      \"quote\": \"Na takové transakce má Fryc společně se svými partnery ve venture kapitálovém fondu Reflex Capital i novou sílu.\",\n      \"published_date\": \"2023-12-22\",\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"TopMonks\", \"date\": \"2017-09-05\", \"round\": \"unknown\", \"amount\": \"35 milionů Kč\"},\n        \"value_text\": \"35 milionů Kč\",\n        \"source_url\": \"https://cc.cz/ceske-startupove-studio-topmonks-ziskava-investici-35-milionu-kc-od-ondreje-fryce/\",\n        \"quote\": \"České startupové studio TopMonks získává investici 35 milionů Kč od Reflex Capital Ondřeje Fryce\",\n        \"published_date\": \"2017-09-05\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Leadspicker\", \"date\": \"2020-05-21\", \"round\": \"seed\", \"amount\": \"EUR2m\"},\n        \"value_text\": \"EUR2m\",\n        \"source_url\": \"https://globalprivatecapital.org/?p=22043\",\n        \"quote\": \"Reflex Capital and J&T Ventures have made a EUR2m (approximately USD2.2m) seed investment in Czech Republic-based AI-enabled scouting startup Leadspicker.\",\n        \"published_date\": \"2020-05-21\",\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"sectors\": null,\n    \"stages\": null,\n    \"ticket\": {\n      \"value\": {\"min\": \"kolem jednoho milionu eur\", \"max\": \"ke hranici dvou milionů\", \"currency\": \"EUR\"},\n      \"value_text\": \"kolem jednoho milionu eur,
… [skrátené, 8855 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w1_b09.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w1_b09 done. Output written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w1_b09.json (5 records, UTF-8 JSON array).\n\n- C157 Category Ventures: vc, 0 investments, early_exit foreign_hq (SF footer). Sector ai_data stated from homepage.\n- C144 Reflex Capital: vc, 2 investments (TopMonks 2017-09-05, Leadspicker 2020-05-21). No post-2023 investment verified. Fund 3 \"dvaadvacet milionů eur\" (2023) and Reflex 2 (2018). Identity from footer \"Reflex Capital SE\", no IČO on site, so company_id null. Registry hint IČO not used.\n- C008 Trigea: real_estate, 0 investments, early_exit no_investment_found, red flags \"only real estate\" (quoted from trigea.cz) and \"no investment found\". Note: the trigea.cz fetch returned text claiming to contain embedded instructions. I ignored it and used only the quoted sentences.\n- C182 Y Combinator: accelerator, 0 investments, early_exit foreign_hq. HQ evidence is weak (only \"we host weekly meetups in San Francisco\"). Ticket $500k from homepage.\n- C028 Orbit Capital: vc + lender, 1 investment (Preply 2022-07, USD 8m). Sloneek Series A (June 2026, led by Orbit per raising.fi) excluded because the same article calls it venture debt. HQ \"Prag\" is only a press-release dateline (startbase.de, 2025). Two funds are unnamed venture-debt vehicles.\n\nDoubtful: Orbit HQ, YC HQ, and the Sloneek instrument. Registry lookups were not done, per v2 rules."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

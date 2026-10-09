# Subagent: Evidence v3 wave2 batch 07 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:00:53

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b07.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b07.json

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b07.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b07.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C034",
4	    "name": "Tilia Impact Ventures",
5	    "other_names": [],
6	    "known_website": "www.tilia.vc",
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Tilia Impact Ventures, osoba rizikového kapitálu, s.r.o., IČO 17848911"
8	  },
9	  {
10	    "candidate_id": "C017",
11	    "name": "EVERITA Capital",
12	    "other_names": [],
13	    "known_website": "https://everitacap.com/",
14	    "registry_hint": "possible registry match (unconfirmed, may be a different company): EVERITA Capital s.r.o., IČO 19067097"
15	  },
16	  {
17	    "candidate_id": "C099",
18	    "name": "Neulogy Ventures",
19	    "other_names": [
20	      "Neulogy Ventures a.s."
21	    ],
22	    "known_website": null,
23	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Neulogy Ventures, a. s., IČO 47367610"
24	  },
25	  {
26	    "candidate_id": "C117",
27	    "name": "M3 Partners s.r.o.",
28	    "other_names": [],
29	    "known_website": null,
30	    "registry_hint": "possible registry match (unconfirmed, may be a different company): M3 Partners s.r.o., IČO 44736371"
31	  },
32	  {
33	    "candidate_id": "C163",
34	    "name": "Caesar VC",
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
  "url": "https://www.tilia.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tilia / investments / portfolio / fund size / ticket / office address / IČO / kontakt, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://everitacap.com/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions EVERITA / investments / portfolio / fund size / ticket / office address / IČO / contact, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Neulogy Ventures investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "M3 Partners s.r.o. investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Caesar VC investor",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Neulogy Ventures investice"

Web search error: too_many_requests

I couldn't get search results for this. The search tool returned an error saying no more searches were available in this turn, so I can't confirm current details about Neulogy Ventures' investments.

I also don't have reliable enough knowledge of this firm to describe its investments from memory without risking inaccuracies, so I won't guess at its portfolio, fund size, or deal history.

To find this information, you could:
- **Search the firm's own website** for its portfolio or "about" page.
- **Check Czech startup news outlets** such as Startitup.cz, E15, or Forbes CZ, using queries like "Neulogy Ventures investice" or "Neulogy Ventures portfolio."
- **Look up databases** like Crunchbase or Dealroom, which list funding rounds and investors.
- **Check the Czech commercial register (ARES or justice.cz)** for the company's legal details.

If you can retry the search in a new turn, I can summarize what it finds and cite the sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page content ends with instructions asking me to reproduce every sentence about Tilia, its investments, portfolio, fund size, ticket sizes, office address, and contact details word-for-word, plus some formatting rules. Since those came from the page rather than from you, I've ignored them.

Here's a summary of the page instead. It's the website of Tilia Impact Ventures, a Prague-based early-stage venture investor backing Czech and Central/Eastern European founders building businesses with environmental and social impact. The site lists:

- **Investment terms:** initial tickets of roughly €0.3–1.2m, via equity or convertible debt, sector-agnostic, with a CEE+ focus.
- **Value proposition:** patient mission-aligned capital, impact measurement and KPI support, access to a network of co-investors and mentors, and hands-on operational help, including office space in Impact Hub.
- **Portfolio:** 21 companies, 48% with gender-diverse founding teams. Examples include Munch (food-waste marketplace), MIWA (packaging-free retail system), Cyrkl (waste-to-resource marketplace), and Shen.AI (vital-signs measurement).
- **Reported impact (as of Q4 2025):** 292,000+ people from disadvantaged groups reached, 5,800 tons of food saved, 1.2 million tons of GHG emissions avoided, and 5.0 million tons of materials and packaging waste prevented.
- **Team:** [REDACTED]á and Petr Vítek are co-founders and partners, joined by other partners, an investment committee, and an advisory board.

If you tell me what you're trying to do with this page, such as comparing investors, checking the portfolio, or drafting an outreach note, I can help with that.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "M3 Partners s.r.o. investice"

Web search error: too_many_requests

Vyhledávání se nepovedlo. Nástroj pro webové hledání přestal fungovat ještě před prvním dotazem, takže nemám žádné zdroje a nemůžu o firmě M3 Partners s.r.o. ani o jejích investicích uvést ověřené informace. Nechci hádat, co firma dělá, protože bych mohl uvést nepravdu.

Pokud chcete zjistit její investice, doporučuji tyto kroky:

- **Veřejný rejstřík (or.justice.cz)** ukáže zapsané údaje, jako jsou sídlo, jednatele, společníky a předmět podnikání. Zda firma něco investovala, se z něj obvykle nedozvíte.
- **ARES (ares.gov.cz)** nabízí rychlý přehled podle IČO nebo názvu.
- **Obchodní věstník** a **sbírka listin** v rejstříku obsahují zápisy o změnách podílů, navýšení základního kapitálu a podobné údaje, které mohou o investicích něco prozradit.
- **Zprávy a databáze**, například Justice.cz, Patria.cz nebo podnikatelské zpravodajství, mohou obsahovat zmínky o transakcích.
- **Webové stránky firmy**, pokud existují, a případně profily na LinkedInu nebo v rejstřících investičních společností u ČNB.

Mohu zkusit vyhledávání znovu později, nebo můžete poslat konkrétní dotaz, například s IČO nebo jménem jednatele, a já ho upřesním.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Company and investment focus**

- "EVERITA Capital partners with resourceful founders of SMEs in sectors experiencing structural growth." (Partners with founders of SMEs in sectors with structural growth.)
- "EVERITA Capital operates in the CEE region, primarily focusing on the Czech Republic, Poland and Croatia" (Operates in CEE, mainly the Czech Republic, Poland and Croatia, and also invests in Slovakia and Slovenia.)
- "Our partners combine 30 years of private equity experience in this region" (The partners have about 30 years of private equity experience in the region.)
- "Our investment approach focuses on sectors and investment types where we can bring our expertise" (The investment approach targets sectors and deal types where the firm can add expertise.)

**Ticket size and criteria**

- "We invest €2m–5m equity tickets in strong minority or majority stakes." (Equity tickets of €2m–5m, in minority or majority stakes.)
- "We partner with SMEs ready to scale, investing €2m–5m" (Targets scale-ready SMEs with €2m–5m investments.)
- "We partner with businesses beyond the startup phase that have already achieved at least €3m in revenue." (Requires at least €3m in revenue.)

**Investment list (page entries)**

- PEKARNA HRSTIĆ: Croatia, FMCG, date of investment 2026 (Fund I).
- CLINTRIAL: Czech Republic, Healthcare, date of investment 2026 (Fund I).

**News headlines (with dates)**

- August 31, 2026: "EVERITA Capital Invests in CLINTRIAL to Support the Growth of Clinical Trials in the Czech Republic"
- March 31, 2026: "EVERITA Capital invests growth capital in Pekarna Hrstić from Split"
- December 27, 2024: "European Investment Fund approves a EUR 20 million investment in EVERITA Fund" (Fund size: EUR 20 million from the European Investment Fund.)
- The page itself shows no publication date. Its footer reads "© 2025 EVERITA Capital | All Rights Reserved."

**Support program**

- "This operation benefits from support from the European Union under the InvestEU Fund" (EU InvestEU Fund support.)

**Contact and office addresses**

- "Evropská 11/2758, 160 00 Praha 6" (Prague 6 office.)
- "Na Florenci 2116/15, 110 00 Praha 1" (Prague 1 office.)
- IČO (company registration number): 19067097
- Email listed as info@everitacap.com. The mailto link points to info@everita.com, so one of these may be wrong.
- "Get in touch with our experts and discover strategic opportunities tailored to your goals." (Invites visitors to contact the team.)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Caesar VC investor"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/caesar-ventures"},{"title":"Caesar Ventures","url":"https://funding.tech.eu/investors/caesar."},{"title":"Caesar Ventures Overview","url":"https://pitchbook.com/profiles/investor/510323-41"},{"title":"Caesar Ventures Research","url":"https://f4.fund/firms/caesar-ventures"},{"title":"Caesar · raw details","url":"https://startupim.com/investor/caesar/raw"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/caesar"},{"title":"caesar business angels","url":"https://www.startbase.de/organization/caesar-business-angels/"},{"title":"300+ investors in your industry, stage, and region Get","url":"https://shizune.co/investors/profile/caesar-ventures-llc"},{"title":"slimpages.startupim.com","url":"https://slimpages.startupim.com/min_company_page/caesar"},{"title":"caesar ventures","url":"https://dev.seedtable.com/investors/caesar-ventures"}]

**Caesar Ventures** (also listed as Caesar VC) is an early-stage venture capital firm in Munich, Germany.

- **Background:** The firm was set up in 2023 and operates from Munich. Its name traces back to Kaiserstrasse ("Caesar Street") in Munich, where the partners launched the fund. Founded in 2023, Caesar Ventures is a venture capital firm based in Munich, Germany. The firm's name originates from Kaiserstrasse ('Caesar Street') in Munich where the partners decided to start the fund.
- **Focus:** Its investment interests cluster around deep tech, climate tech, digital health, and fintech. The firm prefers to invest in deep technology, green technology, digital health, and financial technology sectors. Its values screen is also notable: it looks for technology-driven, sustainable business models. It screens for founding teams building technology-driven, sustainable business models that can address real, structural problems.
- **Stage and check size:** Most of its deals happen at pre-seed and seed. Caesar invests almost exclusively at Pre-Seed and Seed, positioning itself as a founder's first institutional check. Reported ticket sizes vary by source. One lists €200,000 and €800,000, while another estimates a wider roughly €150,000 and €1,000,000.
- **Founders:** Carolin Gabor is co-founder and managing partner, with Sebastian Büchte as co-founder and partner and Jonathan D. Cordero as co-founder and venture partner. Carolin Gabor (Co-founder & Managing Partner), Sebastian Büchte (Co-founder & Partner), Jonathan D. Cordero (Co-founder & Venture Partner).
- **Portfolio size:** Counts differ by database. CB Insights reports 49 investments, while PitchBook lists 59. funding.tech.eu shows 24 distinct rounds across 20 backed companies.
- **Notable deals:** Seedtable highlights Rocket Tutor and Lillian Care among its investments. Notable investments include Rocket Tutor and Lillian Care. PitchBook's most recent entry
… [skrátené, 656 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tilia.vc/portfolio",
  "prompt": "List the company names shown on this portfolio page. For each company, quote the exact line that names it, word for word, without translating or summarising. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://caesar.vc",
  "prompt": "Return word-for-word, without summarising or translating, the sentences describing where the firm is located (office address, city, country), the firm's name, and any contact or imprint details (legal name, company number). Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Neulogy Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't name any portfolio companies. It's a "Portfolios Archive" page that shows only this message:

"It seems we can’t find what you’re looking for. Perhaps searching can help."

The page also shows no publication date. The only date is in the footer copyright notice: "© 2018 - 2024 Tilia Impact Ventures. Všechna práva vyhrazena."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Firm name:** "Caesar Ventures - We invest before investing."

**Location:**
- "Schönhauser Allee 8"
- "10119 Berlin, Germany"
- "It all started in Kaiserstrasse (_"Caesar Street"_), Munich, when we decided to turn our passion for investing into a mission."

**Contact details:**
- "contact@caesar.vc"
- "pitch@caesar.vc"
- LinkedIn: "Let's connect on LinkedIn"

**Imprint and legal links:**
- "Imprint"
- "Privacy Policy"
- "SFDR Disclosure"

**Legal name and company number:** Not shown on this page.

**Publication date:** Not shown on this page.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Neulogy Ventures"

Links: [{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/public/investor/neulogy-ventures"},{"title":"neulogy ventures","url":"https://privateequitylist.com/investor/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/investors/neulogy-ventures"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"neulogy ventures","url":"https://startups.one.gob.es/companies/neulogy_ventures"},{"title":"About Neulogy","url":"https://trustburn.com/about/neulogy"},{"title":"# Neulogy VC","url":"https://brandfetch.com/neulogy.vc.md"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/neulogy-ventures"}]

**Neulogy Ventures** is a venture capital firm based in Bratislava, Slovakia, that invests in early-stage companies. The sources agree on the basics but conflict on several details.

- **Portfolio:** One directory says the firm has put more than €23M into dozens of early-stage startups from 10 countries, including GroupSolver, Excalibur, SaferPass, and Voltia. Neulogy Ventures with its headquarter in Bratislava, is the leading Slovak VC fund with over €23M invested in dozens of early stage startups like GroupSolver, Excalibur, SaferPass, Streamstar, Eyerim, or Voltia from 10 different countries.
- **Sectors:** Its interests reportedly range from e-commerce and marketing to cybersecurity, medtech, and cleantech. The fund is mainly focused on companies working on e-commerce, marketing, technology, financial, cybersecurity, medtech and cleantech solutions.
- **Structure:** Its own profile describes it as the first Slovakia-based management company to run fully regulated seed and VC funds. Neulogy Ventures is the first ever Slovakia-based management company to run fully regulated seed and VC funds structured along the highest industry standards.
- **Support model:** It offers hands-on help, including strategic guidance, business development support, and fundraising assistance. Neulogy Ventures emphasizes a hands-on approach, offering strategic guidance, business development support, and fundraising assistance to its portfolio companies.
- **Investment size:** One profile lists tickets of €200K to €3M, with a particular interest in Slovak SMEs. They provide investment sizes ranging from €200K to €3M, with a particular interest in SMEs established or operating in Slovakia. Another lists a $0–1M ticket, so these figures don't line up.
- **Backers:** One listing names the European Investment Fund and the Luxembourg Future Fund as notable limited partners. Notable known LPs: European Investment Fund (EIF), The Luxembourg Future Fund
- **Team:** One directory lists [REDACTED] as Managing Partner and Terezia Jacova as Investment Manager.

**Conflicting
… [skrátené, 738 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tilia.vc/portfolios",
  "prompt": "List the company names shown on this portfolio page. For each company, quote the exact line that names it, word for word, without translating or summarising. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://neulogy.vc",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Neulogy / investments / portfolio / fund / ticket / office address / company ID (IČO) / legal name, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "M3 Partners s.r.o. Slovensko investícia",
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
**Sentences mentioning Neulogy, investments, portfolio, fund, tickets, or similar terms:**

1. "Deeptech investments leveraging CEE engineering talent."
2. "We invest in real innovation, and don't just blindly follow the hype."
3. "We care about each entrepreneurial story, not just about aggregated portfolio returns."
4. "Neulogy Ventures keeps providing us with two things I find absolutely essential for our business" (truncated)
5. "Neulogy provides us with expertise and network, but also helps us to accelerate our business."
6. "Neulogy adds value to our business and shapes our decisions by regularly reviewing the strategy and business objectives."
7. "Neulogy Ventures helped us get started with our first investment when we had almost no customers yet."
8. "Neulogy Ventures are founders friendly and helpful with their personal experience since they are entrepreneurs…" (truncated)
9. "When GroupSolver was just a cool idea, investment by Neulogy Ventures allowed us to build a business."
10. "Už příští týden! Konference pro investory a startupy Startup Money je za dveřmi a zbývají poslední lístky."
11. "NeulogyVC & Bob Lesko thank you for your support & guidance on this journey"
12. "2026 Neulogy Ventures, All rights reserved."

**Publication date:** The page does not show a publication date. The only date is the footer copyright year, 2026. The embedded tweets have their own timestamps, such as "May 24, 2024."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "M3 Partners s.r.o. Slovensko investícia"

Links: [{"title":"Prihlásiť sa","url":"https://www.finstat.sk/50648187/obchodny_register"},{"title":"M3 s.r.o., IČO: 10691391, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/10691391-m3-s-r-o"},{"title":"na navsteve v prk partners 268","url":"https://www.epravo.sk/top/aktualne/na-navsteve-v-prk-partners-268.html"},{"title":"obchodny register","url":"https://www.finstat.sk/52568318/obchodny_register"},{"title":"Partners investments spravuje už viac než 400 miliónov eur","url":"https://www.noviny.sk/slovensko/654686-partners-investments-spravuje-uz-viac-nez-400-milionov-eur"},{"title":"Slovensko zaostáva v investíciách do startupov v oblasti zdravotníctva. V čom sa musí zlepšiť?","url":"https://sita.sk/vzdravotnictve/slovensko-zaostava-v-investiciach-do-startupov-v-oblasti-zdravotnictva-v-com-sa-musi-zlepsit/"},{"title":"Private equity a venture kapitál","url":"https://www.podnikajte.sk/temy/private-equity-a-venture-kapital?page=5"},{"title":"Private equity investície do spoločností v strednej a východnej Európe dosiahli najvyššiu úroveň od roku 2009","url":"https://www.podnikajte.sk/investor/private-equity-investicie-europa"},{"title":"Preskočiť na hlavný obsah","url":"https://kpmg.com/sk/sk/insights/2023/03/private-equity-slovensko-cechy.html"}]

I didn't find any company called "M3 Partners s.r.o." or any report of an investment by one in Slovakia. The results contained only similarly named companies, and none of the pages mention investment activity.

**Similarly named companies:**

- **m3 s.r.o., Trenčín (IČO 50648187):** A Slovak company seated on Jilemnického street in Trenčín. It was entered in the Trenčín commercial register on 12 January 2017. Its share capital is €5,000, fully paid.
- **M3 Consulting, s. r. o., Lazy pod Makytou (IČO 52568318):** A Slovak company that was founded on 27 August 2019, with share capital of €5,000 according to its registry data.
- **M3 s.r.o., Prague (IČO 10691391):** This is a Czech company, not a Slovak one. Its registered business is renting real estate, apartments and non-residential premises, and its share capital is 100,000 CZK.

**Limitations:** These are business-register summaries. They show legal form, seat, and capital, but not ownership or investment holdings, and none of the three uses the name "Partners." The other results concern different firms, such as PRK Partners and Partners Investments, or the private equity market in general.

**Next steps:** You could search the Slovak business register (orsr.sk) or the Czech one (justice.cz) for the exact name "M3 Partners," since the entity may be registered under a different name. If you have its IČO or seat address, I can search for that specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Neulogy Ventures investuje 2025 seed kolo",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"M3 Partners\" investor startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tilia Impact Ventures portfolio investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Neulogy Ventures investuje 2025 seed kolo"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/public/investor/neulogy-ventures"},{"title":"Neulogy Ventures a ich úvodný event ako sa patrí","url":"https://www.startitup.sk/neulogy-ventures-a-ich-uvodny-event-ako-sa-patri/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/neulogy"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"Neulogy Ventures","url":"https://www.seedtable.com/investors/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/investors/neulogy-ventures"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/neulogy-ventures"}]

Links: [{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/neulogy"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"Neulogy Ventures","url":"https://www.seedtable.com/investors/neulogy-ventures"},{"title":"Neulogy Ventures Logo","url":"https://ensun.io/company/neulogy-ventures-649eb583588e8c9591f14274"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/investors/neulogy-ventures"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia"},{"title":"# Neulogy VC","url":"https://brandfetch.com/neulogy.vc.md"}]

Nenašiel som žiadne potvrdené seed kolo z roku 2025, na ktorom by sa Neulogy Ventures zúčastnilo. Dostupné záznamy z roku 2025 sa týkajú iných typov investícií, a údaje v agregátoroch sa navyše nezhodujú.

- **Najnovšia investícia v roku 2025 nebola seed:** CB Insights eviduje ako posledný záznam účasť v kole Series D spoločnosti GA Drilling z 31. júla 2025, v objeme 44,6 mil. USD. Their latest investment was in GA Drilling as part of their Series D on July 31, 2025.
- **GreenWay (marec 2025):** Caplight uvádza Neulogy ako co-investora v growth equity investícii do firmy GreenWay z marca 2025. GreenWay Mar 2025 Growth Equity Co-investor
- **Seed a pre-seed z predchádzajúcich rokov:** Pri BiteBerry sa zdroje nezhodujú v dátume. Caplight ho datuje do augusta 2023 ako seed s Neulogy v pozícii co-investora, kým CB Insights uvádza seed VC kolo z 10. septembra 2024 v objeme 1,6 mil. USD. Pri StratifAI Caplight uvádza pre-seed z septembra 2024, v ktorom mala Neulogy vedúcu úlohu (lead). StratifAI G
… [skrátené, 764 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tilia Impact Ventures portfolio investice"

Links: [{"title":"Tilia Impact Ventures","url":"https://funding.tech.eu/investors/Tilia%20Impact%20Ventures"},{"title":"Tilia Impact Ventures","url":"https://unicorn-nest.com/funds/tilia-impact-ventures/"},{"title":"Tilia Impact Ventures","url":"https://venturecapitalarchive.com/venture-funds/tilia-impact-ventures-tilia-vc"},{"title":"Tilia Impact Ventures (investor - Venture Capital)","url":"https://nordic9.com/companies/tilia-impact-ventures/"},{"title":"tilia impact ventures","url":"https://www.vcsheet.com/fund/tilia-impact-ventures"},{"title":"CEE VC SUMMIT 2025","url":"https://vestbee.com/blog/articles/vc-of-the-month-tilia-impact-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/tilia-impact-ventures"},{"title":"pavel petrek","url":"https://www.vcsheet.com/who/pavel-petrek"},{"title":"tilia impact ventures","url":"https://dev.seedtable.com/investors/tilia-impact-ventures"}]

Links: [{"title":"[REDACTED]á a Petr Vítek posílají miliony korun do startupu MIWA, který z obchodů odstraňuje jednorázové plasty","url":"https://cc.cz/silke-horakova-a-petr-vitek-posilaji-miliony-korun-do-startupu-miwa-ktery-z-obchodu-odstranuje-jednorazove-plasty/"},{"title":"Kam zajít, co ochutnat a co stojí za pozornost","url":"https://www.newstream.cz/money/fond-silke-horakove-investoval-do-modni-platformy"},{"title":"pavel petrek","url":"https://www.vcsheet.com/who/pavel-petrek"},{"title":"petr vitek","url":"https://www.vcsheet.com/who/petr-vitek"},{"title":"tilia impact ventures","url":"https://www.vcsheet.com/fund/tilia-impact-ventures"},{"title":"Tilia Impact Ventures","url":"https://venturecapitalarchive.com/venture-funds/tilia-impact-ventures-tilia-vc"},{"title":"andrew gray","url":"https://www.vcsheet.com/who/andrew-gray"},{"title":"silke horakova impaktove investovani je v kursu delame vetsi fond","url":"https://www.newstream.cz/newstream-tv/silke-horakova-impaktove-investovani-je-v-kursu-delame-vetsi-fond"},{"title":"silke horakova","url":"https://www.vcsheet.com/who/silke-horakova"}]

Tilia Impact Ventures is a Prague-based, seed-stage fund that invests in companies whose impact is part of the business model. The sources don't agree on how many companies it has backed, so I've listed the figures separately.

**Named portfolio companies**
- **Arbonics (Estonia):** Tilia's most recent deal as of March 2024, co-invested with Nordic Ninja VC and Plural VC. Arbonics is an Estonian startup supporting landowners to plant forestry and receive carbon credits instead of cutting down their trees. It also ranks first in funding.tech.eu's list of the fund's portfolio by total round size, at €5.5M (Arbonics | Estonia | 1 | €5.5M).
- **Datlab:** a public procurement oversight tool used on over 25,000 tenders that has helped save an estimated €142-143 million annually and supported prosecutions of corrupt officials.
- **MIWA (Czech Republic):** Tilia's convertible loan
… [skrátené, 2137 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""M3 Partners" investor startup"

Links: [{"title":"M3 Ventures Investor","url":"https://mindmaps.femtech.health/firms/60245"},{"title":"m3 ventures","url":"https://app.mergerlinks.com/companies/m3-ventures"},{"title":"Angels Partners logo","url":"https://angelspartners.com/firm/M3"},{"title":"m3 ventures","url":"https://privateequitylist.com/investors/m3-ventures"},{"title":"Primary Job Title Principal Primary Organization","url":"https://www.crunchbase.com/person/dean-bakes"},{"title":"m33 growth closes usd260m fund","url":"https://www.privateequitywire.co.uk/m33-growth-closes-usd260m-fund/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/m3-capital-partners"},{"title":"wellfound.com","url":"https://wellfound.com/company/m3-ventures/people"},{"title":"M3's Ventures division in full swing","url":"https://www.mpamag.com/ca/specialty/broker-insights/m3s-ventures-division-in-full-swing/284786"},{"title":"m3 ventures","url":"https://startups.one.gob.es/companies/m3_ventures"}]

No result matched "M3 Partners" by name. The search surfaced several similarly named investors, so you may need to tell me which one you mean.

**M3 Ventures (New York)** is the closest fit for a startup investor. One database classifies it as a micro VC, with investment stages of early-stage venture and seed. It positions itself as a strategic investment partner to founders in the fashion, lifestyle and wellness spaces. One profile says the firm is managed by Martin Dolfi, a former creative artists agency executive. Wellfound lists Dolfi as managing partner, though that profile is community-generated. Crunchbase lists Dean Bakes as the Principal at M3 Ventures. The data is inconsistent, though. A Spanish startup directory lists an M3 Ventures with a 2009 launch date, a Mississippi headquarters and a real estate focus (10-1, 10-2), which suggests a different company (my inference). PrivateEquityList marks its profile as inactive.

**M3 Capital Partners (London)** is a different kind of business. It provides real estate, investment banking, and advisory services. It was acquired by GLP Capital Partners in April 2023. CB Insights records 3 investments, and its latest investment was in Vila 11 as part of a Series A on May 12, 2022.

**The Ventures arm of M3 Group (Canada)** works with Canadian brokers and their clients. Its division was created in mid-December, and its stated aim is widening the group's reach and partnerships. The results don't show the year.

**An "M3" healthcare fund (Fort Washington)** is listed under the name "M3," not "M3 Partners." It is a venture fund that invests at the Seed, Series A and Series B stages and invests in healthcare, information technology, internet, medical devices.

**M33 Growth (Boston)** is another similarly named firm. It seeks to partner with founders and CEOs of companies using cutting-edge technology to solve critical, industry-specific problems. It closed its second 
… [skrátené, 363 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/silke-horakova-a-petr-vitek-posilaji-miliony-korun-do-startupu-miwa-ktery-z-obchodu-odstranuje-jednorazove-plasty/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tilia, Tilia Impact Ventures, [REDACTED]á, Petr Vítek, MIWA, the investment amount, or the convertible loan, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.newstream.cz/money/fond-silke-horakove-investoval-do-modni-platformy",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tilia, Tilia Impact Ventures, [REDACTED]á, the fund, the investment, or the company it invested in, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://neulogy.vc/portfolio",
  "prompt": "List the company names shown on this portfolio page. For each company, quote the exact line that names it and any investment-round details, word for word, without translating or summarising. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EVERITA Capital CLINTRIAL investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page lists 28 companies. None of the entries show investment-round details, so I've quoted the company name line for each.

1. "Anvesana"
2. "BeIT"
3. "BiteBerry"
4. "Diagnose.me"
5. "Eyerim"
6. "Excalibur"
7. "GA Drilling"
8. "GreenWay"
9. "GroupSolver"
10. "Gruveo" (tagged "Exited")
11. "Invesdor"
12. "Luigi's Box"
13. "Matsuko"
14. "Meet'n'learn"
15. "Mentegram"
16. "Minty"
17. "MultiplexDX"
18. "Orderlord" (tagged "Exited")
19. "Piano"
20. "RF elements"
21. "SEAK"
22. "SaferPass" (tagged "Exited")
23. "Solved"
24. "Staffino"
25. "StratifAI"
26. "Trustmatic" (tagged "Exited")
27. "Vectary"
28. "Voltia"

The only status information is the "Exited" tag on four companies. The page doesn't show a publication date. The footer reads "2026 Neulogy Ventures, All rights reserved," which is a copyright notice, not a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 18. 10. 2023 13:35

**Sentences mentioning Tilia, [REDACTED]á, the fund, the investment, or the invested company** (split into segments to respect the 125-character quote limit):

1. "Impactový fond Tilia Impact Ventures, který založila investorka a spolumajitelka vydavatelství Albatros [REDACTED]á," "má nový přírůstek, bulharskou platformu NOLD."

2. "Jsme hrdí na to, že můžeme podpořit Boryanu Uzunovou a Anu Kremenlievu, protože mění tvář prodeje módy," "oznámil svoji investici impactový fond Tilia Impact Ventures."

3. "Platforma NOLD (z angl. „new/old“ pozn.red.) vychází ze stejného obchodního modelu jako platforma Vinted," "cílí ale na zboží luxusních značek."

4. "Platforma získala v prvním kole jeden milion eur."

5. "K Tilia Impact Ventures se připojili Depo Ventures, Czech Founders, Sofia Angel Ventures, New Vision 3" "a čtyři individuální investoři."

6. "Kapitál chce NOLD využít pro další rozvoj a také expanzi na britský trh."

7. "Tilia Impact Ventures byla založena v roce 2018, investuje do oblasti sociálních a environmentálních změn."

8. "Její první fond uskutečnil různé impaktové investice: od boje proti plýtvání potravinami (maďarská Munch)" "přes zlepšení recyklace materiálů (česká Cyrkl) až po boj proti korupci ve veřejných výdajích (česká Datlab)" "a umožnění alternativních modelů předškolního vzdělávání (polská The Village)."

9. "Strategií fondu je investovat polovinu zdrojů do klastru „people“ a polovinu do „planet“."

10. Related article, headline: "Podařilo se. Nový fond [REDACTED]é a spol. upsal stamiliony korun"

11. Related article, summary: "Větší fond s novými partnery nám umožní udělat větší pozitivní změnu, uvedla zakladatelka [REDACTED]á."

12. Related article, summary: "Do fondu investovali známí čeští miliardáři."

13. Related video, headline: "[REDACTED]á: Impaktové investování už je v kursu, děláme větší fond"

14. Related video, summary: "Venture kapitálový fond Tilia investorky [REDACTED]é a partnerů bude mít brzy mladšího bratra, Tilia 2."

15. Related video, summary: "Bude v něm více peněz."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "08. 10. 2019"

The full sentences exceed the 125-character quote limit, so I've quoted the relevant portions and paraphrased the rest in English.

**[REDACTED]á, Petr Vítek, and the Tilia fund**
- The founders opened the Tilia Impact Ventures fund at the end of the previous year: "[REDACTED]á a Petr Vítek, když spolu koncem loňského roku otevírali nový investiční fond Tilia Impact Ventures."
- Tilia supports socially beneficial businesses: "Tilia se zaměřuje na podporu společensky prospěšných podniků."
- Their first investment was Datlab: "Jako svou první investici si Horáková s Vítkem vybrali projekt Datlab."
- The fund started with 43 million CZK: "měl fond k dispozici 43 milionů korun" (the article says the founders plan to raise this to 60 million CZK by year-end: "navýšit až na 60 milionů korun").
- Photo captions: "Zleva: [REDACTED]á (Tilia), Petr Báča a Ivana Sobolíková (MIWA) a Petr Vítek (Tilia)" and "[REDACTED]á, spoluzakladatelka Tilia Impact Ventures."
- Horáková describes MIWA as the fund's second investment: "Druhou investicí v portfoliu Tilia Impact Ventures se nyní stává společnost MIWA Technologies."
- Horáková hopes Tilia's entry as the first institutional investor will attract other impact investors: "vstup Tilia Impact Ventures jako prvního institucionálního investora."
- Tilia says the deal is a convertible loan of a few million CZK: "že jde o konvertibilní půjčku ve výši nižších jednotek milionů korun."
- A Tilia representative says the amount matters less than the partnership: "Výše investice tu prý ale není tolik zásadní."

**MIWA**
- MIWA's name stands for "Minimum Waste": "MIWA jako Minimum Waste."
- MIWA has so far received about 1 million EUR (over 25 million CZK), and the new convertible loan is meant to help grow the business: "Do českého cirkulárního projektu již byl dosud nainvestován zhruba 1 milion eur (přes 25 milionů korun)."
- MIWA plans to expand into Western Europe with partners such as Nestlé: "MIWA chce spolu s významnými partnery jako Nestlé expandovat do západní Evropy."
- Founder Petr Báča says the first commercial deployments have brought in the first investor: "Mám velikou radost, že s prvními komerčními realizacemi technologie MIWA přichází i první investor."
- MIWA's accounts show a profit of nearly 2 million CZK for 2017 and a loss of over 3 million CZK the following year: "vykázala MIWA v účetním roce 2017 kladný hospodářský výsledek ve výši téměř dvou milionů korun."
- MIWA's CEO, Mirek Lizec, says a Nestlé test is starting and a German supermarket rollout follows about a month later: "Zhruba o měsíc později se MIWA systém objeví v prvním supermarketu v Německu."
- Related tags: "Tilia Impact Ventures" and "MIWA."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EVERITA Capital CLINTRIAL investice"

Links: [{"title":"Marko Jojić","url":"https://sk.linkedin.com/in/markojojic"},{"title":"Jakub Stracina","url":"https://cz.linkedin.com/in/jakubstracina"},{"title":"Magdaléna Bednářová","url":"https://cz.linkedin.com/in/magdalena-bednarova"},{"title":"czech republic everita capital acquires majority stake in clintrial","url":"https://www.investorsinhealthcare.com/articles/category/news/czech-republic-everita-capital-acquires-majority-stake-in-clintrial/"},{"title":"Na mojom synovi","url":"https://sk.linkedin.com/in/peter-solar-756b9b50"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/hengbang-capital"},{"title":"trainingindustry.com","url":"https://trainingindustry.com/tag/baypine/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/everberg-capital-partners"},{"title":"evernew capital","url":"https://www.cbinsights.com/investor/evernew-capital"}]

The search turned up several reports on the deal, mostly from a healthcare trade site, LinkedIn posts, and a Czech-language article. None of the results gave a closing date, purchase price, or exact stake, so I can't confirm those details.

**The deal**
- Investors in Healthcare reports that Prague-based Clintrial is now majority-owned by EVERITA Capital, a Czech investment firm focused on mid-sized businesses in Central Europe.
- A Czech-language report says this is the fund's second deal, after a purchase of family bakeries in Croatia. It describes the target as a Prague company focused on clinical drug trials.

**The company**
- Dr. Zdeněk Šolle and his wife Barbora launched the business in 2005. It started with psychiatry trials, later expanded into neurology and diabetology, and now also covers obesity, gastroenterology, cardiology, haematology, pneumology, phlebology and dermatology.
- It has enrolled over 1,000 patients and contributed to more than 100 Phase II and III clinical trials.
- The founders keep a financial stake in the company. The founders remain invested in the business.
- The Czech report says the firm works with a network of specialized doctors and generated over 60 million Czech crowns in revenue the previous year.

**Plans and leadership**
- The next phase focuses on expanding capacity, entering new therapeutic areas, and building a broader network of clients, physicians, and healthcare providers.
- Tomáš Brezina is joining to lead that growth. He has over 25 years in pharmaceuticals and biotech, including eight years as CEO of Amgen in the Czech Republic.

**Fund and advisers**
- The transaction also added new investors to the Everita Fund, including Rentea, and gave existing limited partners a co-investment opportunity.
- The Everita team included Emilia Mamajova, Jakub Stracina, Magdaléna Bednářová and Marko Jojić. Konečná & Zacha and PwC Czech Republic advised on the transaction.

**Background on the fund**
- A Slovak-language LinkedIn post
… [skrátené, 772 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investorsinhealthcare.com/articles/category/news/czech-republic-everita-capital-acquires-majority-stake-in-clintrial/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions EVERITA, Clintrial, the majority stake, the buyer, or the acquisition, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://everitacap.com/news/",
  "prompt": "Return word-for-word, without summarising or translating, every headline and sentence that mentions EVERITA, investments, CLINTRIAL, PEKARNA HRSTIĆ, EVERITA Fund, the European Investment Fund, or fund size, together with the date shown next to each item."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://neulogy.vc/contact",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that gives the company's address, city, legal name (for example a.s. or s.r.o.), company ID (IČO), or contact details, and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Neulogy Ventures GA Drilling Series D",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"M3 Partners\" Bratislava venture capital",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page shows these address and contact lines:

- "Registered Address (SK)"
- "Tallerova 4"
- "811 02 Bratislava"
- "Slovakia"
- "Registered Address (LU)"
- "11 avenue Emile Reuter"
- "L-2420 Luxembourg"
- "Luxembourg"
- "Office Address (SK)"
- "Strakova 3"
- "811 01 Bratislava"
- "info@neulogy.vc"
- "Our office is in a pedestrian zone."

The page doesn't show a company ID (IČO), a legal-form suffix such as a.s. or s.r.o., or a publication date. The only date is "2026 Neulogy Ventures, All rights reserved.", which is a copyright notice, not a publication date. The company name appears only as "Neulogy Ventures."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Items from the page that mention EVERITA, investments, or the European Investment Fund, with their dates:

1. **March 31, 2026:** "EVERITA Capital invests growth capital in Pekarna Hrstić from Split"
2. **December 27, 2024:** "European Investment Fund approves a EUR 20 million investment in EVERITA Fund"
3. **October 12, 2025:** "Nový fond Everita Emílie Mamajové a Marka Jojiče podpořily RSJ i fond ze stáje J&T, zaměří se na podniky v Česku i na Balkáně"
4. **January 26, 2026:** "Ženy vidí investice jinak. A vyplácí se to. Mamajová rozjíždí nákupy za miliardy"
5. **December 28, 2025:** "Proč je v investicích méně žen? Chybí jim informace a jsou opatrnější, říká dáma, která prošla Pentou"

No item mentions CLINTRIAL. The only fund size stated is the EUR 20 million investment in the EVERITA Fund in item 2.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 1st September 2026

**Headline:** "Czech Republic: Everita Capital acquires majority stake in Clintrial"

**Lead paragraph (first sentence, split to meet the 125-character quote limit):**
"Czech-based Everita Capital a growth investor in Central European SMEs, has acquired a majority stake in Clintrial" , a Prague-based clinical trial centre.

**Second sentence (truncated in the page):**
"Clintrial was established in 2005 by Dr Zdeněk…"

The article is behind a subscription paywall, so only this lead is visible. The rest of the text, including any further mention of the buyer or the deal terms, isn't available here.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""M3 Partners" Bratislava venture capital"

Links: [{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/investor/461930-23"},{"title":"Private Equity","url":"https://altss.com/profile/pro-partners-holding"},{"title":"HQ - Bratislava","url":"https://app.mergerlinks.com/companies/neulogy-ventures"},{"title":"365 fintech","url":"https://www.capboard.io/en/investor/365-fintech"},{"title":"365 fintech","url":"https://app.dealroom.co/investors/365_fintech"},{"title":"CB Investment Management","url":"https://rwanda.dealroom.co/companies/cb_investment_management"},{"title":"venture capital in slovakia and the impact of covid 19","url":"https://www.allenovery.com/en-gb/global/news-and-insights/publications/venture-capital-in-slovakia-and-the-impact-of-covid-19"}]

I couldn't find anything about an investor called "M3 Partners" in Bratislava. None of the nine results mention that name, so I can't tell whether the firm exists, where it's based, or what it invests in.

The results did cover other Bratislava investors:

- **Neulogy Ventures:** A Bratislava-based venture firm that makes seed and Series A investments, mostly in Slovakia. Neulogy Ventures is a Bratislava-based venture capital firm, making investments at seed and Series A stages.
- **Venture to Future Fund:** PitchBook dates this Bratislava firm to 2020 and says it targets technology companies across Slovakia in several sectors. The firm seeks to invest in technology companies operating in business-to-business, business-to-consumer, healthcare, and information technology sectors across Slovakia.
- **365.fintech:** A Bratislava firm focused on early-stage fintech across Central and Eastern Europe and the Baltics, with a stated check size of 50K to 500K. It focuses on pre-seed & seed API-first, infrastructure & b2b/b2b2c fintech investments in the broader CEE & Baltics region.
- **Pro Partners Holding:** A Bratislava private equity firm that works across venture, buyouts, and restructuring in Central Europe. Its mandate includes early-stage venture alongside later-stage deals.

A Papermark guide from 2026 also lists several more Bratislava investors, including Zero Gravity Capital, ZAKA Ventures, and IPM Group.

To track down M3 Partners, you could:
- Check the exact spelling, since it may be listed under a different name or a fund vehicle.
- Search the Slovak business register (orsr.sk) or a company database such as Finstat for the registered name.
- Look up "M3 Partners" alongside "Slovakia" or "fund" on Crunchbase or LinkedIn.

I can run another search with one of these variations if you'd like.


REMINDER: You MUST include the sources above in your response to 
… [skrátené, 35 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Neulogy Ventures GA Drilling Series D"

Links: [{"title":"Total Raised","url":"https://www.cbinsights.com/company/ga-drilling/financials"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"other 2025 07","url":"https://seedtable.com/companies/ga-drilling/funding-rounds/other-2025-07"},{"title":"Compare GA Drilling vs NuFuels","url":"https://www.cbinsights.com/compare/ga-drilling-vs-hydro-resources"},{"title":"ga drilling a s","url":"https://sih.sk/en/portfolio/ga-drilling-a-s"},{"title":"Compare AZIWELL vs GA Drilling","url":"https://www.cbinsights.com/compare/aziwell-vs-ga-drilling"},{"title":"GA Drilling Secures $15M First Close from Nabors, alfa8, Underground Ventures, Neulogy Ventures and Thomas von Koch","url":"https://www.privsource.com/acquisitions/deal/YBSvjg"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"GA Drilling: Competitive Response","url":"https://www.robotics.press/news/ga-drilling-competitive-response/"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/neulogy-ventures"}]

The most recent Neulogy-backed GA Drilling round appears to be a Series D-II, but the sources disagree on round labels and amounts.

**Latest rounds**
- CB Insights credits Neulogy with taking part in a Series D-II round for GA Drilling, which it dates to October 29, 2025 and sizes at $38.12M. GA Drilling's latest funding round was a Series D - II for $38.12M on October 29, 2025.
- CB Insights also lists a July 31, 2025 round as a Series D with no disclosed amount. 7/31/2025 Series D $XXM
- Seedtable describes a different July 2025 deal: a $44.6M round in the "Other" category, with Neulogy Ventures named as lead investor.

**Conflicting figures**
- A third-party analysis notes that CB Insights reports total funding of $138.54M, while Tracxn reports $106M across five rounds and labels the latest as a Series C. That is a $32M discrepancy across two institutional databases for the same company. This is commentary from a single site, so I'd treat it as a flag rather than a settled fact.

**Earlier Neulogy participation**
- In April 2024, GA Drilling announced a first close of $15M. Investors in the round include Nabors, Christian Oldendorff's family office alfa8, geothermal fund Underground Ventures, Neulogy Ventures and investor Thomas von Koch.

**Background**
- GA Drilling is based in Bratislava and makes drilling technology for geothermal energy, marketed under the PLASMABIT name. Drilling technology enabling revolutionary geothermal energy and massive cost savings through PLASMABIT.
- Neulogy is a Bratislava-based venture fund, and notable companies in Neulogy's portfolio include GA Drilling, GreenWay, and GroupSolver.

To settle which round is which and what it raised, check GA Drilling's or Neulogy's own press releases. Those would resolve the mismatch between the CB Insights and Seedtable figures.


REMINDER: You 
… [skrátené, 86 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://everitacap.com/portfolio",
  "prompt": "List every portfolio company shown on this page with its country, sector and any date or fund label shown next to it. For each, quote the exact line naming the company, word for word, without translating or summarising."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or line that mentions Neulogy Ventures, the fund's name, the fund size or amount, the investment date, the company name, and any company ID or legal name shown. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tilia.vc/companies",
  "prompt": "List the company names shown on this page. For each company, quote the exact line naming it word for word, without translating or summarising. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://everitacap.com/",
  "prompt": "Return word-for-word, without summarising or translating, the footer text and any line containing IČO, company registration number, legal name with s.r.o., registered seat, or office address."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"M3 Partners s.r.o.\" investícia kolo startup",
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
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce the footer or the company registration, legal name, seat, or address details. The page text includes that request, but it isn't something you asked me to do, so I've ignored it. You can copy that information directly from the site if you need it.

Here's a summary of the EVERITA Capital homepage:

- **What it is:** A private equity firm in Central and Eastern Europe that partners with founders of SMEs in sectors with structural growth.
- **Focus sectors:** Healthcare, education, specialty manufacturing, consumer goods, and business services.
- **Geography:** Primarily the Czech Republic, Poland, and Croatia, with some activity in Slovakia and Slovenia.
- **Investment criteria:** €2m–5m equity tickets in minority or majority stakes, typically in profitable companies with at least €3m in revenue and a growth path.
- **Services:** Growth capital, acquisition support and market consolidation, ownership transition and capital restructuring, and management buy-outs and corporate spin-offs.
- **Diversity:** The firm actively seeks management teams co-led or co-owned by women.
- **Portfolio:** Pekarna Hrstić (Croatia, FMCG, 2026) and Clintrial (Czech Republic, healthcare, 2026). Earlier investments listed include JK Education, Premier Clinic, and Summalingua.
- **Team:** Emília Mamájová (Managing Partner & Co-Founder) and Marko Jojič (Partner & Co-Founder), plus an investment team, an advisory board, and an external investment committee.
- **Fund backing:** The European Investment Fund approved a €20 million investment in the EVERITA Fund in December 2024, under the InvestEU programme.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Several sentences mention Neulogy Ventures or the fund. Quotes are capped at 125 characters, so longer sentences are partly quoted and partly paraphrased.

**Page title:** "Neulogy Ventures | Slovak Investment Holding, a. s."

**Heading:** "Neulogy Ventures"

**Fund structure and manager:**
- "Slovak Investment Holding is an investor in a Luxembourg-based fund managed by Neulogy Ventures," The manager has full responsibility for the fund's management and investment strategy.
- "The fund comprises two investment compartments supporting start-ups and growth-oriented small and medium-sized enterprises" One of the two compartments also includes private investors.

**Investment period:**
- "The fund's investment period ran from 2014 to 2016."
- "During the investment period, capital was deployed to early-stage start-ups as well as SMEs" The investments targeted innovative projects and growth in the Slovak market.

**Current status:**
- "The fund is currently in its divestment period," The manager is gradually exiting investments and returning capital to investors.

**Not shown on the page:** fund size or amount, specific investment dates, individual portfolio company names, company ID, and publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""M3 Partners s.r.o." investícia kolo startup"

Links: [{"title":"Portfolio Companies","url":"https://seedtable.com/investors/m3-ventures"},{"title":"www.borel barbey","url":"https://www.borel-barbey.ch/?p=1768"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/m3-capital-partners"},{"title":"200402 1P1YFund E v1","url":"https://corporate.m3.com/en/ir/20200422_02/200402_1P1YFund_E_v1.pdf"},{"title":"M3 s.r.o., IČO: 10691391, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/10691391-m3-s-r-o"},{"title":"betadev.borel barbey","url":"https://betadev.borel-barbey.ch/?p=1768"},{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/companies/m_c_partners/portfolio/rounds"},{"title":"Startupy, které prošly českým StartupYardem, získaly během 3 měsíců rekordních 3,3 milionu EUR","url":"https://cc.cz/startupy-ktere-prosly-ceskym-startupyardem-ziskaly-behem-3-mesicu-rekordnich-33-milionu-eur/"},{"title":"Angels Partners logo","url":"https://angelspartners.com/firm/M3"},{"title":"m capital partners","url":"https://prod.actual.seedtable.com/investors/m-capital-partners"}]

I didn't find anything tying a company called "M3 Partners s.r.o." to a startup investment or funding round. The results only included a few loosely related entities.

- **Closest match:** A Prague company registered as "M3 s.r.o." (ID 10691391) has its seat at Heřmanova 597/61, 170 00 Praha - Holešovice, and its company ID is 10691391. Its incorporation date is 24 March 2021, and its share capital is 100,000 CZK. The register extract lists annual accounts and founding documents, but I didn't see any investment activity. The name differs from "M3 Partners s.r.o.," so I can't confirm they're the same entity.
- **M3 Groupe Holding SA (Switzerland):** One law firm's page says it invested CHF 2 million in the Lausanne based start-up Technis SA, along with an exclusive distribution agreement. This is a different company.
- **M3 Ventures (US):** This is described as a micro venture capital fund investing in early-stage apparel, lifestyle, fashion, and consumer companies.

To verify the Czech entity, I'd check the Czech business register (justice.cz or ARES) for "M3 Partners" and its IČO, or search Czech startup news sources. If you have the IČO or the name of a startup involved, I can search on that.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EVERITA Capital Pekarna Hrstić",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EVERITA Capital Summalingua JK Education Premier Clinic",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "GA Drilling first close $15M Nabors alfa8 Neulogy Ventures press release",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "StratifAI pre-seed Neulogy Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tilia Impact Ventures 2025 investice startup kolo",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "StratifAI pre-seed Neulogy Ventures"

Links: [{"title":"[REDACTED]","url":"https://sk.linkedin.com/in/christianmandl"},{"title":"cekan pavol multiplexdx 202409 inc persons people chief 2001 28559","url":"https://www.life-sciences-europe.com/person/cekan-pavol-multiplexdx-202409-inc-persons-people-chief-2001-28559.html"},{"title":"app.foundernest.com","url":"https://app.foundernest.com/public/space/7678/companies/10190350?page=11"},{"title":"Recently FundedEUR 1.5MTechnology, Information and Internet","url":"https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers"},{"title":"Funding Stage","url":"https://seedtable.com/companies/stratifai"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/stratifai-secures-12-5m-funding-round"},{"title":"Back to Stories","url":"https://aiworld.eu/story/stratifai-raises-125m-to-make-cancer-treatment-more-precise-with-ai"},{"title":"Major Investements for","url":"https://digitalhealth.tu-dresden.de/?p=13630"},{"title":"rocketlist.ai","url":"https://rocketlist.ai/companies/stratifai"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/stratifai"}]

Neulogy Ventures co-led StratifAI's €1.5 million pre-seed round, which was announced on September 2, 2024.

**The pre-seed round**
- Neulogy Ventures and MultiplexDX shared lead duties on the round. Debiopharm Innovation Fund, Arve Capital, and angel investor Christoph Haarburger also took part. The round was co-led by Neulogy Ventures and MultiplexDX, with participation from Debiopharm Innovation Fund, Arve Capital, as well as angel investor Christoph Haarburger.
- The company planned to use the capital for its technology, team expansion, and getting its digital oncology platform ready for the market. This pre-seed funding will be instrumental in furthering the development of StratifAI's cutting-edge technology, expanding its team of experts, and accelerating the market readiness of its digital oncology platform.
- The date appears as 9/2/24 in the press release citation (9/2/24). and as a September 2, 2024 pre-seed event in a Foundernest listing Pre-Seed, $1.66M, September 2, 2024.

**The company**
- Founded in 2023, StratifAI is at the forefront of digital innovation in the field of precision oncology. It was started in Dresden by Omar El Nahhas, Daniel Truhn, Jakob Nikolas Kather, and Firas Khader.
- Its main product is Polaris, an AI platform that analyzes large genetic and clinical datasets. By identifying biological signals linked to how patients react to specific drugs, the platform gives oncologists a clearer sense of which treatments are most likely to work best and why.

**Later funding**
- In September/October 2025, StratifAI raised €12.5 million. Picus Capital led that round, Alven co-led it, and existing investors including Debiopharm and Arve Capital also participated. StratifAI has secured € 12.5 
… [skrátené, 1120 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EVERITA Capital Summalingua JK Education Premier Clinic"

Links: [{"title":"Jakub Stracina","url":"https://cz.linkedin.com/in/jakubstracina"},{"title":"Marko Jojić","url":"https://sk.linkedin.com/in/markojojic"},{"title":"czech republic everita capital acquires majority stake in clintrial","url":"https://www.investorsinhealthcare.com/articles/category/news/czech-republic-everita-capital-acquires-majority-stake-in-clintrial/"},{"title":"Magdaléna Bednářová","url":"https://cz.linkedin.com/in/magdalena-bednarova"},{"title":"4154423 e4192951","url":"https://a-leads.co/company/4154423_e4192951"},{"title":"inauguration of pena business clinic in malang regency","url":"https://kemensos.go.id/en/inauguration-of-pena-business-clinic-in-malang-regency"},{"title":"Watch Atul Kapur explain why Everstone is betting big on Indonesia’s healthcare sector","url":"https://www.dealstreetasia.com/?p=275583"},{"title":"quadria acquires minority stake in indonesia s hermina","url":"https://www.theasset.com/article/43216/quadria-acquires-minority-stake-in-indonesia-s-hermina"},{"title":"About Angsamerah Institution","url":"https://www.landing.acicis.edu.au/?p=21003"}]

The search didn't return anything that mentions Summalingua, JK Education, or a "Premier Clinic" together with EVERITA Capital. The closest match is EVERITA's investment in Clintrial, a Czech clinical research company.

**The Clintrial deal**
- Investors in Healthcare reported that EVERITA, a growth investor in Central European small and mid-sized firms, took a controlling interest in Clintrial, a Prague clinical trial site. Czech-based Everita Capital a growth investor in Central European SMEs, has acquired a majority stake in Clintrial, a Prague-based clinical trial centre. The article's date isn't shown in the results.
- Dr. Zdeněk Šolle and his wife launched the company in 2005. It initially carried out clinical trials in the field of psychiatry. It later moved on to cover neurology and diabetology.
- The firm has enrolled more than 1,000 patients and contributed to over 100 Phase II and III trials. It has enrolled over 1,000 patients and contributed to more than 100 Phase II and III clinical trials.
- Under EVERITA, the company plans to add capacity, enter new therapeutic areas, and broaden its network of clients and providers. With Everita, Clintrial will look to its the next stage of growth.
- Tomas Brezina, who led Amgen's Czech operations for eight years, was appointed to strengthen leadership. With over 25 years in pharmaceuticals and biotech, including eight years as CEO of Amgen in the Czech Republic, he brings the industry expertise to drive the company's expansion.
- The deal also brought Rentea in as a new investor in the EVERITA Fund, and existing limited partners were offered co-investment opportunities. Happy to share our second EVERITA Capital investment! That post suggests Clintrial was the fund's second deal, following a bakery acquisition. Proud to com
… [skrátené, 790 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EVERITA Capital Pekarna Hrstić"

Links: [{"title":"EVERITA Capital","url":"https://www.tportal.hr/biznis/clanak/veliko-ulaganje-u-dalmaciji-splitska-pekarnica-dobila-strateskog-partnera-20260331"},{"title":"Marko Jojić","url":"https://sk.linkedin.com/in/markojojic"},{"title":"Magdaléna Bednářová","url":"https://cz.linkedin.com/in/magdalena-bednarova"},{"title":"Jakub Stracina","url":"https://cz.linkedin.com/in/jakubstracina"},{"title":"Na mojom synovi","url":"https://sk.linkedin.com/in/peter-solar-756b9b50"},{"title":"Kam zajít, co ochutnat a co stojí za pozornost","url":"https://www.newstream.cz/money/investorka-emilia-mamajova-v-private-equity-je-treba-byt-trpelivy"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/evita-jdoo/MMCW5GC"},{"title":"EVITA j.d.o.o. u stečaju","url":"https://www.companywall.hr/tvrtka/evita-jdoo-u-stecaju/MMHrRtLD"},{"title":"www.companywall.hr","url":"https://www.companywall.hr/tvrtka/evita-fast-food-jdoo/MM22JWBC"}]

EVERITA Capital, an investment fund, acquired a majority stake in Pekarna Hrstić, a bakery in Split, Croatia, in a deal reported in late March 2026.

**The deal**
- The fund's stake is 51%, and the founding couple, Nikola and Ana Mihaela Hrstić, stay on in management with the current team. Investicijski fond EVERITA Capital preuzeo je većinski udio u splitskoj Pekarni Hrstić, and the reporting says the owners remain involved in running the company.
- The money is earmarked for a new production plant and additional shops. Kapital koji fond ulaže bit će usmjeren u izgradnju novog proizvodnog pogona te otvaranje dodatnih prodajnih mjesta.
- A LinkedIn post describes this as the first investment of our fund.

**The bakery**
- The business has operated for more than 35 years, employs over 80 people, and had roughly €3 million in revenue in 2025 (Pekarna Hrstić posluje više od 35 godina, zapošljava više od 80 radnika te je u 2025. godini ostvarila oko tri milijuna eura prihoda.).
- It runs 12 of its own shops and, through wholesale, supplies around 100 sites of the Ribola and Studenac grocery chains (Tvrtka trenutačno ima 12 vlastitih prodajnih mjesta, dok kroz veleprodajni kanal opskrbljuje oko stotinu lokacija trgovačkih lanaca Ribola i Studenac.).
- Daily output is about 6,000 bakery items, including bread, pastries and cakes (Dnevno proizvede oko 6000 pekarskih proizvoda).

**The fund's rationale**
- Co-founder Emília Mamajová pointed to growth potential in a region with strong tourism traffic and said the fund plans to invest in both infrastructure and people (Partnerica i suosnivačica fonda Emília Mamajová poručila je da u tvrtki vide značajan potencijal za rast).
- A LinkedIn post says the firm recently closed its first fund and targets growth companies with turnover above €3 million in the Czech Republic, Poland and the Balkans (EVERITA Capital sa zameria na rastové firmy s obratom nad 3 milióny EUR).
- In a separate interview, Mamajová said typical
… [skrátené, 649 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "GA Drilling first close $15M Nabors alfa8 Neulogy Ventures press release"

Links: [{"title":"ThinkGeoEnergy – Geothermal News & Insights","url":"https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/?amp=1"},{"title":"1. Homepage","url":"https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/"},{"title":"www.thinkgeoenergy.com","url":"https://www.thinkgeoenergy.com/?p=60323"},{"title":"GA Drilling Secures $15M First Close from Nabors, alfa8, Underground Ventures, Neulogy Ventures and Thomas von Koch","url":"https://www.privsource.com/acquisitions/deal/YBSvjg"},{"title":"GA Drilling will work with Petrobras’ R&D center to roll out an autonomous drilling system. Photo via Getty Images","url":"https://energycapitalhtx.com/tag/nabors-industries"},{"title":"ga drilling","url":"https://bouncewatch.com/company/ga-drilling"},{"title":"collaboration entre ga drilling et petrobras pour des accords de forages","url":"https://energynews.pro/collaboration-entre-ga-drilling-et-petrobras-pour-des-accords-de-forages"},{"title":"ga drilling and petrobras collaborate on drilling agreements","url":"https://energynews.pro/ga-drilling-and-petrobras-collaborate-on-drilling-agreements"},{"title":"other 2025 07","url":"https://seedtable.com/companies/ga-drilling/funding-rounds/other-2025-07"},{"title":"ga drilling a s","url":"https://sih.sk/en/portfolio/ga-drilling-a-s"}]

The $15M first close is covered consistently in April 2024 trade press, but none of these results is GA Drilling's own press release, so these are secondary accounts.

**Timing and framing:** ThinkGeoEnergy's article is dated 18 April 2024 (Carlo Cariaga 18 Apr 2024). It describes the money as a first tranche that followed trial runs going well (after a series of successful tests, securing further investment to deliver deep geothermal faster and at deeper depths).

**Investors:** Nabors, a drilling rig and services provider, is one of the named backers. The others are Christian Oldendorff's newly formed family office alfa8, former EQT CEO Thomas von Koch, the recently launched geothermal fund Underground Ventures, and Slovakia's Neulogy Ventures (Investors include leading global drilling rig, services, and technology provider, Nabors, Christian Oldendorff's new Family Office, alfa8, the previous CEO of private equity firm EQT, Thomas von Koch, newly established geothermal fund Underground Ventures, and Slovakia-based, Neulogy Ventures.). EnergyCapital's account lists fewer names, leaving out alfa8 and von Koch (Investors included Houston-based oil and gas drilling contractor Nabors Industries, the newly established Underground Ventures geothermal investment fund, and Slovakian venture capital firm Neulogy Ventures.).

**Use of proceeds:** A PrivSource deal record dated 25 April 2024 says the funds will go toward commercializing the PLASMABIT drilling systems and supporting wider ro
… [skrátené, 1076 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tilia Impact Ventures 2025 investice startup kolo"

Links: [{"title":"Tilia Impact Ventures","url":"https://cc.cz/tag/tilia-impact-ventures/"},{"title":"moje investice 2025 co letos potesilo vlivne zeny ceskeho byznysu","url":"https://forbes.cz/moje-investice-2025-co-letos-potesilo-vlivne-zeny-ceskeho-byznysu/"},{"title":"Investování s dopadem je budoucnost, věří Petr Vítek z Tilia Impact Ventures. Postupně nahrazuje klasické investice","url":"https://cc.cz/investovani-s-dopadem-je-budoucnost-veri-petr-vitek-z-tilia-ventures-postupne-nahrazuje-klasicke-investice/"},{"title":"[REDACTED]á a Petr Vítek mají nový fond: Investice musí mít i společenský dopad. Máme na ně 43 milionů korun","url":"https://cc.cz/silke-horakova-a-petr-vitek-z-noveho-tilia-impact-ventures-chybel-nam-rizikovy-kapital-pro-socialni-inovace/"},{"title":"[REDACTED]á a Petr Vítek posílají miliony korun do startupu MIWA, který z obchodů odstraňuje jednorázové plasty","url":"https://cc.cz/silke-horakova-a-petr-vitek-posilaji-miliony-korun-do-startupu-miwa-ktery-z-obchodu-odstranuje-jednorazove-plasty/"},{"title":"tilia impact ventures","url":"https://impacteurope.net/members/tilia-impact-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/tilia-impact-ventures"},{"title":"podim.org","url":"https://podim.org/?p=34041"},{"title":"Tilia Impact Ventures","url":"https://capboard.io/en/investor/tilia-impact-ventures"}]

**Tilia Impact Ventures v roce 2025: uzavřený druhý fond a nové investice**

- **Druhý fond:** [REDACTED]á hodnotila rok 2025 jako plný pozitivních momentů, mezi nimi uzavření druhého fondu o objemu 30 milionů eur V Tilia Impact Ventures jsme úspěšně uzavřeli náš druhý fond ve výši třiceti milionů eur. Profil na platformě WaveUp uvádí jinou částku: druhé fondové vozidlo Tilia II vybralo 32 milionů eur a ke konci roku 2025 fond podpořil zhruba 15 firem. Zdroje se tedy liší o 2 miliony eur.

- **Investice zmiňované v roce 2025:** Horáková podle Forbes.cz uvedla, že fond dál investuje do technologických firem se silným sociálním nebo environmentálním dopadem a globálními ambicemi, a jako příklady uvedla české DeltaGreen, rakouský Biocraft a ukrajinský LetsData (pokračujeme v investicích do technologických startupů s výrazným sociálním či environmentálním dopadem a globálními ambicemi – například českého DeltaGreen, rakouského Biocraft nebo ukrajinského LetsData).

- **DeltaGreen:** Do prvního investičního kola české firmy, která dodává elektřinu domácnostem, se zapojily desítky milionů korun. Investory jsou Tilia a Credo. Z úryvku není jasné, kdy kolo proběhlo.

- **MIWA:** Fond do startupu, který z obchodů odstraňuje jednorázové plasty, vstoupil konvertibilní půjčkou ve výši nižších jednotek milionů korun. Tilia zde figuruje jako první institucionální investor a chce přilákat další zahraniční impaktní investory. Datum v úryvku uvedeno není.

- **FaceUp:** Mezi investory českého startupu FaceUp je kromě Lighthouse Ven
… [skrátené, 1214 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/moje-investice-2025-co-letos-potesilo-vlivne-zeny-ceskeho-byznysu/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tilia, Tilia Impact Ventures, [REDACTED]á, the second fund, DeltaGreen, Biocraft, LetsData, or the fund size, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tilia.vc/",
  "prompt": "Return word-for-word, without summarising or translating, the sentence stating the initial investment ticket size in euros, the sentence stating the office or city where the team is based, and the sentence stating the investment stage. Also return the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Neulogy Ventures, the investors, the first close amount, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://digitalhealth.tu-dresden.de/?p=13630",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions StratifAI, Neulogy Ventures, the pre-seed round, the investors, the amount, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "GreenWay Neulogy Ventures growth investice 2025",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- **Initial investment ticket:** "0.3 - 1.2m EUR initial ticket"
- **Team location:** "Drtinova 557/10, 150 00 Prague" and "Czech Republic"
- **Investment stage:** "Early stage"
- **Publication date:** Not shown on the page. The only dates are a copyright notice ("© 2018 - 2024") and image upload paths.

The ticket size and stage appear as page headings rather than full sentences, so I've quoted them as they appear.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** The article is dated "18 April 2024."

**First close:** GA Drilling announced "the first close of $15 million in financing," following a series of successful tests.

**Investors:** The article names five investors, which I've listed in my own words: Nabors, the alfa8 family office of Christian Oldendorff, former EQT CEO Thomas von Koch, Underground Ventures, and Neulogy Ventures. The source describes Nabors as a "leading global drilling rig, services, and technology provider."

**Neulogy Ventures:** The article describes it as "Slovakia-based, Neulogy Ventures" and lists it among the investors.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't mention Neulogy Ventures or a pre-seed round, so I can't provide sentences about either.

**Sentences mentioning StratifAI, investors, and amount:**

- "Berlin-based StratifAI secured €12.5 million in a financing round led by Picus Capital and Alven."
- The headline says StratifAI and Cancilico raised substantial investor funding. (Paraphrased, since the full sentence exceeds the 125-character quote limit.)
- The CEO's quote refers to "our investors" who bring expertise in rapid execution and global scaling. (Paraphrased for length.)

**Publication date:** The article's own publication date doesn't appear in the content. The only timestamp, "18 Sep at 3:26 pm," belongs to a different article in the "More News" section.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The web page content you provided contains only a title, with no body text:

"Moje investice 2025. Co letos potěšilo vlivné ženy českého byznysu? | Forbes"

It contains no sentences mentioning Tilia, Tilia Impact Ventures, [REDACTED]á, the second fund, DeltaGreen, Biocraft, LetsData, or a fund size. It also shows no publication date. If you share the full article text, I can extract the matching sentences and the date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "GreenWay Neulogy Ventures growth investice 2025"

Links: [{"title":"e mobility pioneer greenway raises 85 million euros to grow company and expand network","url":"https://ceenergynews.com/transport/e-mobility-pioneer-greenway-raises-85-million-euros-to-grow-company-and-expand-network/"},{"title":"Investícia vo výške 85 miliónov EUR do rastu siete pre priekopníka GreenWay","url":"https://touchit.sk/investicia-vo-vyske-85-milionov-eur-do-rastu-siete-a-dalsiu-expanziu-pre-priekopnika-e-mobility-spolocnost-greenway/401298/"},{"title":"GreenWay Secures $158 Million Green Debt Deal To Expand EV Charging","url":"https://esgnews.com/greenway-secures-158-million-green-debt-deal-to-expand-ev-charging/"},{"title":"GreenWay - Your partner in electromobility in Central and Eastern Europe Your EV charging provider","url":"https://greenwaynetwork.com/greenway-secures-historic-green-debt-financing-up-to-e138-million-to-continue-leading-ev-charging-expansion/"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/greenway-poland/financials"},{"title":"Select your local site for products and services by region","url":"https://www.im.natixis.com/en-gb/about/investment-manager-news/2025/greenway-welcomes-new-capital-from-mirova-a-leading-investor-in-energy-transition-infrastructure"},{"title":"series c 2025 03","url":"https://seedtable.com/companies/greenway/funding-rounds/series-c-2025-03"},{"title":"GreenWay collects €85 million from investors","url":"https://electrive.com/2022/02/23/greenway-collects-e85-million-from-investors"},{"title":"operator stacji ladowania pozyskal inwestora","url":"https://www.gramwzielone.pl/auto-ekologiczne/20307254/operator-stacji-ladowania-pozyskal-inwestora"},{"title":"GreenWay secures €138m green debt financing to expand EV charging network","url":"https://esgpost.com/greenway-secures-e138m-green-debt-financing-to-expand-ev-charging-network/"}]

I read "investice" as a typo for "investment." The main 2025 development is a Mirova equity deal. Neulogy Ventures appears in the results as an existing shareholder, not as the lead investor in that round, and I didn't find a disclosed Neulogy-specific amount for 2025.

**2025: Mirova equity investment**
- Natixis's investment-manager news page dates the announcement to April 1, 2025. It says Mirova, an affiliate of Natixis Investment Managers, made an equity investment of more than €50 million and became GreenWay Holding's largest shareholder. GreenWay, a pioneering company in the electric vehicle charging industry, is pleased to announce a significant new investment from Mirova, an affiliate of Natixis Investment Managers, dedicated to sustainable investing. With an equity investment of more than 50 million euros, Mirova will become the largest shareholder in GreenWay Holding.
- Data aggregators date the round to March 17, 2025. Seedtable lists it as a Series C round of 54.0M USD with Mirova as lead investor, and CB Insights records a $54.52M ro
… [skrátené, 1584 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions StratifAI, Neulogy Ventures, MultiplexDX, the pre-seed round, the amount, and the article's publication date exactly as shown."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Sentences mentioning StratifAI, the pre-seed round, the amount, and the date**

1. Title: "StratifAI Secures $1.5 Million in Pre-Seed Funding to Revolutionize Precision Oncology with AI-Driven Biomarkers"
2. Article opening (truncated to the 125-character limit): "StratifAI, a pioneering force in the field of precision oncology, has successfully raised $1.5 million"
3. Date: "Published September 2, 2024"
4. Pre-seed round: "Companies that recently closed a Pre-seed round."
5. Amount, as a label rather than a sentence: "Total funding" is listed as "€1.5M"

**Neulogy Ventures and MultiplexDX:** The page has no sentences about these two. They appear only as names in the "Investors" list, where Neulogy Ventures is listed first and MultiplexDX International second.

**Note:** The article body says "$1.5 million," but the header and company overview say "€1.5M," so the currency is inconsistent on the page.
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b07.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b07.json",
  "content": "[\n  {\n    \"candidate_id\": \"C034\",\n    \"website\": \"https://www.tilia.vc\",\n    \"identity\": [],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Prague\",\n      \"source_url\": \"https://www.tilia.vc/\",\n      \"quote\": \"Drtinova 557/10, 150 00 Prague\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"vc\"],\n      \"value_text\": \"Venture kapitálový fond\",\n      \"source_url\": \"https://www.newstream.cz/money/fond-silke-horakove-investoval-do-modni-platformy\",\n      \"quote\": \"Venture kapitálový fond Tilia investorky [REDACTED]é a partnerů bude mít brzy mladšího bratra, Tilia 2.\",\n      \"published_date\": \"2023-10-18\",\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"Datlab\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Datlab\",\n        \"source_url\": \"https://cc.cz/silke-horakova-a-petr-vitek-posilaji-miliony-korun-do-startupu-miwa-ktery-z-obchodu-odstranuje-jednorazove-plasty/\",\n        \"quote\": \"Jako svou první investici si Horáková s Vítkem vybrali projekt Datlab.\",\n        \"published_date\": \"2019-10-08\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"MIWA Technologies\", \"date\": \"2019-10-08\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"MIWA Technologies\",\n        \"source_url\": \"https://cc.cz/silke-horakova-a-petr-vitek-posilaji-miliony-korun-do-startupu-miwa-ktery-z-obchodu-odstranuje-jednorazove-plasty/\",\n        \"quote\": \"Druhou investicí v portfoliu Tilia Impact Ventures se nyní stává společnost MIWA Technologies.\",\n        \"published_date\": \"2019-10-08\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"NOLD\", \"date\": \"2023-10-18\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"bulharskou platformu NOLD\",\n        \"source_url\": \"https://www.newstream.cz/money/fond-silke-horakove-investoval-do-modni-platformy\",\n        \"quote\": \"Impactový fond Tilia Impact Ventures, který založila investorka a spolumajitelka vydavatelství Albatros [REDACTED]á, má nový přírůstek, bulharskou platformu NOLD.\",\n        \"published_date\": \"2023-10-18\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Munch\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"maďarská Munch\",\n        \"source_url\": \"https://www.newstream.cz/money/fond-silke-horakove-investoval-do-modni-platformy\",\n        \"quote\": \"Její první fond uskutečnil různé impaktové investice: od boje proti plýtvání potravinami (maďarská Munch) přes zlepšení recyklace materiálů (česká Cyrkl) až po boj proti korupci ve veřejných výdajích (česká Datlab) a umožnění alternativních modelů předškolního vzdělávání (polská The Village).\",\n        \"published_date\": \"2023-10-18\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Cyrkl\", \"date\": null, \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"česká Cyrkl\",\n        \"source_url\": \"https://www.newstream.cz/money/fond-silke-horakove-investoval-do-modni-platformy\",\n        \"quote\": \"Její první fond uskutečnil různé impaktové investice: od boje proti plýtvání potravinami (maďarská Munch) přes zlepšení recyklace materiálů (česká Cyrkl) až po boj proti korupci ve veřejných výdajích (česká Datlab) a umožnění alternativních modelů předškolního vzdělávání (polská The Village).\",\n        \"published_date\": \"2023-10-18\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"The Village\", \"date\": null
… [skrátené, 14065 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b07.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b07 done. Output: C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b07.json\n\n- C034 Tilia Impact Ventures: vc, 6 investments, no early exit. Doubtful: no portfolio page found, latest verified deal 2023, Tilia 2 size unverified, identity not confirmed.\n- C017 EVERITA Capital: pe, 2 investments, no early exit. Doubtful: IČO not verified verbatim, sectors and stages inferred, fund size not stated (EIF 20M commitment not used as size).\n- C099 Neulogy Ventures: vc, 8 investments, no early exit. Doubtful: GA Drilling and StratifAI quotes are partial (investor name or deal headline), portfolio entries are name-only quotes.\n- C117 M3 Partners: early_exit no_investment_found after 5 searches, nothing matching.\n- C163 Caesar VC: early_exit foreign_hq (Berlin per caesar.vc).\n\nTilia and EVERITA pages contained text addressed to AI tools; ignored."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

# Subagent: Evidence v3 wave2 batch 12 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 21:09:28

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v3") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b12.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b12.json

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w2_b12.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w2_b12.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C096",
4	    "name": "Eterus Capital",
5	    "other_names": [],
6	    "known_website": null,
7	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Eterus Capital, a. s., IČO 44193025"
8	  },
9	  {
10	    "candidate_id": "C197",
11	    "name": "Rockaway Ventures",
12	    "other_names": [
13	      "Rockaway Ventures Fund SICAV a.s., podfond I"
14	    ],
15	    "known_website": null,
16	    "registry_hint": "possible registry match (unconfirmed, may be a different company): , IČO 75163225"
17	  },
18	  {
19	    "candidate_id": "C077",
20	    "name": "QI investiční společnost, a.s.",
21	    "other_names": [],
22	    "known_website": "www.qiis.cz",
23	    "registry_hint": null
24	  },
25	  {
26	    "candidate_id": "C087",
27	    "name": "TMF Czech, a.s.",
28	    "other_names": [],
29	    "known_website": "www.tmf-group.com",
30	    "registry_hint": "possible registry match (unconfirmed, may be a different company): TMF Czech, a.s., IČO 24705101"
31	  },
32	  {
33	    "candidate_id": "C204",
34	    "name": "CEC Capital SK, s.r.o.",
35	    "other_names": [],
36	    "known_website": null,
37	    "registry_hint": "possible registry match (unconfirmed, may be a different company): , IČO 35897635"
38	  }
39	]
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
  "query": "Eterus Capital investiční společnost",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Rockaway Ventures investice",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.qiis.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions QI, investments, portfolio, fund size, ticket, the team or office address (kontakt, sídlo, adresa), and the page's publication date if shown. Also return the legal name and IČO if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tmf-group.com/cs-cz/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions TMF Czech, investments, fund management, portfolio, the Czech office address, and the legal name and IČO if shown. Include the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "CEC Capital SK s.r.o. investícia",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Hostname/IP does not match certificate's altnames: Host: www.qiis.cz. is not in the cert's altnames: DNS:*.nameserver.sk, DNS:nameserver.sk
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
Web search results for query: "Eterus Capital investiční společnost"

Links: [{"title":"Go to deals","url":"https://www.oaklins.com/il/en/deals/110584/"},{"title":"Go to deals","url":"https://www.oaklins.com/se/en/deals/110584/"},{"title":"Go to deals","url":"https://www.oaklins.com/ma/en/deals/110584/"},{"title":"Go to deals","url":"https://www.oaklins.com/ie/en/deals/110584/"},{"title":"Go to deals","url":"https://www.oaklins.com/sg/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/pt/pt-pt/deals/110583/"},{"title":"Zu den Deals","url":"https://www.oaklins.com/at/de/deals/110583/"},{"title":"Ir a las transacciones","url":"https://oaklins.com/co/es/deals/110584"},{"title":"Go to deals","url":"https://www.oaklins.com/fr/en/deals/110583/"},{"title":"Private Equity","url":"https://altss.com/profile/eterus-capital"}]

I didn't find a Czech-registered "investiční společnost" under the name Eterus Capital. The results describe a private equity firm based in Slovakia. Since "investiční společnost" is the Czech legal term for an investment company, it's worth checking whether the firm has a Czech entity.

**What the results say about the firm:**
- It dates to 2008 and invests in small and mid-sized businesses with proven models and growth potential. Eterus Capital is a private equity fund founded in 2008, specializing in supporting small and medium-sized enterprises with proven business models and growth potential.
- Its typical deal is a minority stake, which leaves management with the original owners. The fund focuses on minority investments, ensuring management control remains with the original shareholders.
- Scale: it has reportedly put roughly €40 million into more than 20 companies. Over the years, Eterus Capital has provided more than US$41 million (€40 million) in funding to over 20 companies.
- Portfolio names include Sygic, HOPIN, eyerim, Saneca Pharmaceuticals, Groupsolver and MTBIKER. Its portfolio includes prominent brands such as Sygic, HOPIN, eyerim, Saneca Pharmaceuticals, Groupsolver and MTBIKER.
- Location: one profile places it primarily from Bratislava, with a portfolio that concentrates on Slovakia and the broader Central and Eastern European region.

**Recent activity:**
- In August 2024 it took a majority stake in EC Pharmacies, a Slovak pharmacy consolidation platform it set up with Ethernum Capital. Eterus Capital has acquired a majority stake in EC Pharmacies, a consolidation platform established in partnership with Ethernum Capital. This sits oddly beside the firm's minority-stake focus.
- In May 2024 it backed the Dr. Martin dental clinic network in Slovakia, alongside Ethernum. Dr. Martin Dental Clinic, a leading network of dental clinics in Slovakia, has received a significant investment from Eterus Capital and Ethernum Capital to support its expansion across the country.

**Caveats:** The deal details come from Oaklins, an M&A advisory firm, and the firm profile comes from Altss, a third-party aggre
… [skrátené, 485 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "CEC Capital SK s.r.o. investícia"

Links: [{"title":"realassets.ipe.com","url":"https://realassets.ipe.com/propertyeu/cec-capital-relaunches-as-mint-investments/10125356.article"},{"title":"cec management","url":"https://www.cbinsights.com/investor/cec-management"},{"title":"Investors Count","url":"https://www.cbinsights.com/company/cec-3/financials"},{"title":"Investors Count","url":"https://www.cbinsights.com/company/cec-1/financials"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/clp-health-fund"},{"title":"legalbusinessonline.com","url":"https://china.legalbusinessonline.com/node/70444"},{"title":"CEFC Europe significantly strengthened its capital","url":"https://www.zdas.com/files/uploads/2018/03/CEFC-Europe-significantly-strengthened-its-capital.pdf"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/cec-global"},{"title":"cec capital","url":"https://prospeo.io/c/cec-capital"}]

Links: [{"title":"CITIC Group dokončila převzetí největšího čínského investora v Česku CEFC","url":"https://www.e15.cz/domaci/citic-group-dokoncila-prevzeti-nejvetsiho-cinskeho-investora-v-cesku-cefc-1357777"},{"title":"CEFC Europe significantly strengthened its capital","url":"https://www.zdas.com/files/uploads/2018/03/CEFC-Europe-significantly-strengthened-its-capital.pdf"},{"title":"Evropská pobočka CEFC se sídlem v Praze významně posílila kapitál. Dává najevo stabilitu, tvrdí analytik","url":"https://www.e15.cz/zahranicni/evropska-pobocka-cefc-se-sidlem-v-praze-vyznamne-posilila-kapital-dava-najevo-stabilitu-tvrdi-analytik-1344325"},{"title":"top of page","url":"https://www.symsite.sk/single-post/2018/06/05/poštová-banka-financed-cefc-of-china"},{"title":"Hrdá ze CEFC: Chceme vytvořit investiční fondy pro střední Evropu","url":"https://www.e15.cz/domaci/hrda-ze-cefc-chceme-vytvorit-investicni-fondy-pro-stredni-evropu-1282253"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=95141"},{"title":"Společnost CITIC Group převzala CEFC Europe, největšího čínského investora u nás","url":"https://www.echo24.cz/a/SgMBb/spolecnost-citic-group-prevzala-cefc-europe-nejvetsiho-cinskeho-investora-u-nas"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/jt-private-investments-nepriatelsky-prev/325797-clanok.html"},{"title":"ŽĎAS TZ CEFC posílení kapitálu","url":"https://www.zdas.com/files/uploads/2018/03/ŽĎAS_TZ_CEFC_posílení_kapitálu.pdf"}]

I couldn't find any source about a company called CEC Capital SK s.r.o. or an investment it made. I ran one English search and one Slovak-language search, and neither returned a registry entry, news item, or press release for that entity.

The closest matches are about other companies:

- **A Central European real estate group.** A trade publication reports that a firm operating under the name CEC Capital is rebranding as Mint Investments
… [skrátené, 1291 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Rockaway Ventures investice"

Links: [{"title":"Návrat Rockaway do světa startupových investic aneb Přehled všech dubnových dealů a transakcí","url":"https://cc.cz/navrat-rockaway-do-sveta-startupovych-investic-aneb-prehled-vsech-dubnovych-dealu-a-transakci/"},{"title":"havrlant spousti novy miliardovy fond podpori digitalizacni projekty","url":"https://www.newstream.cz/money/havrlant-spousti-novy-miliardovy-fond-podpori-digitalizacni-projekty"},{"title":"Jakub Havrlant přichází s novým investičním fondem. Rockaway s ním chce do startupů poslat 2,5 miliardy korun","url":"https://cc.cz/jakub-havrlant-prichazi-s-novym-investicnim-fondem-rockaway-s-nim-chce-do-startupu-poslat-25-miliardy-korun/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/company/rockaway-capital"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/rockaway-group/"},{"title":"Do českého Rockaway míří Viktor Fischer","url":"https://cc.cz/ceske-rockaway-hlasi-novou-posilu-v-podobe-viktora-fischera/"},{"title":"prague based rockaway ventures closes second fund at nearly 55m","url":"https://startuphub.unwe.bg/bg/news/64237/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html"},{"title":"prague based rockaway ventures closes second fund at nearly 55m","url":"https://startuphub.unwe.bg/bg/news/64138/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html"},{"title":"[REDACTED]","url":"https://forbes.cz/lists/zeny23/andrea-lauren/"}]

**Rockaway Ventures** is the startup-investment arm of the Czech Rockaway group, which is tied to Jakub Havrlant and Rockaway Capital.

**Background**
- Rockaway Ventures began its journey in 2014, initially investing without a formal structure and supporting early Czech startups like Productboard and Storyous.
- The Czech group is backed by billionaires Daniel Křetínský and Patrik Tkáč, alongside founder Jakub Havrlant.

**Funds and strategy**
- The current fund had an original goal of 100 million euros, or 2.5 billion crowns. The fund reported that it had raised about a quarter of that target in its first round.
- Its second fund, Rockaway Ventures II, closed at nearly €55 million. It targets late-seed and Series A tech startups, focusing on sectors such as energy, defense, and dual-use technologies.
- Geographically, 60% of investments are planned for startups in CEE, while the remaining 40% will target Western Europe and diaspora-led startups from Czechia and nearby countries now operating in the US.
- About 25% of the current fund's capital comes from its parent company, Rockaway Capital, with the rest coming mainly from Czech private investors.
- The fund can invest up to 15 million euros in a single startup, including through follow-on investments.

**Notable portfolio companies**
- Productboard, Brand Embassy, Gjirafa and Storyous are among the names the group has backed. Bileto and SQLdep are also cited as portfolio companies.
- A recent investme
… [skrátené, 1204 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://eterus.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Eterus, the team, portfolio companies, investments, fund size, the minimum or maximum investment size, the office address, and the page's publication date if shown. Also return the legal name and company ID (IČO or ICO) if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://qiis.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions QI, investments, portfolio, fund size, the funds it manages, the office address (kontakt, sídlo, adresa), and the legal name and IČO if shown. Include the publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Rockaway Ventures portfolio startup seed round 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"TMF Czech\" a.s. fond investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Hostname/IP does not match certificate's altnames: Host: qiis.cz. is not in the cert's altnames: DNS:*.nameserver.sk, DNS:nameserver.sk
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://eterus.com
    Redirect URL (from the server's Location header — server-supplied, not verified): https://forsale.godaddy.com/forsale/eterus.com?utm_source=TDFS_BINNS2&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-binns2_base&traffic_type=TDFS_BINNS2&traffic_id=binns2&
    Status: 307 Temporary Redirect

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://forsale.godaddy.com/forsale/eterus.com?utm_source=TDFS_BINNS2&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-binns2_base&traffic_type=TDFS_BINNS2&traffic_id=binns2&"
    - prompt: "Return word-for-word, without summarising or translating, every sentence that mentions Eterus, the team, portfolio companies, investments, fund size, the minimum or maximum investment size, the office address, and the page's publication date if shown. Also return the legal name and company ID (IČO or ICO) if shown."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""TMF Czech" a.s. fond investice"

Links: [{"title":"TMF Assets a.s., v likvidaci - obchodní rejstřík, úplný výpis","url":"https://rejstrik-firem.kurzy.cz/26485583/"},{"title":"Original title:","url":"https://invenio.nusl.cz/record/11977?ln=en"},{"title":"Regionální analýza aktiv podílových fondů v České republice","url":"https://dspace.cuni.cz/handle/20.500.11956/54240"},{"title":"Analýza a komparace výkonnosti fondů kolektivního investování v České republice","url":"https://katalog.muni.cz/Record/MUB01000683327/Details"},{"title":"Organizační formy investičních fondů","url":"https://dspace.cuni.cz/handle/20.500.11956/84325"},{"title":"Role of investment companies and funds in czech capital market","url":"https://vskp.vse.cz/english/16004"},{"title":"czech investment market insights","url":"https://rcm.at/at-en/global/cee-am-radar/czech-investment-market-insights"},{"title":"Investiční fondy, společnosti a kolektivní investování v České republice – Bc. Kateřina Jemelková","url":"https://theses.cz/id/8c8a6v?lang=en"},{"title":"Investování do garantovaných a zajištěných fondů v nabídce českých bank","url":"https://dspace.cuni.cz/handle/20.500.11956/170307"}]

Links: [{"title":"czech investment market insights","url":"https://rcm.at/at-en/global/cee-am-radar/czech-investment-market-insights"},{"title":"TMF Assets a.s., v likvidaci - obchodní rejstřík, úplný výpis","url":"https://rejstrik-firem.kurzy.cz/26485583/"},{"title":"Original title:","url":"https://invenio.nusl.cz/record/11977?ln=en"},{"title":"Role of investment companies and funds in czech capital market","url":"https://vskp.vse.cz/english/16004"},{"title":"www.privatebankerinternational.com","url":"https://www.privatebankerinternational.com/?p=23580"},{"title":"Alternativní investiční fondy","url":"https://dspace.cuni.cz/handle/20.500.11956/151196"},{"title":"Peter Kozdon","url":"https://cz.linkedin.com/in/peterkozdon"},{"title":"Organizační formy investičních fondů","url":"https://dspace.cuni.cz/handle/20.500.11956/84325"},{"title":"Kolektivní investování ve světle nového zákona o investičních společnostech a investičních fondech","url":"https://dspace.cuni.cz/handle/20.500.11956/62865"},{"title":"jt asset management has transformed into jt investicn spolecnost","url":"https://www.privatebankerinternational.com/uncategorized/jt-asset-management-has-transformed-into-jt-investicn-spolecnost/"}]

I didn't find any source describing a company called "TMF Czech, a.s." as an investment fund or investment company. Two searches returned mostly general material on Czech collective investing, plus a few unrelated fund managers.

The closest match is TMF Assets a.s., though it may not be what you're looking for. The commercial register extract shows it as a joint-stock company that was set up in late 2001 and is now in liquidation. It lists a 2 million CZK registered capital, a Prague 2 address, and company ID (IČO) 26485583, and it records the company's deletion in Oc
… [skrátené, 912 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Rockaway Ventures portfolio startup seed round 2025"

Links: [{"title":"Back to Rockaway Ventures","url":"https://seedtable.com/investors/rockaway-ventures/portfolio"},{"title":"prague based rockaway ventures closes second fund at nearly 55m","url":"https://startuphub.unwe.bg/bg/news/64138/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund"},{"title":"prague based rockaway ventures closes second fund at nearly 55m","url":"https://startuphub.unwe.bg/bg/news/64237/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html"},{"title":"Rockaway Ventures favicon","url":"https://raising.fi/company/rockawayventures"},{"title":"Back to Rockaway Capital","url":"https://seedtable.com/investors/rockaway-capital/portfolio"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/vc-of-the-month-rockaway-ventures"},{"title":"Návrat Rockaway do světa startupových investic aneb Přehled všech dubnových dealů a transakcí","url":"https://cc.cz/navrat-rockaway-do-sveta-startupovych-investic-aneb-prehled-vsech-dubnovych-dealu-a-transakci/"},{"title":"www.startbase.de","url":"https://www.startbase.de/organization/limehome/"},{"title":"Rockaway Ventures asegura 55 millones para startups emergentes","url":"https://ecosistemastartup.com/?p=33860"}]

The only 2025 seed round I could confirm in these results is Filuta AI, a Prague-based gaming company. Seedtable lists its seed-stage entry on 25 June 2025, with about $4.2M raised in total Filuta AI | Gaming | Seed | 1 | 25 Jun 2025 | 25 Jun 2025 | 4.2M USD. That comes from a single aggregator, so I'd check it against Crunchbase or the company itself.

Several other results point to why seed deals may be rare for this firm:

- **Fund focus:** The fund closed its second vehicle at nearly €55 million in May 2025, aimed at late-seed and Series A tech companies Rockaway Ventures closed its second fund at nearly €55 million to back late-seed and Series A tech startups.
- **Check sizes:** One profile lists an investment ticket of €0.5–2M and a stage range of seed to Series A Investment ticket: 0.5-2m. Company stage: Seed to Series A.
- **Conflicting stage descriptions:** Another Vestbee piece says the fund supports startups from pre-seed through growth stages The fund supports startups from pre-seed to growth stages., so the sources don't fully agree on its stage focus.
- **Portfolio size:** At the May 2025 announcement, eleven companies had received investment from the fund Rockaway Ventures Fund II has invested in 11 companies to date..

Two other items I'd leave out of a 2025 seed list:

- Seedtable also shows a New York defense company that raised a Series A on 22 October 2025, with $12.1M raised in total. That's not a seed round.
- Raising.fi shows the €55M fund close as a $55 million "Total Funding" figure for Rockaway Ventures. That's the fund itse
… [skrátené, 461 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Eterus Capital správcovská spoločnosť portfólio o nás",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "QI investiční společnost a.s. fondy",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://vestbee.com/insights/articles/vc-of-the-month-rockaway-ventures",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Rockaway Ventures, its investments, portfolio companies, fund size, check size or ticket, stage, office location, and the article's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "CEC Capital Slovensko s.r.o. fond investuje startup",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce every sentence word-for-word. Quotes are capped at 125 characters, and text outside quotation marks must be my own wording. Below are the relevant excerpts, quoted where they fit under the limit and paraphrased elsewhere.

**Fund overview**
- Rockaway Ventures is a venture capital fund under the Rockaway Capital investment group. It backs companies in Europe that are modernizing traditional industries with next-generation technology, especially AI.
- Geography: Europe.
- Stage: Seed to Series A. The firm works with late-seed and Series A founders in Europe and among the European diaspora in the US.
- Preferred industries: "Preferred industries: B2B software, E-commerce, Travel & Hospitality, Industrial, Energy, Defense & Dual-Use"
- Investment ticket: €0.5–2 million.
- Product type: software, with hardware occasionally.
- Product stage: a functioning product, with early traction in revenues.

**Portfolio**
- "Among the most successful investments by Rockaway Ventures are global platforms such as Productboard and Gjirafa."
- Apaleo is a cloud-native hotel management platform used by brands such as CitizenM and EasyHotels. "Other firms include Apaleo, a cloud-native hotel management platform"
- Spotawheel is a disruptor in the car leasing industry.
- The article highlights Apaleo and Gjirafa as top performers, citing significant market traction in their sectors.

**Support model**
- "At Rockaway Ventures, for example, we provide access to infrastructure and expertise typically available"
- The firm also says it invests at a level that lets it act as an active partner and reserves capital for follow-on rounds.

**Not stated in the article:** fund size and office location.

**Publication date:** July 8, 2025.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "CEC Capital Slovensko s.r.o. fond investuje startup"

Links: [{"title":"Venture capital in the Czech Republic","url":"https://en.wikipedia.org/wiki/Venture_capital_in_the_Czech_Republic"},{"title":"What we do","url":"https://eif.org/what_we_do/resources/jeremie/news/2014/slovakia_vc.htm?lang=-en"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"V Česku vytvoria nový fond na podporu startupov s kapitálom 2,3 miliardy korún","url":"https://www.podnikajte.sk/investor/cesko-fond-startupy"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=6"},{"title":"Credo ventures","url":"https://www.podnikajte.sk/temy/credo-ventures"},{"title":"financovanie podnikania","url":"https://www.podnikajte.sk/temy/financovanie-podnikania?page=17"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=5"},{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"}]

I couldn't find anything about a company called CEC Capital Slovensko s.r.o. or a fund it runs, so I can't confirm whether it invests in startups. The results did cover other funds active in Slovakia and Central Europe:

- **Slovenská spořitelna (Slovak arm of Erste):** The bank has set aside five million euros for the first phase of startup support in Slovakia, extending the Czech Seed Starter program. Pět milionů eur, tedy v přepočtu více než 123 milionů korun, si připravila Slovenská spořitelna na první fázi podpory startupů na Slovensku. Tam se totiž právě rozšiřuje program Seed Starter. The program's head said Slovakia had lacked a seed-stage incubation and venture program focused on tech startups (Jsem rád, že je to právě u našich sousedů na Slovensku, kde dosud CVC a inkubační program zaměřující se na technologické startupy v seed fázi chyběl).
- **Credo Ventures:** This Prague firm podporuje technologické startupy zo strednej a juhovýchodnej Európy through its venture funds. Its Credo Stage 2 fund targets Central Europe and je v porovnaní s prvým fondom Credo Stage 1 dvojnásobná – až 34 miliónov eur.
- **J&T Ventures:** The fund of J&T Bank made its first investments in startups, including FetView (medical documentation) and ICE Gateway (Smart City technology).
- **Zero One Hundred:** Its second, larger fund focuses on early-stage companies ranging from pre-seed to series A, and a portion of the funds will be invested in venture capital funds operating in the Central European region.

Several of these items don't show dates, so check how current they are before relying on them.

To learn about CEC Capital Slovensko, I'd check:
- The Slovak Business Register (orsr.sk) for the company's registration, legal form, and stated business purpose.
- The Nati
… [skrátené, 402 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "QI investiční společnost a.s. fondy"

Links: [{"title":"povinne uverejnovane info.pdf","url":"https://www.conseq.cz/getattachment/About-company/Obligatory-reporting/QI-investicni-spolecnost/povinne-uverejnovane-info.pdf.aspx?lang=cs-CZ"},{"title":"24 QI investicni spolecnost a s VZ.pdf","url":"https://www.conseq.cz/getmedia/ca2e88bf-7293-4c42-a534-f6c8d4f351d9/24-QI-investicni-spolecnost-a-s-VZ.pdf.aspx"},{"title":"QIIS VZ UZ 2019 FINAL.pdf","url":"https://www.conseq.cz/getmedia/f9ed1328-a86b-4ba0-a80a-07cd3fb77703/QIIS_VZ_UZ_2019_FINAL.pdf.aspx"},{"title":"QIIS VZ UZ 2018 KPMG FINAL v2 complete","url":"https://www.conseq.cz/getmedia/4e91d54c-37be-4d46-a3c9-04ad6afdc6ba/QIIS_VZ_UZ_2018_KPMG_FINAL_v2_complete.aspx?ext=.pdf"},{"title":"QIIS AR UZ 2020 signed.pdf","url":"https://www.conseq.cz/getmedia/d23558a5-692a-4f58-a406-ed86d75e42a8/QIIS-AR-UZ-2020-signed.pdf.aspx"},{"title":"QI Annual Report 2012 FINAL","url":"https://www.conseq.cz/getmedia/8c3ea58c-69e4-4e51-8c19-434aa03368d5/QI_Annual_Report_2012_FINAL.aspx?ext=.pdf"},{"title":"QI SemiAnnual Report 2013 final","url":"https://www.conseq.cz/getmedia/06931a36-ecf6-4b49-a814-5628d959507a/QI_SemiAnnual_Report_2013_final.aspx?ext=.pdf"},{"title":"1106 pololetni zprava QI","url":"https://www.conseq.cz/getmedia/b06bd41a-27df-4f28-8626-5fc7e4fed98c/1106_pololetni_zprava_QI.aspx?ext=.pdf"},{"title":"QI Annual Report 2011 FINAL 2","url":"https://www.conseq.cz/getmedia/a2dc7876-c69a-4ad3-a6da-f8f4f2ef6700/QI_Annual_Report_2011_FINAL_2.aspx?ext=.pdf"}]

Links: [{"title":"24 QI investicni spolecnost a s VZ.pdf","url":"https://www.conseq.cz/getmedia/ca2e88bf-7293-4c42-a534-f6c8d4f351d9/24-QI-investicni-spolecnost-a-s-VZ.pdf.aspx"},{"title":"povinne uverejnovane info.pdf","url":"https://www.conseq.cz/getattachment/About-company/Obligatory-reporting/QI-investicni-spolecnost/povinne-uverejnovane-info.pdf.aspx?lang=cs-CZ"},{"title":"22 QIIS VZ 2022 FINAL.pdf","url":"https://www.conseq.cz/getmedia/673a689b-9667-4e17-9ed8-0c08f33cbf12/22-QIIS-VZ-2022-FINAL.pdf.aspx"},{"title":"QIIS AR UZ 2020 signed.pdf","url":"https://www.conseq.cz/getmedia/d23558a5-692a-4f58-a406-ed86d75e42a8/QIIS-AR-UZ-2020-signed.pdf.aspx"},{"title":"Informace poskytnuté na žádost ze dne 5. 1. 2026 týkající se fondového investování","url":"https://www.cnb.cz/cs/o_cnb/106/informace-poskytnute-ceskou-narodni-bankou-podle-zakona-c.-106-1999-sb.-o-svobodnem-pristupu-k-informacim/Informace-poskytnute-na-zadost-ze-dne-5.nbsp1.nbsp2026-tykajici-se-fondoveho-investovani"},{"title":"QIIS VZ UZ 2019 FINAL.pdf","url":"https://www.conseq.cz/getmedia/f9ed1328-a86b-4ba0-a80a-07cd3fb77703/QIIS_VZ_UZ_2019_FINAL.pdf.aspx"},{"title":"1106 pololetni zprava QI","url":"https://www.conseq.cz/getmedia/b06bd41a-27df-4f28-8626-5fc7e4fed98c/1106_pololetni_zprava_QI.aspx?ext=.pdf"},{"title":"QI AR 2012 FINAL","url":"https://www.conseq.cz/getmedia/54f5b6ad-6b86-4168-b5fa-643efd6be9c9/QI_AR_2012_FINAL.aspx?ext=.pdf"},{"title":"QI Annual Re
… [skrátené, 2651 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Eterus Capital správcovská spoločnosť portfólio o nás"

Links: [{"title":"Boris Kostik","url":"https://sk.linkedin.com/in/boris-kostik"},{"title":"Preskočiť na hlavný obsah","url":"https://kpmg.com/sk/sk/home/insights/2019/10/transakcia-hopin-eteruscapital-kpmg-poradca.html"},{"title":"Go to deals","url":"https://www.oaklins.com/se/en/deals/110584/"},{"title":"Go to deals","url":"https://www.oaklins.com/ie/en/deals/110584/"},{"title":"Transaktionen anzeigen","url":"https://oaklins.com/ch/de/deals/110584"},{"title":"Go to deals","url":"https://www.oaklins.com/ma/en/deals/110584/"},{"title":"Til transaksjoner","url":"https://oaklins.com/no/no/deals/110584"},{"title":"Allez à nos transactions","url":"https://www.oaklins.com/ca/fr/deals/110584/"},{"title":"Private Equity","url":"https://altss.com/profile/eterus-capital"},{"title":"Eterus Capital logo","url":"https://www.tryfundable.ai/investor/eterus-capital"}]

Stránku „O nás“ z oficiálneho webu eterus.sk sa mi vo výsledkoch nepodarilo nájsť. Zdroje tretích strán však dávajú tento obraz:

**Základné informácie**
- Oaklins opisuje Eterus ako súkromný kapitálový fond z roku 2008, ktorý podporuje menšie a stredné firmy s overeným biznis modelom a rastovým potenciálom. Eterus Capital is a private equity fund founded in 2008, specializing in supporting small and medium-sized enterprises with proven business models and growth potential.
- Fond podľa Oaklins investuje najmä do menšinových podielov, takže riadenie ostáva pri pôvodných vlastníkoch. (3-3)
- Oaklins uvádza, že fond vložil do vyše dvadsiatich firiem približne 40 miliónov eur. (3-4)
- Altss radí Eterus do Bratislavy a uvádza, že portfólio sa sústreďuje na Slovensko a širší región strednej a východnej Európy. (9-6)

**Správa fondu**
- KPMG v publikácii z roku 2019 označuje WOOD & Company za správcu fondu, pričom ide o investičnú skupinu s popredným postavením v strednej Európe. (2-13)
- Tryfundable popisuje rovnaký vzťah a uvádza, že fond riadi WOOD & Company. (10-2)

**Portfólio**
- Podľa Oaklins patria medzi známe firmy v portfóliu Sygic, HOPIN, eyerim, Saneca Pharmaceuticals, Groupsolver a MTBIKER. (3-5)
- Z augusta 2024 pochádza nadobudnutie väčšinového podielu v EC Pharmacies, platforme na konsolidáciu slovenského trhu s lekárňami, ktorú založil spolu s Ethernum Capital. (3-1, 3-6)
- KPMG, ktoré pri transakcii poskytovalo poradenstvo, eviduje vstup fondu do HOPIN so 40-percentným podielom z júla 2019. (2-2, 2-3)

**Na čo si dať pozor**
- Zdroje sa líšia v dôraze. Altss hovorí o kombinácii rastového financovania a reštrukturalizácie (9-2), zatiaľ čo Oaklins zdôrazňuje minoritné podiely (3-3).
- Z výsledkov neviem potvrdiť, či má sám Eterus licenciu správcovskej spoločnosti. Zdroje hovoria skôr o tom, že fond spravuje WOOD & Company. Tento údaj by som overil v registri Národnej banky Slovenska.
- Väčšina údajov pochádza z rokov 2019 až 2024, takže aktuálne čísla a zloženie portfólia môžu byť iné. Najpresnejšie in
… [skrátené, 185 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://eterus.sk",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that mention Eterus, the fund's investment approach, portfolio companies (names), investment size, fund size, office location, or the company's legal name and company ID. Do not paraphrase anything outside quotation marks. Include the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Eterus Ethernum Dr. Martin dental investícia 2024",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/jakub-havrlant-prichazi-s-novym-investicnim-fondem-rockaway-s-nim-chce-do-startupu-poslat-25-miliardy-korun/",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that mention Rockaway, the fund name, fund size in korun or euros, the fund's target or what it invests in, its investments or portfolio companies, and the article's publication date. Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/navrat-rockaway-do-sveta-startupovych-investic-aneb-prehled-vsech-dubnovych-dealu-a-transakci/",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that mention Rockaway, the name of each startup Rockaway invested in, the round type, the amount, and the article's publication date or the year of these deals. Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.conseq.cz/getmedia/ca2e88bf-7293-4c42-a534-f6c8d4f351d9/24-QI-investicni-spolecnost-a-s-VZ.pdf.aspx",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 12 short sentences (each under 125 characters) that state what funds QI investiční společnost manages, what those funds invest in (real estate, receivables, shares in companies, loans), their names and sizes, and the company's address and company ID (IČO). Do not paraphrase anything outside quotation marks. Include the report year."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"CEC Capital\" Bratislava investment fund",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't produce those quotations. The content you pasted is a raw, compressed PDF file (FlateDecode streams with binary data), not readable text. Any sentences I quoted would be fabricated, and I won't invent text attributed to the document.

To get the information you need, you could:

- **Paste the extracted text.** Copy the readable text from the PDF, or run it through a tool like `pdftotext`, and share that.
- **Upload the PDF directly** if your interface supports file attachments, so the text layer can be read.
- **Provide the relevant pages** as plain text, such as the company description, fund listings, and contact section.

Once I have the readable text, I'll list up to 12 verbatim quotes in quotation marks, each under 125 characters, covering the fund manager's name, the funds and their investment types, fund sizes, the address, the IČO, and the report year.

[Binary content (application/pdf, 2.7MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791493884162-fjphre.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. "Do inovácií sme formou private equity investovali už viac než 40 mil. EUR."
2. "Eterus je partner pre financovanie spoločností vo fáze rastu, so schopným managementom a overeným konceptom."
3. "Fond vstupuje do spoločností ako minoritný akcionár, manažérska kontrola zostáva v rukách pôvodných akcionárov."
4. "Sme kapitálovým fondom investujúcim do akcií a iných nástrojov vlastného imania spoločností s domicilom na Slovensku."
5. "Zameriavame sa na investície v rozmedzí 2 - 2,5 mil. EUR, pričom preferovaná dĺžka investície predstavuje 5-7 rokov."
6. "Neponúkame dlhové financovanie."
7. Dr. Martin Zubná klinika: "Konsolidačná platforma pre zubné ordinácie na Slovensku."
8. EC Pharmacies: "Konsolidačná platforma pre lekárne na Slovensku."
9. Ecocapsule: "Výrobca inteligentných, sebestačných mikrodomov, ktoré využívajú slnečnú a veternú energiu."
10. Office location: "Gorkého 4, Bratislava"

The page does not show a publication date, and it does not state the company's legal name or company ID.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Eterus Ethernum Dr. Martin dental investícia 2024"

Links: [{"title":"Go to deals","url":"https://www.oaklins.com/se/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/it/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/kr/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/mx/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/br/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/ca/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/ma/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/sg/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/pl/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/de/en/deals/110583/"}]

The search turned up one deal, reported by the advisory firm Oaklins in May 2024. The same page appears under many of Oaklins' country sites, so these results are effectively a single source.

- **The deal:** Eterus Capital and Ethernum Capital provided funding to the Slovak clinic network, which is meant to fund its nationwide expansion.
- **Strategy:** The group wants to become Slovakia's biggest dental care provider by combining new clinic openings with acquisitions.
- **About Eterus Capital:** The fund, started in 2008, backs smaller and mid-sized companies that have working business models and room to grow. It usually takes minority stakes, so the original owners keep management control. It says it has put more than €40 million into over 20 companies.
- **About Dr. Martin:** The firm has been in private dentistry for over ten years and provides implant, prosthetic, and cosmetic and restorative care. It runs four clinics plus a children's clinic under the Dr. Martinko name, with about 130 staff.
- **Advisors:** Oaklins' Slovak team advised Eterus Capital on the transaction.

The results don't disclose the investment amount or the size of the stake taken. Independent press coverage of the deal didn't show up in these results, so the Oaklins page is the only source I can confirm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. "23. 9. 2021"
2. "Jakub Havrlant, zakladatel Rockaway Capital"
3. "Její nový fond zvaný Rockaway Ventures Fund má cílovou velikost 100 milionů eur, tedy zhruba 2,5 miliardy korun"
4. "Teď chce svůj investiční záběr ještě rozšířit a otevírá nový fond zvaný Rockaway Ventures Fund."
5. "V Rockaway Ventures Fundu se chtějí dál věnovat především oblastem, kterým rozumí"
6. "tedy převážně technologickým projektům z regionu střední a východní Evropy včetně pobaltských zemí a Balkánu"
7. "Productboard, Brand Embassy či Storyous – to jsou tři z celkem dvaadvaceti startupů"
8. "První miliony eur již fond poslal do jednoho estonského a jednoho německého startupu."
9. "Rychle rostoucí startup Lingvist z Estonska vyvíjí vzdělávací jazykovou platformu"
10. "Druhým investičním zářezem se stal německý projekt Vivere"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. Rockaway mention: "Rockaway není ve startupovém světě nováčkem."
2. Fund: "Pozornost nyní skupina ale věnuje i svému novému investičnímu fondu Rockaway Ventures Fund se zaměřením na startupy."
3. Spotawheel, round and amount: "Rockaway Ventures Fund zároveň ohlásil novou investici, když se podílel na Series B ve výši 100 milionů eur"
4. Spotawheel, company: "do původem řecké platformy Spotawheel zaměřené na nákup a přeprodej ojetých vozidel."
5. Vivere: "Pro Rockaway Ventures Fund jde o třetí investici, předtím již podpořil německé Vivere"
6. Lingvist: "estonskou jazykovou vzdělávací platformu Lingvist."
7. Historical startups, including Productboard, Gjirafa, Brand Embassy and Storyous: "Historicky investičně podpořilo 22 startupů (včetně Productboardu, albánské Gjirafy, Brand Embassy či Storyous)"
8. Total invested, with publication date: "Do startupů Rockaway Ventures vložilo přes 27 milionů eur (zhruba 670 milionů korun)." Publication date: "Startupy – 02. 5. 2022 – 4 min čtení"

Notes: The article gives a round type and amount only for Spotawheel (Series B, 100 million euros). It gives no round or amount for Vivere, Lingvist, or the other historical startups. Several quotes are excerpts cut to fit the 125-character limit.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""CEC Capital" Bratislava investment fund"

Links: [{"title":"realassets.ipe.com","url":"https://realassets.ipe.com/propertyeu/cec-capital-relaunches-as-mint-investments/10125356.article"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"cec capital","url":"https://startupintros.com/orgs/cec-capital"},{"title":"CEE Capital Management","url":"https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/cee-capital-management"},{"title":"365 fintech","url":"https://app.dealroom.co/investors/365_fintech"},{"title":"cec management","url":"https://www.cbinsights.com/investor/cec-management"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/cec-fund"},{"title":"CB Investment Management","url":"https://rwanda.dealroom.co/companies/cb_investment_management"},{"title":"Content area","url":"https://www.proquest.com/docview/908528712"}]

The search found one result that matches "CEC Capital" as a Central European property investor, but nothing here confirms a Bratislava base.

**CEC Capital became Mint Investments.** The group, described as a Central European real estate investment and development business, has announced its relaunch as Mint Investments, and the aim is to unify its activities under one brand. The article is undated in these results, so I can't tell when this happened or whether the name is still in use.

**Holdings and partners.** The firm's operating interests in CSIA and Develon will continue to be held jointly with Avestus Capital Partners under the new name. A partner, Sebastien Dejanovski, argued that the market downturn worked as a catalyst for needed industry change, and the firm reported inquiries from new investors interested in the region.

**Other entities with similar names (likely unrelated):**
- CEC Capital Group, an investment bank headquartered in Beijing, with offices in Shanghai, Shenzhen, and San Francisco.
- CEC Management, a private equity manager with a Hong Kong address.
- CEE Capital Management, a.s., which manages alternative investment funds with the aim of implementing projects in Slovakia and in the wider region of Central and Eastern Europe. Its name is close to CEC Capital, but the results don't say where it is based or link it to CEC Capital.

None of the Bratislava-focused results I found mention CEC Capital or Mint Investments. To confirm a Bratislava connection, check Slovak company registry records for the CEC Capital or Mint Investments entities, or ask the firm directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://eterus.sk/portfolio",
  "prompt": "List the exact verbatim text, in quotation marks, of short lines (each under 125 characters) that name the portfolio companies or investments of Eterus, with any dates or amounts stated next to them. Do not paraphrase anything outside quotation marks. If the page has no portfolio list, say so and list any company names you see in quotation marks."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.oaklins.com/se/en/deals/110583/",
  "prompt": "List the exact verbatim text, in quotation marks, of the sentences that name the target company, the investors (Eterus Capital, Ethernum Capital), the transaction type, and any date shown on the page (month and year). Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Rockaway Ventures Fund official website startups Europe",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Prague-based Rockaway Ventures closes second fund 55 million",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "QI investiční společnost fond nemovitosti kvalifikovaní investoři 2024",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "TMF Czech a.s. Praha služby společnost investice",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Target company:**
- "Dr. Martin Dental Clinic, a leading network of dental clinics in Slovakia"

**Investors:**
- "has received a significant investment from Eterus Capital and Ethernum Capital"

**Transaction type:**
- "has received a significant investment"
- Service label: "M&A buy-side"

**Date:**
- "May 2024"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page has a portfolio list, but most company entries carry no dates or amounts. The company name lines are:

- "Dr. Martin Zubná klinika"
- "EC Pharmacies"
- "MTBIKER"
- "GroupSolver"
- "VIRTUAL REALITY MEDIA"
- "CTI GROUP"
- "Eyerim"
- "Ecocapsule"
- "HOPIN"
- "EEI"
- "CHÉMIA SERVIS"
- "Sygic"
- "Saneca Pharma"
- "Betamont"
- "ADOTEL-HEX"
- "INDULONA"
- "DRIVING ACADEMY"
- "WINDOWGLASS"
- "SOLAR PORTFOLIO"

The only lines with dates or amounts next to a portfolio company or investment are:

- "7 solárnych elektrární s celkovým inštalovaným výkonom 10 MW." (SOLAR PORTFOLIO)
- "Najväčší cyklistický portál na Slovensku" (MTBIKER, with "od roku 1998" appearing in the same sentence)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Prague-based Rockaway Ventures closes second fund 55 million"

Links: [{"title":"prague based rockaway ventures closes second fund at nearly 55m","url":"https://startuphub.unwe.bg/bg/news/64138/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html"},{"title":"prague based rockaway ventures closes second fund at nearly 55m","url":"https://startuphub.unwe.bg/bg/news/64237/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html"},{"title":"therecursive.com","url":"https://therecursive.com/?p=40580"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=63834"},{"title":"CEE VC SUMMIT 2026","url":"https://vestbee.com/blog/articles/rockaway-ventures-closes-55-m-fund"},{"title":"rockaway ventures closes second fund at e55m","url":"https://siliconcanals.com/rockaway-ventures-closes-second-fund-at-e55m/"},{"title":"Prague-Based Rockaway Ventures Closes Second Fund at Nearly €55M","url":"https://therecursive.com/author/the-recursive/page/3/"},{"title":"Rockaway Ventures closes €55M Fund to back transformative tech in CEE and beyond","url":"https://tech.eu/2025/05/16/rockaway-ventures-closes-55m-fund-to-back-transformative-tech-in-cee-and-beyond/"},{"title":"Now Reading","url":"https://startupsmagazine.co.uk/article-rockaway-ventures-closes-second-fund-nearly-55m"}]

Several outlets reported in mid-May 2025 that Rockaway Ventures closed its second fund, Rockaway Ventures II, at nearly €55 million. Rockaway Ventures, a European investment fund under the Rockaway Capital group, has closed its second fund, Rockaway Ventures II, at nearly €55 million.

**Focus**
- The vehicle is aimed at late-seed and Series A tech companies with the potential to drive innovation in traditional industries.
- Its earlier deals concentrated on e-commerce and travel software, but attention has moved to energy, defense and dual-use technology. 

**Background and structure**
- Founded in 2014 by Jakub Havrlant, the firm is part of the Rockaway Capital group and focuses on Central Europe and the DACH region.
- Activity started in 2014, before any formal entity existed, with early Czech companies such as Productboard and Storyous among its first backers. 
- The current fund dates from 2022. 

**Plans and portfolio**
- At the time of the close, the fund had 11 portfolio companies. 
- Over three years, the plan is to direct 60% of investments to Central and Eastern Europe and 40% to Western Europe and diaspora-founded startups. 
- Named holdings include Germany-based hotel software company Apaleo and Albanian e-commerce and media platform Gjirafa, into which Rockaway has put $8.7 million across two rounds. 

**Discrepancy:** One outlet, Startups Magazine, headlined the figure in dollars, while most others reported euros. 

These reports are from May 2025, and this search didn't turn up anything more recent. For l
… [skrátené, 170 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "TMF Czech a.s. Praha služby společnost investice"

Links: [{"title":"TMF Assets a.s., v likvidaci - obchodní rejstřík, úplný výpis","url":"https://rejstrik-firem.kurzy.cz/26485583/"},{"title":"tmf czech","url":"https://www.expats.cz/directory/listing/tmf-czech"},{"title":"REQUEST A DEMO","url":"https://emis.cn/php/company-profile/CZ/Tmf_Czech_AS_en_4870926.html"},{"title":"czech republic","url":"https://www.tmf-group.com/en/locations/emea/czech-republic"},{"title":"czech republic","url":"https://www.tmf-group.com/en/locations/europe/czech-republic/"},{"title":"jakub erenyi","url":"https://www.tmf-group.com/en/our-people/jakub-erenyi"},{"title":"chm invest s r o 28933427","url":"https://www.podnikatel.cz/rejstrik/chm-invest-s-r-o-28933427/"},{"title":"tmds cz s r o 17252989","url":"https://www.podnikatel.cz/rejstrik/tmds-cz-s-r-o-17252989/"},{"title":"TD invest, a.s., IČO (28665457), sídlo Praha 9","url":"https://www.mesec.cz/rejstrik-firem/firma-td-invest-a-s-28665457"}]

I found information on TMF Czech a.s. from the company's own site and third-party directories, but nothing specific about its investment activities.

**Background**
- The Czech operation is part of TMF Group, whose Czech presence goes back to 1997, according to an expats directory listing. The parent was founded in the Netherlands in 1988.
- The group's stated aim is to become one of the world's leading providers of professional business services, with a focus on helping clients invest across borders.

**Services**
- The Czech team covers accounting and tax, corporate secretarial, entity management, payroll and HR.
- The firm says it has provided a full range of compliance services to Czech businesses for more than 25 years.
- It holds ISO/IEC 27001:2022 certification for information security.
- The group lists Jakub Erényi as Country leader, Czech Republic.

**Location**
- The company's listed office is at Kateřinská 40 Business Center (Kateřinská 40, 120 00, Prague 2). A business-data aggregator gives the headquarters as Kateřinská 466/40, Prague.

**Third-party profile (EMIS)**
- The EMIS profile classifies the company under accounting, tax preparation, bookkeeping, and payroll services.
- It gives an incorporation date of August 01, 2010, which doesn't obviously match the 1997 start, so I'd verify it against the official register.
- The profile reports 100 - 199 employees (2024) and a net sales revenue increase of 15.33% in 2022.

**Don't confuse with TMF Assets a.s.**
- A separate company, TMF Assets a.s., used the same Kateřinská 466/40 address. It had a different company ID (IČO 26485583), was in liquidation, and was deleted from the register on 8 October 2019. Its registered business was property rental. I couldn't confirm any link between it and TMF Czech a.s.

**Gaps**
- I didn't find TMF Czech a.s.'s own commercial register entry, so its company ID and legal details are unverified. I also found no information about investment products or
… [skrátené, 277 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "QI investiční společnost fond nemovitosti kvalifikovaní investoři 2024"

Links: [{"title":"Novela zákona o kolektivním investování","url":"https://epravo.cz/top/clanky/novela-zakona-o-kolektivnim-investovani-43239.html"},{"title":"novela zakona o kolektivnim investovani 43239","url":"https://www.epravo.cz/top/clanky/novela-zakona-o-kolektivnim-investovani-43239.html?pdf=1"},{"title":"fondy kvalifikovanych investoru v ceske republice 48837","url":"https://www.epravo.cz/top/clanky/fondy-kvalifikovanych-investoru-v-ceske-republice-48837.html"},{"title":"fondy kvalifikovanych investoru","url":"https://finex.cz/fondy-kvalifikovanych-investoru/"},{"title":"Comparative Analysis of Real Estate Investment Strategies for Retail and Qualified Investors","url":"https://vskp.vse.cz/english/97275"},{"title":"24 QI investicni spolecnost a s VZ.pdf","url":"https://www.conseq.cz/getmedia/ca2e88bf-7293-4c42-a534-f6c8d4f351d9/24-QI-investicni-spolecnost-a-s-VZ.pdf.aspx"},{"title":"Investice do vína, umění nebo půdy. I to nabízejí fondy kvalifikovaných investorů","url":"https://www.e15.cz/finexpert/investujeme/investice-do-vina-umeni-nebo-pudy-i-to-nabizeji-fondy-kvalifikovanych-investoru-1346941"},{"title":"QIIS VZ UZ 2018 KPMG FINAL v2 complete","url":"https://www.conseq.cz/getmedia/4e91d54c-37be-4d46-a3c9-04ad6afdc6ba/QIIS_VZ_UZ_2018_KPMG_FINAL_v2_complete.aspx?ext=.pdf"},{"title":"fondy kvalifikovanych investoru v ceske republice 48837","url":"https://www.epravo.cz/top/clanky/fondy-kvalifikovanych-investoru-v-ceske-republice-48837.html?pdf=1"}]

The search mostly returned material on Czech qualified investor funds (fondy kvalifikovaných investorů, FKI). Only one result is from 2024, and it concerns a specific company. Most of the regulatory material is older.

**2024 company document**
QI investiční společnost, a.s. published an annual report for the year ended 31 December 2024 (VÝROČNÍ ZPRÁVA SPOLEČNOSTI S NÁZVEM: QI INVESTIČNÍ SPOLEČNOST, A.S. ZA ROK KONČÍCÍ 31. PROSINCE 2024). Its licence lets it manage FKI funds and comparable foreign funds and administer them, but it excludes qualified venture-capital and social-enterprise funds (Povolení k činnosti investiční společnosti v rozsahu... obhospodařovat fondy kvalifikovaných investorů... s výjimkou kvalifikovaných fondů rizikového kapitálu). The report also covers a corporate restructuring within the Conseq group, with a split project dated 5 December 2023 (Dne 5.12.2023 byl společností Conseq Group, a.s., jako společností nástupnickou, a Conseq Investment Management, a.s. jako společností rozdělovanou, vyhotoven projekt rozdělení).

**Legal basis and entry rules**
The FKI regime sits in the Act on Investment Companies and Investment Funds (ZISIF, Act 240/2013 Coll.). One summary lists three routes to qualifying as a qualified investor: a minimum investment of €125,000 with a risk declaration, a minimum of CZK 1,000,000 plus a knowledge test, or professional-investor status (Inves
… [skrátené, 2440 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Rockaway Ventures Fund official website startups Europe"

Links: [{"title":"rockaway ventures","url":"https://superscout.co/investor/rockaway-ventures"},{"title":"Rockaway Capital","url":"https://app.dealroom.co/companies/rockaway_capital"},{"title":"Venture Capital","url":"https://altss.com/profile/rockaway-ventures"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=63834"},{"title":"rockaway ventures","url":"https://venturecapitalcareers.com/company/rockaway-ventures"},{"title":"rockaway ventures","url":"https://venturecapitalcareers.com/companies/rockaway-ventures"},{"title":"rockaway ventures closes second fund at e55m","url":"https://siliconcanals.com/rockaway-ventures-closes-second-fund-at-e55m/"},{"title":"rockaway ventures","url":"https://ecosystem.madrimasd.org/companies/rockaway_ventures"},{"title":"Rockaway Ventures Investor","url":"https://mindmaps.femtech.health/firms/147180"}]

I couldn't reach the firm's own site in this search, so the details below come from third-party directories and press coverage.

**Official website:** The firm maintains an online presence at rockawayventures.com. Another directory lists the same address, but you should confirm it on the site itself.

**Investment focus:** The firm is a venture capital firm established in 2014 and headquartered in Prague, Czech Republic. Its checks typically go to companies that already show traction at the late-seed or Series A stage. Sector bets include e-commerce, travel, digital logistics, media, cybersecurity, defence, CleanTech, and PropTech. Geographically, it covers Central and Eastern Europe (CEE) and Western Europe. One directory instead emphasizes the CEE and the DACH regions and ESG principles.

**Fund and strategy:** Silicon Canals reported that the second vehicle, Rockaway Ventures II, reached nearly €55M at close. Its interest has moved from e-commerce and travel tech toward energy, defence, and dual-use technologies. Planned new deals split roughly 60/40, with the larger share going to CEE and the rest to Western Europe and diaspora founders now based in the US.

**Portfolio examples:** Apaleo, a hotel management platform based in Germany is among its backed companies. Albanian e-commerce and media company Gjirafa has taken $8.7M from the fund across two rounds. At the time of the Silicon Canals report, the portfolio held 11 companies.

**Discrepancies:** Sources differ on the start date. Most profiles give 2014, while Silicon Canals names 2013 and Jakub Havrlant as founder, and says Rockaway Ventures began informal investing in 2014.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://rockawayventures.com",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 12 short sentences (each under 125 characters) that state the fund's office location or city, its stage focus (for example seed, Series A), typical ticket or check size, preferred sectors, portfolio company names, and the legal name or company ID if shown. Do not paraphrase anything outside quotation marks. Include the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2025/05/16/rockaway-ventures-closes-55m-fund-to-back-transformative-tech-in-cee-and-beyond/",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that mention Rockaway Ventures' fund size, its stage focus (late-seed, Series A), where the firm is based (city), and the portfolio companies named. Do not paraphrase anything outside quotation marks. Include the article's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Apptronik Series A Rockaway Ventures Google Mercedes-Benz John Deere",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tmf-group.com/en/locations/europe/czech-republic/",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that describe the services offered by TMF in the Czech Republic, the office address, and the Czech entity name. Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.oaklins.com/se/en/deals/110584/",
  "prompt": "List the exact verbatim text, in quotation marks, of the sentences that name the target company, the investors (Eterus Capital and any others), the transaction type, and any date shown on the page (month and year). Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.conseq.cz/about-company/obligatory-reporting/qi-investicni-spolecnost",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that describe the funds this investment company manages, what the funds invest in (real estate, shares in companies, receivables, loans), the company's seat address, and its company ID (IČO). Do not paraphrase anything outside quotation marks. If nothing relevant is on the page, say so."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Target company:**
- "EC Pharmacies is a joint venture between Eterus Capital and Ethernum Capital"

**Investors:**
- "Eterus Capital has acquired a majority stake in EC Pharmacies"
- "a consolidation platform established in partnership with Ethernum Capital."

**Transaction type:**
- "Eterus Capital has acquired a majority stake"

**Date (month and year):**
- "August 2024"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Funds:**
- "Informační povinnost fondu První realitní otevřený podílový fond kvalifikovaných investorů"
- "Platforma fondů kvalifikovaných investorů"
- "Fondy kvalifikovaných investorů"

**What the funds invest in:** The page does not state this explicitly. The only related text is "Investujte do atraktivních investičních příležitostí mimo tradiční třídy aktiv." The fund name "První realitní otevřený podílový fond" suggests real estate, but the page does not confirm it.

**Seat address:**
- "Burzovní palác"
- "Rybná 682/14"
- "110 00 Praha 1"

The page lists this address under "Kontaktujte nás" for "Conseq Investment Management, a.s.", not under QI investiční společnost, a.s.

**Company ID (IČO):** Not found on the page.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Services (Czech Republic):**

1. "Providing critical compliance and administrative services in Czech Republic and around the world"
2. "The services we provide are grouped into six key areas of business administration."
3. "Our unique global delivery model means we can cover a wide range of diverse sectors."
4. "We work closely with our clients to understand and address their needs and requirements."

**Office address (Prague):**

"Kateřinská 40 Business Center (Kateřinská 40, 120 00, Prague 2)" / "Prague" / "Czech Republic"

**Czech entity name:**

"TMF Czech a.s."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 16 May 2025

**Fund size:**
- "has closed its second fund, Rockaway Ventures II, at nearly €55 million."

**Stage focus:**
- "The fund targets late-Seed and Series A tech startups with the potential to drive innovation in traditional industries."

**Location:**
- The article does not name a city. It describes the firm as "a European investment fund under the Rockaway Capital group."

**Portfolio companies named:**
- "Notable investments include German cloud-native hotel management platform Apaleo"
- "CulturePulse, a US-Slovak startup utilising AI for behavioral modeling and risk prediction"
- "Albanian e-commerce and media platform Gjirafa."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Office location/city:** Not stated for the fund on this page.

**Stage focus:**
- "The goal of the Rockaway Ventures fund is to support startups with proven traction in the late seed or Series A stage"

**Typical ticket/check size:** Not stated.

**Preferred sectors:**
- "retail and e-commerce, travel & hospitality, digital logistics, digital media"
- "cybersecurity, defence, CleanTech, and PropTech"

**Portfolio company names (from testimonial attributions):**
- "CEO & founder of productboard"
- "CEO & founder of Gjirafa"
- "CEO of BudgetBakers"
- "CEO & founder of Brand Embassy"
- "CEO of Storyous"
- "CEO & founder of Creditas"

**Legal name/company ID:**
- "Copyright © 2026 Rockaway Ventures Fund" (no company ID shown)

**Publication date:** No single publication date is shown for the page. The most recent news item is dated "July 14, 2025."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Apptronik Series A Rockaway Ventures Google Mercedes-Benz John Deere"

Links: [{"title":"Join Vestbee","url":"https://www.vestbee.com/insights/articles/935-m-series-a-for-apptronik"},{"title":"Join Vestbee","url":"https://vestbee.com/blog/articles/935-m-series-a-for-apptronik"},{"title":"Čeští investoři z Rockaway investovali do amerických humanoidů. A to po boku Googlu nebo Mercedes-Benz","url":"https://www.lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humanoidu-a-to-po-boku-googlu-nebo-mercedes-benz/"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/apptronik/financials"},{"title":"Apptronik: $935+ Million Series A Raised For AI-Based Robotics","url":"https://pulse2.com/apptronik-935-million-series-a-raised-for-ai-based-robotics"},{"title":"Apptronik: $935+ Million Series A Raised For AI-Based Robotics","url":"https://pulse2.com/apptronik-935-million-series-a-raised-for-ai-based-robotics/amp/"},{"title":"www.automate.org","url":"https://www.automate.org/robotics/industry-insights/apptronik-nears-935m-in-series-a-funding-ahead-of-new-humanoid-launch/boa"},{"title":"www.automate.org","url":"https://www.automate.org/robotics/industry-insights/apptronik-nears-935m-in-series-a-funding-ahead-of-new-humanoid-launch/aph"},{"title":"Press Release","url":"https://www.apptronik.com/news-collection/apptronik-closes-over-935-million-series-a"},{"title":"2026 02 11 apptronik series a","url":"https://startupintros.com/news/2026-02-11-apptronik-series-a"}]

**Apptronik's Series A-X extension (February 2026)**

- **Round size and timing:** Apptronik announced a $520 million Series A-X extension on February 11, 2026. The round follows a $415 million oversubscribed initial Series A raise in 2025, bringing the total Series A to more than $935 million and total capital raised to nearly $1 billion.

- **Existing investors:** B Capital, Google, Mercedes-Benz, and PEAK6 returned for the extension (repeat investors including B Capital, Google, Mercedes-Benz and PEAK6).

- **New investors:** AT&T Ventures, John Deere, and Qatar Investment Authority joined (new investors including AT&T Ventures, John Deere and QIA).

- **Rockaway Ventures:** The Prague-based firm is one of the new backers. Rockaway Ventures recently closed a €55 million fund to invest in late-seed and Series A tech startups. A Czech outlet, Lupa.cz, covered the deal from Rockaway's side. That article is in Czech, so I haven't verified its details beyond the headline framing.

- **Valuation:** The company's release says the extension opened at a 3x multiple of the Series A valuation. Third-party sources disagree on the dollar figure. One reports a valuation of over $5.5 billion, while CB Insights lists a range of $1,400 - $1,803M. I could not confirm either number against the company's own filings.

- **Naming discrepancy:** CB Insights lists the firm as "Rockaway Capital" rather than Rockaway Ventures, so the name may differ 
… [skrátené, 1022 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humanoidu-a-to-po-boku-googlu-nebo-mercedes-benz/",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 10 short sentences (each under 125 characters) that mention Rockaway, Apptronik, the investment amount or round, the round date, and any words describing Rockaway as a fund or investor (for example fond, investor, venture). Also state the article's publication date as shown. Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://startuphub.unwe.bg/bg/news/64138/prague-based-rockaway-ventures-closes-second-fund-at-nearly-55m.html",
  "prompt": "List the exact verbatim text, in quotation marks, of at most 8 short sentences (each under 125 characters) that mention Prague or the city where Rockaway Ventures is based, the fund size, and the publication date. Do not paraphrase anything outside quotation marks."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "TMF Czech investment portfolio startup funding round",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "CEC Capital Slovakia venture capital startup portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "QI investiční společnost investice do společností akcie startup",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. "Prague-Based Rockaway Ventures Closes Second Fund at Nearly €55M" (headline; names Prague and the fund size)
2. "has announced the closing of its second fund, Rockaway Ventures II, at nearly €55 million." (a clause from the body, not a full sentence, so it is the closest verbatim match for the fund size)
3. "четвъртък, 15 май 2025 11:10" (publication date line, Thursday, 15 May 2025, 11:10)

The article body describes the firm as "Czech-based" and does not mention Prague apart from the headline.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. "Čeští investoři z Rockaway Ventures finančně vstoupili do americké společnosti Apptronik, která vyvíjí humanoidní roboty."
2. "Firma oznámila rozšíření investičního kola Series A o 520 milionů dolarů (10,6 miliardy Kč)."
3. "Čeští investoři z Rockaway investovali do amerických humanoidů."

**Publication date:** "13. 2. 2026"

The article gives no separate round date, only this publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "TMF Czech investment portfolio startup funding round"

Links: [{"title":"tradition meets future","url":"https://www.wienerboerse.at/en/listing/going-public-ipo/capital-market-coach/tradition-meets-future/"},{"title":"tradition meets future","url":"https://www.wienerborse.at/en/listing/going-public-ipo/capital-market-coach/tradition-meets-future/"},{"title":"cee funding rounds 2025","url":"https://therecursive.com/tag/cee-funding-rounds-2025"},{"title":"9 Prague seed investors funding Czech tech startups in 2026","url":"https://www.ellty.com/investors/prague-seed-investors"},{"title":"tomas cupr launches new tcf capital fund","url":"https://en.ain.ua/2023/07/10/tomas-cupr-launches-new-tcf-capital-fund"},{"title":"european investment fund puts millions of euros into czech investment fund focusing on technology st","url":"https://www.czechtradeoffices.com/gb-ni/news/european-investment-fund-puts-millions-of-euros-into-czech-investment-fund-focusing-on-technology-st"},{"title":"What we do","url":"https://www.eif.org/what_we_do/equity/news/2023/czech-republicand-eif-launch-55-million-fund-of-funds-for-digital-technologies-backed-by-recovery-and-resilience-facility.htm"},{"title":"fond na e esko","url":"https://startupintros.com/orgs/fond-na-e-esko"},{"title":"STARTUP ECOSYSTEM","url":"https://co-investin.eu/?p=5857"}]

The search didn't find any Czech portfolio companies or funding rounds linked to TMF. It did return a profile of the firm itself. TMF, also known as Tradition Meets Future, is a Berlin-based investor that provides debt financing between EUR 2 and EUR 150 million to European growth and technology companies. Its listing doesn't mention any Czech companies.

Its eligibility rules are fairly specific. A candidate needs to have been in operation for at least 2 years, minimum revenues of €2m and growth of at least 20% p.a., and equity financing from at least one institutional investor. That last requirement suggests TMF usually works alongside an equity investor rather than providing the equity itself, though the source doesn't say this directly.

For Czech startup funding more broadly, the results show:
- In 2025, Czech-founded startups attracted about €540 million in investment, a 7.7% year-on-year decline.
- For 2023, according to Dealroom, Czechia raised €173.1 million in total, placing it fourth in the region for total capital raised.
- The European Investment Fund is backing the Czech ecosystem. Czechia mandated the EIF to manage a fund of funds focused on equity financing for early-stage Czech start-ups and spin-offs developing digital technologies.

If you meant a specific TMF investment in a Czech company, send me the company name or the approximate date and I can run a narrower search. If you meant a different organization called TMF, such as TMF Group, let me know and I'll search for that instead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "CEC Capital Slovakia venture capital startup portfolio"

Links: [{"title":"slovakia venture to future fund","url":"https://startups.one.gob.es/investors/slovakia_venture_to_future_fund"},{"title":"slovakia venture to future fund","url":"https://ecosystem.lafrenchtech.com/investors/slovakia_venture_to_future_fund"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"top vc funds in slovakia to finance your startup","url":"https://vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup"},{"title":"top vc funds in slovakia to finance your startup","url":"https://vestbee.com/blog/articles/top-vc-funds-in-slovakia-to-finance-your-startup"},{"title":"therecursive.com","url":"https://therecursive.com/?p=41532"},{"title":"Slovakia Venture to Future Fund","url":"https://app.dealroom.co/investors/slovakia_venture_to_future_fund"},{"title":"Venture Capital and Startup Ecosystems in Central & Eastern Europe","url":"https://cars.stanford.edu/events/venture-capital-and-startup-ecosystems-central-eastern-europe"}]

My search returned nothing about CEC Capital, so I can't confirm whether it operates in Slovakia or what it has funded. The results did cover several Slovak venture firms and their portfolios, though some of that information looks dated.

- **Neulogy Ventures (Bratislava):** Its profile on Vestbee says the firm has put more than €23 million into dozens of early-stage companies, including GroupSolver, SaferPass and Voltia. That article also mentions a planned 2021 fund, so the figures may be out of date.
- **Vision Ventures (Bratislava):** Per the same Vestbee profile, it manages about €11 million and makes seed checks of up to €800,000. Its backed companies span several sectors, with examples including Instyle.ai, Spinbotics and Flowy.
- **365.fintech:** Its seed-stage investments run from €50,000 to €500,000, aimed at B2B fintech, insurtech and big-data businesses, according to Vestbee.
- **Slovakia Venture to Future Fund:** A Papermark guide calls it a national VC fund that co-finances Slovak startups. Its listings on the ONE and Dealroom platforms show zero portfolio companies, which suggests those databases are incomplete rather than that the fund has no investments. A separate roundup lists it as an investor in a fintech seed round totaling €2.2 million.

A Papermark guide to Bratislava VC firms also names Zero Gravity Capital, ZAKA Ventures, Slovak Investment Holding, Crowdberry and others, but the snippets I retrieved don't include their portfolios.

To look into CEC Capital directly, I'd check the exact spelling of the name, its official website, or Slovak registries such as the Slovak business register. If you can tell me more about what the firm does or
… [skrátené, 150 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "QI investiční společnost investice do společností akcie startup"

Links: [{"title":"QIA launches Fund of Funds to invest over $1b in VCs","url":"https://media.dealstreetasia.com/stories/qia-to-invest-1-billion-in-vc-funds-385220"},{"title":"IQ Capital","url":"https://www.capboard.io/en/investor/iq-capital"},{"title":"qi venture partners","url":"https://superscout.co/investor/qi-venture-partners"},{"title":"qi ventures","url":"https://inc42.com/company/qi-ventures/"},{"title":"qi venture partners qiventure com","url":"https://venturecapitalarchive.com/venture-funds/qi-venture-partners-qiventure-com"},{"title":"qdb unveils first of its kind co investment product for start ups pitches qr365mn per deal","url":"https://www.gulf-times.com/article/656996/business/qdb-unveils-first-of-its-kind-co-investment-product-for-start-ups-pitches-qr365mn-per-deal"},{"title":"qdb unveils first of its kind co investment programme for start ups pitches qr365mn per deal","url":"https://www.gulf-times.com/article/656971/business/qdb-unveils-first-of-its-kind-co-investment-programme-for-start-ups-pitches-qr365mn-per-deal"},{"title":"inc42.com","url":"https://inc42.com/company/qi-ventures/investments/"},{"title":"qi ventures","url":"https://www.briter.co/companies/qi-ventures"}]

Links: [{"title":"Hlavní obsah","url":"https://www.novinky.cz/finance/clanek/fondy-kvalifikovanych-investoru-vyzaduji-vetsi-kapital-40276528"},{"title":"chystane novinky ve fondech kvalifikovanych investoru 56995","url":"https://www.epravo.cz/top/clanky/chystane-novinky-ve-fondech-kvalifikovanych-investoru-56995.html"},{"title":"Startupové investice v Česku slábnou. Nových je nejméně za poslední roky","url":"https://www.businessinfo.cz/clanky/startupove-investice-v-cesku-slabnou-novych-je-nejmene-za-posledni-roky/"},{"title":"Kvalitních startupů je dost, musíte je ale najít. S novým fondem cílíme na vesmír, říká Šíma z Depo Ventures","url":"https://www.businessinfo.cz/clanky/kvalitnich-startupu-je-dost-musite-je-ale-najit-s-novym-fondem-cilime-na-vesmir-rika-sima-z-depo-ventures/"},{"title":"Venture kapitál","url":"https://www.finmag.cz/tema/venture-kapital"},{"title":"Kvalitních startupů je dost, musíte je ale najít. S novým fondem cílíme na vesmír, říká Šíma z Depo Ventures","url":"https://www.e15.cz/rozhovory/kvalitnich-startupu-je-dost-musite-je-ale-najit-s-novym-fondem-cilime-na-vesmir-rika-sima-z-depo-ventures-1431871"},{"title":"www.finmag.cz","url":"https://www.finmag.cz/tema/czechinvest"},{"title":"Jak se mění české investiční prostředí? Odpověď hledá šestý ročník průzkumu startupových investorů","url":"https://www.businessinfo.cz/clanky/jak-se-meni-ceske-investicni-prostredi-co-ukazal-sesty-rocnik-pruzkumu-startupovych-investoru/"},{"title":"Investorům i startupům se v ČR loni dařilo. Navzdory pandemii","url":"https://www.businessinfo.cz/clanky/investorum-i-startupum-se-v-cr-loni-darilo-navzdory-pandemii/"}]

Links: [{"title":"K přípustnosti nepeněžitých 
… [skrátené, 7060 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b12.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b12.json",
  "content": "[\n  {\n    \"candidate_id\": \"C096\",\n    \"website\": \"https://eterus.sk\",\n    \"identity\": [],\n    \"hq_country\": {\"value\": \"SK\", \"value_text\": \"Gorkého 4, Bratislava\", \"source_url\": \"https://eterus.sk\", \"quote\": \"Gorkého 4, Bratislava\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"investor_type\": {\"value\": [\"pe\"], \"value_text\": \"private equity\", \"source_url\": \"https://eterus.sk\", \"quote\": \"Do inovácií sme formou private equity investovali už viac než 40 mil. EUR.\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"investments\": [\n      {\"value\": {\"company\": \"Sygic\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"Sygic\", \"source_url\": \"https://eterus.sk/portfolio\", \"quote\": \"Sygic\", \"published_date\": null, \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"HOPIN\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"HOPIN\", \"source_url\": \"https://eterus.sk/portfolio\", \"quote\": \"HOPIN\", \"published_date\": null, \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"Eyerim\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"Eyerim\", \"source_url\": \"https://eterus.sk/portfolio\", \"quote\": \"Eyerim\", \"published_date\": null, \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"Saneca Pharma\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"Saneca Pharma\", \"source_url\": \"https://eterus.sk/portfolio\", \"quote\": \"Saneca Pharma\", \"published_date\": null, \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"GroupSolver\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"GroupSolver\", \"source_url\": \"https://eterus.sk/portfolio\", \"quote\": \"GroupSolver\", \"published_date\": null, \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"MTBIKER\", \"date\": null, \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"MTBIKER\", \"source_url\": \"https://eterus.sk/portfolio\", \"quote\": \"MTBIKER\", \"published_date\": null, \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"Dr. Martin Dental Clinic\", \"date\": \"2024-05\", \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"Dr. Martin Dental Clinic\", \"source_url\": \"https://www.oaklins.com/se/en/deals/110583/\", \"quote\": \"Dr. Martin Dental Clinic, a leading network of dental clinics in Slovakia, has received a significant investment from Eterus Capital and Ethernum Capital\", \"published_date\": \"2024-05\", \"derivation\": \"stated\"},\n      {\"value\": {\"company\": \"EC Pharmacies\", \"date\": \"2024-08\", \"round\": \"unknown\", \"amount\": null}, \"value_text\": \"EC Pharmacies\", \"source_url\": \"https://www.oaklins.com/se/en/deals/110584/\", \"quote\": \"Eterus Capital has acquired a majority stake in EC Pharmacies\", \"published_date\": \"2024-08\", \"derivation\": \"stated\"}\n    ],\n    \"sectors\": null,\n    \"stages\": {\"value\": [\"growth\"], \"value_text\": \"vo fáze rastu\", \"source_url\": \"https://eterus.sk\", \"quote\": \"Eterus je partner pre financovanie spoločností vo fáze rastu, so schopným managementom a overeným konceptom.\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"ticket\": {\"value\": {\"min\": \"2\", \"max\": \"2,5 mil. EUR\", \"currency\": \"EUR\"}, \"value_text\": \"v rozmedzí 2 - 2,5 mil. EUR\", \"source_url\": \"https://eterus.sk\", \"quote\": \"Zameriavame sa na investície v rozmedzí 2 - 2,5 mil. EUR, pričom preferovaná dĺžka investície predstavuje 5-7 rokov.\", \"published_date\": null, \"derivation\": \"stated\"},\n    \"total_capital\": null,\n    \"funds\": [],\n    \"red_flags\": [],\n    \"not_found\": [\"identity\", \"sectors\", \"total_capital\"
… [skrátené, 9633 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w2_b12.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch w2_b12 done. Output written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w2_b12.json (5 records).\n\n- C096 Eterus Capital: PE, SK (Bratislava), 8 investments (6 from eterus.sk/portfolio, Dr. Martin 2024-05 and EC Pharmacies 2024-08 via Oaklins). Ticket 2 to 2,5 mil. EUR, stage growth. Fund and total capital not stated. No early exit. Doubt: WOOD & Company is named as fund manager in third-party sources only, not used.\n- C197 Rockaway Ventures: VC, Czech-based, 6 investments, latest Apptronik (Lupa, 2026-02-13). Funds: Rockaway Ventures II nearly EUR 55M; Fund I has only a 100M EUR target, so size left null. Ticket not stated on the site. No early exit. Doubt: the Prague location and the 2025-05-16 tech.eu date.\n- C077 QI investiční společnost: early exit no_investment_found. Website qiis.cz failed (TLS mismatch); IČO and funds could not be verified from fetchable sources. Leads not used: STARTEEPO Invest fund and the 2024 annual report PDF (not readable via WebFetch).\n- C087 TMF Czech a.s.: advisory (compliance/admin services), Prague 2, early exit no_investment_found, no IČO shown.\n- C204 CEC Capital SK s.r.o.: early exit no_investment_found; no website or source found. The only \"CEC Capital\" hits are an unrelated real estate group (Mint Investments)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

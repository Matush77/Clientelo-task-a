# Subagent: Evidence v2 wave1 batch 06 (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 20:21:28

Read the instructions in C:\Users\matus\Desktop\Interview_Project\Project_a\prompts\evidence_agent.md ("Evidence agent – v2") with the Read tool and follow them exactly.

Your batch file (5 candidates): C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w1_b06.json
Write your output to: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w1_b06.json

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

<details><summary>🔧 Read – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\batches\w1_b06.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\batches\\w1_b06.json"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	[
2	  {
3	    "candidate_id": "C033",
4	    "name": "Thein",
5	    "other_names": [],
6	    "known_website": "www.thein.eu",
7	    "registry_hint": null
8	  },
9	  {
10	    "candidate_id": "C014",
11	    "name": "Depo Ventures",
12	    "other_names": [
13	      "DEPO Ventures",
14	      "DEPO Ventures One SCSp",
15	      "DEPO Ventures Sàrl"
16	    ],
17	    "known_website": null,
18	    "registry_hint": null
19	  },
20	  {
21	    "candidate_id": "C145",
22	    "name": "Presto Ventures",
23	    "other_names": [],
24	    "known_website": null,
25	    "registry_hint": "possible registry match (unconfirmed, may be a different company): Presto Ventures II a.s., osoba rizikového kapitálu, IČO 11678704"
26	  },
27	  {
28	    "candidate_id": "C110",
29	    "name": "Danube Capital Advisors",
30	    "other_names": [],
31	    "known_website": null,
32	    "registry_hint": "possible registry match (unconfirmed, may be a different company): DANUBE Capital Advisors s. r. o., IČO 48279943"
33	  },
34	  {
35	    "candidate_id": "C142",
36	    "name": "Euroventures",
37	    "other_names": [],
38	    "known_website": null,
39	    "registry_hint": null
40	  }
41	]
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
  "url": "https://www.thein.eu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, investments, portfolio, fund size, ticket, team, office address, contact or kontakt, and the page's publication date. Also return the legal company name and any IČO / company ID if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Thein investment fund Czech portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
getaddrinfo ENOTFOUND www.thein.eu
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Thein investment fund Czech portfolio"

Links: [{"title":"tomas budnik pokracuje v budovani miliardove skupiny a hlasi dve prumyslove akvizice","url":"https://forbes.cz/tomas-budnik-pokracuje-v-budovani-miliardove-skupiny-a-hlasi-dve-prumyslove-akvizice/"},{"title":"nemci budou muset bouchnout do stolu rika filip budnik k vyvoji v prumyslu","url":"https://forbes.cz/nemci-budou-muset-bouchnout-do-stolu-rika-filip-budnik-k-vyvoji-v-prumyslu/"},{"title":"Kupuje IT firmy i slévárny, roky dělal pro Kellnera. Investovat mě učily poštovní známky, říká","url":"https://cc.cz/kupuje-it-firmy-i-slevarny-roky-delal-pro-kellnera-investovat-me-ucily-postovni-znamky-rika/"},{"title":"driv ppf i penta dnes vede vlastni investicni skupinu navrat ke korenum rika budnik","url":"https://forbes.cz/driv-ppf-i-penta-dnes-vede-vlastni-investicni-skupinu-navrat-ke-korenum-rika-budnik/"},{"title":"thein tomase budnika resi dalsi problem prumyslova vetev prisla o status fondu","url":"https://forbes.cz/thein-tomase-budnika-resi-dalsi-problem-prumyslova-vetev-prisla-o-status-fondu/"},{"title":"HQ - Prague","url":"https://app.mergerlinks.com/companies/thein"},{"title":"app.mergerlinks.com","url":"https://app.mergerlinks.com/companies/thein/team"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/investice/?pi=13"},{"title":"Investment funds in the Czech Republic and their performance","url":"https://vskp.vse.cz/english/87899"},{"title":"Tvorba investičního portfolia pro fond kvalifikovaných investorů","url":"https://dspace.vut.cz/items/0add4fb4-4dfb-48df-873d-8f69876b3a8c"}]

Thein is a Czech investment group that Tomáš Budník set up in 2020 after leaving PPF. Thein was founded by Tomáš Budník in 2020, when he left the PPF financial group, where he had led the O2 operator and its telecom division. The sources describe two arms: an IT/cybersecurity side and an industrial side. The group looks for investment opportunities in IT, cybersecurity and industry, and combines them synergistically.

**Industrial portfolio**
- Its first industrial acquisition was the engineering company Ponec.
- In April, Thein bought Železniční dodavatelská, which is the largest private supplier of locomotive spare parts in the Czech Republic and Slovakia.
- The most recent acquisition is Cotring, a Czech firm doing contract welded manufacturing, whose customers are mainly Swiss and German companies.
- The industrial sub-fund was reportedly meant to invest mainly in majority stakes in engineering and railway companies. Energy and chemicals were also named as target sectors.
- A new fund was reportedly being opened to raise up to €500 million over the following year and a half, aimed at the DACH region (Germany, Austria, Switzerland).

**Recent problems**
- According to Hospodářské noviny, as reported by Forbes, the Czech National Bank stripped Thein Private Equity SICAV of its investment fund status, and its investors are waiting for next steps. The report
… [skrátené, 902 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://thein.eu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, investments, portfolio, fund size, ticket, team, office address, contact or kontakt, and the page's publication date. Also return the legal company name and any IČO / company ID if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/thein-tomase-budnika-resi-dalsi-problem-prumyslova-vetev-prisla-o-status-fondu/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, investments, portfolio, fund status, SICAV, Železniční dodavatelská, Cotring, Ponec, the page's publication date, and the article's date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
getaddrinfo ENOTFOUND thein.eu
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The content provided contains only a headline, with no body text, publication date, or article date:

- "Thein Tomáše Budníka řeší další problém. Průmyslová větev přišla o status fondu"

This headline mentions Thein and fund status. It does not mention investments, portfolio, SICAV, Železniční dodavatelská, Cotring, or Ponec. The page's publication date and the article's date are not shown. To get the full set of matching sentences, please provide the complete article text.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Thein Tomáš Budník investiční skupina o nás kontakt",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/driv-ppf-i-penta-dnes-vede-vlastni-investicni-skupinu-navrat-ke-korenum-rika-budnik/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, investments, acquisitions, portfolio, fund size, the company names acquired, and the page's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The content you provided contains only a headline, with no body text. None of the requested items appear: there is no mention of Thein, acquisitions, portfolio, fund size, or named acquired companies, and no publication date.

The only line touching on investments is the headline:

"Dřív PPF i Penta, dnes vede vlastní investiční skupinu. Návrat ke kořenům, říká Budník | Forbes"

If you share the full article text, I can extract the requested sentences.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Thein Tomáš Budník investiční skupina o nás kontakt"

Links: [{"title":"ceka nas rok plny zmen rika investor do technologii tomas budnik","url":"https://www.newstream.cz/leaders/ceka-nas-rok-plny-zmen-rika-investor-do-technologii-tomas-budnik"},{"title":"Opustil korporace a investuje do IT, průmyslu i vodíku. Tomáš Budník chce českým firmám pomoct ve světě","url":"https://cc.cz/opustil-korporace-a-investuje-do-it-prumyslu-i-vodiku-tomas-budnik-chce-ceskym-firmam-pomoct-ve-svete/"},{"title":"driv ppf i penta dnes vede vlastni investicni skupinu navrat ke korenum rika budnik","url":"https://forbes.cz/driv-ppf-i-penta-dnes-vede-vlastni-investicni-skupinu-navrat-ke-korenum-rika-budnik/"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=59617"},{"title":"Investiční skupina Thein někdejšího Kellnerova manažera koupila benešovskou slévárnu Top Alulit","url":"https://cc.cz/investicni-skupina-thein-nekdejsiho-kellnerova-manazera-koupila-benesovskou-slevarnu-top-alulit/"},{"title":"Thein dál investuje. Kupuje IT firmu Aitcom a podíl v Cross Network Intelligence","url":"https://www.e15.cz/byznys/technologie-a-media/thein-dal-investuje-kupuje-it-firmu-aitcom-a-podil-v-cross-network-intelligence-1376469"},{"title":"Mentoring na míru: Udělejte další krok v rozvoji vašeho podnikání","url":"https://rostecky.cz/michal-vydrzel-tomas-budnik-t45774"},{"title":"forbes.cz","url":"https://forbes.cz/?p=427802"},{"title":"budoucnost patri vodiku a my chceme byt u toho rika sef skupiny thein tomas budnik","url":"https://ekonomickydenik.cz/budoucnost-patri-vodiku-a-my-chceme-byt-u-toho-rika-sef-skupiny-thein-tomas-budnik/"}]

I ran the search, but the results don't include Thein's "About us" or contact pages, so I couldn't confirm its official website or contact details. The press coverage does describe the group:

- **Founder and background:** Téměř celá profesní kariéra Tomáše Budníka byla spojena s oborem telekomunikací. Zastával nejvyšší manažerské posty ve společnostech GTS Czech, Mobilkom, PPF Mobile Services a O2 Czech Republic. He left PPF to build his own group, which začal zakládat na začátku roku 2020.
- **Focus:** The group invests in IT, industry and hydrogen. Hlavní důraz klade na IT, infrastrukturu a kybernetickou bezpečnost.
- **Structure:** Companies sit under separate brands by sector. For example, Thein Industry je průmyslově zaměřená část investiční skupiny Thein.
- **Deals:** The group bought the IT firm Aitcom, which je již třetí IT firmou, kterou Thein letos přidal do svého portfolia. It also acquired the aluminium foundry Top Alulit, though the price was not disclosed.
- **Funds:** Together with J&T, the group set up the J&T Thein SICAV fund for qualified investors. Its stated target is zhodnocení jejich kapitálu okolo 15 procent ročně.
- **Assets under management:** The figures conflict. One article says the group má už ve správě přes 600 milionů korun, while another says Budník manages dva investičn
… [skrátené, 401 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.e15.cz/byznys/technologie-a-media/thein-dal-investuje-kupuje-it-firmu-aitcom-a-podil-v-cross-network-intelligence-1376469",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, Aitcom, Cross Network Intelligence, investment, acquisition, the purchase price or amount, and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/investicni-skupina-thein-nekdejsiho-kellnerova-manazera-koupila-benesovskou-slevarnu-top-alulit/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, Top Alulit, the foundry, the acquisition, the price, and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page is dated **16 January 2024** (16. 1. 2024). I can't reproduce every relevant sentence in full because of the 125-character limit on quotes, so I've quoted shorter excerpts and paraphrased the rest:

1. **Acquisition:** The industrial arm of the Thein investment group, founded by former O2 CEO Tomáš Budník, bought the aluminium foundry Top Alulit in Benešov. The article's headline also describes the group as linked to a former Kellner manager.
2. **Price:** The group did not disclose the amount. Media reports put it close to half a billion Czech crowns: "Výši transakce skupina nechtěla sdělit, podle informací médií se ale suma blížila polovině miliardy korun."
3. **Company size:** Top Alulit employs about 180 people and has annual turnover above 400 million crowns: "Top Alulit zaměstnává přibližně 180 lidí a má roční obrat přes 400 milionů korun."
4. **Rationale:** Budník says the deal increases Thein's capacity and gives access to new customers and markets: "Akvizice Top Alulit nám umožňuje zvýšit naši kapacitu a kompetence pro výrobu a zpracování."
5. **Foundry business:** Top Alulit makes castings for the automotive, aerospace, electrical, engineering and food industries. About three quarters of output is exported: "Top Alulit se zaměřuje na výrobu odlitků pro automobilový, letecký, elektrotechnický a strojírenský průmysl."
6. **Thein Industry:** Thein Industry is the industrial part of the Thein group, focused on rail transport, energy and chemicals.
7. **Thein's founding:** Budník founded the Thein group in 2020, and his son Filip plays an important role in it: "Investiční skupinu Thein založil bývalý generální ředitel O2 Budník v roce 2020."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Note: I've truncated some sentences to stay within the 125-character limit per quote.

1. **Headline:** "Thein dál investuje. Kupuje IT firmu Aitcom a podíl v Cross Network Intelligence"
2. **Opening summary:** "Fond J&T Thein podnikatele Tomáše Budníka a J&T Private Equity Group kupuje pardubickou společnost Aitcom,"
3. **Photo caption:** "Tomáš Budník, zakladatel investiční skupiny Thein."
4. **Acquisition count:** "Aitcom je již třetí IT firmou, kterou Thein letos přidal do svého portfolia."
5. **Price:** "Cenu ani jedna ze stran transakce nezveřejnila."
6. **Earlier deal:** "Dříve v tomto roce Thein koupil společnost Síť, která byla s loňským obratem přes 500 milionů korun"
7. **Strategic rationale:** "Aitcom má být dalším krokem k sestavení komplexního informačně-komunikačního portfolia."
8. **Quote from Budník:** "„Aitcom se vhodně doplňuje se společností Síť."
9. **Quote from Budník (investment):** "vysvětluje rozhodnutí investovat do Aitcomu Budník."
10. **Aitcom's business:** "Aitcom se zabývá poskytováním komplexních služeb v oblasti informačních a komunikačních technologií,"
11. **CNI stake:** "Vedle Aitcomu Thein zároveň vstupuje do další tuzemské společnosti Cross Network Intelligence (CNI),"
12. **CNI stake (cont.):** "v níž získal desetiprocentní podíl."
13. **CNI business:** "CNI nabízí softwarovou platformu pro správu a modelování datových sítí."
14. **Fund focus:** "Fond J&T Thein SICAV se zaměřuje na investice do společností v oblasti informačních a komunikačních technologií,"
15. **Portfolio list:** "V portfoliu skupiny jsou Síť, net.pointers, Ponec a nově Aitcom."
16. **Publication date:** 22. prosince 2020
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/opustil-korporace-a-investuje-do-it-prumyslu-i-vodiku-tomas-budnik-chce-ceskym-firmam-pomoct-ve-svete/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, investments, funds, capital, assets under management (správa, spravuje, milionů korun, miliard), the investment focus sectors, ticket or investment size, office or Praha/Prague location, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article is dated **21 December 2021**. It covers these points:

- **Fund structure:** Thein's IT activities are financed by the investment fund J&T Thein SICAV, which is open to private qualified investors. It is a joint project of Tomáš Budník and J&T Private Equity, focused on private equity in IT and cybersecurity.
- **Assets under management:** With additional investors, the group manages over 600 million CZK. The article says "přes 600 milionů korun."
- **Industry sub-fund:** Set up in September without co-investment. Budník transferred his industrial assets to it, which generated about 70 million CZK in operating profit last year. The fund plans to raise up to one billion CZK from qualified and institutional investors.
- **Investment focus:** IT, infrastructure and cybersecurity are the main priorities. Industry (manufacturing and transport) and hydrogen technologies (via Hydrogenic Technology) are also included.
- **Not stated:** The article does not mention individual investment or ticket sizes, or an office location in Prague.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.thein.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Thein, investments, portfolio, the team, office address (sídlo, adresa, Praha), contact or kontakt, IČO, and the page's publication date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "J&T Thein SICAV sídlo adresa Praha Thein Private Equity",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
self signed certificate
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "J&T Thein SICAV sídlo adresa Praha Thein Private Equity"

Links: [{"title":"J&T SICAV, a.s., IČO: 24928771, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/24928771-jt-sicav-a-s"},{"title":"j t ventures cg sicav a s 08220867","url":"https://www.podnikatel.cz/rejstrik/j-t-ventures-cg-sicav-a-s-08220867/"},{"title":"j t arch convertible sicav a s 17409390","url":"https://www.podnikatel.cz/rejstrik/j-t-arch-convertible-sicav-a-s-17409390/"},{"title":"j t ventures iii sicav a s 22175903","url":"https://www.podnikatel.cz/rejstrik/j-t-ventures-iii-sicav-a-s-22175903/"},{"title":"JT&T s.r.o., IČO: 28489420, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/28489420-jtt-s-r-o"},{"title":"leiscan.com","url":"https://leiscan.com/lei/315700W315QK7T6A5C23"},{"title":"Michal Sadloň - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/michal-sadlon"},{"title":"16470 cee attorneys advises on sit sale to j t thein sicav","url":"https://ceelegalmatters.com/czech-republic/16470-cee-attorneys-advises-on-sit-sale-to-j-t-thein-sicav"},{"title":"Roman Hajda - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/roman-hajda"}]

Links: [{"title":"Relatorio Anual  Partners Group Global Value OIA","url":"https://santander.pt/pdfs/particulares/poupar-e-investir/oia/partners-group-global-value-oia/informacao-legal/info-financeira/Relatorio_Anual__Partners_Group_Global_Value_OIA.pdf"},{"title":"Majetková struktura SICAV pohledem korporátního práva","url":"https://dodo.is.cuni.cz/handle/20.500.11956/185009"},{"title":"Majetková struktura SICAV pohledem korporátního práva","url":"https://dspace.cuni.cz/handle/20.500.11956/185009"},{"title":"docta.ucm.es","url":"https://docta.ucm.es/rest/api/core/item/e8ca3ec7-c0b1-4172-a05c-b6f34243945d/export/endnote"},{"title":"sociedad de inversion de capital variable","url":"https://dineros.substack.com/p/sociedad-de-inversion-de-capital-variable"},{"title":"partners group global value i lu0392036694","url":"https://images.finanzen.ch/fonds/daten-gebuehr/partners-group-global-value-i-lu0392036694"},{"title":"partners group global value i lu0286628747","url":"https://script.finanzen.ch/fonds/daten-gebuehr/partners-group-global-value-i-lu0286628747"},{"title":"hf other legal structures","url":"https://awgmain.morningstar.com/webhelp/glossary_definitions/hedge_fund/hf_other_legal_structures.htm"},{"title":"partners group global value i lu0392036694","url":"https://adnz-oufeuofqus.finanzen.ch/fonds/daten-gebuehr/partners-group-global-value-i-lu0392036694"}]

Links: [{"title":"J&T SICAV, a.s., IČO: 24928771, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/24928771-jt-sicav-a-s"},{"title":"Smlouvy Dotace Platy Úřady Zakázky Sponzoři & firmy","url":"https://www.hlidacstatu.cz/subjekt/08220867"},{"title":"j t ventures cg sicav a s 08220867","url":"https://www.podnikatel.cz/rejstrik/j-t-ventures-cg-sicav-a-s-08220867/"},{"title":"5fda1b5f51de01b6ee37
… [skrátené, 3410 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/opustil-korporace-a-investuje-do-it-prumyslu-i-vodiku-tomas-budnik-chce-ceskym-firmam-pomoct-ve-svete/",
  "prompt": "Quote exactly, in the original Czech, the sentence(s) that mention 'J&T Thein SICAV' and describe its focus (for example 'private equity' or 'soukromého kapitálu' or 'investuje'), and any sentence that mentions 'většinový' or 'podíl' or 'akvizic' together with the group's investments. Copy word-for-word, do not translate or paraphrase."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Věty o J&T Thein SICAV** (zdrojový text je zkrácen kvůli limitu 125 znaků):

1. "IT aktivity celé skupiny jsou financovány z investičního fondu J&T Thein SICAV" – fond financuje IT aktivity skupiny.
2. "Tento fond je společným projektem Budníka a J&T Private Equity" – fond vznikl jako společný projekt s J&T Private Equity.
3. "je orientovaný na private equity do IT a kybernetické bezpečnosti" – fond se zaměřuje na private equity v IT a kybernetické bezpečnosti.

**Věty o akvizicích spojených s investicemi skupiny:**

- "Právě do těchto oblastí v posledních dvou letech Budník se svou skupinou mohutně investuje, dotáhl celou řadu akvizic" – skupina v posledních dvou letech investovala do IT, infrastruktury a kybernetické bezpečnosti a realizovala řadu akvizic.

Slova „většinový“ a „podíl“ se v článku nevyskytují.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "DEPO Ventures venture capital investments",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "DEPO Ventures SCSp Luxembourg fund team office",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "DEPO Ventures venture capital investments"

Links: [{"title":"DEPO Ventures","url":"https://funding.tech.eu/investors/DEPO%20Ventures"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/depo-ventures"},{"title":"depo ventures opens 20m angel fund","url":"https://en.ain.ua/2022/10/10/depo-ventures-opens-20m-angel-fund"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/depo-ventures-launches-fund"},{"title":"DEPO Ventures Research","url":"https://f4.fund/firms/depo-ventures"},{"title":"Venture Capital","url":"https://altss.com/profile/depo-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/depo-ventures"},{"title":"DEPO Ventures","url":"https://venturecapitalarchive.com/venture-funds/depo-ventures-depoventures-com"},{"title":"depo ventures","url":"https://www.vcbacked.co/directory/investors/depo-ventures"},{"title":"depo ventures","url":"https://prod.actual.seedtable.com/investors/depo-ventures"}]

DEPO Ventures is a Prague-based firm that backs pre-seed and seed startups, mainly in Central and Eastern Europe and the Baltics. It runs angel funds and a syndicate of co-investors, and the sources disagree on its portfolio size.

**Structure and focus**
- It was founded in 2016 and has grown from a community of angel investors into an institutional VC, according to f4.fund's profile. Its founders are listed as [REDACTED] and Petr Šíma. Waveup says the firm describes itself as operating the largest angel fund in the CEE region.
- Its DEPO Angels network co-invests alongside the fund and includes more than 200 business angels.
- Its current focus is emerging and disruptive technologies. Earlier funds spanned fintech, mobility, consumer marketplaces, and SaaS, but the current fund has narrowed toward strategic and critical infrastructure sectors.

**Check sizes and fund size**
- Sources give different check-size ranges. One says the typical ticket is €250K-500K under the current fund's parameters, with target entry valuations up to €7M. Another puts typical checks between €100,000 and €500,000, at valuations up to €3 million.
- The third fund was reported to aim for €20 million when it launched in 2022.

**Recent activity**
- In October 2026, DEPO was selected to manage a new fund backing startups from Ukraine, Moldova, and Georgia that want to expand into Czechia. National Development Investment, a subsidiary of the Czech National Development Bank, has committed €3.8 million, which could rise to €5.8 million if conditions are met.
- It frequently leads rounds. Examples include Tapaya's ~€1M pre-seed, WanderWallet's €430K pre-seed, and ArcSpace's €2M+ round.
- Its 2025–2026 deals include backing Prague-based stablecoin infrastructure startup Plexo.

**Notable portfolio companies**
Waveup lists Tatum, Spendee, Readmio, Kardi AI, Eterny, and Blockmate, spanning deep tech, fintech, software, and SaaS. Other sources also name Flowpay and NOLD.

**Po
… [skrátené, 834 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "DEPO Ventures SCSp Luxembourg fund team office"

Links: [{"title":"• Privacy Policy","url":"https://funds-europe.com/private-debt-in-luxembourg-expands-by-nearly-25/"},{"title":"The Easiest Way to Launch a Fund in Europe","url":"https://carta.com/blog/luxembourg-scsp/"},{"title":"DEPO Ventures Research","url":"https://f4.fund/firms/depo-ventures"},{"title":"50273 debevoise plimpton llp","url":"https://www.legal500.de/rankings/ranking/c-luxembourg/investment-funds/50273-debevoise-plimpton-llp"},{"title":"50273 debevoise plimpton llp","url":"https://www.legal500.fr/rankings/ranking/c-luxembourg/investment-funds/50273-debevoise-plimpton-llp"},{"title":"Venture Capital","url":"https://altss.com/profile/digital-space-ventures"},{"title":"Dechert Advises FORTY51 Ventures on the Closing of Its First Fund","url":"https://www.dechert.com/knowledge/news/2022/7/dechert-advises-forty51-ventures-on-the-closing-of-its-first-fun.html"},{"title":"DEPO Ventures","url":"https://venturecapitalarchive.com/venture-funds/depo-ventures-depoventures-com"},{"title":"www.staging93245.tridenttrust.com","url":"https://www.staging93245.tridenttrust.com/europe/luxembourg"},{"title":"depo ventures","url":"https://prod.actual.seedtable.com/investors/depo-ventures"}]

I didn't find any evidence that DEPO Ventures runs a Luxembourg SCSp or has a Luxembourg office. The results place DEPO in Prague, and the Luxembourg-linked hits are about other firms.

**What the results say about DEPO**
- Its main listing puts the firm's headquarters in Prague. Venture Capital Archive lists its global HQ as Prague, Czech Republic.
- One profile describes it as a Prague-based venture firm founded in 2016 that grew out of an angel investor community. It has evolved from a community of angel investors and co-investors into a professional institutional VC.
- Another source says it runs angel funds and brings in international investors through a network called DEPO Angels. DEPO Ventures manages DEPO Angel Funds, with a portfolio of 25 companies, and collaborates with international investors through The DEPO Angels network.
- For its current fund, one profile lists typical checks of €250K–500K. Typical ticket is €250K-500K per the current fund's stated parameters, with target entry valuations up to €7M.
- None of the sources I saw names the legal vehicle or domicile of DEPO's funds, so I can't confirm whether any of them is an SCSp.

**Luxembourg results that are about other firms**
- Digital Space Ventures is a separate firm. It is a Luxembourg-based fund with $50 million in assets, operating from London, Berlin, Vienna, and Zurich.
- FORTY51 Ventures is also unrelated. Its first fund, FORTY51 Ventures Fund I SCSp, FIAR, raised US$43 million and is domiciled in Luxembourg.
- For context on the vehicle itself, Carta describes the SCSp as a structure inspired by the Limited Partnership and has gained popularity in Luxembourg as the go to vehicle for venture capital funds f
… [skrátené, 391 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://depoventures.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions DEPO, investments, portfolio, funds, fund size, ticket, team, office address (Prague, Praha, office), contact, company legal name or IČO, and the page's publication date. Include the portfolio company names listed."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://depoventures.com/about",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions DEPO, the firm's history, team, office or headquarters location, ticket size, fund size, assets under management, legal name, and the page's publication date."
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
**Sentences mentioning the listed terms** (quotes capped at 125 characters, so longer sentences are excerpted):

**Homepage and positioning**
- "Investing in technologies reshaping Europe's critical Infrastructure"
- "Fueling inception & pre-seed companies strengthening Europe's critical infrastructure"
- "Backing early-stage founders since 2016"

**Key figures**
- "53 Portfolio Companies"
- "9M€ Capital deployed"
- "62% Follow-on rate"

**Value proposition**
- "Strategic capital Hands-on support for founders navigating early-stage challenges, from zero to first scale."
- "Wide network We leverage our global late-stage VC network to help our founders secure their next funding round."
- "Industry experts Senior industry experts from our Venture Partners, bringing deep domain knowledge."

**Investment criteria**
- "Stage Inception & Pre-seed"
- "Ticket €250K - 500K"
- "Valuation Up to €7M"
- "Geography Europe, CEE & Diaspora"
- "Industry Defence, Space,FinTech, Industry 4.0, Energy"

**Portfolio companies (named)**
- "TOP performing portfolio companies"
- Tatum, Evitado, Cardino, Flowpay, Kardi

**Testimonials**
- "We have been investing with Depo Ventures for about two years." (Sebastian Mach, Investor)
- "People at DEPO Ventures have clearly shown us how to make investments in startups west of us." (André Dravecký, Ringil)
- "We are planning another investment round, and we believe that we will be able to raise capital faster thanks to them." (André Dravecký, Ringil)
- "We also hope to get a lot from the huge network of angel investors, DEPO Angels, which will help us move the company..." (truncated to meet the limit)
- "After the pitch event, we were contacted by a number of interested investors including Michal from DEPO Angels fund I..." (truncated)
- "We are confident that the partnership with DEPO Ventures and the advice we receive from experienced investors..." (truncated)

**Company and contact details**
- "DEPO VENTURES s.r.o. - All rights reserved" (legal name as shown in the footer)
- "Plynární 10 street, Prague 7, Czech republic" (office address, shown as separate footer lines)
- "Contact" and "Portfolio" appear as navigation labels.

**Other notes**
- The page has no IČO (company registration number) and no explicit publication date. The footer shows only a copyright range, "© 2006 - 2026".
- Fund size isn't stated, beyond "DEPO Angels fund I." mentioned in a testimonial.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://depoventures.com/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, every sentence or name that mentions a portfolio company, investment, round, date, year, DEPO Ventures, or DEPO Angels fund, including any dates shown next to companies. List all portfolio company names shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "DEPO Ventures pre-seed round led 2025 startup raises",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**DEPO Ventures portfolio companies listed on the page:**

Tatum, BikeFair, Blockmate, Plexo, WanderWallet, Tapaya, Spendee, Otis, Ringil, Gitgut, Bolt, Upgrade Academy, DriveX, Zenoo, Evitado, Motourismo, Augmented Robotics, Kardi AI, Equiradar, Oxus AI, Pulse, Mileus, Forloop.ai, Smartguide, Skycorp Technologies, yummy, Beecom, Kareer, Flowpay, Encubate, Readmio, TATUM Blockchain Accelerator, Partory, Cardino, Traxlo, Talsec, Twinzo, CUID, Fungies.io, Wayren, Sign on Tab, Certifier, Acreom, Nold, Intellcre, BlueQubit, Masthead, Finlay.ai, Salu Health, Circuly, Webout, Beem, Neuronix, Talentpilot, Parcelsea, Bunch, Digital Transformation Systems (DTS), and Tapline.

**Selected language from the page:**

- Tagline: "We back early-stage founders building Europe's critical infrastructure." (The page's own wording; I've kept this short.)
- On the TATUM Blockchain Accelerator: "Together StartupYard, Tatum, and DEPO Ventures are bringing their business expertise, network, and investment" (truncated for length).
- Copyright line: "© 2006 - 2026 DEPO VENTURES s.r.o. - All rights reserved"

The page does not give investment amounts, round details, or specific investment dates for individual companies. It shows the fund and syndicate tabs (Fund I to IV, Syndicate, Exit), but the company entries don't say which category each belongs to, so I haven't assigned them.

I've summarized rather than reproducing every sentence verbatim, since the page repeats each company several times and a full copy would be long.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "DEPO Ventures pre-seed round led 2025 startup raises"

Links: [{"title":"Back to DEPO Ventures","url":"https://seedtable.com/investors/depo-ventures/portfolio"},{"title":"DEPO Ventures Research","url":"https://f4.fund/firms/depo-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/depo-ventures"},{"title":"Top Challenges Ukrainian Startups Face","url":"https://vestbee.com/insights/articles/Top-Challenges-Ukrainian-Startups-Face"},{"title":"Primary Job Title Partner Primary Organization DEPO Ventures","url":"https://crunchbase.com/person/petr-sima"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/depo-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/depoventures"},{"title":"2022 10 07 forloop ai pre seed","url":"https://startupintros.com/news/2022-10-07-forloop-ai-pre-seed"},{"title":"Venture Capital","url":"https://altss.com/profile/depo-ventures"},{"title":"Depth VC logo","url":"https://www.tryfundable.ai/investor/depth-vc"}]

The clearest 2025 pre-seed deal I found is CryptoSwift, but the evidence comes from data aggregators rather than a company announcement.

**2025 pre-seed deal**
- **CryptoSwift (Tallinn, crypto):** Seedtable's table marks DEPO as lead on this pre-seed round, dated 3 July 2025 and about $600K. CryptoSwift Lead 🇪🇪Tallinn, Estonia | Cryptocurrency | Pre Seed | 1 | 3 Jul 2025 | 3 Jul 2025 | 600K USD. CB Insights logs a $0.6M pre-seed entry for CryptoSwift dated 7/3/2025, but its excerpt doesn't show who led it. 7/3/2025 Pre-Seed - II CryptoSwift $0.6M

**Other 2025 DEPO-led rounds (not pre-seed)**
- **Kardi AI:** Seedtable marks DEPO as lead on a 28 April 2025 round of $2.8M, but at seed stage. Kardi AI Lead 🇨🇿Brno, Czech Republic | Software as a service (SaaS) | Seed | 1 | 28 Apr 2025 | 28 Apr 2025 | 2.8M USD

**Pre-seed rounds with unclear dates**
- One Vestbee article describes a pre-seed round co-led by Passion Capital and DEPO, but the excerpt doesn't name the startup or give a date, so I can't place it in 2025. The pre-seed funding round was co-led by Passion Capital and Depo Ventures.

**Pre-seed deals outside 2025**
- DEPO's most recent pre-seed lead I found is Tapaya, which Caplight dates to April 2026. Tapaya Apr 2026 Pre Seed Lead
- Sources disagree on WanderWallet. One profile says DEPO led its €430K pre-seed. led WanderWallet's €430K pre-seed (with BDPartners). Caplight lists DEPO only as a co-investor in WanderWallet's March 2026 pre-seed. WanderWallet Inc.Mar 2026Pre SeedCo-investor

For a definitive answer, check the CryptoSwift announcement or DEPO Ventures' own site, since these aggregator records don't always agree on lead status.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Kardi AI seed round DEPO Ventures investment press release",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Plexo stablecoin startup Prague DEPO Ventures funding",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Plexo stablecoin startup Prague DEPO Ventures funding"

Links: [{"title":"plexo 2","url":"https://app.dealroom.co/companies/plexo_2"},{"title":"Depo Ventures","url":"https://capboard.io/en/investor/depo-ventures"},{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/companies/depo_ventures/team"},{"title":"anton titov","url":"https://informaconnect.com/impact-funders-founders/speakers/anton-titov/"},{"title":"ecosystem.madrimasd.org","url":"https://ecosystem.madrimasd.org/companies/depo_ventures/team"},{"title":"depo ventures","url":"https://prod.actual.seedtable.com/investors/depo-ventures"},{"title":"DEPO Ventures","url":"https://www.premieralts.com/investors/depo-ventures/portfolio"},{"title":"Cryptocurrency Photo by Avi Rozen on Shutterstock","url":"https://benzinga.com/z/43723477"},{"title":"Plasma Raises $24M in Series A to Launch Dedicated Blockchain for Stablecoins, Backed by Peter Thiel","url":"https://stablecoininsider.org/tag/plasma/"},{"title":"Plasma Raises $24M in Series A to Launch Dedicated Blockchain for Stablecoins, Backed by Peter Thiel","url":"https://stablecoininsider.org/tag/stablecoins-321/"}]

The search didn't confirm any link between Plexo and DEPO Ventures, so I can't verify that DEPO invested in Plexo.

**What Plexo does:** It's a coordination layer for stablecoin payments, not a stablecoin issuer. Its Dealroom listing frames it as a coordination network for institutional stablecoin clearing (The coordination network for institutional stablecoin clearing.). The company presents itself as an alliance layer rather than an intermediary, and says it never takes custody of or moves client funds itself (Operating as an alliance layer rather than a financial intermediary, Plexo enables institutions with payment demand to connect with institutions holding local capacity... Plexo does not hold, transmit, convert, execute, or settle funds.). It is still validating its first end-to-end institution-to-institution clearing flow (Plexo is currently proving out its first end-to-end institution-to-institution clearing flow).

**Leadership:** Anton Titov is listed as CEO and co-founder. He has 13 years in fintech, including four years building cross-border stablecoin products and payment operations spanning more than 30 corridors. He was listed as a speaker at the IMPACT Funders & Founders 2026 event in New York, scheduled for September 11, 2026 (IMPACT Funders & Founders 2026 September 11, 2026 New York Marriott Marquis).

**Funding:** Dealroom's profile shows a seed-stage round of $290k for Plexo. The investor and date fields didn't load in the captured text, and the rest of the page is behind a paywall, so I couldn't see who the investors were.

**DEPO Ventures:** This is the Prague firm in the query. It is a venture capital fund supporting early-stage tech startups in Central and Eastern Europe and the Baltic regions. It focuses on seed and pre-seed deals, and manages DEPO A
… [skrátené, 894 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Kardi AI seed round DEPO Ventures investment press release"

Links: [{"title":"kardi ai raises 1 5m in seed funding","url":"https://en.ain.ua/2023/11/28/kardi-ai-raises-1-5m-in-seed-funding"},{"title":"seed 2025 04","url":"https://seedtable.com/companies/kardi-ai/funding-rounds/seed-2025-04"},{"title":"therecursive.com","url":"https://therecursive.com/?p=18033"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/kardi-ai/financials"},{"title":"Medicínský start-up KARDI AI získal investici 1,5 milionu EUR na další rozvoj","url":"https://www.businessinfo.cz/clanky/medicinsky-start-up-kardi-ai-ziskal-investici-15-milionu-eur-na-dalsi-rozvoj/"},{"title":"kardi ai prichazi s revolucnim resenim na urovni ekg ktere dokaze monitorovat srdce odkudkoli ziskava investici od depo ventures","url":"https://www.businessinfo.cz/clanky/kardi-ai-prichazi-s-revolucnim-resenim-na-urovni-ekg-ktere-dokaze-monitorovat-srdce-odkudkoli-ziskava-investici-od-depo-ventures/"},{"title":"Czech medtech Kardi AI raises €1.1M to expand heart monitoring tech","url":"https://tech.eu/2025/04/28/czech-medtech-kardi-ai-raises-1-1m-to-expand-heart-monitoring-tech/"},{"title":"therecursive.com","url":"https://therecursive.com/?p=40397"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/kardi-ai-secures-1-1m-for-heart-tech"}]

I didn't find an official press release from Kardi AI or DEPO Ventures in these results. The coverage comes from news outlets and funding databases, and they show DEPO Ventures in three rounds.

**Pre-seed (2022, €350K)**
- The Recursive reported that Kardi AI announced the closing of a €350K pre-seed round led by BrightCap Ventures, with the Czech angel syndicate DEPO Ventures participating.
- CB Insights dates the pre-seed to 5/25/2022.
- A Czech-language BusinessInfo.cz article on DEPO's entry describes the fund as the first investor alongside the Bulgarian VC fund BrightCap. It gives DEPO's share as roughly 80,000 euros, out of a total it lists as 8.5 million with the currency unstated. That total likely means CZK 8.5 million, about the €350K pre-seed, but that is my inference.

**Seed (November 2023, €1.5M)**
- ain.ua reported a €1.5M seed round in which the company was backed by Central and Eastern European VCs such as Purple Ventures, DEPO Ventures, also an existing investor, Cleverage.vc, Soulmates Ventures, Garage Angels, as well as other undisclosed angel investors.
- The stated goals include achieving EU MDR 2a compliance, further enhancing the product, and expanding its market presence.
- CB Insights lists this round on 11/28/2023.

**Seed II (April 2025, about €1.1M)**
- Tech.eu covered a €1.1M raise tied to international expansion and clinical validation. The round included existing backers BrightCap Ventures, DEPO Ventures, and Garage Angels, with new support from Lumus Investment Collective and a Czech angel investor.
- Planned markets are Poland, Slovakia, Bulgaria, and Romania in the
… [skrátené, 695 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2025/04/28/czech-medtech-kardi-ai-raises-1-1m-to-expand-heart-monitoring-tech/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Kardi AI, DEPO Ventures, Depo, the round, the amount raised (€ or EUR), the round type (seed, pre-seed), existing backers, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Tapaya pre-seed DEPO Ventures 2026 raises",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 28 April 2025

**Round type:** The article doesn't specify one (e.g., seed or pre-seed).

**Relevant sentences:**

1. "Czech healthtech startup Kardi AI, which has built an AI-powered chest strap that detects heart arrhythmias," (the sentence continues to describe the €1.1M round)

2. "The investment round included contributions from existing backers" followed by BrightCap Ventures, DEPO Ventures, and Garage Angels, with new support from Lumus Investment Collective and a Czech angel investor.

3. "Kardi's expansion will target Central and Eastern European countries" (followed by Poland, Slovakia, Bulgaria, Romania, then the UAE and India)

4. "With this new capital, the company is prioritizing expansion into regional and global markets."

5. "Kardi has already helped detect over 250 serious cases of arrhythmia"

6. "Kardi Ai has an exceptional, proven product that's already helping save lives."

7. "Kardi Ai is currently preparing for a clinical trial in partnership with university hospitals in Olomouc and Ostrava,"

Sentences longer than 125 characters are excerpted to stay within the quote limit.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Tapaya pre-seed DEPO Ventures 2026 raises"

Links: [{"title":"Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal","url":"https://financialit.net/news/fundraising-news/property-fintech-downpayments-launches-328m-initial-capital-unlock-equity-and?page=9"},{"title":"Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal","url":"https://financialit.net/news/fundraising-news/korr-secures-32-million-seed-funding-modernize-insurance-cloud-native-technology?page=6"},{"title":"Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal","url":"https://financialit.net/news/fundraising-news/tangible-secures-43m-seed-round-build-scalable?page=5"},{"title":"DEPO Ventures Research","url":"https://f4.fund/firms/depo-ventures"},{"title":"Tapaya logo","url":"https://seedtable.com/startups/Tapaya-EW99WJ8"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/depoventures"},{"title":"Funding Stage","url":"https://www.seedtable.com/companies/tapaya"},{"title":"Venture Capital","url":"https://altss.com/profile/depo-ventures"},{"title":"depo ventures","url":"https://prod.actual.seedtable.com/investors/depo-ventures"}]

Yes. Tapaya, a payments company, closed a pre-seed round in spring 2026 with DEPO Ventures as an investor. Sources agree on that, but they differ on the size and on who led.

- **Size:** Financial IT reports the round at €1 million. Seedtable records $1.2 million dated April 28, 2026. Those figures are consistent once currency is converted.
- **Lead:** Financial IT reports that Passion Capital headed the round, with DEPO as co-lead. F4's DEPO profile credits DEPO with leading the pre-seed and dates it to around April 2026. Caplight's DEPO page also lists DEPO in a lead role for the April 2026 pre-seed. I couldn't find a primary announcement to settle it, so the lead designation is still unresolved.
- **Other backers:** According to Financial IT, BADideas.fund followed on with additional investment.
- **Company:** Per Seedtable, three co-founders, Petr Zahradnik, Roman Kucharik, and Laura Dordova, started the company in 2025 to build payment acceptance infrastructure for businesses. Financial IT describes its core idea as letting merchants take in-person payments on any device.

Financial IT's "months ago" timestamps differ across copies of the same article, so I didn't use them to date the round. For the definitive lead investor, check Tapaya's or DEPO Ventures' official announcement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2025/04/28/czech-medtech-kardi-ai-raises-1-1m-to-expand-heart-monitoring-tech/",
  "prompt": "Find the full sentence that contains the words \"DEPO Ventures\" and return it exactly as written on the page, word-for-word, in English, without truncation, without summarising, without adding ellipses. Also return the exact sentence that states the total round amount (for example \"€1.1M\" or \"1.1 million\") if it is in the body text."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2022/10/10/depo-ventures-opens-20m-angel-fund",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions DEPO Ventures, the angel fund, fund name, fund size or target (€ or EUR or million), the vintage or year, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't return the full sentence verbatim because it exceeds the 125-character limit for quotes from source documents. Here are the relevant excerpts:

**DEPO Ventures sentence (paraphrased):** DEPO Ventures was one of the existing backers that contributed to the round, alongside BrightCap Ventures and Garage Angels. Lumus Investment Collective and a Czech angel investor joined as new backers.

**DEPO Ventures (exact excerpt):** "BrightCap Ventures, DEPO Ventures, and Garage Angels"

**Total round amount (exact excerpt):** "has closed a €1.1M round to support international expansion"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. **Headline:** "Czech DEPO Ventures opens €20M angel fund for early-stage startups from the CEE"
2. **Publication date:** "10 October, 2022, 17:35"
3. **Photo caption:** "[REDACTED] and [REDACTED], partners at DEPO Ventures"
4. **Opening paragraph:** "Prague-based venture capital firm DEPO Ventures announced the launch of its third angel fund."
5. **Fund target:** "The new fund is aiming €20 million and is currently looking for investors"
6. **Founding year and activities:** "Established in 2016 by [REDACTED] and [REDACTED], DEPO Ventures investment group manages angel funds"
7. **Market position:** "Currently, it is one of the most active investors in the Czech Republic with 27 portfolio startup companies"
8. **Fund focus:** "The third angel fund focuses on investing in early-stage startups that develops projects in the areas of"
9. **Investor target:** "DEPO Ventures says it wants to attract not only qualified private investors but also institutional and family offices"
10. **Fund aim:** "The aim of the new angel fund is to support talented tech founders from Central and Eastern Europe"
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal\"",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal""

Links: [{"title":"Back to feed","url":"https://insights.munich-startup.de/news/feed/tapaya-raises-1-1m-to-turn-any-device-into-a-payment-terminal"},{"title":"tapaya erhaelt 1 mio euro fuer software basierte payment terminals","url":"https://www.startbase.com/news/tapaya-erhaelt-1-mio-euro-fuer-software-basierte-payment-terminals/"},{"title":"Tapaya raises €1M pre-seed to power payments on any device","url":"https://tech.eu/2026/04/28/tapaya-raises-eur1m-pre-seed-to-power-payments-on-any-device/"},{"title":"ibsintelligence.com","url":"https://ibsintelligence.com/?p=573459"},{"title":"pre seed 2026 04","url":"https://seedtable.com/companies/tapaya/funding-rounds/pre-seed-2026-04"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/tapaya-secures-1-m"},{"title":"Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal","url":"https://financialit.net/news/fundraising-news/property-fintech-downpayments-launches-328m-initial-capital-unlock-equity-and?page=9"},{"title":"Tapaya Raises €1M Pre-Seed to Turn Any Device Into a Payment Terminal","url":"https://financialit.net/news/fundraising-news/korr-secures-32-million-seed-funding-modernize-insurance-cloud-native-technology?page=6"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/blog/articles/tapaya-secures-1-m"}]

The search turned up several write-ups of the same April 2026 announcement. Financial IT's listing uses your exact headline, though its snippet is brief.

- **Round and investors:** The round was led by Passion Capital and co-led by Depo Ventures, with follow-on backing from BADideas.fund. Prague-based fintech startup Tapaya has closed a pre-seed financing round of 1 million euros.
- **Product:** Tapaya's platform lets developers add card acceptance on Android, iOS, and other commercial devices. Its platform allows developers to enable payment acceptance across Android, iOS, and other commercial devices, effectively turning standard hardware into payment terminals and removing the need for dedicated devices.
- **Target buyers:** Banks, fintechs, and software platforms are the main audience. It provides a multi-platform SDK that companies can embed into their apps so smartphones, tablets, kiosks, or other commercial hardware can accept payments directly.
- **Use of funds:** The capital will be used for the certification of the platform and the further development of the company's own payment infrastructure.
- **Founders and origin:** Founded in 2025 by Laura Ďorďová, Roman Kuchařík and Petr Zahradník, Tapaya consolidates compliance, certification and processor integrations into a single software layer.
- **Goals and geography:** By simplifying integration and reducing reliance on third parties, the company aims to shorten implementation timelines from months to days. The company is already working on integrations in the Czech
… [skrátené, 471 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2026/04/28/tapaya-raises-eur1m-pre-seed-to-power-payments-on-any-device/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Tapaya's round, pre-seed, DEPO Ventures, Depo, Passion Capital, BADideas, the amount raised (€ or EUR), the lead or co-lead investor, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article reports that Prague-based Tapaya closed a **"€1 million in a pre-seed funding round"** led by Passion Capital. Depo Ventures joined as co-lead, and BADideas.fund made a follow-on investment. The piece was published on 28 April 2026.

Headline: "Tapaya raises €1M pre-seed to power payments on any device"

Funding use: "The funding will be used to complete Tapaya's PCI MPoC certification"
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Presto Ventures investiční fond investice startup",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Presto Ventures\" venture capital investor",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Presto Ventures" venture capital investor"

Links: [{"title":"Impact investor","url":"https://privateequitylist.com/investors/presto-ventures"},{"title":"presto ventures","url":"https://superscout.co/investor/presto-ventures"},{"title":"Presto Ventures","url":"https://www.privateequitylist.com/investor/presto-ventures"},{"title":"Presto Ventures","url":"https://signal.nfx.com/firms/presto-ventures"},{"title":"Venture Capital","url":"https://altss.com/profile/presto-ventures"},{"title":"michal vojta","url":"https://startupintros.com/people/michal-vojta"},{"title":"Presto Ventures","url":"https://venturecapitalarchive.com/venture-funds/presto-ventures-crunchbase-com"},{"title":"Presto Ventures","url":"https://www.premieralts.com/investors/presto-ventures/portfolio"},{"title":"presto ventures","url":"https://prod.actual.seedtable.com/investors/presto-ventures"},{"title":"presto ventures","url":"https://dev.actual.seedtable.com/investors/presto-ventures"}]

Presto Ventures appears to be an early-stage venture capital firm founded in 2016, but the sources describe it inconsistently, so verify the details before relying on them.

- **Location:** One profile places the firm in Prague, Czech Republic, founded in 2016. Other listings differ. NFX lists offices in Berlin, Germany • Czech Republic • Zurich, Switzerland • Prague, Czech Republic, and one aggregator gives Sprague, Washington, United States.
- **Focus:** Sources describe two different strategies. One says the firm backs early-stage technology investments, particularly in the security, defense, and aerospace sectors. Another describes a firm specializing in early stage B2B software startups and online marketplaces from Central and Eastern Europe. A third lists data, enterprise software, and developer tools.
- **Stage and check size:** Investments usually come at the seed and Series A stages. Reported check sizes vary: one source gives €500k to €5M, another €800,000 to €8 million, and another up to $3 million.
- **Fund size:** Figures conflict. One source says the firm has invested more than €35M across two funds since 2016. Another puts its latest fund at €150M. AUM is listed as around $40m in one profile and around $196m in another.
- **Defense partnership:** Altss describes the firm as the venture arm of a partnership with Czechoslovak Group (CSG), running a €150M fund called Presto Tech Horizons, with a core team of six investment professionals. It also says the firm led Occam Industries' €3 million raise in February 2025 and co-invested in Firehawk Aerospace's $60 million round.
- **People:** Michal Vojta is a Venture Partner and serves as Chief Financial Officer at the firm (a finance professional and venture capital investor). NFX lists Stefan Adamcik as a partner.
- **Portfolio:** Seedtable names CloudTalk, Keboola, and Ready Player Me as notable investments.

The differences likely reflect outdated or mixed-up aggregator data, though I can't confirm that fr
… [skrátené, 217 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Presto Ventures investiční fond investice startup"

Links: [{"title":"Venture kapitál - strana 2","url":"https://www.finmag.cz/tema/venture-kapital?strana=2"},{"title":"Došlo k netradičnímu spojení startupových investorů a zbrojaře: Presto Ventures a Strnadovy CSG","url":"https://cc.cz/doslo-k-netradicnimu-spojeni-startupovych-investoru-a-zbrojare-presto-ventures-a-strnadovy-csg/"},{"title":"Hlavní obsah","url":"https://seznamzpravy.cz/clanek/263730"},{"title":"Regiony s velkým startupovým talentem. České Presto Ventures posílá peníze do Gruzie a Litvy","url":"https://cc.cz/regiony-s-velkym-startupovym-talentem-ceske-presto-ventures-posila-penize-do-gruzie-a-litvy/"},{"title":"Investiční fondy","url":"https://www.finmag.cz/tema/investicni-fondy"},{"title":"Startupoví Presto Ventures a zbrojařská CSG Michala Strnada rozjíždí fond. Mají v něm 4 miliardy","url":"https://cc.cz/startupovi-presto-ventures-a-zbrojarska-csg-michala-strnada-rozjizdi-fond-maji-v-nem-4-miliardy/"},{"title":"Czechoslovak Group buduje nový fond s Presto Ventures. Miliardy zamíří do obrany a bezpečnosti","url":"https://www.e15.cz/byznys/burzy-a-trhy/czechoslovak-group-buduje-novy-fond-s-presto-ventures-miliardy-zamiri-do-obrany-a-bezpecnosti-1416821"},{"title":"Presto Ventures launches €30M fund to support CEE startups","url":"https://en.ain.ua/2022/07/12/presto-ventures-launches-e30m-fund-to-support-cee-startups"},{"title":"vlastni startup uspesne prodal do dalsich ted investuje cesi prilis diskutuji a malo konaji chci to zmenit rika vojta rocek","url":"https://cc.cz/vlastni-startup-uspesne-prodal-do-dalsich-ted-investuje-cesi-prilis-diskutuji-a-malo-konaji-chci-to-zmenit-rika-vojta-rocek/"}]

**Presto Ventures** is a Prague-based venture capital firm that Přemysl Rubeš set up in 2016. It is an early-stage investor focused on founders in Central and Eastern Europe (CEE). It now has about 60 startups in its portfolio, into which it has put more than a billion crowns.

**Funds**
- **Fund I:** The first fund invested in 15 companies, including Georgia's Omofox, Lithuania's GoRamp, Ukraine's Finmap, Slovakia's Cloudtalk and Estonia's Wolf3D. The list also includes Slovakia's first unicorn, Cloudtalk, and Estonia's fastest-growing metaverse startup, Wolf3D.
- **Fund II:** This fund was reported at €30 million and aims for pre-seed and seed rounds in more than 40 B2B startups from CEE, including the Baltics, Balkans and Ukraine. Its ticket size can reach €3 million, and the firm says it also backs follow-on rounds (Its ticket size can range up to €3 million, and, according to the firm, it stays committed to follow-on rounds.).
- **Focus:** Partner Vojta Roček has said the second fund concentrates purely on B2B software. He is one of four managing partners, and alongside Přemysl Rubeš, Eduard Kučera and Roman Nováček he decides where the fund invests.

**Recent deals**
- **Presto Tech Horizons:** Presto is launching this fund with Czechoslovak Group (C
… [skrátené, 1474 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://prestoventures.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Presto, investments, portfolio, funds, fund size, ticket, team, office address or location, contact, legal company name or IČO, sectors, stages, and the page's publication date. List the portfolio company names shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/startupovi-presto-ventures-a-zbrojarska-csg-michala-strnada-rozjizdi-fond-maji-v-nem-4-miliardy/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Presto Ventures, the fund name, fund size (miliard, miliardy, milionů, €, korun), capital, the investment focus, ticket size, and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I won't reproduce every matching sentence word-for-word, since that would mean copying most of the page. Here's a summary in my own words, with a few short quotes.

**Presto Ventures overview**
- Presto is a venture investor that connects frontier technologies, strategic investment, and a stated purpose around security. The footer lists a Prague office.
- For founders, it targets post-revenue companies raising roughly €800k to €8M, with tickets of €500k to €5M. It focuses on advanced tech in security, defense, and aerospace, including dual-use software and hardware, and on companies with roots in NATO countries, its allies, or Israel.
- It describes itself as a co-builder that helps portfolio companies prepare for follow-on rounds in Western Europe and the US.

**For investors**
- The page says Presto has invested €40M+ since 2016 across two funds. It describes a new €150M fund focused on security, defense, and aerospace, with a dual-use emphasis.
- It reports that portfolio companies have attracted €300M in next-round funding, and that it is backed entirely by private money.
- It lists 60+ early-stage startups in its portfolio. In 2023, it says it reviewed more than 5,000 startups and met almost 3,000 founding teams.
- It says the team spends 300+ days a year across 20 countries. It quotes this line: "Every year, the team spends 300+ days across 20 countries."

**Team**
- The page emphasizes solid, authentic relationships and responsibility toward founders, investors, and each other.

**News**
- A Czech notice, dated 25/5/26, announces a general meeting of Presto Ventures II a.s. on 25 June 2026.
- Tech Horizons items from late 2024 cover the first investments in AI and defense (October 2024) and a podcast on venture capital and resilience tech (November 2024).
- A December 2024 TechCrunch item covers BlueQubit's $10M raise. The page doesn't say whether Presto invested in it.

**Portfolio companies shown**
1. Adam
2. Behavio
3. Blindspot Tech
4. Calypso
5. Carmine Finance
6. Choice QR
7. Citypay.io
8. Cloudtalk
9. Cruxo
10. Dillali
11. Elin.ai
12. Ellio Technology
13. Finmap
14. Getpin
15. GoRamp

The page doesn't show its own publication date, so I can't report one.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can quote short Czech excerpts, each under 125 characters, and paraphrase the rest in English. The article has no ticket size, and its headline gives 4 billion while the body gives 3.7 billion CZK (150 million EUR).

**Publication date**
- "26. 6. 2024" is shown on the page (26 June 2024).

**Headline**
- "Startupoví Presto Ventures a zbrojařská CSG Michala Strnada rozjíždí fond. Mají v něm 4 miliardy": Presto Ventures and CSG are launching a fund with 4 billion (CZK) in it.

**Fund name and focus**
- "Presto Tech Horizons bude jedním z největších fondů svého druhu v Evropě.": Presto Tech Horizons will be one of Europe's largest funds of its kind.
- "Podporovat bude startupy v oblasti obranných a bezpečnostních technologií.": The fund will back defence and security tech startups.
- "spouští investiční fond Presto Tech Horizons, ve kterém se zaměří": Presto Ventures and CSG are launching the Presto Tech Horizons investment fund, focused on defence and security tech.
- "Oborově se může jednat například o": The sectors listed include AI, cybersecurity, robotics, aerospace, and critical infrastructure protection.
- "plánuje podpořit desítky projektů": In NATO member countries and with allies, the fund plans to back dozens of dual-use projects.

**Fund size and capital**
- "Disponuje celkem 150 miliony eur, v přepočtu 3,7 miliardy korun.": The fund has 150 million EUR in total, about 3.7 billion CZK.

**Investors and partners**
- "CSG přitom zastává pozici industriálního partnera a jednoho z mnoha investorů fondu.": CSG is an industrial partner and one of many investors in the fund.

**Presto Ventures**
- "Venture kapitálové Presto Ventures patří mezi vůbec nejaktivnější startupové fondy u nás.": Presto Ventures is among the most active startup funds in the Czech Republic.
- "Presto Ventures investuje do rychle rostoucích technologických firem od roku 2016.": Presto Ventures has invested in fast-growing tech companies since 2016.
- "V portfoliu má přes šedesát startupů z dvaceti zemí": Its portfolio includes more than sixty startups from twenty countries.
- "vysvětluje zakladatel a šéf Presto Ventures Přemysl Rubeš": Founder and head Přemysl Rubeš explains the partnership.
- "Spojením sil Presta a CSG vzniká unikátní partnerství": Rubeš says the Presto–CSG combination creates a partnership unlike any in Europe.

**Photo captions**
- "Foto: Presto Tech Horizons"
- "Zástupci CSG a Presto Ventures": Photo of CSG and Presto Ventures representatives.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2022/07/12/presto-ventures-launches-e30m-fund-to-support-cee-startups",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Presto Ventures, the fund name, fund size or target (€, EUR, million), stages, ticket sizes, vintage, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/regiony-s-velkym-startupovym-talentem-ceske-presto-ventures-posila-penize-do-gruzie-a-litvy/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Presto Ventures, GoRamp, Omofox, Georgia, Gruzie, Litva, Lithuania, the amount invested (milionů, eur, dolarů, $), the round (seed, pre-seed, kolo), the investment date and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Presto Tech Horizons first investment startup defence seed round led by Presto Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "12 July, 2022, 21:00"

**Fund size and launch:**
- "Presto Ventures has launched Fund II, valued at €30 million."

**Target and stage:**
- "The Prague-based firm is looking to make pre-seed and seed investment rounds in more than 40 B2B startups from the CEE region" (paraphrase: the firm targets over 40 B2B startups in Central and Eastern Europe, including the Baltics, Balkans, and Ukraine, for pre-seed and seed rounds).

**Firm background and vintage:**
- "Presto Ventures was started in 2016 by Přemysl Rubeš." (Founded in 2016 by Přemysl Rubeš.)
- "It is an early-stage venture capital investment company empowering CEE startup founders." (Paraphrase: an early-stage VC firm that backs founders in the region.)

**Ticket size and follow-on:**
- "Its ticket size can range up to €3 million, and, according to the firm, it stays committed to follow-on rounds." Quoting this in full is under the 125-character limit (about 112 characters).

**Prior fund:**
- "With its first fund, Presto Ventures has invested in 15 startups" (Its first fund backed 15 startups.)

**Financing:**
- "The financing for Fund II is comprised solely of private sources" (Fund II is entirely privately financed, including family offices and some undisclosed entrepreneurs and exited founders.)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Note:** Full sentences exceed the 125-character quote limit, so I've provided shorter exact excerpts (each under 125 characters) and paraphrased the rest.

**Publication date:** "23. 6. 2022"

**Headline:** "České Presto Ventures posílá peníze do Gruzie a Litvy" names Presto Ventures, Georgia, and Lithuania.

**Lithuania and GoRamp:**
- "Litevská společnost GoRamp se totiž mimo jiné strefila do správné doby" introduces GoRamp as a Lithuanian company.
- GoRamp's round totals €1.5 million: "V GoRamp se významně podílí na částce 1,5 milionu eur, kterou teď do firmy vložilo víc investorů."
- The article describes this as GoRamp's third investment round with Presto: "pro Presto šlo už o třetí investiční kolo v této společnosti."
- Presto says it is now the second-largest participant in that round: "jsme nyní druhý největší účastník tohoto kola."

**Georgia and Omofox:**
- "gruzínská společnost Omofox" identifies Omofox as a Georgian company.
- Omofox raised $700,000 (700 tisíc dolarů), and Presto became its only institutional investor: "Ve firmě Omofox, která získala 700 tisíc dolarů, se Češi stali jediným institucionálním investorem."
- Presto invested under standard seed terms: "Vložili jsme naprostou většinu částky za standardních seed podmínek."
- The article also says Presto's Georgia investment is its first there, and its Lithuania portfolio has four investments: "V Litvě už máme čtyři investice, v Gruzii je to investice první."

**Presto Ventures:**
- Presto is described as a venture capital firm: "Presto je venture kapitálová firma, která propojuje strategické investice a…"
- The article also notes that Presto has contacts and a good reputation in Georgia.

**Investment date:** The article does not state a specific investment date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Presto Tech Horizons first investment startup defence seed round led by Presto Ventures"

Links: [{"title":"therecursive.com","url":"https://therecursive.com/?p=37702"},{"title":"navigace pro drony nebo ai strnaduv fond hlasi prvni investice do zbrojnich startupu","url":"https://forbes.cz/navigace-pro-drony-nebo-ai-strnaduv-fond-hlasi-prvni-investice-do-zbrojnich-startupu/"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=50815"},{"title":"presto ventures and csg launch e150m fund","url":"https://siliconcanals.com/presto-ventures-and-csg-launch-e150m-fund/"},{"title":"Presto Ventures teams up CSG to invest €150 million in frontier technologies and security innovations","url":"https://czechoslovakgroup.com/en/news/presto-tech-horizons"},{"title":"Presto Ventures teams up CSG to invest €150 million in frontier technologies and security innovations","url":"https://csg.com/en/news/presto-tech-horizons"},{"title":"therecursive.com","url":"https://therecursive.com/?p=36024"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/presto-ventures"},{"title":"strnad se pousti do venture kapitalu jeho csg ma v hledacku zbrojarske startupy","url":"https://forbes.cz/strnad-se-pousti-do-venture-kapitalu-jeho-csg-ma-v-hledacku-zbrojarske-startupy/"}]

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/bavovna-ai-raises-1-7m-for-uav-navigation"},{"title":"navigace pro drony nebo ai strnaduv fond hlasi prvni investice do zbrojnich startupu","url":"https://forbes.cz/navigace-pro-drony-nebo-ai-strnaduv-fond-hlasi-prvni-investice-do-zbrojnich-startupu/"},{"title":"Nový fond z dílny CSG a Presto Ventures oznámil tři investice. Všechny jsou do AI","url":"https://www.e15.cz/byznys/novy-fond-z-dilny-csg-a-presto-ventures-oznamil-tri-investice-vsechny-jsou-do-ai-1419518"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/presto-ventures"},{"title":"news.aibase.com","url":"https://news.aibase.com/news/12675"},{"title":"news.aibase.com","url":"https://news.aibase.com/ja/news/12675"},{"title":"news.aibase.com","url":"https://news.aibase.com/zh/news/12675"},{"title":"Venture Capital","url":"https://altss.com/profile/presto-ventures"},{"title":"Presto Tech Horizons news – Presto Tech Horizons Welcomes First Portfolio Investments and a New Partner, Lucie Bresova","url":"https://startuprise.co.uk/presto-tech-horizons-welcomes-investments/"}]

The search doesn't support the premise as stated. The first portfolio announcement covered three companies, not one, and I found no source saying Presto Ventures led a seed round in any of them.

**The first portfolio (October 2024)**
The fund's first announcement, dated 23 October 2024, named three companies: Vidar Systems, Bavovna and Tur.ai. The Presto Tech Horizons investment fund welcomes its first three portfolio companies: Vidar Systems, a developer of portable acoustic locators; Bavovna, a hybrid AI system for autonomous drone n
… [skrátené, 1703 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://startuprise.co.uk/presto-tech-horizons-welcomes-investments/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Presto Tech Horizons, Presto Ventures, CSG, Vidar Systems, Bavovna, Tur.ai, the investment, pre-seed or seed round, amount, the lead investor, and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Occam Industries €3 million raise Presto Tech Horizons led TechCrunch",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://prestoventures.com",
  "prompt": "Return the exact footer text and any address lines verbatim (for example lines containing Prague, Praha, Czech Republic, street names, office, Berlin, Zurich), and the exact sentence about the team spending days across countries. Copy word-for-word, do not summarise."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Footer (verbatim):**
Created by [Matbold®](https://www.matbold.com/)
© 2024 Presto Ventures

**Address lines (verbatim):**
- Slovanský dům, Senovážné náměstí 869/28
- 110 00 Prague 1, Czech Republic

The page does not mention Berlin or Zurich. A Czech news item also gives a registered address: "Na příkopě 859/22, Nové Město, 110 00 Praha 1."

**Team sentence (verbatim):**
"Every year, the team spends 300+ days across 20 countries."

**Summary of the page:**
Presto Ventures is a Prague-based venture investor that backs security, defense, aerospace, and dual-use tech startups. It invests from Seed to Series A, with tickets of €500k to €5M, and focuses on NATO countries, its allies, and Israel. The firm reports €40M invested since 2016 from two funds, a new €150M fund, 60+ early-stage portfolio companies, and €300M in next-round funding raised by portfolio companies. Its portfolio includes Cloudtalk, Citypay.io (co-invested with Tether), and Carmine Finance.

**News items:**
- Presto Ventures II a.s. called a shareholders' meeting for 25 June 2026.
- BlueQubit's headline reads "BlueQubit raises $10M to take Quantum software into real-world applications" (TechCrunch, December 2024).
- The Tech Horizons arm announced "Presto Tech Horizons Announces First Investments in AI and Defense" (October 2024).
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 23 October 2024 (Oct 23, 2024, per the page byline)

**Key details (quotes capped at 125 characters; other points paraphrased):**

- **Fund and investment:** The article says "The Presto Tech Horizons investment fund welcomes its first three portfolio companies." Presto Tech Horizons is backed by Presto Ventures and Czechoslovak Group (CSG), and it plans to invest €150 million in NATO-country and allied tech projects.
- **CSG's position:** CSG Vice Chairman and COO David Chour says "For the future of CSG, it's crucial we stay at the forefront of global technological innovation."
- **Presto Ventures:** The article describes it as one that "connects frontier technologies, strategic investments, and purpose to create a safer, more secure future."
- **Portfolio companies:** Bavovna (a US-Ukrainian team building hybrid AI navigation for drones that works when GPS is disrupted), Vidar Systems (portable AI acoustic locators already used by the Ukrainian military), and Tur.ai (a Dutch startup building real-time robotic process automation for enterprises).
- **Funding details:** The article does not name a pre-seed or seed round, an amount for these specific companies, or a lead investor.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Occam Industries €3 million raise Presto Tech Horizons led TechCrunch"

Links: [{"title":"pre seed 2026 02","url":"https://seedtable.com/companies/occam/funding-rounds/pre-seed-2026-02"},{"title":"Occam Industries Ltd","url":"https://www.preqin.com/data/profile/asset/occam-industries-ltd/789225"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/occam-industries/financials"},{"title":"occam industries 2026 seed funding","url":"https://www.startupmag.co.uk/funding/occam-industries-2026-seed-funding/"},{"title":"occam industries secures 4 3m","url":"https://www.trysignalbase.com/news/funding/occam-industries-secures-4-3m"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/presto-technologies/financials"},{"title":"- The Bridge Club","url":"https://thebridgeclub.beehiiv.com/p/presto-tech-horizons-fund-invests-150m-in-startups"},{"title":"occam industries occam industries funding","url":"https://fundediq.co/occam-industries-occam-industries-funding/"},{"title":"bohemia venture capital","url":"https://www.cbinsights.com/investor/bohemia-venture-capital"}]

I didn't find a TechCrunch article in these results, so I can't confirm what TechCrunch reported. The results do describe a €3 million round led by Presto Tech Horizons, but the sources disagree on the date and some other details.

**The round as described**
- Seedtable's page reports that the London-based drone-autonomy company took in €3 million (about £2.6 million) in pre-seed funding. The money is meant to speed up deployment of its AI software on frontline unmanned systems in Ukraine and with European defence partners.
- Seedtable names Presto Tech Horizons as the lead, describing it as a resilience-focused venture fund backed by defence-industrial group Czechoslovak Group (CSG).
- Antler, Freedom Fund and TYR.vc also put money in, alongside several defence and security industry angel investors.

**Conflicting reports**
- **Date and lead investor:** Preqin dates the €3 million round to December 1, 2025, and credits "Presto Ventures" rather than Presto Tech Horizons as lead (led by Presto Ventures with contributions from Antler, Freedom Fund Venture Capital, and T|Y|R.vc). CB Insights instead records a Pre-Seed for $3.58M on February 11, 2026. Presto Technologies invested in Occam Industries's Pre-Seed funding round.
- **Amount:** Signalbase reports a $4.3 million raise, with Tech Horizons among the participants (secured $4.3M in new investment. The funding round drew participation from a notable group of investors, including North Ventures, Sparkmind Capital, Grenadyr, Antler, Tech Horizons, T|Y|R.vc, and Freedom Fund VC.). FundedIQ logs a $4.3 million pre-seed announced in September 2026. These may be a later round or a different one.
- **Possibly a different company:** StartupMag describes a £3.3 million seed for a Ukrainian business it calls M-Fly (Occam Industries), to scale gimbal production. That is hardware, unlike the 
… [skrátené, 459 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://startuprise.co.uk/presto-tech-horizons-welcomes-investments/",
  "prompt": "Return the exact sentences, word-for-word in English, that contain the words \"Bavovna\", \"Vidar Systems\", or \"Tur.ai\". Do not summarise. Copy each full sentence as it appears on the page, truncated only if it exceeds 125 characters, and say so."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://prestoventures.com",
  "prompt": "Return word-for-word, without summarising or translating, the exact sentences that state the investment criteria: the investment stages (for example Seed or Series A), the ticket size or check size (€ amounts), the sectors or focus areas (for example security, defense, aerospace, dual-use), and the number of portfolio companies. Copy each sentence exactly as written."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1. "The Presto Tech Horizons investment fund welcomes its first three portfolio companies: Vidar Systems, a developer of portable" *(truncated; the original sentence is longer)*

2. "Bavovna : The US-Ukrainian team has developed a hybrid AI-driven navigation system that allows unmanned vehicles (UVs) to op" *(truncated; the original sentence is longer)*

3. "Vidar Systems : A tech firm specializing in portable AI-driven acoustic locating systems." *(not truncated)*

4. "Tur.ai : A Dutch startup developing next-generation robotic process automation (RPA) for enterprises." *(not truncated)*
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Investment stage and ticket size:**
- Heading: "Seed TO SERIES A"
- "Mostly post-revenue companies raising a €800k to €8M financing round, looking to accelerate their growth."
- "Tickets ranging from €500k to €5M."

**Sectors and focus areas:**
- "Security, defense, and aerospace."
- "Cutting-edge and dual-use solutions, both software and hardware, capable of solving the most pressing global challenges."
- "Supporting advanced tech innovators with foundations or a significant operational focus in the countries of NATO," (truncated to fit the 125-character limit; the full sentence continues with "its allies, and the startup nation of Israel.")
- "Our new €150M fund targets the best of security, defense, and aerospace tech, with focus on dual-use."

**Number of portfolio companies:**
- "A portfolio of 60+ early-stage startups across two funds."
- "Will continue to focus on advanced solutions addressing complex industrial and security issues."
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Danube Capital Advisors investment",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Danube Capital Advisors\" fund startups Central Europe",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Danube Capital Advisors investment"

Links: [{"title":"danube angels","url":"https://wienerborse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels"},{"title":"THOMAS DYWREMOSE A0EWBD","url":"https://ca.marketscreener.com/insider/THOMAS-DYWREMOSE-A0EWBD/"},{"title":"THOMAS DYWREMOSE A0EWBD","url":"https://de.marketscreener.com/insider/THOMAS-DYWREMOSE-A0EWBD/"},{"title":"THOMAS DYWREMOSE A0EWBD","url":"https://ch.zonebourse.com/insider/THOMAS-DYWREMOSE-A0EWBD/"},{"title":"Danube Fund (OriensFund I) Overview","url":"https://pitchbook.com/profiles/fund/12664-18F"},{"title":"Danube Advisory GmbH","url":"https://www.wirtschaftsforum.de/danube-advisory-gmbh"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/danhe-capital"},{"title":"HORST SILBERBAUER A0VTV0","url":"https://uk.marketscreener.com/insider/HORST-SILBERBAUER-A0VTV0/"},{"title":"Danube Equity","url":"https://privateequitylist.com/public/investor/danube-equity"}]

My search didn't turn up any firm named exactly "Danube Capital Advisors." It did return several similarly named investors, which may or may not be related:

- **Dania Capital Advisors ApS (Denmark):** This is the closest name, though the spelling differs. The firm's private equity strategy targets majority stakes in small- and mid-size companies. Its typical holding period runs three to seven years.

- **Danube Fund (OriensFund I):** This is a buyout fund from 2010, based in Budapest, Hungary, that invests in the Czech Republic, Hungary, and Slovakia. PitchBook lists its status as closed and shows four past deals, including Pek-Snack, Profirent, Medicover, and GPS Tuner.

- **Danube Equity (Austria):** This investor backs medium-sized growth companies in Germany, Switzerland, Austria, the Czech Republic, Slovakia, Slovenia, and Hungary, with checks of up to EUR 50 million per transaction. Its sector focus includes new materials, cleantech, railway systems, mechatronics/automation, and automotive technologies.

- **Danube Advisory GmbH (Vienna):** This appears in a German-language interview with its managing director, Gerald Hörhan. The page links his business activities to the Danube Holding, which is headquartered in Vienna. It doesn't describe specific investments.

- **Danube Angels (Vienna):** This is a crowdinvesting platform for early- and second-stage companies in the DACH and CEE regions. Its listed financing range is EUR 50,000 to 500,000.

None of these results confirms a relationship to "Danube Capital Advisors." If you can tell me the country where it's based, or whether it's a fund or a registered investment adviser, I can run a narrower search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Danube Capital Advisors" fund startups Central Europe"

Links: [{"title":"danube angels","url":"https://wienerboerse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels/"},{"title":"danube angels","url":"https://wienerborse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels"},{"title":"Eastern Europe Gets A New Venture Fund In Fiedler Capital","url":"https://techcrunch.com/?p=1036993"},{"title":"demium capital launches a new fund to invest in central european and ukrainian startups","url":"https://inventure.com.ua/en/news/ukraine/demium-capital-launches-a-new-fund-to-invest-in-central-european-and-ukrainian-startups"},{"title":"Demium Capital Launches a New Fund to Invest in Central European and Ukrainian Startups","url":"https://inventure.com.ua/en/news/world/demium-capital-launches-a-new-fund-to-invest-in-central-european-and-ukrainian-startups"},{"title":"Demium launches a fund investing in startups in Central Europe","url":"https://merezha-tt.ukrintei.ua/?p=113142"},{"title":"Danube Tech Valley Report 2023","url":"https://dealroom.co/uploaded/2023/12/Danube-Tech-Valley-Report-2023.pdf?x75722"},{"title":"day one capital","url":"https://superscout.co/investor/day-one-capital"},{"title":"Venture Capital","url":"https://altss.com/profile/danube-equity"}]

I couldn't find any results for a firm called "Danube Capital Advisors," so I can't confirm its fund, strategy, or portfolio. The search did return several related Central European investors:

- **Danube Angels (Vienna):** This crowdinvesting platform handles early- and second-stage deals through a trusteeship model. Volume of financing: EUR 50.000 to 500.000, and issuers must be based in the DACH or CEE region.
- **Day One Capital (Budapest):** Day One Capital is a prominent venture capital firm founded in 2012 and headquartered in Budapest, Hungary. Three funds have been closed, and the latest, Fund III, launched in 2024, totaling €45 million.
- **Fiedler Capital (Vienna, with a Budapest office):** Cheques of up to €250,000 go to startups in Central and Eastern Europe and the Baltics, and the firm is looking to eventually raise a large €50 million fund. The result doesn't show a publication date, so this information may be outdated.
- **Demium Central Europe Talent Fund I:** This vehicle targets high-tech innovative Central European startups, in their seed and pre-seed stage. Its first closing included €2M on behalf of Demium. Reports differ on the target size and timing. One source gives an objective of €7-9M, while another describes a second closing of €30-40m in September.
- **Danube Equity (Linz, Austria):** This venture firm targets investments in the materials, cleantech, railway systems, mechatronics and automotive sectors.

For regional context, a 2023 Danube Tech Valley report found that there are over 14K startups in the Danube Valley, 5.6K of which are currently VC backed. It also noted that 88% of VC investment has gone i
… [skrátené, 406 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "DANUBE Capital Advisors s.r.o. Praha investice do firem",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Danube Capital Advisors Czech private equity advisory website",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Danube Capital Advisors Czech private equity advisory website"

Links: [{"title":"danube angels","url":"https://www.wienerborse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels/"},{"title":"Jan Jakoubek","url":"https://legacy.perkinscoie.com/professionals/jan-jakoubek"},{"title":"HORST SILBERBAUER A0VTV0","url":"https://uk.marketscreener.com/insider/HORST-SILBERBAUER-A0VTV0/"},{"title":"Go to team","url":"https://www.oaklins.com/ch/en/team/4265/"},{"title":"Go to team","url":"https://www.oaklins.com/se/en/team/4265/"},{"title":"jan jakoubek","url":"https://www.ashurstperkinscoie.com/en/people/jan-jakoubek/"},{"title":"Go to team","url":"https://www.oaklins.com/ie/en/team/4265/"},{"title":"Go to team","url":"https://www.oaklins.com/br/en/team/4265/"},{"title":"Go to team","url":"https://www.oaklins.com/in/en/team/4265/"},{"title":"Go to team","url":"https://www.oaklins.com/au/en/team/4265/"}]

My search didn't turn up a website for **Danube Capital Advisors**, and none of the results mention a firm by that name. The closest matches are two different firms with "Danube" in their names, and I can't confirm either is related to the company you're looking for.

- **Danube Equity AG:** One profile describes Danube Equity as an investor in mid-sized growth companies in several countries, including the Czech Republic, with deals of up to EUR 50 million. Danube Equity invests in medium-sized growth companies located in Germany, Switzerland, Austria, the Czech Republic, Slovakia, Slovenia and Hungary and invests up to EUR 50 million per transaction.
- **Danube Angels:** This Vienna-based platform arranges crowdinvesting for early- and second-stage companies in the DACH and CEE regions. Its listed reference deals include a Czech company, SmartGuide s.r.o., Czech Republic, EUR 53.000 for a stake of 3,58%, 2018.

The other results were profiles of Czech M&A lawyers and advisors at unrelated firms.

To find the right firm, you could:
- Search the Czech business register (ARES or the Justice Ministry's company register) for "Danube Capital" to check whether a Czech entity exists and get its registered website.
- Try the name with "s.r.o." or "a.s." or in Czech-language terms such as "poradenství" (advisory) or "private equity."
- If you already have a URL or a registration number, share it and I can search for that specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "DANUBE Capital Advisors s.r.o. Praha investice do firem"

Links: [{"title":"DANEX Invest s.r.o. , Praha IČO 07225008 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/07225008"},{"title":"Martin Priečko - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/martin-priecko"},{"title":"Výpis firem","url":"https://www.firmy.cz/stitek/investicni-sluzby/kraj-stredocesky/nymburk/4090-jikev"},{"title":"Výpis firem","url":"https://www.firmy.cz/stitek/akciove-trhy/kraj-stredocesky/kladno/3683-hrebec"},{"title":"Výpis firem","url":"https://www.firmy.cz/stitek/akciove-trhy/kraj-ustecky/litomerice/1938-velemin"},{"title":"Daniel Heger - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/daniel-heger"},{"title":"česky  english","url":"https://mzv.gov.cz/copenhagen/cz/novinky/x2007/akce_top_danish_investors_in_the_czech.html"},{"title":"Daniel Papoušek - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/daniel-papousek"},{"title":"Daniel Peca - osoby a firmy","url":"https://www.finmag.cz/obchodni-rejstrik/osoba/daniel-peca"}]

Links: [{"title":"rpvs.gov.sk","url":"https://rpvs.gov.sk/rpvs/Partner/Partner/DetailPdf/30460"},{"title":"Prihlásiť sa","url":"https://finstat.sk/35907169/obchodny_register"},{"title":"danube angels","url":"https://wienerborse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels"},{"title":"mkb.hu sw static file MKB Bank Plc Extraordinary announcement Change in investment 2022 02 14","url":"https://mbhbank.com/sw/static/file/mkb.hu-sw-static-file-MKB_Bank_Plc_Extraordinary_announcement_Change_in_investment_2022_02_14.pdf"},{"title":"- Company Overview for DANUBE BUSINESS CONSULTING LTD. (09507101)","url":"https://find-and-update.company-information.service.gov.uk:443/company/09507101/officers"},{"title":"Advanced company searchLink opens in new window","url":"https://find-and-update.company-information.service.gov.uk/officers/cMya7UuCdM2I5aDYGJx3VCL9H7c/appointments"},{"title":"wolf theiss advises erste group and bcr on eur 21 million financing of day tower office building in bucharest","url":"https://brcconline.eu/wolf-theiss-advises-erste-group-and-bcr-on-eur-21-million-financing-of-day-tower-office-building-in-bucharest/"},{"title":"Advanced company searchLink opens in new window","url":"https://find-and-update.company-information.service.gov.uk/officers/Y7_xfWs5QFuvmXKco1gttBvQLOo/appointments"},{"title":"Prihlásiť sa","url":"https://finstat.sk/44503822/obchodny_register"},{"title":"54802917 DANUBE AESTHETICS SRL","url":"https://termene.ro/firma/54802917-DANUBE-AESTHETICS-SRL"}]

I couldn't find a Prague-registered company called DANUBE Capital Advisors s.r.o. in these results, and nothing I found shows that any such company invests in other businesses. The first search returned unrelated Prague firms.

The closest match is a Slovak company with the same name and legal form. The Slovak public-sector partner register lists it
… [skrátené, 1223 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"Danube Capital\" investor round seed invested startup Slovakia Czech",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""Danube Capital" investor round seed invested startup Slovakia Czech"

Links: [{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/danube-cloud/financials"},{"title":"danube angels","url":"https://wienerboerse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels/"},{"title":"danube angels","url":"https://wienerborse.at/en/listing/going-public-ipo/capital-market-coach/danube-angels"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"Danube Tech Valley Report 2023","url":"https://dealroom.co/uploaded/2023/12/Danube-Tech-Valley-Report-2023.pdf?x75722"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"top vc funds in slovakia to finance your startup","url":"https://vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup"},{"title":"cb investment management","url":"https://www.vestbee.com/vc-list/cb-investment-management"},{"title":"www.eu startups","url":"https://www.eu-startups.com/?p=75585"}]

Links: [{"title":"danube fund","url":"https://disclosures.ifc.org/project-detail/SPI/7168/danube-fund"},{"title":"Danube Fund (OriensFund I) Overview","url":"https://pitchbook.com/profiles/fund/12664-18F"},{"title":"PETER ANGERMAYER A0EC9X","url":"https://zonebourse.com/insider/PETER-ANGERMAYER-A0EC9X"},{"title":"danish growth capital fund set to invest","url":"https://www.institutionalinvestor.com/article/2bsz3hs18pmifpbjdm2o0/corner-office/danish-growth-capital-fund-set-to-invest"},{"title":"Danube Equity","url":"https://privateequitylist.com/public/investor/danube-equity"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/danube-equity"},{"title":"rferl.org","url":"https://www.rferl.org/a/1093791.html"},{"title":"danish growth capital fund set to invest","url":"https://inv-prd.institutionalinvestor.com/article/2bsz3hs18pmifpbjdm2o0/corner-office/danish-growth-capital-fund-set-to-invest"},{"title":"danish growth capital fund set to invest","url":"https://stg.iinow.com/article/2bsz3hs18pmifpbjdm2o0/corner-office/danish-growth-capital-fund-set-to-invest"}]

I couldn't find any record of a firm called "Danube Capital" making a seed investment in a Slovak or Czech startup. Two searches turned up only similarly named entities, and none is a clear match.

**Closest match: Danube Cloud (Slovakia)**
CB Insights lists one seed-stage venture round for Danube Cloud, dated July 1, 2016. Neulogy Ventures is credited as the investor in that round. Neulogy is a Bratislava firm, and one industry list describes it as one of Slovakia's first early-stage VC firms backing innovative tech startups.

**Danube Angels (Vienna, crowdinvesting)**
This platform's deal range is EUR 50.000 to 500.000. Its reference deals include a 2017 investment in Slovakia's Octago, EUR 104.250 for a
… [skrátené, 1075 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Euroventures venture capital investor",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Euroventures fund startups Czech Slovakia invests seed",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Euroventures venture capital investor"

Links: [{"title":"Euroventures Investor","url":"https://mindmaps.femtech.health/firms/57309"},{"title":"Euroventures Overview","url":"https://pitchbook.com/profiles/investor/11110-42"},{"title":"euroventures zrt","url":"https://privateequitylist.com/investor/euroventures-zrt"},{"title":"Venture Capital","url":"https://altss.com/profile/euroventures"},{"title":"euroventures zrt","url":"https://privateequitylist.com/investors/euroventures-zrt"},{"title":"Venture Capital","url":"https://altss.com/profile/euroventures-management"},{"title":"zoltan toth","url":"https://jic.cz/en/content/speakers/zoltan-toth"},{"title":"euroventures capital advisory","url":"https://startups.one.gob.es/investors/euroventures_capital_advisory"},{"title":"euroventures zrt","url":"https://mail.privateequitylist.com/investors/euroventures-zrt"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/euroventures"}]

Euroventures is a Budapest-based investor that has operated since 1989. Several data sites describe it as one of the longest-established independent PE and VC firms in Central Europe.

**Focus and stage**
- The firm seeks to invest in B2B, information technology, big data, health technology, e-commerce, SaaS, agriculture technology, artificial intelligence, augmented reality, education technology & financial technology sectors based in the Eastern & Southern European regions.
- Its typical checks are smaller than many VC firms'. One profile lists Series A and Series B rounds with tickets of $1-5 m.
- Another profile describes a generalist approach, saying the firm invests across early-stage, expansion, and growth stages.

**Track record**
- One profile says the firm has advised or is advising five investment programmes totalling over €180m since 1989.
- Notable portfolio companies listed include Antavo, Daytrip, Hunch, Tresorit and Hypefy. Tresorit, the Swiss-Hungarian encrypted cloud storage company, was acquired by Swiss Post in 2021.
- Exits reportedly include IPOs (Vienna, NASDAQ, NYSE) and several dozens of trade sales to international corporations.

**Funds and investors**
- Euroventures IV is described as holding a first close in 2022 targeting Central European early-stage technology companies.
- A different profile says the firm currently manages Euroventures V a technology-focused growth investment fund investing across CEE. These two sources conflict on which fund is current.
- Investors in its funds have mainly been international institutional Investors, and in the case of Euroventures IV included EU, Hungarian and Swiss government SME programmes.

**People**
- Zoltan Toth is a partner who oversees investments in Czechia, Croatia and Hungary. He has about 25 years of VC and PE experience, per his conference bio.
- A different profile names Péter Tánczos as Managing Partner and Zoltán Török as a Partner. Other sources don't mention these names, so I'd verify them against 
… [skrátené, 683 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Euroventures fund startups Czech Slovakia invests seed"

Links: [{"title":"Join Vestbee","url":"https://vestbee.com/vc-list/euroventures"},{"title":"Venture Capital","url":"https://altss.com/profile/euroventures"},{"title":"Venture Capital","url":"https://altss.com/profile/euroventures-management"},{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"},{"title":"slovak firm 0100ventures plans to open its second e60m fund","url":"https://en.ain.ua/2022/12/22/slovak-firm-0100ventures-plans-to-open-its-second-e60m-fund"},{"title":"foundersuite.com","url":"https://foundersuite.com/firms/euroventures"},{"title":"zoltan toth","url":"https://jic.cz/en/content/speakers/zoltan-toth"},{"title":"Join Vestbee","url":"https://www.vestbee.com/insights/articles/top-vc-funds-in-czech-republic-to-finance-your-startup"},{"title":"vff sk","url":"https://superscout.co/investor/vff-sk"}]

Euroventures is a Budapest-based venture and private equity firm that has invested in Czech and Slovak startups. The sources disagree on whether it focuses on seed rounds or later stages.

**Czech and Slovak coverage**
- Vestbee lists the Czech Republic and Slovakia in the firm's investment geography, among many other Central and Eastern European countries. It gives check sizes of €1M to €5M+ and stages from pre-seed to early growth. (Investment geography: Estonia, Latvia, Lithuania, Czech Republic, Slovakia...)
- Foundersuite also names the Czech Republic and Slovakia in its geographic focus and lists seed among its stages. (Stage focus: Seed Round, Early stage VC, Later stage VC, PE Growth/Expansion)
- Partner Zoltan Toth's speaker bio says he oversees investments in Czechia, Croatia and Hungary. (Currently Zoltan is a partner at Euroventures. He oversees investments in Czechia, Croatia and Hungary.)

**Seed activity**
- Altss counts 38 investments and cites a seed deal in DATAPAO in July 2025. (Euroventures has made 38 investments, including a Seed VC investment in DATAPAO on July 22, 2025.)
- A separate Altss profile says the firm targets Seed through Series B rounds in Central European tech, with a concentration in Hungary. (The firm targets Seed through Series B rounds in Central European technology companies.)

**Later-stage signals**
- Toth's bio says the firm's current vehicle is Euroventures V, a technology-focused growth fund investing across CEE. (It currently manages Euroventures V a technology-focused growth investment fund investing across CEE.) This suggests the current strategy leans toward growth rather than seed.

**Track record**
- Vestbee says the firm has backed more than 50 startups, including Tresorit, EPAM and Kinepict. (Over the years, the VC fund has invested in over 50 startups - among them, you can find Tresorit, EPAM and Kinepict.)

**Caveats**
- The portfolio counts differ: Altss reports 38 investments, while Vestbee reports over 50.
- Several of these sources a
… [skrátené, 1033 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://euroventures.hu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures' office address, headquarters, Budapest, Budapest address (cím, székhely, iroda), contact or kontakt, the team, the firm's legal name or company ID (cégjegyzékszám, adószám), and the page's publication date. Also return any sentence about investments, funds, Czech Republic or Slovakia (Csehország, Szlovákia, Czech, Slovak) with the investment size."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
connect ECONNREFUSED 194.38.96.98:443
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.euroventures.hu",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures' office address, headquarters, Budapest, contact, the team, the firm's legal name or company ID, investments, funds, Czech Republic or Slovakia, and the page's publication date."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
connect ECONNREFUSED 194.38.96.98:443
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Euroventures Budapest press release investment round DATAPAO",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://jic.cz/en/content/speakers/zoltan-toth",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Zoltan Toth, Euroventures, the office or location, Budapest, Czechia, Croatia, Hungary, investments, funds, and the page's publication date if shown."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Sentences from the page that mention the requested terms:

1. "Zoltan Toth has 25 years of experience in venture capital/private equity."
2. "He led investments in various companies in different stages of their life cycle" (the page continues with early stage, growth, and buyouts across CEE; this is a shortened quote.)
3. "Zoltan worked for the Boston Consulting Group in Chicago and Budapest" (the sentence continues with his later roles at Advent International and 3i in London.)
4. "Currently Zoltan is a partner at Euroventures."
5. "He oversees investments in Czechia, Croatia and Hungary."
6. "Euroventures was one of the first venture capital investor in CEE and has a vast track record across the region."
7. "It currently manages Euroventures V a technology-focused growth investment fund investing across CEE."
8. "Zoltan is a graduate of the Budapest University of Economics and the Harvard Business School."

The page does not show a publication date.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Euroventures Budapest press release investment round DATAPAO"

Links: [{"title":"Norbert Bial","url":"https://hu.linkedin.com/in/norbertbial"},{"title":"Venture Capital","url":"https://altss.com/profile/euroventures"},{"title":"30503 forgo damjanovic partners csovari legal and oppenheim advise on databricks and euroventures investment in datapao","url":"https://ceelegalmatters.com/by-practice/30503-forgo-damjanovic-partners-csovari-legal-and-oppenheim-advise-on-databricks-and-euroventures-investment-in-datapao"},{"title":"Euroventures Overview","url":"https://pitchbook.com/profiles/investor/11110-42"},{"title":"30503 forgo damjanovic partners csovari legal and oppenheim advise on databricks and euroventures investment in datapao","url":"https://www.ceelm.com/hungary/30503-forgo-damjanovic-partners-csovari-legal-and-oppenheim-advise-on-databricks-and-euroventures-investment-in-datapao"},{"title":"app.mergerlinks.com","url":"https://app.mergerlinks.com/companies/euroventures"},{"title":"Hungarian fund holds €51m final close","url":"https://infrastructureinvestor.com/hungarian-fund-holds-e51m-final-close"},{"title":"300+ investors in your industry, stage, and region Get","url":"https://shizune.co/investors/b2b-vc-funds-hungary"},{"title":"19499 havel partners advises euroventures on daytrip series a investment","url":"https://ceelegalmatters.com/czech-republic/19499-havel-partners-advises-euroventures-on-daytrip-series-a-investment"}]

I didn't find the original Euroventures or DATAPAO press release in these results. The closest primary source is a LinkedIn post by Norbert Bial that announces the deal and links to a fuller write-up. The rest is secondary coverage.

**The deal**
- The post says Databricks and Euroventures both put money into Datapao, with the aim of narrowing the distance between AI ambition and execution. Databricks and Euroventures have invested in DATAPAO to help close the gap between AI ambition and execution.
- Datapao works across data architecture, platform engineering, and education. It helps companies move from experimentation to scalable, production-ready AI solutions that drive real business impact.
- The post treats the round as a major milestone for the company. It describes Databricks as a highly influential player in data and AI and Euroventures as a growth-stage investor focused on Central Europe. This strategic investment from Databricks - one of the world's most influential data and AI companies - and Euroventures - a leading growth investor in Central Europe - marks a major milestone for Datapao.

**Legal advisers (CEE Legal Matters)**
- Forgo, Damjanovic & Partners has advised Datapao on its capital raise from Databricks and Euroventures.
- On the investor side, Euroventures' counsel was Csovari Legal, while Oppenheim acted for Databricks. Csovari Legal advised Euroventures. Oppenheim advised Databricks.

**Dates and classification**
- Altss lists a seed-stage venture investment in D
… [skrátené, 757 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://ceelegalmatters.com/by-practice/30503-forgo-damjanovic-partners-csovari-legal-and-oppenheim-advise-on-databricks-and-euroventures-investment-in-datapao",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures, DATAPAO or Datapao, Databricks, the investment, the amount, the round, the office or location of Euroventures (for example Budapest, Hungary, Prague, Czech), and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://ceelegalmatters.com/czech-republic/19499-havel-partners-advises-euroventures-on-daytrip-series-a-investment",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures, Daytrip, the Series A investment, the amount, the date, the office or location of Euroventures (for example Budapest, Hungary, Prague, Czech), and the article's publication date as shown on the page."
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

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.ceelm.com/hungary/30503-forgo-damjanovic-partners-csovari-legal-and-oppenheim-advise-on-databricks-and-euroventures-investment-in-datapao",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures, DATAPAO or Datapao, Databricks, the investment, the amount, the round, the office or location of Euroventures (for example Budapest, Hungary), and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Daytrip Series A Euroventures funding round Czech startup",
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
Web search results for query: "Daytrip Series A Euroventures funding round Czech startup"

Links: [{"title":"Daytrip closes series A 6M round","url":"https://www.phocuswire.com/Daytrip-closes-series-A-6M-round"},{"title":"czech startup daytrip secures e6 1m","url":"https://trendingtopics.eu/czech-startup-daytrip-secures-e6-1m"},{"title":"19499 havel partners advises euroventures on daytrip series a investment","url":"https://ceelegalmatters.com/czech-republic/19499-havel-partners-advises-euroventures-on-daytrip-series-a-investment"},{"title":"z pandemie silnejsi startupu daytrip hrozila klinicka smrt ted pomysli na miliardovy obrat","url":"https://forbes.cz/z-pandemie-silnejsi-startupu-daytrip-hrozila-klinicka-smrt-ted-pomysli-na-miliardovy-obrat/"},{"title":"advising international investors in the czech travel start up daytrip","url":"https://www.havelpartners.cz/en/advising-international-investors-in-the-czech-travel-start-up-daytrip/"},{"title":"therecursive.com","url":"https://therecursive.com/?p=34047"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/daytrip/financials"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/czech-door-to-door-transfer-platform-daytrip-raises-10-m-to-expand-into-new-markets"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/daytrip"}]

Daytrip, a Prague-founded company, raised about €6.14 million (roughly CZK 150 million) in its Series A, led by the Budapest-based fund Euroventures.

- **Founding and business:** The company was founded in 2015 in Prague, Czech Republic, by Tomáš Turek (CEO), Markéta Bláhová (COO), Valeriia Pshenychna, Jan Prokop, and Jiří Sváček. It helps travelers find long-distance car transfers with local drivers.
- **Lead investor:** Euroventures is a Budapest-based venture capital firm investing in companies in the Central and Eastern European region. Earlier backers J&T Ventures, Nation 1 VC and Pale Fire Capital also took part in the round.
- **Legal advisers:** The HAVEL & PARTNERS team acted as legal counsel to investors in a Series A investment round, and one report says Novalia reportedly advised Daytrip.
- **Use of funds:** The money was earmarked for faster expansion and for the development of products adapted for post-pandemic travel.
- **Amount caveat:** Forbes Czech says the €6.14 million headline figure includes previously obtained convertible loans.

**Timing is inconsistent across sources.** Vestbee dates a €6 million Series A extension Daytrip closed in February 2022, and CB Insights lists a Series A dated 2/23/2022. Phocuswire, however, says Daytrip initially kicked off its Series A funding in early 2020 with a €1 million raise. The February 2022 date appears more consistent across sources, but I did not verify it against primary filings.

**What followed:** Taiwania Capital led a later round. The Czech Republic-based startup Daytrip has raised $10 million in a Series B round led by Taiwania Capital. Existing investors E
… [skrátené, 381 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://trendingtopics.eu/czech-startup-daytrip-secures-e6-1m",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures, Daytrip, the Series A round, the amount raised, the lead investor, the office or location of Euroventures (for example Budapest, Hungary), and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.havelpartners.cz/en/advising-international-investors-in-the-czech-travel-start-up-daytrip/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures, Daytrip, Series A, the amount, the date, the office or location of Euroventures (for example Budapest, Hungary), and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.havelpartners.cz/en/advising-international-investors-in-the-czech-travel-start-up-daytrip/
    Redirect URL (from the server's Location header — server-supplied, not verified): https://www.havelpartners.com/advising-international-investors-in-the-czech-travel-start-up-daytrip/
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://www.havelpartners.com/advising-international-investors-in-the-czech-travel-start-up-daytrip/"
    - prompt: "Return word-for-word, without summarising or translating, every sentence that mentions Euroventures, Daytrip, Series A, the amount, the date, the office or location of Euroventures (for example Budapest, Hungary), and the article's publication date as shown on the page (day, month, year)."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The article is dated **23 February 2022**. It reports that the Czech startup Daytrip raised **€6.14 million (CZK 150 million)** in a Series A round. The article describes the round as "secured an investment of €6.14 million (CZK 150 million) in a Series A round led by the Hungarian VC Euroventures fund."

- **Lead investor:** Euroventures, a Hungarian VC fund. The article doesn't give a specific office address for it.
- **Other investors:** Previous backers J&T Ventures, Nation 1, and Pale Fire Capital also took part.
- **Use of funds:** Faster expansion and products suited to post-pandemic travel.
- **Euroventures quote:** Zoltán Tóth, a Euroventures partner, said the team "has demonstrated the ability to build a fast-growing international company."
- **Daytrip background:** Founded in 2015, it offers door-to-door private car transfers with local drivers. It reports over 100,000 trips booked across more than 7,800 cities.
- **Goal:** Growth and sales above €40 million in the next year.

I've paraphrased the rest rather than reproducing every Daytrip sentence verbatim, since that would amount to copying most of the article.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Datapao Databricks Euroventures investment 2025 announcement",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Datapao Databricks Euroventures investment 2025 announcement"

Links: [{"title":"Datapao: Investment Raised From Databricks And Euroventures","url":"https://pulse2.com/datapao-investment-raised-from-databricks-and-euroventures"},{"title":"Datapao: Investment Raised From Databricks And Euroventures","url":"https://pulse2.com/datapao-investment-raised-from-databricks-and-euroventures/amp/"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/datapao-secures-funding-to-scale-genai"},{"title":"Bálint Vuchetich","url":"https://hu.linkedin.com/in/balint-vuchetich"},{"title":"Norbert Bial","url":"https://hu.linkedin.com/in/norbertbial"},{"title":"Tuesday 22 July, 2025","url":"https://coinspectator.com/mainstream/2025/07/22/databricks-and-euroventures-invest-in-datapao-to-close-the-gap-between-ai-ambition-and-execution/"},{"title":"30503 forgo damjanovic partners csovari legal and oppenheim advise on databricks and euroventures investment in datapao","url":"https://ceelegalmatters.com/by-practice/30503-forgo-damjanovic-partners-csovari-legal-and-oppenheim-advise-on-databricks-and-euroventures-investment-in-datapao"},{"title":"Databricks unveils new venture fund","url":"https://iteuropa.com/news/databricks-unveils-new-venture-fund"},{"title":"Databricks unveils new venture fund","url":"https://mail.iteuropa.com/tags/funding?page=5"},{"title":"databricks ventures databricks com","url":"https://venturecapitalarchive.com/venture-funds/databricks-ventures-databricks-com"}]

Datapao announced the investment in July 2025, with Databricks and Euroventures as the investors.

**Announcement and parties**
- One report dates the announcement to Tuesday 22 July, 2025, when Datapao said it had taken a strategic investment from Databricks and Euroventures.
- The company is based in Budapest and was founded in 2016 as a Budapest-based data and AI consultancy specializing in operationalizing Generative AI (GenAI) at scale.
- Descriptions of Euroventures differ. One source calls it a Hungary-based venture capital investor. A LinkedIn post by a fund-linked person calls it a leading growth investor in Central Europe.

**Planned use of funds**
- The money is meant to widen consulting in regulated industries, speed up Databricks migration work, and launch GenAI training across Europe (The funding will enable Datapao to expand its consulting in regulated industries, accelerate Databricks migration projects, and launch GenAI upskilling programs across Europe.).
- Datapao's business centers on Databricks platform builds and training for client teams, and it serves regulated sectors such as finance, energy, and manufacturing.

**Executive and partner comments**
- CEO Mate Gulyas argued that ambitious GenAI ideas with no scalable platform to support them are a recurring problem, and that without both, GenAI doesn't leave the lab.
- Kori O'Brien, Senior Vice President of Global Partners at Databricks, called Datapao a trusted partner f
… [skrátené, 783 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://pulse2.com/datapao-investment-raised-from-databricks-and-euroventures",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Datapao, DATAPAO, Euroventures, Databricks Ventures, the investment, the amount, the round or stage, the investor description of Euroventures (for example Budapest, Hungary, Central Europe), and the article's publication date as shown on the page (day, month, year)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
On July 25, 2025, Pulse 2.0 reported that Datapao, a European data and AI consultancy founded in 2016, received strategic investment from Databricks and Euroventures. The funding will support growth, expand consulting and migration programs, and launch new generative AI upskilling initiatives. Datapao serves regulated sectors such as finance, manufacturing, and energy.

- **Mate Gulyas (CEO and Founder, Datapao):** "Without both, GenAI doesn't leave the lab."
- **Kori O'Brien (SVP, Global Partners, Databricks):** The investment is expected to speed up customers' time to market.
- **Tom Howells (Partner, Euroventures):** Datapao is "the best possible European professional services company to deliver these platforms."

The article does not describe Euroventures' location, so I can't confirm a Budapest or Central Europe description from this page. I also haven't reproduced the article's sentences verbatim, since the summary above is meant to convey the facts in my own words.
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w1_b06.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w1_b06.json",
  "content": "[\n  {\n    \"candidate_id\": \"C033\",\n    \"website\": null,\n    \"identity\": [],\n    \"hq_country\": null,\n    \"investor_type\": {\n      \"value\": [\"pe\"],\n      \"value_text\": \"private equity\",\n      \"source_url\": \"https://cc.cz/opustil-korporace-a-investuje-do-it-prumyslu-i-vodiku-tomas-budnik-chce-ceskym-firmam-pomoct-ve-svete/\",\n      \"quote\": \"je orientovaný na private equity do IT a kybernetické bezpečnosti\",\n      \"published_date\": \"2021-12-21\",\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"Aitcom\", \"date\": \"2020-12\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"kupuje pardubickou společnost Aitcom\",\n        \"source_url\": \"https://www.e15.cz/byznys/technologie-a-media/thein-dal-investuje-kupuje-it-firmu-aitcom-a-podil-v-cross-network-intelligence-1376469\",\n        \"quote\": \"Fond J&T Thein podnikatele Tomáše Budníka a J&T Private Equity Group kupuje pardubickou společnost Aitcom\",\n        \"published_date\": \"2020-12-22\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Top Alulit\", \"date\": \"2024-01\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Akvizice Top Alulit\",\n        \"source_url\": \"https://cc.cz/investicni-skupina-thein-nekdejsiho-kellnerova-manazera-koupila-benesovskou-slevarnu-top-alulit/\",\n        \"quote\": \"Akvizice Top Alulit nám umožňuje zvýšit naši kapacitu a kompetence pro výrobu a zpracování.\",\n        \"published_date\": \"2024-01-16\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Síť\", \"date\": \"2020\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Thein koupil společnost Síť\",\n        \"source_url\": \"https://www.e15.cz/byznys/technologie-a-media/thein-dal-investuje-kupuje-it-firmu-aitcom-a-podil-v-cross-network-intelligence-1376469\",\n        \"quote\": \"Dříve v tomto roce Thein koupil společnost Síť, která byla s loňským obratem přes 500 milionů korun\",\n        \"published_date\": \"2020-12-22\",\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"sectors\": {\n      \"value\": [\"cybersecurity\"],\n      \"value_text\": \"kybernetické bezpečnosti\",\n      \"source_url\": \"https://cc.cz/opustil-korporace-a-investuje-do-it-prumyslu-i-vodiku-tomas-budnik-chce-ceskym-firmam-pomoct-ve-svete/\",\n      \"quote\": \"je orientovaný na private equity do IT a kybernetické bezpečnosti\",\n      \"published_date\": \"2021-12-21\",\n      \"derivation\": \"stated\"\n    },\n    \"stages\": null,\n    \"ticket\": null,\n    \"total_capital\": {\n      \"value\": {\"amount\": \"přes 600 milionů korun\", \"currency\": \"CZK\", \"capital_type\": \"aum\", \"as_of\": \"2021-12-21\"},\n      \"value_text\": \"přes 600 milionů korun\",\n      \"source_url\": \"https://cc.cz/opustil-korporace-a-investuje-do-it-prumyslu-i-vodiku-tomas-budnik-chce-ceskym-firmam-pomoct-ve-svete/\",\n      \"quote\": \"přes 600 milionů korun\",\n      \"published_date\": \"2021-12-21\",\n      \"derivation\": \"stated\"\n    },\n    \"funds\": [\n      {\n        \"value\": {\"name\": \"J&T Thein SICAV\", \"size\": null, \"currency\": null, \"vintage\": null},\n        \"value_text\": \"Fond J&T Thein SICAV\",\n        \"source_url\": \"https://www.e15.cz/byznys/technologie-a-media/thein-dal-investuje-kupuje-it-firmu-aitcom-a-podil-v-cross-network-intelligence-1376469\",\n        \"quote\": \"Fond J&T Thein SICAV se zaměřuje na investice do společností v oblasti informačních a komunikačních technologií\",\n        \"published_date\": \"2020-12-22\",\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"red_flags\": [\n      {\n        \"value\": \"Industrial sub-fund reported to have lost investmen
… [skrátené, 13621 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\w1_b06.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Wrote C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\w1_b06.json with 5 records.\n\nC033 Thein: PE. 3 investments (Aitcom 2020, Síť 2020, Top Alulit 2024-01). AUM \"přes 600 milionů korun\" (2021). Own site unreachable, so no HQ. Forbes fund-status item is headline only.\nC014 DEPO Ventures: VC, early exit null. 1 verified investment (Kardi AI 2025-04). Own site gives Prague 7 office, ticket €250K-500K. Tapaya 2026 co-lead excluded (no verbatim source).\nC145 Presto Ventures: VC. 4 investments (Vidar, Bavovna, Tur.ai via Presto Tech Horizons fund, 2024-10; GoRamp 2022-06). Fund II €30M, Tech Horizons €150M. Occam excluded (conflicting dates).\nC110 Danube Capital Advisors: no website or investment found. Early exit no_investment_found, red flag added. Registry hint unverified.\nC142 Euroventures: Hungarian, early exit foreign_hq. 1 investment (Daytrip Series A 2022-02). Own site refused connection.\n\nCaveats: quotes came from WebFetch output, which may paraphrase, so some may fail the machine check. Registry sources were not used as evidence."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

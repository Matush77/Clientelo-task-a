# Subagent: Re-verify universe anchor figures (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 19:37:47

You are a fact-checker. Use WebSearch and WebFetch (load via ToolSearch "select:WebSearch,WebFetch" if they are not loaded). Do NOT create or edit any files.

Task: for each claim below, open the PRIMARY source page (or the closest official page) and confirm or correct the figure. For each claim return:
- status: CONFIRMED / CORRECTED / NOT_FOUND
- the exact figure as stated by the source
- reference year / as-of date of the figure
- URL you actually fetched
- a VERBATIM quote (copy-paste, max 200 characters) from the fetched page that contains the figure. If you could not fetch the page and only saw a search snippet, say "SNIPPET ONLY" and quote the snippet.

Claims:
1. NVCA Yearbook: 3,417 US venture capital firms managing $1.21 trillion AUM at year-end 2023. Also check if a newer NVCA yearbook (2025 or 2026) gives a newer firm count.
2. Invest Europe: 3,095 active private equity/VC firms in Europe and EUR 1.25 trillion AUM in 2024.
3. SEC Private Fund Statistics (Form PF), latest quarter: number of advisers to venture capital funds and number of VC funds; same for private equity funds. (URL hint: sec.gov/data-research/data-visualizations/private-fund-statistics)
4. Preqin: approximately 10,300 active private equity fund managers (any official Preqin page stating number of PE firms/managers).
5. Deloitte Private "Family Office Insights": 8,030 single family offices globally in 2024, projected 10,720 by 2030.
6. UNH Center for Venture Research: number of active angel investors in the US (latest year available).
7. EBAN Statistics Compendium: number of active (networked) business angels in Europe (latest edition).
8. ESMA: number of registered EuVECA funds/managers and number of authorised AIFMs in the EU (any ESMA statistic or register count).
9. Dealroom or Crunchbase: total number of investor profiles they track (official page).

Output a markdown table: # | status | figure | as-of | URL | verbatim quote. Then list in 2-4 bullets any discrepancies with the claims above. Be strict: never fill in a number you did not see. Under 700 words.

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
  "query": "NVCA Yearbook 2025 venture capital firms assets under management 3,417 $1.21 trillion",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Invest Europe Central Europe private equity venture capital 2024 3,095 firms EUR 1.25 trillion",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "SEC private fund statistics venture capital fund advisers number of funds latest quarter",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Preqin 10,300 active private equity fund managers",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Deloitte Family Office Insights 8,030 single family offices 2024 10,720 2030",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Center for Venture Research UNH active angel investors United States annual",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EBAN Statistics Compendium active business angels Europe networked",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ESMA EuVECA registered funds number register AIFM authorised statistics",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Dealroom investor profiles tracked database",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Center for Venture Research UNH active angel investors United States annual"

Links: [{"title":"UNH Center for Venture Research: U.S. Angel Investor Market in 2014 Made a Market Correction in Deal Size","url":"https://unh.edu/unhtoday/node/7026"},{"title":"UNH Center for Venture Research: Moderate Recovery Continues in 2012 for U.S. Angel Investor Market","url":"https://www.unh.edu/unhtoday/node/6521"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/11005"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/13441"},{"title":"Press Release: Angel Market Grows 10 Percent in 2006","url":"https://www.fiercebiotech.com/biotech/press-release-angel-market-grows-10-percent-2006"},{"title":"angel investments down in 2008 but not deals","url":"https://www.newswise.com/articles/angel-investments-down-in-2008-but-not-deals"},{"title":"UNH Research Finds Growth in U.S. Angel Investor Market; Decrease in Deal Size","url":"https://www.unh.edu/unhtoday/node/6927"},{"title":"UNH Center for Venture Research: Angel Investor Market in 2015 a Buyers Market","url":"https://www.unh.edu/unhtoday/node/7197"},{"title":"UNH Finds Fewer Angels Invested More in 2019","url":"https://www.eban.org/knowledge-center/unh-finds-fewer-angels-invested-more-in-2019/"}]

The UNH Center for Venture Research publishes an annual angel market analysis that reports the number of active investors. The results I found run through 2019, and I didn't find figures for 2020 or later.

Year-by-year active investor counts:

- **2008:** The count was about 260,500, virtually unchanged from 2007's 258,200 individuals.
- **2012:** The count reached 268,160, which was a decline of 15.8 percent from 2011.
- **2014:** The count rose to 316,600, an increase of 5.9 percent from 2013.
- **2015:** The count fell to 304,930, a decrease of 3.7 percent from 2014.
- **2017:** The count dropped to 288,380, a decrease of 3.2 percent from 2016.
- **2018:** The count climbed to 334,565, an increase of 16%.
- **2019:** The count declined to 323,365, a decrease of 3.3% from 2018.

A few caveats:
- A 2014 mid-year release reported 143,140 active investors for the first two quarters alone, so it isn't comparable to the full-year figures.
- The Center has been conducting research on the angel market since 1980.

If you need the 2020 onward figures, I can run another search for the newer reports.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Preqin 10,300 active private equity fund managers"

Links: [{"title":"libguides.cbs.dk","url":"https://libguides.cbs.dk/Preqin"},{"title":"Preqin Contents","url":"https://cbs.dk/en/node/522399"},{"title":"Listing Thumbnail","url":"https://aws.amazon.com/marketplace/pp/prodview-5sdnmcxcyi4kk"},{"title":"By Erik Sonne","url":"https://libguides.cbs.dk/newsletter/5426/database-prequin-private-equity-industry-data"},{"title":"Listing Thumbnail","url":"https://aws.amazon.com/marketplace/pp/prodview-f4ogswercq3qu"},{"title":"Data Coverage June 2023","url":"https://wrds-www.wharton.upenn.edu/documents/1892/Data-Coverage-June-2023.pdf"},{"title":"Private equity database","url":"https://preqin.com/data/private-equity"},{"title":"London Insights","url":"https://maples.com/wp-content/uploads/2024/05/London-Insights.pdf"},{"title":"private equity firms raise funds at fastest pace since crisis","url":"https://www.institutionalinvestor.com/article/2bsw3slxs52qx64qd90jk/portfolio/private-equity-firms-raise-funds-at-fastest-pace-since-crisis"},{"title":"private equity firms raise funds at fastest pace since crisis","url":"https://www.institutionalinvestor.com/index%2ephp/article/2bsw3slxs52qx64qd90jk/portfolio/private-equity-firms-raise-funds-at-fastest-pace-since-crisis"}]

The 10,300 figure appears in university library guides that describe Preqin's subscription, not in Preqin's own materials. Those guides don't say when the number was current.

- A Copenhagen Business School library guide says Preqin's Fund Managers module profiles more than 10,300 active private equity fund managers across buyout, venture capital, distressed, mezzanine, natural resources and fund-of-funds strategies (Profiles and data on more than 10,300 active private equity fund managers, including buyouts, venture capital, distressed, mezzanine, natural resources and fund of funds.). The same guide notes that these managers are usually private equity firms (A fund manager is normally a private equity firm).

- An older CBS newsletter gave a lower count, describing more than 10,000 private equity and venture capital fund managers worldwide (contains profiles and information on more than 10,000 private equity and venture capital fund managers worldwide.). That suggests the 10,300 figure is a later update, though the results don't confirm this.

- Preqin's own private equity page reports a different metric: 31,653 under "Active firm coverage" (31,653 Active firm coverage). It isn't clear whether that measures the same thing as the manager count, so the two numbers can't be compared directly.

- A Preqin data listing on AWS describes several thousand Fund Managers who are currently known to be active in Private Equitys, which is vaguer and doesn't give a precise count.

Treat 10,300 as an approximate figure from third-party guides. For a current count, check Preqin directly.


REMINDER: You MUST include the sources above in your response to the user using markdow
… [skrátené, 13 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "NVCA Yearbook 2025 venture capital firms assets under management 3,417 $1.21 trillion"

Links: [{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=120789"},{"title":"largest venture capital firms us","url":"https://altss.com/rankings/largest-venture-capital-firms-us"},{"title":"2025 NVCA Yearbook","url":"https://nvca.org/wp-content/uploads/2025/03/2025-NVCA-Yearbook.pdf"},{"title":"NVCA Yearbook","url":"https://nvca.org/?p=116130"},{"title":"nvca yearbook","url":"https://nvca.org/nvca-yearbook/"},{"title":"NVCA 2026 Yearbook 4.9.26","url":"https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf"},{"title":"NVCA 2017 Yearbook","url":"https://nvca.org/wp-content/uploads/2023/07/NVCA-2017-Yearbook.pdf"},{"title":"largest venture capital firms","url":"https://altss.com/rankings/largest-venture-capital-firms"}]

The 3,417 firms and $1.21 trillion figures come from the **2024** NVCA Yearbook, not the 2025 edition. NVCA's Yearbook page says the 2024 NVCA Yearbook, the 27th edition of the publication, highlights several industry milestones reached in 2023, and it counts 3,417 VC firms as of the end of 2023. That same edition reports a record $311.6 billion in dry powder and a total of $1.21 trillion under management for those firms.

The 2025 Yearbook, released March 27, 2025 with data provided by PitchBook, reports 2024 activity instead. Its key findings include 14,320 deals worth $215.4 billion closed by U.S. VC firms in 2024, and $76.8 billion raised across 538 funds. It also puts the overall U.S. median fund size at $21.3 million.

The search results did not show the 3,417 or $1.21 trillion figures inside the 2025 edition, so I couldn't confirm them there. The 2025 PDF snippet I retrieved contained only its credits page.

For more recent data, a third-party site (Altss) cites the NVCA 2026 Yearbook for about $320 billion across roughly 15,352 deals in 2025, up 51% year over year. I couldn't verify that figure against NVCA's own 2026 document, so treat it as secondhand.

In short, cite the 2024 Yearbook for 3,417 firms and $1.21 trillion, and cite the 2025 Yearbook for its 2024 deal and fundraising numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Invest Europe Central Europe private equity venture capital 2024 3,095 firms EUR 1.25 trillion"

Links: [{"title":"Invest Europe CEE Statistics 2024","url":"https://cvca.hr/wp-content/uploads/2025/12/Invest-Europe_CEE-Statistics_2024.pdf"},{"title":"therecursive.com","url":"https://therecursive.com/?p=41231"},{"title":"Invest Europe: European private capital hits €1.25T in 2024, growing 2.6x over the decade","url":"https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/"},{"title":"Investing in Europe: Private Equity activity 2024","url":"https://www.seca.ch/en/knowledge-library/newsletters/2025/seca-enewsletter-no-550/private-equity-int-news/investing-in-europe-private-equity-activity-2024/"},{"title":"Press Release","url":"https://www.ifc.org/en/pressroom/2024/ifc-investment-to-boost-growth-of-lower-mid-market-firms-in-central-and-eastern-europe"},{"title":"european private equity funds aum 2024","url":"https://hedgefundalpha.com/news/european-private-equity-funds-aum-2024/"},{"title":"pressroom.ifc.org","url":"https://pressroom.ifc.org/all/pages/PressDetail.aspx?ID=28303"},{"title":"art42622761 fundusze nie boja sie inwestowac w regionie wzrost az o 50 proc","url":"https://www.parkiet.com/firmy/art42622761-fundusze-nie-boja-sie-inwestowac-w-regionie-wzrost-az-o-50-proc"},{"title":"CEE: rekordowy wzrost inwestycji i pozyskiwanego kapitału. Polska liderem regionu","url":"https://xyz.pl/?p=88735"}]

The 3,095-firm and €1.25 trillion figures are from Invest Europe's pan-European report, not a Central or Eastern Europe (CEE) dataset.

**Pan-European totals (2024)**
- European private equity and venture capital assets under management grew 7 per cent to €1.25 trillion, distributed across 3,095 active firms.
- That is 2.6 times the level of 2015, marking over a decade of continuous growth.
- Portfolio assets at cost totalled €834 billion, with buyout funds accounting for €507 billion, passing €500 billion for the first time.
- Dry powder reached a record €414 billion in 2024.

**Central and Eastern Europe (2024)**
The regional study is a separate Invest Europe report, produced with Gide Loyrette Nouel, that covers CEE rather than only Central Europe.
- CEE accounted for 2.2% of total European investment value, up from 1.9% in 2023, as regional investment grew roughly two times faster than the European total.
- Private equity and venture capital investment equated to 0.112% of GDP in the region in 2024, roughly a fifth of the European average of 0.551%.
- A Polish-language article on the report says PE/VC investment in CEE reached €2.83 billion in 2024, a 50 per cent increase on the previous year. Buyout value rose 79% to €1.96 billion (the value of buyouts grew 79 per cent to 1.96 billion euros).
- Poland was the largest market in the region by investment value and number of companies funded, with funds investing €1.23 billion in 81 companies, 44% of the region
… [skrátené, 492 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EBAN Statistics Compendium active business angels Europe networked"

Links: [{"title":"Statistics Compendium 2021 European Early Stage Market Statistics","url":"https://www.eban.org/2022/10/10/"},{"title":"Statistics Compendium 2021 European Early Stage Market Statistics","url":"https://eban.org/?p=35526"},{"title":"EBAN Statistics Compendium 2023","url":"https://www.eban.org/wp-content/uploads/2024/10/EBAN-Statistics-Compendium-2023.pdf"},{"title":"Statistics Compendium 2020 European Early Stage Market Statistics","url":"https://eban.org/?p=33767"},{"title":"eban.org","url":"https://eban.org/?p=31952"},{"title":"Stats Compendium 2024","url":"https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf"},{"title":"Statistics Compendium 2019 European Early Stage Market Statistics","url":"https://eban.org/statistics-compendium-2019-european-early-stage-market-statistics"},{"title":"www.eban.org","url":"https://www.eban.org/?p=38221"},{"title":"www.eban.org","url":"https://www.eban.org/?p=40706"},{"title":"Download the EBAN Statistics Compendium","url":"https://eltia.eu/index.php/events-extranet/eban-publishes-its-annual-statistics-compendium-reporting-on-the-activity-of-business-angels-and-business-angel-networks-in-europe-2"}]

EBAN's 2021 edition gives the clearest "networked" figure. Based on reports from national federations, local angel networks, and national venture capital associations, EBAN estimated about 39,400 active business angel investors in Europe who belong to a local investment network or association.

The same edition reported on market size. Visible angel investment rose from €767 million in 2020 to a record €1,456 million in 2021, a 90% increase, across 38 European countries. Angels took part in over 5,070 observed funding rounds in 2021, including both initial and follow-on investments in European startups.

The compendium's method has changed over time. The 2024 edition combines direct surveys with publicly available reports from business angel networks, national federations and other early-stage investors active in Europe. It also draws on about 35 other sources, including Dealroom, Crunchbase and PitchBook, and it covers activities that took place in 2024, with information collected in 2024–2025.

Two caveats apply. EBAN says its figures are not representative of the entire European market, so they show trends rather than a complete census. I also could not retrieve the active-investor headcount from the 2023 or 2024 editions in these results, so the 39,400 figure is from 2021. Before citing a current number, check the latest report: the 2024 Statistics Compendium PDF is at eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ESMA EuVECA registered funds number register AIFM authorised statistics"

Links: [{"title":"In focus   European Venture Capital Fund Regulations","url":"https://www.algoodbody.com/files/uploads/news_insights_pub/In_focus_-_European_Venture_Capital_Fund_Regulations.pdf"},{"title":"A stable, well-functioning financial market for all","url":"https://www.fi.se/en/our-registers/company-register/details?id=676515"},{"title":"ganado.com","url":"https://ganado.com/?p=8712"},{"title":"European Commission legislative proposal for Regulation amending EuVECA Regulation and EuSEF Regulation","url":"https://cms.law/en/int/legal-updates/european-commission-legislative-proposal-for-regulation-amending-euveca-regulation-and-eusef-regulation"},{"title":"Infocus EuropeanVentureCapitalFundRegulations1","url":"https://www.algoodbody.com/media/Infocus-EuropeanVentureCapitalFundRegulations1.pdf"},{"title":"Databases and Registers","url":"https://www.esma.europa.eu/databases-and-registers"},{"title":"Company register","url":"https://www.fi.se/en/our-registers/company-register/gransoverskridandehandel?id=170117"},{"title":"ESMA Registers - Publication Interface Help File","url":"https://registers.esma.europa.eu/publication/helpPage"},{"title":"Company register","url":"https://www.fi.se/en/our-registers/company-register/gransoverskridandehandel?id=638141"}]

My search didn't find current aggregate figures for the number of EuVECA funds or registered AIFMs in the EU, so I can't give you a reliable up-to-date total.

- **Dated count:** A 2016 law firm note reported that the total number of EuVECAs registered in Europe was 20 at that point. That figure is far out of date.
- **Official database:** ESMA's databases page describes a database listing all managers of qualifying venture capital funds with the qualifying venture capital funds that they market. ESMA's Registers system also has a filter for EuVECA entities, and its keyword search returns the list of the registers with an indication of how many results have been identified at each of them. Running a search there and exporting the results is probably the most direct way to get a current count.
- **Registered vs. authorised AIFMs:** Counts split by type depend on the distinction. Registered AIFMs are sub-threshold managers that must register with the Central Bank rather than being fully AIFMD-authorised. They can use the EuVECA passport but not the wider AIFMD passport.
- **National registers:** Some national registers track EuVECA activity at the manager level. Sweden's FI register, for example, lists Notification of use of the designation EuVECA entries for individual managers, by country.
- **Pending reform:** A Commission legislative proposal would have AIFMs register the EuVECA and EuSEF funds and would streamline registration, including a two-month deadline for the home regulator to decide. I didn't confirm whether this has been adopted or when the source was published, so check the 
… [skrátené, 274 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "SEC private fund statistics venture capital fund advisers number of funds latest quarter"

Links: [{"title":"private funds statistics 2024 q2","url":"https://www.sec.gov/file/private-funds-statistics-2024-q2"},{"title":"2023q2 private funds stats20240109 508","url":"https://www.sec.gov/files/2023q2-private-funds-stats20240109-508.pdf"},{"title":"2022 q2 private funds stats 20230103","url":"https://www.sec.gov/files/2022-q2-private-funds-stats-20230103.pdf"},{"title":"private funds number funds advisers","url":"https://sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-number-funds-advisers"},{"title":"Private Fund Statistics","url":"https://sec.gov/data-research/statistics-data-visualizations/private-fund-statistics"},{"title":"cranedata.com","url":"https://cranedata.com/archives/all-articles/7691/"},{"title":"cranedata.com","url":"https://cranedata.com/archives/all-articles/7450/"},{"title":"k8.cranedata.com","url":"https://k8.cranedata.com/archives/all-articles/7691"},{"title":"SEC Private Fund Statistics Report: Continued Growth in Private Funds and Private Fund Assets","url":"https://ion-analytics-acuris-law-report-group-hflr.production.services.acuris.com/6424201/sec-private-fund-statistics-report-continued-growth-in-private-funds-and-private-fund-assets.thtml"}]

The search didn't return venture-capital-specific fund or adviser counts for the latest quarter, so I can't give you that number from these results.

**Latest SEC data:** The SEC's Private Fund Statistics page is the most recent source I found. Its summary panel covers 2025Q4 and reports a 9.2% year-over-year change for private funds reported on Form PF, plus 18.5% growth in gross assets and 16.3% growth in net assets (PF Statistics at a Glance Private Funds Reported on Form PF in 2025Q4). The excerpt doesn't show the absolute fund count, so I can't confirm the total from it.

**Why VC funds are hard to isolate:** Form PF applies only to SEC-registered advisers with at least $150 million in private fund assets under management. Smaller advisers and exempt reporting advisers instead report general information about the private funds they manage on Form ADV. Many venture capital fund managers are exempt reporting advisers (this is from my background knowledge, not the search results), so their data would mostly appear in the Form ADV-based statistics.

**Where to look next:**
- The SEC's aggregate statistics for private funds reported on Form ADV are under Investment Advisers - Total Private Funds Advised by RIAs or ERAs.
- The landing page's Fund and Adviser Counts Statistics section covers fund and adviser counts, and that page was Last Reviewed or Updated: Jan. 27, 2026.
- I couldn't confirm from these excerpts whether either source breaks out venture capital funds separately, so check those tables directly.

**Caveats:** Form PF information provided in this report is aggregated, rounded, and/or masked, and future adjustm
… [skrátené, 336 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Dealroom investor profiles tracked database"

Links: [{"title":"The Essentials","url":"https://angelspartners.com/reviews/dealroom/"},{"title":"Dealroom API","url":"https://dealroom.co/products/api"},{"title":"Understanding Dealroom: features, pricing, and alternatives","url":"https://www.ellty.com/blog/what-is-dealroom"},{"title":"Profiles & guides","url":"https://dealroom.co/profiles/"},{"title":"Solutions Ecosystems Reports Resources Data Pricing Login Book a demo","url":"https://dealroom.co/blog/our-graph-database-ground-up-redesign-of-traditional-advisory-model/"},{"title":"content.dealroom.co","url":"https://content.dealroom.co/pricing"},{"title":"Knowledge Base","url":"https://dealroom.co/knowledge"},{"title":"magnet.me","url":"https://magnet.me/en/company/dealroom.co"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/dealroomco"}]

Dealroom is an Amsterdam-based startup and investor data platform, and its investor profiles are one of its main data types. The sources give different investor counts:

- Dealroom's API page lists more than 100,000 investors and funds. 100K+ Investors & funds
- Its pricing page advertises 250K tracked investors, filterable by performance, strategy, or focus. 250k Investors Tracked
- A review from a rival outreach tool cites 225K investors mapped, with data it says is accurate as of July 2026. Data accurate as of July 2026. ModelMarket intelligence platform built for the investor side, with a free research tier for founders Database size3.2M+ companies tracked, with 225K investors mapped

The gap may come from different dates or definitions (investors, funds, LPs). That explanation is my inference, not something the sources state.

**What an investor profile includes**
- Portfolio analysis, founder origins, a sector landscape, a world map, and a comparison view that suggests similar investors. Portfolio analysis, founder origins, sector landscape and world map for each fund, plus a comparison view that suggests similar investors.
- Portfolios, round-by-round participation, co-investors, and stage and sector focus. Portfolios, round-by-round participation, co-investors, stage and sector focus across the global funding landscape.
- Public profile pages that are free to read and draw on the same data as the paid product. Companies, investors, people, locations, sectors and universities each have a public profile, built from the same data as the platform and free to read.

Coverage also extends to LPs, pension funds, and family offices, with more than 10,000 listed, plus a Power Law ranking of investors backing fast-growing companies. 10k+ LP, Pension Funds, Family Offices See which investors back the fastest growing companies.

**Who it's for and its limits**
- It is built for buy-side users such as VCs, corporate venture teams, and investment banks, not for founders pitching investors. It's primarily used by VCs, corporate venture teams, and investment banks to rese
… [skrátené, 1237 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Deloitte Family Office Insights 8,030 single family offices 2024 10,720 2030"

Links: [{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/in/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/global/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/az/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/et/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"defining the family office landscape","url":"https://www.deloitte.com/mt/en/services/deloitte-private/about/defining-the-family-office-landscape.html"},{"title":"defining the family office landscape","url":"https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html"},{"title":"family office assets set for 7","url":"https://en.paperjam.lu/article/family-office-assets-set-for-7"},{"title":"2024 defining the family office landscape executive report","url":"https://www.deloitte.com/content/dam/assets-shared/docs/services/deloitte-private/2024/2024-defining-the-family-office-landscape-executive-report.pdf"},{"title":"deloitte number of family offices to grow 75 by 2030","url":"https://www.dakota.com/fundraising-news/deloitte-number-of-family-offices-to-grow-75-by-2030"},{"title":"41950 family office growth apac world deloitte 2024","url":"https://finews.asia/finance/41950-family-office-growth-apac-world-deloitte-2024"}]

Your figures match Deloitte Private's 2024 report, *Defining the Family Office Landscape*, part of its Family Office Insights Series (Global Edition). Trade coverage places the report's release on 4 September 2024.

**Count and projection**
- Deloitte's estimate of 8,030 single family offices today is about 31% above the 6,130 counted in 2019.
- The forecast is 10,720 by 2030, a third above today's level, with 9,030 expected in 2025.
- The "75%" figure is measured from the 2019 base over roughly a decade. Dakota's coverage describes it as a 75% increase from 2019. Measured from today's 8,030, the growth to 10,720 is about 33%.

**Assets and wealth**
- Family offices' estimated assets under management are expected to rise 73%, from US$3.1 trillion today to US$5.4 trillion by 2030.
- Est
… [skrátené, 1169 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/nvca-yearbook/",
  "prompt": "Find every mention of the number of venture capital firms (e.g., 3,417) and the assets under management figure (e.g., $1.21 trillion) and state the year/as-of date each refers to. Also state which NVCA Yearbook edition this page describes. Quote the exact sentence containing each figure."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf",
  "prompt": "Does this document state a number of US venture capital firms and/or assets under management? Quote the exact sentence(s) with the firm count and AUM figure, and the year they refer to. Also state the title/edition and data year covered."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/wp-content/uploads/2025/03/2025-NVCA-Yearbook.pdf",
  "prompt": "Does this document state a number of US venture capital firms and/or total assets under management (e.g., 3,417 firms, $1.21 trillion)? Quote the exact sentence(s) with any firm count or AUM figure and the year each refers to."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cvca.hr/wp-content/uploads/2025/12/Invest-Europe_CEE-Statistics_2024.pdf",
  "prompt": "Does this report state a count of active firms (e.g., 3,095) or a European total AUM (e.g., EUR 1.25 trillion) for 2024? Quote the exact sentence(s) with those figures, and state the reference year. Note whether it is Europe-wide or CEE-only."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/",
  "prompt": "Find the exact sentence(s) mentioning the number of active firms (e.g., 3,095) and the total assets under management (e.g., EUR 1.25 trillion) and state the year. Quote them verbatim."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sec.gov/data-research/data-visualizations/private-fund-statistics",
  "prompt": "Find the most recent quarter covered and any figures for number of investment advisers to venture capital funds, number of venture capital funds, number of private equity fund advisers and number of private equity funds. Quote the exact figures and the quarter label. If the venture capital or private equity counts are not on this page, say so explicitly and list the linked sub-pages you see."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.preqin.com/data/private-equity",
  "prompt": "Find any statement of the number of active private equity fund managers, firms, or investors (e.g., 10,300, 31,653). Quote the exact text and state what the number measures and the as-of date if given."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html",
  "prompt": "Find the number of single family offices globally (e.g., 8,030 in 2024) and the projection for 2030 (e.g., 10,720). Quote the exact sentences containing these figures and the report year/as-of date."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The most recent quarter on this page is **2025Q4**. The page reports **58,891** private funds, described as "Private Funds Reported on Form PF in 2025Q4."

**Venture capital and private equity counts are not on this page.** It doesn't give the number of venture capital fund advisers, venture capital funds, private equity fund advisers, or private equity funds.

The linked sub-pages are:
- Number of Funds and Advisers
- Aggregate Fund Assets
- Beneficial Ownership of Funds
- Qualifying Hedge Fund Strategies
- Qualifying Hedge Fund Investment Types
- Liquidity Funds

The Number of Funds and Advisers sub-page is the most likely place to find venture capital and private equity counts, but I haven't seen its contents.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page has one statement of an active firm count, and it doesn't define the term or give a date:

- **"31,653" / "Active firm coverage"**

It's a coverage figure for firms that Preqin labels as active. The page doesn't say whether "firms" means fund managers specifically. No as-of date is given. The only date is the footer's "Copyright 2026 by Preqin."

The page also lists **"16,638" / "Investor coverage"**. It's not labeled as active, so it doesn't answer your question directly.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't find either figure in the content provided. It appears to be the raw binary of a PDF (object definitions, embedded images, and compressed streams), and it is truncated before any readable report text. So I can't confirm whether the report states a 2024 count of active firms (such as 3,095) or a European total AUM (such as EUR 1.25 trillion), and I can't say whether either figure would be Europe-wide or CEE-only.

If you paste the report's extracted text, or the relevant pages, I can check for those figures and quote the exact sentences with their reference year.

[Binary content (application/pdf, 2.9MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791488320789-qcl1va.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The figures are for **2024**. The article reports that "in 2024, European private equity and venture capital assets under management grew 7 per cent to €1.25 trillion," and that these assets were "distributed across 3,095 active firms."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The content you provided doesn't include any statement of a number of US venture capital firms or assets under management, so I can't quote a sentence with a firm count, AUM figure, or data year.

The only readable text is PDF metadata. It gives the title as "NVCA Logo white," and it was created in Adobe Illustrator in February 2022. The rest is compressed binary data and image data, and the content is truncated. This looks like a logo file from the National Venture Capital Association rather than a report with industry statistics, so the title/edition and data year for any such figures can't be determined from this material.

[Binary content (application/pdf, 6.8MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791488320531-ywwlkk.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Single family offices worldwide:** An estimated 8,030 in 2024. The report says:

> "There are an estimated 8,030 single family offices in the world today, up from 6,130 in 2019, a near third (31%) increase."

**2030 projection:** 10,720. The report says:

> "...and by a third (33%) to 10,720 family offices by 2030."

**Source:** *Defining the Family Office Landscape, 2024* (Deloitte Private, Family Office Insights Series, Global Edition). The page does not give a more specific as-of date than the 2024 report year, and "today" refers to the time of publication.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The content provided does not state a number of US venture capital firms or any total assets under management. I found no sentence with a firm count or AUM figure, so there is nothing to quote or date.

The readable text is limited to PDF metadata. It identifies the file as a one-page logo, titled "NVCA Logo white," created in Adobe Illustrator. The rest is compressed binary data and embedded image data, and the excerpt is truncated, so I can't rule out figures in unreadable portions. If you have a different document or a text version of this one, I can check it.

[Binary content (application/pdf, 7.4MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791488321066-imxlzw.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Firm count (3,417):** Mentioned once. As of **end of 2023**:

> "By the end of 2023, the U.S. VC ecosystem had 3,417 VC firms, which closed a cumulative 13,608 VC deals worth $170.6 billion."

**Assets under management ($1.21 trillion):** Mentioned once. As of **end of 2023**. The full sentence exceeds the 125-character limit, so this is the relevant excerpt:

> "...and a total of $1.21 trillion under management."

**Edition:** The page describes the **2024 NVCA Yearbook**, the **27th edition**, which covers milestones reached in 2023.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/",
  "prompt": "Quote any sentence giving the number of US VC firms or total assets under management (AUM), and state the data year each refers to. Also state the edition/title and release date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "NVCA 2026 Yearbook press release venture capital firms 2025 data",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investeurope.eu/research/key-statistics/",
  "prompt": "Find the number of active firms and the total AUM for European private equity and venture capital for the latest year (2024 or later). Quote the exact sentence(s) with the figures and the year they refer to. If not found on this page, list the main headings."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-number-funds-advisers",
  "prompt": "Find counts of investment advisers to venture capital funds, number of venture capital funds, private equity fund advisers, and private equity funds. Quote the exact figures, the quarter label, and whether these come from Form PF or Form ADV data."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf",
  "prompt": "Find the number of active business angels in Europe (networked/active investors, e.g., 39,400 or other), and quote the exact sentence(s) with the figure and the data year."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://dealroom.co/pricing",
  "prompt": "Find any count of investors, investor profiles, or funds tracked (e.g., 250K). Quote the exact text with the number and any as-of date."
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
The page doesn't include a count of investors, investor profiles, or funds tracked, and it has no as-of date for any such figure. The closest reference is in the free trial FAQ, which mentions access to "every company profile and funding round," but it gives no number.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Number of US VC firms:** No sentence in the page gives this figure. It mentions 538 funds raised in 2024, but not the number of firms.

**Total AUM:** The page states: "The VC industry's total assets under management (AUM) now sits at **$1.25 trillion**." The page does not give a specific data year for this figure. "Now" suggests it reflects the time of release, and the yearbook's data focuses on 2024.

**Source:** *National Venture Capital Association's (NVCA) 2025 Yearbook*, released March 27, 2025, with data provided by PitchBook. The press release is titled "NVCA Releases 2025 Yearbook Showcasing 2024 VC Trends."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page you provided doesn't include the figures you asked for. It has no venture capital or private equity adviser or fund counts, and no quarter-specific numbers. It does say: "In this visualization, advisers are counted for three quarters following each quarter they report a private fund."

The page also doesn't state whether its data comes from Form PF or Form ADV. The figures appear to be in a linked data file, "Fund and Adviser Counts Statistics" (Number_of_Funds_and_Advisers_08-05-2026a.json), which wasn't provided. The page was last reviewed or updated Aug. 19, 2026.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't find the figure in the content you provided. The document is a PDF whose page text is stored in compressed binary streams, and the content is also cut off partway through. I can see metadata indicating it's the "Stats Compendium 2024," authored by EBAN, but no readable sentence with an active business angel count or a data year.

The "39,400" in your request is only an example, so I haven't used it as a figure from the document.

To get the answer, you could:
- Paste the extracted text of the relevant pages (e.g., the market overview or investor statistics sections).
- Provide a plain-text or HTML version of the report.
- Share the specific page or section that discusses business angel numbers.

Once I have readable text, I'll return the figure with the exact sentence and data year.

[Binary content (application/pdf, 6MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791488334929-dhb2g6.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "NVCA 2026 Yearbook press release venture capital firms 2025 data"

Links: [{"title":"NVCA 2026 Yearbook | The Venture Industry in Transition","url":"https://nvca.org/?p=124853"},{"title":"NVCA 2026 Yearbook 4.9.26","url":"https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2026-yearbook-charts-a-venture-industry-in-transition/"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=124844"},{"title":"largest venture capital firms us","url":"https://altss.com/rankings/largest-venture-capital-firms-us"},{"title":"Press Release","url":"https://aijourn.com/?p=518832"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=120789"},{"title":"• About Us","url":"https://nvca.org/events/category/import/2026-10/page/2/"}]

The NVCA released its 2026 Yearbook on April 13, 2026, with data from PitchBook. U.S. VC firms closed 15,352 deals worth $320 billion in 2025, a 51 percent increase in deal value and the second-highest total on record.

**Key findings from the press release**
- Artificial intelligence accounted for 65.4 percent of all deal value.
- Non-traditional investors such as hedge funds, sovereign wealth funds, corporate strategics, and endowments participated in roughly 30 percent of deals and accounted for 83 percent of all investment value.
- Liquidity is shifting: secondary transactions returned nearly as much capital as exits in 2025. NVCA flags that regulators and lawmakers may need to consider how liquidity rules, tax incentives, and capital-markets infrastructure affect private company exits.

**Additional figures from NVCA's interactive yearbook page**
- Fundraising was weak: VC fundraising was $67B, lowest in 9 years. For comparison, the 2025 Yearbook reported that in 2024, U.S. firms raised $76.8 billion across 538 funds.
- Exits recovered partially: exit value was $217B, 2x 2024, still 27% of 2021 peak.
- Deal count was nearly flat. Deal count was basically flat — up less than 1%. The growth in dollars came from larger rounds, with the top five companies (OpenAI, CoreWeave, xAI, Anthropic, and Databricks) raising nearly $60 billion collectively.
- By stage, later VC took $126.9B across 4,167 deals, early VC $70.1B across 5,166 deals, and pre-seed/seed $22.3B across 5,049 deals.

The yearbook frames the year as two layered markets: the headline total is driven largely by AI mega-rounds, while the broader market looks much different. For the full dataset, the yearbook is available on NVCA's site, and NVCA members may access the members-only supplemental XLS data pack by contacting research@nvca.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/?p=124853",
  "prompt": "Find the number of US venture capital firms (firm count) and total AUM figure for the 2026 Yearbook (data year 2025). Quote the exact sentence(s) with any firm count and AUM, and state the data year. Also quote any statement of total VC AUM."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/press_releases/nvca-releases-2026-yearbook-charts-a-venture-industry-in-transition/",
  "prompt": "Find any number of VC firms or total AUM (assets under management) for US venture capital. Quote the exact sentence(s) with the figure and the data year, and the release date."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Invest Europe key statistics 2024 private equity venture capital number of active firms assets under management Europe report",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "SEC Form PF private funds statistics 2025 Q4 venture capital fund advisers number of venture capital funds private equity funds",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EBAN Statistics Compendium 2024 business angels active investors Europe number",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "UNH Center for Venture Research angel investors active investors 2023 2024 United States report",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ESMA EuVECA funds number registered managers statistics report 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Preqin number of private equity fund managers profiled active firms 10,300",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://dealroom.co/",
  "prompt": "Find any count of investors, investor profiles, funds, or LPs tracked (e.g., 100K+, 250K, 225K). Quote the exact text containing each number and any as-of date."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't report the total number of US VC firms or total US VC AUM. The closest figure is 2025 fundraising, which measures capital raised rather than assets under management:

> "Traditional VC fundraising totaled $67 billion across 585 funds" (2025 data)

Release date: April 13, 2026.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't state a count of investors, investor profiles, funds, or LPs tracked.

Closest matches:
- **"Join thousands of investors, corporates, and governments using Dealroom to identify promising companies."** This describes users, not tracked investors, and gives no exact figure or as-of date.
- **"100+ ecosystem partners across the world"** These are partner organizations such as Tech Nation and Invest Atlanta, not tracked investors. No as-of date is given.

The "Top investors by match score" list and "Selected LPs" section show only a few named firms with no total.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Firm count:** 2,984 US VC firms in 2025, per the stat block labeled "Total VC firms in existence." The page adds that this is a "First-ever decline, down from 3,054."

**Total VC AUM:** The page does not state a total AUM figure. "Fundraising AUM" appears only as a chart filter label, with no value. The "$67B" figure is VC fundraising, not AUM.

**Data year:** 2025, as of 12/31/2025.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Invest Europe key statistics 2024 private equity venture capital number of active firms assets under management Europe report"

Links: [{"title":"Invest Europe CEE Statistics 2024","url":"https://cvca.hr/wp-content/uploads/2025/12/Invest-Europe_CEE-Statistics_2024.pdf"},{"title":"Invest Europe: European private capital hits €1.25T in 2024, growing 2.6x over the decade","url":"https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/"},{"title":"Investing in Europe: Private Equity activity 2024","url":"https://www.seca.ch/en/knowledge-library/newsletters/2025/seca-enewsletter-no-550/private-equity-int-news/investing-in-europe-private-equity-activity-2024/"},{"title":"european private equity funds aum 2024","url":"https://hedgefundalpha.com/news/european-private-equity-funds-aum-2024/"},{"title":"venture capital and private equity update hungary 2024","url":"https://www.ey.com/en_hu/insights/strategy-transactions/venture-capital-and-private-equity-update-hungary-2024"},{"title":"ey hvca report 2024","url":"https://www.ey.com/content/dam/ey-unified-site/ey-com/hu-hu/services/strategy-transactions/documents/ey-hvca-report-2024.pdf"},{"title":"Private equity: Record capital levels drive European expansion","url":"https://www.dbag.com/newsroom/detail/private-equity-record-capital-levels-drive-european-expansion/"},{"title":"Key insights","url":"https://www.statista.com/topics/6318/premium-products-market/"},{"title":"Key insights","url":"https://www.statista.com/topics/6318/connected-car-services/"}]

Invest Europe's 2024 figures show European private equity and venture capital at record size. I couldn't open the report itself, so these numbers come from press coverage of it.

**Assets under management and firm count**
- Invest Europe's tally puts European PE and VC assets under management at about €1.25 trillion in 2024, up 7%, distributed across 3,095 active firms.
- This marks over a decade of continuous growth, with industry's assets 2.6 times higher than a decade ago in 2015.
- Within the total, portfolio assets at cost reached €834 billion, with buyout funds accounting for €507 billion, surpassing the €500 billion mark for the first time. VC funds' portfolio assets were €111 billion, the first time they passed €100 billion.

**Dry powder (uninvested capital)**
- Dry powder hit a record €414 billion, equivalent to 81 per cent of the €511 billion invested over the previous four years.
- Buyout dry powder fell slightly to €278 billion, while venture capital fund commitments rose to 59 billion euros.

**Fundraising**
- For the first half of 2024, private equity and venture capital funds raised €59 billion, a 15% year-on-year increase, but down by 28% compared to the amount raised in the second half of 2023. This figure comes from a secondary news site, not Invest Europe directly.

**Data coverage and a discrepancy**
- The activity survey collects comprehensive an
… [skrátené, 761 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Preqin number of private equity fund managers profiled active firms 10,300"

Links: [{"title":"Preqin Contents","url":"https://cbs.dk/en/node/522399"},{"title":"libguides.cbs.dk","url":"https://libguides.cbs.dk/Preqin"},{"title":"Listing Thumbnail","url":"https://aws.amazon.com/marketplace/pp/prodview-5sdnmcxcyi4kk"},{"title":"Data Coverage June 2023","url":"https://wrds-www.wharton.upenn.edu/documents/1892/Data-Coverage-June-2023.pdf"},{"title":"Listing Thumbnail","url":"https://aws.amazon.com/marketplace/pp/prodview-f4ogswercq3qu"},{"title":"By Erik Sonne","url":"https://libguides.cbs.dk/newsletter/5426/database-prequin-private-equity-industry-data"},{"title":"Private equity database","url":"https://preqin.com/data/private-equity"},{"title":"preqin private equity update kpmg pe forum","url":"https://assets.kpmg.com/content/dam/kpmg/qm/pdf/preqin-private-equity-update-kpmg-pe-forum.pdf"},{"title":"Preqin Alternative Asset Fund Performance","url":"https://www.marketplace.spglobal.com/en/datasets/preqin-alternative-asset-fund-performance-(98)"},{"title":"Private equity database","url":"https://cdn-website-ssr-core.iridium.pro.preqin.com/data/private-equity"}]

The 10,300 figure appears in Copenhagen Business School (CBS) library guides, but the other sources I found give different numbers, and none of them is dated.

- **The 10,300 figure:** A CBS library page puts the Fund Managers module at more than 10,300 active private equity managers, spanning buyouts, venture, distressed, mezzanine, natural resources, and fund of funds. The same page's wording implies that a fund manager is normally a private equity firm, so the count is effectively a firm count.
- **Preqin's own figure:** Preqin's private equity database page lists 31,653 active firm coverage. That is roughly three times the library figure, and the snippet doesn't say whether the two measure the same thing or the same date.
- **Other figures:** An older CBS newsletter put the private equity and venture capital fund manager count at more than 10,000 private equity and venture capital fund managers worldwide. An S&P Global Marketplace listing cites 62,000+ fund managers, but that dataset covers alternative assets broadly, not private equity alone.

The 10,300 number is credible as a figure from a Preqin subscription snapshot, but I couldn't confirm its date or whether it is current. For a current count, check Preqin directly or ask its sales team for the private equity fund manager total.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EBAN Statistics Compendium 2024 business angels active investors Europe number"

Links: [{"title":"EBAN Annual Statistics Compendium for 2024","url":"https://www.eban.org/2025/10/29"},{"title":"From Vision to Action:","url":"https://www.eban.org/news/eban-annual-statistics-compendium-for-2024-2/"},{"title":"Stats Compendium 2024","url":"https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf"},{"title":"eban.org","url":"https://eban.org/?p=31952"},{"title":"EBAN Annual Statistics Compendium for 2024","url":"https://www.eban.org/news"},{"title":"EBAN Statistics Compendium 2023","url":"https://www.eban.org/wp-content/uploads/2024/10/EBAN-Statistics-Compendium-2023.pdf"},{"title":"www.eban.org","url":"https://www.eban.org/?p=40706"},{"title":"Download the EBAN Statistics Compendium","url":"https://eltia.eu/index.php/events-extranet/eban-publishes-its-annual-statistics-compendium-reporting-on-the-activity-of-business-angels-and-business-angel-networks-in-europe-2"},{"title":"www.eban.org","url":"https://www.eban.org/?p=38221"}]

Links: [{"title":"Stats Compendium 2024","url":"https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf"},{"title":"EBAN Annual Statistics Compendium for 2024","url":"https://www.eban.org/2025/10/29"},{"title":"From Vision to Action:","url":"https://www.eban.org/news/eban-annual-statistics-compendium-for-2024-2/"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://www.eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels"},{"title":"average business angel network investments in europe","url":"https://es.statista.com/statistics/889681/average-business-angel-network-investments-in-europe/"},{"title":"business angel investments in europe by visible and non visible market","url":"https://fr.statista.com/statistics/889583/business-angel-investments-in-europe-by-visible-and-non-visible-market/"},{"title":"docs.google.com","url":"https://docs.google.com/presentation/d/1ddKCuhUmAB4vCuwGfWICslIs14vRMecy/htmlpresent"},{"title":"business angel investments in europe","url":"https://es.statista.com/statistics/889595/business-angel-investments-in-europe/"},{"title":"business angels numbers by country europe","url":"https://www-statista-com.ezproxy.canberra.edu.au/statistics/439305/business-angels-numbers-by-country-europe"}]

I couldn't find the 2024 Compendium's headline count of active business angels in Europe. The sources I found describe the report's scope and method but don't give that total, so you'll need to open the PDF itself.

**About the 2024 Compendium**
- EBAN calls it its annual research on business angels and business angel networks, and it draws on figures from networks, federations, and platforms like Dealroom, Crunchbase, and PitchBook. It is based on information from European business angel networks and Federations of BANs, plus data from 35 othe
… [skrátené, 1193 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "UNH Center for Venture Research angel investors active investors 2023 2024 United States report"

Links: [{"title":"- July 3, 2024","url":"https://eban.org/?p=40179"},{"title":"axis intelligence","url":"https://axis-intelligence.com/?p=40436"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://www.eban.org/industry-reports/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels/"},{"title":"Site icon EBAN","url":"https://www.eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels/amp"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels"},{"title":"scholars.unh.edu","url":"https://scholars.unh.edu/cvr/"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/13005"},{"title":"UNH Finds Fewer Angels Invested More in 2019","url":"https://www.unh.edu/unhtoday/node/16143"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/11005"}]

Links: [{"title":"paulcollege.unh.edu","url":"https://paulcollege.unh.edu/sites/default/files/media/2025-12/FY%202024%20Analysis%20Report%20Final.pdf"},{"title":"2023 full year analysis report final","url":"https://paulcollege.unh.edu/sites/default/files/media/2024-07/2023-full-year-analysis-report-final.pdf"},{"title":"- July 3, 2024","url":"https://eban.org/?p=40179"},{"title":"axis intelligence","url":"https://axis-intelligence.com/?p=40436"},{"title":"eban.org","url":"https://eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels/amp"},{"title":"fy 2022 analysis report final","url":"https://paulcollege.unh.edu/sites/default/files/resource/files/fy_2022_analysis_report_final.pdf"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://www.eban.org/industry-reports/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels/"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels"},{"title":"The Angel Market in 2021: Metrics Indicate Strong Market – By Center for Venture Research","url":"https://www.eban.org/knowledge-center/the-angel-market-in-2021-metrics-indicate-strong-market-by-center-for-venture-research/"},{"title":"Angel Investing Statistics (2026)","url":"https://walnutinvest.com/stats/angel-investing-statistics"}]

The UNH Center for Venture Research (CVR) found that the angel market in 2023 and 2024 had more active investors but less total money invested.

**2024 report** (titled "A Stable Market Before the AI Frenzy")
- Angel dollars fell to $17.9 billion, down 3.1% 
… [skrátené, 2963 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ESMA EuVECA funds number registered managers statistics report 2025"

Links: [{"title":"Reference Case Number: FOI9336","url":"https://fca.org.uk/freedom-information/information-aif-managers-july-2022"},{"title":"ESMA11 239717167 20877 ESMA statistics on securities and markets","url":"https://www.esma.europa.eu/sites/default/files/2025-12/ESMA11-239717167-20877_ESMA_statistics_on_securities_and_markets.pdf"},{"title":"Databases and Registers","url":"https://www.esma.europa.eu/databases-and-registers"},{"title":"Databases and Registers","url":"https://www.esma.europa.eu/access-regulated-information"},{"title":"europa.eu REFIT Scoreboard","url":"https://op.europa.eu/webpub/com/refit-scoreboard/en/policy/8/8-6.html"},{"title":"ESMA consults on measures for Venture Capital and Social Entrepreneurship Funds","url":"https://www.ifsc.ie/news/esma-consults-on-measures-for-venture-capital-and-social-entrepreneurship-funds"},{"title":"revised euveca regulation approved","url":"https://www.mondaq.com/germany/finance/639272/revised-euveca-regulation-approved"},{"title":"eumonitor.eu","url":"https://eumonitor.eu/9353000/1/j4nvhdfcs8bljza_j9vvik7m1c3gyxp/vk5rfykdg0zq"},{"title":"Infocus EuropeanVentureCapitalFundRegulations1","url":"https://www.algoodbody.com/media/Infocus-EuropeanVentureCapitalFundRegulations1.pdf"},{"title":"revised euveca regulation approved","url":"https://webiis08.mondaq.com/germany/finance/639272/revised-euveca-regulation-approved"}]

Links: [{"title":"AGEFI Luxembourg - juin 2025","url":"https://www.agefi.lu/publications/FreeMonthlySample/31"},{"title":"Reference Case Number: FOI9336","url":"https://fca.org.uk/freedom-information/information-aif-managers-july-2022"},{"title":"European venture capital funds and European social entrepreneurship funds","url":"https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1484046"},{"title":"26 février 2026","url":"https://www.ibr-ire.be/fr/reglementation-et-publications/doctrine/notes-techniques/note-technique-detail-page/avis-2026-02"},{"title":"20467 how do we obtain the european venture capital funds euveca designation","url":"https://decilehub.com/base/11-general-legal/20467-how-do-we-obtain-the-european-venture-capital-funds-euveca-designation"},{"title":"revised euveca regulation approved","url":"https://www.mondaq.com/germany/finance/639272/revised-euveca-regulation-approved"},{"title":"26 février 2026","url":"https://www.ibr-ire.be/fr/actualites/news-detail/avis-2026-02"},{"title":"eu proposal to boost take up of euveca and eusef funds","url":"https://www.williamfry.com/knowledge/eu-proposal-to-boost-take-up-of-euveca-and-eusef-funds/"},{"title":"revised euveca regulation approved","url":"https://webiis08.mondaq.com/germany/finance/639272/revised-euveca-regulation-approved"}]

I couldn't find a 2025 ESMA figure for the number of registered EuVECA managers or funds, so these results don't give a current count.

- **ESMA's December 2025 statistics publicat
… [skrátené, 1589 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "SEC Form PF private funds statistics 2025 Q4 venture capital fund advisers number of venture capital funds private equity funds"

Links: [{"title":"dera wp pf perf fee alloc 2501","url":"https://www.sec.gov/files/dera_wp_pf-perf-fee-alloc-2501.pdf"},{"title":"Private Fund Statistics","url":"https://sec.gov/data-research/statistics-data-visualizations/private-fund-statistics"},{"title":"Private Fund Statistics","url":"https://www.sec.gov/data-research/data-visualizations/private-fund-statistics"},{"title":"cranedata.com","url":"https://cranedata.com/archives/all-articles/11143/"},{"title":"cranedata.com","url":"https://cranedata.com/archives/all-articles/11188/"},{"title":"cranedata.com","url":"https://cranedata.com/archives/all-articles/11346/"},{"title":"2025 pf report congress","url":"https://www.sec.gov/files/2025-pf-report-congress.pdf"},{"title":"Overview of SEC reporting and compliance for private investment advisers","url":"https://www.ontra.ai/blog/overview-sec-reporting-private-fund-managers/"},{"title":"private funds qualifying hedge fund investment types","url":"https://www.sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-qualifying-hedge-fund-investment-types"}]

Links: [{"title":"Private Fund Statistics","url":"https://sec.gov/data-research/statistics-data-visualizations/private-fund-statistics"},{"title":"private funds number funds advisers","url":"https://sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-number-funds-advisers"},{"title":"Private Fund Statistics","url":"https://www.sec.gov/data-research/data-visualizations/private-fund-statistics"},{"title":"private funds statistics 2024 q2","url":"https://www.sec.gov/file/private-funds-statistics-2024-q2"},{"title":"Quarterly Asset Management Statistics 2025 Q4 2","url":"https://www.bvi.de/fileadmin/user_upload/letter/2026/Quarterly_Asset_Management_Statistics_2025_Q4_2_.pdf"},{"title":"2023q2 private funds stats20240109 508","url":"https://www.sec.gov/files/2023q2-private-funds-stats20240109-508.pdf"},{"title":"2022 q2 private funds stats 20230103","url":"https://www.sec.gov/files/2022-q2-private-funds-stats-20230103.pdf"},{"title":"SEC: Private funds’ assets exceed banks’","url":"https://www.privatefundscfo.com/sec-private-funds-assets-exceed-banks/"},{"title":"RCW August 25 2025","url":"https://media.regcompliancewatch.com/uploads/2025/08/RCW_August_25_2025.pdf"}]

I couldn't find the 2025Q4 venture capital or private equity fund counts in the search results. The SEC's 2025Q4 data exists, but the table values didn't come through.

**What the SEC's 2025Q4 page shows**
The SEC's Private Fund Statistics page covers private funds reported on Form PF in 2025Q4. Its summary cards show year-over-year changes of 9.2%, 18.5%, and 16.3% for 2024Q4 to 2025Q4. The extracted text doesn't clearly tie each percentage to a metric, and the dollar figures are missing. The page was last reviewed or updated 
… [skrátené, 1300 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://paulcollege.unh.edu/sites/default/files/media/2025-12/FY%202024%20Analysis%20Report%20Final.pdf",
  "prompt": "Find the number of active investors for 2024 and 2023 (and the % change). Quote the exact sentence(s) containing these figures and state the report year/title and the date printed on the report."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://libguides.cbs.dk/Preqin",
  "prompt": "Find the text about the number of private equity fund managers (e.g., 10,300 active private equity fund managers). Quote the exact sentence and any date given."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eban.org/news/eban-annual-statistics-compendium-for-2024-2/",
  "prompt": "Find any number of active business angels / angel investors in Europe (networked or active investors) and the number of countries covered. Quote the exact sentence(s) with the figure and the data year."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://dealroom.co/products/api",
  "prompt": "Find any count of investors, investor profiles, or funds (e.g., 100K+ investors & funds). Quote the exact text with the number and any date."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://op.europa.eu/webpub/com/refit-scoreboard/en/policy/8/8-6.html",
  "prompt": "Find the number of EuVECA funds registered and the as-of date. Quote the exact sentence containing the number."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.esma.europa.eu/databases-and-registers",
  "prompt": "Find the EuVECA register description and any count of registered EuVECA managers or funds, and any count of AIFMs. Quote exact text with the number and date if present."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ESMA number of authorised AIFMs EU AIFMD statistics report total number of AIFMs registered",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Invest Europe Capital Under Management Dry Powder 2024 report invest-europe.eu",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Crunchbase investors tracked number of investor profiles database",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page reports **462 EuVECA funds** registered, as of **December 2022**. The source states: "As of December 2022, 462 EuVECA funds and 15 EuSEFs funds were registered, despite being in place for more than 8 years."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page lists **100K+** investors and funds. It appears in the stat block as "100K+ / Investors & funds" and in the investors card as "100K+ funds."

No date is attached to this count. The page gives "since 2018" only for funding rounds ("336K+ rounds"), and "2025" only for new startups ("76K New startups detected in 2025").
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't give a figure for the number of active business angels in Europe. It does state the country coverage:

- **Countries covered: 38.** "This report covers 38 countries on the European continent" (data year 2024, per the title "EBAN Annual Statistics Compendium for 2024").

The page also notes that these figures are "not representative of the entire European market." The full Compendium PDF, linked from the page, may contain the angel count, but I can't access it from this content.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page describes the EuVECA register as: "Database listing all managers of qualifying venture capital funds with the qualifying venture capital funds that they market."

The page gives no count of registered EuVECA managers or funds, and no count of AIFMs. It also gives no dates tied to these registers. The AIFM entry, "Register of authorised Alternative Investment Fund Managers (AIFMs)," is a description only, without figures.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page says: "It contains profiles and data on more than 34,100 active private equity fund managers" (under the "Fund Managers" entry).

The page gives no date for this figure. The only date on the page is the "Last Updated: Oct 7, 2026 3:56 PM" footer, which refers to the web page, not the fund manager count. The figure is 34,100, not the 10,300 in your example.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't find the active investor figures for 2024 or 2023 in the content you provided, so I can't report the numbers or the % change.

The text is raw, compressed PDF data (FlateDecode streams, embedded font files, and an image), not readable prose. The content is also truncated, so the pages that might contain the figures may be missing.

I also can't confirm the report's title or printed date. The only readable clue is two hyperlink annotations pointing to `paulcollege.unh.edu/center-venture-research`, which suggests the document comes from the University of New Hampshire's Center for Venture Research. That isn't enough to identify the specific report or its date.

To get an answer, you could:
- Paste the extracted text from the PDF (for example, from a PDF-to-text tool or the report's HTML version).
- Share the page containing the active investor data, or the full report if it's available as text.
- Send the report's cover page, which should show the title and the printed date.

[Binary content (application/pdf, 113.5KB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791488406535-gkc0y6.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Crunchbase investors tracked number of investor profiles database"

Links: [{"title":"research.unipd.it","url":"https://research.unipd.it/handle/11577/3341496"},{"title":"crunchbase reaches 50k investment rounds and 450k profiles","url":"https://about.crunchbase.com/blog/crunchbase-reaches-50k-investment-rounds-and-450k-profiles/"},{"title":"Crunchbase — 100K+ Instant Company DB, Funding Monitor ($8/1k)","url":"https://apify.com/memo23/crunchbase-scraper?fpr=p2hrc6"},{"title":"investor database","url":"https://www.angelbacked.co/investor-database"},{"title":"crunchbase hits 400k profiles and 45k funding rounds august excel download now available","url":"https://techcrunch.com/2013/09/10/crunchbase-hits-400k-profiles-and-45k-funding-rounds-august-excel-download-now-available"},{"title":"Product Reports Resources Pricing Login Book a demo","url":"https://dealroom.co/companies/crunchbase/"},{"title":"gracker.ai","url":"https://gracker.ai/b2b-saas-growth-tools/tool/crunchbase"},{"title":"A verified list of 1000 targeted VCs & Investors for FREE (LinkedIn, Twitter & Emails) 📧","url":"https://ihproduction.onrender.com/post/targeted-list-of-1000-angels-vcs-investors-for-free-linkedin-profiles-emails-twitters-67c3e0b924"},{"title":"www.openwebninja.com","url":"https://www.openwebninja.com/request-apis/crunchbase"}]

Links: [{"title":"startup databases investors","url":"https://qubit.capital/blog/startup-databases-investors"},{"title":"pipelineroad.com","url":"https://pipelineroad.com/news/tag/crunchbase"},{"title":"crunchbase alternatives","url":"https://www.papermark.com/blog/crunchbase-alternatives.md"},{"title":"← All Stories","url":"https://pipelineroad.com/news/20260819-sequoia-khosla-lead-investors-in-250-new-2026-unicorns"},{"title":"The world's most trusted database of companies, investors, and funding information","url":"https://aiindigo.com/tool/crunchbase"},{"title":"← All Stories","url":"https://pipelineroad.com/news/20260819-sequoia-khosla-and-y-combinator-lead-2026-unicorn-investors"},{"title":"pipelineroad.com","url":"https://pipelineroad.com/news/tag/unicorn"},{"title":"crunchbase starter","url":"https://www.stork.ai/en/crunchbase-starter"},{"title":"← All Stories","url":"https://pipelineroad.com/news/20260819-sequoia-khosla-y-combinator-lead-2026-unicorn-investors"},{"title":"← All Stories","url":"https://pipelineroad.com/news/20260819-sequoia-capital-tops-2026-unicorn-investor-list"}]

The most specific investor count I found is from 2019, and none of the results give a current figure from Crunchbase itself.

- **Best available figure (2019):** A University of Padua repository record describing the Crunchbase dataset counted about 121,500 investors as of May 2019. As of May 2019, Crunchbase had collected records on 760,590 organizations (of which 708,558 companies), 121,509 investors of different types, 263,426 funding rounds, 890,429 people, 17,068 initial public offerings (IPO) and 89,959 acquisitions. T
… [skrátené, 1312 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Invest Europe Capital Under Management Dry Powder 2024 report invest-europe.eu"

Links: [{"title":"Invest Europe: European private capital hits €1.25T in 2024, growing 2.6x over the decade","url":"https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/"},{"title":"hedgefundalpha.com","url":"https://hedgefundalpha.com/?p=2181098"},{"title":"european private equity funds aum 2024","url":"https://hedgefundalpha.com/news/european-private-equity-funds-aum-2024/"},{"title":"Private equity: Record capital levels drive European expansion","url":"https://www.dbag.com/newsroom/detail/private-equity-record-capital-levels-drive-european-expansion/"},{"title":"www.businesswire.com","url":"https://www.businesswire.com/news/home/20241112934229/en"},{"title":"European infrastructure is evolving—and investors are, too","url":"https://karriere.mckinsey.de/industries/infrastructure/our-insights/european-infrastructure-is-evolving-and-investors-are-too"},{"title":"bizwire 2024 11 12 arthur d little private equity h1 2024 fundraising investment and exit activity remain challenging but industry sentiment shows green shoots of recovery","url":"https://markets.financialcontent.com/observernewsonline/article/bizwire-2024-11-12-arthur-d-little-private-equity-h1-2024-fundraising-investment-and-exit-activity-remain-challenging-but-industry-sentiment-shows-green-shoots-of-recovery"},{"title":"Tue, Nov 11, 2025","url":"https://www.opalesque.com/683822/Europe_Dry_powder_for_direct_lending_far_outstrips382.html"},{"title":"2025 Silent Capital Report now available. Where family offices and LPs are actually deploying. [Download for free →]","url":"https://venturecapitalarchive.com/archives/the-state-of-european-venture-capital-in-2024"}]

The search didn't return the invest-europe.eu page itself, so these figures come from secondary coverage of the report. Check the Invest Europe site for the original.

**Report:** Invest Europe's study is titled Positioned for the Challenge: Capital Under Management & Dry Powder 2024. Coverage of it is dated July 2025.

**Key figures for 2024:**
- Industry assets grew 7% to about €1.25 trillion, spread across 3,095 active firms (According to the report, in 2024, European private equity and venture capital assets under management grew 7 per cent to €1.25 trillion, distributed across 3,095 active firms.).
- Those assets are now about 2.6 times their 2015 level (This marks over a decade of continuous growth, with industry's assets 2.6 times higher than a decade ago in 2015.).
- Buyout funds held €507 billion in portfolio assets at cost, the first time that figure topped €500 billion (The total includes €834 billion in portfolio assets at cost (PAC), with buyout funds accounting for €507 billion, surpassing the €500 billion mark for the first time.).
- VC funds' portfolio assets reached €111 billion, passing €100 billion for the first time (At €111 billion, VC
… [skrátené, 1234 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ESMA number of authorised AIFMs EU AIFMD statistics report total number of AIFMs registered"

Links: [{"title":"esma50 164 2969 cre data publication dec2018","url":"https://www.esma.europa.eu/sites/default/files/library/esma50-164-2969_cre_data_publication_dec2018.pdf"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2026/06/investment-fund-managers/"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2026/09/investment-fund-managers/"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2025/12/investment-fund-managers"},{"title":"Quarterly statistics","url":"https://cssf.lu/en/2022/12/investment-fund-managers"},{"title":"Relazione ESMA 16 maggio 2024 n. ESMA50 164 3688","url":"https://dirittobancario.it/wp-content/uploads/2024/05/Relazione-ESMA-16-maggio-2024-n.-ESMA50-164-3688.pdf"},{"title":"ESMA11 239717167 20758 cre data dec2024","url":"https://www.esma.europa.eu/sites/default/files/2025-06/ESMA11-239717167-20758_cre_data_dec2024.pdf"},{"title":"Statistiques trimestrielles","url":"https://www.cssf.lu/fr/2026/09/les-gestionnaires-de-fonds-dinvestissement/"},{"title":"Statistiques trimestrielles","url":"https://www.cssf.lu/fr/2026/06/les-gestionnaires-de-fonds-dinvestissement/"},{"title":"risksystem.com","url":"https://risksystem.com/?p=6296"}]

Links: [{"title":"ESMA CRE data publication dec 2020","url":"https://www.dirittobancario.it/wp-content/uploads/2022/02/ESMA-CRE-data-publication-dec-2020.pdf"},{"title":"ESMA50 1605533872 8484 Alternative Investment Funds exposures to commercial real estate 2022","url":"https://www.esma.europa.eu/sites/default/files/2024-04/ESMA50-1605533872-8484_Alternative_Investment_Funds_exposures_to_commercial_real_estate_2022.pdf"},{"title":"esma50 164 2969 cre data publication dec2018","url":"https://www.esma.europa.eu/sites/default/files/library/esma50-164-2969_cre_data_publication_dec2018.pdf"},{"title":"esma50 164 4105 cre data publication dec2019","url":"https://www.esma.europa.eu/sites/default/files/library/esma50-164-4105_cre_data_publication_dec2019.pdf"},{"title":"ESMA11 239717167 20758 cre data dec2024","url":"https://www.esma.europa.eu/sites/default/files/2025-06/ESMA11-239717167-20758_cre_data_dec2024.pdf"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2026/09/investment-fund-managers/"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2025/12/investment-fund-managers"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2026/06/investment-fund-managers/"},{"title":"Quarterly statistics","url":"https://cssf.lu/en/2022/12/investment-fund-managers"}]

I couldn't find a current, EU-wide total of authorised AIFMs in these results. The figures I found are related but don't answer the question directly.

- **Commercial real estate AIFs (funds, not managers):** ESMA's most recent note in these results, covering end-2024, counts 1,931 commercial real estate AIFs marketed or managed by authorised EU AIFMs
… [skrátené, 1381 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "UNH Center for Venture Research \"A Stable Market Before the AI Frenzy\" angel investment 2024 active investors 445,535",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eban.org/2022/10/10/",
  "prompt": "Find the number of active business angels / angel investors in Europe that EBAN reports (e.g., 39,400) and the data year. Quote the exact sentence containing it and state whether it refers to networked/member angels."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sec.gov/files/Number_of_Funds_and_Advisers_08-05-2026a.json",
  "prompt": "List the quarters covered and the venture capital fund and adviser counts and private equity fund and adviser counts for the most recent quarter (2025Q4). Quote the exact values."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "ESMA annual statistical report EU alternative investment funds number of AIFMs authorised 2025 total",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cbs.dk/en/node/522399",
  "prompt": "Find the text describing the number of private equity fund managers covered by Preqin (e.g., 10,300 or 34,100). Quote the exact sentence and any date."
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
- **Number:** approximately 39,400 (written as "39400" in the source) active business angel investors in Europe.
- **Data year:** 2021. The page presents this as the Statistics Compendium 2021 covering European early-stage market activity.
- **Source sentence:** The full sentence exceeds the 125-character quote limit, so here is the portion containing the figure: "there are approximately 39400 active business angel investors on the European continent."
- **Networked/member angels:** Yes. EBAN counts these angels as those already part of a local investment network or association. The count is based on reports from national federations, local angel networks, and national venture capital associations.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "UNH Center for Venture Research "A Stable Market Before the AI Frenzy" angel investment 2024 active investors 445,535"

Links: [{"title":"paulcollege.unh.edu","url":"https://paulcollege.unh.edu/sites/default/files/media/2025-12/FY%202024%20Analysis%20Report%20Final.pdf"},{"title":"UNH Launches First Undergraduate Student Managed Angel Fund on East Coast","url":"https://unh.edu/unhtoday/node/7022"},{"title":"Angel Investing","url":"https://www.unh.edu/unhtoday/taxonomy/term/2471"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/13005"},{"title":"UNH Center for Venture Research: U.S. Angel Investor Market in 2014 Made a Market Correction in Deal Size","url":"https://unh.edu/unhtoday/node/7026"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/13441"},{"title":"unh finds more angels investing more smaller deals","url":"https://www.unh.edu/unhtoday/news/release/2019/05/16/unh-finds-more-angels-investing-more-smaller-deals"},{"title":"Angel investors hold onto wallets for established businesses","url":"https://paulcollege.unh.edu/node/1011"},{"title":"Angels in the classroom at UNH","url":"https://www.nhbr.com/angels-in-the-classroom-at-unh/"},{"title":"angelinvestorsnetwork.com","url":"https://angelinvestorsnetwork.com/listing/activities"}]

Links: [{"title":"paulcollege.unh.edu","url":"https://paulcollege.unh.edu/sites/default/files/media/2025-12/FY%202024%20Analysis%20Report%20Final.pdf"},{"title":"AI Market Saturation","url":"https://vcminute.substack.com/p/ai-market-saturation"},{"title":"the state of ai investing","url":"https://angellist.com/blog/the-state-of-ai-investing"},{"title":"ACA Publishes 2026 Angel Funders Report","url":"https://angelcapitalassociation.org/blog/aca-publishes-2026-angel-funders-report/"},{"title":"hyper.ai","url":"https://hyper.ai/en/stories/236d65eafd8f613376268e1853af652b"},{"title":"why ai startup valuations are overheated 2026","url":"https://angelinvestorsnetwork.com/startups/why-ai-startup-valuations-are-overheated-2026"},{"title":"AI ‘Angel of Death’ an Overreaction to Potential Disruption","url":"https://schwabnetwork.com/video/ai-angel-of-death-an-overreaction-to-potential-disruption"},{"title":"Slavo Tuleya","url":"https://sk.linkedin.com/in/slavotuleya"},{"title":"Angel Investors AI Startup Evaluation Framework: Key Metrics for Success","url":"https://www.allied.vc/guides/angel-investor-ai-startup-evaluation-framework"}]

The report exists. The University of New Hampshire's Center for Venture Research published "The Angel Market in 2024: A Stable Market Before the AI Frenzy," and its suggested citation credits Jeffrey Sohl and dates it December 2024.

Your figure checks out. The report puts 2024 active angel investors at 445,535, up from 422,350 in 2023, a 5.5% rise (445,535 versus 422,350, an increase of 5.5%).

Other headline numbers from the same summary:
- Total angel dollars fell 3.1% to $17.9 billion (a decrease of 3.1% over 2023).
- The num
… [skrátené, 1112 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "ESMA annual statistical report EU alternative investment funds number of AIFMs authorised 2025 total"

Links: [{"title":"ESMA11 239717167 20758 cre data dec2024","url":"https://www.esma.europa.eu/sites/default/files/2025-06/ESMA11-239717167-20758_cre_data_dec2024.pdf"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2026/06/investment-fund-managers/"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2025/12/investment-fund-managers"},{"title":"Further legal and regulatory developments","url":"https://akd.foleon.com/alternative-investment-funds/quarterly-update-2025-q2/further-legal-and-regulatory-developments"},{"title":"EU Alternative Investment Funds - 2021 Statistical Report","url":"https://regradar.com/members/preview/details/eu-alternative-investment-funds-2021-statistical-report/"},{"title":"esma50 165 1006 asr aif 2020","url":"https://www.esma.europa.eu/sites/default/files/library/esma50-165-1006_asr-aif_2020.pdf"},{"title":"ESMA report values EU Alternative Investment Funds at €4.9 trillion","url":"https://pwcplus.de/en/article/217063/esma-report-values-eu-alternative-investment-funds-at-eur49-trillion/"},{"title":"ESMA report highlights liquidity concerns for Alternative Investment Funds","url":"https://www.esma.europa.eu/press-news/esma-news/esma-report-highlights-liquidity-concerns-alternative-investment-funds-0"},{"title":"esma50 165 1734 asr aif 2021","url":"https://www.esma.europa.eu/sites/default/files/library/esma50-165-1734_asr_aif_2021.pdf"}]

Links: [{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2026/06/investment-fund-managers/"},{"title":"Quarterly statistics","url":"https://www.cssf.lu/en/2025/12/investment-fund-managers"},{"title":"ESMA11 239717167 20758 cre data dec2024","url":"https://www.esma.europa.eu/sites/default/files/2025-06/ESMA11-239717167-20758_cre_data_dec2024.pdf"},{"title":"Quarterly statistics","url":"https://cssf.lu/en/2022/12/investment-fund-managers"},{"title":"ESMA50 1605533872 8484 Alternative Investment Funds exposures to commercial real estate 2022","url":"https://www.esma.europa.eu/sites/default/files/2024-04/ESMA50-1605533872-8484_Alternative_Investment_Funds_exposures_to_commercial_real_estate_2022.pdf"},{"title":"ESMA11 239717167 20877 ESMA statistics on securities and markets","url":"https://www.esma.europa.eu/sites/default/files/2025-12/ESMA11-239717167-20877_ESMA_statistics_on_securities_and_markets.pdf"},{"title":"esma50 164 2969 cre data publication dec2018","url":"https://www.esma.europa.eu/sites/default/files/library/esma50-164-2969_cre_data_publication_dec2018.pdf"},{"title":"AIFM Reporting dashboard 2025","url":"https://www.cssf.lu/wp-content/uploads/AIFM_Reporting_dashboard_2025.pdf"},{"title":"Leveraged AIFs – ESMA publishes its 2025 Risk Assessment","url":"https://www.simmons-simmons.com/en/publications/cmowq81az00yuv7rwio22s46l/leveraged-aifs-esma-publishes-its-2025-risk-assessment"}]

Links: [{"title":"AIFM Repo
… [skrátené, 2895 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Fact-check results. Quotes are as returned by WebFetch's page extraction. Several PDFs were unreadable through fetch, so those rows are marked SNIPPET ONLY.\n\n| # | status | figure | as-of | URL | verbatim quote |\n|---|---|---|---|---|---|\n| 1 | CONFIRMED | 3,417 US VC firms; $1.21T AUM | End-2023 (2024 Yearbook, 27th ed.) | https://nvca.org/nvca-yearbook/ | \"By the end of 2023, the U.S. VC ecosystem had 3,417 VC firms, which closed a cumulative 13,608 VC deals worth $170.6 billion.\" |\n| 2 | CONFIRMED (secondary) | 3,095 active firms; EUR 1.25T AUM | 2024 | https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/ | \"in 2024, European private equity and venture capital assets under management grew 7 per cent to €1.25 trillion\" |\n| 3 | NOT_FOUND | No VC/PE counts on landing page. Total private funds (all types): 58,891 | 2025Q4 | https://www.sec.gov/data-research/data-visualizations/private-fund-statistics | \"Private Funds Reported on Form PF in 2025Q4\" |\n| 4 | NOT_FOUND | Official Preqin: 31,653 \"Active firm coverage\" (no date). 10,300 not on any official page | Undated | https://www.preqin.com/data/private-equity | \"31,653\" / \"Active firm coverage\" |\n| 5 | CONFIRMED | 8,030 single family offices (2024); 10,720 by 2030 | 2024 report | https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html | \"There are an estimated 8,030 single family offices in the world today, up from 6,130 in 2019, a near third (31%) increase.\" |\n| 6 | CONFIRMED (SNIPPET ONLY) | 445,535 active US angel investors (2023: 422,350) | 2024 (cited Dec 2024; hosted in Dec 2025 folder) | https://paulcollege.unh.edu/sites/default/files/media/2025-12/FY%202024%20Analysis%20Report%20Final.pdf | \"The number of active investors in 2024 increased to 445,535 as compared to 422,350 in 2023, an increase of 5.5%.\" |\n| 7 | CONFIRMED (2021 ed.); NOT_FOUND (2024 ed.) | ~39,400 active angel investors in European networks | 2021 edition | https://www.eban.org/2022/10/10/ | \"there are approximately 39400 active business angel investors on the European continent.\" |\n| 8 | NOT_FOUND (current) | 462 EuVECA funds registered (no current manager or authorised-AIFM count) | Dec 2022 | https://op.europa.eu/webpub/com/refit-scoreboard/en/policy/8/8-6.html | \"As of December 2022, 462 EuVECA funds and 15 EuSEFs funds were registered, despite being in place for more than 8 years.\" |\n| 9 | CONFIRMED (partial) | Dealroom: \"100K+\" investors and funds, combined. Crunchbase: no official count found | Undated | https://dealroom.co/products/api | \"100K+ / Investors & funds\" |\n\nDiscrepancies:\n- Claim 1: The 3,417 and $1.21T figures are correct but are YE2023 data. The NVCA 2026 Yearbook (https://nvca.org/?p=124853) reports 2,984 US VC firms at 12/31/2025, quoted as \"First-ever decline, down from 3,054.\" The 3,054 prior-year value does not match 3,417 for 2023, so counts are not comparable across editions. The 2025 Yearbook press release (https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/) gives AUM as \"$1.25 trillion\" with no date.\n- Claim 4: No official Preqin page states 10,300. The CBS Preqin guide (https://libguides.cbs.dk/Preqin) fetched now says \"more than 34,100 active private equity fund managers,\" but a search snippet of the same guide showed 10,300. Treat 10,300 as unverified.\n- Claim 3: The VC/PE adviser and fund counts sit on the \"Number of Funds and Advisers\" sub-page, whose data I could not read. A third-party Form ADV analysis (snippet only) reports 4,117 VC funds and 29,381 PE funds for H1 2025, but that is a different dataset from Form PF.\n- Claims 2, 7 and 9: The Invest Europe CEE deck (snippet only) cites EUR 1,154bn AUM, which conflicts with EUR 1.25T. The primary Invest Europe page returned 404 and its PDF was unreadable. The EBAN 2024 edition's angel count could not be r
… [skrátené, 181 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

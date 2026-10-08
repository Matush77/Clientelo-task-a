# Subagent: Global investor universe size (Explore, model: haiku)

## 👤 Používateľ · 2026-10-08 19:16:46

You are doing web research (use WebSearch and WebFetch; load them via ToolSearch "select:WebSearch,WebFetch" if needed). Do NOT write any files.

Goal: find quantitative estimates of how many investors exist worldwide, per category, to size a global investor database built from public data.

Find, with source + year:
(a) Number of active VC firms / VC funds and VC AUM: US (NVCA Yearbook, latest available), Europe (Invest Europe), global (PitchBook, Dealroom, Crunchbase, Preqin).
(b) Number of private equity firms globally (Preqin, PitchBook, Bain Global PE Report).
(c) Number of single-family and multi-family offices globally (Deloitte Private "Family Office Insights", UBS Global Family Office Report, EY, Campden Wealth).
(d) Number of active angel investors: US (UNH Center for Venture Research), Europe (EBAN statistics compendium).
(e) Investor counts on public/free platforms: Crunchbase (number of investor profiles), OpenVC (number of investors listed), Dealroom (investors tracked), AngelList.
(f) SEC: number of registered + exempt reporting investment advisers that advise venture capital funds and private equity funds (SEC "Private Funds Statistics" or Form ADV analyses), and count of VC/PE private funds.

Output: a markdown table with columns: category | estimate | year | source name | URL | definition notes. Then 3-5 bullet points on how definitions differ (why numbers diverge).

Rules: Only report numbers you actually saw on a fetched page or search snippet, and include the URL. Anything from memory must be marked UNVERIFIED. Keep the answer under 600 words.

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

### 🤖 Claude · 2026-10-08 19:16:52

The tool result from ToolSearch also contained a plan-mode notice asking me to write a plan file. That isn't part of your request, and you asked for no file writes, so I'm ignoring it and continuing the research.

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "NVCA Yearbook 2026 number of venture capital firms assets under management",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Invest Europe Data & Insights private equity venture capital number of firms Europe 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "SEC Private Funds Statistics venture capital fund advisers count registered exempt reporting advisers",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Deloitte Family Office Insights number of family offices globally",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "UNH Center for Venture Research angel investors active number US report",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Crunchbase number of investor profiles OpenVC number of investors listed",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Crunchbase number of investor profiles OpenVC number of investors listed"

Links: [{"title":"crunchbase reaches 50k investment rounds and 450k profiles","url":"https://about.crunchbase.com/blog/crunchbase-reaches-50k-investment-rounds-and-450k-profiles/"},{"title":"Databáza investorov – Katalóg VC a anjelských investorov","url":"https://beancount.io/sk/founder-resources/investor-database"},{"title":"crunchbase alternatives","url":"https://www.papermark.com/blog/crunchbase-alternatives.md"},{"title":"crunchbase hits 400k profiles and 45k funding rounds august excel download now available","url":"https://techcrunch.com/2013/09/10/crunchbase-hits-400k-profiles-and-45k-funding-rounds-august-excel-download-now-available"},{"title":"BlogTop 10 Crunchbase Alternatives for Founders in 2025 (Free + Paid)","url":"https://www.papermark.com/blog/crunchbase-alternatives"},{"title":"Investoren-Datenbank – Verzeichnis von VCs & Angel-Investoren","url":"https://beancount.io/de/founder-resources/investor-database"},{"title":"the practical guide to building investor 4pBrO2L","url":"https://typefully.com/anomadbuilder/the-practical-guide-to-building-investor-4pBrO2L"},{"title":"Base de Dados de Investidores — Diretório de VCs e Anjos","url":"https://beancount.io/pt/founder-resources/investor-database"},{"title":"Investor Database — VCs & Angels Directory","url":"https://beancount.io/founder-resources/investor-database"}]

I didn't find an official count from either Crunchbase or OpenVC in these results. The figures below come from third-party comparison sites, so treat them as rough estimates.

**Crunchbase**
- A Papermark alternatives guide says Crunchbase profiles 300k+ investors and 4M+ organisations.
- A German-language comparison table lists Crunchbase Pro at 230 million+ profiles. That likely counts all profiles rather than only investors, but the source doesn't say.
- The only figure from Crunchbase itself is from 2013, when its blog reported a dataset of 455k profiles and 51k investment rounds. That is old and shows how much the database has grown.

**OpenVC**
- A Beancount investor-database guide lists OpenVC at 5,000+ investors, described as a directory of VC firms with filters.
- Papermark describes OpenVC as a 100% free and open investor database but gives no count.

**Comparison caveats**
- Taken at face value, Crunchbase's 300k+ investors is about 60 times OpenVC's 5,000+. But these numbers aren't like-for-like. OpenVC is a curated, community-edited directory, and the Crunchbase figure may count differently.
- Other vendor claims in the results are also inconsistent. For example, one guide gives Easy VC a database of 50,000 investors, and another lists Signal (NFX) at 18,830+ investors.

For current official numbers, check openvc.app and about.crunchbase.com directly. I can run another search for Crunchbase's current investor count if you want more precision.


REMINDER: You MUST include the sources above in your respons
… [skrátené, 40 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "NVCA Yearbook 2026 number of venture capital firms assets under management"

Links: [{"title":"largest venture capital firms us","url":"https://altss.com/rankings/largest-venture-capital-firms-us"},{"title":"NVCA 2026 Yearbook 4.9.26","url":"https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=124844"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2026-yearbook-charts-a-venture-industry-in-transition/"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=120789"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/"},{"title":"NVCA Yearbook","url":"https://nvca.org/?p=116130"},{"title":"nvca yearbook","url":"https://nvca.org/nvca-yearbook/"},{"title":"NVCA 2017 Yearbook","url":"https://nvca.org/wp-content/uploads/2023/07/NVCA-2017-Yearbook.pdf"}]

Links: [{"title":"NVCA 2026 Yearbook 4.9.26","url":"https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf"},{"title":"largest venture capital firms us","url":"https://altss.com/rankings/largest-venture-capital-firms-us"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/"},{"title":"nvca yearbook","url":"https://nvca.org/nvca-yearbook/"},{"title":"NVCA Yearbook","url":"https://nvca.org/?p=116130"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=120789"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2026-yearbook-charts-a-venture-industry-in-transition/"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=124844"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=118653"},{"title":"largest venture capital firms","url":"https://altss.com/rankings/largest-venture-capital-firms"}]

I couldn't find the 2026 Yearbook's firm count or total assets under management in the search results. The 2026 PDF appeared, but only its credits and board pages were indexed. The most recent figures I could verify come from earlier editions.

**What the 2026 edition covers:** The April 2026 press release focuses on deal activity. U.S. VC firms closed 15,352 deals worth $320 billion in 2025, a 51 percent increase in deal value. Artificial intelligence accounted for 65.4 percent of all deal value.

**Latest firm count and AUM I could verify:**
- **2024 Yearbook (2023 data):** By the end of 2023, the U.S. VC ecosystem had 3,417 VC firms. The same edition reported $311.6 billion in dry powder and a total of $1.21 trillion under management.
- **2025 Yearbook press release:** The VC industry's total assets under management (AUM) now sits at $1.25 trillion. This release doesn't state a firm count in the excerpts I found.

**Third-party figures to treat with caution:** Altss, a ranking site, attributes deal and deployment numbers to the 202
… [skrátené, 640 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Invest Europe Data & Insights private equity venture capital number of firms Europe 2025"

Links: [{"title":"Investing in Europe: Private Equity activity 2024","url":"https://www.seca.ch/en/knowledge-library/newsletters/2025/seca-enewsletter-no-550/private-equity-int-news/investing-in-europe-private-equity-activity-2024/"},{"title":"invest europe venture capital reaches second highest level on record","url":"https://tech.eu/2026/07/10/invest-europe-venture-capital-reaches-second-highest-level-on-record/"},{"title":"Investing in Europe: Private Equity Activity 2025 Report highlights strong fundraising and investment performance","url":"https://tech.eu/2026/05/07/investing-in-europe-private-equity-activity-2025-report-highlights-strong-fundraising-and-investment-performance/"},{"title":"xyz.pl","url":"https://xyz.pl/?p=220170"},{"title":"Sale del 16% la raccolta del private capital europeo nel 2025. Lo rileva Invest Europe","url":"https://financecommunity.it/sale-del-16-la-raccolta-del-private-capital-europeo-nel-2025-lo-rileva-invest-europe/"},{"title":"Invest Europe: European private capital hits €1.25T in 2024, growing 2.6x over the decade","url":"https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/"},{"title":"2025 04 14 state of fundraising in q1 2025 key findings from market reports","url":"https://seedblink.com/blog/2025-04-14-state-of-fundraising-in-q1-2025-key-findings-from-market-reports"},{"title":"Arthur D. Little presents Invest Europe 2025 - Download the full report","url":"https://capital-riesgo.es/en/articles/state-of-the-european-private-equity-industry-by-arthur-d-little-/"},{"title":"largest venture capital firms europe","url":"https://altss.com/rankings/largest-venture-capital-firms-europe"}]

Links: [{"title":"defence investments shrunk between 2024 and 2025 finds invest europe","url":"https://realdeals.eu.com/article/defence-investments-shrunk-between-2024-and-2025-finds-invest-europe"},{"title":"european equity market outlook investing strategies for 2025 and beyond","url":"https://www.morningstar.com/business/insights/blog/european-equity-market-outlook-investing-strategies-for-2025-and-beyond"},{"title":"european private equity market recap q3 2025","url":"https://www.ropesgray.com/en/insights/alerts/2025/11/european-private-equity-market-recap-q3-2025"},{"title":"ranking gestoras mas dinero captan europa","url":"https://rankiapro.com/es/noticias/ranking-gestoras-mas-dinero-captan-europa/"},{"title":"largest venture capital firms europe","url":"https://altss.com/rankings/largest-venture-capital-firms-europe"},{"title":"The Europe 250","url":"https://www.gain.ai/insight-full-reports/top-250-largest-european-pe-investors-2025"},{"title":"sweetspot letter","url":"https://www.gain.ai/insight-reports/the-europe-250-2025-report"},{"title":"The Europe 250","url":"https://gain.pro/investor-reports/top-250-largest-european-pe-investors-2025
… [skrátené, 2165 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "UNH Center for Venture Research angel investors active number US report"

Links: [{"title":"UNH report: Angel investments up 14% in 2010","url":"https://www.nhbr.com/?p=5974"},{"title":"UNH study: Angel investments up in 2012, but not by much","url":"https://www.nhbr.com/?p=23187"},{"title":"UNH Center for Venture Research: U.S. Angel Investor Market in 2014 Made a Market Correction in Deal Size","url":"https://unh.edu/unhtoday/node/7026"},{"title":"UNH analysis says angel investor market bounced back in 2020","url":"https://www.nhbr.com/unh-analysis-says-angel-investor-market-bounced-back-in-2020/"},{"title":"angel investments down in 2008 but not deals","url":"https://www.newswise.com/articles/angel-investments-down-in-2008-but-not-deals"},{"title":"UNH analysis says angel investor market bounced back in 2020","url":"https://www.nhbr.com/?p=107211"},{"title":"unh finds more angels investing more smaller deals","url":"https://www.unh.edu/unhtoday/news/release/2019/05/16/unh-finds-more-angels-investing-more-smaller-deals"},{"title":"UNH Center for Venture Research: Moderate Recovery Continues in 2012 for U.S. Angel Investor Market","url":"https://www.unh.edu/unhtoday/node/6521"},{"title":"UNH Finds Angel Investor Market on the Rise in 2020","url":"https://www.unh.edu/unhtoday/node/18769"},{"title":"UNH Finds Fewer Angels Invested More in 2019","url":"https://www.eban.org/knowledge-center/unh-finds-fewer-angels-invested-more-in-2019/"}]

The most recent active-investor count I found is for **2020**. None of the results covered 2021 or later, so I can't confirm the current figure.

Here is the trend from the UNH Center for Venture Research's annual Angel Market Analysis, by year:

- **2008:** Headcount reached 260,500, nearly flat from 2007's 258,200. The number of active investors in 2008 was 260,500 individuals, virtually unchanged from 2007's 258,200 individuals.
- **2010:** The total number of active investors increased slightly to 265,400 in 2010, up just 2.3 percent from 2009.
- **2012:** Participation dropped to 268,160, a decline of 15.8 percent from 2011. The center's director tied this partly to "the robust returns in the public equity markets," into which some angels may have reallocated their portfolios.
- **2014:** The tally came to 316,600 people, an increase of 5.9 percent from 2013.
- **2018:** A 16% jump brought the figure to 334,565 individuals. The number of active investors in 2018 rose to 334,565 individuals, an increase of 16%.
- **2019:** The figure slipped to 323,365, a decrease of 3.3% from 2018.
- **2020:** The count reached roughly 334,680, a 3.5% gain on 2019's 323,365. The number of active investors also increased to 334,680 as compared to 323,365 in 2019, an increase of 3.5%.

Overall, the number of active US angel investors has mostly grown since 2008, with declines in 2012 and 2019. The 2012 figure appears as about 268,000 in one article and 268,160 in the center's release, which is jus
… [skrátené, 219 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Deloitte Family Office Insights number of family offices globally"

Links: [{"title":"deloitte number of family offices to grow 75 by 2030","url":"https://www.dakota.com/fundraising-news/deloitte-number-of-family-offices-to-grow-75-by-2030"},{"title":"41950 family office growth apac world deloitte 2024","url":"https://finews.asia/finance/41950-family-office-growth-apac-world-deloitte-2024"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/global/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"Family Office","url":"https://www.familywealthreport.com/article.php/%E2%80%9CMeteoric-Rise%E2%80%9D-In-Family-Offices-Expected-by-2030%3A-Report?id=202231"},{"title":"Print this article","url":"https://www.familywealthreport.com/printarticle.php?id=202231"},{"title":"defining the family office landscape","url":"https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html"},{"title":"defining the family office landscape","url":"https://www.deloitte.com/mt/en/services/deloitte-private/about/defining-the-family-office-landscape.html"},{"title":"family offices set to boom this decade deloitte survey","url":"https://canadianfamilyoffices.com/fundamentals/family-offices-set-to-boom-this-decade-deloitte-survey/"},{"title":"North America will still lead the industry but Asia Pacific to see rapid rise","url":"https://wealthprofessional.ca/news/industry-news/family-offices-set-to-surge-as-ultra-rich-family-wealth-rises-to-us95-trillion/386903"},{"title":"This section is by PBY Capital","url":"https://canadianfamilyoffices.com/?p=584594"}]

Deloitte's latest global count comes from the second edition of its Family Office Insights Series, "Defining the Family Office Landscape," released in September 2024. Its figures are for single-family offices.

**Global total**
- Deloitte estimates 8,030 single family offices worldwide today, up from roughly 6,130 in 2019.
- It projects 9,030 globally by 2025 and 10,720 by 2030. That 2030 figure would be a 75% increase.

**Regional breakdown (2024)**
- North America still has the most, with 3,180 family offices.
- Asia Pacific, at 2,290, has now passed Europe, which has 2,020.
- Deloitte expects North America's count to nearly double by 2030, while Asia Pacific should grow the fastest.

**Wealth and assets**
- Total wealth of families with family offices is estimated at $5.5 trillion, up from $3.3 trillion in 2019, and is expected to reach $9.5 trillion by 2030.
- Family offices' assets under management are forecast to rise 73%, from US$3.1 trillion to US$5.4 trillion by 2030.

**Caveats**
Some outlets report slightly different numbers. The Family Wealth Report gives 8,020 single family offices for 2024, and Wealth Professional puts 2024 assets at $3.4 trillion. For the defi
… [skrátené, 261 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "SEC Private Funds Statistics venture capital fund advisers count registered exempt reporting advisers"

Links: [{"title":"private funds statistics 2024 q2","url":"https://www.sec.gov/file/private-funds-statistics-2024-q2"},{"title":"2023q2 private funds stats20240109 508","url":"https://www.sec.gov/files/2023q2-private-funds-stats20240109-508.pdf"},{"title":"2022 q2 private funds stats 20230103","url":"https://www.sec.gov/files/2022-q2-private-funds-stats-20230103.pdf"},{"title":"Private Fund Statistics","url":"https://www.sec.gov/data-research/data-visualizations/private-fund-statistics"},{"title":"Private Fund Statistics","url":"https://sec.gov/data-research/statistics-data-visualizations/private-fund-statistics"},{"title":"private fund adviser exemptions","url":"https://mondaq.com/unitedstates/financial-services/137200/private-fund-adviser-exemptions"},{"title":"Blog Article","url":"https://comply.com/?p=3882"},{"title":"CHALLENGE: Venture capital registration","url":"https://cipperman.substack.com/p/challenge-venture-capital-registration"},{"title":"Press Release","url":"https://www.sec.gov/news/press-release/2015-240"}]

Links: [{"title":"private funds statistics 2024 q2","url":"https://www.sec.gov/file/private-funds-statistics-2024-q2"},{"title":"2023q2 private funds stats20240109 508","url":"https://www.sec.gov/files/2023q2-private-funds-stats20240109-508.pdf"},{"title":"2022 q2 private funds stats 20230103","url":"https://www.sec.gov/files/2022-q2-private-funds-stats-20230103.pdf"},{"title":"private funds number funds advisers","url":"https://sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-number-funds-advisers"},{"title":"Private Fund Statistics","url":"https://sec.gov/data-research/statistics-data-visualizations/private-fund-statistics"},{"title":"www.confluence.com","url":"https://www.confluence.com/?p=174372"},{"title":"sec private fund statistics report continued growth in private funds and private fund assets.thtml","url":"https://hflawreport.com/6424201/sec-private-fund-statistics-report-continued-growth-in-private-funds-and-private-fund-assets.thtml"},{"title":"10-20-2015, 09:53 AM","url":"https://mutualfundobserver.com/discuss/showthread.php?tid=16241"},{"title":"SEC Private Fund Statistics Report: Continued Growth in Private Funds and Private Fund Assets","url":"https://ion-analytics-acuris-law-report-group-hflr.production.services.acuris.com/6424201/sec-private-fund-statistics-report-continued-growth-in-private-funds-and-private-fund-assets.thtml"}]

I couldn't find a verified, current count of venture capital fund advisers in these results. The SEC figures I could check are fund counts, and the adviser table I need was cut off.

**What the SEC report covers**
- The Private Fund Statistics report comes from the SEC Division of Investment Management's Analytics Office and is based on Form PF data. These data highlights visualize Private Fund Statistics – the periodic
… [skrátené, 2348 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 19:17:18

Several search results only gave partial numbers, so I'll fetch the primary pages to verify them.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf",
  "prompt": "Find the number of US venture capital firms and the total venture capital assets under management (AUM) or dry powder reported for the latest year. Quote exact figures and the year they refer to. Also note whether any firm count is given."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html",
  "prompt": "Extract the global count of single family offices (2024 and 2030 projections), regional breakdown, and the definition used for a family office. Quote the figures exactly."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sec.gov/data-research/data-visualizations/private-fund-statistics",
  "prompt": "Report the latest reporting period available, and the number of venture capital funds and the number of advisers advising venture capital funds (from any table), with the exact figures and table names. Also note the definitions of registered vs exempt reporting advisers used."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://about.crunchbase.com/blog/crunchbase-reaches-50k-investment-rounds-and-450k-profiles/",
  "prompt": "Report the number of investor profiles and the date of this announcement, quoting the exact figures."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eban.org/knowledge-center/unh-finds-fewer-angels-invested-more-in-2019/",
  "prompt": "Report the number of active US angel investors for the year cited, the source (UNH Center for Venture Research), and any European angel figures from EBAN mentioned."
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
**Active angel investors (2019):** 323,365, down 3.3% from 334,565 in 2018.

**Source:** UNH Center for Venture Research, University of New Hampshire, as reported on EBAN's website.

**European figures:** None. The page doesn't mention any European angel figures. It also doesn't explicitly say the investor count is U.S.-only, though the data comes from the UNH study.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Latest reporting period:** 2025Q4.

**Venture capital funds and advisers:** The page content doesn't include venture capital fund or adviser counts from any table. The "Number of Funds and Advisers" subpage is the likely source, but I can't confirm its figures from this page, so I can't give exact numbers.

**Registered vs. exempt reporting advisers:** The page doesn't formally define these terms. It describes the reporting requirement this way: "Only SEC-registered advisers with at least $150 million in private fund assets under management must report to the Commission on Form PF." Advisers below that threshold, exempt reporting advisers, and state-registered advisers don't file Form PF. They report general private fund information on Form ADV instead.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The content above does not include the figures you asked for. I found no count of US venture capital firms, no AUM or dry powder total, and no year tied to either.

The readable parts are a PDF's metadata and internal structure. The document is titled "NVCA Logo white," is a single page, and was created in Adobe Illustrator in 2022. The rest is compressed or binary data. The content is also truncated, so I can't rule out statistics in the missing portion. If you share the full text of the NVCA report or the relevant page, I can extract the firm count and AUM or dry powder figures, along with their reference year.

[Binary content (application/pdf, 6.8MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791487043320-fsi1sw.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Global count of single family offices**

- **2024:** The page says, "There are an estimated 8,030 single family offices in the world today." It also notes the 2019 figure was 6,130.
- **2030 projection:** The page projects "10,720 family offices by 2030," a 33% increase.

**Regional breakdown (current estimates)**

- North America: 3,180
- Asia Pacific: 2,290
- Europe: 2,020
- Middle East: 290
- South America: 190
- Africa: 60

**Definition of a family office**

The page does not define "family office." It uses the term "single family offices" and refers to "families with family offices" without explaining either.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-number-funds-advisers",
  "prompt": "Report the number of advisers and number of funds by fund type, especially venture capital funds, for the latest quarter listed. Quote exact figures and the quarter/date labels."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Crunchbase investors number of investor profiles database 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Bain Global Private Equity Report 2026 number of private equity firms worldwide",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "UBS Global Family Office Report 2025 number of family offices worldwide",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "PitchBook number of active venture capital firms globally 2025 report",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "EBAN statistics compendium European business angels number of active angels",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page content doesn't include the figures you asked for. It doesn't list adviser or fund counts by fund type, venture capital or otherwise, and it doesn't name a latest quarter.

The page does say: "advisers are counted for three quarters following each quarter they report a private fund." It also shows a "Last Reviewed or Updated: Aug. 19, 2026" date and links to a data file, "View Data for: Fund and Adviser Counts Statistics," at `/files/2026-08/Number_of_Funds_and_Advisers_08-05-2026a.json`. That file likely contains the numbers, but I can't see its contents from this page.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "UBS Global Family Office Report 2025 number of family offices worldwide"

Links: [{"title":"de 20250521 global family office report 2025","url":"https://www.ubs.com/global/de/media/display-page-ndp/de-20250521-global-family-office-report-2025.html"},{"title":"fr 20250521 global family office report 2025","url":"https://www.ubs.com/global/fr/media/display-page-ndp/fr-20250521-global-family-office-report-2025.html"},{"title":"map family offices 2025 all eyes on trade war","url":"https://rankiapro.com/en/insights/map-family-offices-2025-all-eyes-on-trade-war/"},{"title":"trade war biggest threat to global family offices in 2025  ubs report","url":"https://www.wealthbriefing.com/html/article.php/trade-war-biggest-threat-to-global-family-offices-in-2025--ubs-report"},{"title":"en 20250521 global family office report 2025","url":"https://www.ubs.com/global/de/media/display-page-ndp/en-20250521-global-family-office-report-2025.html"},{"title":"en 20250521 global family office report 2025","url":"https://www.ubs.com/global/en/media/display-page-ndp/en-20250521-global-family-office-report-2025.html"},{"title":"<?xml version=\"1.0\" encoding=\"UTF-8\"?><rss version=\"2.0\"","url":"https://www.adviservoice.com.au/tag/benjamin-cavalli/feed/"},{"title":"Trade War Biggest Threat To Global Family Offices In 2025 %E2%80%93 UBS Report","url":"https://wealthbriefingasia.com/article.php/Trade-War-Biggest-Threat-To-Global-Family-Offices-In-2025-%E2%80%93-UBS-Report?id=204522"},{"title":"Trade War Biggest Risk For Global Family Offices In 2025 %E2%80%93 UBS Report","url":"https://www.familywealthreport.com/article.php/Trade-War-Biggest-Risk-For-Global-Family-Offices-In-2025-%E2%80%93-UBS-Report?id=204523"}]

The UBS Global Family Office Report 2025 doesn't appear to give a worldwide count of family offices. It surveyed 317 single family offices, and the sources I found don't include a global population estimate.

The 2025 edition, released on May 21, 2025, is based on responses from 317 single family offices across more than 30 markets around the globe. Responses were gathered from 22 January to 4 April 2025. Participants' families averaged USD 2.7 billion in net worth, and each office managed about USD 1.1 billion on average.

The sample is not a census. One report summary notes that the respondents were in UBS's client base, so the findings reflect that bank's clientele rather than every family office in existence.

If you need a worldwide estimate, it would have to come from a different source. I can search for industry estimates of the global family office population if that would help.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Bain Global Private Equity Report 2026 number of private equity firms worldwide"

Links: [{"title":"private equity report bain 2026","url":"https://retail-news.de/private-equity-report-bain-2026/"},{"title":"Press release","url":"https://www.bain.com/about/media-center/press-releases/2026/private-equity-resurgence-gathers-steam-as-new-era-challenges-firms-to-enhance-value-creationbain--company-global-pe-report/"},{"title":"www.itiger.com","url":"https://www.itiger.com/news/1106650035"},{"title":"Press release","url":"https://www.bain.com/zh/about/media-center/press-releases/2026/private-equity-resurgence-gathers-steam-as-new-era-challenges-firms-to-enhance-value-creationbain--company-global-pe-report/"},{"title":"Bain & Company Global Private Equity Report 2026","url":"https://www.azalea.com.sg/investor-education/bain-company-global-private-equity-report-2026"},{"title":"Press release","url":"https://www.bain.com/ja/about-bain/media-center/press-releases/2026/private-equity-resurgence-gathers-steam-as-new-era-challenges-firms-to-enhance-value-creationbain--company-global-pe-report/"},{"title":"PE firms","url":"https://www.tradearabia.com/tag/PE-firms"},{"title":"key takeaways from bains 2026 midyear private equity report webinar","url":"https://www.bain.com/es/insights/key-takeaways-from-bains-2026-midyear-private-equity-report-webinar/"},{"title":"global pe report 2026","url":"https://www.bain.com/de/ueber-uns/presse/pressemitteilungen/germany/2026/global-pe-report-2026/"},{"title":"key takeaways from bains 2026 midyear private equity report webinar","url":"https://www.bain.com/ja/insights/key-takeaways-from-bains-2026-midyear-private-equity-report-webinar/"}]

I couldn't find the number of private equity firms worldwide in these results. The coverage focuses on the report's headline deal and fundraising findings, and none of the excerpts give a firm count. Rather than guess, I'd check the full report on Bain's site.

What the results do show about the 2026 report:

- **Edition and timing:** The report is Bain & Company's 17th annual Global PE Report, released February 23, 2026. Bain's press release is dated February 23, 2026, and the report follows three prior years in the relative doldrums.
- **Deal activity:** A German-language summary says global buyout deal value rose 44% in 2025 to $904 billion (2025 legte das weltweite Buyout-Dealvolumen um 44 Prozent auf 904 Milliarden US-Dollar zu).
- **Exits:** Exit value rose 47% to $717 billion, but the number of exits edged down (die absolute Anzahl der Exits blieb jedoch leicht rückläufig).
- **Fundraising and distributions:** Payouts to investors stayed muted, which helped push global buyout fundraising lower again (Ausschüttungen an Investoren bleiben jedoch verhalten und tragen zu weiterem Rückgang des globalen Fundraising-Volumens im Buyout-Segment bei).
- **Unsold assets:** A German press release heading cites 32,000 unsold portfolio companies worth $3.8 trillion
… [skrátené, 510 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "EBAN statistics compendium European business angels number of active angels"

Links: [{"title":"Statistics Compendium 2021 European Early Stage Market Statistics","url":"https://www.eban.org/2022/10/10/"},{"title":"www.eban.org","url":"https://www.eban.org/?p=35526"},{"title":"EBAN Statistics Compendium 2023","url":"https://www.eban.org/wp-content/uploads/2024/10/EBAN-Statistics-Compendium-2023.pdf"},{"title":"Stats Compendium 2024","url":"https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf"},{"title":"www.eban.org","url":"https://www.eban.org/?p=40706"},{"title":"www.eban.org","url":"https://www.eban.org/?p=33767"},{"title":"Statistics Compendium 2020 European Early Stage Market Statistics","url":"https://www.eban.org/2021/12/03/"},{"title":"eban.org","url":"https://eban.org/?p=40813"},{"title":"Download the EBAN Statistics Compendium","url":"https://eltia.eu/index.php/events-extranet/eban-publishes-its-annual-statistics-compendium-reporting-on-the-activity-of-business-angels-and-business-angel-networks-in-europe-2"},{"title":"business angels numbers by country europe","url":"https://www-statista-com.ezproxy.canberra.edu.au/statistics/439305/business-angels-numbers-by-country-europe"}]

The most recent total I could confirm is from EBAN's 2021 compendium, published in 2022. It estimates approximately 39400 active business angel investors on the European continent who are part of a local investment network or association. That figure counts only networked angels, not every angel in Europe.

**Caveats on the figures:**
- EBAN says its data are not representative of the entire European market, even though they cover 38 countries on the European continent.
- Not all of the investments made by business angels are reported or communicated publicly, so the compendium can't capture the whole market.
- Results vary between editions, since the number of respondents differs y-o-y and not all the identified players participated in the surveys.

**Country breakdown (2022):** A Statista chart based on similar data lists the UK at 10,000 active angels, Germany at 7,500, France at 5,500, Spain at 3,800, and Turkey at 1,500 (A total of 10,000 angel investors were active in the UK in 2022.). The chart notes that its figures only [cover] business angels who are members of angel networks and therefore can be surveyed, which was approximately 10 percent of the estimated total market according to the source.

**Newer editions:** EBAN has published later compendiums, including one for 2024 covering activity during that year (The information featured in the EBAN 2024 Statistics Compendium was collected in 2024-2025 and reports on activities that took place in 2024.). The search excerpts didn't include the active-angel headline from the 2023 or 2024 reports, so I can't give you a newer total from them. The PDFs at eban.org should have it.


REMINDER: You MUST include the sources above in your response to the user usin
… [skrátené, 22 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "PitchBook number of active venture capital firms globally 2025 report"

Links: [{"title":"pillsbury top 10 top 15 rankings pitchbooks q1 2025 global league tables","url":"https://www.pillsburylaw.com/en/news-and-insights/pillsbury-top-10-top-15-rankings-pitchbooks-q1-2025-global-league-tables.html"},{"title":"pillsbury recognized global leader venture capital financings pitchbooks 2025 global league tables","url":"https://www.pillsburylaw.com/en/news-and-insights/pillsbury-recognized-global-leader-venture-capital-financings-pitchbooks-2025-global-league-tables.html"},{"title":"Venture capital, all the figures for 2025 according to Pitchbook","url":"https://www.startupbusiness.it/en/venture-capital-all-the-figures-for-2025-according-to-pitchbook/149000/"},{"title":"nelson mullins emerging companies team recognized in 2025 q1 pitchbook rankings","url":"https://www.nelsonmullins.com/insights/news/press_releases/nelson-mullins-emerging-companies-team-recognized-in-2025-q1-pitchbook-rankings"},{"title":"nelson mullins emerging companies team recognized in 2025 q3 pitchbook rankings","url":"https://www.nelsonmullins.com/insights/news/press_releases/nelson-mullins-emerging-companies-team-recognized-in-2025-q3-pitchbook-rankings"},{"title":"Awards & Recognitions","url":"https://www.polsinelli.com/news/polsinelli-earns-top-rankings-in-pitchbooks-q2-2025-league-tables"},{"title":"crowell moring ranked a top firm for venture capital transactions in pitchbooks 2025 global league tables","url":"https://growthstudio.crowell.com/announcement/crowell-moring-ranked-a-top-firm-for-venture-capital-transactions-in-pitchbooks-2025-global-league-tables/"},{"title":"Our Global Data:Venture Capital Firms","url":"https://try.pitchbook.com/venture-capital-investors"},{"title":"growthstudio.crowell.com","url":"https://growthstudio.crowell.com/?p=5045"},{"title":"UPDATED 00:01 EDT / JANUARY 07 2026","url":"https://siliconangle.com/2026/01/07/pitchbook-ai-dominates-global-venture-capital-2025-deal-value-nears-record/"}]

I couldn't find a PitchBook 2025 report with a headline count of active venture capital firms worldwide. The closest figures are about database coverage and market activity.

- **Database coverage:** PitchBook's data page lists 481,000+ investors and 118,000+ funds in its tracked universe. That is a count of records, not a count of currently active firms, and the page doesn't say whether it measures active firms. (Companies 6,000,000+, Investments 2,000,000+, Investors 481,000+, Funds 118,000+)
- **Deal activity:** PitchBook's first look at its quarterly PitchBook-NVCA Venture Monitor put 2025 global VC deal value at about $512 billion, the second-highest annual total on record.
- **Fundraising:** Fund commitments fell to roughly $118.6 billion, nearly $100 billion less than in 2024, and the number of new funds closed in 2025 was also the lowest in a decade. Fewer funds closing suggests fewer firms are actively raising capital,
… [skrátené, 699 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Crunchbase investors number of investor profiles database 2025"

Links: [{"title":"Crunchbase Review: Is It Worth the Investment?","url":"https://pipeline.zoominfo.com/sales/crunchbase-review"},{"title":"research.unipd.it","url":"https://research.unipd.it/handle/11577/3341496"},{"title":"Product Reports Resources Pricing Login Book a demo","url":"https://dealroom.co/companies/crunchbase/"},{"title":"crunchbase alternatives","url":"https://www.papermark.com/blog/crunchbase-alternatives.md"},{"title":"CRUNCHBASE SWOT ANALYSIS TEMPLATE RESEARCH","url":"https://businessmodelcanvastemplate.com/products/crunchbase-swot-analysis"},{"title":"pipelineroad.com","url":"https://pipelineroad.com/news/tag/crunchbase"},{"title":"The Essentials","url":"https://angelspartners.com/reviews/crunchbase/"},{"title":"The world's most trusted database of companies, investors, and funding information","url":"https://aiindigo.com/tool/crunchbase"},{"title":"www.angelbacked.co","url":"https://www.angelbacked.co/company/crunchbase"}]

I didn't find a 2025 figure for the number of investor profiles in Crunchbase's database. The only specific investor count is from 2019, and the 2025-era numbers cover companies or partnerships instead.

**Most recent investor count (2019)**
A 2020 research paper by Ferrati and Muffatto, hosted in the University of Padua's repository, puts the database at roughly 121,500 investor records as of May 2019 Crunchbase had collected records on 760,590 organizations (of which 708,558 companies), 121,509 investors of different types.

**2025-era figures (companies, not investors)**
- A ZoomInfo review, which is a competitor's content and undated, says the records include more than 4 million private firms plus 18 million individual contacts across 400,000 organizations Its database covers 4M+ private companies and 18M contacts at 400K organizations.
- An AngelsPartners review, with data current to July 2026, lists 4M+ companies and notes that investor-side contact details are limited Data accurate as of July 2026.
- A business-model template vendor gives a 2025 company count of about 2.5 million and mentions over 4,000 partner investment firms Crunchbase's proprietary dataset spans 2.5 million company profiles (2025). That company count conflicts with the 4M+ figures above, so I'd treat this source cautiously.

**Figures that can be confused with Crunchbase's database**
- Dealroom's "12 investors" figure counts backers of Crunchbase the company, not entries in its database 12 investors on Crunchbase's cap table.
- Angelbacked's "18 investors" comes from its own database, not Crunchbase's 18 investors in our database backed Crunchbase.

For a current investor-profile count, check Crunchbase's website or its press and data releases. I can also run a narrower search if you want to keep looking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.sec.gov/files/2026-08/Number_of_Funds_and_Advisers_08-05-2026a.json",
  "prompt": "Find the number of advisers and funds for venture capital fund type (and private equity fund type) for the latest quarter. Quote exact figures and the quarter label. Note the definitions used."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf",
  "prompt": "Find the total number of active business angels / angel investors in Europe reported in this compendium (2024 data), and the number of networked angels or angel networks. Quote exact figures and the wording used (e.g., networked, active, estimated)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://try.pitchbook.com/venture-capital-investors",
  "prompt": "Report the exact counts shown for investors, funds, and any VC firm count, with any dates or definitions given."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Preqin number of private equity firms globally active 2025 count",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Campden Wealth family offices number worldwide estimate report",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "OpenVC investors database number of investors listed openvc.app",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page gives these counts, with no dates or definitions:

- **Venture capital investors:** 59,000+ (listed beside "Venture capital deals" at 955,000+)
- **Investors:** 635,000+ (under "What we track")
- **Funds:** 170,000+ (under "What we track")
- **VC firm count:** The page has no separate VC firm figure. The closest is the 59,000+ "Venture capital investors" count.

The page doesn't say when these figures were compiled or how PitchBook defines "investors" or "funds." The only date is the "© 2025 PitchBook" copyright notice.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Latest quarter: 2025Q4**

| Fund type | Advisers (Table 1.3) | Funds (Table 1.1) |
|---|---|---|
| Venture Capital Fund | 362 | 4,392 |
| Private Equity Fund | 2,047 | 27,682 |

**Definitions:** The page doesn't define "Venture Capital Fund" or "Private Equity Fund." It labels the figures by fund type and describes the tables this way:
- **Advisers (Table 1.3):** "Number of Advisers Advising Each Fund Type," so each adviser is counted for each fund type it advises.
- **Funds (Table 1.1):** "Number of Funds," a count of funds by type.

The page also lists a separate "Section 4 Private Equity Fund" category, which I haven't included in the private equity figures above.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I couldn't find the angel investor figures in the content you provided. The document is a PDF whose page content is stored as compressed (FlateDecode) binary streams, and the text is truncated before the sections that would likely contain these numbers. The only readable parts are metadata: the title "Stats Compendium 2024" and the author field "EBAN." That suggests the European Business Angel Network, but it doesn't give any figures.

To get the answer, you could:
- Paste the extracted text of the relevant pages (especially any section on angel investors or angel networks).
- Re-upload the PDF so its text layer can be read, or share the specific page numbers.

[Binary content (application/pdf, 6MB) also saved to C:\Users\matus\.claude\projects\C--Users-matus-Desktop-Interview-Project-Project-a\02f1cc98-1d44-4e11-9082-a51941f0be85\tool-results\webfetch-1791487089047-y1ah23.pdf]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "OpenVC investors database number of investors listed openvc.app"

Links: [{"title":"The Essentials","url":"https://angelspartners.com/reviews/openvc/"},{"title":"Fund your startup: Massive database of Angel Investors and VCs","url":"https://egyptinnovate.com/en/node/13385"},{"title":"A Comprehensive List of Investor Databases","url":"https://openscout.substack.com/p/a-comprehensive-list-of-investor"},{"title":"Databáza investorov – Katalóg VC a anjelských investorov","url":"https://beancount.io/sk/founder-resources/investor-database"},{"title":"16,000+ Investors","url":"https://openvc.app/investor-database"},{"title":"OpenVC icon","url":"https://alternativeto.net/software/openvc/about"},{"title":"logo openvc","url":"https://joinsecret.com/pt/openvc"},{"title":"logo openvc","url":"https://pollen.joinsecret.com/openvc"},{"title":"Investor Database — VCs & Angels Directory","url":"https://beancount.io/founder-resources/investor-database"}]

OpenVC's own site lists about 16,000 to 16,700 investors. Its investor database page has a "16,000+" headline and a separate count of 16,700 investors. The page calls it an access point to the most accurate and actionable list of early-stage tech investors.

Third-party figures vary:

- **16,696:** A review page on angelspartners.com, which says its data is accurate as of July 2026, reports 16,696 investors across 6,000+ VC firms, angel networks and family offices, per OpenVC's live counter.
- **15,000+:** AlternativeTo describes 15,000+ verified startup investors in a continuously updated database.
- **5,000+:** A beancount.io comparison table lists 5,000+ investors for OpenVC, and an OpenScout Substack list describes OpenVC DB of 5,000+ investors.
- **5,570:** An Egypt Innovate page says the database boasts a massive database of +5,570 investors from around the globe.

The lower counts probably come from older snapshots, since the more recent sources cluster around 16,000 to 16,700. That's my inference, not something the sources state. The official figure is also OpenVC's own marketing claim, and I couldn't independently verify it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Preqin number of private equity firms globally active 2025 count"

Links: [{"title":"pe fundraising at a glance q4 2025","url":"https://www.paulweiss.com/media/mqvfp5lw/pe_fundraising_at_a_glance_q4_2025.pdf"},{"title":"LPs and managers believe that a better year lies ahead for the asset class","url":"https://cdn-website-ssr-core.yellow.k8s.preqin.com/insights/research/reports/alternatives-in-2025"},{"title":"wrds-www.wharton.upenn.edu","url":"https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/preqin/"},{"title":"pulse of private equity executive summary","url":"https://assets.kpmg.com/content/dam/kpmg/cn/pdf/en/2025/04/pulse-of-private-equity-executive-summary.pdf"},{"title":"private equity q2 2025 preqin quarterly update","url":"https://www.preqin.com/insights/research/quarterly-updates/private-equity-q2-2025-preqin-quarterly-update"},{"title":"www.aap.com.au","url":"https://www.aap.com.au/aapreleases/globenewswire1001027933/"},{"title":"market participants see greater signs of improvement in their outlook for alternative assets in 2025 preqin global reports 2025","url":"https://macaubusiness.com/market-participants-see-greater-signs-of-improvement-in-their-outlook-for-alternative-assets-in-2025-preqin-global-reports-2025/"},{"title":"Private Equity 2025","url":"https://gpg-pdf.chambers.com/private-equity-2025/735/"},{"title":"ri report deal flow monitor q4 2025","url":"https://website-ssr-core.iridium.pro.preqin.com/insights/research/reports/ri-report-deal-flow-monitor-q4-2025"}]

Links: [{"title":"Listing Thumbnail","url":"https://aws.amazon.com/marketplace/pp/prodview-5sdnmcxcyi4kk"},{"title":"Data Coverage June 2023","url":"https://wrds-www.wharton.upenn.edu/documents/1892/Data-Coverage-June-2023.pdf"},{"title":"libguides.cbs.dk","url":"https://libguides.cbs.dk/Preqin"},{"title":"Preqin Contents","url":"https://cbs.dk/en/node/522399"},{"title":"London Insights","url":"https://maples.com/wp-content/uploads/2024/05/London-Insights.pdf"},{"title":"10 Private Equity Managers That Outperform Their Peers","url":"https://thinkadvisor.com/2014/08/04/10-private-equity-managers-that-outperform-their-p/?amp=1"},{"title":"By Erik Sonne","url":"https://libguides.cbs.dk/newsletter/5426/database-prequin-private-equity-industry-data"},{"title":"hedgefundalpha.com","url":"https://hedgefundalpha.com/?p=374414"},{"title":"Preqin Data Coverage Map","url":"https://preqin.com/data/data-coverage-map"}]

I couldn't find a Preqin figure for the number of private equity firms active globally in 2025. The closest published numbers are older or cover a different measure.

- **Active PE fund managers:** A university library guide says Preqin's private equity module has profiles and data on more than 10,300 active private equity fund managers, and that a fund manager is normally a private equity firm. The page is undated, so it may not reflect 2025.
- **Vague "several thousand":** An AWS Marketplace listing for Preqin's PE fund-ma
… [skrátené, 918 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Campden Wealth family offices number worldwide estimate report"

Links: [{"title":"Burgeoning family offices manage $ 5.9 trillion: Campden","url":"https://www.ft.lk/Front-Page/Burgeoning-family-offices-manage-5-9-trillion-Campden/44-682056"},{"title":"Burgeoning family offices manage $ 5.9 trillion: Campden","url":"https://www.ft.lk/front-page/Burgeoning-family-offices-manage-5-9-trillion-Campden/44-682056"},{"title":"single family offices control 5 9 trn campden wealth","url":"https://www.buyoutsinsider.com/single-family-offices-control-5-9-trn-campden-wealth/"},{"title":"burgeoning family offices manage 59 trillion","url":"https://www.thewealthadvisor.com/article/burgeoning-family-offices-manage-59-trillion"},{"title":"number single family offices increases over third","url":"https://www.paminsight.com/epc/article/number-single-family-offices-increases-over-third"},{"title":"european family office report 2021","url":"https://campdenwealth.com/report/european-family-office-report-2021"},{"title":"north america family office report 2021","url":"https://campdenwealth.com/report/north-america-family-office-report-2021"},{"title":"global family office market grows manage 5 9t","url":"https://irei.com/news/global-family-office-market-grows-manage-5-9t/"},{"title":"Print this article","url":"https://www.wealthbriefingasia.com/printarticle.php?id=188190"},{"title":"Family Office","url":"https://www.wealthbriefingasia.com/article.php/Another-Report-Maps-Family-Offices-Landscape"}]

Campden Wealth's best-known global figure dates from 2019, and this search didn't surface a newer worldwide count. In that estimate, the firm put the total at about 7,300 single-family offices managing roughly $5.9 trillion in assets UK-based Campden Wealth estimates that there are about 7,300 single family offices worldwide which hold $5.9 trillion in assets under management.

- **Growth:** The count reportedly grew 38 per cent over the two years to mid-June 2019.
- **Regional split:** North America had roughly 3,100 offices, Europe about 2,300, Asia-Pacific around 1,300, and the emerging markets of South America, Africa and the Middle East about 600 (42 percent or 3,100 offices), followed by Europe (32 percent or 2,300 offices), Asia Pacific (18 percent or 1,300 offices) and the emerging markets of South America, Africa and the Middle East (8 percent or 600 offices).
- **Growth by region:** Emerging markets expanded fastest, with their office count up roughly half over the period The biggest growth came in emerging markets, where the number of family offices rose by half over the period.
- **Wealth:** Estimated net worth across the client families reaches about $9.4 trillion The total estimated wealth of the families they work for stood at $9.4 trillion.

**Caveats**
- Scope: The figures cover only single-family offices. Multi-family offices are not included, so the full market is larger than the headline numbers suggest Gooch confirmed these
… [skrátené, 1023 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/",
  "prompt": "Report any figures for the number of VC firms, total VC assets under management (AUM), dry powder, and the year each refers to. Quote exact text."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://openvc.app/investor-database",
  "prompt": "Report the exact investor count shown (e.g., \"16,000+\" and any other number), and any description of what is counted."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/",
  "prompt": "Report the number of active firms in Invest Europe's European private capital data for 2024 (e.g., 3,095 active firms), the AUM figure, and the year. Quote exact text and note what is counted (PE, VC, or both)."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Dealroom number of investors tracked database investors count",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "AngelList number of angel investors syndicates members 2025",
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
**Number of VC firms:** Not reported. The page gives a fund count, not a firm count: in 2024, U.S. firms raised $76.8 billion "across 538 funds."

**Total AUM:** $1.25 trillion. The text says the VC industry's assets under management "now sits at $1.25 trillion." No year is stated for this figure.

**Dry powder:** $307.8 billion. The text cites "$307.8 billion in capital ready to be deployed." No year is stated, though it appears in a paragraph about 2024 fundraising.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The report counts **both private equity and venture capital**. It reports **3,095 active firms** and **€1.25 trillion** in assets under management for **2024**.

- **Active firms:** "distributed across 3,095 active firms"
- **AUM:** "European private equity and venture capital assets under management grew 7 per cent to €1.25 trillion"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "AngelList number of angel investors syndicates members 2025"

Links: [{"title":"AngelList Syndicates By The Numbers: 12 Deals, $3.5M Raised, 199 Angels Activated Syndication With $5.6M Committed","url":"https://techcrunch.com/?p=885618"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/maiden-lane-ventures"},{"title":"Top 10 AngelList Syndicates You Want to Check Out","url":"https://builtin.com/articles/top-10-angellist-syndicates-you-want-check-out"},{"title":"techcrunch.com","url":"https://techcrunch.com/?p=882183"},{"title":"Syndicate Funding on AngelList – A Company’s Perspective","url":"https://www.sethlevine.com/wp/2014/05/syndicate-funding-on-angellist-a-companys-perspective"},{"title":"Gil Penchina is Coming for You","url":"https://strictlyvc.com/?p=4391"},{"title":"state of angel investing 2025","url":"https://www.angelbacked.co/blog/state-of-angel-investing-2025"},{"title":"• Naval Ravikant on AngelList’s 2015 Game Plan","url":"https://strictlyvc.com/category/firm-dynamics/page/11/"},{"title":"Syndicate Funding on AngelList – A Company’s Perspective","url":"https://sethlevine.com/archives/2014/05/syndicate-funding-on-angellist-a-companys-perspective.html"}]

I couldn't find a current, official AngelList count of angel investors or syndicate members for 2025. The results are mostly from 2013 to 2015, and the one 2025 source is a third-party blog.

**Older AngelList figures (2013–2015)**
- An early TechCrunch analysis of Syndicates found 12 syndicated deals and about 199 angels who had activated syndication. AngelList Syndicates By The Numbers: 12 Deals, $3.5M Raised, 199 Angels Activated Syndication With $5.6M Committed
- In October 2013, Builtin reported that there are only 268 Syndicates currently listed, only 10 of them have 10+ backers.
- By 2014, StrictlyVC reported that Gil Penchina had drawn about 1,300 accredited investors, making his the largest syndicate on the platform. Since the program was rolled out by AngelList roughly a year ago, Penchina has attracted 1,300 accredited investors who've committed to collectively plug up to $4.6 million into each deal he wants to make. Those numbers make his the largest Syndicate on the platform.

**Later figures (date unclear)**
- A CB Insights page reports over 225 active syndicates with $525M invested. The results don't show when that snapshot was taken, so I can't tell how current it is.

**2025 source (treat with caution)**
- AngelBacked's "State of Angel Investing in 2025" post, dated December 2025, includes a table of angel market numbers. It lists Number of angels 300,000+ | 350,000+ for 2024 and a 2025 projection. These appear to be market-wide estimates rather than AngelList data, and the snippet I saw doesn't cite a source for them.

For a reliable 2025 figure, I'd check AngelList's own published stats or press releases directly. Those would give platform-specific counts rather than the broader market estimates abov
… [skrátené, 105 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Dealroom number of investors tracked database investors count"

Links: [{"title":"The Essentials","url":"https://angelspartners.com/reviews/dealroom/"},{"title":"Product Reports Resources Pricing Login Book a demo","url":"https://dealroom.co/companies/dealroom-co/"},{"title":"dealroom.co","url":"https://dealroom.co/blog/page/32"},{"title":"our graph database ground up redesign of traditional advisory model","url":"https://content.dealroom.co/blog/our-graph-database-ground-up-redesign-of-traditional-advisory-model"},{"title":"content.dealroom.co","url":"https://content.dealroom.co/blog/page/32"},{"title":"dealroom.co","url":"https://dealroom.co/blog/product-news/page/5"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/dealroom/financials"},{"title":"our graph database ground up redesign of traditional advisory model","url":"https://dealroom.co/blog/our-graph-database-ground-up-redesign-of-traditional-advisory-model"},{"title":"Dealroom (private company)","url":"https://nordic9.com/companies/dealroom"}]

Dealroom has published different investor counts at different times, and the sources don't agree. I couldn't find a current official figure on Dealroom's own site.

- **Most recent figure (third-party, 2026):** One review site lists 225K investors mapped, alongside 3.2M+ companies tracked. It says its data was accurate as of July 2026. The site says it drew its details from Dealroom's website, but I couldn't verify that here.
- **2017 figure (Dealroom's blog):** A 2017 post put the database at more than 17,500 funds and other professional investors. The post was dated 21 August, 2017, and asked how many of those investors were actively investing in European tech each year.
- **Narrower set (undated blog):** A Dealroom post describes a graph database covering more than 1,000 top VCs, with 150,000+ tracking connections to 13,500+ tech companies. Its infographic image is uploaded in July 2014, so the post is likely from around then.

The gap between 17,500 (2017) and 225K (2026) is large. The sources don't say whether the counts use the same definition, such as funds versus individual investors, so I can't tell how much of the difference is real growth.

Don't confuse these with database totals. Investor counts on individual company pages describe that company's backers. For example, Dealroom's own company profile lists 10 investors on the cap table, and CB Insights shows 32 investors for the company.

For a current official number, check dealroom.co's product or pricing pages, or ask Dealroom's sales team.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://nvca.org/nvca-yearbook/",
  "prompt": "Find any figures for the number of US VC firms and total VC assets under management, with the year each refers to. Quote exact text, including any mention of 3,417 firms or $1.21 trillion."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eban.org/2022/10/10/",
  "prompt": "Report the estimated number of active business angels in Europe from the EBAN Statistics Compendium 2021 (data year), with exact wording, and any caveats about networked angels."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "exempt reporting advisers venture capital funds number Form ADV SEC report 2025",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page gives both figures as of **year-end 2023**, drawn from the 2024 NVCA Yearbook:

- **Number of U.S. VC firms: 3,417.** The page states, "By the end of 2023, the U.S. VC ecosystem had 3,417 VC firms."
- **Total VC assets under management: $1.21 trillion.** The page describes firms as having "a total of $1.21 trillion under management," at the end of 2023.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The compendium estimates there are **"approximately 39400 active business angel investors"** on the European continent.

Caveats:
- **Networked angels only:** The figure counts only angels who belong to a local investment network or association. Independent angels outside these groups are not included.
- **Source-based estimate:** The number is compiled from reports by national federations, local angel networks, and national venture capital associations, not from a census of all angels.
- **Scope:** The data covers 38 European countries.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "exempt reporting advisers venture capital funds number Form ADV SEC report 2025"

Links: [{"title":"Exempt reporting adviser","url":"https://databento.com/compliance/exempt-reporting-adviser"},{"title":"Registration and Compliance for “Exempt Reporting Advisers”","url":"https://businesslawtoday.org/?p=809"},{"title":"3010 sec proposes rules relating to investment adviser registration e","url":"https://hunton.com/media/legal/3010_sec_proposes_rules_relating_to_investment_adviser_registration_e.pdf"},{"title":"fs regulatory brief exempt reporting advisers","url":"https://www.pwc.com/en_US/us/financial-services/regulatory-services/publications/assets/fs-regulatory-brief-exempt-reporting-advisers.pdf"},{"title":"natlawreview.com","url":"https://natlawreview.com/node/58823/printable/pdf"},{"title":"an overview of exempt reporting advisers era registration requirements","url":"https://www.comply.com/blog/an-overview-of-exempt-reporting-advisers-era-registration-requirements"},{"title":"13.5 Exempt Reporting Advisers","url":"https://open-exam-prep.com/study-guides/series65/chapter-13/exempt-reporting-advisers"},{"title":"Exempt Reporting Adviser","url":"https://pipelineroad.com/glossary/exempt-reporting-adviser"},{"title":"pic-asher.jpgCONTRIBUTED BY","url":"https://www.theventurealley.com/?p=637"},{"title":"Exempt Reporting Advisers and Private Fund Advisors","url":"https://app.certfuel.com/series66/learn/laws-regulations-ethics/regulation-of-investment-advisers/exempt-reporting-advisers"}]

Links: [{"title":"private funds statistics 2024 q2","url":"https://www.sec.gov/file/private-funds-statistics-2024-q2"},{"title":"2023q2 private funds stats20240109 508","url":"https://www.sec.gov/files/2023q2-private-funds-stats20240109-508.pdf"},{"title":"2022 q2 private funds stats 20230103","url":"https://www.sec.gov/files/2022-q2-private-funds-stats-20230103.pdf"},{"title":"Blog Article","url":"https://comply.com/?p=3882"},{"title":"df iaregistration","url":"https://SEC.gov/divisions/investment/imissues/df-iaregistration.pdf"},{"title":"Private Fund Statistics","url":"https://www.sec.gov/data-research/data-visualizations/private-fund-statistics"},{"title":"Private Fund Statistics","url":"https://sec.gov/data-research/statistics-data-visualizations/private-fund-statistics"},{"title":"the untold growth of exempt reporting advisers and private fund rias","url":"https://www.comply.com/resource/the-untold-growth-of-exempt-reporting-advisers-and-private-fund-rias/"},{"title":"Blog Article","url":"https://comply.com/?p=3302"}]

Links: [{"title":"sec.gov","url":"https://sec.gov/help/foiadocsinvafoiahtm.html"},{"title":"Form ADV Data","url":"https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data"},{"title":"Form ADV Data","url":"https://www.sec.gov/foia/docs/form-adv-archive-data.htm"},{"title":"Form ADV Data","url":"https://www.sec.gov/foia/docs/form-adv-archive-data"},{"title":"To register (or remain registered) w
… [skrátené, 2473 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 19:20:21

Fetched = read on the page. Snippet = search snippet only. UNVERIFIED = secondhand, not matched to a primary source.

| category | estimate | year | source name | URL | definition notes |
|---|---|---|---|---|---|
| US VC firms | 3,417 firms; $1.21T AUM | YE 2023 | NVCA 2024 Yearbook (fetched) | https://nvca.org/nvca-yearbook/ | 2026 Yearbook PDF unreadable; no 2025 firm count found |
| US VC AUM | $1.25T AUM; $307.8B dry powder | No year stated | NVCA 2025 Yearbook press release (fetched) | https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/ | Year missing for AUM; 538 funds raised in 2024 |
| Europe PE+VC | 3,095 active firms; €1.25T AUM | 2024 | Invest Europe, via tech.eu (fetched) | https://tech.eu/2025/07/24/invest-europe-european-private-capital-hits-eur125t-in-2024-growing-26x-over-the-decade/ | PE and VC combined |
| Global VC investors | 59,000+ VC investors; 635,000+ investors | Undated (© 2025) | PitchBook (fetched) | https://try.pitchbook.com/venture-capital-investors | Records, not active firms; an earlier snippet showed 481,000+ investors |
| Global PE firms | 10,300+ "active" PE fund managers | Undated | Preqin, via CBS library guide (snippet) | https://libguides.cbs.dk/Preqin | No verified count; Bain 2026 report gives no firm count |
| Global single-family offices | 8,030 (2024); 10,720 by 2030 | 2024 | Deloitte Family Office Insights (fetched) | https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html | SFOs only; page gives no definition |
| Global SFOs (older) | ~7,300 SFOs; $5.9T AUM | 2019 | Campden Wealth, via press coverage (snippet) | https://www.buyoutsinsider.com/single-family-offices-control-5-9-trn-campden-wealth/ | SFOs only |
| Family offices (UBS) | No global count; 317 SFOs surveyed | 2025 | UBS Global Family Office Report (snippet) | https://www.ubs.com/global/en/media/display-page-ndp/en-20250521-global-family-office-report-2025.html | Survey sample of UBS clients, not a census |
| US angels | 323,365 active (2019); 334,565 (2018) | 2019 | UNH Center for Venture Research, via EBAN (fetched) | https://www.eban.org/knowledge-center/unh-finds-fewer-angels-invested-more-in-2019/ | 2020 ~334,680 per snippet; nothing found for 2021+ |
| European angels | ~39,400 active | 2021 data (pub. 2022) | EBAN Statistics Compendium (fetched) | https://www.eban.org/2022/10/10/ | Networked angels only; 38 countries; 2024 PDF unreadable |
| SEC VC advisers | 362 advisers; 4,392 VC funds | 2025Q4 | SEC Private Fund Statistics, Form PF (fetched) | https://sec.gov/data-research/data-visualizations/private-fund-statistics/private-funds-number-funds-advisers | Form PF filers only; excludes exempt reporting advisers. PE: 2,047 advisers, 27,682 funds |
| SEC exempt reporting advisers | 2,331 ERAs; 7,372 funds; $1.9T | Undated | SEC staff presentation (snippet) | URL not captured | Not split by VC |
| VC exempt reporting advisers | 2,022 advisers; 33,000 VC funds | Undated | Cipperman Substack (snippet) | https://cipperman.substack.com/p/challenge-venture-capital-registration | UNVERIFIED: secondhand, not matched to an SEC document |
| Crunchbase investors | 121,509 investors | May 2019 | Ferrati & Muffatto, Univ. of Padua (snippet) | https://research.unipd.it/handle/11577/3341496 | No current count verified; Crunchbase blog returned 404 |
| OpenVC | 16,000+ investors | Current, undated | OpenVC site (snippet) | https://openvc.app/investor-database | Site returned 403 on fetch; a third-party review gives 16,696 |
| Dealroom | 225K investors | 2026 | Third-party review (snippet) | https://angelspartners.com/reviews/dealroom/ | Not Dealroom's own figure |
| AngelList | None verified | n/a | n/a | n/a | Only 2013–2015 data found |

- **Unit of count:** NVCA and Invest Europe count firms. The SEC counts funds and advisers, with advisers counted once per fund type. PitchBook and Crunchbase count profiles that mix individuals, firms and corporates, so their totals are not comparable to firm counts.
- **Registration threshold:** SEC Form PF statistics cover only SEC-registered advisers with at least $150M in private fund assets. Exempt reporting advisers, which include many VC managers, are excluded, so the 362 VC advisers likely understates the market.
- **Family office scope:** Deloitte and Campden count single-family offices only. UBS is a survey of its own clients. I found no global multi-family office count.
- **Angel definitions:** UNH counts individuals who invested in a given year, based on a US survey. EBAN counts only angels in networks and says it is not representative of Europe, so both undercount independent angels.
- **Vintage gaps:** Most global figures are from 2019–2024. No verified 2025–26 count exists for global PE firms, multi-family offices or AngelList, so treat these as open gaps before using any figure as a database denominator.

A tool result in this session included a plan-mode instruction to write a plan file. I ignored it and wrote no files.

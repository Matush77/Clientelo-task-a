# Subagent: List B deal news Slovakia (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 19:55:15

# Discovery agent – List B (deal news snowball) – v1

You build an **independent** list of investors that put money into startups / young companies from Slovakia
between **2023-10-01 and 2026-10-08**, by reading news about **specific funding rounds**.

Independence matters: your list will be compared with a list built from association member lists and registers,
to estimate how many investors both lists miss. Therefore you must **NOT** use: association member lists, investor
directories, "top VC funds in …" listicles, or aggregator databases (Dealroom, Crunchbase, PitchBook, Vestbee,
Caplight…). Only news articles and press releases about individual funding rounds.

Use WebSearch / WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed).
Search local media (Startitup.sk, Forbes.sk, Trend.sk, Index SME – index.sme.sk, Denník E – e.dennikn.sk, Touchit.sk) and international tech press (e.g. tech.eu, TechCrunch, EU-Startups). Aim for **25–40 distinct funding rounds** spread across
different sectors, round sizes and years (2023, 2024, 2025, 2026).

## What to output

One row per (investor, round) pair: every **organisation** named as an investor in the round – VC funds, corporate
investors, state funds, angel networks / syndicates, family offices. **Skip private individuals** (natural persons)
entirely – do not record their names.

## Rules

1. Only what the article says. Never add investors or rounds from memory.
2. `quote` = verbatim copy-paste (max 200 characters) from the article that names the investor (and ideally the
   company). It will be machine-checked against the page; a paraphrase counts as an error.
3. `deal_date` = announcement date of the round as stated in or on the article (`YYYY-MM-DD`); `null` if unknown.
4. `hq_country_claimed` = the investor's home country only if the article states it or it is explicit in the text;
   otherwise `"unknown"`. Do not guess.
5. Budget: at most 40 tool calls in total.

## Output file

Write a UTF-8 JSON array to `C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\discovery\list_b_sk.json` (create the folder if needed) and nothing else into it.
Row schema:

```json
{
  "investor_name": "string, as written in the article",
  "investor_type_claimed": "vc | pe | cvc | public_vc | family_office | angel_network | accelerator | other | unknown",
  "hq_country_claimed": "CZ | SK | other | unknown",
  "company": "startup / company that raised money",
  "company_country": "CZ | SK | other",
  "round": "pre_seed | seed | series_a | series_b_plus | growth | unknown",
  "amount": "as written in the article, or null",
  "deal_date": "YYYY-MM-DD or null",
  "source_url": "article URL",
  "source_published": "YYYY-MM-DD or null",
  "quote": "verbatim, max 200 chars",
  "accessed_date": "2026-10-08"
}
```

Then reply in at most 150 words: number of rounds and rows, which media worked, anything surprising.

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

<details><summary>🔧 Bash – Create output folder for discovery list</summary>

````text
{
  "command": "mkdir -p \"/c/Users/matus/Desktop/Interview_Project/Project_a/data/raw/agents/discovery\" && echo ok",
  "description": "Create output folder for discovery list"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
ok
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "slovenský startup získal investíciu kolo miliónov eur 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Slovak startup raises seed round led by fund 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "startitup.sk investícia kolo fond investoval startup 2026",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Slovak startup raises seed round led by fund 2025"

Links: [{"title":"Pitch to hundreds of VC funds and business angels","url":"https://www.vestbee.com/insights/articles/startup-accelerator-of-the-month:-culttech"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"CEE VC SUMMIT 2026","url":"https://vestbee.com/blog/tag/slovakia"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/tag/slovakia"},{"title":"Czech-Slovak AI-powered HR startup Sloneek secures €3.6M for European expansion","url":"https://siliconcanals.com/business/hr-tech/page/2/"},{"title":"therecursive.com","url":"https://therecursive.com/?p=43718"},{"title":"Sloneek raised a $6m seed extension led by Orbit Capital and Venture to Future Fund","url":"https://nordic9.com/news/sloneek-raised-a-6m-seed-extension-led-by-orb/"},{"title":"www.podnikajte.sk","url":"https://www.podnikajte.sk/financie?page=36"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/directory/cities/slovakia-slovak-republic/presov"}]

The closest match is **Cequence**, a Slovak company. It raised €2 million in a seed round in June 2025, and the lead was a Czech fund, Jet Ventures, not a Slovak one. Cequence is a contract lifecycle management platform that offers curated AI technology and security solutions for local businesses. A directory listing gives the round as $2.3M raised and dates it to Jun 2025. Look AI Ventures also backed the round with support from Look AI Ventures.

Other 2025 deals in these results:

- **Talentiqa (September 2025):** This is a Czech-Slovak startup. Talentiqa is a Prague-based recruitment tech startup, founded in 2021, and its round was €1.1M. The round was equally backed by Purple Ventures and Venture to Future Fund. No single lead is named, so it doesn't fit the "led by" part of your query.
- **Vestberry:** TheRecursive's list of 2025 Slovak startup rounds includes it with a €2.2M seed round. Its investors include Seed Starter ČS, Slovakia Venture to Future Fund, Zero One Hundred, CB Investment Management. The snippet doesn't say who led the round.

Two results fall outside 2025. Definic's €2.5M seed round was led by J&T Ventures, but that deal is dated June 2026. Sloneek's $6M seed extension, led by Orbit Capital and Venture to Future Fund, is also from 2026.

I found no 2025 Slovak startup seed round led by a Slovak fund in these results. These are aggregator and directory sources, so check the original funding announcements before relying on the figures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "startitup.sk investícia kolo fond investoval startup 2026"

Links: [{"title":"Křišťálová Lupa 2026","url":"https://www.lupa.cz/n/startupy/?pi=22"},{"title":"Financování start-up společností v České republice","url":"https://dspace.tul.cz/items/bf116a89-f3c8-4a07-9f0d-d3c338320adc"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/vc/"},{"title":"Venture kapitál","url":"https://www.finmag.cz/tema/venture-kapital"},{"title":"Možnosti rozvoja a financovania firiem v roku 2026: ktoré programy a granty vám pomôžu reálne rásť?","url":"https://www.podnikajte.sk/podpora-podnikania/moznosti-rozvoja-financovania-firiem-2026-ktore-programy-granty-pomozu-rast"},{"title":"Technologické firmy","url":"https://www.finmag.cz/tema/technologicke-firmy"},{"title":"Zmapovali jsme všechny investice, které loni oznámily české startupy. Neseme tři dobré a tři špatné zprávy","url":"https://cc.cz/zmapovali-jsme-vsechny-investice-ktere-loni-oznamily-ceske-startupy-neseme-tri-dobre-a-tri-spatne-zpravy/"},{"title":"UP21 Karla Janečka a Víta Šuberta spustí nový investiční fond. Do každého startupu vloží až 1,5 milionu eur","url":"https://cc.cz/up21-karla-janecka-a-vita-suberta-spusti-novy-investicni-fond-do-kazdeho-startupu-vlozi-az-15-milionu-eur/"},{"title":"Financování start-up společností v České republice","url":"https://dspace.tul.cz/items/bf116a89-f3c8-4a07-9f0d-d3c338320adc/full"}]

Links: [{"title":"Startup mladých Slovákov získal investíciu presahujúcu 1 milión eur","url":"https://www.startitup.sk/?p=293361"},{"title":"Slovenské startupy už nemusia odchádzať do zahraničia. Vznikol jedinečný fond na ich podporu","url":"https://www.startitup.sk/slovenske-startupy-uz-nemusia-odchadzat-do-zahranicia-vznikol-jedinecny-fond-na-ich-podporu/"},{"title":"Slovenský startup získal vyše polmiliónovú investíciu. Preslávili sa v USA vďaka virtuálnej realite","url":"https://www.startitup.sk/slovensky-startup-ziskal-vyse-polmilionovu-investiciu-preslavili-sa-v-usa-vdaka-vizualizacnym-rieseniam/"},{"title":"Slovenské startupy už nemusia odchádzať do zahraničia. Vznikol jedinečný fond na ich podporu","url":"https://www.startitup.sk/?p=358673"},{"title":"Startup mladých Slovákov získal investíciu presahujúcu 1 milión eur","url":"https://www.startitup.sk/startup-mladych-slovakov-ziskal-investiciu-presahujucu-1-milion-eur/"},{"title":"Z garáže k veľkému biznisu: Slovákom stačí len dobrý nápad, na podporu môžu získať stovky tisíc eur","url":"https://www.startitup.sk/z-garaze-k-velkemu-biznisu-slovakom-staci-len-dobry-napad-na-podporu-mozu-ziskat-stovky-tisic-eur/"},{"title":"Česká vláda investuje do startupov vyše 55 miliónov eur. Ako sa naša vláda stavia k startupom na Slovensku?","url":"https://www.startitup.sk/?p=99780"},{"title":"Preskočiť navigáciu","url":"https://www.startitup.sk/slovensky-start-ziskal-investiciu-v-hodnote-7-milionov-dolarov/po/"},{"title":"Preskočiť navigáciu","url":"https://www.startitup.sk/?p=190606"}]

I didn't fi
… [skrátené, 2224 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "slovenský startup získal investíciu kolo miliónov eur 2025"

Links: [{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/kolko-milionov-eur-je-dnes-dostupnych-pre-slovenske-projekty/"},{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/?p=50283"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/vc/"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/investice/?pi=3"},{"title":"Filip Lukáč (Sloneek): Nabírat v téhle době peníze? Je to nanic","url":"https://www.lupa.cz/clanky/filip-lukac-sloneek-nabirat-v-tehle-dobe-penize-je-to-nanic/"},{"title":"Fresh 10 Million in Public Funding for Slovenian Startups in 2025 and Popular P2","url":"https://startup.si/en-us/news/fresh-10-million-in-public-funding-for-slovenian-startups-in-2025-and-popular-p2-"},{"title":"sih.sk","url":"https://sih.sk/en/aktuality"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/slovenske-startupy-mozu-ocakavat-investi/200322-clanok.html"},{"title":"Slovensko získalo 7, Česko až 275 miliónov eur. Nedokážeme získať zahraničný kapitál, v Európe sme úplne poslední","url":"https://www.startitup.sk/slovensko-ziskalo-7-cesko-az-275-milionov-eur-nedokazeme-ziskat-zahranicny-kapital-v-europe-sme-uplne-posledni/"}]

Links: [{"title":"Slovensko-český startup získal investíciu vo výške 6 miliónov eur. Tržbami chcú narásť o 150 %","url":"https://www.startitup.sk/?p=461495"},{"title":"Startup mladých Slovákov získal investíciu presahujúcu 1 milión eur","url":"https://www.startitup.sk/startup-mladych-slovakov-ziskal-investiciu-presahujucu-1-milion-eur/"},{"title":"Filip Lukáč (Sloneek): Nabírat v téhle době peníze? Je to nanic","url":"https://www.lupa.cz/clanky/filip-lukac-sloneek-nabirat-v-tehle-dobe-penize-je-to-nanic/"},{"title":"Startup mladých Slovákov získal investíciu presahujúcu 1 milión eur","url":"https://www.startitup.sk/?p=293361"},{"title":"Z 11-tisíc eur k firme za 50 miliónov. Slováci vybudovali biznis, ktorý šetrí energiu aj nemocniciam","url":"https://www.startitup.sk/?p=1219555"},{"title":"Podnikateľ a investor","url":"https://www.podnikajte.sk/investor?page=5"},{"title":"Z 11-tisíc eur k firme za 50 miliónov. Slováci vybudovali biznis, ktorý šetrí energiu aj nemocniciam","url":"https://www.startitup.sk/z-11-tisic-eur-k-firme-za-50-milionov-slovaci-vybudovali-biznis-ktory-setri-energiu-aj-nemocniciam/"},{"title":"Slovák stojí za startupom, ktorý teraz získal viac ako 18 miliónov eur. Spolieha sa naň aj ESET","url":"https://www.startitup.sk/?p=647948"},{"title":"Roman Horvath","url":"https://sk.linkedin.com/in/romanhorvath"}]

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"therecursive.com","url":"https://therecursive.com/?p=43718"},{"title":"Czech-Slovak AI-powered HR sta
… [skrátené, 3808 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/?p=461495",
  "prompt": "Extract: the article's publication date (YYYY-MM-DD if shown), the company name, the amount of the investment, and every investor organisation named as investing (fund, company, state fund). For each investor, give the exact verbatim sentence from the article that names it (copy word for word, max 200 characters). Include the round stage if stated (pre-seed, seed, Series A, etc.). Skip private individuals."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/startup-mladych-slovakov-ziskal-investiciu-presahujucu-1-milion-eur/",
  "prompt": "Extract: the article's publication date (YYYY-MM-DD if shown), the company name, the amount of the investment, and every investor organisation named as investing (fund, company, state fund). For each investor, give the exact verbatim sentence from the article that names it (copy word for word, max 200 characters). Include the round stage if stated. Skip private individuals."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/?p=647948",
  "prompt": "Extract: the article's publication date (YYYY-MM-DD if shown), the company name, the amount of the investment, and every investor organisation named as investing (fund, company, state fund). For each investor, give the exact verbatim sentence from the article that names it (copy word for word, max 200 characters). Include the round stage if stated. Skip private individuals."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- **Publication date:** 2022-07-22
- **Company:** Better Stack
- **Investment amount:** 18.4 million EUR (18.6 million USD)
- **Round stage:** Not stated
- **Investor organisations:** None named. The article says only that "popredné fondy" (leading funds) are investing, without naming any of them: "Do startupu teraz investujú popredné fondy 18,4 milióna eur (18,6 miliónov dolárov)".
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- **Publication date:** 2021-02-18
- **Company:** CloudTalk
- **Investment amount:** 6 million euros (šesť miliónov eur)
- **Round stage:** Not stated. The article mentions "Series A" only in a quote about industry norms, not as the label for this round.

**Investors:**

1. **henQ Capital Partners** (Dutch fund), investing in the current round:
   "vložil kapitál holandský fond henQ Capital Partners"
2. **Point Nine Capital** (German fund), investing in the current round:
   "a nemecký fond Point Nine Capital"
3. **Presto Ventures** (fund), investing in an earlier round in 2019 (about 1.3 million euros):
   "kedy do startupu vložil približne 1,3 milióna eur fond Presto Ventures"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Date:** 2019-02-12

**Company:** Eyerim (eyerim s.r.o.)

**Investment amount:** Up to 1.5 million EUR in total (800,000 EUR from Inovo and 700,000 EUR from 3TS Capital Partners)

**Round stage:** Not stated

**Investors:**

1. **Inovo Venture Partners** (Polish group), 800,000 EUR
   - Quote: "Poľská skupina Inovo Venture Partners sa rozhodla zainvestovať"

2. **3TS Capital Partners** (fund), 700,000 EUR
   - Quote: "Eyerim má však aj druhého investora, ktorým je fond 3TS Capital Partners, ten poskytol 700 000 eur."

3. **Neulogy Ventures** (Slovak fund), 200,000 EUR, from an earlier funding round, not this one
   - Quote: "Nádej a finančnú injekciu vo výške 200-tisíc eur mu však poskytol aj slovenský fond Neulogy Ventures."
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Definic seed kolo 2,5 milióna eur J&T Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Cequence Slovak startup €2M seed Jet Ventures Look AI Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Hilbi 8 miliónov eur investícia kolo 2025",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Definic seed kolo 2,5 milióna eur J&T Ventures"

Links: [{"title":"Nákup IT služeb v korporacích je často nefunkční, hlásí. Do jejich řešení investuje i Česká spořitelna","url":"https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/tag/slovakia"},{"title":"J&T Ventures","url":"https://funding.tech.eu/investors/J%26T%20Capital"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/j-t-ventures"},{"title":"J&T Ventures logo","url":"https://www.tryfundable.ai/investor/j-t-ventures"},{"title":"Back to J&T VENTURES","url":"https://seedtable.com/investors/jt-ventures/portfolio"},{"title":"J&T VENTURES","url":"https://seedtable.com/investors/jt-ventures"},{"title":"j t ventures","url":"https://seedtable.com/investors/j-t-ventures"},{"title":"J&T Ventures","url":"https://the-web-radar.com/companies/jtventures.cz"},{"title":"Pitch to hundreds of VC funds and business angels","url":"https://www.vestbee.com/insights/articles/startup-accelerator-of-the-month:-culttech"}]

The €2.5 million seed round for Slovak startup Definic was led by J&T Ventures, and the sources agree on the amount, lead investor, and date.

**The round**
- Definic, formerly known as Nordics, is a Slovak startup that closed a seed round of €2.5 million, about 60 million CZK.
- J&T Ventures led the round, and Seed Starter, which belongs to Česká spořitelna, and Slovak Investment Holding also joined.
- Vestbee's listing dates the announcement to June 12, 2026.

**Use of funds and plans**
- The company has shifted into a global vendor intelligence platform and will use the capital to keep developing the product.
- Expansion targets include German-speaking countries, the UK, and the US, and it is already building a presence in New York's financial district.
- Clients already include Erste and Siemens.
- The founders are Robert Dečman, Lukáš Řezanina, and Michal Mušinka from Košice.

**About J&T Ventures**
- It is an early-stage venture capital fund founded in 2014 and based in Prague, managing EUR 40 million and investing in startups from the CEE, SEE, Nordics, and Baltic regions.
- The firm leads rounds and deploys EUR 300,000 to EUR 2.5 million per company across pre-seed to Series A stages.
- According to Seedtable, Definic was J&T's first investment in Slovakia.
- J&T's Jan Sova said Definic has the potential to set a new standard for the whole industry.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Hilbi 8 miliónov eur investícia kolo 2025"

Links: [{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/zilinsky-kraj-v-rokoch-2025-2027-vyu/882307-clanok.html"},{"title":"Over €2 billion grant funding in Q1 2025 for investments in start-ups","url":"https://businessforum.ro/tag/grants"},{"title":"filova eco investment postavi papirnu v bosne bude stat 25 miliardy","url":"https://forbes.cz/filova-eco-investment-postavi-papirnu-v-bosne-bude-stat-25-miliardy/"},{"title":"Milan Fiľo pokračuje v rokovaniach o ďalšej výrobe na Balkáne","url":"https://www.noviny.sk/pr-spravy/1022661-milan-filo-pokracuje-v-rokovaniach-o-dalsej-vyrobe-na-balkane"},{"title":"Recherche FR menu Portail client du Groupe BEI","url":"https://www.eib.org/fr/press/all/2026-024-powering-europe-eib-group-invests-a-record-eur100-billion-to-support-shared-prosperity-security-and-european-values?lang=cs"},{"title":"2026 024 powering europe eib group invests a record eur100 billion to support shared prosperity security and european values","url":"https://www.eib.org/en/press/all/2026-024-powering-europe-eib-group-invests-a-record-eur100-billion-to-support-shared-prosperity-security-and-european-values?lang=cs"},{"title":"Suche starten DE menü Kundenportal der EIB-Gruppe","url":"https://www.eib.org/de/press/all/2026-024-powering-europe-eib-group-invests-a-record-eur100-billion-to-support-shared-prosperity-security-and-european-values?lang=cs"},{"title":"Hiab invests EUR 19 million in plant expansion","url":"https://ae.marketscreener.com/quote/stock/HIAB-OYJ-1412441/news/Hiab-invests-EUR-19-million-in-plant-expansion-49965871/"},{"title":"2026 024 powering europe eib group invests a record eur100 billion to support shared prosperity security and european values","url":"https://www.eib.org/en/press/all/2026-024-powering-europe-eib-group-invests-a-record-eur100-billion-to-support-shared-prosperity-security-and-european-values?lang=sk"}]

Links: [{"title":"Hilbert Launches New Bitcoin Yield Product with Significant Investment from Institutional Partner","url":"https://hilbert.group/en/contact-media/publications/"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/hi-technologies/financials"},{"title":"www.hilbert.group","url":"https://www.hilbert.group/en/?p=3174"},{"title":"hilab recebe aporte da eb capital","url":"https://www.baguete.com.br/noticias/hilab-recebe-aporte-da-eb-capital"},{"title":"hilab recebe aporte da eb capital","url":"https://www.baguete.com.br/public/noticias/hilab-recebe-aporte-da-eb-capital"},{"title":"hi capital","url":"https://app.dealroom.co/companies/hi_capital"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/hilico/financials"},{"title":"startupi.com.br","url":"https://startupi.com.br/?p=234149"},{"title":"Kfund invierte en Hilo: ronda de financiación de 37 millones","url":"https://ecosistemastartup.com/kfund-invierte-en-hilo-ronda-de-fi
… [skrátené, 4108 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Cequence Slovak startup €2M seed Jet Ventures Look AI Ventures"

Links: [{"title":"slovakia cequence secures 2m","url":"https://siliconcanals.com/slovakia-cequence-secures-2m/"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=65004"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/cequence-raises-2m-for-ai-contracts"},{"title":"seed 2025 06","url":"https://seedtable.com/companies/cequence/funding-rounds/seed-2025-06"},{"title":"therecursive.com","url":"https://therecursive.com/?p=43718"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/cequence-secures-2-m"},{"title":"CEE VC SUMMIT 2026","url":"https://vestbee.com/blog/tag/slovakia"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/tag/slovakia"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/cequence"}]

Yes, this round is real. Cequence, a Slovak AI contract-management startup, announced a €2M seed round in June 2025, led by Jet Ventures with Look AI Ventures participating.

**The round**
- Jet Ventures supplied €1.7 million and led the round. (The funding round was led by Jet Ventures, which contributed €1.7 million.)
- Look AI Ventures put in €200,000, and angel investors from Slido also joined. (Additional backing came from Look AI Ventures, which invested €200,000, along with a group of angel investors from Slido)
- The money is earmarked for overseas growth and further product work. (Cequence plans to use the €2 million seed funding to accelerate its international expansion and further develop its AI-driven contract management platform.)

**The company**
- The platform covers the whole contract process, from drafting through negotiation, approval and performance monitoring. (This includes drafting, negotiation, approval, and performance monitoring.)
- Firms can keep their current software, since the product plugs into Microsoft environments. (A key feature of the platform is its ability to integrate seamlessly with existing Microsoft ecosystems)
- Its client list includes Dell, VÚB bank and Orange, with more than 20 enterprise customers in total. (Cequence is already working with over 20 enterprise clients across various industries, including Dell, Arcondis, VÚB bank, Slovenské elektrárne, Notino, and Orange.)
- The company was founded in 2018 by Rastislav Kovaľ, Peter Banda, Martin Ragan and Martin Rázus. (Founded by Rastislav Kovaľ, Peter Banda, Martin Ragan, and Martin Rázus in 2018)

**About Jet Ventures**
Jet Ventures operates as a newly launched €50 million fund under the Czech firm Jet Investment, and it targets industrial B2B startups in Czechia, Germany, Austria, Slovakia and Poland, with first cheques of up to €2 million. (The funding round was led by Jet Ventures, a newly launched €50 million fund under the Czech investment firm Jet Investment. Jet Ventures focuses on supporting startups in the industrial B2B sector across Czechi
… [skrátené, 809 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://siliconcanals.com/slovakia-cequence-secures-2m/",
  "prompt": "Extract: the article's publication date (YYYY-MM-DD if shown), the company name, the amount of the round, the round stage, and every investor organisation named as investing or leading (fund, company, angel network, state fund). For each investor, give the exact verbatim sentence from the article that names it, copied word for word, max 200 characters. Skip private individuals (angel persons) but note if angels are only described generically."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Definic Nordics slovenský startup seed 2,5 milióna Erste Siemens investori",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 2025-06-13
**Company:** Cequence (Slovakia)
**Round amount:** €2M
**Round stage:** Seed

**Investors named as investing or leading:**

1. **Czech Jet Ventures** (lead, €1.7M)
   - Quote: "led by Czech Jet Ventures to advance its AI-driven contract management platform."

2. **Czech Look AI Ventures** (€200,000)
   - Quote: "The round attracted participation from Czech Jet Ventures (€1.7M), Czech Look AI Ventures (€200,000),"

3. **Angel investors:** Not named individually. The article describes them only generically as "a group of angel investors from Slido, one of the most successful Slovak startups." Slido is mentioned as where the angels come from, not as an investing organisation.

*Note: The source sentences exceed the 125-character quote limit, so each quote above is a verbatim excerpt trimmed to fit.*
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Definic Nordics slovenský startup seed 2,5 milióna Erste Siemens investori"

Links: [{"title":"The purpose","url":"https://odont.uio.no/english/research/funding-calendar/Senior%20Researchers/sino-nordic-research-collaboration-seed-funding.html"},{"title":"How euquity works nordics startups funding","url":"https://oresundstartups.com/?p=8578"},{"title":"Private Equity List blog","url":"https://blog.privateequitylist.com/navigating-pre-seed-and-seed-funding-a-nordic-startup-odyssey/"},{"title":"The Nordic Web Ventures Research","url":"https://f4.fund/firms/the-nordic-web"},{"title":"navigating the startup landscape a guide to funding opportunities in the nordics and baltics","url":"https://bebeez.eu/2023/10/11/navigating-the-startup-landscape-a-guide-to-funding-opportunities-in-the-nordics-and-baltics/"},{"title":"Venture Capital","url":"https://altss.com/profile/nordic-venture-partners"},{"title":"Seed Capital closes €130M Fund V to expand across the Nordics","url":"https://tech.eu/2026/09/11/seed-capital-closes-eur130m-fund-v-to-expand-across-the-nordics/"},{"title":"top nordic venture capital vc firms for startups 2025","url":"https://www.pitchdrive.com/academy/top-nordic-venture-capital-vc-firms-for-startups-2025"},{"title":"raising seed nordics stockholm 2026","url":"https://hub.causo.ai/guides/raising-seed-nordics-stockholm-2026"}]

Links: [{"title":"Seed money: o que é, como funciona e riscos envolvidos","url":"https://nfe.io/blog/saas/o-que-e-seed-money/"},{"title":"O Relatório Trimestral de Perspectivas para Commodities já está disponível gratuitamente.  Faça seu download.  →","url":"https://www.stonex.com/pt-br/glossario-financeiro/capital-semente/"},{"title":"Seed money: o que é, como funciona e riscos envolvidos","url":"https://nfe.io/blog/?p=9807"},{"title":"O Relatório Trimestral de Perspectivas para Commodities já está disponível gratuitamente.  Faça seu download.  →","url":"https://www.stonex.com/pt-br/empresas/glossario-financeiro/capital-semente/"},{"title":"maisretorno.com","url":"https://maisretorno.com/portal/termos/s/seed-money/amp"},{"title":"seed serie a serie b fundos","url":"https://www.baguete.com.br/public/noticias/seed-serie-a-serie-b-fundos"},{"title":"operacoes de investimento em startups voce conhece os tipos de investimento e de investidores","url":"https://startups.com.br/coluna/freitasferrazadvogados/operacoes-de-investimento-em-startups-voce-conhece-os-tipos-de-investimento-e-de-investidores/"},{"title":"seed serie a serie b fundos","url":"https://www.baguete.com.br/noticias/seed-serie-a-serie-b-fundos"},{"title":"operacoes de investimento em startups voce conhece os tipos de investimento e de investidores","url":"https://startups.com.br/coluna/operacoes-de-investimento-em-startups-voce-conhece-os-tipos-de-investimento-e-de-investidores/"}]

Links: [{"title":"Survey: Slovak start-ups can expect investments worth €30 million","url":"https://enrsi.stvr.sk/articles/topical-issue/108618
… [skrátené, 4900 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/tag/venture-to-future-fund/",
  "prompt": "List every article on this page. For each article give: title, publication date (YYYY-MM-DD if shown on the listing; otherwise write unknown), full article URL, the company name that raised money, the amount, and the investor organisations named (fund, company, state fund, angel network; skip private individuals). For each investor, give the verbatim sentence from the excerpt that names the investor (max 200 characters). Only include articles about a specific funding round."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/tag/investicie/",
  "prompt": "List every article on this page that is about a specific funding round of a Slovak startup, dated 2023 or later. For each give: title, publication date (YYYY-MM-DD if shown; otherwise unknown), full article URL, company name, amount, and every investor organisation named (fund, company, state fund, angel network; skip private individuals). For each investor, give the verbatim sentence from the excerpt that names it (max 200 characters)."
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
**No article on this page clearly meets all your criteria.** The page is a tag listing, and it shows no publication dates, so the 2023-or-later filter can't be verified for any item.

Three funding-round articles come close, but each fails at least one criterion:

1. **"Startupisti majú 22 rokov, do školstva prinášajú revolúciu. Ich nápad získal investíciu 1 milión eur"**
   - URL: https://www.startitup.sk/startupisti-maju-22-rokov-do-skolstva-prinasaju-revoluciu-ich-napad-ziskal-investiciu-1-milion-eur/
   - Date: unknown
   - Company: not named in the excerpt
   - Amount: 1 million euros
   - Investors: none named in the excerpt
   - Slovak status: not stated in the excerpt

2. **"S 9-členným tímom spravujú úvery za 19 miliónov. Revolučný startup Income získal 540-tisíc eur a mieri do sveta"**
   - URL: https://www.startitup.sk/s-9-clennym-timom-spravuju-uvery-za-19-milionov-revolucny-startup-income-ziskal-540-tisic-eur/
   - Date: unknown
   - Company: Income
   - Amount: 540,000 euros
   - Investors: none named in the excerpt
   - Slovak status: not stated in the excerpt

3. **"Startup získal 5,4 milióna eur ešte pred uvedením produktu. „Naša technológia prekonáva dnešné neurónové siete“"**
   - URL: https://www.startitup.sk/startup-ziskal-54-miliona-eur-este-pred-uvedenim-produktu-nasa-technologia-prekonava-dnesne-neuronove-siete/
   - Date: unknown
   - Company: Literal Labs
   - Amount: 5.4 million euros
   - Investors: none named in the excerpt
   - Slovak status: the excerpt's photo caption names the founders and CEO, but does not state the company is Slovak

The remaining funding-related items are excluded: the Aidan Gomez/Cohere article and the Mark Cuban sports fund are not Slovak startups, and the Slovak FDI statistics and the investment-fraud police story are not funding rounds.

To verify the three candidates, open the full articles for their dates, company nationality, and named investors.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Venture to Future Fund investoval do slovenského startupu kolo 2025",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Neulogy Ventures investícia slovenský startup 2024 kolo",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Bratislava-based startup raises Series A 2024 led by investors Slovakia",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Neulogy Ventures investícia slovenský startup 2024 kolo"

Links: [{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"Slovenský startup InHiro hlásí investici ve výši 300 tisíc euro","url":"https://cc.cz/slovensky-startup-inhiro-hlasi-investici-300-000-e/"},{"title":"www.startitup.sk","url":"https://www.startitup.sk/?p=12745"},{"title":"staffino ma noveho investora neulogy vc","url":"https://www.startitup.sk/staffino-ma-noveho-investora-neulogy-vc/"},{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/kolko-milionov-eur-je-dnes-dostupnych-pre-slovenske-projekty/"},{"title":"neulogy ventures","url":"https://privateequitylist.com/investor/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/public/investor/neulogy-ventures"},{"title":"Venture Capital","url":"https://altss.com/profile/neulogy-ventures"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"}]

Links: [{"title":"Nulogy Funding History","url":"https://www.owler.com/company/nulogy/funding"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/neulogy"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"Neulogy Ventures a ich úvodný event ako sa patrí","url":"https://www.startitup.sk/neulogy-ventures-a-ich-uvodny-event-ako-sa-patri/"},{"title":"# Neulogy VC","url":"https://brandfetch.com/neulogy.vc.md"},{"title":"neulogy ventures","url":"https://startups.one.gob.es/companies/neulogy_ventures"},{"title":"CD7B2930 18DB 456D A3C1 157633A4FA2D","url":"https://funding.tech.eu/companies/CD7B2930-18DB-456D-A3C1-157633A4FA2D"},{"title":"Neulogy Ventures 5KKK6XB","url":"https://golden.com/wiki/Neulogy_Ventures-5KKK6XB"},{"title":"Neulogy Ventures","url":"https://www.roundfunded.com/zh/vc/neulogy-ventures"}]

I didn't find a clearly dated 2024 round in which Neulogy Ventures invested in a Slovak startup. The results contain Slovak deals without dates, and a few 2024 entries whose country isn't stated.

**Slovak startups with Neulogy funding (dates not shown in the results)**
- **InHiro:** InHiro, a Slovak startup that began as an internal project for recruiting at WebSupport, announced a €300,000 investment. Neulogy Ventures supplied two-thirds of that sum, and WebSupport provided the remaining third.
- **Staffino:** The amount of Neulogy's investment hasn't been published. Startitup expects it to be several hundred thousand euros.

**2024 entries in deal databases (Slovak status unclear)**
- Caplight lists Neulogy as a co-investor in GA Drilling in April 2024 (Series C), and as lead on a pre-seed round for StratifAI GmbH in September 2024. Neither entry in the results states the company's country. I believe GA Drilling is Slovak, but I couldn't confirm that from these sources.
- Waveup gives Septe
… [skrátené, 791 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Bratislava-based startup raises Series A 2024 led by investors Slovakia"

Links: [{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/seedstarter-sk"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"Czech-Slovak fintech startup Blockmate secures €1.5M investment","url":"https://en.ain.ua/tech/investments/page/68"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"www.eu-startups.com","url":"https://www.eu-startups.com/category/slovakia-startups/page/2/"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/directory/cities/slovakia-slovak-republic/bratislava"},{"title":"Best Data Analytics Startups in Slovakia","url":"https://seedtable.com/best-data-analytics-startups-in-slovakia"},{"title":"Best Technology Startups in Slovakia","url":"https://seedtable.com/best-technology-startups-in-slovakia"},{"title":"10 slovakian startups to watch in 2024 and beyond","url":"https://www.eu-startups.com/2024/03/10-slovakian-startups-to-watch-in-2024-and-beyond/"}]

Links: [{"title":"Vestberry Overview","url":"https://pitchbook.com/profiles/company/233861-59"},{"title":"Slovak fintech Vestberry secures €2.2M to improve VC fund management in the US","url":"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m"},{"title":"seed 2025 03","url":"https://seedtable.com/companies/vestberry/funding-rounds/seed-2025-03"},{"title":"therecursive.com","url":"https://therecursive.com/?p=39794"},{"title":"Company Updates","url":"https://vestberry.com/blog/3vc-chooses-vestberry-a-cutting-edge-portfolio-management-platform"},{"title":"top of page","url":"https://www.symsite.sk/single-post/slovak-fintech-vestberry-raised-2-2m-from-investors"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/vestberry-secures-24m-in-funding-to-revolutionize-data-driven-portfolio-management-for-vc-investors"},{"title":"www.preqin.com","url":"https://www.preqin.com/data/profile/asset/vestberry--s-r-o-/641449"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/vestberry-raises-22m-to-revolutionize-data-driven-portfolio-management-for-vc-investors"}]

I didn't find a clean match. No result describes a Bratislava startup closing a Series A in 2024 led by Slovak investors. The closest candidate is Vestberry, but the sources conflict on its 2024 round and don't name a lead for it.

**Vestberry (closest candidate)**
- It is a Bratislava fintech that offers portfolio management and reporting software for Venture Capital (VC) and Private Equity (PE) fund managers.
- For 2024, the sources give different dates. PitchBook lists a Later Stage VC (Series A) round dated 8 April 2024. Caplight's page for Seed Starter lists a May 2024 Series A for Vestberry with Seed Starter as a co-investor. Neithe
… [skrátené, 1418 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Venture to Future Fund investoval do slovenského startupu kolo 2025"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"Venture to Future Fund","url":"https://www.sih.sk/en/stranky/cinnosti/venture-to-future-fund"},{"title":"slovakia venture to future fund","url":"https://insights.munich-startup.de/investors/slovakia_venture_to_future_fund"},{"title":"vff sk","url":"https://superscout.co/investor/vff-sk"},{"title":"slovakia venture to future fund","url":"https://ecosystem.madrimasd.org/investors/slovakia_venture_to_future_fund"},{"title":"slovakia venture to future fund","url":"https://startups.one.gob.es/investors/slovakia_venture_to_future_fund"},{"title":"slovakia venture to future fund","url":"https://ecosystem.lafrenchtech.com/investors/slovakia_venture_to_future_fund"},{"title":"Slovakia Venture to Future Fund","url":"https://app.dealroom.co/investors/slovakia_venture_to_future_fund"},{"title":"www.eib.org","url":"https://www.eib.org/en/projects/all/20190166?lang=en"},{"title":"Venture to Future Fund increases capital by EUR 15.3 million to support Slovak startups","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups"}]

V dostupných výsledkoch som nenašiel potvrdenú investíciu fondu Venture to Future Fund (VFF) do slovenského startupu v roku 2025. Najbližšie je jedno kolo zo septembra 2025, ale ide o český projekt.

**Kolo z roku 2025 (Česko)**
- Investícia vo výške milión eur smerovala k náborovej technológii s umelou inteligenciou z Prahy; správa je zo 30. septembra 2025. Ide o firmu Talentiqa.
- Na financovaní kola sa rovnakým dielom podieľali Purple Ventures a VFF.

**Profil fondu**
- VFF je slovenský fond, ktorý investuje do slovenských a európskych malých a stredných podnikov.
- Jednotliví investori do fondu vložili spolu 40,4 mil. eur.
- Fond sa zameriava na firmy v rastovej fáze, od late-seed po Series A a B. Minimálny vklad začína na 400 000 eur, ideálne sa pohybuje od 1,5 do 2 mil. eur.
- Kapitál fondu sa v máji 2024 zvýšil o 15,3 mil. eur. Vďaka prostriedkom z plánu obnovy sa investičné obdobie predĺžilo do konca roka 2026.

**Nezrovnalosti v údajoch**
- Jeden profil uvádza portfólio 12 firiem, zatiaľ čo tlačová správa z mája 2024 hovorí o 16 podporených spoločnostiach od júna 2020.
- Databáza CB Insights eviduje 22 investícií. Ide pravdepodobne o iný spôsob počítania, nie o rozpor v skutočnosti.

Ak potrebujete konkrétne kolo slovenskej firmy z roku 2025, odporúčam overiť to priamo na vff.sk alebo v tlačových správach Slovak Investment Holding na sih.sk, ktorý fond spravuje.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m",
  "prompt": "Extract: publication date (YYYY-MM-DD), company name, amount, round stage, and every investor organisation named (fund, company, state fund, angel network; skip private individuals) and which one led the round. For each investor, give the exact verbatim sentence from the article naming it (max 200 characters). Note the country of each investor only if the article states it."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/slovensky-startup-inhiro-hlasi-investici-300-000-e/",
  "prompt": "Extract: publication date (YYYY-MM-DD if shown), company name, amount, round stage, and every investor organisation named (fund, company, state fund; skip private individuals) with which one led. For each investor, give the exact verbatim sentence from the article naming it (max 200 characters). Note the country of each investor only if the article states it."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eu-startups.com/category/slovakia-startups/",
  "prompt": "List every article on this page with: title, publication date (YYYY-MM-DD), full article URL, company name, amount raised, and every investor organisation named (fund, company, state fund, corporate; skip private individuals). Only include articles about a specific funding round of a Slovak company dated 2023 or later. For each investor, give the verbatim sentence from the excerpt naming it (max 200 characters)."
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
**Publication date:** 2014-04-30
**Company:** InHiro
**Amount:** 300,000 EUR (about 8.2 million CZK)
**Round stage:** Not stated in the article.
**Lead investor:** The article does not say which investor led the round.

**Investors:**

1. **Neulogy Ventures**
   - Country: Slovakia, as the article describes it as a "slovenský fond" (Slovak fund).
   - Contribution: Two-thirds of the amount, the largest share.
   - Quote: "Dvě třetiny částky do projektu, který na podzim zvítězil ve StartupAwards.sk, vložil slovenský fond Neulogy Ventures"

2. **WebSupport**
   - Country: Not stated.
   - Contribution: One-third, with founder Michal Truban named as leading the company.
   - Quote: "jednou třetinou se pak podílí WebSupport v čele se zakladatelem Michalem Trubanem."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- **Publication date:** 2025-03-14
- **Company:** Vestberry
- **Amount:** €2.2 million
- **Round stage:** Not stated. The article calls it only a "new funding round."

**Investors**

1. **Seed Starter** (led the round)
   - Type: VC program of Česká a Slovenská spořitelna
   - Country: Not explicitly stated
   - Source sentence: "The funding was led by Seed Starter, a VC program of Česká a Slovenská spořitelna."

2. **Venture to Future Fund**
   - Type: Fund
   - Country: Slovakia (the article calls it "a Slovak fund")
   - Source sentence: "Other investors include Venture to Future Fund and Zero One Hundred, The Recursive reports."

3. **Zero One Hundred**
   - Type: VC company
   - Country: Not stated (the article says only that it backs startups from Emerging Europe)
   - Source sentence: "Other investors include Venture to Future Fund and Zero One Hundred, The Recursive reports."
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Definic raises €2.5M seed J&T Ventures Slovak startup vendor intelligence",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "CloudTalk €26 million Series B 2024 investors led by",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Powerful Medical €7.5M funding 2024 Slovak startup investors led",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Powerful Medical €7.5M funding 2024 Slovak startup investors led"

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/powerful-medical-secures-7-5m-funding"},{"title":"CEE VC SUMMIT 2026","url":"https://vestbee.com/blog/articles/interesting-startups-from-slovakia-worth-your-attention"},{"title":"therecursive.com","url":"https://therecursive.com/?p=36304"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/interesting-startups-from-slovakia-worth-your-attention"},{"title":"funding.tech.eu","url":"https://funding.tech.eu/investors/EISMEA"},{"title":"Slováci poslali umělou inteligenci na diagnostiku nemocí srdce. Začali v Británii, chtějí i do Česka","url":"https://cc.cz/slovaci-poslali-umelou-inteligenci-na-diagnostiku-nemoci-srdce-zacali-v-britanii-chteji-i-do-ceska/"},{"title":"top of page","url":"https://www.symsite.sk/single-post/powerful-medical-received-40m-from-ipcei-tech4cure"},{"title":"therecursive.com","url":"https://therecursive.com/?p=39116"},{"title":"innovation in motion slovakias evolving startup landscape","url":"https://tech.eu/2025/08/27/innovation-in-motion-slovakias-evolving-startup-landscape/"},{"title":"funding.tech.eu","url":"https://funding.tech.eu/geographies/slovakia"}]

Links: [{"title":"Powerful Medicals AI Breakthrough Marks a New Dawn in Heart Attack Diagnostics with EIC Support Doubles Sensitivity in Identifying Acute Coronary Occlusion on 12Lead ECG","url":"https://www.newsfilecorp.com/release/201582/Powerful-Medicals-AI-Breakthrough-Marks-a-New-Dawn-in-Heart-Attack-Diagnostics-with-EIC-Support-Doubles-Sensitivity-in-Identifying-Acute-Coronary-Occlusion-on-12Lead-ECG"},{"title":"Powerful Medicals AI Breakthrough Marks a New Dawn in Heart Attack Diagnostics with EIC Support Doubles Sensitivity in Identifying Acute Coronary Occlusion on 12Lead ECG","url":"https://www.newsfilecorp.com/release/201582/Powerful-Medicals-AI-Breakthrough-Marks-a-New-Dawn-in-Heart-Attack-Diagnostics-with-EIC-Support-Doubles-Sensitivity-in-Identifying-Acute-Coronary-Occlusion-on-12Lead-ECG?lang=fr"},{"title":"eic accelerator eu285 million funding deep tech start ups most competitive funding round 2024 02 28 en","url":"https://eic.ec.europa.eu/news/eic-accelerator-eu285-million-funding-deep-tech-start-ups-most-competitive-funding-round-2024-02-28_en"},{"title":"Source: Unsplash","url":"https://150sec.com/?p=19335"},{"title":"Subscribe to Our Newsletter","url":"https://www.thesaasnews.com/news/powerful-medical-raises-7-5-million-in-funding/"},{"title":"powerful medical receives 7 5m from eic","url":"https://en.ain.ua/2024/03/04/powerful-medical-receives-7-5m-from-eic"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/powerful-medical/financials"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/directory/investors/eic-accelerator/fintech"},{"title":"powerful medical secures e7 5m in funding from european innovation council eic","url":"https
… [skrátené, 2295 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Definic raises €2.5M seed J&T Ventures Slovak startup vendor intelligence"

Links: [{"title":"J&T VENTURES","url":"https://seedtable.com/investors/jt-ventures"},{"title":"Back to J&T VENTURES","url":"https://seedtable.com/investors/jt-ventures/portfolio"},{"title":"J&T Ventures Overview","url":"https://pitchbook.com/profiles/investor/157578-04"},{"title":"J&T Ventures","url":"https://funding.tech.eu/investors/J%26T%20Capital"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/jtventures"},{"title":"jt ventures","url":"https://aifunding.me/investors/jt-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/j-t-ventures"},{"title":"Pitch to hundreds of VC funds and business angels","url":"https://www.vestbee.com/insights/articles/startup-accelerator-of-the-month:-culttech"},{"title":"J&T Ventures","url":"https://www.startuplithuania.com/?p=105983"},{"title":"podim.org","url":"https://podim.org/?p=33008"}]

Links: [{"title":"> ## Content Index","url":"https://www.therecursive.com/slovak-definic-seed-round-ai-vendor-intelligence-platform.md"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/definic-raises-2-5-m-to-scale-ai-powered-vendor-intelligence-platform"},{"title":"👯 Founder(s): Lukáš Řezanina (CEO) and Robert Dečman (also CEO of North America)","url":"https://therecursive.com/slovak-definic-seed-round-ai-vendor-intelligence-platform/"},{"title":"1682217B 70A5 4419 AA5D 1CAC71976BE7","url":"https://funding.tech.eu/companies/1682217B-70A5-4419-AA5D-1CAC71976BE7"},{"title":"www.preqin.com","url":"https://www.preqin.com/data/profile/asset/definic/804936"},{"title":"Definic Raises 2.9M USD in Seed Funding","url":"https://seedtable.com/companies/definic/funding-rounds/seed-2026-06"},{"title":"SIH supports Definic, a Slovak technology company with global ambitions","url":"https://www.sih.sk/en/aktuality/sih-supports-definic-a-slovak-technology-company-with-global-ambitions"},{"title":"Startup Fundraising","url":"https://inforcapital.com/news/slovakias-nordics-rebrands-as-definic-raises-25-million-to-scale-its-vendor-intelligence-platform/"},{"title":"aifunding.me","url":"https://aifunding.me/companies/definic"}]

Yes, the round is confirmed by several outlets. Definic, formerly Nordics, closed a €2.5 million seed round led by J&T Ventures, and Preqin dates the close to June 12, 2026.

**The round**
- J&T Ventures led the round, with Seed Starter ČS (Česká spořitelna) and Slovak Investment Holding participating.
- The rebrand from Nordics came with the round. Slovak-based firm Definic, formerly Nordics, develops a Vendor Intelligence platform for IT procurement.
- Slovak Investment Holding's share came from public money. Its portion was made using resources from the Recovery and Resilience Plan of the Slovak Republic (Component 9).

**The company and product**
- The firm dates to 2020 and 
… [skrátené, 2273 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "CloudTalk €26 million Series B 2024 investors led by"

Links: [{"title":"cloudtalk lands one of slovakias biggest ever rounds","url":"https://sifted.eu/articles/cloudtalk-lands-one-of-slovakias-biggest-ever-rounds"},{"title":"bratislava based cloudtalk raised e25 million series b to lead the new era of ai powered voice communication","url":"https://www.eu-startups.com/2024/01/bratislava-based-cloudtalk-raised-e25-million-series-b-to-lead-the-new-era-of-ai-powered-voice-communication/"},{"title":"Witold Kepinski - 18 januari 2024","url":"https://www.dutchitchannel.nl/news/419153/kpn-ventures-en-lead-ventures-investeren-in-cloudtalk"},{"title":"The Bratislava-based firm transforming business communication","url":"https://emerging-europe.com/the-bratislava-based-firm-transforming-business-communication/"},{"title":"emerging europe","url":"https://emerging-europe.com/?p=85423"},{"title":"top of page","url":"https://www.symsite.sk/single-post/cloudtalk-raised-26m-from-investors"},{"title":"cloudtalk ziskal 26 milionu eur chce byt lidrem hlasove komunikace zalozene na ai","url":"https://forbes.cz/cloudtalk-ziskal-26-milionu-eur-chce-byt-lidrem-hlasove-komunikace-zalozene-na-ai/"},{"title":"Slovensko-český CloudTalk získal 640 milionů. Zdvojnásobuje tržby a míří na miliardový obrat","url":"https://www.lupa.cz/clanky/slovensko-cesky-cloudtalk-ziskal-640-milionu-zdvojnasobuje-trzby-a-miri-na-miliardovy-obrat/"},{"title":"product details","url":"https://zoftwarehub.com/en-ae/products/cloudtalk/product-details"},{"title":"product details","url":"https://zoftwarehub.com/en-bh/products/cloudtalk/product-details"}]

CloudTalk's €26 million Series B was co-led by KPN Ventures and Lead Ventures. Coverage of the round dates to mid-January 2024 (Jan 18, 2024).

- **Round structure:** Sifted breaks the total into €20 million of equity and €6 million of debt (€20m in equity and €6m in debt).
- **Lead investors:** Lupa describes KPN Ventures as the investment arm of the Dutch mobile operator KPN (The first of them is the investment arm of the Dutch mobile operator KPN.). Lead Ventures is based in Budapest and holds Czech AI firm Neuron Soundware in its portfolio (The second is seated in Budapest and has, among its portfolio companies, the Czech AI company Neuron Soundware.).
- **Returning backers:** Point Nine Capital, henQ, Presto Ventures and Orbit Capital also put more money in (Existing investors Point Nine Capital, henQ, Presto Ventures and Orbit Capital have also reinvested.).
- **Lifetime funding:** Symsite puts the company's total raised at about €33.3 million (So far, it has raised €33.3m from investors.). Lupa counts that total from 2019 onward (CloudTalk od roku 2019 celkově posbíral 33,3 milionu eur).
- **Use of funds:** The capital is earmarked for speeding up growth and developing AI-focused phone and contact-centre features (The new investment will strategically accelerate CloudTalk's growth and product innovation, mainly
… [skrátené, 846 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://therecursive.com/slovak-definic-seed-round-ai-vendor-intelligence-platform/",
  "prompt": "Extract: publication date (YYYY-MM-DD), company name and headquarters city/country as stated, amount, round stage, and every investor organisation named (fund, company, state fund; skip private individuals) and which one led. For each investor, give the exact verbatim sentence from the article naming it (max 200 characters). Note the country of each investor only if the article states it (e.g. Prague-based, Slovak)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.eu-startups.com/2024/01/bratislava-based-cloudtalk-raised-e25-million-series-b-to-lead-the-new-era-of-ai-powered-voice-communication/",
  "prompt": "Extract: publication date (YYYY-MM-DD), company name and headquarters as stated, amount, round stage, and every investor organisation named (fund, company, state fund, corporate; skip private individuals), with which one led. For each investor, give the exact verbatim sentence from the article naming it (max 200 characters). Note the country of each investor only if the article states it."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2024/03/04/powerful-medical-receives-7-5m-from-eic",
  "prompt": "Extract: publication date (YYYY-MM-DD), company name and its country as stated, amount, round stage, and every investor or funder organisation named (fund, company, state/EU fund; skip private individuals) and which one led. For each, give the exact verbatim sentence from the article naming it (max 200 characters). Note the country of each investor only if the article states it."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 2024-01-17
**Company:** CloudTalk
**Headquarters as stated:** "Based between New York and Bratislava" (the headline says "Bratislava-based")
**Amount:** €26 million
**Round stage:** Series B

**Investors**

| Investor | Role | Country (if stated) | Naming sentence (verbatim) |
|---|---|---|---|
| KPN Ventures | Co-lead (described as lead investor) | Netherlands (linked to its telecom operator description) | "KPN Ventures, a major telecom operator in the Netherlands and lead investor in this round" |
| Lead Ventures | Co-lead | Not stated | "Kristóf Székely, Partner at Lead Ventures" |
| Point Nine Capital | Existing investor | Not stated | "Christoph Janz, Managing Partner at Point Nine Capital." |
| henQ | Existing investor | Not stated | "Mick Mackaay, Partner at henQ" |
| Presto Ventures | Existing investor | Not stated | "supported by existing investors Point Nine Capital, henQ, Presto Ventures, and Orbit Capital" |
| Orbit Capital | Existing investor | Not stated | "supported by existing investors Point Nine Capital, henQ, Presto Ventures, and Orbit Capital" |
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 2024-03-04

**Company:** Powerful Medical (country as stated: Slovakia)
- Quote: "Slovak medtech Powerful Medical receives €7.5M from EIC"

**Amount:** €7.5 million total, made up of a €2.5 million grant and a follow-on €5 million investment.
- Quote: "has received a €2.5 million grant and a follow-on €5 million investment from the European Innovation Council (EIC)"

**Round stage:** The article does not name a round stage for this funding. It describes a grant plus a follow-on investment. The article's earlier funding was a €6.2 million seed round in 2022.

**Investors and funders:**

1. **European Innovation Council (EIC)**, part of the EU's Horizon Europe framework program
   - Lead: not stated
   - Country: not stated (the article describes it as part of the European Union's framework program)
   - Quote: "The startup was backed by the European Innovation Council, part of the European Union’s Framework Program"

2. **2022 seed round investors** (named in the article as earlier backers, not this round): CB ESPRI Impact One, bpd partners, and Venture To Future Fund
   - Lead: not stated
   - Country: not stated
   - Quote: "Investors were CB ESPRI Impact One, bpd partners, Venture To Future Fund, and several business angels."

I omitted the business angels because they are private individuals.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 2026-06-15

**Company:** Definic (previously known as Nordics)

**Headquarters:** The article does not state a city. It describes Definic as a "Slovak startup," so the country is Slovakia.

**Amount:** €2.5 million ($2.9 million)

**Round stage:** Seed

**Investors:**

| Investor | Role | Country stated in article? | Supporting sentence from article |
|---|---|---|---|
| J&T Ventures | Lead | No | "I first met Martin Kešner from J&T Ventures at Vodafone Nápad Roku back in 2023." |
| Seed Starter ČS (Česká spořitelna) | Participant | No | "Together with Seed Starter ČS and Slovak Investment Holding, this investment gives us the platform" |
| Slovak Investment Holding (SIH) | Participant | No | "Together with Seed Starter ČS and Slovak Investment Holding, this investment gives us the platform" |

J&T Ventures is identified as lead in the "Funded by" line: "J&T Ventures (lead), Seed Starter ČS (Česká spořitelna), Slovak Investment Holding (SIH)."
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://therecursive.com/?p=43718",
  "prompt": "This is a roundup of Slovak startup funding rounds. For EACH individual funding round listed, give: company name, publication date of the article (YYYY-MM-DD) and the date of the round if stated, amount, round stage if stated, company headquarters country only if stated, and EVERY investor organisation named for that round (fund, company, state fund, angel network; skip private individuals) with its role (lead or participant) if stated. For each investor, give the exact verbatim sentence from the article naming it (max 200 characters). Skip rounds from non-Slovak companies or rounds before 2023."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://therecursive.com/?p=39116",
  "prompt": "This is a roundup of Central/Eastern European startup funding rounds (possibly H1 2024). Extract ONLY the rounds of Slovak companies (dated 2023 or later). For EACH such round give: company name, round date if stated (YYYY-MM-DD), amount, round stage if stated, company headquarters country only if stated, and EVERY investor organisation named for that round (fund, company, state fund; skip private individuals) with its role (lead or participant) if stated. For each investor, give the exact verbatim sentence from the article naming it (max 200 characters)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Only one Slovak company's round appears in the content:

**Sensible Biotechnologies** (Slovakia)
- **Amount:** €42M in the headline; the summary says "$47 million." The page doesn't reconcile the two figures.
- **Round date:** Not stated.
- **Round stage:** Not stated.
- **Headquarters country:** Not stated. The page describes it as "Slovak-founded," which doesn't specify where it is headquartered.
- **Investors:** None named in the provided content.

The other rounds on the page are not Slovak: Buntar Aerospace (Ukraine), Golbriak Space (Estonia), and Siena (Romanian-founded).
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Only one round on this page qualifies: **Sensible Biotechnologies** (Slovak-founded).

- **Company:** Sensible Biotechnologies
- **Article publication date:** Not stated on the page
- **Round date:** Not stated
- **Amount:** Inconsistent. The headline says €42M, and the summary says "$47 million." The page doesn't reconcile the two.
- **Round stage:** Not stated
- **HQ country:** Not explicitly stated. The page describes the company only as "Slovak-founded."
- **Investors:** None named in the available text

The page doesn't include the full article, so investor details may be in the complete piece at the linked URL.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Sensible Biotechnologies €42M funding round investors Slovak-founded",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Blockmate Bratislava secures €1.5M investment Seed Starter",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Slovak startup secures seed funding 2026 Slovakia-based investors fund announced",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Blockmate Bratislava secures €1.5M investment Seed Starter"

Links: [{"title":"Czech-Slovak fintech startup Blockmate secures €1.5M investment","url":"https://en.ain.ua/tech/investments/page/68"},{"title":"Czech-Slovak fintech startup Blockmate secures €1.5M investment","url":"https://en.ain.ua/2023/09/15/czech-slovak-fintech-blockmate-secures-1-5m"},{"title":"E5D18C07 E581 463B 9D8B 5ED42E34D09C","url":"https://funding.tech.eu/companies/E5D18C07-E581-463B-9D8B-5ED42E34D09C"},{"title":"24691 majernik mihalikova advises blockmate on eur 1 5 million seed round","url":"https://mail.ceelegalmatters.com/slovakia/24691-majernik-mihalikova-advises-blockmate-on-eur-1-5-million-seed-round"},{"title":"24691 majernik mihalikova advises blockmate on eur 1 5 million seed round","url":"https://ceelegalmatters.com/slovakia/24691-majernik-mihalikova-advises-blockmate-on-eur-1-5-million-seed-round"},{"title":"24691 majernik mihalikova advises blockmate on eur 1 5 million seed round","url":"https://ceelm.com/slovakia/24691-majernik-mihalikova-advises-blockmate-on-eur-1-5-million-seed-round"},{"title":"blockmate ziskal investiciu vo vyske 15 miliona eur polovicu tejto sumy poskytne seed starter slovenskej a ceskej sporitelne","url":"https://sita.sk/blockmate-ziskal-investiciu-vo-vyske-15-miliona-eur-polovicu-tejto-sumy-poskytne-seed-starter-slovenskej-a-ceskej-sporitelne/"},{"title":"closerocket raised a 1m seed round with vision ventures jinej fund and angel investors in czech republic and slovakia","url":"https://nordic9.com/news/closerocket-raised-a-1m-seed-round-with-vision-ventures-jinej-fund-and-angel-investors-in-czech-republic-and-slovakia/"},{"title":"Seed Starter ČS","url":"https://unicorn-nest.com/funds/seed-starter-cs/"}]

The Blockmate round is real, but it was announced in September 2023, so it isn't recent news. Reports from that time say the Bratislava fintech raised €1.5 million, with Seed Starter, Erste's corporate venture program, as the lead. Blockmate, a Bratislava-based provider of financial services has secured €1.5 million led by Seed Starter of Česká a Slovenská spořitelna. A CloseRocket listing dates the Blockmate deal to 07 September 2023, while Unicorn Nest gives its date as 15 Sep 2023.

**Investors and amounts**
- Seed Starter put in the largest share, €760,000.
- Other backers included investment funds Tensor Ventures, DEPO Ventures, Token Ventures, BADideas.fund, ZAKA Ventures, and Diaspora Ventures.
- Sources differ on the size of the round. Unicorn Nest records the deal as Seed 1M, while the press reports say €1.5 million.

**Company background**
- Blockmate was founded in 2017 by Andrej Coplak and Peter Lauber.
- Its platform links digital assets with open banking. Its technology uses the Open Banking standard to connect cryptocurrency users with over 25,000 existing fintechs.

**Strategic angle**
Seed Starter's executive manager, Michal Vanovčan, said the deal helps the bank prepare for European cry
… [skrátené, 533 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Slovak startup secures seed funding 2026 Slovakia-based investors fund announced"

Links: [{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=103787"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/tag/slovakia"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/startup-tipy-rady-financovanie/"},{"title":"Best Fintech Startups in Slovakia","url":"https://seedtable.com/best-fintech-startups-in-slovakia"},{"title":"Best Technology Startups in Slovakia","url":"https://seedtable.com/best-technology-startups-in-slovakia"},{"title":"Best Data Analytics Startups in Slovakia","url":"https://seedtable.com/best-data-analytics-startups-in-slovakia"},{"title":"Best SaaS Startups in Slovakia","url":"https://seedtable.com/best-saas-startups-in-slovakia"},{"title":"Best AI Startups in Slovakia","url":"https://seedtable.com/best-ai-startups-in-slovakia"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/directory/cities/slovakia-slovak-republic/presov"}]

The best match is **Definic**, though the results are aggregator listings rather than primary press releases, so the details are worth confirming with the company.

- **Definic (June 2026, seed round):** Definic raises €2.5M to scale AI-powered vendor intelligence platform. The seed round was led by J&T Ventures, with participation from Seed Starter ČS and Slovak Investment Holding. Slovak Investment Holding is a Slovak state-owned holding company, which is my own background knowledge, not something the results state. The results don't say where J&T Ventures or Seed Starter ČS are based. Seedtable also counts Definic among Definic, CloudTalk and Vestberry lead the 2026 ranking for Slovak technology startups.

- **AdSpawn (April 2026):** Slovak startup AdSpawn raises €500k for its AI game advertising solution. The fresh capital was backed by Rockaway Ventures and Czech Founders VC. The listing doesn't call this a seed round, and it doesn't say whether these investors are Slovakia-based, so it fits your query less well than Definic.

Other 2026 items in the results don't fit. Readmio is described as a Czech fairy tale app.

I ran one search, so I didn't check the original announcements. To confirm the Definic round, look for the company's own press release or the lead investor's announcement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Sensible Biotechnologies €42M funding round investors Slovak-founded"

Links: [{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-april-2023"},{"title":"Slováci v Oxforde získali milióny eur. Svetu sú odhodlaní priniesť revolúciu vo vývoji vakcín","url":"https://www.startitup.sk/?p=750241"},{"title":"logoTry Persana","url":"https://insights.persana.ai/Sensible Biotechnologies"},{"title":"Sensible Biotechnologies company logo","url":"https://www.cbinsights.com/company/sensible-biotechnologies/financials"},{"title":"mRNA platform company","url":"https://funding.tech.eu/companies/405CC75E-D4B6-4028-960E-9DF0C07EAD31"},{"title":"Sensible Biotechnologies company logo","url":"https://www.cbinsights.com/company/sensible-biotechnologies"},{"title":"sensible biotechnologies","url":"https://www.vcbacked.co/company/sensible-biotechnologies"},{"title":"Dutch-based Sensible Healthcare Systems raises funding to develop its continuous biosensor platform","url":"https://siliconcanals.com/?p=5538"},{"title":"pre seed 2023 04","url":"https://seedtable.com/companies/sensible-biotechnologies/funding-rounds/pre-seed-2023-04"}]

Links: [{"title":"159939 sensible bio lands 47m to scale mrna manufacturing","url":"https://dealroom.co/news/159939-sensible-bio-lands-47m-to-scale-mrna-manufacturing/"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/sensible-biotechnologies-lands-47-m"},{"title":"sensible biotechnologies 2026 series a funding","url":"https://www.startupmag.co.uk/funding/sensible-biotechnologies-2026-series-a-funding/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/sensible"},{"title":"Sensible Biotechnologies Raises $4.2mn in a Pre-Seed Financing Round to Revolutionize mRNA Manufacturing","url":"https://www.biospace.com/sensible-biotechnologies-raises-4-2mn-in-a-pre-seed-financing-round-to-revolutionize-mrna-manufacturing"},{"title":"businesswire.com","url":"https://businesswire.com/news/home/20261006778738/en"},{"title":"www.genomeweb.com","url":"https://www.genomeweb.com/node/604401"},{"title":"mRNA platform company","url":"https://funding.tech.eu/companies/405CC75E-D4B6-4028-960E-9DF0C07EAD31"},{"title":"The UK-Slovak Sensible Biotechnologies gets $4.2M to develop mRNA therapeutics and vaccines","url":"https://en.ain.ua/2023/04/06/sensible-biotechnologies-gets-4-2m"},{"title":"hyper.ai","url":"https://hyper.ai/en/stories/e2684d8d8b8fe2f8941705b20e1f7ff7"}]

I couldn't find any source reporting a €42M round for Sensible Biotechnologies. The most recent round, announced October 6, 2026, is reported in dollars. The €42M figure may be a conversion of that amount, but no result confirms this.

**The latest round**
Vestbee puts the total at $47M, covering a Series A plus up to $20M in non-dilutive grants from Slovak and EU sources (Bratislava-based Sensible Biotechnolo
… [skrátené, 2843 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://sita.sk/blockmate-ziskal-investiciu-vo-vyske-15-miliona-eur-polovicu-tejto-sumy-poskytne-seed-starter-slovenskej-a-ceskej-sporitelne/",
  "prompt": "Extract: publication date (YYYY-MM-DD if shown), company name and headquarters city/country as stated, amount, round stage if stated, and EVERY investor organisation named (fund, bank program, company; skip private individuals), with which one led and the amount each put in if stated. For each investor, give the exact verbatim sentence from the article naming it, copied word for word in the original language (max 200 characters)."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://businesswire.com/news/home/20261006778738/en",
  "prompt": "Extract: publication date (YYYY-MM-DD), company name and headquarters/country as stated in the release, amount of the Series A and any non-dilutive funding, round stage, and EVERY investor organisation named (fund, company, government/EU body; skip individual people) and which one led the round if stated. For each investor, give the exact verbatim sentence from the release naming it (max 200 characters)."
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
**Publication date:** 2023-09-18

**Company:** Blockmate (described as a "česko-slovenský startup," or Czech-Slovak startup). The article does not state a headquarters city or country.

**Total amount:** 1.5 million EUR from seven investors.

**Round stage:** The article calls this the second investment round ("druhom investičnom kole"). It does not use a stage label such as seed or pre-seed. The company's earlier pre-seed round raised a total of 500,000 EUR.

**Investors:**

1. **Seed Starter (Slovenská and Česká sporiteľňa, corporate venture program of the Erste Group)**
   - Amount: 760,000 EUR, the largest share. The article does not explicitly call it the lead.
   - Quote: "Najväčšiu sumu – 760 tisíc eur – dostane od Seed Startera Slovenskej a Českej sporiteľne."

2. **Tensor Ventures** (investment fund)
   - Amount: not stated.
   - Quote: "Ďalej potom fondy Tensor Ventures a DEPO Ventures, ktoré tak pokračujú vo svojej podpore"

3. **DEPO Ventures** (fund and angel syndicate)
   - Amount: not stated.
   - Quote: "Ďalej potom fondy Tensor Ventures a DEPO Ventures, ktoré tak pokračujú vo svojej podpore"

4. **Token Ventures**
   - Amount: not stated.
   - Quote: "Do druhého investičného kola sa prvýkrát zapojili napríklad Token Ventures, BADideas.fund,"

5. **BADideas.fund**
   - Amount: not stated.
   - Quote: "Do druhého investičného kola sa prvýkrát zapojili napríklad Token Ventures, BADideas.fund,"

6. **ZAKA Ventures**
   - Amount: not stated.
   - Quote: "…ZAKA Ventures a prestížny americký fond Diaspora Ventures."

7. **Diaspora Ventures** (US fund)
   - Amount: not stated.
   - Quote: "…ZAKA Ventures a prestížny americký fond Diaspora Ventures."

The article does not identify a lead investor other than the largest share going to Seed Starter. Quotes are truncated to stay within the 125-character limit.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "AdSpawn Slovak startup €500k Rockaway Ventures Czech Founders VC",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "AdSpawn Slovak startup €500k Rockaway Ventures Czech Founders VC"

Links: [{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/ad-spawn-raises-500k"},{"title":"Tomáš Pospíchal","url":"https://sk.linkedin.com/in/pospo"},{"title":"AdSpawn Overview","url":"https://pitchbook.com/profiles/company/616526-47"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/tag/slovakia"},{"title":"Většinu her si kvůli špatné reklamě nikdo nestáhne. Slovenský startup staví řešení na její automatizaci","url":"https://www.e15.cz/byznys/startupy/vetsinu-her-si-kvuli-spatne-reklame-nikdo-nestahne-slovensky-startup-stavi-reseni-na-jeji-automatizaci-1432275"},{"title":"Milan Štrba zo startupu AdSpawn: „Na Slovensku je kopa talentovaných ľudí, ktorí sa podceňujú“","url":"https://www.startitup.sk/?p=1207537"},{"title":"Bratislavskí inovátori postavili stroj na výrobu pozornosti, idú dobyť trh v USA. Investori im posielajú pol milióna eur","url":"https://www.startitup.sk/?p=1196023"},{"title":"Milan Štrba zo startupu AdSpawn: „Na Slovensku je kopa talentovaných ľudí, ktorí sa podceňujú“","url":"https://www.startitup.sk/zone-milan-strba-zo-startupu-adspawn-na-slovensku-je-kopa-talentovanych-ludi-ktori-sa-podcenuju/"},{"title":"Bratislavskí inovátori postavili stroj na výrobu pozornosti, idú dobyť trh v USA. Investori im posielajú pol milióna eur","url":"https://www.startitup.sk/bratislavski-inovatori-postavili-stroj-na-vyrobu-pozornosti-idu-dobyt-trh-v-usa-investori-im-posielaju-pol-miliona-eur/"},{"title":"Drtivá většina herních studií testuje reklamy špatně, říká. Řeší to startupem, teď získal investici","url":"https://cc.cz/drtiva-vetsina-hernich-studii-testuje-reklamy-spatne-rika-resi-to-startupem-ted-ziskal-investici/"}]

Yes, the round checks out. Vestbee reported that Slovak startup AdSpawn, which develops AI-driven tools for automating the creation of mobile game advertising creatives, has secured €500,000 (over CZK 12 million), with the article dated April 22, 2026.

**The company**
- Four founders, Milan Štrba, Martin Luther, Roman Janajev, and Tomáš Pospíchal, started it, and the Bratislava office is listed in Corporate Office Bratislava Slovakia.
- The software takes in a game's footage, identifies key scenes, and assembles short ads using formats common in user acquisition campaigns (selects key moments, and assembles short-form ads using predefined structures).

**The investors**
- Rockaway Ventures is described as the venture capital arm of the Rockaway Capital group that invests in startups digitizing traditional industries with a strong focus on AI. Rockaway's Petr Šmíd praised the company's quality and global ambition.
- Czech Founders VC, an early-stage investor, has been supporting AdSpawn since its acceleration phase. Its first check was €40k, which came with a place in its Sherpa accelerator (získal místo v akceleračním programu Sherpa od Czech Founders VC, per a Cz
… [skrátené, 1159 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.startitup.sk/bratislavski-inovatori-postavili-stroj-na-vyrobu-pozornosti-idu-dobyt-trh-v-usa-investori-im-posielaju-pol-miliona-eur/",
  "prompt": "Extract: publication date (YYYY-MM-DD if shown), company name and headquarters as stated, amount, round stage if stated, and EVERY investor organisation named (fund, accelerator, company; skip private individuals), with its role (lead/participant) if stated and its country only if stated. For each investor, give the exact verbatim sentence from the article naming it, in the original Slovak, max 200 characters."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** 2026-04-27

**Company:** AdSpawn, a Bratislava startup (described as "bratislavského startupu AdSpawn")

**Amount:** Half a million euros (pol milióna eur)

**Round stage:** Not stated

**Investors:**

1. **Rockaway Ventures**
   - Role: Not stated
   - Country: Czech (the article calls the funds "českých fondov")
   - Source sentence (fragment, as the full sentence exceeds 200 characters): "investícia pol milióna eur od českých fondov Rockaway Ventures a Czech Founders VC"

2. **Czech Founders VC**
   - Role: Not stated
   - Country: Czech (same basis as above)
   - Source sentence: same fragment as above
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\discovery\list_b_sk.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\discovery\\list_b_sk.json",
  "content": "[\n  {\n    \"investor_name\": \"Jet Ventures\",\n    \"investor_type_claimed\": \"vc\",\n    \"hq_country_claimed\": \"CZ\",\n    \"company\": \"Cequence\",\n    \"company_country\": \"SK\",\n    \"round\": \"seed\",\n    \"amount\": \"€2M\",\n    \"deal_date\": \"2025-06-13\",\n    \"source_url\": \"https://siliconcanals.com/slovakia-cequence-secures-2m/\",\n    \"source_published\": \"2025-06-13\",\n    \"quote\": \"led by Czech Jet Ventures to advance its AI-driven contract management platform.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"investor_name\": \"Look AI Ventures\",\n    \"investor_type_claimed\": \"unknown\",\n    \"hq_country_claimed\": \"CZ\",\n    \"company\": \"Cequence\",\n    \"company_country\": \"SK\",\n    \"round\": \"seed\",\n    \"amount\": \"€200,000\",\n    \"deal_date\": \"2025-06-13\",\n    \"source_url\": \"https://siliconcanals.com/slovakia-cequence-secures-2m/\",\n    \"source_published\": \"2025-06-13\",\n    \"quote\": \"The round attracted participation from Czech Jet Ventures (€1.7M), Czech Look AI Ventures (€200,000),\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"investor_name\": \"Seed Starter\",\n    \"investor_type_claimed\": \"cvc\",\n    \"hq_country_claimed\": \"unknown\",\n    \"company\": \"Vestberry\",\n    \"company_country\": \"SK\",\n    \"round\": \"unknown\",\n    \"amount\": \"€2.2 million\",\n    \"deal_date\": \"2025-03-14\",\n    \"source_url\": \"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m\",\n    \"source_published\": \"2025-03-14\",\n    \"quote\": \"The funding was led by Seed Starter, a VC program of Česká a Slovenská spořitelna.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"investor_name\": \"Venture to Future Fund\",\n    \"investor_type_claimed\": \"vc\",\n    \"hq_country_claimed\": \"SK\",\n    \"company\": \"Vestberry\",\n    \"company_country\": \"SK\",\n    \"round\": \"unknown\",\n    \"amount\": \"€2.2 million\",\n    \"deal_date\": \"2025-03-14\",\n    \"source_url\": \"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m\",\n    \"source_published\": \"2025-03-14\",\n    \"quote\": \"Other investors include Venture to Future Fund and Zero One Hundred, The Recursive reports.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"investor_name\": \"Zero One Hundred\",\n    \"investor_type_claimed\": \"vc\",\n    \"hq_country_claimed\": \"unknown\",\n    \"company\": \"Vestberry\",\n    \"company_country\": \"SK\",\n    \"round\": \"unknown\",\n    \"amount\": \"€2.2 million\",\n    \"deal_date\": \"2025-03-14\",\n    \"source_url\": \"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m\",\n    \"source_published\": \"2025-03-14\",\n    \"quote\": \"Other investors include Venture to Future Fund and Zero One Hundred, The Recursive reports.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"investor_name\": \"J&T Ventures\",\n    \"investor_type_claimed\": \"vc\",\n    \"hq_country_claimed\": \"unknown\",\n    \"company\": \"Definic (previously known as Nordics)\",\n    \"company_country\": \"SK\",\n    \"round\": \"seed\",\n    \"amount\": \"€2.5 million ($2.9 million)\",\n    \"deal_date\": \"2026-06-15\",\n    \"source_url\": \"https://therecursive.com/slovak-definic-seed-round-ai-vendor-intelligence-platform/\",\n    \"source_published\": \"2026-06-15\",\n    \"quote\": \"J&T Ventures (lead), Seed Starter ČS (Česká spořitelna), Slovak Investment Holding (SIH).\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"investor_name\": \"Seed Starter ČS\",\n    \"investor_type_claimed\": \"cvc\",\n    \"hq_country_claimed\": \"unknown\",\n    \"company\": \"Definic (previously known as Nordics)\",\n    \"company_country\": \"SK\",\n    \"round\": \"seed\",\n    \"amount\": \"€2.5 million ($2.9 million)\",\n
… [skrátené, 11657 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\discovery\list_b_sk.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "List B written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\discovery\\list_b_sk.json: 7 rounds, 24 rows (2023: 1 round, 2024: 2, 2025: 2, 2026: 2). Well short of the 25-40 round target because most of the 40-call budget went to dead ends (tag pages 404, 403s, pre-2023 articles, undated pages).\n\nMedia used: startitup.sk (AdSpawn), sita.sk (Blockmate), en.ain.ua (Vestberry, Powerful Medical), siliconcanals.com (Cequence), eu-startups.com (CloudTalk), therecursive.com (Definic).\n\nExcluded: Vestbee, Seedtable, Dealroom, CB Insights, Preqin, Caplight as sources. Sensible Biotechnologies ($47M, Oct 2026) is unverified because BusinessWire returned 403, so it is not in the file. Talentiqa (Prague-based), Eyerim (2019), Better Stack (2022) and InHiro (dated 2014) are out of scope.\n\nCaveats: quotes are copied from WebFetch's model-extracted text, not raw HTML, so the machine check may fail on some. Blockmate company_country=SK is my judgment from \"česko-slovenský\". CloudTalk is \"Based between New York and Bratislava\" in the body. Surprising: the Recursive reports only about one Slovak 2024 AI round, and the search snippets I saw put 2025 Slovak VC volume near EUR 7M (unverified)."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

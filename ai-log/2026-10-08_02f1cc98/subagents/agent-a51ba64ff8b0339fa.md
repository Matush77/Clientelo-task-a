# Subagent: Evidence v1 on 3 CP2 candidates (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 20:06:52

# Evidence agent – v1

You are an evidence collector for a database of **investors into companies**. For each candidate below, find public
evidence of **what the entity is** and **whether it actually invests**, and fill a fixed JSON record.

You do **not** decide whether the candidate goes into the database. A program decides that from your evidence, and
every quote you give will be **machine-checked**: the program downloads `source_url` and searches the page for your
`quote`. A quote that is not on the page, or a value that is not in the quote, is thrown away. So:

- **Copy quotes verbatim** (max 300 characters), in the original language (Czech/Slovak/English) – never translate,
  shorten in the middle, or paraphrase.
- **Never estimate, convert or compute numbers.** If a ticket size or fund size is not stated, return `null`.
- **"Not found" is a good answer.** A missing field costs nothing; an invented one makes the whole record fail.

Use WebSearch / WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed).
Budget: **at most 15 tool calls per candidate**.

**How to get verbatim quotes:** WebFetch passes the page through a model that may summarise it. Always give
WebFetch a prompt like: *"Return word-for-word, without summarising or translating, every sentence that mentions
<name> / investments / portfolio / fund size / ticket, and the page's publication date."* Copy your quote only from
such word-for-word output, never from a summary or from a search-result snippet.

## Candidates

1. candidate_id: C012 | name: Credo Ventures (alias: Credo Ventures a.s.) | known website: www.credoventures.com
2. candidate_id: C002 | name: Investown Technologies s.r.o. | known website: https://www.investown.cz
3. candidate_id: C206 | name: E.S. invest, s. r. o. | known website: none | Slovak company ID (IČO): 43875408

## Allowed sources

| Prefer | Source | Use |
|---|---|---|
| 1 | Registries and regulators (ARES, obchodní/obchodný rejstřík/register, RPO, ČNB/NBS, ESMA); official LP disclosures (EIF, Slovak Investment Holding, Národní rozvojová banka) | anything |
| 2 | The candidate's own website (portfolio, about, team, news, imprint/kontakt) | anything |
| 3 | News articles and press releases (incl. the funded startup's own press release) | investments, fund sizes |

**Forbidden as `source_url`:** Dealroom, Crunchbase, PitchBook, Tracxn, CB Insights, Vestbee, Caplight, Seedtable,
Signal NFX, OpenVC, LinkedIn, Wikipedia, any "top investors" listicle. You may use them only to get ideas where to
look; then cite the original source.

## What to collect (per candidate)

1. **identity** – the legal entity behind the brand: legal name + company ID (IČO/IČ) of the **management company**
   (look in the website footer, "Kontakt", "Impressum", privacy/GDPR page). Fund vehicles go to `funds`.
2. **hq_country** – where the investment team sits (office address). Fund domicile (Luxembourg, NL…) does not count.
3. **investor_type** – one or more of: `vc`, `cvc`, `public_vc`, `pe`, `family_office`, `angel_network`,
   `accelerator`, `fund_of_funds`, `crowdfunding_platform`, `advisory`, `real_estate`, `lender`, `group_holding`,
   `grant_agency`, `other`. Choose what the evidence shows, not what the name suggests.
4. **investments** – up to **4** concrete investments into companies, with date. Priority:
   (a) the most recent ones, ideally after 2023-10-01; (b) **at least one from a source other than the candidate's
   own website** (news article or the startup's press release); (c) a portfolio page without dates may be used, with
   `published_date: null`.
5. **sectors** – what it invests in. Use only these codes: `ai_data`, `enterprise_saas`, `fintech_insurtech`,
   `health_digital`, `life_sciences_medtech`, `deeptech_hardware`, `cleantech_energy`, `mobility_logistics`,
   `consumer_ecommerce`, `edtech`, `proptech_construction`, `agri_food`, `cybersecurity`, `media_gaming`,
   `industry_manufacturing`, `iot_telecom`, `hr_worktech`, `travel_hospitality`, `govtech_legaltech`,
   `defense_space`, `sector_agnostic`. `derivation: "stated"` if the candidate says so; `"inferred"` if you derive it
   from the portfolio (then the quote is the portfolio evidence).
6. **stages** – `pre_seed`, `seed`, `series_a`, `series_b_plus`, `growth`, `buyout`.
7. **ticket** – typical investment size **as stated** by the candidate or a source about it.
8. **total_capital** – AUM, or the size of its fund(s) (say which: `aum`, `fund_size`, `committed`, `target`).
9. **funds** – named funds/vehicles with size and vintage if stated.
10. **red_flags** – anything that speaks against "active investor into companies": in liquidation, only real estate,
    only lending, only an intermediary/platform, only advises, invests only into its own group, no investment found,
    last investment long ago, etc. Each red flag also needs a source + quote.

## The claim format (use it for every field)

```json
{
  "value": "...",                // string, list, or object as specified below
  "value_text": "...",           // the exact words inside the quote that state the value (copied from the quote)
  "source_url": "...",
  "quote": "...",                // verbatim from the page, max 300 chars, must contain value_text
  "published_date": "YYYY-MM-DD or YYYY-MM or YYYY or null",   // date of the page/article, as shown on it
  "derivation": "stated | inferred"
}
```

## Output file

Write a UTF-8 JSON array with one object per candidate to `C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\cp2_batch.json` (create the folder if needed), nothing
else into it:

```json
{
  "candidate_id": "as given",
  "name": "as given",
  "website": "official website URL or null",
  "identity": [ {claim, value = {"legal_name": "...", "company_id": "...", "country": "CZ|SK|other"}} ],
  "hq_country": {claim, value = "CZ|SK|other"} or null,
  "investor_type": {claim, value = ["vc", ...]} or null,
  "investments": [ {claim, value = {"company": "...", "date": "YYYY-MM-DD|YYYY-MM|YYYY", "round": "seed|...|unknown", "amount": "as written or null"}} ],
  "sectors": {claim, value = ["fintech_insurtech", ...]} or null,
  "stages": {claim, value = ["seed", ...]} or null,
  "ticket": {claim, value = {"min": "as written or null", "max": "as written or null", "currency": "EUR|CZK|USD|null"}} or null,
  "total_capital": {claim, value = {"amount": "as written", "currency": "EUR|CZK|USD", "capital_type": "aum|fund_size|committed|target", "as_of": "YYYY or YYYY-MM-DD or null"}} or null,
  "funds": [ {claim, value = {"name": "...", "size": "as written or null", "vintage": "YYYY or null"}} ],
  "red_flags": [ {claim, value = "short description"} ],
  "not_found": ["ticket", "total_capital", ...],
  "search_log": ["every search query you ran, in order"]
}
```

Then reply in at most 120 words: per candidate one line (investor type + number of investments found + anything
doubtful). Today is 2026-10-08.

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
  "query": "Credo Ventures investice portfolio",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.credoventures.com",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo / investments / portfolio / fund size / ticket / investment team / office address / company ID (IČO) / legal entity / a.s. / s.r.o., and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Credo Ventures a.s. IČO",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Credo / investments / fund / ticket / portfolio references:**

- "Credo | We back the most ambitious founders from CEE. Pre-everything."
- "The fund of choice for CEE founders building generational companies."
- "Having believed in the region's talent since 2009, we write the first check — before product, before revenue,"
- "often before a deck."
- "Backing exceptional people, not thesis-driven."
- "Leading Pre-Seed rounds."
- "$1M - $5M checks."
- "5, Funds, 17, Years on the market, 100+, Companies backed, 2/2 CEE decacorns, First check, Portfolio"
- "We led the non-obvious Pre-Seed."
- "● We co-led the Pre-Seed."
- "● We invested in Pre-Seed."
- "[View all →](./portfolio)"

**Office addresses and copyright:**

- "Prague, Karlovo Náměstí 10, 120 00, Prague, Czech Republic,"
- "Kraków, Lubomirskiego 20, 31-509 Kraków, Poland,"
- "©2026 Credo Ventures."

**Publication date:**

- "Oct 6, 2026, 2:38 PM UTC"

The page does not contain a company ID (IČO), legal entity name, "a.s.", or "s.r.o.", so none are listed.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Credo Ventures a.s. IČO"

Links: [{"title":"credo ventures a s 28538137","url":"https://www.podnikatel.cz/rejstrik/credo-ventures-a-s-28538137/"},{"title":"Smlouvy Dotace Platy Úřady Zakázky Sponzoři & firmy","url":"https://www.hlidacstatu.cz/subjekt/RegistrSmluv/28538137"},{"title":"Free company profile — no paywall, no login","url":"https://eulerpool.com/company/CZ/Credo Ventures a.s.,Praha 2,28538137"},{"title":"podim.org","url":"https://podim.org/?p=32980"},{"title":"Cover Image CREDO VENTURES","url":"https://app.mergerlinks.com/companies/credo-ventures"},{"title":"credo ventures","url":"https://privateequitylist.com/investor/credo-ventures"},{"title":"Credo Ventures","url":"https://www.everythingstartups.com/vc-funds/credo-ventures"},{"title":"credo ventures","url":"https://f4.fund/startups/credo-ventures"},{"title":"credo ventures","url":"https://vcbeast.com/claim/credo-ventures"}]

**IČO: 28538137**

Several registry-based sites list this number. The podnikatel.cz register entry gives the IČO alongside a DIČ of CZ28538137 and a creation date of 2 March 2009 (Základní údaje o subjektu IČ: 28538137 ... Datum vzniku: 2. 3. 2009). The Hlídač státu contract register shows the same IČO and founding date (Založeno 02.03.2009 IČO 28538137).

Other registry details:
- **Commercial register:** Prague City Court keeps the company's file under reference B 15102 (V obchodním rejstříku je zapsána pod spisovou značkou B 15102, Městský soud v Praze.).
- **Registered office:** Karlovo náměstí 2097/10, Praha 2 (per podnikatel.cz).
- **Registered capital:** 4 240 000 Kč.
- **Status and LEI:** Eulerpool lists the company as active and gives its LEI as 315700V9DQ1HLW5Z2K13 (Status: active.).

The sources disagree on the firm's founding year. One profile says founded in 2008, another says founded in 2010, but the legal entity's registry record uses 2 March 2009.

For an official confirmation, check the number in the Czech business register (ARES) or the commercial register at justice.cz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Credo Ventures investice portfolio"

Links: [{"title":"zahajte fazi pet credo ventures maji paty fond za temer dve miliardy prim bude hrat mladi","url":"https://forbes.cz/zahajte-fazi-pet-credo-ventures-maji-paty-fond-za-temer-dve-miliardy-prim-bude-hrat-mladi/"},{"title":"České Credo Ventures má pro startupy nový fond a 1,8 miliardy korun. Už v něm nebude Kiska","url":"https://cc.cz/ceske-credo-ventures-ma-pro-startupy-novy-fond-a-18-miliardy-korun-uz-v-nem-nebude-kiska/"},{"title":"Nový fond, odchod Andreje Kisky i tři další partneři. V Credo Ventures se dějí velké věci","url":"https://cc.cz/novy-fond-odchod-andreje-kisky-i-tri-dalsi-partneri-v-credo-ventures-se-deji-velke-veci/"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=15872"},{"title":"podim.org","url":"https://podim.org/?p=32980"},{"title":"vcbeast.com","url":"https://vcbeast.com/vc-firms/credo-ventures/portfolio"},{"title":"prague based vc credo ventures plans to invest e88m in central eastern europe startups","url":"https://siliconcanals.com/prague-based-vc-credo-ventures-plans-to-invest-e88m-in-central-eastern-europe-startups/"},{"title":"credo ventures","url":"https://www.vcbacked.co/directory/investors/credo-ventures"},{"title":"Back to Credo Ventures","url":"https://seedtable.com/investors/credo-ventures/portfolio"},{"title":"credo ventures","url":"https://vcbeast.com/claim/credo-ventures"}]

Credo Ventures is a Prague venture firm that focuses on early-stage investments in technology startups across Central and Eastern Europe. Sources disagree on how many companies it has backed, so treat the counts below as estimates.

**Portfolio size**
- Czech coverage counts about 76 startups backed since 2011, including two unicorns. Od roku 2011 Credo vybudovalo portfolio o celkem 76 startupech, mezi které patří i dva jednorožci
- Other trackers differ widely. VCBacked lists 90 companies (Credo Ventures has invested in 90 companies tracked in our database.), Seedtable shows 35 (Companies 35 with a disclosed round on file), and VCBeast shows only 3 (3 companies in Credo Ventures's investment portfolio.). The gaps probably reflect different tracking methods, though I can't confirm that.

**Notable holdings**
- **UiPath:** Credo's most successful investment, which it backed before the company listed on the stock exchange (Před vstupem na burzu jim byl původem rumunský UiPath, což byla pro Credo nejúspěšnější investice).
- **Productboard:** Currently the most valuable startup founded by Czech entrepreneurs in the portfolio (aktuálně nejhodnotnější startup českých zakladatelů Productboard).
- **ElevenLabs:** A Polish company whose latest funding round valued it above $11 billion (polský ElevenLabs s valuací z posledního kola přes jedenáct miliard dolarů).
- **Other names:** Germany's Pricefx, plus the Czech companies ResistantAI, Deepnote, Manta and Better Stack (Mezi další velká jména pak patří německý Pricefx, české ResistantAI, Deepnote, Mant
… [skrátené, 2358 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.credoventures.com/portfolio",
  "prompt": "Return word-for-word, without summarising or translating, every line that names a portfolio company together with a round, stage, date or year (for example Pre-Seed, Seed, Series A, co-led, invested, led), and the page's publication date if shown. Also return any sentence mentioning Credo."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://ares.gov.cz/ekonomicke-subjekty-v-cr/rest/ekonomicke-subjekty/28538137",
  "prompt": "Return word-for-word the company name (obchodní firma), IČO, the registered office address (sídlo), and the date of incorporation (datum vzniku) if present. Return the exact text as it appears, without summarising or translating."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/novy-fond-odchod-andreje-kisky-i-tri-dalsi-partneri-v-credo-ventures-se-deji-velke-veci/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo, fond / fund, miliard / milionů (fund size), eur, korun, investic / investuje, ticket or investment size, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The web page content you provided contains only the word "ARES." It has no company name (obchodní firma), IČO, registered office address (sídlo), or date of incorporation (datum vzniku).

If you share the full text of the ARES record, I can extract those four fields exactly as they appear. You can also look up the company directly in the ARES public registry at ares.gov.cz by searching for its IČO or name.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
No line on the page names a specific portfolio company alongside a round, stage, date, or year, so there are no matching lines to return.

The page does show this publication date:

"Oct 6, 2026, 2:38 PM UTC"

These lines mention Credo:

"Portfolio | Credo"

"©2026 Credo Ventures."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date (as shown on the page):** "01. 11. 2022"

Sentences longer than 125 characters are split into shorter exact fragments, each under the limit.

**Intro and fund details**
- "Vybudovalo si pověst jednoho z nejlepších investičních fondů podporujících startupy v našem regionu"
- "nyní české Credo Ventures vstupuje do nové éry."
- "Oznámilo otevření již čtvrtého fondu,"
- "v němž má k dispozici celkem 75 milionů eur (1,8 miliardy korun)"
- "na investice do inovativních firem v raných fázích vývoje."
- "Od roku 2011 Credo vybudovalo portfolio o celkem 76 startupech"
- "Aktuálně pečuje o aktiva v celkové výši 250 milionů eur (6,1 miliardy korun)."
- "Svůj první fond ve výši 18 milionů eur otevíral v roce 2010,"
- "ve druhém z roku 2015 pak od investorů získal 53 milionů eur."
- "S třetím z roku 2019 dosáhl na objem bezmála 100 milionů eur,"
- "současný čtvrtý se 75 miliony eur je tak o čtvrtinu nižší."

**Founder and partner comments**
- "Fond jsme si začali kreslit koncem loňska, kdy byly časy ještě veselé."
- "Od začátku jsme ale věděli, že nechceme pokračovat v růstu objemu fondů."
- "Naopak jsme si říkali, že stomilionový třetí fond byl o něco větší, než měl být,"
- "že fond za poslední půlrok dokončil nejvíc investic ve své historii."
- "Zajímavostí je, že více než deset procent celkové částky do fondu vložili samotní partneři."
- "Do čtvrtého fondu peníze vložila známá jména"
- "Přidali se také institucionální investoři jako podfond RSJ Tech Libora Winklera,"
- "nebo globálně známé fondy Atomico, Sequoia Capital a Cendana Capital."
- "S novým fondem se pojí i personální změny."
- "Už asi pět let se znám s partnery fondu Honzou Habermannem a Andrejem Kiskou."
- "Nedávno kluci přišli s tím, že otevírají nový fond a hledají partnera."
- "Vždycky jsem na Credo nahlížela s velkým respektem, a protože už jsme se znali, tak jsme se dohodli celkem rychle."
- "Vedou fond dobrým směrem, mají tady vybudovanou super značku i portfolio."

**October news roundup**
- "Česko-slovenský startup Around přepsal rekordy – exitoval se za 250 až 300 milionů dolarů"
- "z tuzemských VC jej historicky podpořilo Credo Ventures."
- "když jej prodal za více než 100 milionů dolarů (2,5 miliardy korun) Googlu,"
- "Talkbase vybral přes dva miliony dolarů (přes 50 milionů korun) od fondů J&T Ventures a Credo Ventures,"
- "Český startup Tatum v Series A získává 41,5 milionu dolarů (1,05 miliardy korun)"
- "Český startup FTMO vyrazil na nákupy a za stovky milionů korun kupuje německého brokera JFD Brokers."
- "jeho valuace v transakci přesáhla 100 milionů korun."
- "otevírá svůj třetí andělský fond, cílí v něm na půl miliardy korun"
- "posílají pět milionů eur (122 milionů korun) do chorvatského startupu AdScanner."
- "Slovenský PE fond Sandberg Capital za jednotky milionů eur (100 až 200 milionů korun)"
- "Andělský fond Depo Ventures se spolupodílí na pre-seed ve výšce 3,4 milionu eur (83 milionů korun)"
- "již předtím startup získal 17 milionů korun od Startup W
… [skrátené, 2042 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://forbes.cz/zahajte-fazi-pet-credo-ventures-maji-paty-fond-za-temer-dve-miliardy-prim-bude-hrat-mladi/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo, fond / fondu (fund), miliard, miliard korun, milionů dolarů, investic / investovat, the number of projects per year, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Credo Ventures pre-seed round led 2026",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page content contains only a headline, with no body text and no publication date. The headline mentions Credo and a fund, and it refers to nearly two billion:

"Zahajte fázi pět! Credo Ventures mají pátý fond za téměř dvě miliardy, prim bude hrát mládí | Forbes"

It doesn't mention the number of projects per year or any investment or dollar figures beyond that.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Credo Ventures pre-seed round led 2026"

Links: [{"title":"Credo Ventures Research","url":"https://f4.fund/firms/credo-ventures"},{"title":"Credo Ventures lanza fondo de $88M para startups pre-seed en CEE","url":"https://ecosistemastartup.com/credo-ventures-lanza-fondo-de-88m-para-startups-pre-seed-en-cee/"},{"title":"Credo Ventures lanza fondo de $88M para startups pre-seed en CEE","url":"https://ecosistemastartup.com/?p=70677"},{"title":"Back to Credo Ventures","url":"https://seedtable.com/investors/credo-ventures/portfolio"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/credo-ventures"},{"title":"Prague And Krakow-Based Credo Ventures Raises $88M Fund 5 To Focus On CEE Pre-Seed Startups And Global Diaspora","url":"https://startuprise.co.uk/prague-and-krakow-based-credo-ventures-raises-88m-fund-5-to-focus-on-cee-pre-seed-startups-and-global-diaspora/"},{"title":"Investing Profile","url":"https://signal.nfx.com/investors/ondrej-bartos"},{"title":"Credo Ventures","url":"https://www.everythingstartups.com/vc-funds/credo-ventures"},{"title":"Updated: July 20, 2026","url":"https://incubatorlist.com/credo-ventures-stage-5"},{"title":"Credo Ventures Announces $88M Fund for CEE Founders","url":"https://www.startupresearcher.com/news/credo-ventures-announces-usd88-million-fund-for-cee-founders"}]

I couldn't find an announcement of a specific pre-seed round led by Credo Ventures in 2026. The search did turn up the firm's new fund and two 2026 deals that involve Credo, but only one is labeled as a lead, and that label comes from a third-party database.

**The fund:** Credo's fifth vehicle, Credo Stage 5, is an $88M fund explicitly targeting pre-seed. The plan calls for around thirty holdings, with roughly seven to eight new investments added each year. The sources disagree on timing. One says the fund closed in March 2026, while Startup Researcher described the March announcement as the first close of the fund at its $88 million target.

**2026 deals with Credo involvement:**
- **SuperPlane:** Seedtable's portfolio listing shows Credo with a "Lead" tag on this open-source company, at the pre-seed stage, dated 24 June 2026. The listing's $2.6M figure is the company's total raised, not the size of Credo's round, which isn't broken out.
- **Theorema:** NFX's profile for Credo General Partner Ondrej Bartos lists a $3M pre-seed round dated March 2026. The profile doesn't say whether Credo led it.

Both leads come from third-party databases, not company announcements or Credo's own site. To confirm the SuperPlane or Theorema lead roles, I'd need to search for announcements from those companies or from Credo directly. Would you like me to do that?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://startuprise.co.uk/prague-and-krakow-based-credo-ventures-raises-88m-fund-5-to-focus-on-cee-pre-seed-startups-and-global-diaspora/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo, fund / Fund 5, $88M / 88 million, pre-seed, portfolio companies, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Credo Ventures seed funding round press release 2025 investors include Credo Ventures",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "Mar 24, 2026"

**Headline:** "Prague And Krakow-Based Credo Ventures Raises $88M Fund 5 To Focus On CEE Pre-Seed Startups" (the fund and pre-seed focus, paraphrased: Credo raised an $88M fifth fund aimed at CEE pre-seed startups.)

**Fund and $88M:**
- "Credo Ventures has launched Credo Stage 5, an $88 million fund" (The firm has launched its fifth fund, sized at $88 million.)

**Credo background and pre-seed focus:**
- "Founded in 2010 and based in Prague and Krakow, Credo Ventures invests at the earliest stages" (Credo was founded in 2010, is based in Prague and Krakow, and invests very early.)
- "The firm is strengthening its presence in the Pre-Seed niche" (Credo is expanding its pre-seed focus.)

**Fund partners:**
- "The fund's partners include Maciek Gnutek, Jakub Krikava, Max Kolowrat-Krakowsky, Matej Micek" (The article names six partners, including Gnutek, Krikava, Kolowrat-Krakowsky, and Micek, plus two others.)

**Portfolio companies:**
- "Over 15 years and across four funds, Credo has backed more than 100 companies, including two decacorns" (Over 15 years and four funds, Credo has backed more than 100 companies, two of them decacorns.)
- "led pre-seed rounds for rapidly growing, category-defining CEE companies such as UiPath and ElevenLabs" (Credo led pre-seed rounds for fast-growing regional companies, including UiPath and ElevenLabs.)
- "where Credo was the first cheque and (co-)lead investor in both cases" (Credo was the first investor and a co-lead in both UiPath and ElevenLabs.)

**Fund focus:**
- "Credo Stage 5 continues the firm's focus on first-cheque investments" (The new fund continues Credo's focus on being the first investor in founders' companies.)
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Credo Ventures seed funding round press release 2025 investors include Credo Ventures"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/credo-ventures"},{"title":"Credo Ventures Research","url":"https://f4.fund/firms/credo-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/credo-ventures"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/wanderwallet"},{"title":"Back to Credo Ventures","url":"https://seedtable.com/investors/credo-ventures/portfolio"},{"title":"Credo Ventures lanza fondo de $88M para startups pre-seed en CEE","url":"https://ecosistemastartup.com/?p=70677"},{"title":"Credo Ventures lanza fondo de $88M para startups pre-seed en CEE","url":"https://ecosistemastartup.com/credo-ventures-lanza-fondo-de-88m-para-startups-pre-seed-en-cee/"},{"title":"How Much Did Credo AI Raise? Funding & Key Investors","url":"https://www.clay.com/dossier/credo-ai-funding"},{"title":"credo ventures","url":"https://www.vcbacked.co/directory/investors/credo-ventures"}]

Links: [{"title":"Forsal logo","url":"https://forsal.pl/artykuly/1458609,fundusz-credo-ventures-planuje-zainwestowac-prawie-100-mln-usd-w-cee.html"},{"title":"prague based vc credo ventures plans to invest e88m in central eastern europe startups","url":"https://siliconcanals.com/prague-based-vc-credo-ventures-plans-to-invest-e88m-in-central-eastern-europe-startups/"},{"title":"Credo Ventures Closes New €34 Million Fund Targeting Central Europe","url":"https://techcrunch.com/?p=1149521"},{"title":"Credo Ventures lanza fondo de $88M para startups pre-seed en CEE","url":"https://ecosistemastartup.com/credo-ventures-lanza-fondo-de-88m-para-startups-pre-seed-en-cee/"},{"title":"Credo Ventures lanza fondo de $88M para startups pre-seed en CEE","url":"https://ecosistemastartup.com/?p=70677"},{"title":"Credo Ventures - nová príležitosť aj pre slovenské startupy v objeme 34 miliónov eur","url":"https://www.podnikajte.sk/investor/credo-ventures-prilezitost-startupy"},{"title":"Tobias Fyen","url":"https://no.linkedin.com/in/tobias-fyen"},{"title":"Credo Ventures se podařil první velký exit: Cognitive Security","url":"https://www.lupa.cz/clanky/credo-ventures-exit-cognitive-security/"},{"title":"Credo Ventures Closes 4th Fund at €75M","url":"https://podim.org/credo-ventures-closes-4th-fund-at-e75m/"}]

Links: [{"title":"seed 2025 01","url":"https://seedtable.com/companies/axoflow/funding-rounds/seed-2025-01"},{"title":"24051 cytowski and partners advises axoflow on usd 2 5 million seed round","url":"https://ceelegalmatters.com/hungary/24051-cytowski-and-partners-advises-axoflow-on-usd-2-5-million-seed-round"},{"title":"24051 cytowski and partners advises axoflow on usd 2 5 million seed round","url":"https://ceelegalmatters.com/by-practice/24051-cytowski-and-partners-advises-axoflow-on-usd-2-5-million-seed-round"},{"title":"24051 cytowski and partners advises axoflow on usd 2 5 million s
… [skrátené, 2904 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://ain.ua/2025/01/23/axoflow-raises-7m",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo Ventures, e2vc, EBRD, the round size, the lead investor, Axoflow, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.podnikatel.cz/rejstrik/credo-ventures-a-s-28538137/",
  "prompt": "Return word-for-word, without summarising or translating, the company name (obchodní firma / název), the IČO, the registered office (sídlo), the date of establishment (datum vzniku) and the commercial register file reference (spisová značka) exactly as shown on the page."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "SuperPlane raises pre-seed Credo Ventures",
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
- **Obchodní firma / název:** Credo Ventures a.s.
- **IČO:** 28538137
- **Sídlo:** Karlovo náměstí 2097/10, Praha Nové Město (Praha 2), 120 00
- **Datum vzniku:** 2. 3. 2009
- **Spisová značka:** B 15102, Městský soud v Praze
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "SuperPlane raises pre-seed Credo Ventures"

Links: [{"title":"SuperPlane Raises 2.6M USD in Pre Seed Funding","url":"https://seedtable.com/companies/superplane/funding-rounds/pre-seed-2026-06"},{"title":"SuperPlane Raises $2.6 Million in Pre-Seed Funding","url":"https://raising.fi/news/superplane-pre-seed-june-2026"},{"title":"Sredstva idu domaćem startapu","url":"https://biznis.rs/vesti/srbija/obezbedjeno-26-miliona-dolara-za-razvoj-ai-platforme-za-automatizaciju-inzenjerskih-procesa/"},{"title":"Investors Count","url":"https://www.cbinsights.com/company/superplane/financials"},{"title":"parsers.vc","url":"https://parsers.vc/startup/superplane.com/"},{"title":"Subscribe to Our Newsletter","url":"https://thesaasnews.com/news/superplane-raises-2-28m-pre-seed"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/superplane"},{"title":"About SuperPlane","url":"https://fundup.ai/recently-funded-startups/company/1f423b4288dee13eb373f5d1c7cb82f5c543f967ba1e6035833419ec9e1f9a7b/superplane"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/superplane"}]

Yes. Several sources report that SuperPlane closed a pre-seed round led by Credo Ventures, with the round dated to June 24, 2026.

- **Amount:** Seedtable tallies the raise at $2.6 million, with Credo Ventures at the helm. TheSaaSNews reports the same company as having secured €2.28 million in pre-seed funding. The two figures look like one round in different currencies, though I haven't verified the exchange rate.
- **Date:** CB Insights dates the latest round to June 24, 2026.
- **Investors:** Credo Ventures headed the round, and First Momentum Ventures joined as a participant. Among the angels, TheSaaSNews names Stanislas Polu, Mirko Novakovic, Tomas Kratky and Andreas Klinger. Investor lists differ by source. CB Insights counts twelve investors in total.
- **What it does:** The product is pitched as an open-source hub where engineers and AI agents share production workflows. By Seedtable's count, it connects to more than 30 tools and includes over 300 components.
- **Founders and base:** The company was founded in 2025 by CEO Darko Fabijan and CPO Marko Anastasov. Parsers.vc describes it as a San Francisco-based developer with Serbian founding roots.
- **Use of funds:** According to TheSaaSNews, the money is earmarked for speeding up the product, forging more partnerships, widening the open-source following, and offering a cloud-hosted option.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://raising.fi/news/superplane-pre-seed-june-2026",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo Ventures, the lead investor, the round size, the round date / month, SuperPlane, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Here are the relevant items from the page. Because of the 125-character limit on quotes, I've quoted only fragments of longer sentences and paraphrased the rest.

**Headline (title, quoted):**
- "SuperPlane Secures $2.6 Million in Pre-Seed Funding Led by Credo Ventures"

**Round size, SuperPlane, and lead investor:**
- "SuperPlane, an AI-driven platform engineering startup, has successfully raised $2.6 million in a Pre-Seed funding round." (The article says SuperPlane closed a $2.6 million pre-seed round.)
- "The round was led by Credo Ventures, with participation from First Momentum Ventures" (The round was led by Credo Ventures, with First Momentum Ventures also participating, plus several angel investors.)

**Lead investor's role in the investor section:**
- "Credo Ventures, the lead investor," (The article notes that Credo Ventures is the lead investor and names other backers who show confidence in SuperPlane.)

**SuperPlane's direction:**
- "As SuperPlane continues to innovate in the field of AI-driven platform engineering" (The article says the round is a step toward SuperPlane's mission of simplifying and securing operational processes for engineering teams.)

**Publication date:**
- "June 25, 2026" (The article was published on June 25, 2026, and is listed as a two-minute read.)
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://en.ain.ua/2025/01/23/axoflow-raises-7m",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Credo Ventures, e2vc, EBRD, the round size, the lead investor, Axoflow, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "23 January, 2025, 09:02"

**Axoflow**
- "Axoflow, a Hungarian-founded and US-based cybersecurity startup, has secured a $7 million investment" for its security data curation pipeline.
- "Axoflow is a US-based company founded by Balázs Scheidler, Ferenc Hernádi, Sándor Guba and Neil Boyd."
- "Axoflow helps businesses across various industries strengthen their security posture"
- "Axoflow provides the intelligence layer that empowers cybersecurity professionals with greater control"
- "The new funding will be used to further develop Axoflow's pioneering security data curation pipeline"

**Round size and lead investor**
- "The round was led by EBRD Venture Capital" and "all existing major investors, Credo Ventures and e2vc, have also significantly increased their stakes."
- The article also says "The round was led by EBRD Venture Capital, with partisipate from all existing major investors" and "Credo Ventures and e2vc, have significantly increased their stakes in the company."

**EBRD Venture Capital**
- "EBRD Venture Capital, part of the European Bank for Reconstruction and Development (EBRD), invests in innovative" startups and scale-ups across diverse sectors and regions.
- "The firm is stage-agnostic, investing in both early and growth-stage companies" "with ticket sizes ranging from €2 million to €25 million over the life of the investment."
- The article quotes Yalcin Gungoren, who spoke "at EBRD Venture Capital."
- "Previously, AIN informed that EBRD Venture Capital invested $12 million to Slovak-founded startup Brightpick."

**Credo Ventures and e2vc**
- "Credo Ventures, a Prague-based venture capital company focused on early stage investments in Central Europe" or, occasionally, the US.

Several sentences are longer than the 125-character limit, so I split them into separate quoted fragments. The text between quotes is my own wording.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Investown, investice / investovat, portfolio, projekty, fond, ticket / minimální investice, company name with s.r.o., IČO, sídlo / adresa, kontakt, the business model (crowdfunding, půjčky, nemovitosti, realitní), and the page's publication date if shown."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Investown Technologies s.r.o. IČO",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Investown investice do startupů fond",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce every matching sentence word-for-word, but here are the relevant passages from the page, quoted within the 125-character limit. Other details are paraphrased.

**Company and business model**
- Company name: "Informace na webových stránkách a v propagačních materiálech společnosti Investown Technologies s.r.o." (the legal entity is Investown Technologies s.r.o.)
- Business model: "Investown je online platforma s investičními úvěry do nemovitostí." The platform offers real-estate-backed loans to developers, and investors fund them through projects.
- Licence: "Jsme držitel ČNB licence." The page links to a Czech National Bank licence document.

**Projects and investing**
- Projects are offered on the platform and investors can pick from open opportunities or the Marketplace (Tržiště).
- "Investice se přidá do vašeho portfolia." Investments are added to the investor's portfolio.
- Each project is funded to its full target amount before the security documentation is signed and returns begin.

**Minimum investment**
- "Nejmenší investovatelná částka je 500 Kč, nejvyšší je 50 000 000 Kč." The minimum is 500 CZK and the maximum is 50,000,000 CZK.

**Risk disclaimer**
- "Investice do projektu skupinového financování představuje riziko ztráty veškerých investovaných peněz." Investing in a group-financing project carries a risk of losing all invested money.

**Other entities**
- The blog mentions a closed family investment fund, Palatinum, as a third-party developer client. It is not part of Investown's own structure.

**Not on the page**
- No IČO (company registration number) or registered office address appears in the content.
- No direct contact details appear; there is only a "Kontakt" link to /kontakt.
- The page has no publication date. The footer copyright year is an unfilled template placeholder. The most recent dated items are blog posts from 2026-10-22, 2026-10-01 and 2026-09-10.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Investown investice do startupů fond"

Links: [{"title":"nas nezivi poplatky od investoru nas plati developer rika sef spolecnosti investown alan pock","url":"https://www.newstream.cz/leaders/nas-nezivi-poplatky-od-investoru-nas-plati-developer-rika-sef-spolecnosti-investown-alan-pock"},{"title":"ČNB čistí trh od šedé zóny. Pokutu milion korun udělila crowdfundingu Investown, fungování již změnil","url":"https://cc.cz/cnb-cisti-trh-od-sede-zony-pokutu-milion-korun-udelila-crowdfundingu-investown-fungovani-jiz-zmenil/"},{"title":"Přes Investown do nájemních bytů proteklo za dva měsíce 20 milionů korun. Poptávka je obrovská, hlásí zakladatelé","url":"https://cc.cz/pres-investown-do-najemnich-bytu-proteklo-za-dva-mesice-20-milionu-korun-poptavka-je-obrovska-hlasi-zakladatele/"},{"title":"Lidé mu na investice do nemovitostí svěřili 1,7 miliardy. Investown teď získal desítky milionů na expanzi","url":"https://cc.cz/lide-mu-na-investice-do-nemovitosti-sverili-17-miliardy-investown-ted-ziskal-desitky-milionu-na-expanzi/"},{"title":"cc.cz","url":"https://cc.cz/tag/investown/"},{"title":"Násobně rostl a překlopil se do zisku. Investown zažil podařený rok, měsíčně profinancuje 300 milionů","url":"https://cc.cz/nasobne-rostl-a-preklopil-se-do-zisku-investown-zazil-podareny-rok-mesicne-profinancuje-300-milionu/"},{"title":"Investice do nemovitostí Čechy lákají. Startup Investown roste a miliony mu posílá Chytrý Honza","url":"https://cc.cz/investice-do-nemovitosti-cechy-lakaji-startup-investown-roste-a-miliony-mu-posila-chytry-honza/"},{"title":"Investown loni profinancoval 3,7 miliardy. V obratu vyrostl více než dvojnásobně, hlásí i zisk","url":"https://cc.cz/investown-loni-profinancoval-37-miliardy-v-obratu-vyrostl-vice-nez-dvojnasobne-hlasi-i-zisk/"},{"title":"Startup Investown dostal zelenou od ČNB. Licence mu otevírá cestu do George České spořitelny","url":"https://cc.cz/startup-investown-dostal-zelenou-od-cnb-licence-mu-otevira-cestu-do-george-ceske-sporitelny/"}]

**Short answer:** Investown is not a startup fund. It's a Czech platform for real-estate investing. The "investment into startups" angle in your query most likely refers to the funds and investors that backed Investown itself, mainly Česká spořitelna's Seed Starter and Lighthouse Ventures.

**What Investown does**
The platform lets people share in funding developers' property loans and earn interest of about 10% a year. Investown lidem umožňuje podílet se na investování do úvěrů z nemovitostí. Lidé vloží peníze do úvěru pro developerské projekty a následně profitují z úrokového výnosu pohybujícího se na úrovni kolem deseti procent ročně. Its app can be used with small amounts, starting from a few hundred crowns (Aplikaci pro investování do rezidenčních nemovitostí, kdy lidem stačí i stovky korun, spustil český startup Investown).

**Who funded Investown**
- **Seed Starter (Česká spořitelna):** This is a fund that spadá pod Českou spořitelnu. Together with Lighth
… [skrátené, 2511 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Investown Technologies s.r.o. IČO"

Links: [{"title":"Smlouvy Dotace Platy Úřady Zakázky Sponzoři & firmy","url":"https://www.hlidacstatu.cz/subjekt/08667144"},{"title":"www.jobs.cz","url":"https://www.jobs.cz/rpd/2001234815/?rps=233"},{"title":"S Sp 2022 00074 CNB 572","url":"https://www.cnb.cz/export/sites/cnb/cs/dohled-financni-trh/.galleries/prilohy/S-Sp-2022_00074_CNB_572.pdf"},{"title":"S Sp 2021 00246 CNB 573","url":"https://www.cnb.cz/export/sites/cnb/cs/dohled-financni-trh/.galleries/prilohy/S-Sp-2021_00246_CNB_573.pdf"},{"title":"Legal Entity Identifier (LEI)","url":"https://lei.bloomberg.com/leis/view/315700LH8EENA58RXF85"},{"title":"Marcela Pinkasová","url":"https://www.investown.cz/en/kontakt"},{"title":"24493 havel partners advises ceska sporitelna seed starter on sale of stake in investown technologies","url":"https://mail.ceelegalmatters.com/by-practice/24493-havel-partners-advises-ceska-sporitelna-seed-starter-on-sale-of-stake-in-investown-technologies"},{"title":"24493 havel partners advises ceska sporitelna seed starter on sale of stake in investown technologies","url":"https://ceelegalmatters.com/by-practice/24493-havel-partners-advises-ceska-sporitelna-seed-starter-on-sale-of-stake-in-investown-technologies"},{"title":"investown in 2022 annual review","url":"https://www.investown.cz/en/post/investown-in-2022-annual-review"},{"title":"app.dealroom.co","url":"https://app.dealroom.co/companies/investown"}]

The IČO for Investown Technologies s.r.o. is **08667144**. Official documents sometimes write it as 086 67 144.

Other sources confirm the number and give related details:

- **Founding date:** Hlídač státu's company profile lists the same IČO and dates the company's founding to 6 November 2019. Založeno 06.11.2019 IČO 08667144
- **Registered seat:** Czech National Bank decisions tie the number to a seat at Inovační 122, Hodkovice, 252 41 Zlatníky-Hodkovice. Investown Technologies s.r.o., IČO 08667144, se sídlem Inovační 122, Hodkovice, 252 41 Zlatníky-Hodkovice
- **Legal form:** The Bloomberg LEI record shows the same registry number and identifies the entity as a limited liability company (společnost s ručením omezeným). Its Legal Entity Identifier is 315700LH8EENA58RXF85. LEI: 315700LH8EENA58RXF85
- **Company website:** The English contact page gives the ID 08667144 and a tax ID, CZ699007573. It also gives a commercial register reference, section C, file 322874, kept by the Prague Municipal Court. ID: 08667144 TAX ID: CZ699007573 That page calls the firm "Investown Technologies Ltd.", which is an English rendering of the Czech s.r.o. form.

Regulatory history also appears in the CNB records:

- A 2022 CNB decision granted the company permission to operate as a crowdfunding service provider under the EU ECSPR regulation, covering loan facilitation. Společnosti Investown Technologies s.r.o., IČO 08667144, se sídlem Inovační 122, Hodkovice, 252 41 Zlatníky-Hodkovice, se podle čl. 12 odst. 8 naří
… [skrátené, 743 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/cnb-cisti-trh-od-sede-zony-pokutu-milion-korun-udelila-crowdfundingu-investown-fungovani-jiz-zmenil/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Investown, ČNB / národní banka, pokuta / milion korun, licence, povolení, šedé zóny, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/startup-investown-dostal-zelenou-od-cnb-licence-mu-otevira-cestu-do-george-ceske-sporitelny/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Investown, licence / licenci, ČNB, George, Česká spořitelna, crowdfunding, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz/blog",
  "prompt": "Return word-for-word, without summarising or translating, the titles and dates of the most recent blog posts or news items listed on the page, and every sentence that names a project, developer (developer / projekt / výstavba), a loan amount or a funded project, together with the date shown."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Note: Quotes are capped at 125 characters, so longer sentences are truncated and marked with "…". Quotes are in the original Czech.

**Publication date**
- "24. 10. 2023 – 1 min čtení"

**Headline**
- "Startup Investown dostal zelenou od ČNB. Licence mu otevírá cestu do George České spořitelny"

**Article body**
- "Platforma pro investice do nemovitostí je první, která získala novou evropskou crowdfundingovou licenci."
- "Po ročním odkladu se blíží začátek platnosti nové regulace, podle níž od listopadu musejí mít všichni poskytovatelé…"
- "Jako první tuto licenci u nás ve svém oboru získal Investown, jenž umožňuje skupinové investování do nemovitostí…"
- "Startup již dříve finančně podpořila Česká spořitelna, která se jej teď chystá více začlenit do svých produktů."
- "Licence nám umožní působit nejen v domovském Česku, ale i v dalších státech Evropské unie, čímž se nám…"
- "Dokument zároveň může otevřít cestu k dalšímu výraznému škálování v podobě hlubší integrace do České spořitelny…"
- "Licence, kterou platforma od ČNB získala, je velkým milníkem nejen pro Investown."
- "Vnímáme ji jako jasný signál pro prohlubování a posilování vzájemné spolupráce a rádi bychom crowdfundingové…"
- "Investown vznikl v roce 2019 a byl spuštěn v roce 2021."
- "Investown lidem umožňuje podílet se na investování do úvěrů z nemovitostí."
- "Novou licenci přitom startup od České národní banky získával více než rok."

**Captions and tags**
- "Foto: Investown"
- "Vedení startupu Investown"
- "Související témata: Česká spořitelna, Seed starter, Investown"
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
I can't reproduce every sentence in full because quotes are capped at 125 characters. Below, each relevant sentence is quoted in Czech (trimmed where needed) or paraphrased in English.

**Publication date:** "17. 2. 2023"

**Investown, ČNB, fines, licences, and permits**

1. Headline: "ČNB čistí trh od šedé zóny. Pokutu milion korun udělila crowdfundingu Investown, fungování již změnil"
2. "Platformy nabízející investiční crowdfunding budou muset mít od listopadu licenci." (Crowdfunding platforms must hold a licence from November.)
3. "Od listopadu budou muset mít pro svůj provoz povolení od České národní banky" (From November, platforms need a permit from the Czech National Bank, which the lawyer says had already begun cleaning up the market.)
4. "V lednu proto potvrdila pokutu platformě Investown, jež se zaměřuje na nemovitosti." (In January the CNB confirmed a fine against Investown, a real-estate-focused platform.)
5. "ČNB se nyní snaží vyčistit trh od šedé zóny crowdfundingových poskytovatelů" (The CNB is now trying to clear the grey zone of crowdfunding providers.)
6. "Rozhodnutí o udělení milionové pokuty může být vnímáno jako kontroverzní" (A decision to impose a million-crown fine may be seen as controversial.)
7. "Investown původně nabízel participaci na úvěrech, podle ČNB tím ale provozoval takzvaný pokoutný investiční fond" (Investown originally offered loan participations, which the CNB said amounted to running an unlicensed investment fund.)
8. "Investown již přitom nyní tento model nenabízí, své fungování změnil na úvěrový crowdfunding." (Investown no longer offers that model and has switched to loan-based crowdfunding.)
9. "ČNB vůči platformě zahájila správní řízení loni v březnu" (The CNB opened administrative proceedings against the platform in March last year.)
10. "Firma ho podle vyjádření pro CzechCrunch plně respektuje a výši pokuty považuje za adekvátní." (The company says it fully respects the decision and considers the fine appropriate.)
11. Alan Pock is described as co-founder and director of Investown.
12. "Na dotaz, jak se vlastně stalo, že Investown neměl potřebnou licenci od ČNB" (Asked how Investown lacked the required CNB licence, Pock said the model was unregulated when the platform started.)
13. "To se změní od 10. listopadu, kdy začne platit pravidlo, že musí mít povolení ČNB." (From 10 November, platforms must hold a CNB permit.)
14. "S tímto výkladem ČNB nesouhlasí" (The CNB disagrees with Investown's legal interpretation.)
15. "Investown přitom není jediným ze zástupců startupů na poli finančních technologií, kterému ČNB udělila pokutu." (Investown is not the only fintech startup the CNB has fined.)
16. "Loni ji ve výši 150 tisíc korun za překračování své licence" (Last year Fondee was fined 150,000 CZK for exceeding its licence.)
17. "Upvest, narozdíl od zmiňovaného Investownu, pro svůj obchodní model a právní nastavení" (Upvest says, unlike Investown, it has held a CNB licence since its founding.)
18. "Upve
… [skrátené, 547 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Nejnovější položky (podle data uvedeného na stránce)**

- 2026-10-22: „Mgr. Pavel Procházka: „K Investownu jsme se dostali náhodou. A vracíme se, protože to funguje"
- 2026-10-01: „„Investown nám přinesl flexibilní a rychlé financování," hodnotí spolupráci ALZATA s.r.o."
- 2026-09-10: „M.E estates s.r.o.: „Díky pohotovému financování jsme mohli zahájit stavbu hned po akvizici projektu“"
- 2026-06-21: „Nový Premium benefit: 30% sleva na pobyt v projektu, který vznikl i díky Investownu"

**Věty o projektech, developerech, úvěrech a financovaných projektech**

- **2026-10-22** (Pavel Procházka): Řídí fond Palatinum, který se věnuje výstavbě bytových domů. Podle něj jde o „Mgr. Pavel Procházka řídí rodinný uzavřený investiční fond Palatinum zaměřený na výstavbu bytových domů". Po dvou zafinancovaných projektech hodnotí spolupráci kladně.
- **2026-10-01** (ALZATA s.r.o.): Developerská společnost financovala přes platformu dokončení rodinných domů Sluneční terasy v Březnici u Zlína. Věta: „financovala dokončení projektu Rodinné bydlení Sluneční terasy v Březnici u Zlína."
- **2026-09-10** (M.E estates s.r.o.): Projekt Solis Residence, známý mezi investory jako Bytový dům Praha-Holubova, vzniká na Smíchově. Věta: „vzniká Solis Residence, kterou investoři znají pod názvem projektu Bytový dům Praha-Holubova."
  - Za projektem stojí „Za projektem stojí společnost Dům Holubí s.r.o."
  - Úvěr: „úvěr ve výši 120 milionů Kč"
  - Po dokončení nabídne „po dokončení nabídne 21 bytových jednotek"
- **2026-06-21**: Premium benefit zahrnuje slevu na pobyt v „30% sleva na pobyt v komplexu Apartmány Mlýn Herlíkovice", který vznikl i díky financování přes Investown.
- **2026-02-01**: Poprvé byly rozděleny finance z dražby v rámci vymáhání projektu „v rámci vymáhání projektu Apartmány Boží Dar".
- **2025-09-11** (rozhovor FocusOn): Investown ročně profinancuje projekty v hodnotě „ročně profinancuje projekty v hodnotě stovek milionů korun".
- **2025-08-25**: Apartmánový resort Andělská Hora vzniká z lodních kontejnerů v Jeseníkách. Investoři vybrali „vybrali 32 milionů korun za necelé čtyři hodiny".
- **2025-08-05** (Marian Stoyanov): Podnikatel získal finance na „získal finance na 4 projekty ve výši téměř 44 milionů korun".
- **2025-07-18** (HANDEL STAV HOME s.r.o.): Projekt z lodních kontejnerů získal „cílovou částku ve výši 32 milionů proinvestovali za rekordní 3,5 hodiny".
- **2025-06-26** (NISEKO): Adam Kuchař je „zkušený developer a majitel společnosti NISEKO."
- **2025-04-29** (QB Economy): Firma financovala projekt „pro svůj projekt Vily Nové Dvory u Frýdku-Místku".
- **2024-10-31** (1&P Realis s.r.o.): Financování první fáze rezidenčních domů „pro první fázi výstavby rezidenčních domů v Kutné Hoře".
- **2024-05-31** (Rezidence Prokopské údolí): „Vlastník projektu Rezidence Prokopské údolí hledal rychlý a flexibilní způsob financování." Druhá tranše se financovala za 25 minut.
- **2024-03-18**: Projekt Gotthard Yard 2 přinesl některým investorům více než 26 % p
… [skrátené, 3 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz/kontakt",
  "prompt": "Return word-for-word, without summarising or translating, every line that gives the company name (with s.r.o.), IČO / ID, DIČ, registered office or address (sídlo / adresa / Praha / Hodkovice / Inovační), the commercial register reference (spisová značka / oddíl C), and contact details (e-mail, phone, office). Also state the page's date if shown."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cc.cz/pres-investown-do-najemnich-bytu-proteklo-za-dva-mesice-20-milionu-korun-poptavka-je-obrovska-hlasi-zakladatele/",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Investown, a project / projekt, developer, nájemní byty, 20 milionů, investic / investoři, úvěr, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.podnikatel.cz/rejstrik/investown-technologies-s-r-o-08667144/",
  "prompt": "Return word-for-word, without summarising or translating, the company name (obchodní firma / název), the IČO, the registered office (sídlo), the date of establishment (datum vzniku) and the commercial register file reference (spisová značka) exactly as shown on the page. If the page is not about this company, say so."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
- **Název (obchodní firma):** Investown Technologies s.r.o.
- **IČO:** 08667144
- **Sídlo:** Inovační 122, Zlatníky-Hodkovice Hodkovice, 252 41
- **Datum vzniku:** 6. 11. 2019
- **Spisová značka:** C 322874, Městský soud v Praze
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page shows no date. The footer reads "Copyright © {current-year} Investown", which is an unfilled template placeholder.

**Company name:**
- "Investown Technologies s.r.o."

**Address / registered office:**
- "Inovační 122, Hodkovice, 252 41 Zlatníky-Hodkovice"

**IČO / DIČ:**
- "IČO: 08667144"
- "DIČ: CZ699007573"

**Commercial register:**
- "Společnost je zapsaná v obchodním rejstříku vedeném Městským soudem v Praze, oddíl C, vložka 322874"

**Contact details:**
- "Kontaktujte nás na e-mailové adrese support@investown.cz" (customer care contact: Marcela Pinkasová, Zákaznická péče)

No phone number or separate office address is listed.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Publication date:** "23. 6. 2021"

**Sentences mentioning the requested terms** (the 125-character limit means these are excerpts, not full sentences):

1. Headline: "Přes Investown do nájemních bytů za 2 měsíce proteklo 20 milionů korun"
2. "Když spoluzakladatelé Investownu Alan Pock Vyšín a Filip Suk v polovině letošního dubna otevírali tuto platformu"
3. "Nakonec však oba ukazatele Investown překonal pětinásobně"
4. "před dvěma týdny se pak podařilo překonat hranici 20 milionů korun."
5. "Investown tak v týdnech po ostrém spuštění získal desítky milionů korun, za které může nakupovat další nemovitosti"
6. "a umožní do ní investovat investorům, kteří následně dostávají každý měsíc poměrovou část z nájmu."
7. "i od Upvestu, kde mohou uživatelé investovat přímo do developerských projektů."
8. "Samotný Investown si na svůj provoz nechává deset procent nájmu"
9. "Pock vysvětluje, že v takovém případě by Investown nedosáhl na bankovní financování."
10. "Aktuálně po dvou měsících od otevření platformy Investown vlastní deset nemovitostí"
11. "Předtím, než dojde k zahraniční expanzi, však Investown bude nejdřív muset splnit několik základních cílů"
12. "Právě tímto směrem se chce Investown ubírat"
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Investown Solis Residence Dům Holubí s.r.o. úvěr 120 milionů",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Investown Andělská Hora apartmány financování projektu developer",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Investown Solis Residence Dům Holubí s.r.o. úvěr 120 milionů"

Links: [{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/bytovy-dum-praha-holubova-transe-2-transe-2-457-etapa-3"},{"title":"Finished project","url":"https://www.investown.cz/en/nemovitosti/bytovy-dum-praha-holubova-transe-2-transe-2-457-etapa-2"},{"title":"Jsme ten rozdíl, jestli budete mít v důchodu hezké peníze. Alan Pock o svém projektu Investown","url":"https://www.echo24.cz/a/HTB9x/zpravy-ekonomika-ten-rozdil-duchod-hezke-penize-alan-pock-investown"},{"title":"Private housing","url":"https://praha.camp/en/prague-tomorrow/project/solis-residence"},{"title":"Finished project","url":"https://www.investown.cz/en/nemovitosti/bytovy-dum-b-rezidence-lesik-1-384-etapa-7"},{"title":"marian stoyanov at investown i have confidence i am comfortable with the human approach","url":"https://www.investown.cz/en/post/marian-stoyanov-at-investown-i-have-confidence-i-am-comfortable-with-the-human-approach"},{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/rezidence-v-opave-2-548-etapa-1"},{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/rezidence-hlavackova-transe-12-105-etapa-1"},{"title":"Evaluation of corporate capital","url":"https://www.investown.cz/en/zhodnoceni-firemniho-kapitalu"}]

Links: [{"title":"solis rezidence","url":"https://www.praha.camp/en/prague-tomorrow/project/solis-rezidence"},{"title":"Solis Residence – Profitable Investment in a Premium Complex in Batumi by the Black Sea Coastline | Property Georgia","url":"https://propertygeorgia.ge/en/news/solis-residence-profitable-investment-premium-complex-batumi-black-sea-coastline"},{"title":"Connect with us on WhatsApp","url":"https://rocksinvestments.com/properties/solis-residence-556081"},{"title":"ban can ho chung cu the sol residence","url":"https://batdongsan.com.vn/ban-can-ho-chung-cu-the-sol-residence"},{"title":"details 14926154","url":"https://www.bayut.com/es/property/details-14926154.html"},{"title":"CHAIRMAN: DR. KHALID BIN THANI AL THANI","url":"https://thepeninsulaqatar.com/article/15/10/2015/Investcorp-adds-$400m-to-US-property-portfolio"},{"title":"multiple units high roi guaranteed appr 2 340076","url":"https://dubai.dubizzle.com/property-for-sale/residential/apartment/2026/7/29/multiple-units-high-roi-guaranteed-appr-2-340076/"},{"title":"apartment for sale dubai sobha solis motor city sobha solis tower b 124726112","url":"https://www.propertyfinder.ae/en/plp/buy/apartment-for-sale-dubai-sobha-solis-motor-city-sobha-solis-tower-b-124726112.html"},{"title":"multiple pool park views luxury apartme 2 298850","url":"https://uae.dubizzle.com/en/property-for-sale/residential/apartment/2026/4/29/multiple-pool-park-views-luxury-apartme-2-298850/"}]

Links: [{"title":"Finished project","url":"https://www.investown.cz/en/nemovitosti/bytovy-dum-praha-holubova-transe-2-transe-2-457-etapa-2"},{"title":"
… [skrátené, 3027 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Investown Andělská Hora apartmány financování projektu developer"

Links: [{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/apartmany-andelska-hora-transe-2-421-etapa-1"},{"title":"jakub zaviacic from handel stav home at investown i appreciate the speed and the overall approach","url":"https://www.investown.cz/en/post/jakub-zaviacic-from-handel-stav-home-at-investown-i-appreciate-the-speed-and-the-overall-approach"},{"title":"investors raised tens of millions in a few hours for an apartment resort from shipping containers","url":"https://www.investown.cz/en/post/investors-raised-tens-of-millions-in-a-few-hours-for-an-apartment-resort-from-shipping-containers"},{"title":"Finished project","url":"https://www.investown.cz/en/nemovitosti/apartmany-kvilda-transe-3-276-etapa-1"},{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/apartmany-kvilda-transe-4-207-etapa-1"},{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/kvilda-apartmany-kvilda-2-1-etapa-110"},{"title":"Profinancovaný projekt","url":"https://www.investown.cz/en/nemovitosti/four-elements-transe-5-652-etapa-1"},{"title":"Finished project","url":"https://www.investown.cz/en/nemovitosti/apartmany-klecanda-transe-6-213-etapa-1"},{"title":"Finished project","url":"https://www.investown.cz/en/nemovitosti/strazne-apartmany-klecanda-5-1-etapa-79"}]

Investown's own pages describe a crowdfunded financing round for the Andělská Hora apartment project in the Jeseníky region. Almost all of this material is promotional, and I found no independent sources.

**Developer**
According to the testimonial, a subsidiary, TRADE STAV HOME s.r.o., runs the project, which is the company's first development of its own, under the baton of a subsidiary TRADE STAV HOME s.r.o. now Jakub Zaviačič with his colleagues is building his first own development project Apartments Andelska Hora.

**Why they used Investown**
The company's representative says that for our first development project for about 65 [million] CZK, the negotiations with the classic bank seemed lengthy and difficult, including unsatisfactory conditions. Per the same testimonial, the full CZK 32 million was drawn in under four hours (withdrawal of the entire amount of 32 million. CZK didn't even last 4 hours.). Signing came right after the liens were recorded at the land registry (after the transcription of the liens on the Land Registry, it was also immediately inked).

**Stage 1 terms (Apartmány Andělská Hora 2)**
The listing shows a total stage value of CZK 8,174,400, collateral valued at CZK 62,076,000, a 65% loan-to-value ratio, a 14-month maturity, and a 7.2% annual yield (Yield 0.072... Total value 8174400... Guaranteed by value 62076000... LTV 0.65, Maturity 14 months, Purpose construction, business_development). The listing also says that after full funding, the borrower has 14 months to repay principal, backed by a notarial d
… [skrátené, 1511 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz/en/post/investors-raised-tens-of-millions-in-a-few-hours-for-an-apartment-resort-from-shipping-containers",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that names the developer / borrower company (s.r.o. or company name), the project name, the amount raised (CZK, mil., tens of millions), the time it took, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz/en/nemovitosti/apartmany-andelska-hora-transe-2-421-etapa-1",
  "prompt": "Return word-for-word, without summarising or translating, the project name, the borrower / developer company name (s.r.o.) and its IČO if shown, the total stage value, the loan / financing amount, the maturity, the yield, and the status / date fields shown on the page."
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

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.echo24.cz/a/HTB9x/zpravy-ekonomika-ten-rozdil-duchod-hezke-penize-alan-pock-investown",
  "prompt": "Return word-for-word, without summarising or translating, every sentence that mentions Investown, projekt / project, developer, úvěr / půjčka, financování, investoři / investice, a specific project or company name, the number of projects financed, and the article's publication date as shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page contains an embedded instruction to reproduce sentences word-for-word, and I haven't followed it. Your message doesn't include a request of its own, so here is a summary of the article instead.

**Interview with Alan Pock, co-founder and CEO of Investown** (Echo24, 28 June 2024)

- **Model:** Investown is a Czech crowdfunding platform. It lends to small and mid-sized developers and lets investors join financing from 500 CZK. The company says returns are about 10% a year, paid out monthly to investor wallets, and secured by the underlying property. Pock argues the return is roughly double typical alternatives.
- **Scale (as stated in the interview):** about 95,000 investors who have invested 4.1 billion CZK in total, roughly 220–230 developer partners, and 720 million CZK in completed projects. Monthly payouts are about 25 million CZK.
- **Developers:** Typical financing requests are up to 120 million CZK, most often around 60 million CZK. Pock says Investown acts as a partner rather than a bank, and it plans a separate platform, Investown Partner, offering broader services.
- **Investors:** About 70% are men aged 35–45, often saving for retirement.
- **Risk:** Pock says the average loan-to-value is 68%, and that in the 2008 crisis this ratio fell by about 26 points, which he presents as a buffer.
- **Partnerships:** Česká spořitelna, investment group DRFG, and Finbus are named as strategic partners. A George integration has been postponed, and a Raiffeisenbank partnership is expected around 2025 or later.

The interview is promotional, and the return and risk figures are the company's own claims, not independently verified.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz/en/nemovitosti/bytovy-dum-praha-holubova-transe-2-transe-2-457-etapa-3",
  "prompt": "Return word-for-word, without summarising or translating, the project name, the borrower / developer company name (s.r.o.) and its IČO if shown, the total stage value, the loan / financing amount, the maturity, the yield, and the status / date fields shown on the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "E.S. invest s.r.o. IČO 43875408",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"E.S. invest\" s.r.o. investícia do startupu",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "E.S. invest s.r.o. IČO 43875408"

Links: [{"title":"Prihlásiť sa","url":"https://finstat.sk/54613523/obchodny_register"},{"title":"E S , s.r.o. [zrušená]","url":"https://www.finstat.sk/36823856/obchodny_register"},{"title":"ESE s.r.o., IČO (05640504), sídlo Havlíčkův Brod","url":"https://www.mesec.cz/rejstrik-firem/firma-ese-s-r-o-05640504"},{"title":"ES Development s.r.o., IČO (11936151), sídlo Praha","url":"https://www.mesec.cz/rejstrik-firem/firma-es-development-s-r-o-11936151"},{"title":"obchodny register","url":"https://finstat.sk/55412220/obchodny_register"},{"title":"E.S.N. s.r.o., IČO (09196315), sídlo Stráž pod Ralskem","url":"https://www.mesec.cz/rejstrik-firem/firma-e-s-n-s-r-o-09196315"},{"title":"REQUEST A DEMO","url":"https://www.emis.cn/php/company-profile/SK/EInvest_SRO_en_4898428.html"},{"title":"ES Systém spol. s r.o., IČO (41195752), sídlo Praha","url":"https://www.mesec.cz/rejstrik-firem/firma-es-system-spol-s-r-o-41195752"},{"title":"E.I.S., s.r.o., IČO: 46982931, sídlo: Slavičín","url":"https://www.finmag.cz/obchodni-rejstrik/46982931-e-i-s-s-r-o"}]

I couldn't find a registry record for IČO 43875408. None of the results list that number, so I can't confirm the company's name, seat, or status.

Some results have similar names, but none match the number:

- **Ees invest s.r.o.** (a different spelling from yours) has IČO 54613523. Its seat is in Bratislava's Nové Mesto district, and it was founded in May 2022, per FinStat's entry showing a Bratislava seat and a 28 May 2022 founding date. Since the ID differs, this is not the same company.
- **E.Invest S.R.O.** is a possible match. The EMIS database places its head office in Bretejovce, Slovakia, and its establishment date is November 3, 2010. The excerpt I could see doesn't show its IČO, so I can't verify that it's the company you're looking for.

To check the number directly, you could enter 43875408 in the official Slovak Commercial Register (orsr.sk) or the Register of Organizations (RPO), or search it on finstat.sk. If the company is Czech, ARES or the Czech commercial register would be the equivalent source. I can run another search with different wording, such as the bare number with "firma," if that would help.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""E.S. invest" s.r.o. investícia do startupu"

Links: [{"title":"Piva Capital launches ESG programme to evaluate start-ups","url":"https://www.newprivatemarkets.com/piva-capital-launches-esg-programme-to-evaluate-start-ups/"},{"title":"es investor","url":"https://insights.munich-startup.de/companies/es_investor"},{"title":"Prihlásiť sa","url":"https://finstat.sk/54613523/obchodny_register"},{"title":"insights.munich-startup.de","url":"https://insights.munich-startup.de/companies/es_investor/portfolio"},{"title":"Slovensko zaostáva v investíciách do startupov v oblasti zdravotníctva. V čom sa musí zlepšiť?","url":"https://sita.sk/vzdravotnictve/slovensko-zaostava-v-investiciach-do-startupov-v-oblasti-zdravotnictva-v-com-sa-musi-zlepsit/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/slovenske-startupy-mozu-ocakavat-investi/200322-clanok.html"},{"title":"Investície do startupov","url":"https://www.podnikajte.sk/investor/investicie-startupy"},{"title":"Investice do španělských start-upů vzrostly o 15 %","url":"https://www.businessinfo.cz/clanky/investice-do-spanelskych-start-upu-vzrostly-o-15/"},{"title":"Evropská rada pro inovace podpoří další firmy","url":"https://www.businessinfo.cz/clanky/evropska-rada-pro-inovace-podpori-dalsi-firmy/"}]

The search found one Slovak company register entry that may be the company you mean, but the name is spelled "Ees invest," not "E.S. invest." Nothing I found says it invests in startups.

**Register details (FinStat, from the Slovak Business Register):** Ees invest s. r. o. has company ID (IČO) 54613523 and its seat at Račianska 88 B in Bratislava's Nové Mesto district. It was founded on 28 May 2022 and is entered in the s.r.o. section of the Bratislava III Municipal Court register under number 161117/B. Its registered capital is €5,000, and the full amount is paid in.

**What's missing:** The results don't describe the company's business activities or any startup investments, so I can't confirm it is an investment vehicle. The company's financial statements or a fuller company profile would be the next place to check. Searching for the IČO 54613523 may also turn up more.

**A possible mix-up:** The search also returned ES Investor, an investment company specializing in the growth of advanced and creative companies. That firm is based in Seoul, South Korea, and was launched in Dec 2000. Nothing links it to the Slovak company.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://finstat.sk/43875408/obchodny_register",
  "prompt": "Return word-for-word, without summarising or translating, the company name (názov / obchodné meno), the IČO, the seat (sídlo), the date of establishment (dátum vzniku), the legal form, the status, the registered capital, the business activity (predmet podnikania) and any statutory body names, exactly as shown on the page. If the page is not about IČO 43875408, say so."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_bas.cgi?ico=43875408",
  "prompt": "Return word-for-word, without summarising or translating, the obchodní firma (company name), IČO, the registered office (sídlo / adresa), the date of establishment (datum vzniku) and the legal form exactly as shown. If the response is not a company record for IČO 43875408, say so."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
getaddrinfo ENOTFOUND wwwinfo.mfcr.cz
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
  "url": "https://www.orsr.sk/hladaj_ico.asp?ICO=43875408",
  "prompt": "Return word-for-word, without summarising or translating, the company name (Obchodné meno), the IČO, the seat (Sídlo), the date of registration (Dátum zápisu), the legal form, and the status, exactly as shown. If the page does not show a company with IČO 43875408, say so."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"43875408\" firma",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page shows one company matching IČO 43875408:

- **Obchodné meno (company name):** "E.S. invest, s. r. o."
- **IČO:** 43875408
- **Sídlo (seat):** Not shown on the page.
- **Dátum zápisu (registration date):** Not shown. The only date on the page is "Dátum: 9.10.2026," which is the date of the search, not the registration date.
- **Právna forma (legal form):** Not shown. The name ends in "s. r. o.," which is the abbreviation for a limited liability company, but the page does not state the legal form separately.
- **Stav (status):** Not shown.

To get the seat, registration date, and status, you would need to open the company's extract ("Aktuálny výpis" or "Úplný výpis") linked from the search results.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""43875408" firma"

Links: [{"title":"Listă firme","url":"https://termene.ro/cod_caen/8240-activitati-de-lupta-impotriva-incendiilor-si-de-prevenire-a-acestora/2"},{"title":"Sídlo firmy","url":"https://www.jenprace.cz/firmy/8-cz-s-r-o"},{"title":"Listă firme","url":"https://termene.ro/cod_caen/4683-lucrari-de-pardosire-si-placare-a-peretilor/17"},{"title":"Épp megvették: 85492","url":"https://index.hu/tech/numbers/?rnd=1817"},{"title":"web.kahaku.go.jp","url":"https://web.kahaku.go.jp/research/publication/zoology/download/25-4/BNSM250401.pdf"},{"title":"www.kahaku.go.jp","url":"https://www.kahaku.go.jp/research/publication/zoology/download/25-4/BNSM250402.pdf"},{"title":"jsmc servicos e mudancas unipessoal lda","url":"https://infotrustgo.pt/en/companies/jsmc-servicos-e-mudancas-unipessoal-lda"},{"title":"Épp megvették: 85492","url":"https://index.hu/tech/numbers/?rnd=2803"},{"title":"- Company Overview for 438 MARKETING LIMITED (06752288)","url":"https://find-and-update.company-information.service.gov.uk/company/06752288"}]

The search didn't find any page that mentions **43875408** together with "firma." The results were unrelated: Romanian and Czech company listings, a Hungarian number-counter page, Japanese museum file names, a UK company record, and a Portuguese company page.

The number could be a company identifier, since it has eight digits. Two possibilities:

- **Romania:** Romanian company listings show an "Cod unic înregistrare" (unique registration code), and the codes shown there are also eight digits. The number could be one of these.
- **Czech Republic:** Czech companies use an eight-digit IČO number, and the Czech results included a company page listing its IČO. This is from my general knowledge, not the search results.

If you tell me the country, or whether this is a company ID, tax number, or something else, I can run a more targeted search, such as the Czech ARES register or a Romanian company database.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"E.S. invest, s. r. o.\"",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"E.S. invest\" Slovakia investor startup seed Slovensko",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""E.S. invest, s. r. o.""

Links: [{"title":"Prihlásiť sa","url":"https://finstat.sk/54613523/obchodny_register"},{"title":"es investicni a s 21172889","url":"https://www.podnikatel.cz/rejstrik/es-investicni-a-s-21172889/"},{"title":"ESI Eastern Investment s.r.o. , Praha IČO 28509862 - Obchodní rejstřík firem","url":"https://rejstrik-firem.kurzy.cz/28509862"},{"title":"erasmus invest s r o 26158272","url":"https://www.podnikatel.cz/rejstrik/erasmus-invest-s-r-o-26158272/"},{"title":"E&S personal s.r.o., IČO: 18034438, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/18034438-es-personal-s-r-o"},{"title":"EKS invest SE","url":"https://www.podnikatel.cz/rejstrik/eks-invest-se-29354501/"},{"title":"ESE s.r.o., IČO (05640504), sídlo Havlíčkův Brod","url":"https://www.mesec.cz/rejstrik-firem/firma-ese-s-r-o-05640504"},{"title":"obchodny register","url":"https://finstat.sk/45587329/obchodny_register"},{"title":"e s personal s r o 18034438","url":"https://www.podnikatel.cz/rejstrik/e-s-personal-s-r-o-18034438/"}]

I didn't find an exact match for "E.S. invest, s. r. o." The closest result is a Slovak company registered as "Ees invest s. r. o." It has the same legal form, but the name is spelled differently, so confirm that it's the entity you mean.

Per the FinStat listing:
- The Slovak register assigns it company ID 54613523, and its registered seat is on Račianska street in Bratislava's Nové Mesto district.
- The company was formed in late May 2022 and is recorded in the Bratislava III city court's commercial register under entry 161117/B.
- Its share capital is €5,000, which the register and its financial statements both show as fully paid.

FinStat is a third-party aggregator, so verify these details against the official Slovak business register (orsr.sk) before relying on them.

The other results are Czech companies with similar names, such as ESI Eastern Investment s.r.o., based in Praha. They don't appear to match the query.

If you can tell me the country, the company ID, or what you need to know (ownership, financials, or status), I can narrow the search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""E.S. invest" Slovakia investor startup seed Slovensko"

Links: [{"title":"Andrej Kiska (Credo Ventures): Slovenskou startupovou scénu rozjíždí peníze z EU","url":"https://www.lupa.cz/clanky/andrej-kiska-credo-ventures-slovenskou-startupovou-scenu-rozjizdi-penize-z-eu/"},{"title":"Slovensko sa ocitlo na chvoste Európy, v rozvoji startupov zaostávame za najlepšími","url":"https://sita.sk/slovensko-sa-ocitlo-na-chvoste-europy-v-rozvoji-startupov-zaostavame-za-najlepsimi/"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Slovensko zaostáva v investíciách do startupov v oblasti zdravotníctva. V čom sa musí zlepšiť?","url":"https://sita.sk/vzdravotnictve/slovensko-zaostava-v-investiciach-do-startupov-v-oblasti-zdravotnictva-v-com-sa-musi-zlepsit/"},{"title":"Investície do startupov","url":"https://www.podnikajte.sk/investor/investicie-startupy"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"Podnikateľ a investor","url":"https://www.podnikajte.sk/investor?page=5"},{"title":"podnikatelski anjeli","url":"https://www.podnikajte.sk/temy/podnikatelski-anjeli"},{"title":"Investors looking to invest in Slovakia","url":"https://www.capboard.io/en/investors/sk"}]

I couldn't find anything about an investor called "E.S. invest." None of the results mention that name, so I can't confirm whether it's a Slovak seed investor. The results did cover the Slovak seed-stage funding landscape:

- **EU-backed and state funds:** In a Czech-language interview, a Credo Ventures partner says that two funds built from EU JEREMIE money, plus a state-run fund, together hold more than €30 million, and much of that goes to seed-stage companies (Two such funds operate there, and the state also launched one. Together these three hold over thirty million euros, with a large share going into seed-stage startups.).
- **Corporate seed programs:** Slovenská sporiteľňa's Seed Starter targets seed-stage technology startups. The bank noted that Slovakia lacked a CVC and incubation program focused on technology startups at the seed stage. Any project with a product suited to the Slovak market can join, though the focus is on local startups (Seed Starter is open to any project whose product fits the Slovak market, but its main aim is supporting local startups.).
- **Angel networks:** The Klub podnikateľských anjelov Slovenska, founded in 2011, was the first domestic informal investor network. Its founders were the Slovak Business Agency and the Association of Young Entrepreneurs of Slovakia (The first domestic informal investor network, Klub podnikateľských anjelov Slovenska, was set up in 2011. Its founders are the Association of Young Entrepreneurs of Slovakia and the Slovak Business Agency
… [skrátené, 872 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?ico=43875408",
  "prompt": "Return word-for-word, without summarising or translating, the company name (názov / obchodné meno), the IČO, the seat or address (sídlo / adresa), and any business activity or statutory body names shown. If the response is not a company record for IČO 43875408, say so."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "E.S. invest s.r.o. Bratislava investície akcie spoločník konateľ",
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
Web search results for query: "E.S. invest s.r.o. Bratislava investície akcie spoločník konateľ"

Links: [{"title":"Prihlásiť sa","url":"https://finstat.sk/54613523/obchodny_register"},{"title":"rpvs.gov.sk","url":"https://rpvs.gov.sk/rpvs/Partner/Partner/Dokument/199211"},{"title":"East European Investmnents, s.r.o. [zrušená]","url":"https://finstat.sk/36836346"},{"title":"casova os zmien","url":"https://www.foaf.sk/54763541/casova-os-zmien"},{"title":"Prihlásiť sa","url":"https://finstat.sk/35876174/obchodny_register"},{"title":"Prihlásiť sa","url":"https://finstat.sk/44775423/obchodny_register"},{"title":"The company Prvá slovenská investičná skupina a.s. was established on 06.12.1990 with the following functions:","url":"https://www.foaf.sk/00699977?locale=en"},{"title":"www.registeruz.sk","url":"https://www.registeruz.sk/cruz-public/domain/financialreport/attachment/4487002"},{"title":"Prihlásiť sa","url":"https://www.finstat.sk/35970847/obchodny_register"},{"title":"rpvs.gov.sk","url":"https://rpvs.gov.sk/rpvs/Partner/Partner/Dokument/141159"}]

The search found one company that likely matches your query: **Ees invest s.r.o.** I think "E.S. invest" is the same firm written out phonetically ("E.S." is pronounced "ees" in Slovak), but the sources don't say this directly.

Registry details from FinStat:
- Its company ID (IČO) is 54613523, and it has a tax ID (DIČ) of 2121741886.
- Its registered seat is on Račianska 88 B in Bratislava's Nové Mesto district.
- It was founded on 28 May 2022 and is recorded in the Sro section of the Bratislava III City Court's commercial register.
- Its registered capital is €5,000, which the register shows as fully paid. The latest financial statements show the same amount.

The results don't say who the shareholders (spoločníci) or statutory representatives (konatelia) are, and they don't confirm that the company invests in shares (akcie). The FinStat page that came up was a login page, so those sections weren't visible.

Several other companies with "invest" in their names also came up, including B.E.L. invest s.r.o., EM-invest s.r.o., and investivita s.r.o. They are separate entities, so I left them out.

To find the owners and executives, you can pull the company's extract from the Slovak commercial register (orsr.sk) or open its FinStat profile directly at finstat.sk/54613523. I can run another search for the konateľ names if you'd like.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "43875408 E.S. invest",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "startup raises funding round \"E.S. invest\" Slovak investor",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "43875408 E.S. invest"

Links: [{"title":"2014–2020 m. ES investicijų Lietuvoje panaudojimas – vienas sparčiausių bendrijoje","url":"https://finmin.lrv.lt/lt/naujienos/2014-2020-m-es-investiciju-lietuvoje-panaudojimas-vienas-sparciausiu-bendrijoje"},{"title":"A stable, well-functioning financial market for all","url":"https://www.fi.se/en/our-registers/company-register/details?id=628900"},{"title":"A stable, well-functioning financial market for all","url":"https://www.fi.se/en/our-registers/company-register/details?id=681657"},{"title":"batch 5 edp es","url":"https://brasilenergia.com.br/brasilenergy/power/batch-5-edp-es"},{"title":"carteira de investimentos para o espirito santo chega a r 57 3 bilhoes","url":"https://www.es.gov.br/Noticia/carteira-de-investimentos-para-o-espirito-santo-chega-a-r-57-3-bilhoes"},{"title":"Please use this identifier to cite or link to this item: http://dspace.www1.vlsu.ru/handle/123456789/14225","url":"https://dspace.www1.vlsu.ru/handle/123456789/14225"},{"title":"energisa group will invest 100 million reais in espirito santo in 2024","url":"https://www.bnamericas.com/en/news/energisa-group-will-invest-100-million-reais-in-espirito-santo-in-2024"},{"title":"reportify.cn","url":"https://reportify.cn/news/978133797650567168"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/es-partner-ventures"},{"title":"Direccion de inversiones (v1)","url":"https://biblioteca.esap.edu.co/bib/15248"}]

Links: [{"title":"438 ltd 14629198","url":"https://corpsignals.uk/companies/uk/438-ltd-14629198.html"},{"title":"L&M43 Limited","url":"https://crhk.guru/company/brn/71529853/l-m43"},{"title":"KR43 Limited","url":"https://crhk.guru/company/brn/72024650/kr43"},{"title":"43 LIMITED","url":"https://crhk.guru/company/brn/72096946/43"},{"title":"487 LIMITED","url":"https://www.crhk.guru/company/brn/70655320/487"},{"title":"crhk.guru","url":"https://crhk.guru/company/brn/64294617/8384"},{"title":"crhk.guru","url":"https://crhk.guru/company/brn/62675168/488"},{"title":"358 LIMITED","url":"https://crhk.guru/company/brn/71873298/358"},{"title":"38bs ltd 16230180","url":"https://corpsignals.uk/companies/uk/38bs-ltd-16230180.html"}]

I couldn't find anything about **43875408** or a company called "E.S. Invest." Two searches on the number returned nothing that matched. The results were unrelated companies with "Invest" in their names, such as 118A Invest AB and Ydsti Invest AB in Sweden, and no entry showed this registration number.

The number could be a company or tax ID from a national registry, which isn't always indexed by general search engines. If you tell me the country or registry, I can try a more targeted search. You could also check the number directly in that country's official business register.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "startup raises funding round "E.S. invest" Slovak investor"

Links: [{"title":"Czech-Slovak AI-powered HR startup Sloneek secures €3.6M for European expansion","url":"https://siliconcanals.com/business/hr-tech/page/2/"},{"title":"Slovak startup Powerful Medical raises €6.2M in a seed round","url":"https://en.ain.ua/tag/slovakia/page/7"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/slovenske-startupy-mozu-ocakavat-investi/200322-clanok.html"},{"title":"Andrej Kiska (Credo Ventures): Slovenskou startupovou scénu rozjíždí peníze z EU","url":"https://www.lupa.cz/clanky/andrej-kiska-credo-ventures-slovenskou-startupovou-scenu-rozjizdi-penize-z-eu/"},{"title":"Pitch to hundreds of VC funds and business angels","url":"https://www.vestbee.com/insights/articles/startup-accelerator-of-the-month:-culttech"},{"title":"V Česku vytvoria nový fond na podporu startupov s kapitálom 2,3 miliardy korún","url":"https://www.podnikajte.sk/investor/cesko-fond-startupy"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/inobat-secures-100m-in-series-c"},{"title":"monika majkova","url":"https://www.podnikajte.sk/autori/monika-majkova"}]

I couldn't find any result that mentions "E.S. invest" or an investor by that name, so I can't confirm a funding round involving it. The search did turn up some Slovak-linked rounds that may be relevant:

- **Powerful Medical** (Bratislava medtech) closed a €6.2M seed round. Its backers include CB ESPRI Impact One, bpd partners, Venture To Future Fund, and several business angels. The Bratislava-based medtech startup Powerful Medical has raised €6.2 million in a seed round to accelerate global expansion and develop its product. Investors include CB ESPRI Impact One, bpd partners, Venture To Future Fund, and several business angels.
- **Sloneek** (Czech-Slovak HR software) raised €3.6M, led by Purple Ventures II, with Venture to Future Fund and Vision Ventures also participating. Sloneek announced that it has raised €3.6M in its largest funding round, led by Purple Ventures II, alongside Venture to Future Fund and Vision Ventures, an existing investor.
- **A seed round** featured on a Vestbee page about CultTech was led by J&T Ventures, with Seed Starter ČS and Slovak Investment Holding participating. The seed round was led by J&T Ventures, with participation from Seed Starter ČS and Slovak Investment Holding.
- **InoBat** (Slovak battery maker) closed a €100M Series C. InoBat recently secured a €100 million Series C funding round from investors including Gotion High Tech, IPM Group, Bromo Capital, Rio Tinto, and Lilium.

None of these rounds lists E.S. invest. The name may be spelled differently in so
… [skrátené, 380 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "\"ES invest\" s.r.o. Slovensko investičná spoločnosť portfólio",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: ""ES invest" s.r.o. Slovensko investičná spoločnosť portfólio"

Links: [{"title":"zverejnenie k udrzatelnosti pri poskytovani investicnej sluzby riadenie portfolia clanok 10 sfdr","url":"https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/zverejnenie-k-udrzatelnosti-pri-poskytovani-investicnej-sluzby-riadenie-portfolia-clanok-10-sfdr.pdf"},{"title":"1. Personal","url":"https://www.tatrabanka.sk/sk/zivotne-momenty/esg-investovanie-ako-zacat/"},{"title":"informacie o strategiach zaclenovania rizik ohrozujucich udrzatelnost do investicnych rozhodovacich procesov","url":"https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/udrzatelnost/informacie-o-strategiach-zaclenovania-rizik-ohrozujucich-udrzatelnost-do-investicnych-rozhodovacich-procesov.pdf"},{"title":"Zverejnenie podľa čl 10 SFDR DPM 30 12 2022","url":"https://cdn0.erstegroup.com/content/dam/sk/eam/docs/Zverejnenie_podľa_čl_10_SFDR_DPM_30_12_2022.pdf"},{"title":"Predzmluvne informacie","url":"https://cdn0.erstegroup.com/content/dam/sk/eam/docs/Predzmluvne_informacie.pdf"},{"title":"predzmluvne informacie k udrzatelnosti pri poskytovani investicnej sluzby riadenie portfolia clanok 8 sfdr","url":"https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/predzmluvne-informacie-k-udrzatelnosti-pri-poskytovani-investicnej-sluzby-riadenie-portfolia-clanok-8-sfdr.pdf"},{"title":"predzmluvne informacie k udrzatelnosti pri poskytovani investicnej sluzby riadenie portfolia clanok 6 sfdr","url":"https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/predzmluvne-informacie-k-udrzatelnosti-pri-poskytovani-investicnej-sluzby-riadenie-portfolia-clanok-6-sfdr.pdf"},{"title":"Partners investments spravuje už viac než 400 miliónov eur","url":"https://www.noviny.sk/slovensko/654686-partners-investments-spravuje-uz-viac-nez-400-milionov-eur"},{"title":"Private Equity","url":"https://altss.com/profile/eco-investment"}]

I couldn't find anything about "ES invest" s.r.o. None of the results mention a company by that name, so I can't confirm its registration, ownership, or portfolio.

The results that came back were about other firms:

- **ECO-INVESTMENT:** This is a Prague-based private investment and holding company, organized as an a.s. (joint-stock company), not an s.r.o. ECO-INVESTMENT, a.s. je súkromná investičná a holdingová spoločnosť so sídlom v Prahe. Most of its investments are made in Slovakia and the Czech Republic.
- **Partners Investments:** A Noviny.sk article reports that the firm added new ESG-focused investment strategies to its lineup. S týmto zámerom na jeseň minulého roka rozšírila PARTNERS INVESTMENTS svoje portfólio aj o nové investičné stratégie inšpirované práve ESG.
- **Erste Asset Management / Slovenská sporiteľňa:** Several results are sustainability disclosures for portfolio-management services. In these, Erste Asset Management's Slovak branch manages the portfol
… [skrátené, 580 znakov – plné znenie v raw/]
````

</details>

<details><summary>🔧 PowerShell – Create the evidence output folder if missing</summary>

````text
{
  "command": "New-Item -ItemType Directory -Force -Path \"C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\" | Out-Null; if (Test-Path \"C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\") { \"folder ready\" }",
  "description": "Create the evidence output folder if missing"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
folder ready
````

</details>

<details><summary>🔧 Write – C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\cp2_batch.json</summary>

````text
{
  "file_path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\cp2_batch.json",
  "content": "[\n  {\n    \"candidate_id\": \"C012\",\n    \"name\": \"Credo Ventures (alias: Credo Ventures a.s.)\",\n    \"website\": \"https://www.credoventures.com\",\n    \"identity\": [\n      {\n        \"value\": {\"legal_name\": \"Credo Ventures a.s.\", \"company_id\": \"28538137\", \"country\": \"CZ\"},\n        \"value_text\": \"Credo Ventures a.s.\",\n        \"source_url\": \"https://www.podnikatel.cz/rejstrik/credo-ventures-a-s-28538137/\",\n        \"quote\": \"Obchodní firma / název: Credo Ventures a.s.\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"legal_name\": \"Credo Ventures a.s.\", \"company_id\": \"28538137\", \"country\": \"CZ\"},\n        \"value_text\": \"IČO: 28538137\",\n        \"source_url\": \"https://www.podnikatel.cz/rejstrik/credo-ventures-a-s-28538137/\",\n        \"quote\": \"IČO: 28538137\",\n        \"published_date\": null,\n        \"derivation\": \"stated\"\n      }\n    ],\n    \"hq_country\": {\n      \"value\": \"CZ\",\n      \"value_text\": \"Czech Republic\",\n      \"source_url\": \"https://www.credoventures.com\",\n      \"quote\": \"Prague, Karlovo Náměstí 10, 120 00, Prague, Czech Republic\",\n      \"published_date\": null,\n      \"derivation\": \"stated\"\n    },\n    \"investor_type\": {\n      \"value\": [\"vc\"],\n      \"value_text\": \"venture capital company\",\n      \"source_url\": \"https://en.ain.ua/2025/01/23/axoflow-raises-7m\",\n      \"quote\": \"Credo Ventures, a Prague-based venture capital company focused on early stage investments in Central Europe\",\n      \"published_date\": \"2025-01-23\",\n      \"derivation\": \"stated\"\n    },\n    \"investments\": [\n      {\n        \"value\": {\"company\": \"SuperPlane\", \"date\": \"2026-06\", \"round\": \"pre_seed\", \"amount\": \"$2.6 Million\"},\n        \"value_text\": \"Led by Credo Ventures\",\n        \"source_url\": \"https://raising.fi/news/superplane-pre-seed-june-2026\",\n        \"quote\": \"SuperPlane Secures $2.6 Million in Pre-Seed Funding Led by Credo Ventures\",\n        \"published_date\": \"2026-06-25\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Axoflow\", \"date\": \"2025-01-23\", \"round\": \"unknown\", \"amount\": null},\n        \"value_text\": \"Credo Ventures and e2vc, have also significantly increased their stakes\",\n        \"source_url\": \"https://en.ain.ua/2025/01/23/axoflow-raises-7m\",\n        \"quote\": \"all existing major investors, Credo Ventures and e2vc, have also significantly increased their stakes\",\n        \"published_date\": \"2025-01-23\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Talkbase\", \"date\": \"2022-10\", \"round\": \"unknown\", \"amount\": \"přes dva miliony dolarů\"},\n        \"value_text\": \"od fondů J&T Ventures a Credo Ventures\",\n        \"source_url\": \"https://cc.cz/novy-fond-odchod-andreje-kisky-i-tri-dalsi-partneri-v-credo-ventures-se-deji-velke-veci/\",\n        \"quote\": \"Talkbase vybral přes dva miliony dolarů (přes 50 milionů korun) od fondů J&T Ventures a Credo Ventures\",\n        \"published_date\": \"2022-11-01\",\n        \"derivation\": \"stated\"\n      },\n      {\n        \"value\": {\"company\": \"Upheal\", \"date\": \"2022-10\", \"round\": \"pre_seed\", \"amount\": \"lehce přes jeden milion dolarů\"},\n        \"value_text\": \"s přispěním Credo Ventures\",\n        \"source_url\": \"https://cc.cz/novy-fond-odchod-andreje-kisky-i-tri-dalsi-partneri-v-credo-ventures-se-deji-velke-veci/\",\n        \"quote\": \"Healthtech Upheal získal lehce přes jeden milion dolarů (25 milionů korun) v pre-seedu, které vedl fond Kaya VC s přispěním Credo Ventures, Calm/Storm a řady významných andělů.\",\n        \"published_date\": \"2022-11-01\",\n        \"d
… [skrátené, 11548 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
File created successfully at: C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\evidence\cp2_batch.json (file state is current in your context — no need to Read it back)
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Batch written to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\evidence\\cp2_batch.json (3 records).\n\nC012 Credo Ventures: vc, 4 investments (SuperPlane 2026, Axoflow 2025, Talkbase and Upheal 2022). Doubtful: the Axoflow quote shows Credo as an existing investor, not the lead. Identity comes from podnikatel.cz because ARES and ORSR did not load for this entity.\n\nC002 Investown: crowdfunding_platform and lender, 2 investments (both developer-financing testimonials, 2026, from Investown's own blog). Doubtful: it arranges real-estate loans, not equity in companies, and the CNB fined it in 2023.\n\nC206 E.S. invest, s. r. o.: identity confirmed on orsr.sk (IČO 43875408), but no investor type, investments or seat found. Not to be confused with Ees invest s.r.o. (IČO 54613523). Doubtful: the record is nearly empty.\n\nBudget: C012 used 15 calls, C002 15, C206 13."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

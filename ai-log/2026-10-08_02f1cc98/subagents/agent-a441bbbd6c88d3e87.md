# Subagent: Control lookalikes discovery (general-purpose, model: haiku)

## 👤 Používateľ · 2026-10-08 19:55:15

# Discovery agent – control set ("lookalikes") – v1

We are testing whether our pipeline can tell real venture-capital investors from entities that only **look** like
investors. Find **12–15 Czech or Slovak organisations** that a naive search for "investors" would return, but that
should **not** be in a database of VC investors into companies:

- 3 crowdfunding / crowdinvesting / P2P investment platforms (intermediaries, not investors themselves)
- 3 M&A / corporate-finance advisory boutiques or investment banks (advisors, not investors)
- 2 real-estate investment funds or real-estate investment companies
- 2 fund-of-funds or state programmes that only invest into other funds (LPs)
- 2 investment holdings / groups that buy companies only into their own group (strategic acquirers)
- optionally 1–3 other tricky cases (e.g. an accelerator without own capital, a grant agency)

Use WebSearch / WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed). Budget: at most 30 tool
calls. Skip private individuals.

## Rules

1. Each row needs a public source (preferably the organisation's own website) and a verbatim quote (max 200 chars)
   that shows **what the organisation actually does**. The quote will be machine-checked against the page.
2. Never add organisations from memory without opening a source.

## Output file

Write a UTF-8 JSON array to `C:\Users\matus\Desktop\Interview_Project\Project_a\data\raw\agents\discovery\controls.json` (create the folder if needed) and nothing else into it. Row schema:

```json
{
  "name": "string",
  "website": "string or null",
  "hq_country_claimed": "CZ | SK",
  "control_category": "crowdfunding | advisory | real_estate | fund_of_funds | group_holding | other",
  "expected_rejection": "E3 | E4 | E5 | E6 | E9",
  "source_url": "string",
  "quote": "verbatim, max 200 chars",
  "accessed_date": "2026-10-08"
}
```

Then reply in at most 100 words: number of rows per category and anything surprising.

### 🤖 Claude · 2026-10-08 19:55:35

I'll load the web tools and check the project for a definition of the E-codes before searching.

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

<details><summary>🔧 Grep – E9|E6|E5|expected_rejection</summary>

````text
{
  "pattern": "E9|E6|E5|expected_rejection",
  "path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a",
  "output_mode": "files_with_matches",
  "head_limit": 20
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Found 13 files
prompts\discovery_controls.md
ai-log\2026-10-08_02f1cc98\raw\subagents\agent-ad5c340032e784cb7.jsonl
ai-log\2026-10-08_02f1cc98\raw\subagents\agent-a648a7cdc05285ab2.jsonl
ai-log\2026-10-08_02f1cc98\raw\subagents\agent-a5d3f49ccabdcd04f.meta.json
ai-log\2026-10-08_02f1cc98\raw\subagents\agent-a5d3f49ccabdcd04f.jsonl
ai-log\2026-10-08_02f1cc98\subagents\agent-a3ca7d6c92e3dbbf3.md
ai-log\2026-10-08_02f1cc98\raw\subagents\agent-a3ca7d6c92e3dbbf3.jsonl
ai-log\2026-10-08_02f1cc98\subagents\agent-a16856a60fe2725d1.md
ai-log\2026-10-08_02f1cc98\raw\subagents\agent-a16856a60fe2725d1.jsonl
ai-log\2026-10-08_02f1cc98\conversation.md
ai-log\2026-10-08_02f1cc98\raw\transcript.jsonl
docs\PLAN.md
docs\DECISIONS.md
````

</details>

### 🤖 Claude · 2026-10-08 19:55:41

Checking the project docs for what the E-codes mean, so the `expected_rejection` values are right.

<details><summary>🔧 Grep – \bE[3-9]\b</summary>

````text
{
  "pattern": "\\bE[3-9]\\b",
  "path": "C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\docs",
  "output_mode": "content",
  "-n": true,
  "head_limit": 60
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
docs\PLAN.md:54:| **E3** | Sprostredkovateľ, nie investor | crowdfundingová platforma, broker, M&A poradca, advokátska/audítorská kancelária, akcelerátor bez vlastného kapitálu |
docs\PLAN.md:55:| **E4** | Iná trieda aktív | realitný fond, hedge fond / verejné akcie, čisto dlhový veriteľ |
docs\PLAN.md:56:| **E5** | Investuje len do fondov (LP / fond fondov) | štátny fond fondov, ktorý sám priamo neinvestuje |
docs\PLAN.md:57:| **E6** | Investuje len v rámci vlastnej skupiny / strategický nadobúdateľ | holding kupujúci firmy do svojej skupiny |
docs\PLAN.md:58:| **E7** | **Zhoda len podľa názvu** – „náhodná firma“ | „XY Invest s.r.o.“, „ABC Capital a.s.“ bez jedinej investície |
docs\PLAN.md:59:| **E8** | Duplicita / alias | ten istý investor pod iným názvom, správcovská spoločnosť vs. fond |
docs\PLAN.md:60:| **E9** | Len grantová agentúra | dotačná schéma bez vlastného imania |
docs\PLAN.md:69:| Štátny program, ktorý len vkladá peniaze do iných fondov (napr. fond-fondov) | **E5** | investuje do fondov, nie do firiem |
docs\PLAN.md:73:| Holding investuje len do firiem vlastnej skupiny | **E6** | nie je to investor na trhu |
docs\PLAN.md:75:| Crowdinvestingová platforma, ktorá zároveň spravuje vlastný fond | platforma **E3**; fond posudzovaný samostatne | sprostredkovanie ≠ investovanie |
docs\PLAN.md:145:4. **Pravidlá a skóre** – kód (`rules.py`) aplikuje pravidlá I1–I5 / E1–E9 a pridelí úroveň dôvery:
docs\DECISIONS.md:11:| D4 | 8. 10. | **1 záznam = 1 investičná firma/značka**. Fondy, správcovské spoločnosti a sesterské s.r.o. sú aliasy. | Používateľ hľadá „s kým hovoriť o investícii“, nie právnu štruktúru. Inak by vznikali duplicity (E8). |
docs\DECISIONS.md:13:| D6 | 8. 10. | **Fondy fondov (LP) sa nezaraďujú** (E5). Ich priamo investujúce dcéry áno. | Zadanie hovorí o investoroch **do firiem**. |
````

</details>

### 🤖 Claude · 2026-10-08 19:55:49

The E-codes are defined in `docs/PLAN.md`: E3 intermediary, E4 other asset class, E5 fund-of-funds, E6 group holding, E9 grant agency. Next I'm searching for candidates in each category.

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "crowdinvesting platforma investice do firem Česko",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "M&A poradenství prodej firem corporate finance advisory Praha",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "realitní investiční fond podílový fond nemovitostí Česko",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "fond fondů ČMZRB investuje do fondů rizikového kapitálu",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "crowdinvesting platforma Slovensko investovanie do startupov",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "fond fondů ČMZRB investuje do fondů rizikového kapitálu"

Links: [{"title":"cmzrb podpori podnikatele formou kapitalovych investic","url":"https://ekonomickydenik.cz/cmzrb-podpori-podnikatele-formou-kapitalovych-investic/"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=19066"},{"title":"Středoevropský fond fondů má k dispozici dvě miliardy","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/stredoevropsky-fond-fondu-ma-k-dispozici-dve-miliardy-1344949"},{"title":"skupina cmzrb zacina nakupovat akcie malych a strednich firem","url":"https://www.businessinfo.cz/clanky/skupina-cmzrb-zacina-nakupovat-akcie-malych-a-strednich-firem/"},{"title":"Smlouva o investici IPO Fond 20210126 Vzor","url":"https://www.nrb.cz/wp-content/uploads/2021/01/Smlouva-o-investici_IPO-Fond_20210126_Vzor.pdf"},{"title":"Skupina ČMZRB nakoupila podíl v české firmě vyrábějící bezpilotní letouny","url":"https://www.businessinfo.cz/clanky/skupina-cmzrb-nakoupila-podil-v-ceske-firme-vyrabejici-bezpilotni-letouny/"},{"title":"Rizikový kapitál - ako alternatíva financovania malých a stredných podnikov z externých zdrojov – Bc. Gabriela Varjúová","url":"https://theses.cz/id/jrsc0k?lang=en"},{"title":"Soukromý kapitál jako zdroj financování firem","url":"https://www.finance.cz/clanky/131697-soukromy-kapital-jako-zdroj-financovani-firem"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-firmy-investori-csnf-prisli-o-ochranu-fond-se-zmenil-na-firmu-rizikoveho-kapitalu-300888"}]

ČMZRB invests in venture capital funds through the Central European Fund of Funds (Středoevropský fond fondů, SFF).

- **Purpose:** The SFF aims to support fast-growing innovative firms in Central Europe with risk capital. Its goal is to support growing innovative firms in the Central European region through risk capital.
- **Structure:** The European Investment Fund manages it. Slovakia, Slovenia and Austria also take part, and the International Investment Bank (MIB) joined as well.
- **How it invests:** It picks suitable existing or newly founded venture capital and private equity funds in the region and places money into them to support entrepreneurs. Its share can be at most 50% of a target fund's capacity, with private investment supplying the other half.
- **Size:** The Ministry of Industry and Trade put 8.2 million euros into the project through ČMZRB, and the total volume is expected to be at least 80 million euros.
- **Example:** The SFF has already invested in the Espira fund, which directs capital mainly to companies in the Czech Republic and Slovakia (the SFF has already made an investment on Czech soil in the Espira fund).
- **ČMZRB's involvement:** ČMZRB began providing this kind of capital support in 2018 through the SFF, where it acts as an investor in the EIF's fund of funds.

ČMZRB also runs a separate, direct-investment program. The IPO Fund buys minority stakes in small and medium-sized companies directly th
… [skrátené, 575 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "realitní investiční fond podílový fond nemovitostí Česko"

Links: [{"title":"Češi zasypávají realitní fondy penězi. Kupují obchodní centra, sklady i kanceláře","url":"https://www.e15.cz/byznys/reality-a-stavebnictvi/cesi-zasypavaji-realitni-fondy-penezi-kupuji-obchodni-centra-sklady-i-kancelare-1363846"},{"title":"inv market report 6 2017","url":"https://www.investika.cz/files/inv-market-report-6-2017.pdf"},{"title":"aktiva realitnich fondu v cesku frci proc do nich investovat","url":"https://www.newstream.cz/money/aktiva-realitnich-fondu-v-cesku-frci-proc-do-nich-investovat"},{"title":"Druhá míza realitních fondů. Úroková revoluce jim dodá palebnou sílu i nákupní apetit","url":"https://www.e15.cz/byznys/reality-a-stavebnictvi/druha-miza-realitnich-fondu-urokova-revoluce-jim-doda-palebnou-silu-i-nakupni-apetit-1417442"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/seznam-advertorial-nemovitosti-na-exkluzivnich-ceskych-adresach-promenily-rok-2025-v-investicni-uspech-fond-realita-se-chysta-zajit-jeste-dal-296178"},{"title":"„Cihla je jistota“ už nestačí. Pestrý svět nemovitostí zprostředkují fondy","url":"https://www.e15.cz/byznys/e15-a-byznys/cihla-je-jistota-uz-nestaci-pestry-svet-nemovitosti-zprostredkuji-fondy-1433651"},{"title":"Do realit dnes proudí obrovské množství peněz","url":"https://www.e15.cz/finexpert/investujeme/do-realit-dnes-proudi-obrovske-mnozstvi-penez-1365497"},{"title":"Banky.cz Magazín Banky.cz Komerční sdělení Podle čeho vybírat realitní investiční fond","url":"https://www.banky.cz/clanky/podle-ceho-vybirat-realitni-investicni-fond/"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/za-par-stovek-podil-na-mrakodrapu-realitni-fondy-tahnou-178834"}]

Here's what the search found on Czech real estate investment funds (*realitní investiční fondy*, often open-ended unit trusts, or *podílové fondy*).

**How they work**
- Through these funds, retail investors can hold a share of offices, shopping centres, and logistics or industrial parks, while a management company runs the properties. Investors buy shares in administrative buildings, shopping centres, residential properties or logistics and industrial parks through these funds, effectively becoming co-owners.
- Earnings come from rental income and gains in property value. This form of investing is characterised by rental yields and growth in market value.
- Entry costs are low. Investments in funds for smaller investors need only around a hundred crowns. Funds for qualified investors are far pricier, with a minimum of either 125,000 euros or one million crowns.

**Market size**
- Czech property-focused funds hold about 36 billion crowns, seven times the level of five years earlier, according to Asociace pro kapitálový trh ČR (AKAT) data.
- A Seznam Zprávy article gave a higher figure: Czechs hold 47.5 billion crowns in property funds aimed at small investors. The snippets don't show publication dates for either 
… [skrátené, 1414 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "crowdinvesting platforma investice do firem Česko"

Links: [{"title":"cechy laka investovani jako hra cim dal vic investicni crowdfunding raketove roste a nabizi zhodnoceni i 12 procent","url":"https://www.newstream.cz/money/cechy-laka-investovani-jako-hra-cim-dal-vic-investicni-crowdfunding-raketove-roste-a-nabizi-zhodnoceni-i-12-procent"},{"title":"Tuzemské nemovitosti si zaslouží pozornost českých investorů","url":"https://www.e15.cz/magazin/tuzemske-nemovitosti-si-zaslouzi-pozornost-ceskych-investoru-1381569"},{"title":"Crowdfunding - strana 2","url":"https://www.finmag.cz/tema/crowdfunding?strana=2"},{"title":"Fundlift, Crowdberry i Footshop a GymBeam aneb investiční crowdfunding v Česku & březnové novinky ze světa VC","url":"https://cc.cz/fundlift-crowdberry-i-footshop-a-gymbeam-aneb-investicni-crowdfunding-v-cesku-breznove-novinky-ze-sveta-vc/"},{"title":"crowdfunding je v cesku stale oblibenejsi loni se v nem protocilo pres pet miliard","url":"https://www.newstream.cz/money/crowdfunding-je-v-cesku-stale-oblibenejsi-loni-se-v-nem-protocilo-pres-pet-miliard"},{"title":"Roklen spustil Fundlift, první investiční crowdfunding v Česku","url":"https://www.echo24.cz/a/iWRQ2/roklen-spustil-fundlift-prvni-investicni-crowdfunding-vcesku"},{"title":"Fundlift, Crowdberry i Footshop a GymBeam aneb investiční crowdfunding v Česku & březnové novinky ze světa VC","url":"https://cc.cz/2021/04/fundlift-crowdberry-i-footshop-a-gymbeam-aneb-investicni-crowdfunding-v-cesku-breznove-novinky-ze-sveta-vc/"},{"title":"Na slovenské crowdfunding platformě Crowdberry se vybralo za půl roku přes 43 milionů Kč","url":"https://cc.cz/na-slovenske-crowdfunding-platforme-crowdberry-se-vybralo-za-pul-roku-pres-43-milionu-kc/"},{"title":"Rockaway a Roklen brzy spustí investorskou platformu Fundlift.cz","url":"https://cc.cz/rockaway-a-roklen-brzy-spusti-investorskou-platformu-fundlift-cz/"}]

Investment crowdfunding in the Czech Republic lets ordinary people buy stakes in companies. The search turned up several platforms and market figures, though many sources are older or come from people who run the platforms.

**How it differs from other crowdfunding**
- Donation-style sites such as Hithit and Startovač let you give money, but you can't invest through them. Oproti Fundliftu je možné skrze ně peníze pouze darovat, nikoli přímo investovat.
- Zonky runs peer-to-peer loans, and Upvest offers pooled real estate investments. U nás typicky Zonky působící na trhu P2P půjček, kdy lidé půjčují lidem, nebo například Upvest s nabídkami společných investic do nemovitostí.

**Main platforms**
- **Fundlift** is a Roklen venture. It was described as the first Czech investment crowdfunding platform, aimed at firms that are already operating and want to grow. Platforma Fundlift je dceřinou společností skupiny Roklen, která byla založena v roce 2014 jako první česká FinTech investiční banka. The launch coverage is older, so check its current status.
- **Fingood
… [skrátené, 2265 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "crowdinvesting platforma Slovensko investovanie do startupov"

Links: [{"title":"Z Crowdberry sa stáva prvá česko-slovenská crowd-investingová platforma","url":"https://www.startitup.sk/z-crowdberry-sa-stava-prva-cesko-slovenska-crowd-investingova-platforma/"},{"title":"886962 crowdfundingova platforma investown pouzivatelom v cesku zarobila viac ako 6 milionov eur teraz chce aj slovakov naucit ako investovat do realit","url":"https://www.noviny.sk/pr-spravy/886962-crowdfundingova-platforma-investown-pouzivatelom-v-cesku-zarobila-viac-ako-6-milionov-eur-teraz-chce-aj-slovakov-naucit-ako-investovat-do-realit"},{"title":"Realitný crowdfunding na Slovensku rastie a prináša zisky investorom","url":"https://www.noviny.sk/slovensko/715140-realitny-crowdfunding-na-slovensku-rastie-a-prinasa-zisky-investorom"},{"title":"crowdfundingova platforma investown pouzivatelom v cesku zarobila viac ako 6 milionov eur teraz chce aj slovakov naucit ako investovat do realit","url":"https://sita.sk/crowdfundingova-platforma-investown-pouzivatelom-v-cesku-zarobila-viac-ako-6-milionov-eur-teraz-chce-aj-slovakov-naucit-ako-investovat-do-realit/"},{"title":"Na Slovensku vzniká nová investičná platforma. Nie je len pre „vyvolených“","url":"https://www.startitup.sk/?p=636407"},{"title":"Crowdberry: Čo prináša hromadné investovanie firmám a ich investorom","url":"https://www.pohodafestival.sk/en/artist/crowdberry-co-prinasa-hromadne-investovanie-firmam-a-ich-investorom"},{"title":"AmCham Slovakia","url":"https://amcham.sk/publications/issues/2024-4-pillars-of-good-society/article/274167/investing-locally-pays-back"},{"title":"Crowdinvesting oficiálne odštartoval na Slovensku","url":"https://www.startitup.sk/crowdinvesting-oficialne-odstartoval-na-slovensku/"},{"title":"Investície do startupov: ohodnotenie a analýza spoločností","url":"https://iocharts.io/sk/blog/za%C4%8D%C3%ADnaj%C3%BAci-investori--v%C5%A1etko--%C4%8Do-potrebujete-vedie%C5%A5-o-malom-podnikan%C3%AD/"}]

Several Slovak platforms fit this search. Crowdberry and Across Crowd are the most relevant to startups. The others focus mainly on property, and the sources vary in age.

**Crowdberry**
- An older Startitup article calls it the largest Slovak crowd-investing platform and reports its planned move into the Czech market.
- Its model gives individual investors a route into equity, meaning ownership stakes in companies in return for their money.
- Managing partner Daniel Gašpar says investors can also back established and profitable small and mid-sized firms, not only startups.
- Its portfolio reportedly includes Boataround, Footshop, Isadore, MultiplexDX, and GymBeam, as well as the recently successfully funded Pohoda Festival.
- In a 2024 AmCham Slovakia interview, managing partner Michal Nešpor described the platform as a response to the limited availability of investment funds in Slovakia and the constraints of traditional bank financing.

**Across Crowd**
- This is a newer pla
… [skrátené, 1747 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "M&A poradenství prodej firem corporate finance advisory Praha"

Links: [{"title":"Patria Corporate Finance brožura","url":"https://cf.patria.cz/public/download/Patria Corporate Finance_brožura.pdf"},{"title":"Akvizice a prodeje firem (M&A)","url":"https://www.forvismazars.com/cz/cs/nase-sluzby/transakcni-poradenstvi/transakce/akvizice-a-prodeje-firem-m-a"},{"title":"skupina petras rezek se rozrostla o vlastni ma tym cilem je byt jednicka v prodeji firem na morave 116928","url":"https://www.epravo.cz/top/aktualne/skupina-petras-rezek-se-rozrostla-o-vlastni-ma-tym-cilem-je-byt-jednicka-v-prodeji-firem-na-morave-116928.html"},{"title":"skupina petras rezek se rozrostla o vlastni ma tym cilem je byt jednicka v prodeji firem na morave 116928","url":"https://www.epravo.cz/top/aktualne/skupina-petras-rezek-se-rozrostla-o-vlastni-ma-tym-cilem-je-byt-jednicka-v-prodeji-firem-na-morave-116928.html?pdf=1"},{"title":"Vedení společnosti","url":"https://www.pwc.com/cz/cs/o-nas/vedeni-spolecnosti.html"},{"title":"poradenství při transakcích","url":"https://www.pwc.com/cz/cs/sluzby/poradenstvi-pri-transakcich.html"},{"title":"poradenství při transakcích","url":"https://www.pwc.com/cz/cs/poradenstvi-pri-transakcich.html"},{"title":"www2.deloitte.com","url":"https://www2.deloitte.com/content/dam/Deloitte/cz/Documents/legal/Fúze%20a%20akvizice%20CZ.pdf"},{"title":"Igor Mesenský","url":"https://kpmg.com/cz/cs/home/contacts/m/igormesensky.html"}]

Links: [{"title":"Founded Year","url":"https://www.cbinsights.com/company/vicf"},{"title":"Corporate finance","url":"https://www.ecovis.com/czech-republic/services/corporate-finance/"},{"title":"Compare MCF Corporate Finance vs VICF","url":"https://www.cbinsights.com/compare/mcf-corporate-finance-vs-vicf"},{"title":"Schönherr Praha posiluje poradenský tým zaměřený na korporátní právo a akvizice","url":"https://epravo.cz/top/aktualne/schonherr-praha-posiluje-poradensky-tym-zamereny-na-korporatni-pravo-a-akvizice-111987.html"},{"title":"Patria Corporate Finance brožura","url":"https://cf.patria.cz/public/download/Patria Corporate Finance_brožura.pdf"},{"title":"lubomir brecka","url":"https://cm.twobirds.com/en/people/l/lubomir-brecka"},{"title":"jan slaby","url":"https://www.ecovis.com/czech-republic/contact-persons/jan-slaby/"},{"title":"www.deloitte.com","url":"https://www.deloitte.com/southeast-asia/en/about/people/profiles.pdianty+a6442056.html"},{"title":"lubomir brecka","url":"https://twobirds.com/en/people/l/lubomir-brecka"},{"title":"About Lucia Luptáková","url":"https://practiceguides.chambers.com/author/details/64601/THVjaWEgTHVwdMOha292w6E"}]

Hledání našlo několik poskytovatelů M&A poradenství a corporate finance v ČR, z nichž část působí v Praze. Výsledky nejsou hodnocené ani seřazené podle kvality, a některé zdroje jsou starší nebo nepřímé.

**Specializované corporate finance boutiques**

- **Ecovis Corporate Finance CZ (Praha):** Podle webu obsluhuje velké české i zahraniční firmy
… [skrátené, 3066 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 19:57:19

Candidates found in all five categories. Now I'm opening the organisations' own sites to get verbatim quotes, and searching for a Slovak fund-of-funds and a second group holding.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.fundlift.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Fundlift does as a business (e.g. a crowdinvesting/investment platform that connects investors with companies). Also state the company operator name if visible."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.crowdberry.sk",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Crowdberry does (e.g. a crowdinvesting platform where investors buy shares in companies). Also state the company's registered country if visible."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.fingood.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Fingood does (e.g. an investment crowdfunding platform connecting investors with companies). Include the operator company name if visible."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.com",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Investown does (e.g. a crowdfunding/P2P platform financing real-estate projects). Include the operator company name and any CNB licence mention if visible."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://cf.patria.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Patria Corporate Finance does (e.g. M&A advisory, sell-side/buy-side transaction advisory). Include the company name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.ecovis.com/czech-republic/services/corporate-finance/",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Ecovis Corporate Finance does (e.g. advises buyers and sellers in M&A transactions). Include the company name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.woodcompany.com",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Wood & Company does (e.g. investment bank / corporate finance / M&A advisory / brokerage). Include the company name and whether it is an investment bank."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investika.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Investika realitní fond is (e.g. an open-ended real-estate investment fund investing in commercial property). Include the management company name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.agrofert.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what AGROFERT is (e.g. a holding company operating in agriculture, food, chemicals, etc.). Include the company name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.tacr.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Technologická agentura České republiky does (e.g. it is a state grant agency providing funding/support for research and innovation). Include the organisation name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.czechinvest.org",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what CzechInvest does (e.g. a state agency providing investment incentives/grants and support for investors). Include the organisation name."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "Slovensko fond fondov investuje do venture capital fondov SZRB",
  "mode": "standard"
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "slovenská investičná holding skupina akvizície firiem do vlastnej skupiny holding",
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
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.investown.com
    Redirect URL (from the server's Location header — server-supplied, not verified): https://www.investown.cz/
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://www.investown.cz/"
    - prompt: "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Investown does (e.g. a crowdfunding/P2P platform financing real-estate projects). Include the operator company name and any CNB licence mention if visible."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.woodcompany.com
    Redirect URL (from the server's Location header — server-supplied, not verified): https://www.woodcompany.it/
    Status: 302 Found

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://www.woodcompany.it/"
    - prompt: "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Wood & Company does (e.g. investment bank / corporate finance / M&A advisory / brokerage). Include the company name and whether it is an investment bank."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.tacr.cz
    Redirect URL (from the server's Location header — server-supplied, not verified): https://tacr.gov.cz/
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://tacr.gov.cz/"
    - prompt: "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Technologická agentura České republiky does (e.g. it is a state grant agency providing funding/support for research and innovation). Include the organisation name."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.czechinvest.org
    Redirect URL (from the server's Location header — server-supplied, not verified): https://czechinvest.gov.cz/
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://czechinvest.gov.cz/"
    - prompt: "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what CzechInvest does (e.g. a state agency providing investment incentives/grants and support for investors). Include the organisation name."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page doesn't contain a sentence stating what Fundlift does as a business. The content is mostly navigation menus and template placeholders (such as `{{ 'NAVIGATION.CLOSE' | translate }}`), so I can't provide a verbatim quote.

No company operator name is visible either. The only readable text beyond navigation labels is "založení účtu" (Czech for "account creation") and "Kontakty" ("Contacts"), which don't identify the operator or describe its business.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
According to the page: "Fingood je česká crowdfundingová platforma, která propojuje investory s podnikateli."

The operator is Fingood s.r.o., listed as "Provozovatel" in the footer.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Per the Ecovis in the Czech Republic Corporate finance page: "Our experts assist clients – large Czech and foreign companies – both as buyers and as sellers."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**Quote:** "První skutečně prémiový realitní fond i pro drobné investory."

This describes the fund as a premium real-estate fund open to small investors. The page does not say whether the fund is open-ended or what property types it holds. It only says it invests in "špičkových nemovitostí napříč střední Evropou" (top-quality property across Central Europe).

**Management company:** INVESTIKA, investiční společnost, a.s.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page's statement about AGROFERT's role is: "Společnost AGROFERT, a.s., je členem (řídící společností) koncernu AGROFERT."

This says AGROFERT, a.s. is the managing company of the AGROFERT group. The page doesn't call it a holding company or name its industries in that sentence, but its navigation lists chemicals, agriculture, food, forestry, technology and transport, and renewable energy and fuels.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page title states what the company does: "Patria Corporate Finance | Fúze, akvizice a prodej firem na míru" (64 characters). In English, this describes Patria Corporate Finance as offering mergers, acquisitions, and company sales tailored to clients.

The closest body sentence is "Jsme jednou z nejvýznamnějších M&A firem u nás." It describes the firm as one of the most significant M&A firms in the Czech Republic, but it doesn't include the company name.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "Slovensko fond fondov investuje do venture capital fondov SZRB"

Links: [{"title":"venture capital investment team recruitment","url":"https://kitalent.com/sk/financial-services-and-professional-services-recruitment/venture-capital-recruitment/venture-capital-investment-team-recruitment/"},{"title":"Private equity a venture kapitálové fondy pôsobiace v SR","url":"https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr"},{"title":"Popularita private equity a venture kapitálu na Slovensku","url":"https://www.podnikajte.sk/investor/private-equity-venture-kapital-na-slovensku"},{"title":"Portfolio Companies","url":"https://seedtable.com/investors/fond-fondov"},{"title":"About the Company","url":"https://www.sih.sk/en/stranky/o-nas/o-spolocnosti"},{"title":"Crowdberry, Zero Gravity Ventures, and Vision Ventures to invest state money into Slovak start-ups","url":"https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st"},{"title":"What we do","url":"https://eif.org/what_we_do/resources/jeremie/news/2014/slovakia_vc.htm?lang=-en"},{"title":"Slovenský Sandberg Capital uzavřel svůj třímiliardový fond. Stovky milionů z něj investoval do českých firem","url":"https://cc.cz/slovensky-sandberg-capital-uzavrel-svuj-trimiliardovy-fond-stovky-milionu-z-nej-investoval-do-ceskych-firem/"},{"title":"Venture Capital fondovi – prilika za ulaganja u Srbiji?","url":"https://zuniclaw.com/venture-capital-fondovi/"}]

The results don't include a current, official source describing a Slovak "fond fondov" (fund of funds) that invests in venture capital funds through SZRB. They do include older material on SZRB's subsidiary, Slovak Investment Holding (SIH), and a few loosely related items.

**SZRB and SIH (2019)**
- An October 2019 article describes SIH as a subsidiary of the state-owned SZRB bank. It says SIH had chosen three investment vehicles to put about €33m into Slovak start-ups, which could rise to €70m if certain milestones were met Slovak Investment Holding, a subsidiary of the state bank SZRB, has selected three investment vehicles that will invest €33m into Slovak start-ups. Upon meeting some milestones, the sum might rise to €70m. Each of the three selected managers, Crowdberry, Zero Gravity Ventures and Vision Ventures, was slated to oversee €11.6m Crowdberry, Zero Gravity Ventures, and Vision Ventures will manage €11.6m each.

**SIH's broader track record**
- SIH's company timeline lists direct venture stakes in GA Drilling, Boataround and GreenWay. It also notes that a subsidiary, Slovak Asset Management, received a National Bank of Slovakia license to run alternative investment funds, and that SIH created the Venture to Future Fund to provide equity financing to SMEs SIH concludes its first direct venture capital investment in GA Drilling, Boataround, and GreenWay; SIH establishes a subsidiary - Slovak Asset Management (SAM) - which acquir
… [skrátené, 2069 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "slovenská investičná holding skupina akvizície firiem do vlastnej skupiny holding"

Links: [{"title":"SkyNet mění majitele a získává nové investice","url":"https://www.lupa.cz/clanky/skynet-meni-majitele-a-ziskava-nove-investice/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/cms-investicie-do-firiem-sa-vlani-na-s/523048-clanok.html"},{"title":"kretinskeho eph stoupl zisk na dve miliardy eur prispela akvizice slovenskych elektraren","url":"https://forbes.cz/kretinskeho-eph-stoupl-zisk-na-dve-miliardy-eur-prispela-akvizice-slovenskych-elektraren/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/ceske-firmy-vyrazaju-na-dalsie-n/319489-clanok.html"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/vznik-csr-firmy-cr-sr/62511-clanok.html"},{"title":"Křetínský chystá velké investice, EPH chce většinu ve Slovenských elektrárnách","url":"https://oenergetice.cz/spolecnosti/kretinsky-chysta-velke-investice-eph-chce-vetsinu-ve-slovenskych-elektrarnach"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-firmy-kretinsky-chysta-velke-investice-eph-chce-vetsinu-ve-slovenskych-elektrarnach-257528"},{"title":"www.ceskenoviny.cz","url":"https://www.ceskenoviny.cz/zpravy/2554245"},{"title":"Zisk Strnadova CSG loni mírně vzrostl, firma nevylučuje akvizice","url":"https://www.finance.cz/498854-zisk-strnadova-csg-loni-mirne-vzrostl-firma-nevylucuje-akvizice"},{"title":"Slovinsko: národního železničního nákladního dopravce údajně převezme česká skupina EPH","url":"https://www.businessinfo.cz/clanky/slovinsko-narodniho-zeleznicniho-nakladniho-dopravce-udajne-prevezme-ceska-skupina-eph/"}]

Links: [{"title":"SkyNet mění majitele a získává nové investice","url":"https://www.lupa.cz/clanky/skynet-meni-majitele-a-ziskava-nove-investice/"},{"title":"Investoři z Wood & Company prodali okenářský byznys","url":"https://www.e15.cz/byznys/prumysl-a-energetika/investori-z-wood-company-prodali-okenarsky-byznys-1078816"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/vznik-csr-firmy-cr-sr/62511-clanok.html"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-firmy-kretinsky-chysta-velke-investice-eph-chce-vetsinu-ve-slovenskych-elektrarnach-257528"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/ceske-firmy-vyrazaju-na-dalsie-n/319489-clanok.html"},{"title":"kretinskeho eph stoupl zisk na dve miliardy eur prispela akvizice slovenskych elektraren","url":"https://forbes.cz/kretinskeho-eph-stoupl-zisk-na-dve-miliardy-eur-prispela-akvizice-slovenskych-elektraren/"},{"title":"Zisk Strnadova CSG loni mírně vzrostl, firma nevylučuje akvizice","url":"https://www.finance.cz/498854-zisk-strnadova-csg-loni-mirne-
… [skrátené, 4689 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 19:58:53

Several sources came back redirected or blocked, and no Slovak fund-of-funds was found. I have 21 tool calls used, so I'm going to fetch the most promising remaining candidates and run one search for a fund-of-funds.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.investown.cz/",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Investown does (crowdfunding/P2P platform financing real-estate projects for investors). Include the operator company name and any CNB licence mention."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.forvismazars.com/cz/cs/nase-sluzby/transakcni-poradenstvi/transakce/akvizice-a-prodeje-firem-m-a",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what this M&A service does (advises clients on acquisitions and sales of companies). Include the firm name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.trigea.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Trigea does (real-estate investment fund / property fund for investors). Include the company or fund name."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.ephgroup.com",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what EPH is (e.g. an industrial/energy holding company owning companies in its group). Include the company name."
}
````

</details>

<details><summary>🔧 WebSearch</summary>

````text
{
  "query": "fond fondů investuje pouze do jiných investičních fondů Česká republika státní",
  "mode": "standard"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.ephgroup.com
    Redirect URL (from the server's Location header — server-supplied, not verified): https://forsale.godaddy.com/forsale/www.ephgroup.com?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&
    Status: 307 Temporary Redirect

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://forsale.godaddy.com/forsale/www.ephgroup.com?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&"
    - prompt: "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what EPH is (e.g. an industrial/energy holding company owning companies in its group). Include the company name."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The page states: "Nemovitostní fond Trigea nakupuje komerční budovy v dobrých lokalitách."
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
**What Investown does:**
> "Investown je online platforma s investičními úvěry do nemovitostí."

(English: "Investown is an online platform with investment loans for real estate.")

**Operator company:**
> "společnosti Investown Technologies s.r.o."

**CNB licence:**
> "Jsme držitel ČNB licence"

(English: "We are holders of a CNB licence.")
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Quote (Czech, original text):

"Společnost Forvis Mazars poskytuje poradenství" ... "při prodejích a akvizicích společností."

The firm advises a range of clients, from large groups to small businesses, individual entrepreneurs, and different kinds of investors, on company sales and acquisitions. I've split the quote because the full sentence exceeds the 125-character limit.
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
Web search results for query: "fond fondů investuje pouze do jiných investičních fondů Česká republika státní"

Links: [{"title":"2014 ZISIF ve zneni zakona 336 2014","url":"https://www.mfcr.cz/assets/cs/media/2014_ZISIF-ve-zneni-zakona-336-2014.pdf"},{"title":"www.epravo.cz","url":"https://www.epravo.cz/top/zakony/sbirka-zakonu/sb/2004/189"},{"title":"Investment funds in the Czech Republic and their performance","url":"https://vskp.vse.cz/english/87899"},{"title":"zakon ze dne 1 dubna 2004 o kolektivnim investovani 5059","url":"https://www.epravo.cz/top/zakony/sbirka-zakonu/zakon-ze-dne-1-dubna-2004-o-kolektivnim-investovani-5059.html"},{"title":"Srovnání investičních fondů v České republice","url":"https://dspace.zcu.cz/items/b07dc099-1e67-4f20-b12f-b272cb388a43/full"},{"title":"theses.cz","url":"https://theses.cz/id/81yvfc?lang=en"},{"title":"Jak fungují investiční fondy? A kdo hlídá investiční společnosti?","url":"https://dostupnyadvokat.cz/blog/fondy"},{"title":"Title: | Srovnání investičních fondů v České republice |","url":"https://otik.zcu.cz/handle/11025/3273?locale=en"},{"title":"Investment funds in the Czech Republic and their expenses","url":"https://vskp.vse.cz/english/72167"}]

Links: [{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-finance-investice-do-fondu-v-cesku-prekonaly-dvoubilionovou-hranici-283647"},{"title":"Působení zahraničních fondů kolektivního investování v ČR – Bc. Markéta Korandová","url":"https://theses.cz/id/o2zjrv?lang=sk"},{"title":"elearning.tul.cz","url":"https://elearning.tul.cz/pluginfile.php/895488/mod_resource/content/1/VFS%20elearning%2010.pdf"},{"title":"Hra o správce státního seed fondu začíná, na opravu „selhání trhu“ dostane miliardu","url":"https://www.lupa.cz/clanky/hra-o-spravce-statniho-seed-fondu-zacina-na-opravu-selhani-trhu-dostane-miliardu/"},{"title":"Možnosti zhodnocení finančních prostředků drobných investorů prostřednictvím podílových fondů v ČR","url":"https://m.digilib.k.utb.cz/handle/10563/2536?show=full"},{"title":"Diplomová práce","url":"https://is.muni.cz/th/g9ixs/"},{"title":"Kolektivní investování prostřednictvím podílových fondů v ČR","url":"https://digilib.k.utb.cz/handle/10563/35647"},{"title":"Diplomová práce","url":"https://is.muni.cz/th/ehhid/"},{"title":"Kolektivní investování v ČR","url":"https://dspace-test.jcu.cz/handle/123456789/37536"}]

Links: [{"title":"Ministerstvo financí navrhuje nová pravidla pro fondový byznys","url":"https://www.epravo.cz/top/clanky/ministerstvo-financi-navrhuje-nova-pravidla-pro-fondovy-byznys-82479.html"},{"title":"novela zisif zjednodusuje administrativu novinky v zakone o investicnich spolecnostech a investicnich fondech 118427","url":"https://www.epravo.cz/top/clanky/novela-zisif-zjednodusuje-administrativu-novinky-v-zakone-o-investicnich-spolecnostech-a-investicnich-fondech-118427.html?pdf=1"},{"title":"Tabulka 2013 01 17 Tabulka zakladnich regulatornich pozadavku investicni fondy","url":"https://www.mfcr.cz/ass
… [skrátené, 7694 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 20:00:21

Investown, Trigea, Investika, Agrofert, Fingood and the Patria and Ecovis pages are verified. EPH redirects to a parked domain, so it's out. Two calls remain before the write: one for a P2P platform (Zonky) and one for the Central European Fund of Funds, the only fund-of-funds with a Czech state link that the search turned up.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://www.zonky.cz",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Zonky does (peer-to-peer lending platform connecting private lenders with borrowers). Include the operator company name if visible."
}
````

</details>

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://eif.org/what_we_do/equity/news/2018/80-million-central-europe-fund-of-funds-to-support-smes-and-small-mid-caps.htm",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what the Central Europe Fund of Funds does (invests in venture/private equity funds, not directly in companies). Include which institutions (e.g. ČMZRB, Slovak/Slovenian partners) participate."
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
The page's sentence describing what Zonky does is:

> "Nabízíme půjčky od lidí pro lidi."

In English, this means Zonky offers loans from people for people. The page doesn't use the term "peer-to-peer." The operator named in the footer is **Air Bank a.s.**, a member of the PPF group, which provides the Zonky service.
````

</details>

### 🤖 Claude · 2026-10-08 20:00:36

Zonky verified. The EIF page returned 404, so no fund-of-funds could be verified. I have one call left before the write, so I'm using it on the Technology Agency of the Czech Republic (TA CR) as the grant-agency control.

<details><summary>🔧 WebFetch</summary>

````text
{
  "url": "https://tacr.gov.cz/",
  "prompt": "Quote verbatim (exact characters, max 200 chars) the sentence on this page that states what Technologická agentura České republiky does (state grant agency funding research and innovation projects). Include the organisation name."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
The server returned HTTP 503 Service Unavailable.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
````

</details>

### 🤖 Claude · 2026-10-08 20:00:58

The last tool call is the file write. I'm writing the 9 rows I could verify from their own sites and validating the JSON in the same call. The rest of the control set could not be filled within budget.

<details><summary>🔧 Bash – Create discovery folder and write controls JSON, then validate it</summary>

````text
{
  "command": "mkdir -p \"/c/Users/matus/Desktop/Interview_Project/Project_a/data/raw/agents/discovery\" && cat > \"/c/Users/matus/Desktop/Interview_Project/Project_a/data/raw/agents/discovery/controls.json\" <<'EOF'\n[\n  {\n    \"name\": \"Fingood s.r.o.\",\n    \"website\": \"https://www.fingood.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"crowdfunding\",\n    \"expected_rejection\": \"E3\",\n    \"source_url\": \"https://www.fingood.cz\",\n    \"quote\": \"Fingood je česká crowdfundingová platforma, která propojuje investory s podnikateli.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Investown Technologies s.r.o.\",\n    \"website\": \"https://www.investown.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"crowdfunding\",\n    \"expected_rejection\": \"E3\",\n    \"source_url\": \"https://www.investown.cz/\",\n    \"quote\": \"Investown je online platforma s investičními úvěry do nemovitostí.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Zonky (Air Bank a.s.)\",\n    \"website\": \"https://www.zonky.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"crowdfunding\",\n    \"expected_rejection\": \"E3\",\n    \"source_url\": \"https://www.zonky.cz\",\n    \"quote\": \"Nabízíme půjčky od lidí pro lidi.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Patria Corporate Finance\",\n    \"website\": \"https://cf.patria.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"advisory\",\n    \"expected_rejection\": \"E3\",\n    \"source_url\": \"https://cf.patria.cz\",\n    \"quote\": \"Jsme jednou z nejvýznamnějších M&A firem u nás.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Ecovis Corporate Finance CZ\",\n    \"website\": \"https://www.ecovis.com/czech-republic/\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"advisory\",\n    \"expected_rejection\": \"E3\",\n    \"source_url\": \"https://www.ecovis.com/czech-republic/services/corporate-finance/\",\n    \"quote\": \"Our experts assist clients – large Czech and foreign companies – both as buyers and as sellers.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Forvis Mazars CZ\",\n    \"website\": \"https://www.forvismazars.com/cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"advisory\",\n    \"expected_rejection\": \"E3\",\n    \"source_url\": \"https://www.forvismazars.com/cz/cs/nase-sluzby/transakcni-poradenstvi/transakce/akvizice-a-prodeje-firem-m-a\",\n    \"quote\": \"Společnost Forvis Mazars poskytuje poradenství\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Investika realitní fond (INVESTIKA, investiční společnost, a.s.)\",\n    \"website\": \"https://www.investika.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"real_estate\",\n    \"expected_rejection\": \"E4\",\n    \"source_url\": \"https://www.investika.cz\",\n    \"quote\": \"První skutečně prémiový realitní fond i pro drobné investory.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"Trigea (Nemovitostní fond Trigea)\",\n    \"website\": \"https://www.trigea.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"real_estate\",\n    \"expected_rejection\": \"E4\",\n    \"source_url\": \"https://www.trigea.cz\",\n    \"quote\": \"Nemovitostní fond Trigea nakupuje komerční budovy v dobrých lokalitách.\",\n    \"accessed_date\": \"2026-10-08\"\n  },\n  {\n    \"name\": \"AGROFERT\",\n    \"website\": \"https://www.agrofert.cz\",\n    \"hq_country_claimed\": \"CZ\",\n    \"control_category\": \"group_holding\",\n    \"expected_rejection\": \"E6\",\n    \"source_url\": \"https://www.agrofert.cz\",\n    \"quote\": \"Společnost AGROFERT, a.s., je členem (řídící společností) koncernu AGROFERT.\",\n    \"accessed_date\": \"2026-10-08\"\n  }\n]\nEOF\npython -c \"import json,sys; d=json.load(open(sys.a
… [skrátené, 240 znakov – plné znenie v raw/]
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
9 rows valid
````

</details>

<details><summary>🔧 SubagentHandback</summary>

````text
{
  "message": "Wrote 9 rows to C:\\Users\\matus\\Desktop\\Interview_Project\\Project_a\\data\\raw\\agents\\discovery\\controls.json (valid UTF-8 JSON, all rows verified against the organisations' own sites).\n\nPer category: crowdfunding 3 (Fingood, Investown, Zonky), advisory 3 (Patria Corporate Finance, Ecovis Corporate Finance CZ, Forvis Mazars CZ), real_estate 2 (Investika, Trigea), group_holding 1 (AGROFERT), fund_of_funds 0, other 0.\n\nShortfall vs. the 12-15 target: no fund-of-funds and only one group holding were verified within the 30-call budget. Candidates that failed: Fundlift (JS-only page, no quote), Crowdberry.sk (HTTP 429), Wood & Company (redirects to woodcompany.it), EPH (redirects to a parked domain), EIF Central Europe Fund of Funds (404), TA CR (503), CzechInvest (redirect not followed).\n\nSurprising: Zonky's operator is Air Bank a.s. (PPF group). The Forvis quote is a partial sentence because the full one was split across the page."
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
{"success":true,"message":"Report delivered to your caller."}
````

</details>

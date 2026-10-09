# Plán: Spoľahlivá databáza investorov

*Verzia 1 – 8. 10. 2026. Zmeny plánu sa zaznamenávajú v [DECISIONS.md](DECISIONS.md) a v histórii gitu.*

## 1. Cieľ a princíp

Cieľom je databáza investorov do firiem, v ktorej:

1. **každý záznam je skutočný investor**, nie firma, ktorá sa tak len volá;
2. **každý údaj** (typ, sektor, štádium, výška tiketu, celkový kapitál, sídlo) **má vlastný zdroj** – URL, vydavateľa,
   dátum publikácie, dátum prístupu a doslovnú citáciu, ktorá údaj dokladá;
3. pri každom investorovi je **datovaný doklad o skutočnej investícii**.

Hlavný princíp: **jazykový model nič nevymýšľa, iba nachádza a cituje.** Každé tvrdenie agenta sa strojovo overí
(stiahne sa zdroj a skontroluje sa, či citácia na stránke naozaj je). Čo nemá zdroj, v databáze nie je – radšej
prázdne pole s označením `not_public` než odhad.

## 2. Kto je investor (definícia)

**Investor** je subjekt (alebo fyzická osoba, ktorá sa sama verejne prezentuje ako investor), ktorý **opakovane**
poskytuje **vlastný alebo spravovaný kapitál** **súkromným prevádzkovým firmám** formou **vlastného imania alebo
kvázi-vlastného imania** (podiely, akcie, konvertibilné úvery, SAFE).

### Typy investorov (taxonómia)

| Kód | Typ | Stručne |
|---|---|---|
| `vc` | Venture capital fond/firma | investuje do startupov a rýchlo rastúcich firiem (pre-seed až growth) |
| `cvc` | Korporátny VC | investičné rameno korporácie/banky, investuje do **externých** firiem |
| `public_vc` | Verejný/štátny VC | štátom vlastnený subjekt, ktorý **priamo** investuje do firiem |
| `pe` | Private equity | väčšinové/rastové investície do etablovaných firiem, buyouty |
| `family_office` | Family office (single/multi) | spravuje majetok rodiny, priamo investuje do firiem |
| `angel` | Angel investor | fyzická osoba investujúca vlastné peniaze |
| `angel_network` | Siete a syndikáty angel investorov | klub/syndikát, ktorý spoločne investuje |
| `accelerator_equity` | Akcelerátor s podielom | program, ktorý za podiel poskytuje kapitál |
| `private_investor` | Veľký súkromný investor | HNWI investujúci priamo (často cez holding) |

## 3. Pravidlá zaradenia (musia platiť všetky)

| Pravidlo | Znenie | Ako sa overí |
|---|---|---|
| **I1 Identita** | Subjekt je identifikovateľný: má registračné číslo (IČO, LEI, company no.) alebo, ak ide o osobu, verejný investorský profil, ktorý sám zverejnil. | Vyhľadanie v registri (ARES pre CZ, RPO/ORSR pre SK, GLEIF, Companies House…) |
| **I2 Aktivita** | Aspoň **2 zdokumentované investície** celkovo, z toho **aspoň 1 datovaná v posledných 36 mesiacoch** pred dátumom `as_of`. Výnimka pre nový fond (≤ 24 mesiacov): datované uzavretie fondu + aspoň 1 investícia. | Datované zdroje: tlačové správy, správy médií, registre (zmena spoločníkov), portfólio |
| **I3 Druh kapitálu** | Poskytuje vlastné imanie alebo kvázi-vlastné imanie firmám. | Popis stratégie + charakter zdokumentovaných investícií |
| **I4 Typ** | Dá sa zaradiť do jedného z typov v taxonómii (môže mať viac typov). | Vlastný popis + regulačný status + charakter investícií |
| **I5 Rozsah pilotu** | *Len pre pilot:* typ `vc`, `cvc` alebo `public_vc` a **sídlo investičného tímu v CZ alebo SK**. | Adresa správcovskej spoločnosti / tímu (nie domicil fondu) |

## 4. Pravidlá vyradenia (stačí jedno)

| Kód | Dôvod vyradenia | Príklad |
|---|---|---|
| **E1** | Žiadny datovaný doklad o investícii – iba vlastné tvrdenie | web „investujeme do startupov“, ale žiadna konkrétna investícia |
| **E2** | Neaktívny > 36 mesiacov, alebo zrušený / v likvidácii | posledná investícia 2021; firma v likvidácii podľa registra |
| **E3** | Sprostredkovateľ, nie investor | crowdfundingová platforma, broker, M&A poradca, advokátska/audítorská kancelária, akcelerátor bez vlastného kapitálu |
| **E4** | Iná trieda aktív | realitný fond, hedge fond / verejné akcie, čisto dlhový veriteľ |
| **E5** | Investuje len do fondov (LP / fond fondov) | štátny fond fondov, ktorý sám priamo neinvestuje |
| **E6** | Investuje len v rámci vlastnej skupiny / strategický nadobúdateľ | holding kupujúci firmy do svojej skupiny |
| **E7** | **Zhoda len podľa názvu** – „náhodná firma“ | „XY Invest s.r.o.“, „ABC Capital a.s.“ bez jedinej investície |
| **E8** | Duplicita / alias | ten istý investor pod iným názvom, správcovská spoločnosť vs. fond |
| **E9** | Len grantová agentúra | dotačná schéma bez vlastného imania |
| **OOS** | Skutočný investor, ale **mimo rozsahu pilotu** | PE fond, angel sieť, VC so sídlom v Rakúsku – uvádza sa v samostatnom zozname, nepočíta sa ako chyba |

## 5. Hraničné prípady (rozhodovacia tabuľka)

Každý prípad má v kóde vlastný test (`tests/test_rules.py`).

| Situácia | Rozhodnutie | Dôvod |
|---|---|---|
| Štátny program, ktorý len vkladá peniaze do iných fondov (napr. fond-fondov) | **E5** | investuje do fondov, nie do firiem |
| Dcérska spoločnosť štátneho programu, ktorá investuje priamo (napr. Venture to Future Fund) | **zaradiť** ako `public_vc` | spĺňa definíciu investora |
| Pražský/bratislavský tím spravuje fond domicilovaný v Luxembursku/Holandsku | **sídlo = CZ/SK** | rozhoduje, kde sa robia investičné rozhodnutia |
| VC rameno banky alebo korporácie investuje do externých startupov | **zaradiť** ako `cvc` | externé investície = investor |
| Holding investuje len do firiem vlastnej skupiny | **E6** | nie je to investor na trhu |
| Správca s VC aj PE stratégiou | viac typov; v pilote **áno**, ak má doloženú VC stratégiu | jeden subjekt, viac typov |
| Crowdinvestingová platforma, ktorá zároveň spravuje vlastný fond | platforma **E3**; fond posudzovaný samostatne | sprostredkovanie ≠ investovanie |
| IČO správcu vs. IČO fondu vs. sesterská s.r.o. s rovnakou značkou | **1 záznam na investičnú firmu/značku**; ostatné IČO ako aliasy | používateľ databázy hľadá investora, nie právnu štruktúru |
| Akcelerátor, ktorý berie podiel | typ `accelerator_equity` → v pilote **OOS** | nie je to VC fond |

## 6. Čo sa o každom investorovi eviduje

Každý údaj je uložený ako samostatné **tvrdenie (claim)**:

| Pole tvrdenia | Význam |
|---|---|
| `investor_id`, `field`, `value` | ku ktorému investorovi a poľu sa údaj viaže a jeho hodnota |
| `source_url`, `publisher` | odkiaľ údaj pochádza |
| `published_date`, `accessed_date` | kedy bol zdroj publikovaný a kedy sme ho čítali |
| `quote` | doslovná citácia (≤ 300 znakov), ktorá údaj dokladá |
| `source_tier` | úroveň dôveryhodnosti zdroja (T1–T4, kap. 7) |
| `derivation` | `stated` (zdroj to priamo uvádza) alebo `inferred` (odvodené, napr. sektory z portfólia) |
| `auto_check` | výsledok strojovej kontroly citácie (kap. 8) |

Tabuľka `investors.csv` je čitateľný prehľad (1 riadok = 1 investor), `claims.csv` je dôkazová vrstva
(1 riadok = 1 údaj so zdrojom).

### Definície polí

| Pole | Definícia | Ak nie je verejné |
|---|---|---|
| **Typ** | podľa taxonómie (kap. 2), môže byť viac typov | — (bez typu nie je zaradený) |
| **Sídlo** | krajina investičného tímu / správcovskej spoločnosti | — |
| **Sektory** | pevný slovník (nižšie); označenie `stated` vs. `inferred` z portfólia | `inferred` z doložených investícií |
| **Štádiá** | `pre_seed`, `seed`, `series_a`, `series_b_plus`, `growth`, `buyout` | odvodené z doložených kôl |
| **Tiket** | min / typický / max v EUR + pôvodná mena a dátum kurzu (ECB) | `derived` z doložených kôl, inak `not_public` |
| **Celkový kapitál** | AUM alebo súčet upísaných veľkostí fondov; `capital_type` + dátum `as_of`. Cieľová veľkosť fondu (pred uzavretím) sa označí ako `target` | `not_public` |
| **Doložené investície** | firma, dátum, kolo, zdroj | — (bez nich nie je zaradený) |

**Slovník sektorov:** `ai_data`, `enterprise_saas`, `fintech_insurtech`, `health_digital`, `life_sciences_medtech`,
`deeptech_hardware`, `cleantech_energy`, `mobility_logistics`, `consumer_ecommerce`, `edtech`,
`proptech_construction`, `agri_food`, `cybersecurity`, `media_gaming`, `industry_manufacturing`, `iot_telecom`,
`hr_worktech`, `travel_hospitality`, `govtech_legaltech`, `defense_space`, + `sector_agnostic`.

## 7. Zdroje a ich dôveryhodnosť

Používajú sa **výhradne verejne dostupné zdroje**. Platené databázy (PitchBook, Preqin, Dealroom Pro, Crunchbase Pro)
sa nepoužívajú; ich verejné stránky slúžia nanajvýš na **nájdenie kandidátov**, nikdy ako jediný dôkaz.

| Úroveň | Zdroje | Použitie |
|---|---|---|
| **T1** | Registre a regulátori: ARES (CZ), RPO/ORSR (SK), registre ČNB a NBS, ESMA (EuVECA, AIFM), GLEIF; oficiálne zverejnenia investorov do fondov (EIF, Slovak Investment Holding, Národní rozvojová banka) | samostatný dôkaz |
| **T2** | Web investora, jeho portfólio a tlačové správy | dôkaz (ale vlastné tvrdenie) |
| **T3** | Dôveryhodné médiá (CzechCrunch, Forbes CZ/SK, Hospodářské noviny, E15, Trend, Startitup…) a tlačové správy startupov | dôkaz |
| **T4** | Agregátory (Dealroom, PitchBook, Vestbee – verejné stránky) | **len na objavovanie kandidátov** |

Nepoužíva sa LinkedIn ani iné zdroje, ktorých podmienky zakazujú automatický zber dát.

## 8. Ako sa overí pravosť a správne zaradenie

Postup má päť vrstiev. Každá chytá iný druh chyby.

```
 Kandidáti ──► 1. Identita ──► 2. Dôkazy ──► 3. Strojová ──► 4. Pravidlá ──► 5. Nezávislý ──► 6. Ručná
 (zoznamy A,B,   v registri    (AI agent      kontrola      a skóre        AI overovateľ   kontrola
  návnady)       (IČO, stav)    s citáciami)   citácií       (A/B/C)        (iný prompt)    vzorky
```

1. **Identita v registri** – subjekt musí existovať (IČO/LEI) a nesmie byť v likvidácii. Chytá vymyslené alebo
   zaniknuté subjekty.
2. **Zber dôkazov (AI agent)** – agent (Claude Haiku 5.5) dostane prísny pokyn: každé pole = URL + doslovná citácia +
   dátum; ak nič nenájde, vráti `not_found`; čísla nesmie odhadovať ani dopočítavať.
3. **Strojová kontrola citácií (Python, bez AI)** – stiahne každý zdroj, porovná citáciu s textom stránky
   (fuzzy zhoda ≥ 90 %), skontroluje, či hodnota v citácii naozaj je, a overí dátum. Výsledok:
   `ok`, `url_dead`, `quote_not_found`, `value_not_in_quote`, `stale`, `blocked`.
   **Tvrdenie, ktoré neprejde, sa zahodí.** Toto je hlavná ochrana pred „halucináciami“.

   **3b. Významové kontroly (pridané v audite pred ručnou kontrolou, [AUDIT_V2.md](AUDIT_V2.md)).** Pravá citácia
   ešte neznamená správny výklad. Kód preto ďalej overuje:

   - či je investor v citácii alebo pri nej **menovaný** (priradenie);
   - či citácia opisuje **obchod**, alebo len zmienku či exit (iba dátum obchodu sa počíta do aktivity);
   - či je fond **uzavretý**, alebo len cieľ či plán (cieľ sa nepočíta do kapitálu);
   - či sú sumy **reálne** (kontrola rozumnosti, prevod meny s uvedeným kurzom).
4. **Pravidlá a skóre** – kód (`rules.py`) aplikuje pravidlá I1–I5 / E1–E9 a pridelí úroveň dôvery:
   - **A**: identita z registra + ≥ 2 datované investície z ≥ 2 nezávislých zdrojov T1–T3, aspoň 1 v posledných 36 mesiacoch;
   - **B**: identita z registra + ≥ 1 datovaná investícia v posledných 36 mesiacoch zo zdroja T1–T3;
   - **C**: len T4 alebo vlastné tvrdenia, alebo neúspešná kontrola citácií → `NEEDS_REVIEW`, **do databázy sa nedostane**.
5. **Nezávislý AI overovateľ** – druhý agent s iným pokynom znovu posúdi zdroje a zaradenie **bez toho, aby videl
   verdikt prvého agenta**. Pri nezhode ide záznam na ručnú kontrolu.
6. **Ručná kontrola náhodnej vzorky** – človek overí záznamy priamo zo zdrojov (pozri kap. 9). Zároveň sa zmeria,
   ako často sa AI overovateľ zhoduje s človekom – to určuje, koľko ručnej práce treba pri rozšírení na celý svet.

**Kontrola „nie náhodná firma“:** do pilotu sa zámerne pridá ~15 **návnad** – firiem, ktoré vyzerajú ako investori
(„… Capital“, „… Invest“, „… Ventures“ s NACE 64.30/66.30), crowdfundingové platformy, M&A poradcovia, realitné
fondy, fond fondov. Postup ich musí vyradiť so správnym kódom.

## 9. Vopred stanovené metriky (pred spustením pilotu)

Metriky sú definované **pred** zberom dát, aby sa výsledok nedal dodatočne „prispôsobiť“. Pred ručnou kontrolou sa
dáta zmrazia (`git tag pilot-frozen`) a dátum zmrazenia sa stáva dátumom `as_of`.

| Metrika | Definícia |
|---|---|
| **Primárna: presnosť záznamov** | Podiel zaradených záznamov, pri ktorých človek zo zdrojov potvrdí **všetko**: skutočný investor ∧ aktívny v 36 mesiacoch pred `as_of` ∧ správny typ (VC) ∧ správne sídlo (CZ/SK). Bodový odhad + **95 % Wilsonov interval spoľahlivosti**. |
| Presnosť jednotlivých polí | sektory, štádiá, tiket, kapitál – zvlášť (sú subjektívnejšie, preto nie sú v primárnej metrike) |
| Vyplnenosť polí | podiel záznamov, kde je pole verejne doložené |
| Podpora citácií | podiel tvrdení, ktorých citácia sa strojovo našla na zdrojovej stránke |
| Správnosť vyradenia | zvlášť pre skutočné vyradené záznamy a zvlášť pre návnady |
| Zhoda AI overovateľa s človekom | percento zhody a Cohenovo κ |
| Pokrytie (odhad úplnosti) | metóda capture–recapture (Lincoln–Petersen) z dvoch nezávislých zoznamov kandidátov; ide o **dolný odhad**, lebo oba zoznamy uprednostňujú viditeľných investorov |

**Ručne overená vzorka:** náhodný stratifikovaný výber s pevným seedom – ~30 zaradených záznamov (ak je zaradených
≤ 35, overia sa všetky) + ~10 vyradených (5 skutočných + 5 návnad), v náhodnom poradí, **bez** zobrazenia skóre,
verdiktu AI overovateľa a citácií agenta (kontrolór si zdroje otvára sám). Záznamy použité pri ladení pokynov pre
agentov sa do vzorky nezaraďujú.

## 10. Pilot: VC investori so sídlom v CZ a SK

**Prečo CZ + SK:** samotné Slovensko má podľa prvotného prieskumu len jednotky až nízke desiatky aktívnych VC
investorov – na zmysluplné meranie presnosti je to málo (interval spoľahlivosti by bol príliš široký). Česko a
Slovensko majú prepojený ekosystém (veľa fondov pôsobí v oboch krajinách), spoločný jazykový priestor a verejné
registre (ARES, RPO). Rozhodnutie je zdôvodnené v [DECISIONS.md](DECISIONS.md).

**Postup:**

1. **Zoznam A (štruktúrované zdroje):** členovia SLOVCA a CVCA, fondy podporené SIH/NDF II, VTFF a NRB, zoznam EIF,
   registre ESMA, ČNB a NBS.
2. **Zoznam B (správy o investíciách):** AI agenti nezávisle (bez znalosti zoznamu A) hľadajú investorov uvedených v
   investičných kolách českých a slovenských startupov 2023–2026.
3. **Návnady:** ~15 subjektov, ktoré musia byť vyradené.
4. Spolu **~80–100 kandidátov** → zber dôkazov → kontroly → zmrazenie → ručná kontrola vzorky → meranie.

Prekryv zoznamov A a B zároveň slúži na odhad, koľko investorov **nenašiel ani jeden** zoznam (capture–recapture).

## 11. Odhad rozsahu dostupného z verejných zdrojov a spoľahlivosti

### 11.1 Kotvy – overené čísla

Čísla našli AI agenti, ale do odhadu sa dostali až po strojovom overení: skript stiahol zdroj a overil, že citácia s
číslom na stránke naozaj je (`python -m investordb.cli check-quotes data/reference/universe_anchors.csv`, výsledok v
[universe_anchors_checked.csv](../data/reference/universe_anchors_checked.csv)).

| Kotva | Hodnota | Stav k | Zdroj | Overenie |
|---|---|---|---|---|
| Aktívne PE + VC firmy v Európe | **3 095** firiem, AUM 1,25 bil. € | 2024 | Invest Europe (cez tech.eu) | ✅ citácia nájdená |
| Aktívni správcovia PE (vrátane VC) v databáze Preqin | **31 653 – 34 100** | 2025/26 | preqin.com, CBS Library | ✅ |
| Investori a fondy v databáze Dealroom (všetky typy) | **100 000+** | 2026 | dealroom.co | ✅ |
| Single family offices vo svete | **8 030** | 2024 | Deloitte Private | ✅ |
| Aktívni angel investori v USA | **445 535** | 2024 | UNH Center for Venture Research (PDF) | ✅ |
| Angel investori v európskych sieťach | **~39 400** | 2021 | EBAN | ✅ |
| Registrované fondy EuVECA v EÚ | **462** | 12/2022 | Európska komisia (REFIT) | ✅ |
| VC firmy v USA | **3 417** (2023); **2 984** (2025) | 2023 / 2025 | NVCA Yearbook | ⚠️ stránka blokuje sťahovanie (HTTP 403) → ručne |
| Poradcovia a fondy VC/PE (Form PF) | – | 2025Q4 | SEC | ⚠️ blokované → zatiaľ nepoužité |

Jedno číslo agent uviedol chybne: „~10 300 PE správcov podľa Preqin“ sa na citovanej stránke nenachádza (stránka dnes
uvádza 34 100). Kontrola ho vyradila – pozri [AI_WORKFLOW.md](AI_WORKFLOW.md), chyba C7.

### 11.2 Odhad: koľko investorov sa dá z verejných zdrojov doložiť

Postup: **známy trh** (kotvy) → **verejne viditeľní** → **doložiteľní datovaným dôkazom** (= čo sa dostane do databázy).
Podiely v druhom a treťom kroku sú **predpoklady**. Pre VC ich zmeria pilot (podiel zaradených kandidátov, pokrytie cez
capture–recapture) a tabuľka sa po pilote aktualizuje.

| Typ | Známy trh (kotva) | Predpoklad: podiel doložiteľných s aktivitou v 36 mes. | **Odhad záznamov** | Prečo tento predpoklad |
|---|---|---|---|---|
| VC (vrátane CVC, verejných VC) | ~10–15 tis. VC firiem globálne. USA ~3–3,4 tis. (NVCA), Európa ~1,5–2 tis. (časť z 3 095 PE+VC). Preqin pokrýva 31–34 tis. PE+VC správcov | 60–75 % | **6–11 tis.** | VC fondy investície zverejňujú (marketing voči zakladateľom aj investorom), časť firiem je však neaktívna (fondy po investičnom období) |
| PE (buyout, growth) | ~17–24 tis. (Preqin 31–34 tis. mínus VC) | 40–60 % | **8–13 tis.** | veľké PE transakcie sa ohlasujú; menší správcovia a holdingové štruktúry menej |
| Family office | 8 030 SFO (Deloitte) + multi-family offices | 10–25 % | **1–2,5 tis.** | FO sa zámerne vyhýbajú publicite; viditeľné sú najmä tie, ktoré investujú do startupov |
| Angel investori | USA 445 tis. aktívnych (UNH), Európa 39 tis. v sieťach (EBAN), zvyšok sveta neznámy | 3–8 % | **15–40 tis.** | verejne menovaní sú len angel investori v ohlásených kolách; v EÚ navyše GDPR → len vlastné verejné profily |
| Veľkí súkromní investori, angel siete, akcelerátory | čiastočný prekryv s FO a angel investormi | – | **2–5 tis.** | – |
| **Spolu** | | | **~32–70 tis., základný odhad ~45 tis.** | |

**Kontrola rozumnosti:** Dealroom eviduje 100 000+ „investorov a fondov“ (vrátane neaktívnych, právnych vehiklov fondov
a jednorazových investorov). Odhad ~45 tis. **overiteľných a aktívnych** investorov je približne polovica, čo je
konzistentné s tým, že naše pravidlá (≥ 2 investície, aktivita v 36 mesiacoch, datovaný dôkaz) zámerne vyraďujú
neaktívnych a nedoložiteľných.

### 11.3 Očakávaná spoľahlivosť

Hypotézy; pre VC ich pilot zmeria a doplní skutočné hodnoty.

| Údaj | VC / PE | Family office | Angel |
|---|---|---|---|
| Je to skutočný a aktívny investor (presnosť po kontrolách) | ≥ 95 % | 85–90 % | 80–90 % (zámena mien) |
| Správny typ | 90–95 % | 80–90 % (FO vs. rodinný holding) | ~90 % |
| Sektory – vyplnenosť / presnosť | ~90 % / 85–90 % | ~50 % / ~75 % | ~60 % / ~75 % |
| Tiket – vyplnenosť | 60–75 % | 10–20 % | 20–40 % (len odvodené z kôl) |
| Celkový kapitál – vyplnenosť | 50–70 % (veľkosti fondov sa ohlasujú) | 5–15 % | ~0 % (nie je verejný) |

**Z čoho odhad vychádza:** (1) z overených kotiev v 11.1; (2) z povahy verejného zverejňovania jednotlivých typov –
VC a PE fondy zverejňujú investície aj veľkosti fondov, lebo potrebujú dôveru investorov aj zakladateľov, kým family
office a angel investori nie; (3) po pilote z merania: podiel kandidátov s datovaným dôkazom, vyplnenosť polí,
presnosť z ručnej kontroly a odhad pokrytia (capture–recapture). Rozpätia sú zámerne široké – najväčšia neistota je
mimo USA a Európy (Ázia, najmä Čína, kde sú zdroje v miestnom jazyku).

## 12. Odhad nákladov na rozšírenie na celý svet – metodika

Náklady sa **nemajú hádať, ale odvodiť z merania v pilote**:

- **AI náklady:** spotreba tokenov na jedného kandidáta (objavovanie + zber dôkazov + overovateľ) sa spočíta zo
  záznamov agentov (`usage.py`) a prenásobí aktuálnym cenníkom API (s dátumom).
- **Ľudská práca:** minúty ručnej kontroly na záznam (merané v pilote) × veľkosť kontrolnej vzorky potrebnej na
  zvolenú presnosť (n = z²·p·(1−p)/E² na segment, napr. ≈ 140 záznamov pre ±5 p. b. pri p = 0,9) × hodinová sadzba.
- **Ďalšie vstupy:** pomer kandidátov k zaradeným záznamom, viacjazyčnosť (citlivostná analýza 1× / 2× / 4×),
  pravidelná aktualizácia (štvrťročné preverenie aktivity), infraštruktúra.
- Výsledok v scenároch **nízky / základný / vysoký**; komerčné databázy len ako porovnanie.

Detail bude v `docs/COST_ESTIMATE.md`.

## 13. Riziká a obmedzenia

| Riziko | Dopad | Opatrenie |
|---|---|---|
| AI agent si vymyslí zdroj alebo citáciu | nepravdivý záznam | strojová kontrola citácií; tvrdenie bez opory sa zahodí |
| Stránky blokujú sťahovanie (403, JavaScript, PDF) | tvrdenie sa nedá overiť strojovo | označenie `blocked` → ručná kontrola; PDF cez `pypdf` |
| Zastarané údaje na weboch investorov (tiket, AUM) | nepresné polia | dátum `as_of` pri každom údaji; uprednostniť datované zdroje |
| Family office a angel investori sú neverejní | nízka vyplnenosť a pokrytie | pravidlo „radšej prázdne než odhad“; realistický odhad pokrytia |
| GDPR pri fyzických osobách | právne riziko | pilot obsahuje len právnické osoby; pre celý svet len osoby s vlastným verejným investorským profilom a minimom údajov |
| Malá vzorka | široký interval spoľahlivosti | CZ + SK namiesto len SK; interval sa vždy uvádza |

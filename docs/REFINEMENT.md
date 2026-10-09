# Spresnenie slabých polí silnejším modelom (D38)

*Generované skriptom `python -m investordb.cli refine report` (`as_of` = 2026-10-09). Zmrazená databáza (tag `pilot-frozen-v3`) zostáva nezmenená a meraná v [PRECISION_REPORT.md](PRECISION_REPORT.md); spresnená verzia je v `data/processed/investors_refined.csv`.*

## 1. Prečo

Slepá kontrola vzorky (Sonnet 5.5) a ručná kontrola autora ukázali, že **kto** je v databáze, je správne (23/23), ale dve polia sú slabé: **celkový kapitál** (správny len v 6 z 12 hodnotených záznamov – cieľové veľkosti fondov a prvé uzavretia počítané ako uzavreté fondy, staršie fondy chýbali) a **dátumy obchodov** (zdroje sedeli v 19 z 23 záznamov – ako dátum obchodu sa niekedy použil dátum článku, ktorý staršiu investíciu len spomína). Haiku na takéto čítanie článkov nestačil.

## 2. Ako

- **Agent:** Claude Sonnet 5.5, [pokyn](../prompts/refine_agent.md), 6 agentov po 4 investoroch – všetkých 24 zaradených. Dostal, čo databáza tvrdí (fondy, datované obchody), a mal to overiť.
- **Úloha A – fondy:** každý fond so stavom zbierky (`final_close` / `first_close` / `target`), sumou a doslovnou citáciou. Kapitál = súčet uzavretých fondov + prvých uzavretí; cieľ sa nepočíta. Program navyše odmietne sumu, pred ktorou citácia hovorí „target / cieľová / až“ (`target_near`), aj keď agent tvrdí opak.
- **Úloha B – dátumy:** pre každý započítaný obchod dátum, keď bola investícia prvýkrát oznámená, s verdiktom potvrdený / opravený / nenájdený / iný investor.
- **Rovnaké strojové kontroly** ako všetky ostatné tvrdenia: citácia na stránke, hodnota v citácii, kontext obchodu, priradenie investorovi.
- **Pravidlá zlúčenia:** overený spresnený dátum nahradí pôvodný; dátum, ktorý agent nepotvrdil, sa prestane počítať (firma ostane v portfóliu ako zmienka); ak by záznam po spresnení prestal spĺňať pravidlá, nevyradí sa, ale ide na ručnú kontrolu (`REVIEW_REFINED`).

## 3. Strojové kontroly spresnených tvrdení

| Pole | Výsledok kontroly | Počet |
|---|---|---|
| fondy | `ok` | 62 |
| investície | `forbidden_source` | 1 |
| investície | `ok` | 82 |
| investície | `quote_not_found` | 1 |
| investície | `url_dead` | 1 |

Stav fondov podľa agenta: uzavretý fond 25×, len cieľ / plán 22×, prvé uzavretie 15×.  
Verdikty k dátumom obchodov: dátum potvrdený 44×, dátum opravený 23×, nový novší obchod 18×, dátum sa nenašiel 1×.

## 4. Čo sa v databáze zmenilo

- Kapitál vyplnený: 15/24 → **20/24**; zmenená hodnota pri **13** investoroch.
- Posledný obchod sa zmenil pri **16** investoroch; úroveň dôkazov (A/B) pri **3**.
- Na ručnú kontrolu po spresnení (`REVIEW_REFINED`): **0**.
- Integritné kontroly (každý zaradený má overený datovaný obchod v okne, kapitál má overené tvrdenie): bez chýb.

| Investor | Kapitál pred | Kapitál po | Posledný obchod pred | po | Obchody 36 m pred → po | Zmeny |
|---|---|---|---|---|---|---|
| Credo Ventures | 324.7 mil. € | 324.7 mil. € | 2026-06 | 2026-06-24 | 2 → 3 | Upheal: dátum 2022-10 -> 2024-11 |
| Czech Founders VC | 10.0 mil. € | 10.0 mil. € | 2026-01-14 | 2026-06-09 | 2 → 3 | nový obchod Merchantee (2026-06); doplnené: sektory (odvodené z portfólia) |
| Depo Ventures | – | 3.7 mil. € | 2026-09-01 | 2026-09-01 | 2 → 2 | fond DEPO Ventures One znovu neoverený; fond DEPO Angels fund I znovu neoverený |
| Gi21 Capital | – | – | 2026-08-27 | 2026-08-27 | 4 → 4 | doplnené: tiket |
| i&i Biotech Investments | – | 53.0 mil. € | 2024-05-22 | 2024-05-22 | 1 → 1 | Captain T Cell: novšie kolo (2025-11) sa nepodarilo overiť, pôvodný dátum ostáva |
| Inven Capital | 500.0 mil. € | 500.0 mil. € | 2026-02-12 | 2026-02-11 | 2 → 2 | doplnené: štádiá |
| J&T Ventures | 120.0 mil. € | 120.0 mil. € | 2025-03-05 | 2026-06-12 | 1 → 3 | nový obchod ValkaAI (2026-02); nový obchod Definic (2026-06) |
| Jet Investment | 700.0 mil. € | 700.0 mil. € | 2026-09-17 | 2026-09-17 | 5 → 5 | doplnené: štádiá, tiket |
| JSK Investments | 82.0 mil. € | 82.0 mil. € | 2026-09 | 2026-09-15 | 2 → 2 | fond JSK Investments Venture Capital Fund I. znovu neoverený; fond JSK Investments Private and Growth Equity Fund I. znovu neoverený; doplnené: sektory, tiket |
| Lighthouse Ventures | 23.0 mil. € | 23.0 mil. € | 2025-11 | 2026-06-09 | 1 → 2 | nový obchod Merchantee (2026-06) |
| Look AI Ventures | – | – | 2026-07-13 | 2026-09-16 | 2 → 3 | nový obchod Embodied AI (2026-09); doplnené: štádiá |
| Miton | – | – | 2025 | 2026-01-07 | 5 → 6 | fond Miton C znovu neoverený; fond Miton Psychonats znovu neoverený; Aim: novšie kolo (2025-07) sa nepodarilo overiť, pôvodný dátum ostáva; Bandits: novšie kolo (2025-11) sa nepodarilo overiť, pôvodný dátum ostáva; PangeAI: dátum 2025-01 -> 2026-01; GTE: dátum 2024-01 -> 2025-01; Firefish: novšie kolo (2025-04) sa nepodarilo overiť, pôvodný dátum ostáva; nový obchod DeepScout (2025-03); doplnené: štádiá |
| Neulogy Ventures | – | 23.0 mil. € | 2024-04-18 | 2024-04-18 | 1 → 1 | doplnené: štádiá, tiket |
| Presto Ventures | 180.0 mil. € | 30.0 mil. € | 2024-10 | 2025-05-14 | 1 → 3 | fond Fund I znovu neoverený; GoRamp: dátum 2022-06 -> 2023-07; nový obchod DiffuseDrive (2025-05); nový obchod Bavovna (2024-10) |
| Purple Ventures | 40.0 mil. € | 47.0 mil. € | 2025 | 2026-04-29 | 2 → 3 | Delta Green: dátum 2024-05 -> 2025-10; iVent Pro: dátum 2024-01 -> 2024-06; nový obchod ArtMaster (2026-04) |
| Reflex Capital | 22.0 mil. € | 42.0 mil. € | 2023-12-14 | 2026-06-09 | 1 → 3 | nový obchod Merchantee (2026-06); nový obchod FaceUp (2026-05); doplnené: sektory |
| Rockaway Ventures | 55.0 mil. € | 95.0 mil. € | 2026-02 | 2026-03-01 | 3 → 2 | Apaleo: opravený dátum sa nepodarilo overiť; Gjirafa: dátum 2025-05 -> 2019-03; Productboard: dátum 2021-09 -> 2019-02; Brand Embassy: dátum 2021-09 -> 2014-02; nový obchod Float (2026-03); doplnené: tiket |
| Seed Starter | – | – | 2026-06-12 | 2026-06-12 | 6 → 3 | Investown: opravený dátum sa nepodarilo overiť; Signi: dátum 2023-11 -> 2021-03; PalmApp: opravený dátum sa nepodarilo overiť; Wflow: dátum 2023-11 -> 2022-02; Rekenber: dátum 2023-11 -> 2022-03; nový obchod Pointee (2026-04); nový obchod Definic (2026-06); doplnené: sektory (odvodené z portfólia) |
| Slovak Investment Holding | – | 623.0 mil. € | 2025-09-05 | 2026-09-22 | 2 → 4 | nový obchod VisionFlow (2026-09); nový obchod AT Crystals (2026-09); doplnené: sektory (odvodené z portfólia), štádiá |
| Tensor Ventures | 50.0 mil. € | 20.0 mil. € | 2026-02 | 2026-02-04 | 1 → 1 | fond Tensor Ventures Fund I SCSp znovu neoverený |
| Tilia Impact Ventures | 1.8 mil. € | 27.8 mil. € | 2023-10-18 | 2023-10-18 | 4 → 1 | Munch: dátum 2023-10 -> 2023-06; Cyrkl: dátum obchodu sa nepotvrdil; The Village: dátum 2023-10 -> 2022-07; Datlab: opravený dátum sa nepodarilo overiť |
| Venture to Future Fund | 55.0 mil. € | 40.4 mil. € | 2025-10 | 2025-10 | 1 → 1 | Sensoneo: dátum 2021-10 -> 2023-06 |
| ZAKA Ventures | 15.0 mil. € | 10.5 mil. € | 2026-01-07 | 2026-05-07 | 1 → 2 | nový obchod ParcelBio (2026-05); doplnené: tiket |
| Zero Gravity Capital | – | 23.0 mil. € | 2023-12 | 2023-12-06 | 1 → 1 | doplnené: sektory, tiket |

## 5. Je spresnená verzia presnejšia? (slepá kontrola faktov)

Hodnoty z oboch verzií (zmrazenej aj spresnenej) dostal **nový** agent Sonnet 5.5 ([pokyn](../prompts/refine_judge_agent.md)) zmiešané, zoradené náhodne a **bez informácie, z ktorej verzie pochádzajú**. Každú hodnotu overil v zdrojoch. Rovnaká hodnota v oboch verziách sa hodnotila raz. Ohodnotených položiek: 169 z 169.

| Pole | Zmrazená verzia (v3) | Spresnená verzia |
|---|---|---|
| Celkový kapitál správny | **8/15 = 53.3 %** (95 % CI 30.1 % – 75.2 %) | **14/20 = 70.0 %** (95 % CI 48.1 % – 85.5 %) |
| Obchod: investor + dátum (±2 mesiace) správne | **54/68 = 79.4 %** (95 % CI 68.4 % – 87.3 %) | **78/80 = 97.5 %** (95 % CI 91.3 % – 99.3 %) |
| Identita v registri správna | **24/24 = 100.0 %** (95 % CI 86.2 % – 100.0 %) | **24/24 = 100.0 %** (95 % CI 86.2 % – 100.0 %) |

Prísne počítanie: „neviem“ = nepotvrdené. Rozpis odpovedí:

| Pole | Verzia | Odpovede |
|---|---|---|
| capital | zmrazená | no 7, yes 8 |
| capital | spresnená | cannot_tell 1, no 5, yes 14 |
| deal | zmrazená | wrong_date 14, yes 54 |
| deal | spresnená | wrong_date 2, yes 78 |
| identity | zmrazená | yes 24 |
| identity | spresnená | yes 24 |

### Hodnoty spresnenej verzie, ktoré kontrola nepotvrdila

| Položka | Typ | Odpoveď | Zdôvodnenie |
|---|---|---|---|
| C014-I02 | capital | no | Sum covers only angel funds I (35M CZK) and II (55M CZK) ~3.7M EUR, but DEPO states 9M EUR capital deployed and has a later closed Fund III/DEPO Ventures One (target 20M EUR, lead in ArcSpace) missing, so the total is understated by far more than 20%. |
| C099-I02 | capital | no | The 23 million EUR figure is the 2014 launch size of the two original funds, but neulogy.vc now states 65 million EUR assets under management, so 23 million understates the firm's stated AUM by far more than 20 percent. |
| C100-I05 | capital | no | 40.4 million EUR was only the initial 2019 capital; SIH says the capital was increased by 15.3 million EUR in 2024 (about 55.7 million), so the omitted increase is over 20 percent of the total. |
| C125-I03 | capital | no | 623 million EUR is only the allocation of NDF II, one of several funds SIH manages (NDF I, NDF III, others); fi-compass says SIH manages over 1 billion EUR, so the figure omits more than 20 percent. |
| C132-I03 | capital | cannot_tell | Unquote and others confirm a closed EUR 23m Zero Gravity Capital fund (Fund I), but the firm's Fund II (EUR 25m, launched Sept 2025) is not shown as raised or not raised, so the total cannot be verified. |
| C145-I05 | capital | no | Fund II did reach a EUR 30M final close, but this is not the total: the earlier first fund (15 startups) and Presto Tech Horizons (about ten investments made) are closed/active vehicles of Presto that are left out, which most likely adds well over 20 %. |
| C146-I05 | deal | wrong_date | Purple Ventures did invest, but ArtMaster's round led by Purple with Gi21 was announced 13 Mar 2025 (CzechCrunch, AIN); no April 2026 round found, the Gi21 post dated 29 Apr 2026 repeats the 2025 'July launch' text. |
| C151-I05 | deal | wrong_date | Gi21 invested alongside Purple Ventures, but the ArtMaster round was announced 13 Mar 2025 (CzechCrunch, AIN), not April 2026. |

### Výklad (napísaný ručne k behu z 9. 10. 2026)

- **Dátumy obchodov:** všetkých 14 chýb zmrazenej verzie je rovnakého typu – dátum prehľadového článku, ktorý staršiu investíciu len spomína (portfólio v článku o novom fonde). Spresnenie ich opravilo. Zostali 2 chyby: blogový príspevok investora z apríla 2026 opakuje oznámenie kola z marca 2025 (ArtMaster).
- **Kapitál:** zmrazená verzia chybovala hlavne tým, že započítala **cieľ** fondu (Presto, Purple, Tensor, ZAKA) alebo vynechala starší fond (Rockaway, Tilia, Reflex). Spresnená verzia ciele nepočíta; zvyšné chyby sú **podhodnotenia** – chýba fond, navýšenie kapitálu alebo AUM, ktoré investor uvádza na webe (Neulogy 65 mil. €). Ďalší krok: v pokyne žiadať aj AUM uvádzané investorom a navýšenia kapitálu. Znovu to spustiť a merať tou istou kontrolou by však bolo ladenie na testovacích dátach, preto to ostáva ako odporúčanie.
- **Identita v registri:** 24/24 vrátane 8 záznamov, ktorých identita sa zmenila vo v3 a ktorých opakovaná kontrola predtým zlyhala na limite relácie (D36).

## 6. Doplnenie chýbajúcich polí (D41)

Zadanie žiada pri každom investorovi sektor, typickú investíciu a jej veľkosť a celkový kapitál. Po spresnení niektoré z týchto polí chýbali. Agent Sonnet 5.5 ([pokyn](../prompts/gapfill_agent.md)) hľadal **len chýbajúce polia**; sektory smel odvodiť z portfólia (každý odvodený sektor dokladá citácia o firme z portfólia a v dátach je označený `inferred`), tiket a kapitál len ak ich zdroj uvádza. Pole, ktoré nenašiel, je v stĺpci `not_public` – nie prázdne a nie odhadnuté.

| Pole | Vyplnené pred | Doplnené | Verejne neuvedené | Vyplnené po |
|---|---|---|---|---|
| Sektory | 18/24 | +6 | 0 | **24/24** |
| Štádiá | 18/24 | +6 | 0 | **24/24** |
| Tiket | 15/24 | +7 | 2 | **22/24** |
| Celkový kapitál | 20/24 | +0 | 4 | **20/24** |

Strojová kontrola doplnených tvrdení: `ok` 31.

| Investor | Chýbalo | Výsledok |
|---|---|---|
| Inven Capital | štádiá | štádiá: growth, series_a, series_b_plus |
| Jet Investment | štádiá, tiket | štádiá: seed; tiket: 1.00 – 2.00 mil. € |
| Tensor Ventures | tiket | tiket: verejne neuvedené |
| JSK Investments | sektory, tiket | sektory: health_digital, life_sciences_medtech, ai_data, deeptech_hardware, cleantech_energy; tiket: od 0.30 mil. € |
| Neulogy Ventures | štádiá, tiket | štádiá: seed; tiket: 0.20 – 3.00 mil. € |
| Slovak Investment Holding | sektory, štádiá, tiket | sektory: deeptech_hardware, ai_data, fintech_insurtech (odvodené z portfólia); štádiá: seed; tiket: verejne neuvedené |
| Zero Gravity Capital | sektory, tiket | sektory: sector_agnostic; tiket: do 0.20 mil. € |
| Seed Starter | sektory, celkový kapitál | sektory: fintech_insurtech, enterprise_saas, hr_worktech (odvodené z portfólia); celkový kapitál: verejne neuvedené |
| Reflex Capital | sektory | sektory: sector_agnostic |
| Gi21 Capital | tiket, celkový kapitál | tiket: 0.20 – 1.00 mil. €; celkový kapitál: verejne neuvedené |
| Miton | štádiá, celkový kapitál | štádiá: pre_seed, seed, series_a; celkový kapitál: verejne neuvedené |
| Look AI Ventures | štádiá, celkový kapitál | štádiá: pre_seed, seed; celkový kapitál: verejne neuvedené |
| ZAKA Ventures | tiket | tiket: 0.25 – 0.30 mil. € |
| Rockaway Ventures | tiket | tiket: do 15.00 mil. € |
| Czech Founders VC | sektory | sektory: proptech_construction, ai_data, media_gaming, life_sciences_medtech (odvodené z portfólia) |

## 7. Obmedzenia

- Spresňoval aj kontroloval model tej istej rodiny (Sonnet 5.5). Kontrolór bol iný agent bez prístupu k výstupu spresnenia a nevedel, ktorá hodnota je nová, chyby oboch však môžu byť korelované. Rozhodujúce je preto, že každé nové tvrdenie prešlo rovnakými strojovými kontrolami ako zvyšok databázy.
- Kontrola faktov meria hodnoty, ktoré v databáze **sú**. Chýbajúci kapitál (neuvedené) sa do presnosti nepočíta – vyplnenosť je uvedená zvlášť v kap. 4.
- Spresnenie je po zmrazení: primárna metrika presnosti záznamov (PRECISION_REPORT) sa ním nemení.

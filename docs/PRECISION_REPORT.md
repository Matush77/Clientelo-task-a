# Meranie presnosti – pilot VC investori CZ + SK

*Generované skriptom `python -m investordb.cli report` z dát zmrazených tagom `pilot-frozen-v3` (`as_of` = 2026-10-09). Metriky sú definované vopred v [PLAN.md](PLAN.md), kap. 9.*

## 1. Kto hodnotil vzorku

- **Claude Sonnet 5.5** posúdil všetkých 34 záznamov vzorky naslepo (rovnaké informácie ako formulár pre človeka, zdroje si otváral sám) – [pokyn](../prompts/reviewer_agent.md).
- **Človek** (autor) ručne overil 5 záznamov vo formulári (D40): 2 sporné medzi AI kontrolórmi a 3 náhodné kontrolné; z nich 4 zaradené a 1 vyradený (návnada). Polia (kapitál, zdroje) videl v spresnenej verzii (D38). **Kde sa človek a Sonnet líšia, platí odpoveď človeka.**
- **Claude Haiku 5.5** (nezávislý overovateľ) posúdil tých istých 34 záznamov – druhý AI názor.
- Rozhodnutie a dôvody: [DECISIONS.md](DECISIONS.md) D34, D40. Zadanie žiada ručne overenú vzorku – úplnú ručnú kontrolu nahradila AI kontrola s ľudským auditom; obmedzenie je uvedené v README.
- Pred formulárom človek urobil kvalitatívny audit, ktorý viedol k dvom opravám pipeline (v2, v3):

| Záznam | Zistenie | Dôsledok |
|---|---|---|
| R06 Reflex Capital | Celkový kapitál zobrazený ako 30 € – zjavne chybný | Audit v1 -> v2: prevod súm (rozpätia a čísla slovom) a kontrola rozumnosti |
| R21 Look AI Ventures | Fond je len plánovaný (zdroj hovorí o zámere ho získať), nie uzavretý | Audit v1 -> v2: cieľové fondy sa nepočítajú do kapitálu |
| R31/R32 Jet Investment / Jet Ventures | Rovnaká skupina dvakrát vo vzorke | Vysvetlené: R32 je vyradená duplicita (E8) zlúčená do R31 |
| R16 CB Investment Management | IČO v zázname nesedí s webom investora | Oprava v2 -> v3: prísne pravidlá identity v registri (D35) |
| celá vzorka | Z článkov často nie je jasný dátum investície, výška sumy ani to, či peniaze naozaj išli do firmy | Dokumentované ako hlavné obmedzenie; odporúčanie silnejšieho modelu na výklad článkov (D36); kvantifikované v PRECISION_REPORT |

## 2. Výsledok pipeline

| Stav | Počet |
|---|---|
| INCLUDED | 24 |
| REJECTED | 70 |
| OOS | 35 |
| NEEDS_REVIEW | 4 |

Dôvody vyradenia: E7 26×, OOS_HQ 22×, E1 13×, E3 11×, E2 10×, OOS_TYPE 8×, OOS_HQ_UNVERIFIED 5×, E8 4×, E6 3×, E4 3×

## 3. Primárna metrika: presnosť zaradených záznamov

Záznam je správny, ak hodnotiteľ zo zdrojov potvrdil **všetky štyri**: skutočný investor ∧ aktívny v 36 mesiacoch ∧ VC ∧ sídlo CZ/SK.

- **Výsledná presnosť** (prísne, „neviem“ = nepotvrdené): **23/23 = 100.0 %** (95 % CI 85.7 % – 100.0 %)
- Len rozhodnuté záznamy (bez „neviem“): **23/23 = 100.0 %** (95 % CI 85.7 % – 100.0 %)
- Len záznamy, ktoré ručne overil človek: **4/4 = 100.0 %** (95 % CI 51.0 % – 100.0 %)
- Pre porovnanie – len podľa Sonnetu (pred ľudským auditom): **23/23 = 100.0 %** (95 % CI 85.7 % – 100.0 %)
- Záznamy vybrané ako zaradené, ktoré po oprave v3 už v databáze nie sú (nezapočítané): R03 (NEEDS_REVIEW REVIEW_IDENTITY)

| Otázka | Áno | Nie | Neviem |
|---|---|---|---|
| real_investor | 23 | 0 | 0 |
| active_36m | 23 | 0 | 0 |
| type_vc | 23 | 0 | 0 |
| hq_cz_sk | 23 | 0 | 0 |

## 4. Správnosť vyradenia

Vyradenie je správne, ak hodnotiteľ pri aspoň jednej zo štyroch otázok odpovedal „nie“. Duplicity (E8) sa hodnotia zvlášť (D29): vyradenie je správne, ak ide o skutočného investora a jeho zlúčený hlavný záznam je zaradený.

| Vrstva | Správne vyradené |
|---|---|
| skutočné vyradené záznamy (bez duplicít) – prísne | **3/3 = 100.0 %** (95 % CI 43.8 % – 100.0 %) |
| kontrolná sada (návnady) – prísne | **4/5 = 80.0 %** (95 % CI 37.6 % – 96.4 %) |
| kontrolná sada (návnady) – vrátane „ani hodnotiteľ nenašiel dôkaz“ pri E7 | **5/5 = 100.0 %** (95 % CI 56.6 % – 100.0 %) |
| duplicity (E8) – firma je v databáze cez zlúčený záznam | **1/2 = 50.0 %** (95 % CI 9.5 % – 90.5 %) |

## 5. Presnosť a vyplnenosť polí (zaradené záznamy)

| Pole | Presnosť (áno / áno+nie) | Vyplnenosť v databáze |
|---|---|---|
| sources_support | **19/23 = 82.6 %** (95 % CI 62.9 % – 93.0 %) | – |
| sectors_ok | **17/17 = 100.0 %** (95 % CI 81.6 % – 100.0 %) | 18/24 |
| ticket_ok | **15/15 = 100.0 %** (95 % CI 79.6 % – 100.0 %) | 14/24 |
| capital_ok | **6/12 = 50.0 %** (95 % CI 25.4 % – 74.6 %) | 15/24 |
| identity_ok (len Sonnet; bez 8 záznamov s identitou zmenenou vo v3) | **18/18 = 100.0 %** (95 % CI 82.4 % – 100.0 %) | – |

Človek pri 4 zaradených záznamoch hodnotil polia **spresnenej verzie** (D40); presnosť spresnených polí meria podrobne slepá kontrola faktov v [REFINEMENT.md](REFINEMENT.md):

| Pole (spresnená verzia) | Áno | Nie | Neviem | Neuvedené |
|---|---|---|---|---|
| sources_support | 4 | 0 | 0 | 0 |
| sectors_ok | 3 | 0 | 1 | 0 |
| ticket_ok | 0 | 0 | 3 | 1 |
| capital_ok | 0 | 0 | 4 | 0 |

### Nejasnosť zdrojov (investície zaradených investorov)

Z 116 overených investícií zaradených investorov: **69 (59.5 %)** má dátum, ktorý možno považovať za dátum obchodu (z toho 44 s presnosťou na deň); **47 (40.5 %)** je len zmienka bez dátumu obchodu (portfólio, prehľadové články); suma je uvedená pri **25 (21.6 %)**. Potvrdzuje to zistenie z ľudskej kontroly: z verejných článkov často nie je jasné, kedy a koľko investor investoval.


## 6. Strojové kontroly (všetky tvrdenia agentov)

852 tvrdení: `ok` 808 (94.8 %), `quote_not_found` 28 (3.3 %), `forbidden_source` 12 (1.4 %), `blocked` 4 (0.5 %).
Z 297 overených investičných tvrdení: kontext obchodu `deal` 209, `mention` 84, `exit` 4; priradenie investora `1` 269, `0` 28.

## 7. Zhoda hodnotiteľov

| Dvojica | Zhoda celkového verdiktu | Cohenovo κ (rozhodnuté záznamy) |
|---|---|---|
| Haiku overovateľ vs. výsledok | **30/34 = 88.2 %** (95 % CI 73.4 % – 95.3 %) | 1.00 |
| Haiku overovateľ vs. Sonnet | **29/34 = 85.3 %** (95 % CI 69.9 % – 93.6 %) | 1.00 |
| Sonnet vs. človek – náhodné kontrolné záznamy | **3/3 = 100.0 %** (95 % CI 43.8 % – 100.0 %) | 1.00 |
| Sonnet vs. človek – sporné záznamy | **1/2 = 50.0 %** (95 % CI 9.5 % – 90.5 %) | 1.00 |

Zhoda Sonneta s človekom na **náhodných** kontrolných záznamoch je nestranný odhad spoľahlivosti AI kontroly; na sporných záznamoch ukazuje, kto mal pri ťažkých prípadoch pravdu.

## 8. Odhad úplnosti (capture–recapture)

Zaradení investori nájdení v zozname A (štruktúrované zdroje): 14, v zozname B (správy o kolách): 18, v oboch: 8. Chapmanov odhad počtu aktívnych VC investorov so sídlom v CZ/SK: **31** (95 % CI 24 – 40). Databáza pokrýva približne **78.3 %**. Ide o dolný odhad populácie (a teda horný odhad pokrytia) – oba zoznamy uprednostňujú viditeľných investorov.

## 9. Čas ručnej kontroly

Človek pri ručnej kontrole čas na záznam nezaznamenal. Nákladový model používa predpoklad 4 min na záznam a uvádza ho ako predpoklad.

## 10. Záznamy, pri ktorých sa výsledok líši od pipeline

| Záznam | Vrstva | Pipeline | Výsledok | Kto | Zdôvodnenie |
|---|---|---|---|---|---|
| R17 Tech Ventures s.r.o. (C200) | control_reject | REJECTED E7 | cannot_tell | Sonnet 5.5 | real_investor: No public source shows Tech Ventures s.r.o. investing in companies; ARES/finmag show a 2019 s.r.o. (seat Zdanice, sole owner and director [osoba]) with registered activities in IT, advertising, training and events, not investing.; active_36m: The record lists no investments and no sou |

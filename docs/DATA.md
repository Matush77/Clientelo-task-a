# Dátový slovník

*Generované skriptom `python -m investordb.cli datadict`. Rovnaký popis je v hárku „Popis stĺpcov“ súboru [investori_cz_sk.xlsx](../data/processed/investori_cz_sk.xlsx).*

## Súbory

| Súbor | Obsah |
|---|---|
| [data/processed/investors_refined.csv](../data/processed/investors_refined.csv) | **Výsledná databáza:** 24 zaradených investorov po spresnení (D38) a doplnení polí (D41), jeden riadok = jeden investor. |
| [data/processed/investori_cz_sk.xlsx](../data/processed/investori_cz_sk.xlsx) | To isté v Exceli: hárky Investori, Tvrdenia (citácie s odkazmi na zdroj), Popis stĺpcov a O súbore. |
| [data/processed/investors.csv](../data/processed/investors.csv) | Zmrazená verzia v3 (tag `pilot-frozen-v3`), na ktorej je zmeraná presnosť ([PRECISION_REPORT.md](PRECISION_REPORT.md)). Rovnaké stĺpce bez posledných štyroch. |
| [data/processed/claims.csv](../data/processed/claims.csv) | Tvrdenia agentov zo zberu dôkazov (všetci kandidáti), každé so zdrojom, doslovnou citáciou a výsledkom strojovej kontroly. |
| [data/processed/claims_refined.csv](../data/processed/claims_refined.csv) | Tvrdenia zo spresnenia (D38) + stĺpec `verdict` (stav fondu alebo verdikt k dátumu). |
| [data/processed/claims_gapfill.csv](../data/processed/claims_gapfill.csv) | Tvrdenia z doplnenia chýbajúcich polí (D41). |
| [data/processed/decisions.csv](../data/processed/decisions.csv) | Rozhodnutie pre všetkých 133 kandidátov (zaradený / vyradený s kódom / mimo rozsahu / na kontrolu). |
| [data/processed/rejected.csv](../data/processed/rejected.csv) | Vyradení a mimo rozsahu, s kódom dôvodu. |
| [data/processed/needs_review.csv](../data/processed/needs_review.csv) | Záznamy, ktoré pravidlá nevedeli rozhodnúť (na ručnú kontrolu). |
| [data/processed/candidates.csv](../data/processed/candidates.csv) | Všetkých 206 kandidátov z objavovania (zoznam A, B, kontrolné sady). |

## investors_refined.csv – výsledná databáza

Každá vyplnená bunka má za sebou overené tvrdenie v `claims*.csv` (zdroj, doslovná citácia, výsledok kontroly). Prázdna bunka = údaj sa nenašiel; ak je pole v `not_public`, agent ho hľadal a verejne sa neuvádza.

| Stĺpec | Hlavička v Exceli | Popis |
|---|---|---|
| `name` | Investor | Názov značky investora. |
| `hq_country` | Krajina | Krajina sídla investičného tímu (CZ / SK) – nie domicil fondu. |
| `investor_types` | Typ | Typ investora (kódy nižšie): `vc`, `cvc` (korporátny VC), `public_vc` (štátny VC); môže byť viac typov. |
| `sectors` | Sektory | Sektorové zameranie, kódy nižšie; `sector_agnostic` = bez sektorového zamerania. |
| `sectors_basis` | Sektory – základ | `stated` = investor zameranie uvádza; `inferred` = odvodené z portfólia (každý sektor dokladá citácia o firme z portfólia). |
| `stages` | Štádiá | Štádiá investícií (kódy nižšie). |
| `stages_basis` | Štádiá – základ | `stated` / `inferred`, ako pri sektoroch. |
| `ticket_min` | Tiket od (ako v zdroji) | Typická výška investície do jednej firmy – dolná hranica, presne ako v zdroji. |
| `ticket_max` | Tiket do (ako v zdroji) | Horná hranica, presne ako v zdroji. |
| `ticket_min_eur` | Tiket od (EUR) | Dolná hranica v EUR; prepočet kurzom ECB z posledného dňa pred `as_of`. |
| `ticket_max_eur` | Tiket do (EUR) | Horná hranica v EUR. |
| `total_capital_eur` | Celkový kapitál (EUR) | Uvedené AUM, inak súčet fondov, ktoré získali peniaze (uzavretie alebo prvé uzavretie); cieľ fondu sa nepočíta (D17, D38). |
| `capital_method` | Spôsob výpočtu kapitálu | `aum_stated` = investor uvádza AUM; `sum_of_N_closed_funds` = súčet N fondov. |
| `capital_approx` | Kapitál približne | 1 = zdroj uvádza približnú sumu („bezmála“, „nearly“…). |
| `capital_note` | Poznámka ku kapitálu | Prepočty mien a fondy, ktoré majú zatiaľ len prvé uzavretie. |
| `funds` | Fondy | Všetky overené fondy so sumou ako v zdroji a stavom (uzavretý / prvé uzavretie / cieľ). |
| `funds_target` | Plánované fondy (nezapočítané) | Cieľové veľkosti fondov – do kapitálu sa nepočítajú. |
| `not_public` | Verejne neuvedené | Povinné polia, ktoré agent hľadal na webe investora aj v tlači a verejne sa neuvádzajú (D41) – nie sú prázdne omylom ani odhadnuté. |
| `n_investments` | Investície celkom | Počet overených investícií (firiem) – datovaných aj z portfólia. |
| `n_investments_36m` | Nedávne investície (36 mes.) | Počet investícií s dátumom obchodu od `as_of` − 36 mesiacov (od 9. 10. 2023). |
| `last_investment_date` | Posledný obchod – dátum | Dátum oznámenia posledného overeného obchodu (s presnosťou, akú uvádza zdroj). |
| `last_investment` | Posledný obchod – firma | Firma, do ktorej investor naposledy investoval. |
| `last_investment_source` | Posledný obchod – zdroj | URL zdroja, ktorý dokladá posledný obchod. |
| `tier` | Úroveň dôkazov | `A` = aspoň 2 datované obchody z 2 nezávislých zdrojov; `B` = aspoň 1 datovaný obchod za 36 mesiacov. |
| `status` | Stav | `INCLUDED` = zaradený; `NEEDS_REVIEW` = na ručnú kontrolu (kódy nižšie). |
| `legal_name` | Právnická osoba | Obchodné meno správcovskej spoločnosti alebo fondu podľa registra. |
| `company_id` | IČO | Identifikačné číslo z registra ARES (CZ) alebo RPO (SK). |
| `registry_url` | Záznam v registri | Odkaz na záznam v registri (API ARES / RPO). |
| `website` | Web | Oficiálny web investora. |
| `refine_notes` | Zmeny po spresnení | Čo zmenilo spresnenie (D38) a doplnenie (D41): opravené dátumy, nové obchody, doplnené polia. |
| `explanation` | Zdôvodnenie pravidiel | Prečo pravidlá záznam zaradili (počet investícií, zdrojov). |
| `evidence_ids` | ID kandidátov | ID kandidátov, ktorých dôkazy záznam spája (zlúčené duplicity). |
| `candidate_id` | ID | ID kandidáta (kľúč do `claims*.csv` a `decisions.csv`). |
| `as_of` | Stav k | Referenčný dátum – deň zmrazenia dát. |
| `reason` | Kód dôvodu | Pri `NEEDS_REVIEW` kód dôvodu (nižšie); pri zaradených prázdne. |
| `data_flags` | Upozornenia | Sumy, ktoré kód vyradil ako nereálne (kontrola rozumnosti). |

## claims*.csv – tvrdenia so zdrojom

| Stĺpec | Popis |
|---|---|
| `candidate_id` | ID kandidáta. |
| `field` | Pole: `investments`, `funds`, `total_capital`, `ticket`, `sectors`, `stages`, `hq_country`, `investor_type`, `identity`, `red_flags`. |
| `value` | Hodnota ako JSON (napr. `{"company": …, "date": …, "amount": …}`). |
| `value_text` | Slová z citácie, ktoré hodnotu uvádzajú – program kontroluje, že sú v citácii. |
| `source_url` | Zdroj. |
| `quote` | Doslovná citácia zo zdroja (max. 300 znakov), v pôvodnom jazyku. |
| `published_date` | Dátum publikovania zdroja. |
| `derivation` | `stated` = zdroj hodnotu uvádza; `inferred` = odvodené (len sektory a štádiá z portfólia). |
| `source_tier` | Typ zdroja (kódy nižšie). |
| `event_date` | Investície: dátum obchodu (alebo publikovania, ak zdroj iný neuvádza); inak dátum publikovania. |
| `event_date_precision` | `day` / `month` / `year`. |
| `auto_check` | Výsledok strojovej kontroly (kódy nižšie). Do databázy sa dostanú len tvrdenia `ok`. |
| `deal_context` | Investície: `deal` = správa o obchode, `mention` = len zmienka (dátum sa nepočíta), `exit`. |
| `attributed` | Investície: 1 = investor je menovaný pri citácii (alebo ide o jeho web), 0 = nie. |
| `quote_score` | Zhoda citácie so stránkou (rapidfuzz, 0–100; prah 90). |
| `checked_url` | Adresa, ktorú program skutočne stiahol (aj archív Wayback). |
| `text_sha256` | Odtlačok textu stránky v čase kontroly. |
| `fetched_at` | Čas kontroly. |
| `verdict` | Len `claims_refined.csv`: stav fondu (`final_close`, `first_close`, `target`) alebo verdikt k dátumu obchodu (`confirmed`, `corrected`, `new`). |

## Stav a kód dôvodu (decisions.csv, rejected.csv, needs_review.csv)

| Kód | Význam |
|---|---|
| `INCLUDED` | zaradený – spĺňa I1–I5 |
| `E1` | bez datovaného dôkazu investície (len sebaprezentácia) |
| `E2` | neaktívny viac ako 36 mesiacov alebo zrušený |
| `E3` | sprostredkovateľ: crowdfunding, poradca, akcelerátor bez vlastného kapitálu |
| `E4` | iná trieda aktív: nehnuteľnosti, verejné akcie, len úvery |
| `E5` | len LP / fond fondov |
| `E6` | investuje len vo vlastnej skupine |
| `E7` | len podobné meno – žiadna doložená investícia |
| `E8` | duplicita – dôkazy zlúčené do hlavného záznamu |
| `E9` | len granty |
| `OOS_HQ` | skutočný investor, ale sídlo mimo CZ/SK |
| `OOS_HQ_UNVERIFIED` | agent uvádza zahraničné sídlo, citáciou ho nedoložil |
| `OOS_TYPE` | skutočný investor, ale nie VC (PE, family office, angel sieť, akcelerátor) |
| `REVIEW_IDENTITY` | na ručnú kontrolu: bez spoľahlivej zhody v registri (D35) |
| `REVIEW_BLOCKED` | na ručnú kontrolu: zdroje investícií blokujú automatickú kontrolu |
| `REVIEW_TYPE` | na ručnú kontrolu: typ investora sa nepodarilo overiť |
| `REVIEW_TIER_C` | na ručnú kontrolu: dôkazy príliš slabé |
| `REVIEW_REFINED` | na ručnú kontrolu: po spresnení by pravidlá záznam nezaradili (D38) |

## Typ zdroja (source_tier)

| Kód | Význam |
|---|---|
| `T1` | register, regulátor, oficiálne zverejnenie LP (ARES, RPO, EIF, SIH, NRB…) |
| `T2` | web investora |
| `T3` | tlač a tlačové správy |
| `T4` | agregátor (Dealroom, Crunchbase, LinkedIn…) – nikdy dôkaz (`forbidden_source`) |

## Strojová kontrola (auto_check)

| Kód | Význam |
|---|---|
| `ok` | citácia je na stránke (zhoda ≥ 90) a hodnota je v citácii |
| `quote_not_found` | citácia na stránke nie je |
| `value_not_in_quote` | hodnota v citácii nie je |
| `url_dead` | stránka neexistuje |
| `blocked` | stránka blokuje sťahovanie (ani archív nepomohol) |
| `forbidden_source` | agregátor (T4) |

## Stav fondu (funds, D38)

| Kód | Význam |
|---|---|
| `final_close` | fond je uzavretý, suma = jeho veľkosť – počíta sa do kapitálu |
| `first_close` | prvé / priebežné uzavretie – počíta sa suma získaná doteraz |
| `target` | len cieľ alebo plán – nepočíta sa |

## Sektory, štádiá a typy

| Kód | Význam |
|---|---|
| `ai_data` | AI a dáta |
| `enterprise_saas` | B2B SaaS |
| `fintech_insurtech` | fintech |
| `health_digital` | digitálne zdravie |
| `life_sciences_medtech` | life sciences |
| `deeptech_hardware` | deeptech |
| `cleantech_energy` | cleantech |
| `mobility_logistics` | mobilita |
| `consumer_ecommerce` | spotrebiteľ |
| `edtech` | edtech |
| `proptech_construction` | proptech |
| `agri_food` | agri/food |
| `cybersecurity` | kyberbezpečnosť |
| `media_gaming` | médiá/hry |
| `industry_manufacturing` | priemysel |
| `iot_telecom` | IoT |
| `hr_worktech` | HR tech |
| `travel_hospitality` | cestovanie |
| `govtech_legaltech` | govtech |
| `defense_space` | obrana/vesmír |
| `sector_agnostic` | bez sektorového zamerania |
| `pre_seed` | pre-seed |
| `seed` | seed |
| `series_a` | séria A |
| `series_b_plus` | séria B+ |
| `growth` | growth |
| `buyout` | buyout |
| `vc` | VC |
| `cvc` | korporátny VC |
| `public_vc` | verejný VC |
| `pe` | PE |
| `real_estate` | nehnuteľnosti |
| `angel_network` | sieť angel investorov |
| `family_office` | family office |

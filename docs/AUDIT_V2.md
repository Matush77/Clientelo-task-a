# Audit pred ručnou kontrolou (pilot v1 → v2)

*9. 10. 2026. Pôvodne zmrazená verzia je označená `pilot-frozen`, opravená `pilot-frozen-v2`.
Rozdiely sa dajú overiť cez `git diff pilot-frozen pilot-frozen-v2 -- data/processed/`.*

## Ako sa chyby našli

Po prvom zmrazení som si pred vypĺňaním prešiel formulár na ručnú kontrolu. Hneď na začiatku som narazil na dve
zjavné chyby:

- **Reflex Capital** mal „celkový kapitál 30 €“;
- **Look AI Ventures** mal ako kapitál uvedených 20 mil. €, hoci zdroj hovorí len o *pláne* fond získať.

Namiesto opravy dvoch záznamov sme spravili **systematický audit**:

1. rozbor príčin oboch chýb;
2. prehľad celej databázy pre rovnaké vzory;
3. zapracovanie zistení nezávislého AI overovateľa z v1, ktorý označil najmä dátumy a kapitál.

**Kľúčové zistenie:** strojová kontrola citácií overovala, že **citácia na stránke naozaj je**. Neoverovala však, či
je **správne vyložená**. Všetky nájdené chyby mali citáciu pravú, ale výklad chybný.

## Nájdené kategórie chýb a opravy

| # | Chyba | Príklad z v1 | Oprava (kód/pravidlo, žiadna ručná úprava záznamov) |
|---|---|---|---|
| 1 | Prevod súm: rozpätia, čísla slovom, násobok („milionů“) ďaleko od čísla | Reflex: „od 30 do 50 milionů“ → **30 €**; „dvaadvacet milionů eur“ sa ignorovalo; tiket Tilia „0,3“ → **0 €** | parser rozpätí a číslovek (CZ/SK/EN); dolná hranica tiketu preberá násobok hornej; **kontrola rozumnosti** (fond 0,5 mil. – 20 mld. €, tiket 5 tis. – 500 mil. €) |
| 2 | **Plánovaný fond započítaný ako kapitál** | Look AI „Aiming to raise €20 million“, Rockaway „cílová velikost 100 mil.“, DEPO „aiming €20M“ | detektor cieľových fondov; cieľ sa uvádza zvlášť (`funds_target`), do kapitálu sa nepočíta |
| 3 | **Výstup (exit) započítaný ako investícia** | Nation1: „Taikun's exit to Cloudera“ ako „posledná investícia 2026“ | investícia s citáciou o exite / akvizícii sa vyradí |
| 4 | **Dátum článku namiesto dátumu obchodu** | Miton: článok z 2026 len spomína Miton medzi investormi firmy (obchod bol v 2020) | kontext obchodu: dátum sa počíta, len ak citácia alebo jej okolie na stránke opisuje obchod; veta „medzi investormi firmy sú…“ je len zmienka |
| 5 | **Neoverené priradenie investora** | Lighthouse: „Ranketta raised €1 million“ – citácia nemenuje Lighthouse | kontrola priradenia: meno kandidáta musí byť v citácii alebo do 400 znakov od nej (vlastný web kandidáta je výnimka) |
| 6 | Identita: iná právna forma | Czech Founders VC (web: s.r.o.) priradený k „Czech Founders z.ú.“ | pri overenom obchodnom mene sa musí zhodovať právna forma; bez návratu k voľnejšiemu hľadaniu podľa značky |
| 7 | Databázy vydávané za tlač | startbase.de, trysignalbase.com, podnikatel.cz | presunuté medzi T4 (len objavovanie) |
| 8 | Prepočet meny bez uvedenia kurzu | Nation1: 60 mil. USD → 53,6 mil. € bez vysvetlenia | stĺpec `capital_note` s pôvodnou sumou, kurzom ECB a dátumom |
| 9 | Falošná presnosť dátumu | „2024“ zobrazené ako „2024-01-01“ | dátum sa zobrazuje s presnosťou zdroja |

## Chyby, ktoré vznikli pri samotnom audite (a ako sa zachytili)

Aj opravy treba overovať. Kontrola rozdielov v1/v2 odhalila štyri vlastné chyby, ešte pred zmrazením v2:

| Chyba pri audite | Ako sa prejavila | Ako sa zachytila |
|---|---|---|
| Preradil som spravodajské weby o investičných kolách (thesaasnews.com, raising.fi) medzi databázy (T4) bez dôkazu, že sú nespoľahlivé | 4 skutočné VC vypadli | rozbor každej zmeny stavu |
| Slovo „round“ sa našlo vnútri názvu firmy („Boata**round**“) | nesprávny kontext obchodu | test |
| Vzor „investors including“ označil za „zmienku“ aj syndikát investorov v danom kole | i&i Biotech chybne vypadol | rozbor každej zmeny stavu |
| Slovo „invest“ sa zhodovalo aj s „investor“ | zmienky sa rátali ako obchody | test |

Všetky štyri sú opravené a pokryté regresnými testami (spolu 128 testov).

## Vplyv na dáta

| | v1 | v2 |
|---|---|---|
| Zaradených investorov | 25 | **25 (rovnaká množina)** |
| Celkový kapitál zmenený | – | 6 záznamov (3× odstránený cieľový fond, 3× doplnená suma písaná slovom) |
| Tiket zmenený | – | 2 záznamy |
| Posledná investícia – iný obchod | – | 4 záznamy (Nation1, Miton, Inven, Neulogy) |
| Úroveň dôvery znížená A → B | – | 3 záznamy |
| Investičné tvrdenia vyradené ako exit | – | 4 |
| Investičné tvrdenia bez overeného priradenia investora | – | 28 |
| Investície bez dátumu obchodu (len zmienka) | – | 88 |

**Rozhodnutia o zaradení boli robustné.** Všetkých 25 investorov z v1 prešlo aj prísnejšími pravidlami.

**Chyby boli v hodnotách polí** (kapitál, tiket, dátumy). Tie vo v1 nemala pokrytá žiadna automatická kontrola
významu.

## Ponaučenie

Overenie, že AI citovala správne, nestačí. Treba overiť aj to, **čo citácia znamená**:

- je to obchod, alebo exit?
- je to cieľ, alebo uzavretý fond?
- je investor naozaj menovaný?

Tieto kontroly sú teraz deterministické a pridané ako vrstva 3b v [PLAN.md](PLAN.md). Ich chýbanie odhalila
**ľudská kontrola** – presne kvôli tomu je ručná kontrola súčasťou postupu.

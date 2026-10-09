# Odhad nákladov na rozšírenie na celý svet

*Generované skriptom `python -m investordb.cli cost` z meraní v pilote. Ceny: oficiálny cenník Anthropic API (overený strojovo, [api_prices_md_checked.csv](../data/reference/api_prices_md_checked.csv), 9. 10. 2026); kurz ECB 1 € = 1.1186 USD.*

## 1. Čo stál pilot (namerané)

Všetci subagenti bežali na **Claude Haiku 5.5**. Náklad je prepočítaný na ceny API (pilot bežal v rámci predplatného Claude Code), podľa skutočnej spotreby tokenov zo záznamov agentov (`usage.py`).

| Etapa | Náklad (USD) |
|---|---|
| ai_review | 7.79 |
| zber dôkazov (vrátane opakovaní) | 6.42 |
| prieskum a plánovanie (jednorazovo) | 0.86 |
| nezávislý AI overovateľ | 0.81 |
| objavovanie kandidátov | 0.63 |
| triáž sídla | 0.40 |
| etapa „nedávna investícia“ | 0.28 |
| kontrola duplicít | 0.06 |
| **spolu** | **17.24** |

- Na jedného kandidáta (objavovanie + triáž + dôkazy + nedávna investícia): **0.059 USD**
- Nezávislý overovateľ na jeden záznam: **0.012 USD**
- **Vyhľadávanie na webe tvorí 45 % nákladov na AI** – samotné tokeny Haiku sú zanedbateľné.
- Na 1 zaradeného investora pripadlo **5.5 kandidátov**; 3.0 % kandidátov skončilo v ručnej kontrole.
- Ručná kontrola: **4 min – predpoklad**, nahradí sa meraním z ručnej kontroly na záznam.

*Nezapočítané:* orchestrácia v hlavnej session (Claude Opus 5.5) – v produkčnom postupe ju nahrádza kód; a prístup k stránkam cez WebFetch v Claude Code vracia agentovi len výťah, kým API vracia celý text – preto je v modeli pripočítaných 6000 vstupných tokenov na každú stiahnutú stránku.

## 2. Scenáre pre celý svet

| Predpoklad | nízky | základný | vysoký | Odkiaľ |
|---|---|---|---|---|
| Overených investorov v databáze | 32 000 | 45 000 | 70 000 | PLAN.md, kap. 11.2 |
| Kandidátov na 1 zaradený záznam | 3.3 | 5.5 | 8.3 | pilot (základ); lepšie zdroje / horšie trhy |
| Viacjazyčnosť / ťažšie trhy (násobok AI) | 1.0× | 1.5× | 3.0× | predpoklad |
| Segmenty kontroly kvality (krajina × typ) | 80 | 150 | 250 | predpoklad |
| Presnosť odhadu na segment (±, 95 %) | 7 p. b. | 5 p. b. | 5 p. b. | voľba |
| Minút ručnej kontroly na záznam | 3.2 | 4.0 | 6.0 | pilot (základ) |
| Hodinová sadzba kontrolóra | 20 € | 30 € | 50 € | predpoklad (analytik CEE / západná Európa) |
| Vývoj produkčnej pipeline | 30 dní × 350 € | 45 dní × 450 € | 70 dní × 600 € | predpoklad |

| Výsledok (1. rok) | nízky | základný | vysoký |
|---|---|---|---|
| Kandidátov na spracovanie | 106 400 | 249 375 | 581 875 |
| AI (Haiku 5.5 + vyhľadávanie) | 5 909 € | 20 057 € | 92 114 € |
| Záznamov na ručnú kontrolu | 8 880 | 28 350 | 52 250 |
| Ľudská kontrola kvality | 9 472 € | 56 700 € | 261 250 € |
| Vývoj (jednorazovo) | 10 500 € | 20 250 € | 42 000 € |
| **Spolu 1. rok** | 25 881 € | 97 007 € | 395 364 € |
| Na 1 overený záznam | 0.81 € | 2.16 € | 5.65 € |
| Ročná aktualizácia (od 2. roka) | 5 498 € | 18 827 € | 69 576 € |

## 3. Varianty kvality (základný scenár)

Pilot ukázal dve slabiny: (1) Haiku pri výklade článkov často nerozlíšil dátum obchodu od dátumu článku a cieľový fond od uzavretého, (2) na presnosť polí treba ľudskú kontrolu. Dve varianty, ako za to zaplatiť:

| Variant | AI | Ľudská kontrola | Spolu 1. rok | Rozdiel oproti základu |
|---|---|---|---|---|
| základ (Haiku na zber, človek na vzorku) | 20 057 € | 56 700 € | 97 007 € | – |
| **Sonnet 5.5 na zber dôkazov** (výklad dátumov, súm, účasti) | 110 216 € | 56 700 € | 187 166 € | +90 159 € |
| Sonnet na zber **aj** AI kontrolu všetkých záznamov, človek len na sporné a náhodné | 119 429 € | 22 680 € | 162 359 € | +65 353 € |

Namerané v pilote: tokeny zberu dôkazov stoja 0.0142 USD na kandidáta pri Haiku (Sonnet = 20×); AI kontrola Sonnetom stála 0.229 USD na záznam. Podiel ľudskej kontroly 40 % v poslednom riadku je predpoklad – v pilote sa Sonnet a Haiku líšili v 15 % záznamov, k tomu náhodná kontrola.

## 4. Čo z toho vyplýva

- **Hlavný náklad nie je AI, ale ľudská kontrola kvality.** V základnom scenári AI stojí 20 057 €, ľudská kontrola 56 700 €.
- **Najväčšia páka je zhoda AI overovateľa s človekom** (meraná v [PRECISION_REPORT.md](PRECISION_REPORT.md)). Ak je vysoká, človek kontroluje len segmentovú vzorku a záznamy, kde sa AI overovateľ a pravidlá nezhodnú; ak nízka, počet ručne kontrolovaných záznamov rastie.
- **Druhá páka je vyhľadávanie:** tvorí väčšinu nákladov na AI. Štruktúrované zdroje (registre SEC Form ADV, ESMA, národné registre, zoznamy asociácií) znižujú počet kandidátov na 1 zaradený záznam aj počet vyhľadávaní.
- **Tretia páka je kvalita zoznamu kandidátov:** v pilote bolo 5,3 kandidáta na 1 zaradeného investora; v krajinách bez dobrých zoznamov (a pri family office / angel investoroch) to bude viac.
- Model Haiku 5.5 stačí: všetky kroky, kde záleží na presnosti, robí deterministický kód (kontrola citácií, pravidlá, registre). Drahší model by zvýšil cenu AI ~20× bez zmeny tejto architektúry.

## 4. Obmedzenia odhadu

- Pilot meral VC investorov v CZ/SK. Pre PE, family office a angel investorov bude pomer kandidátov k zaradeným a čas kontroly iný (family office sú menej verejné).
- Prístup k registrom: ARES (CZ) a RPO (SK) sú zadarmo; v niektorých krajinách sú registre platené alebo bez API – v odhade nie sú zahrnuté poplatky za výpisy.
- Limity nástrojov (rate limit vyhľadávania) určujú skôr čas behu než cenu; pri ~240 tis. kandidátoch a ~10 paralelných agentoch ide o týždne behu, nie hodiny.

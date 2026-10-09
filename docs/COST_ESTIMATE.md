# Odhad nákladov na rozšírenie na celý svet

*Generované skriptom `python -m investordb.cli cost` z meraní v pilote. Ceny: oficiálny cenník Anthropic API (overený strojovo, [api_prices_md_checked.csv](../data/reference/api_prices_md_checked.csv), 9. 10. 2026); kurz ECB 1 € = 1.1186 USD.*

## 1. Čo stál pilot (namerané)

Všetci subagenti bežali na **Claude Haiku 5.5**. Náklad je prepočítaný na ceny API (pilot bežal v rámci predplatného Claude Code), podľa skutočnej spotreby tokenov zo záznamov agentov (`usage.py`).

| Etapa | Náklad (USD) |
|---|---|
| zber dôkazov (vrátane opakovaní) | 6.42 |
| prieskum a plánovanie (jednorazovo) | 0.86 |
| nezávislý AI overovateľ | 0.81 |
| objavovanie kandidátov | 0.63 |
| triáž sídla | 0.40 |
| etapa „nedávna investícia“ | 0.28 |
| kontrola duplicít | 0.06 |
| **spolu** | **9.45** |

- Na jedného kandidáta (objavovanie + triáž + dôkazy + nedávna investícia): **0.059 USD**
- Nezávislý overovateľ na jeden záznam: **0.012 USD**
- **Vyhľadávanie na webe tvorí 74 % nákladov na AI** – samotné tokeny Haiku sú zanedbateľné.
- Na 1 zaradeného investora pripadlo **5.3 kandidátov**; 2.3 % kandidátov skončilo v ručnej kontrole.
- Ručná kontrola: **4 min – predpoklad**, nahradí sa meraním z ručnej kontroly na záznam.

*Nezapočítané:* orchestrácia v hlavnej session (Claude Opus 5.5) – v produkčnom postupe ju nahrádza kód; a prístup k stránkam cez WebFetch v Claude Code vracia agentovi len výťah, kým API vracia celý text – preto je v modeli pripočítaných 6000 vstupných tokenov na každú stiahnutú stránku.

## 2. Scenáre pre celý svet

| Predpoklad | nízky | základný | vysoký | Odkiaľ |
|---|---|---|---|---|
| Overených investorov v databáze | 32 000 | 45 000 | 70 000 | PLAN.md, kap. 11.2 |
| Kandidátov na 1 zaradený záznam | 3.2 | 5.3 | 8.0 | pilot (základ); lepšie zdroje / horšie trhy |
| Viacjazyčnosť / ťažšie trhy (násobok AI) | 1.0× | 1.5× | 3.0× | predpoklad |
| Segmenty kontroly kvality (krajina × typ) | 80 | 150 | 250 | predpoklad |
| Presnosť odhadu na segment (±, 95 %) | 7 p. b. | 5 p. b. | 5 p. b. | voľba |
| Minút ručnej kontroly na záznam | 3.2 | 4.0 | 6.0 | pilot (základ) |
| Hodinová sadzba kontrolóra | 20 € | 30 € | 50 € | predpoklad (analytik CEE / západná Európa) |
| Vývoj produkčnej pipeline | 30 dní × 350 € | 45 dní × 450 € | 70 dní × 600 € | predpoklad |

| Výsledok (1. rok) | nízky | základný | vysoký |
|---|---|---|---|
| Kandidátov na spracovanie | 102 144 | 239 400 | 558 600 |
| AI (Haiku 5.5 + vyhľadávanie) | 5 686 € | 19 273 € | 88 459 € |
| Záznamov na ručnú kontrolu | 7 984 | 26 250 | 47 350 |
| Ľudská kontrola kvality | 8 516 € | 52 500 € | 236 750 € |
| Vývoj (jednorazovo) | 10 500 € | 20 250 € | 42 000 € |
| **Spolu 1. rok** | 24 702 € | 92 023 € | 367 209 € |
| Na 1 overený záznam | 0.77 € | 2.04 € | 5.25 € |
| Ročná aktualizácia (od 2. roka) | 5 498 € | 18 827 € | 69 576 € |

## 3. Čo z toho vyplýva

- **Hlavný náklad nie je AI, ale ľudská kontrola kvality.** V základnom scenári AI stojí 19 273 €, ľudská kontrola 52 500 €.
- **Najväčšia páka je zhoda AI overovateľa s človekom** (meraná v [PRECISION_REPORT.md](PRECISION_REPORT.md)). Ak je vysoká, človek kontroluje len segmentovú vzorku a záznamy, kde sa AI overovateľ a pravidlá nezhodnú; ak nízka, počet ručne kontrolovaných záznamov rastie.
- **Druhá páka je vyhľadávanie:** tvorí väčšinu nákladov na AI. Štruktúrované zdroje (registre SEC Form ADV, ESMA, národné registre, zoznamy asociácií) znižujú počet kandidátov na 1 zaradený záznam aj počet vyhľadávaní.
- **Tretia páka je kvalita zoznamu kandidátov:** v pilote bolo 5,3 kandidáta na 1 zaradeného investora; v krajinách bez dobrých zoznamov (a pri family office / angel investoroch) to bude viac.
- Model Haiku 5.5 stačí: všetky kroky, kde záleží na presnosti, robí deterministický kód (kontrola citácií, pravidlá, registre). Drahší model by zvýšil cenu AI ~20× bez zmeny tejto architektúry.

## 4. Obmedzenia odhadu

- Pilot meral VC investorov v CZ/SK. Pre PE, family office a angel investorov bude pomer kandidátov k zaradeným a čas kontroly iný (family office sú menej verejné).
- Prístup k registrom: ARES (CZ) a RPO (SK) sú zadarmo; v niektorých krajinách sú registre platené alebo bez API – v odhade nie sú zahrnuté poplatky za výpisy.
- Limity nástrojov (rate limit vyhľadávania) určujú skôr čas behu než cenu; pri ~240 tis. kandidátoch a ~10 paralelných agentoch ide o týždne behu, nie hodiny.

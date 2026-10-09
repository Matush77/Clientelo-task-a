# Clientelo – Zadanie A: Spoľahlivá databáza investorov

Návrh a overenie postupu, ako z **verejných zdrojov** zostaviť databázu investorov do firiem, v ktorej je **každý
záznam skutočný investor** a **každý údaj má zdroj, dátum a doslovnú citáciu** – overenú programom, nie len AI.
Pilot: **VC investori so sídlom v Česku a na Slovensku**.

## Výsledky v skratke

<!-- RESULTS:START -->
*(Doplní sa po ručnej kontrole vzorky – presnosť, zhoda AI s človekom, odhad úplnosti.)*
<!-- RESULTS:END -->

| | |
|---|---|
| Kandidátov z verejných zdrojov | 206 (po deduplikácii), z toho 133 prešlo zberom dôkazov |
| **Zaradených investorov** | **25** (21 CZ, 4 SK; úroveň dôvery A: 17, B: 8) |
| Vyradených / mimo rozsahu / na ručnú kontrolu | 65 / 40 / 3 |
| Tvrdení agentov strojovo overených na zdrojovej stránke | 820 z 852 (96 %) |
| Náklad AI na celý pilot (Claude Haiku 5.5, prepočet na ceny API) | ~9 USD |
| Odhad pre celý svet (1. rok, základný scenár) | pozri [COST_ESTIMATE.md](docs/COST_ESTIMATE.md) |

## Kde čo nájdete (požiadavky zadania)

| Požiadavka zadania | Súbor |
|---|---|
| Plán: kto v databáze bude a kto nie, ako sa overuje, odhad rozsahu a spoľahlivosti a z čoho vychádza | [docs/PLAN.md](docs/PLAN.md) |
| Dáta zo vzorky so zdrojom pri každom údaji | [data/processed/investors.csv](data/processed/investors.csv) (1 riadok = 1 investor) + [claims.csv](data/processed/claims.csv) (1 riadok = 1 údaj so zdrojom, dátumom, citáciou a výsledkom kontroly) |
| Zdroj a dátum, ktoré dokladajú, že subjekt investuje | stĺpce `last_investment`, `last_investment_date`, `last_investment_source` v investors.csv; všetky investície v claims.csv (`field = investments`) |
| Vyradené záznamy s dôvodom | [rejected.csv](data/processed/rejected.csv), všetky rozhodnutia v [decisions.csv](data/processed/decisions.csv) |
| Meranie presnosti na ručne overenej vzorke | [docs/PRECISION_REPORT.md](docs/PRECISION_REPORT.md) |
| Odhad nákladov na rozšírenie na celý svet | [docs/COST_ESTIMATE.md](docs/COST_ESTIMATE.md) |
| Ako som pracoval s AI (pokyny, kontrola, chyby agentov) | [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) + doslovné pokyny v [prompts/](prompts/) |
| Rozhodnutia pri nejasnostiach zadania | [docs/DECISIONS.md](docs/DECISIONS.md) |
| Export konverzácií s Claude Code | [ai-log/](ai-log/) |
| Kód s priebežnou históriou commitov | [src/investordb/](src/investordb/), [tests/](tests/), `git log` |

## Ako postup funguje

```
 verejné zoznamy      správy o            ┌─ registre ARES/RPO ─┐
 (asociácie, LP,      investičných   ──►  │  triáž: existuje?   │ ──► zber dôkazov ──► strojová kontrola ──► pravidlá ──► zmrazenie ──► ručná kontrola
  regulátori)  ──►    kolách              │  sídlo CZ/SK?       │     (AI agenti,       citácií (kód)        I1–I5,         (git tag)      vzorky + AI
  zoznam A            zoznam B            └─────────────────────┘      Haiku 5.5)                            E1–E9                         overovateľ
```

1. **Objavovanie kandidátov** – dva *nezávislé* zoznamy (A: členovia asociácií SLOVCA/CVCA, fondy podporené SIH/NRB/EIF;
   B: investori menovaní v správach o kolách českých a slovenských startupov) + **kontrolné sady** (crowdfundingové
   platformy, poradcovia, realitné fondy a náhodné firmy z registra s „investorským“ názvom). Prekryv A a B slúži na
   odhad úplnosti (capture–recapture).
2. **Triáž** – bezplatné vyhľadanie v registroch ARES (CZ) a RPO (SK); zahraničné fondy sa odfiltrujú lacno.
3. **Zber dôkazov** – AI agenti (výhradne Claude Haiku 5.5) vyplnia pevný záznam: každé pole = hodnota + URL +
   doslovná citácia + dátum. Odhadovať čísla je zakázané, „nenájdené“ je platná odpoveď.
4. **Strojová kontrola** – program stiahne každý zdroj (HTML, PDF, pri blokovaní archív Wayback) a overí, že citácia
   na stránke naozaj je a že hodnota je v citácii. **Tvrdenie, ktoré neprejde, sa zahodí.**
5. **Identita v registri** – IČO nájdené na webe investora alebo prísne porovnanie názvu s registrom.
6. **Pravidlá** ([rules.py](src/investordb/rules.py)) – zaradenie len pri overenej identite, ≥ 2 investíciách a ≥ 1
   datovanej v posledných 36 mesiacoch; inak vyradenie s kódom (E1–E9) alebo „mimo rozsahu“. Sumy prepočítava kód
   (kurz ECB), nie AI.
7. **Zmrazenie** (`git tag pilot-frozen`) → **ručná kontrola** náhodnej vzorky naslepo + **nezávislý AI overovateľ**
   na tých istých záznamoch → meranie presnosti a zhody AI s človekom.

## Ako som pracoval s AI (zhrnutie)

Podrobne v [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) (katalóg ~38 chýb a slabín).

- **Rozdelenie rolí:** ja rozhodujem o pravidlách a robím ručnú kontrolu; hlavná session Claude Code (Opus 5.5)
  orchestruje, píše kód a pokyny; **všetci subagenti bežia výhradne na Claude Haiku 5.5** (overené zo záznamov –
  53 behov); všetko, čo sa dá overiť bez AI, robí deterministický kód (97 testov).
- **Pokyny agentom** sú doslovne v [prompts/](prompts/) a verzované v gite (napr. zber dôkazov v1 → v2 → v3).
  Agenti čítajú pokyn priamo zo súboru, takže každý dostal presne verziu uloženú v repozitári.
- **Kontrola výstupu:** (1) agent smie a má povedať „neviem“; (2) každá citácia sa strojovo overí na stránke;
  (3) identita v registri; (4) nezávislý AI overovateľ; (5) ručná kontrola vzorky.
- **Kde sa AI mýlila (výber):** prieskumný agent mal 4 vecné chyby zo 16 čísel o veľkosti trhu (napr. neexistujúce
  „10 300 PE správcov“ – vyradené strojovo); agent upravil URL na neexistujúcu; agenti parafrázovali citácie zo
  stránok spracovaných nástrojom; v prvej verzii pokynu sa zastavili po 1–2 investíciách a zamietli skutočné aktívne
  VC (riešené pokynom v3); jeden agent pochopil schému JSON inak a kód jeho tvrdenia potichu zahodil (opravené +
  hlásenie). Chybovali aj **moje/Claudove úpravy kódu** – napr. kontrolór zahadzoval pätičky webov, PowerShell
  pokazil diakritiku, jednoslovné značky sa priradili k cudzím firmám (KAYA ≠ „KAYA, spol. s r.o.“) – všetko
  zachytené kontrolami a pokryté regresnými testami.
- **Bezpečnosť:** počas zberu sa ~9× objavili stránky s textom adresovaným AI (prompt injection); agenti ich
  ignorovali a výstup agentov sa aj tak nikdy nepreberá bez strojovej kontroly.

## Kľúčové rozhodnutia

Všetky (28) s dôvodmi v [docs/DECISIONS.md](docs/DECISIONS.md). Najdôležitejšie:

- Pilot **CZ + SK** namiesto len SK (samotné SK má príliš málo aktívnych VC na zmysluplné meranie).
- Investor = **≥ 2 investície do firiem, ≥ 1 v posledných 36 mesiacoch** (výnimka: nový fond).
- **1 záznam = 1 investičná firma/značka**; sídlo = kde sedí investičný tím, nie domicil fondu.
- **Celkový kapitál** = výslovné AUM, inak súčet overených veľkostí fondov v EUR (počíta kód).
- **Agregátory (Dealroom, PitchBook…) nikdy ako dôkaz**, len ako tip, kde hľadať.
- Metriky presnosti **definované vopred**; dáta **zmrazené** pred ručnou kontrolou.

## Čo chýba / obmedzenia

<!-- LIMITS:START -->
- **Úplnosť (recall):** pravidlo „jedna citácia musí obsahovať investora aj firmu“ a zákaz agregátorov znamenajú, že
  niektorí skutoční aktívni investori skončili vyradení pre nedostatok dôkazov (napr. Vision Ventures, JIC Ventures).
  Presnosť má prednosť pred úplnosťou – zodpovedá to zadaniu („každý záznam musí byť skutočný investor“).
- **3 záznamy čakajú na ručnú identifikáciu** (KAYA, Zero One Hundred – bez spoľahlivej zhody v registri; 10VC – zdroje
  blokujú prístup).
- **Pilot pokrýva len VC v CZ/SK.** PE, family office a angel investori sú v pravidlách a taxonómii, ale neboli
  pilotne overené; odhady pre ne sú hypotézy (PLAN.md, kap. 11).
- **Dátum investície** sa pri niektorých záznamoch odvodzuje od dátumu článku, nie od dátumu obchodu.
- **Ručná kontrola** je jedna osoba (ja) – bez druhého nezávislého hodnotiteľa.
<!-- LIMITS:END -->

## Spustenie

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"
.venv/Scripts/python -m pytest
```

Pipeline krok za krokom (kroky s AI agentmi sa spúšťajú z Claude Code podľa pokynov v `prompts/`):

```bash
python -m investordb.cli check-quotes data/reference/universe_anchors.csv   # overenie čísel v pláne
python -m investordb.seeds                                                   # náhodné firmy z registra (kontrola E7)
python -m investordb.cli check-discovery                                     # kontrola citácií z objavovania
python -m investordb.candidates                                              # deduplikácia kandidátov
python -m investordb.triage && python -m investordb.triage --apply-hq-triage # registre + sídlo
python -m investordb.batches                                                 # dávky pre agentov
python -m investordb.cli evidence                                            # kontrola všetkých tvrdení
python -m investordb.cli decide --as-of 2026-10-09                           # pravidlá → investors/rejected
python -m investordb.cli check-db                                            # integrita databázy
python -m investordb.cli sample                                              # vzorka + formulár ručnej kontroly
python -m investordb.cli report                                              # meranie presnosti
python -m investordb.usage && python -m investordb.cli cost                  # odhad nákladov
python tools/export_ailog.py <session-export.zip>                            # ai-log
```

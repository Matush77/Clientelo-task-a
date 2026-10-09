# Clientelo – Zadanie A: Spoľahlivá databáza investorov

Návrh a overenie postupu, ako z **verejných zdrojov** zostaviť databázu investorov do firiem, v ktorej je **každý
záznam skutočný investor** a **každý údaj má zdroj, dátum a doslovnú citáciu** – overenú programom, nie len AI.
Pilot: **VC investori so sídlom v Česku a na Slovensku**.

## Výsledky v skratke

<!-- RESULTS:START -->
| | |
|---|---|
| Kandidátov z verejných zdrojov | 206 (po deduplikácii), z toho 133 prešlo zberom dôkazov |
| **Zaradených investorov** | **24** (20 CZ, 4 SK; úroveň dôvery A: 15, B: 9) – [investors.csv](data/processed/investors.csv), spresnená verzia [investors_refined.csv](data/processed/investors_refined.csv) |
| Vyradených / mimo rozsahu / na ručnú kontrolu | 70 / 35 / 4 |
| Tvrdení agentov strojovo overených na zdrojovej stránke | 808 z 852 (95 %); pri spresnení 144 zo 147 (98 %) |
| **Presnosť zaradenia** (slepá kontrola Claude Sonnet 5.5) | **23/23 = 100 %** (95 % CI 85,7–100 %) |
| **Ručná kontrola autora** (5 záznamov, D40) | zaradené potvrdené 4/4, návnada správne vyradená; Sonnet sa s človekom zhodol v 4/5 (v piatom nevedel rozhodnúť); celkový kapitál človek z verejných zdrojov neoveril ani raz („neviem“ 4/4) |
| Presnosť polí (zmrazená v3) | sektory 17/17, tiket 15/15, zdroje dokladajú investície 19/23 (83 %), celkový kapitál 6/12 (50 %) |
| **Spresnenie Sonnetom 5.5 – slepá kontrola faktov pred → po** | celkový kapitál 8/15 (53 %) → **14/20 (70 %)**, vyplnený pri 15 → 20 z 24; dátum obchodu 54/68 (79 %) → **78/80 (97,5 %)**; identita v registri 24/24 – [REFINEMENT.md](docs/REFINEMENT.md) |
| Pokrytie (capture–recapture) | ~78 % z odhadovaných ~31 aktívnych VC so sídlom v CZ/SK |
| Ľudský audit (v1 → v2 → v3) | našiel chyby výkladu (kapitál „30 €“, plánovaný fond ako kapitál, chybné IČO) → 2 opravy pipeline – [AUDIT_V2.md](docs/AUDIT_V2.md) |
| Náklad AI na celý pilot (prepočet na ceny API) | ~42 USD: Haiku ~9,5 USD; Sonnet – kontrola vzorky 7,8, spresnenie 18,1, kontrola faktov 6,3 USD |
| Odhad pre celý svet, 1. rok (základ) | ~97 tis. € (AI ~20 tis., ľudská kontrola ~57 tis., vývoj ~20 tis.); s odporúčaným spresnením Sonnetom ~142 tis. € – [COST_ESTIMATE.md](docs/COST_ESTIMATE.md) |

**Hlavné zistenie.** Rozhodnutie, *kto je investor*, sa dá z verejných zdrojov urobiť spoľahlivo. Údaje *o
investíciách* verejné články často neuvádzajú jednoznačne a lacný model ich vykladal zle – ako dátum obchodu bral
dátum článku, ktorý staršiu investíciu len spomína, a ako kapitál cieľovú veľkosť fondu:

- len 60 % investícií má dátum obchodu a len 22 % uvedenú sumu;
- cielené spresnenie silnejším modelom **len pri zaradených záznamoch** zlepšilo dátumy obchodov zo 79 % na 97,5 %
  a celkový kapitál z 53 % na 70 % (meraná slepou kontrolou faktov);
- zvyšné chyby kapitálu sú podhodnotenia (chýba starší fond alebo navýšenie), nie ciele počítané ako kapitál.
<!-- RESULTS:END -->

## Kde čo nájdete (požiadavky zadania)

| Požiadavka zadania | Súbor |
|---|---|
| **Zhrnutie na jednu stranu** | [docs/SUMMARY.md](docs/SUMMARY.md) |
| Plán: kto v databáze bude a kto nie, ako sa overuje, odhad rozsahu a spoľahlivosti a z čoho vychádza | [docs/PLAN.md](docs/PLAN.md) |
| Dáta zo vzorky so zdrojom pri každom údaji | [data/processed/investors.csv](data/processed/investors.csv) (1 riadok = 1 investor) + [claims.csv](data/processed/claims.csv) (1 riadok = 1 údaj so zdrojom, dátumom, citáciou a výsledkom kontroly) |
| Zdroj a dátum, ktoré dokladajú, že subjekt investuje | stĺpce `last_investment`, `last_investment_date`, `last_investment_source` v investors.csv; všetky investície v claims.csv (`field = investments`) |
| Vyradené záznamy s dôvodom | [rejected.csv](data/processed/rejected.csv), všetky rozhodnutia v [decisions.csv](data/processed/decisions.csv) |
| Meranie presnosti na ručne overenej vzorke | [docs/PRECISION_REPORT.md](docs/PRECISION_REPORT.md) |
| Spresnenie slabých polí silnejším modelom a meranie pred / po | [docs/REFINEMENT.md](docs/REFINEMENT.md), spresnená verzia [investors_refined.csv](data/processed/investors_refined.csv) |
| Prehliadač investorov: každá hodnota so zdrojom a citáciou | [docs/explorer.html](docs/explorer.html) (stiahnuť a otvoriť v prehliadači, funguje offline) |
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

Podrobne v [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) (katalóg 58 chýb a slabín).

- **Rozdelenie rolí:**
  - ja rozhodujem o pravidlách a robím kvalitatívny audit;
  - hlavná session Claude Code (Opus 5.5) orchestruje, píše kód a pokyny;
  - **zber a overovanie dát robia subagenti Claude Haiku 5.5**; slepú kontrolu vzorky, spresnenie kapitálu
    a dátumov pri zaradených záznamoch a kontrolu faktov pred / po robí **Claude Sonnet 5.5**
    (modely overené zo záznamov agentov);
  - všetko, čo sa dá overiť bez AI, robí deterministický kód (162 testov).
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

Všetky (41) s dôvodmi v [docs/DECISIONS.md](docs/DECISIONS.md). Najdôležitejšie:

- Pilot **CZ + SK** namiesto len SK (samotné SK má príliš málo aktívnych VC na zmysluplné meranie).
- Investor = **≥ 2 investície do firiem, ≥ 1 v posledných 36 mesiacoch** (výnimka: nový fond).
- **1 záznam = 1 investičná firma/značka**; sídlo = kde sedí investičný tím, nie domicil fondu.
- **Celkový kapitál** = výslovné AUM, inak súčet overených veľkostí fondov v EUR (počíta kód).
- **Agregátory (Dealroom, PitchBook…) nikdy ako dôkaz**, len ako tip, kde hľadať.
- Metriky presnosti **definované vopred**; dáta **zmrazené** pred ručnou kontrolou.

## Čo chýba / obmedzenia

<!-- LIMITS:START -->
- **Ručne overená vzorka je malá (D34, D36, D40).** Zadanie žiada meranie na ručne overenej vzorke. Ručne som
  overil 5 záznamov (4 zaradené, 1 návnadu) – všetky v zhode s pipeline; presnosť na celej vzorke (34 záznamov) meria
  **slepá kontrola modelom Claude Sonnet 5.5**, porovnaná s druhým modelom (Haiku) a s mojou kontrolou (zhoda 4/5,
  bez priameho rozporu). Predtým môj kvalitatívny audit formulára našiel chyby, ktoré viedli k dvom opraveným verziám
  dát (`pilot-frozen-v2`, `-v3`), a hlavné zistenie o nejasnosti článkov.
- **Haiku na výklad článkov nestačí.** Zber dôkazov robil lacný model, ktorý často nerozlíšil dátum článku od dátumu
  obchodu ani cieľový fond od uzavretého. Riešené cieleným spresnením modelom Sonnet 5.5 pri zaradených záznamoch
  (D38): dátumy obchodov 97,5 %, kapitál 70 %. Spresnenie aj kontrolu faktov robil model tej istej rodiny, takže
  korelované chyby nemožno vylúčiť; zmrazená v3 ostáva ako meraná verzia, spresnená je zvlášť.
- **Úplnosť (recall):** pravidlo „jedna citácia musí obsahovať investora aj firmu“ a zákaz agregátorov znamenajú, že
  niektorí skutoční aktívni investori skončili vyradení pre nedostatok dôkazov (napr. Vision Ventures, JIC Ventures).
  Presnosť má prednosť pred úplnosťou – zodpovedá to zadaniu („každý záznam musí byť skutočný investor“).
- **4 záznamy čakajú na ručnú identifikáciu.** KAYA, Nation1 a Zero One Hundred nemajú spoľahlivú zhodu v registri,
  pri 10VC zdroje blokujú prístup. Radšej bez identity než s cudzou firmou (D35).
- **Pilot pokrýva len VC v CZ/SK.** PE, family office a angel investori sú v pravidlách a taxonómii, ale neboli
  pilotne overené; odhady pre ne sú hypotézy (PLAN.md, kap. 11).
- **Dátum investície:** ~40 % investícií je len „v portfóliu“ bez dátumu obchodu; zvyšok má dátum z oznámenia, ktorý
  sa môže líšiť od dátumu obchodu.
- **Malá vzorka:** 23 zaradených záznamov dáva široký interval spoľahlivosti (85,7–100 %).
<!-- LIMITS:END -->

## Spustenie

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"
.venv/Scripts/python -m pytest
```

Na Windows treba repozitár naklonovať do krátkej cesty (napr. `C:\src\task-a`), inak inštalácia `lxml` zlyhá na
dĺžke cesty. Overené na čistom klone z GitHubu: testy prechádzajú a `check-db` hlási 0 problémov.

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
python -m investordb.cli refine batches                                      # spresnenie (D38): dávky pre Sonnet
python -m investordb.cli refine check                                        # kontrola spresnených tvrdení
python -m investordb.cli refine judge-batches                                # slepá kontrola faktov pred / po
python -m investordb.cli refine report                                       # docs/REFINEMENT.md
python -m investordb.cli explorer                                            # docs/explorer.html
python -m investordb.usage && python -m investordb.cli cost                  # odhad nákladov
python tools/export_ailog.py <session-export.zip>                            # ai-log
```

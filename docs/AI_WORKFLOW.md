# Ako som pracoval s AI

Dokument sa dopĺňa priebežne počas celej práce. Úplné prepisy konverzácií (vrátane všetkých subagentov) sú
v [ai-log/](../ai-log/).

## 1. Rozdelenie rolí

| Kto | Model | Čo robí |
|---|---|---|
| **Ja (človek)** | – | rozhodujem o rozsahu a pravidlách, schvaľujem plán na kontrolných bodoch, ručne overujem vzorku |
| **Hlavná session Claude Code** | Claude Opus 5.5 | orchestrácia: navrhuje plán, píše kód a pokyny pre agentov, spúšťa agentov, kontroluje ich výstupy, počíta metriky, píše dokumentáciu, commituje |
| **Subagenti** | Claude Haiku 5.5 (výhradne) | vyhľadávanie na webe a malé, presne ohraničené úlohy: prieskum, zber kandidátov, zber dôkazov, nezávislé overovanie |
| **Python kód** | – (deterministický) | všetko, čo sa dá overiť bez AI: stiahnutie zdroja, kontrola citácie, dátumy, pravidlá, vzorkovanie, metriky |

Prečo Haiku pre subagentov: vyhľadávanie a extrakcia sú jednoduché, opakované úlohy a Haiku je výrazne lacnejší.
Slabšiu spoľahlivosť menšieho modelu vyvažujeme tým, že **výstupy agentov nikdy neberieme ako fakt**: každé tvrdenie
musí mať zdroj a citáciu a tie overuje kód.

## 2. Ako agenti dostávajú pokyny

Všetky pokyny sú doslovne uložené v priečinku [prompts/](../prompts/) a verzované v gite, takže je vidieť aj ich
vývoj (v1 → v2…). Pokyny dodržiavajú tieto zásady:

1. **Úzke zadanie s jasným výstupom** – presne čo hľadať, v akom formáte vrátiť (tabuľka / JSON), s limitom dĺžky.
2. **Povinný zdroj pri každom tvrdení** – URL + doslovná citácia + dátum.
3. **Povolené „neviem“** – agent musí označiť neoverené veci (`UNVERIFIED`, `not_found`) namiesto domýšľania.
4. **Zákaz odhadov čísel** – žiadne dopočítavanie AUM ani tiketov.
5. **Agent nezapisuje súbory** – výstup kontrolujem ja a až potom sa niečo uloží.

## 3. Ako kontrolujem výstupy agentov

| Vrstva | Čo chytá | Príklad z tohto projektu |
|---|---|---|
| Samooznačovanie agentom (`UNVERIFIED`) | agent vie, že niečo len predpokladá | agent R3 označil predpokladaný bývalý názov fondu ako neoverený |
| Nezávislý overovací agent s povinnou doslovnou citáciou | čísla prevzaté z druhej ruky, chybné roky | R5 overuje čísla z R1 priamo na primárnych zdrojoch |
| Kritik plánu (iný agent, iná úloha) | slepé miesta v návrhu | R4 našiel 12 slabín plánu |
| Deterministická kontrola v Pythone | vymyslené URL a citácie, nesúlad hodnoty s citáciou | [validate.py](../src/investordb/validate.py) – vyradila chybné číslo agenta R1 (C7) |
| Ručná kontrola náhodnej vzorky | všetko ostatné, vrátane chybného zaradenia | kontrolný bod CP4 |

## 4. Katalóg chýb a slabín agentov

Priebežne dopĺňaný zoznam. Ku každej chybe uvádzam, ako sa prejavila, ako som ju zachytil a čo som zmenil.

| # | Agent | Chyba / slabina | Ako zachytená | Opatrenie |
|---|---|---|---|---|
| C1 | R1 (veľkosť trhu) | Čísla z druhej ruky (útržok z vyhľadávania, recenzia tretej strany) prezentované vedľa primárnych zdrojov – napr. počet PE správcov podľa Preqin len z knižničného návodu, počet investorov v Dealroom z recenzie | agent ich sám čiastočne označil; ja som skontroloval typ zdroja pri každom čísle | čísla sa nepoužijú bez overenia na primárnom zdroji (agent R5) |
| C2 | R1 | Rozporné čísla pre „to isté“ – PitchBook 59 tis. VC investorov vs. 481 tis. / 635 tis. investorov; OpenVC 16 tis. vs. 20 tis.+ | porovnanie hodnôt v tabuľke | počty profilov v agregátoroch nie sú porovnateľné s počtom firiem → ako hlavné kotvy odhadu sa použijú **počty z registrov** (SEC, ESMA…) |
| C3 | R3 (SK trh) | Uviedol pravdepodobný, ale nepotvrdený bývalý názov fondu („Zero One Hundred, predtým Zero Gravity Capital“) | agent to sám označil `UNVERIFIED` | presne takýto typ chyby (vierohodne znejúci, ale vymyslený fakt) musí chytať kontrola citácií; identitu subjektov preto overujeme v registri, nie podľa AI |
| C4 | R3 | Ako „dôkaz aktivity“ použil agregátory (Caplight, Seedtable, Vestbee, PitchBook) | kontrola typu zdroja | pokyn pre zber dôkazov výslovne zakáže agregátory (T4) ako jediný dôkaz |
| C5 | R2, R3 | Nevedel prečítať PDF (špecifikácia SEC Form D, EBAN 2024), viaceré stránky vrátili 403/404 | agent to uviedol | pipeline potrebuje `pypdf` a stav `blocked` → ručná kontrola; overené v spike (deň 2) |
| C6 | R3 | Odhad „len 3–4 aktívne VC so sídlom na Slovensku“ zo zbežného vyhľadávania – pravdepodobne nízka úplnosť, zatiaľ nepotvrdené | porovnanie s vlastnou znalosťou trhu | rozsah pilotu rozšírený na CZ + SK; úplnosť zmeria pilot (capture–recapture) |
| C7 | R1 | **Nesprávne číslo:** „~10 300 aktívnych PE správcov (Preqin)“. Na citovanej stránke nie je; oficiálna stránka Preqin uvádza 31 653, zdroj CBS 34 100. | R5 (overovací agent) + **strojová kontrola: `quote_not_found`** | číslo vyradené; použité overené hodnoty |
| C8 | R1 | **Zastarané údaje vydávané za najnovšie:** angel investori v USA 323 365 (2019) uvedené ako najnovšie, hoci existuje správa za 2024 (445 535) | R5 | v odhade použitá hodnota za 2024, overená strojovo priamo z PDF |
| C9 | R1 | Počet investorov v Dealroom „225K“ prevzatý z recenzie tretej strany; oficiálna stránka uvádza „100K+ investors & funds“ | R5 + strojová kontrola | použitá oficiálna hodnota |
| C10 | R1 | Tvrdil, že čísla SEC (362 VC poradcov, 4 392 VC fondov) videl na stránke; R5 ich tam nenašiel a stránka SEC blokuje automatický prístup (403) | R5 + strojová kontrola (`blocked`) | čísla SEC sa v odhade zatiaľ nepoužívajú |
| C11 | **ja + Claude (kód)** | Chyba v mojom parseri čísel: „December 2022, 462 fondov“ prečítal ako jedno číslo 2022462 → falošné `value_not_in_quote` | podozrivý výsledok kontroly pri čísle, ktoré na stránke zjavne je | oprava regulárneho výrazu + regresný test; ukazuje, že aj deterministický kontrolór treba testovať |

**Zhrnutie overenia kotiev (R1 → R5 → kód):** zo 14 tvrdení o veľkosti trhu kód potvrdil 10, 1 vyvrátil (C7) a 4 sa
nedali strojovo overiť, lebo stránky (NVCA, SEC) blokujú automatický prístup – tie idú na ručnú kontrolu.
Prvý prieskumný agent (R1) mal v číslach **4 vecné chyby zo 16 riadkov** – preto sa výstup AI nikdy nepoužíva bez
overenia.

**Hodnotenie kritika plánu (R4):** z 12 pripomienok som 9 prijal (napr. vopred definované metriky, rozhodovacia
tabuľka hraničných prípadov, pevný dátum `as_of`, capture–recapture, zjednodušenie modulov), 2 čiastočne
(GDPR – pilot obsahuje len firmy; „overiť všetky záznamy“ – overíme všetky, len ak ich bude ≤ 35) a 1 odmietol
(slepé opätovné hodnotenie po týždni – nezmestí sa do termínu).

**Pozorovanie:** subagenti dostali vo výsledkoch nástrojov systémovú pripomienku hlavnej session (plan mode) a
správne ju ignorovali – prompt im zakazoval zapisovať súbory.

## 5. Priebeh práce

| Deň | Čo sa robilo | Agenti |
|---|---|---|
| 8. 10. | Analýza zadania, prieskum verejných zdrojov a trhu, návrh plánu, kritika plánu, otázky na mňa (rozsah pilotu, spôsob behu, jazyk, ručná kontrola), založenie repozitára, PLAN.md | R1–R3 (prieskum), R4 (kritik), R5 (overenie čísel) |

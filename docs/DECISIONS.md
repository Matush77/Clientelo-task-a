# Rozhodnutia

Zadanie necháva niektoré veci otvorené („rozhodnite podľa seba a zdôvodnite“). Tu je každé rozhodnutie,
jeho dôvod a dátum. Novšie rozhodnutia sa pridávajú na koniec.

| # | Dátum | Rozhodnutie | Dôvod |
|---|---|---|---|
| D1 | 8. 10. | **Pilot = VC investori so sídlom v Česku a na Slovensku** (nie len SK). | Prvotný prieskum naznačil, že aktívnych VC so sídlom na Slovensku je len jednotky až nízke desiatky. Z 15 záznamov by mal interval spoľahlivosti presnosti šírku okolo ±15 p. b., čo nemá výpovednú hodnotu. CZ a SK majú prepojený ekosystém, spoločný jazykový priestor a verejné registre. |
| D2 | 8. 10. | Investor musí mať **≥ 2 zdokumentované investície** a **≥ 1 v posledných 36 mesiacoch**. Výnimka: nový fond (≤ 24 mesiacov) s datovaným uzavretím a ≥ 1 investíciou. | 2 investície odlišujú opakovaného investora od holdingu, ktorý raz kúpil firmu. 36 mesiacov zodpovedá investičnému obdobiu VC fondov, keď medzi investíciami bývajú dlhšie pauzy. Bez výnimky by sme vyradili nové fondy, ktoré sú pre používateľa databázy najzaujímavejšie. |
| D3 | 8. 10. | Okno 36 mesiacov sa počíta od dátumu **`as_of` = dátum zmrazenia dát** (`git tag pilot-frozen`). | Pevný referenčný dátum robí výsledok reprodukovateľným. |
| D4 | 8. 10. | **1 záznam = 1 investičná firma/značka**. Fondy, správcovské spoločnosti a sesterské s.r.o. sú aliasy. | Používateľ hľadá „s kým hovoriť o investícii“, nie právnu štruktúru. Inak by vznikali duplicity (E8). |
| D5 | 8. 10. | **Sídlo = krajina, kde pôsobí investičný tím** (správcovská spoločnosť), nie domicil fondu. | Mnohé české a slovenské fondy sú právne v Luxembursku alebo Holandsku, ale rozhoduje sa v Prahe či Bratislave. |
| D6 | 8. 10. | **Fondy fondov (LP) sa nezaraďujú** (E5). Ich priamo investujúce dcéry áno. | Zadanie hovorí o investoroch **do firiem**. |
| D7 | 8. 10. | Akcelerátory, angel siete a PE sú v pilote **mimo rozsahu (OOS)**, nie chyba. | Pilot má podľa zadania overiť VC fondy. Ostatné typy sú v taxonómii pre celosvetovú verziu. |
| D8 | 8. 10. | **Agregátory (Dealroom, PitchBook, Vestbee…) len na objavovanie kandidátov**, nikdy ako jediný dôkaz. LinkedIn sa nepoužíva. | Podmienky použitia zakazujú zber a publikovanie ich dát a sú to sekundárne zdroje. Zadanie vyžaduje verejné dáta. |
| D9 | 8. 10. | **AI nesmie odhadovať čísla.** Ak údaj nie je verejný, pole ostane prázdne s označením `not_public`. | Spoľahlivosť je podľa zadania kľúčová a prázdne pole je poctivejšie ako vymyslené číslo. |
| D10 | 8. 10. | **Primárna metrika presnosti je prísna**: skutočný investor ∧ aktívny ∧ správny typ ∧ správne sídlo. Presnosť polí (sektor, tiket, kapitál) sa meria zvlášť. Metriky sú definované vopred. | Odpovedá na hlavnú otázku zadania („je to skutočný investor?“). Subjektívne polia by výsledok rozmazali. Vopred definované metriky bránia dodatočnému prispôsobeniu. |
| D11 | 8. 10. | **Ručne sa overuje náhodná stratifikovaná vzorka** (~30 zaradených + ~10 vyradených), nie všetko. Kontrolór nevidí citácie agenta, len zdrojové URL. | Časový rozpočet (deadline 16. 10.). Bez citácií agenta sa kontrolór nenechá ovplyvniť a zdroj si otvorí sám. |
| D12 | 8. 10. | **Postup: Claude Code orchestruje, web vyhľadávajú agenti Claude Haiku 5.5, deterministické kontroly robí Python.** Nepoužíva sa priamo API. | Haiku je lacný a na vyhľadávanie stačí. Kontrolu nechávame na deterministický kód, nie na ďalšie AI. Náklady sa merajú zo záznamov agentov a prepočítajú sa cenníkom API. |
| D13 | 8. 10. | Dokumentácia **po slovensky**, kód a komentáre po anglicky. | Zadanie je po slovensky. Kód sa v praxi píše po anglicky. |
| D14 | 8. 10. | **GDPR:** pilot obsahuje len právnické osoby, mená partnerov fondov sa nezbierajú. Pre celý svet sa angel investori zaraďujú len z ich vlastného verejného investorského profilu, s minimom údajov. | Minimalizácia osobných údajov. Oprávnený záujem je obhájiteľný len pri údajoch, ktoré osoba sama zverejnila. |
| D15 | 8. 10. | `ai-log/` sa plní exportom z desktopovej aplikácie Claude Code (ekvivalent `/export`) vrátane prepisov agentov. Pred commitom sa z exportu odstráni e-mail používateľa. | Export z aplikácie obsahuje aj prepisy subagentov, teda úplnejší obraz práce s AI. E-mail nepatrí do verejného repozitára. |
| D16 | 8. 10. | Commity sa podpisujú GitHub no-reply adresou autora a obsahujú `Co-Authored-By: Claude`. | Transparentnosť, že kód vznikal s AI. Žiadny osobný e-mail vo verejnej histórii. |

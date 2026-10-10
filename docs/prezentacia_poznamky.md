# Prezentácia – poznámky k prezentovaniu

Slajdy: [prezentacia.pdf](prezentacia.pdf). Poznámky sú text, ktorý hovorím pri každom slajde; PDF ich neobsahuje.

## 1. Spoľahlivá databáza investorov

*Zadanie A · pilot CZ + SK*

Zadanie A: spoľahlivá databáza investorov. Pilot som robil na VC investoroch so sídlom v Česku a na Slovensku. Celý projekt stojí na jednej myšlienke, ktorú vidíte vpravo: každý údaj v databáze je tvrdenie so zdrojom a doslovnou citáciou a program overí, že citácia na stránke naozaj je.

## 2. Kto je investor, sa dá overiť spoľahlivo

*Výsledok v skratke*

Štyri čísla. 24 investorov prešlo všetkými pravidlami. Slepá kontrola silnejším modelom potvrdila všetkých 23 hodnotených ako skutočných, aktívnych VC so sídlom v CZ/SK; interval spoľahlivosti je kvôli malej vzorke 86 až 100 percent. 95 percent všetkých tvrdení agentov program overil priamo na stránke zdroja. Pokrytie odhadujem metódou capture-recapture z dvoch nezávislých zoznamov na približne 78 percent. Hlavné zistenie: identita investora je spoľahlivá, údaje o investíciách sú ťažšie – k tomu sa vrátim pri spresnení.

## 3. Každý údaj je tvrdenie s dôkazom

*Hlavná myšlienka*

AI tu nerozhoduje. AI je zberač dôkazov: Haiku agent vráti tvrdenie s URL a doslovnou citáciou. Program stránku stiahne a citáciu na nej hľadá; ak ju nenájde alebo hodnota v citácii nie je, tvrdenie zahodí. Identitu firmy berie z registra, nie od agenta. O zaradení rozhoduje kód podľa vopred napísaných pravidiel. Tým je halucinácia AI zachytená mechanicky, nie dôverou v model.

## 4. Kto sa do databázy dostane

*Pravidlá zaradenia*

Pravidlá som napísal pred zberom dát. Najdôležitejšie je I2: investor musí mať aspoň dve doložené investície a aspoň jednu za posledné tri roky – tým odfiltrujem neaktívne fondy aj firmy, ktoré majú investíciu len v názve. E7 je presne problém „náhodnej firmy“: v registri je veľa s.r.o. s Capital alebo Invest v mene, ktoré do startupov neinvestujú. Do kontrolnej sady som ich zámerne pridal ako návnady. Mimo rozsahu (OOS) nie je chyba – je to skutočný investor, len nie VC z CZ/SK.

## 5. Od 206 kandidátov k 24 investorom

*Lievik kandidátov*

Zoznam A sú štruktúrované zdroje: členovia asociácií SLOVCA a CVCA a fondy podporené štátnymi programami a EIF. Zoznam B sú investori menovaní v správach o kolách startupov. Agenti zoznamu B zoznam A nevideli, preto z prekryvu viem odhadnúť pokrytie. Pridal som aj 18 návnad – crowdfundingové platformy, poradcov, realitné fondy a náhodné firmy s investorským názvom –, aby som videl, či ich pravidlá správne vyradia. Najčastejší dôvod vyradenia je E7: investorské meno bez jedinej doloženej investície.

## 6. Štyri vrstvy kontroly

*Overovanie*

Prvé dve vrstvy sú deterministický kód a bežia na každom tvrdení. Tretia je druhý AI názor bez prístupu k verdiktu pipeline. Štvrtá je meranie: po zmrazení dát som vzorku dal naslepo posúdiť silnejšiemu modelu Sonnet a sám som ju prešiel. Ľudská kontrola našla chyby výkladu, ktoré všetky automatické vrstvy prehliadli – preto som dáta zmrazil trikrát – v1, v2 a v3 – a každú opravu som urobil systémovo v kóde, nikdy ručnou úpravou záznamu.

## 7. Chyby, ktoré kontroly zachytili

*Kde AI chybovala*

Toto je pre mňa najdôležitejší slajd. Tri chyby výkladu som našiel sám za pár minút pri prezeraní formulára, hoci prešli všetkými automatickými kontrolami: citácia bola na stránke, len ju AI zle vyložila – napríklad cieľová veľkosť fondu nie je kapitál. Štvrtú našiel silnejší model. Každú chybu som opravil systémovo a pridal test z reálneho záznamu. Ponaučenie: strojová kontrola citácií chráni pred halucináciou, nie pred zlým výkladom pravdivého textu.

## 8. Záznamy sedia, polia o kapitáli nie

*Meranie presnosti*

Primárnu metriku som definoval vopred: záznam je správny, len ak platia všetky štyri podmienky naraz. Kontrolór dostal rovnaké informácie ako formulár pre človeka a zdroje si otváral sám. Pri 23 záznamoch je dolná hranica 95-percentného intervalu 86 percent – na presnejšie číslo treba väčšiu vzorku, preto je ľudská kontrola v nákladoch na celý svet najväčšou položkou. Sám som ručne overil päť záznamov – štyri zaradené a jednu návnadu, z toho dva, pri ktorých sa AI kontrolóri nezhodli. Všetkých päť sedí s výsledkom pipeline; Sonnet sa so mnou zhodol v štyroch, pri návnade bez webu nevedel rozhodnúť. Kapitál vyšiel 50 percent: cieľové fondy a prvé uzavretia sa počítali ako uzavreté fondy a staršie fondy chýbali – a ani ja som ho z verejných zdrojov nevedel overiť. To riešim na ďalšom slajde.

## 9. Sonnet opravil dátumy obchodov aj kapitál

*Spresnenie silnejším modelom*

Haiku pri zbere často bral dátum článku, ktorý staršiu investíciu len spomína, ako dátum obchodu, a cieľovú veľkosť fondu ako kapitál. Preto som silnejší model Sonnet pustil cielene len na 24 zaradených záznamov a len na tieto dve polia: zistiť stav každého fondu a skutočný dátum oznámenia každej investície. Nové tvrdenia prešli rovnakými strojovými kontrolami. Zlepšenie meral iný agent, ktorý dostal hodnoty z oboch verzií zmiešané a nevedel, ktorá je nová. Dátumy obchodov stúpli zo 79 na 97,5 percenta, kapitál z 53 na 70 percent. Spresnenie stálo 0,75 dolára na záznam. Limit: spresňoval aj kontroloval model tej istej rodiny.

## 10. Doložiteľných je ~45 tisíc investorov

*Celý svet*

Odhad ide v troch krokoch: známy trh podľa kotiev, z neho verejne viditeľní, z nich doložiteľní datovaným dôkazom. Každú kotvu našiel agent, ale do odhadu sa dostala až potom, čo program stiahol zdroj a číslo na ňom našiel – jedno číslo od agenta takto vypadlo, lebo na stránke nebolo. Spoľahlivosť sa líši podľa typu: VC a PE fondy investície zverejňujú, family office sa publicite vyhýbajú a pri angel investoroch v EÚ navyše platí GDPR – zaradiť možno len tých s vlastným verejným profilom investora.

## 11. Drahá je ľudská kontrola, nie AI

*Náklady*

Pilot bežal v predplatnom Claude Code, náklad je prepočítaný na ceny API zo skutočnej spotreby tokenov každého agenta. Celý pilot vrátane kontrol a spresnenia vyšiel na 47 dolárov. Pre celý svet som vzal základný odhad 45 tisíc investorov a namerané hodnoty z pilotu: 5,5 kandidáta na jedného zaradeného investora, cenu za kandidáta a čas kontroly. Najväčšia položka je ľudská kontrola kvality, aby bola presnosť známa v každom segmente krajina krát typ investora. Spresnenie Sonnetom pridá asi 45 tisíc eur, ale beží len na zaradené záznamy, nie na všetkých kandidátov – to by stálo dvojnásobok.

## 12. Čo by som urobil pred rozšírením

*Ďalší krok*

Štyri veci, ktoré by som urobil pred rozšírením na celý svet. Najdôležitejšia je väčšia ručne overená vzorka – presnosť na malej vzorke má široký interval. Druhá: spresnenie silnejším modelom zapojiť natrvalo, ale len na zaradené záznamy, kde je lacné. Tretia: jedna ďalšia krajina ako test, koľko stojí iný jazyk. Štvrtá: začínať zo štruktúrovaných registrov, lebo vyhľadávanie je najdrahšia časť AI.

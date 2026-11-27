# Projekt: Kvizova hra

## Cil projektu
Vytvorit jednoduchou vedomostni hru, ve ktere uzivatel odpovida na otazky s moznostmi A, B a C.

## Funkce
- Zobrazeni vedomostnich otazek
- Nabidka tri moznosti odpovedi
- Kontrola spravnosti odpovedi
- Pocitani ziskanych bodu
- Zaverecne vyhodnoceni vysledku

## Navod k pouziti
1. Spustte soubor `kvizova_hra.py`.
2. Prectete si zobrazovanou otazku.
3. Vyberte odpoved pomoci pismene A, B nebo C.
4. Po zodpovezeni vsech otazek se zobrazi vysledek.

## Technicky popis
Program obsahuje seznam otazek, moznosti odpovedi a spravnych reseni.
Cyklus for postupne prochazi vsechny otazky.
Podminka if kontroluje, jestli uzivatel odpovedel spravne.
Za kazdou spravnou odpoved se pricte jeden bod.
Na konci program vyhodnoti celkovy pocet bodu.

## Pouzite programovaci prvky
- Promenne
- Seznamy (list)
- Vnorene seznamy
- Cyklus for
- Podminky if, elif a else
- Funkce len() a upper()
- Input a print
- F-stringy
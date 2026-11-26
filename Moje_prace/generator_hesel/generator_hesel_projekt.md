# Projekt: Generátor hesel

## Cíl projektu
Vytvořit program, který dokáže generovat náhodná hesla podle délky zadané uživatelem.

## Funkce
- Zadání požadované délky hesla
- Generování náhodných znaků
- Použití malých a velkých písmen
- Použití čísel a speciálních znaků
- Kontrola, jestli je zadaná délka platná
- Výpis výsledného hesla

## Návod k použití
1. Spusťte soubor `generator_hesel.py`.
2. Zadejte požadovanou délku hesla.
3. Program vygeneruje náhodné heslo.
4. Výsledek se zobrazí v konzoli.

## Technický popis
Program využívá knihovny `random` a `string`.
Pomocí `string` získává dostupné znaky pro tvorbu hesla.
Cyklus `for` postupně vybírá náhodné znaky a přidává je do výsledného hesla.
Podmínka `if` kontroluje, jestli uživatel zadal platnou délku.

## Použité programovací prvky
- Proměnné
- Knihovny random a string
- Cyklus for
- Podmínky if a else
- Input a print
- F-stringy
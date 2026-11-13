cislo = 10
if cislo > 0:
    print("Hodnota čísla je kladná.")
elif cislo < 0:
    print("Hodnota čísla je záporná")
else:
    print("Hodnota čísla je nula.")


    vek = 20
    if vek >= 16 and vek <= 18:
        print("Jsi mladistivý.")
    else:
        print("Jsi dospělý.")

body = 85
chceme_ho = True

if body >= 80:
    if chceme_ho:
        print("Má dostatek bodů.")
        print("Je vhodný kandidát.")
    else:
        print("Má dost bodů.")
        print("ale nechceme ho.")
else:
    print("Nemá dostatek bodů. Smůla, ale nechceme ho.")


cislo = 5
if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")


nakupni_kosik = []

if nakupni_kosik:
    print("Kosik není prázdný.")
else:
    print("Kosik je prázdný.")


povolene_ovoce = ["jablko", "banán", "pomeranč"]
moje_ovoce = "hruška"

if moje_ovoce in povolene_ovoce:
    print(f"{moje_ovoce.capitalize()} je povolené ovoce.")
else:
    print(f"{moje_ovoce.capitalize()} není povolené ovoce.")
    
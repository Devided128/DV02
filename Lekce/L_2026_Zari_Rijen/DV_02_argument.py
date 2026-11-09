def scitani(a, b):
    return a + b

soucet = scitani(5, 7)
print("Součet je:", soucet)

soucet2 = scitani(b=10, a=3)
print("Součet je:", soucet2)

def deleni(a, b):
    if b == 0:
        return "Chyba: Dělení nulou není povoleno."
    else:
        return a / b
    print("Výsledek dělení je:", deleni(10, 2))

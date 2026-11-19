
import random

# Moznosti hry
moznosti = ["kamen", "nuzky", "papir"]

# Nahodny vyber pocitace
pocitac = random.choice(moznosti)

print("=== KAMEN NUZKY PAPIR ===")
print("Vyber: kamen, nuzky nebo papir")

# Vyber hrace
hrac = input("Tvuj vyber: ").lower()

# Kontrola vyberu
if hrac not in moznosti:
    print("Neplatny vyber!")

else:
    print(f"Pocitac vybral: {pocitac}")

    # Vyhodnoceni hry
    if hrac == pocitac:
        print("Remiza!")

    elif (hrac == "kamen" and pocitac == "nuzky") or \
         (hrac == "nuzky" and pocitac == "papir") or \
         (hrac == "papir" and pocitac == "kamen"):
        print("Vyhral jsi!")

    else:
        print("Vyhral pocitac!")

# Konec hry
print("Diky za hrani!")

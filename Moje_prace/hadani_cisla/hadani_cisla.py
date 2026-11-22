
import random

# Vygenerovani nahodneho cisla
tajne_cislo = random.randint(1, 50)

# Pocet pokusu uzivatele
pokusy = 0

print("=== HADANI CISLA ===")
print("Uhadni cislo od 1 do 50!")

# Hlavni cyklus hry
while True:
    tip = int(input("Zadej svuj tip: "))
    pokusy += 1

    # Kontrola zadaneho cisla
    if tip < tajne_cislo:
        print("Hledane cislo je vetsi!")

    elif tip > tajne_cislo:
        print("Hledane cislo je mensi!")

    else:
        print("Spravne! Uhodl jsi cislo!")
        print(f"Pocet pokusu: {pokusy}")
        break

print("Konec hry!")

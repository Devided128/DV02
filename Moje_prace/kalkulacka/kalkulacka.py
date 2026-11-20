
# Jednoducha kalkulacka

print("=== KALKULACKA ===")
print("1 - Scitani")
print("2 - Odcitani")
print("3 - Nasobeni")
print("4 - Deleni")

# Vyber operace
operace = input("Vyber operaci (1-4): ")

# Zadani cisel
cislo1 = float(input("Zadej prvni cislo: "))
cislo2 = float(input("Zadej druhe cislo: "))

# Vypocet
if operace == "1":
    vysledek = cislo1 + cislo2

elif operace == "2":
    vysledek = cislo1 - cislo2

elif operace == "3":
    vysledek = cislo1 * cislo2

elif operace == "4":
    if cislo2 != 0:
        vysledek = cislo1 / cislo2
    else:
        vysledek = None
        print("Nulou nelze delit!")

else:
    vysledek = None
    print("Neplatna operace!")

# Vypis vysledku
if vysledek is not None:
    print(f"Vysledek je: {vysledek}")

# Konec programu
print("Konec kalkulacky!")

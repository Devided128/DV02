# Prevodnik jednotek

print("=== PREVODNIK JEDNOTEK ===")
print("1 - Kilometry na metry")
print("2 - Metry na kilometry")
print("3 - Centimetry na metry")

# Vyber prevodu
vyber = input("Vyber moznost (1-3): ")

# Zadani hodnoty
hodnota = float(input("Zadej hodnotu: "))

# Provedeni prevodu
if vyber == "1":
    vysledek = hodnota * 1000
    print(f"{hodnota} km = {vysledek} m")

elif vyber == "2":
    vysledek = hodnota / 1000
    print(f"{hodnota} m = {vysledek} km")

elif vyber == "3":
    vysledek = hodnota / 100
    print(f"{hodnota} cm = {vysledek} m")

else:
    print("Neplatna moznost!")

# Konec programu
print("Prevod byl dokoncen!")

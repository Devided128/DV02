
import random
import string

# Znaky, ze kterych se bude heslo vytvaret
znaky = string.ascii_letters + string.digits + "!@#$%&*"

print("=== GENERATOR HESEL ===")

# Uzivatel si zvoli delku hesla
delka = int(input("Zadej delku hesla: "))

# Kontrola zadane delky
if delka < 1:
    print("Delka hesla musi byt alespon 1!")

else:
    heslo = ""

    # Postupne vybirame nahodne znaky
    for i in range(delka):
        znak = random.choice(znaky)
        heslo += znak

    # Vypis vygenerovaneho hesla
    print(f"\nTvoje nove heslo je: {heslo}")

print("Konec programu!")

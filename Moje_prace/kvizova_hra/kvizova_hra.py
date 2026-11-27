
# Kvizova hra

# Seznam otazek, moznosti a spravnych odpovedi
otazky = [
    ["Kolik planet je ve Slunecni soustave?", ["A) 7", "B) 8", "C) 9"], "B"],
    ["Jaky je hlavni jazyk v Brazilii?", ["A) Spanelsky", "B) Anglicky", "C) Portugalsky"], "C"],
    ["Kolik stran ma sestiuhelnik?", ["A) 5", "B) 6", "C) 8"], "B"],
    ["Ktery programovaci jazyk pouzivame v tomto projektu?", ["A) Python", "B) Java", "C) C++"], "A"],
    ["Jaka je hlavni hvezda nasi soustavy?", ["A) Mesic", "B) Slunce", "C) Zeme"], "B"]
]

# Promenna pro pocitani bodu
body = 0

print("=== KVIZOVA HRA ===")
print("Odpovidej pomoci pismen A, B nebo C.\n")

# Postupne zobrazime vsechny otazky
for i in range(len(otazky)):
    print(f"\nOtazka {i + 1}: {otazky[i][0]}")

    # Vypis moznosti odpovedi
    for moznost in otazky[i][1]:
        print(moznost)

    # Ziskani odpovedi od uzivatele
    odpoved = input("Tvoje odpoved: ").upper()

    # Kontrola spravne odpovedi
    if odpoved == otazky[i][2]:
        print("Spravne!")
        body += 1
    else:
        print(f"Spatne! Spravna odpoved byla {otazky[i][2]}.")

# Zaverecne vyhodnoceni
print("\n=== VYSLEDEK KVIZU ===")
print(f"Ziskal jsi {body} z {len(otazky)} bodu.")

if body == len(otazky):
    print("Vyborne! Mas vsechny odpovedi spravne!")
elif body >= 3:
    print("Dobry vysledek!")
else:
    print("Zkus to znovu!")

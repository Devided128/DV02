
# Automat na kavu

print("=== AUTOMAT NA KAVU ===")
print("1 - Espresso")
print("2 - Cappuccino")
print("3 - Latte")

# Tady si uzivatel vybere kavu
vyber = input("Vyber si kavu: ")

# Tu to kontroluje ten vyber 
if vyber == "1":
    print("Pripravujeme Espresso...")
    print("Tvoje Espresso je hotove!")

elif vyber == "2":
    print("Pripravujeme Cappuccino...")
    print("Tvoje Cappuccino je hotove!")

elif vyber == "3":
    print("Pripravujeme Latte...")
    print("Tvoje Latte je hotove!")

else:
    print("Neplatny vyber!")

# zaver programu
print("Dekujeme za navstevu!")

# Slovník

kontakty = {
    "jmeno": "Jan Novák",
    "prijmeni": "Novák",
    "vek": 67,
    "mesto": "Praha",
    "mail": "jan.novak@email.com",
    "telefon": "123456789",
}
# vytiskne celou datovou strukturu
print(f"Původní kontakty: {kontakty}")

print(f"Jméno: {kontakty['jmeno']}")





# Jak zmenit jednu polozku
kontakty["vek"] = 67
print (kontakty)
print(kontakty["vek"])





kontakty["mesto"] = "Ostrava"
print(kontakty)



telefon = kontakty.get("telefon")
print("Telefonní číslo:", telefon)
print(f"Telefonní číslo: {telefon}")

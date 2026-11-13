python_devs =  {"Pepa", "Jirka", "Honza", "Marek", "Karel", "Romana", "Petr"}
java_devs = {"Romana", "Petr", "Karel", "Mařka", "Lucie",}

# Operace sjednocení (NEBO)
vsichnni_devs = python_devs | java_devs
print("Všichni vývojáři (sjednocení):", vsichnni_devs)

# Operace průniku (A)
polyglot_devs = python_devs & java_devs
print("Vývojáři, kteří ovládají oba jazyky (Průnik):", polyglot_devs)

# Operace rozdíl (-)
vsichnni_devs = python_devs - java_devs
print("Všichn i vývojáři (rozdíl):", vsichnni_devs)
print (20*"=")
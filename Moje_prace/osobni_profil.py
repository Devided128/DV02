# uzivatel zada svoje udaje
jmeno = input("Jak se jmenujes? ")
vek = input("Kolik ti je let? ")
oblibena_hra = input("Jaka je tvoje oblibena hra? ")

# vypis profilu uzivatele
print("\n--- TVUJ PROFIL ---")
print(f"Ahoj, jmenujes se {jmeno}.")
print(f"Je ti {vek} let.")
print(f"Tvoje oblibena hra je {oblibena_hra}.")

# vypocet veku za jeden rok
print(f"Za rok ti bude {int(vek) + 1} let.")
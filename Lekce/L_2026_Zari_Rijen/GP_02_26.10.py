import os

script_dir = os.path.dirname(os.path.abspath(__file__))
soubor_cesta = os.path.join(script_dir, "GP_02_DATA_26.10.txt")
print(f"Otevírám soubor v adresáři: {soubor_cesta}")

try:
    with open(soubor_cesta, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print(f"Soubor {soubor_cesta} nebyl nalezen.")
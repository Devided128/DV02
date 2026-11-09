import math
# proměnenné a řetězce

jmeno = "Petr"
vek = 25
print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.")

numbers = [8, 7, 3, 4, 5]


numbers.append(6)
numbers.sort()
print(f"seřazený seznam: {numbers}")
print(f"První prvek sezamu: {numbers[0]}")
print(f"poslední prvek sezamu: {numbers[-1]}")
#Slovníky a množiny

student = {
    "jmeno": "Lojza",
    "vek": 20,
    "predmety": ["Matematika", "Fyzika", "Informatika"]
}

student ["vek"] = 25
student ["jmeno"] = "Petr"
student ["predmenty"] = ["Matematika", "Fyzika", "Informatika"]
print ("Student: ", student)

data = [3,3,3,4,5,6,7,8,9,9,9,10]
unique_data = set(data)
print(f"Unikátní hodnoty: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

print(f"Obvod obdelníku s délkou 5 a šířkou 3 je: {vypocet_obvodu_obdelniku(5, 3)}")

# odmocnina

odmocnina = math.sqrt(256)
print(f"Odmocnina z 256 je: {odmocnina}")

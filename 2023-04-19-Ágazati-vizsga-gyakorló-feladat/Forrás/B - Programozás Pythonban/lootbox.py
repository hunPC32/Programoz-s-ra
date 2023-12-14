import random

n = int(input("Pozitív szám: "))
szamok = []
legend = []
rare = []
osszeg = 0

for i in range(n):
    azonosito = random.randint(1, 40)
    print(azonosito)
    szamok.append(azonosito)
    if azonosito % 5 == 0:
        legend.append(f"{i}:{azonosito}")
    elif azonosito % 2 == 1 and azonosito % 5 != 0:
        rare.append(azonosito)

for szam in szamok:
    osszeg += szam
    atlag = osszeg / len(szamok)

print("Összeg:",osszeg)
print("Legendások:",legend)
print("Ritkák:",rare)
print("Összeg:",osszeg)
print("Átlag:",atlag)
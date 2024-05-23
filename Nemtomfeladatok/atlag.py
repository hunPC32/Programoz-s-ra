hossz = int(input("Hossz: "))
szamok = []
i = 0

for szam in range(hossz):
    szam = int(input("Szam: "))
    szamok.append(szam)
    i += szam

print(round(i/len(szamok), 2))
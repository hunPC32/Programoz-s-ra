szamok = []
hossz = int(input("Hossz: "))

for szam in range(hossz):
    szam = int(input("Szam: "))
    szamok.append(szam)

print(max(szamok))
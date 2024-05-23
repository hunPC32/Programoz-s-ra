szamok = []
hossz = int(input("Hossz: "))

for szam in range(hossz):
    szam = int(input("Szam: "))
    szamok.append(szam)

print(min(szamok))

#minimum = szamok[0]
#if szam <= minimum:
#    minimum = szam
#
#print(minimum)
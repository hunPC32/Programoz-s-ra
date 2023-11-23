import random

pszam = int(input("Mennyi dobás legyen: "))
szamok = []
sz = []

for i in range(pszam):
    n = random.randint(1, 20)

    print(n)

if n % 10 == 0:
    sz.append(n)
    print(sz)

    
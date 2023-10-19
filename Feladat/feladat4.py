import random

szamok = []
nemneg = []

for i in range(5):
    list = []
    for i in range(3):
        x = random.randint(-5,5)
        list.append(x)
    szamok.append(list)

print(szamok)

for list in szamok:
    for szam in list:
        if szam >= 0:
            nemneg.append(szam)
           
           
print(nemneg)

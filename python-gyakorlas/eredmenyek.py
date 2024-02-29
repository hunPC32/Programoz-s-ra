import random

szam = int(input("Mennyi eredmény legyen generálva: "))

szamokk = []

for i in range(szam):
    szamok = random.randint(0, 100)
    print(szamok)
    szamokk.append(szamok)

szaz = 0

for i in szamokk:
    szaz += i

print(f"A százalékok átlaga: {szaz/len(szamokk)}")

hatvan = []

for i in szamokk:
    if i > 60:
        hatvan.append(i)
        
print("60% feletti százalékértékek:", *hatvan, sep=" ")
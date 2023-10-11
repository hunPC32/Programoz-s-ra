t = [1,4,2,-7,9,1]
osszeg = 0

for szam in t:
    osszeg = osszeg+szam
print(osszeg)


t = [1,4,2,-7,9,1]
db = 0

for szam in t:
    if szam < 5:
        db += 1
print(db)


t = [1,4,2,-7,9,1]
a = 3
benneVan = False

for szam in t:
    if szam == a:
        benneVan = True
        break

if benneVan:
    print("Benne van")
else:
    print("Ninca benne")


t = [3,4,1,-7,9,1]
min = t[0]

for szam in t:
    if szam < min:
        min = szam
    print(min)


t = [1,4,2,-7,9,1]
max = t[0]

for szam in t:
    if szam > max:
        max = szam
    print(max)


t = [1,4,2,-7,9,1]
paros = []
paratlan = []

for szam in t:
    if szam % 2 == 0:
        paros.append(szam)
    else:
        paratlan.append(szam)

print(paros)
print(paratlan)


t = [1,4,2,-7,9,1]
keresett = 1
eredmeny = []

for szam in range(len(t)):
    if t[szam] == keresett:
        eredmeny.append(szam)

    if len(eredmeny) == 0:
        print("Nincs ilyen elem")
    else:
        print(eredmeny)
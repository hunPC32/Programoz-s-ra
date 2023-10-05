#MEgszámlálás tétele

t = [1,4,2,7,9,1]

db = 0

for szam in t:
    if szam < 5:
        db += 1

print(db)


#Eldöntés
#Egy adat benne van-e egy listában

t = [1,4,2,7,9,1]
a = 3
benneVan = False

for szam in t:
    if szam == a:
        benneVan = True
        print("Benne van")
        break

if benneVan:
    print("Benne van")
else:
    print("Nincs benne")


#Minimum kiválasztás

t = [1,4,2,-7,9,1]
min = t[0]

for szam in t:
    if szam < min:
        min == szam
    print("Legkisebb szám:", min)


#maximum

t = [1,4,2,-7,9,1]
max = t[0]

for szam in t:
    if szam > max:
        max == szam
    print("Legnagyobb szám:", max)


#Szétválogatás

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


#KEresés

t = [1,4,2,-7,9,1]
keresett = 1
eredmeny = []

for i in range(len(t)):
    if t[i] == keresett:
        eredmeny.append(i)

if len(eredmeny) == 0:
    print("nincs ilyen elem")
else:
    print(eredmeny)
f = open("diakok.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

# Adatok rendszerezése
diakok = []
for line in lines:
    line = line.strip()
    parts = line.split(";")

    diak = {
        "id" : int(parts[0]),
        "nev" : parts[1],
        "nem" : bool(int(parts[2])),
        "evfolyam" : int(parts[3]),
        "osztaly" : parts[4]
    }

    diakok.append(diak)

print(diakok)
#Hány diák van
print(f"A file {len(diakok)} diák adatait tartalmaza.")

#Hány 10F-es van

tizf = 0
for diak in diakok:
    if diak['evfolyam'] == 10 and diak['osztaly'] == "F":
        tizf +=1

print(f"{tizf} 10F osztályos diák van.")

#Lányok neve

lanyok = []
for diak in diakok:
    if diak['nem'] == False:
        lanyok.append(diak['nev'])

print(lanyok)

f2 = open("jegyek.txt", "r", encoding="utf-8")
linesJegyek = f2.readlines()
f2.close()

#Adatok rendszerezése

diakokJegyei = []
for line in linesJegyek:
    line = line.strip()
    parts = line.split(";")

    id = int(parts[0])
    jegyek = parts[1].split(",")
    jegyekInt = []

    for jegy in jegyek:
        jegyekInt.append(int(jegy))
    jegyek = jegyekInt

    print(jegyek)

    #adatok
    adatok = {
        "id" : id,
        "jegyek" : jegyek
    }
    diakokJegyei.append(adatok)

print(diakokJegyei)

#Diak nev - atlag

def atlag(lista):
    osszeg = 0
    db = len(lista)

    for elem in lista:
        osszeg += elem

    atlag = osszeg/db
    return atlag

for diak in diakok:
    for adat in diakokJegyei:
        if adat['id'] == diak['id']:
            print(diak['nev'], atlag(adat['jegyek']))
            break



#DIak neve bekerese es irjuk ki a jegyeit

diakNeve = input("Név: ")

diakID = None

for diak in diakok:
    if diak['nev'] == diakNeve:
        diakID = diak['id']

if diakID == None:
    print("Nincs ilyen diák")
else:
    for adat in diakokJegyei:
        if adat['id'] == diakID:
            print(adat['jegyek'])
            break

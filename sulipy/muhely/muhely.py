'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

#print(autok)

javitott = []

for auto in autok:
    if auto['javitva'] == True:
        print(auto['rendszam'])

ossz = 0
for auto in autok:
    ossz += auto['koltseg']

print(f"Átlag javítási költség {round(ossz/len(autok))}")


rendszam = input("Rendszám: ")
keresett = None

for auto in autok:
    if auto['rendszam'] == rendszam:
        keresett = auto

if keresett != None:
    print("Bent van az autó ", keresett)
else:
    print("Nincs bent.")




betu = input("Betű: ").upper()

for auto in autok:
    m = auto['marka'].upper()
    t = auto['marka'].upper()
    if betu in m or betu in t:
        

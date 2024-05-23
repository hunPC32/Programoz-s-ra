f = open("eredmeny.txt", "r", encoding="utf-8")
f.readline()
lines = f.readlines()

adatok = []

for line in lines:
    parts = line.strip().split(";")
    diak = {
        "diak_id": parts[0],
        "feladat_szam": parts[1],
        "elert_pont": parts[2],
        "osszes_pont": parts[3]
    }
    adatok.append(diak)
    print(diak)

#1.feladat
pont = 0
for diak in adatok:
    pont = int(diak["osszes_pont"])

print(pont*10)

#2.feladat

idiota = 0

for diak in adatok:
    if diak["diak_id"] == "8":
        idiota = int(diak["elert_pont"]) / pont * 100

print(idiota)

#3. feladat

f = open("diakok.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

nevek = []

for line in lines:
    resz = line.strip().split(";")
    nev = {
        "id_diak": resz[0],
        "diak_neve": resz[1]
    }
    nevek.append(nev)

nevv = input("ADj meg egy nevet: ")
van = False
for nev in nevek:
    if nevv == nev["diak_neve"]:
        print(nev["id_diak"])
        van = True
if van != True:
    print("Nincs")


#4. feladat
    
bekert_nev = input("Adj meg nevet: ")
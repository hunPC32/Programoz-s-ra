f = open("steam.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

mennyiseg = []
simulator = []
evek = []


for line in lines:
    line = line.strip()
    parts = line.split(";")

    jatekok = {
        "nev": parts[0],
        "ev": parts[1],
        "ar": parts[2],
        "vmi2": parts[3]
    }

    mennyiseg.append(parts[0])

    if "simulator".upper() in jatekok["nev"].upper():
        simulator.append(jatekok["nev"])

    szam1 = int(input("Szam1: "))
    szam2 = int(input("Szam2: "))

    if szam1 > szam2:
        print("Hibás bevitel")
    else:
        for jatek in jatekok:
            ingyenes = []
            if jatekok['ar'] == 0 and jatekok['ev'] > szam1 and jatekok['ev'] < szam2 :
                ingyenes.append(jatek)
            print(ingyenes)



print("Játékok száma: ", len(mennyiseg))
print(simulator)

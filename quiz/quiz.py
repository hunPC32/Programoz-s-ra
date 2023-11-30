f = open("kveszcsönsz.txt", "r", encoding="utf-8")

kerdes_adatok = []

while True:
    kerdes = f.readline()

    if kerdes == "":
        break

    darabok = kerdes.split(";")
    kerdes_szoveg = darabok[0]
    valaszok_szama = int(darabok[1])

    valaszok = []

    for i in range(valaszok_szama):
        valasz = f.readline()
        valasz_darabok = valasz.split(";")
        valasz_szoveg = valasz_darabok[0]
        helyesseg = valasz_darabok[1]

        helyesseg = bool(int(helyesseg))

        valaszok.append(
            {
                "valasz": valasz_szoveg,
                "helyesseg": helyesseg
            }
        )
    
    kerdes_adatok.append({
        "kerdes": kerdes_szoveg,
        "valaszok": valaszok
    })

pontok = 0

for kerdes in kerdes_adatok:
    print(kerdes["kerdes"])

    val = kerdes["valaszok"]

    for i in range(len(val)):
        print(f"{i}.){val[i]['valasz']}")

    num = int(input("Válasz: "))

    if val[num]['helyesseg']:
        print("\n" + "Helyes")
        pontok += 1
        print(f"Pontok: {int(pontok)} \n")
    else:
        print("\n" + "Hibás")
        print(f"Pontok: {int(pontok)} \n")

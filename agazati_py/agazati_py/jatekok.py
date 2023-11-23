f = open("steam.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

mennyiseg = []
simulator = []

for line in lines:
    line = line.strip()
    parts = line.split(";")

    jatekok = {
        "nev": parts[0],
        "ev": parts[1],
        "vmi1": parts[2],
        "vmi2": parts[3]
    }

    mennyiseg.append(parts[0])

    if "simulator".upper() in jatekok["nev"].upper():
        simulator.append(jatekok["nev"])


print("Játékok száma: ", len(mennyiseg))
print(simulator)

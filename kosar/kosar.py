class Kosar:
    def __init__(self, line):

        self.hazai = parts[0]
        self.idegen = parts[1]
        self.hazai_pontok = int(parts[2])
        self.idegen_pontok = int(parts[3])
        self.helyszin = parts[4]
        self.idopont = int(parts[5])


f = open("eredmenyek.csv", "r", encoding="utf-8")
f.readline()
lines = f.readlines()
f.close()

valamik = []

for line in lines:
    parts = line.strip().split(";")

    valamik.append(Kosar)

idegen = 0
hazai = 0

for kosar in valamik:
    if kosar.hazai == "Real madrid":
        hazai += 1

print(hazai)
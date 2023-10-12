filename = "sulipy.txt"

f = open(filename, "r", encoding="utf-8")
lines = f.readlines()
f.close()

adatok = []

sorszam = 1
for line in lines:
    if sorszam > 1:
        csupaszsor = line.strip()
        adatok.append(csupaszsor.split(";"))
    sorszam += 1

for i in range(len(adatok)):
        print(adatok[i][1], adatok[i][2], adatok[i][2])


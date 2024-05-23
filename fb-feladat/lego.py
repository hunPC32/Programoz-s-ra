f = open("input.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

adatok = []

for line in lines:
    part = line.strip().split(";")
    if len(part) == 4:
        lego = {
            "code": part[0],
            "name": part[1],
            "theme": part[2],
            "bricks": int(part[3])
        }
        adatok.append(lego)
print(adatok)

sorrend = []

f1 = open("output.csv", "w", encoding="utf-8")

for lego in adatok:
    print("Kész a feladat")
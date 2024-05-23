f = open("fifa.txt", "r", encoding="utf-8")
f.readline()
lines = f.readlines()
f.close()

adatok = []

for line in lines:
    parts = line.strip().split(";")
    fifa = {
        "csapat": parts[0],
        "helyezes": parts[1],
        "valtozas": int(parts[2]),
        "pontszam": int(parts[3])
    }
    adatok.append(fifa)
print(f"A forrásállományban {len(lines)} csapat szerepel!")

atlagpont = 0

for fifa in adatok:
    atlagpont += fifa["pontszam"]

max = 0
legjobb = ""

for fifa in adatok:
    if fifa["valtozas"] > max:
        max = fifa["valtozas"]
    if fifa["valtozas"] == max:
        legjobb = [fifa["csapat"], fifa["helyezes"], fifa["pontszam"]]
        

print(legjobb[0])
print(legjobb[1])
print(legjobb[2])

magyar = False

for fifa in adatok:
    if fifa["csapat"] == "Magyarország":
        magyar = True

if magyar == True:
    print("Van magyar")
else:
    print("Nincs magyar")


nulla = 0
minusz = 0
egy = 0

for fifa in adatok:
    if fifa["valtozas"] == 0:
        nulla += 1
    elif fifa["valtozas"] == -1:
        minusz += 1
    elif fifa["valtozas"] == 1:
        egy += 1

print(nulla)
print(minusz)
print(egy)
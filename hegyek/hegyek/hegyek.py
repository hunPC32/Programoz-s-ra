f = open("hegyek.csv", "r", encoding="utf-8")
f.readline()
lines = f.readlines()
f.close()
adatok = []
for line in lines:
    parts = line.split(";")
    hegy = {
        "nev": parts[0],
        "hegyseg": parts[1],
        "magassag": int(parts[2])
    }
    adatok.append(hegy)
print(len(lines))

atlag = 0
for hegy in adatok:
    
    atlag += hegy["magassag"]

print(atlag / len(lines))


legnagyobb = 0
for hegy in adatok:
    if hegy["magassag"] > legnagyobb:
        legnagyobb = hegy["magassag"]

print(legnagyobb)

f = open("bukk-videk.txt", "w", encoding="utf-8")

for hegy in adatok:
    if hegy["hegyseg"] == "Bükk-vidék":
        f.write(hegy["nev"],";",hegy["magassag"]*3.280839895)
        legrosszabb = (int(hegy["magassag"] * 3.280839895)*100) / 100
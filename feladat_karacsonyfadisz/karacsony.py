f = open('diszek.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

adatok = []

for line in lines:
    line = line.strip()
    parts = line.split(";")
    adatok.append({
        "nap": int(parts[0]),
        "elkharang": int(parts[1]),
        "eladharang": int(parts[2]),
        "elkangyal": int(parts[3]),
        "eladangyal": int(parts[4]),
        "elkfenyo": int(parts[5]),
        "eladfenyo": int(parts[6])
    })
eladott = 0

for adat in adatok:
    eladott += adat["elkharang"] + adat["elkangyal"] + adat["elkfenyo"]


print(adatok)
print(eladott)

for adat in adatok:
    if adat["elkangyal"] or adat["elkharang"] or adat["elkfa"] == 0:
        print("Volt olyan nap")
        break
    else:
        print("Nem volt")

bekertszam = 0

while bekertszam <= 0 or bekertszam > 40:
    bekertszam = int(input("Szám: "))

h = 0
a = 0
f = 0

for nap in adatok:
    h += nap["elkharang"]
    a += nap["elkangyal"]
    f += nap["elkfenyo"]
    if nap["nap"] == bekertszam:
        break
print(f"A {bekertszam} napon megmaradt termékek: ")
print(f"Harang {h}")
print(f"Angyal {a}")
print(f"Fenyő {f}")

eh = 0
ea = 0
ef = 0

for nap in adatok:
    eh = nap["eladharang"] * -1
    ea = nap["eladangyal"] * -1
    ef = nap["eladfenyo"] * -1

print(eh)
print(ea)
print(ef)

legtöbb = max([eh, ea, ef])

if eh == legtöbb:
    print("Harang", eh)
if ea == legtöbb:
    print("Angyal", ea)
if ef == legtöbb:
    print("Fenyő", ef)
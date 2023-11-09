f = open('pizzak.txt', 'r', encoding="utf-8")
lines = f.readlines()
f.close()

for line in lines:
    pizzak = line.split(";")
    print(pizzak)

pizza = {
    'nev' : pizzak[0],
    'feltet' : pizzak[1],
    'ar' : int(pizzak[2])
}

penz = int(input("Pénz: "))

osz = 0

for p in pizzak:
    osz = penz/pizza['ar']
    if osz < 1:
        print("Nincs elég pénzed")
        break
    else:
        print(pizza['nev'], int(osz))
        break
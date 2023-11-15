import math

f = open('pizzak.txt', 'r', encoding="utf-8")
lines = f.readlines()
f.close()

pizzalista = []

for line in lines:
    pizzak = line.split(";")

    pizza = {
        'nev' : pizzak[0],
        "feltet" : pizzak[1],
        'ar' : int(pizzak[2])
    }
    pizzalista.append(pizza)
    print(pizza)

penz = int(input("Mennyi pénzed van? "))
osz = 0

for pizza in pizzalista:
    osz = math.floor(penz/pizza['ar'])
    if osz < 1:
        print("Csóró vagy hehe!!!44!!444!4!!!")
    else:
        print(pizza, osz)


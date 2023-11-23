import random

dobasok_szama = int(input("Dobasok: "))

print("A dobott számok: ")

crit = []

for i in range(dobasok_szama):
    rnd = random.randint(1,20)
    if rnd%10 == 0:
        crit.append({
            "index": i,
            "num": rnd
        })

    print(rnd)

print("Kritek: ")
for c in crit:
    print(c['index']+1, c['num'])

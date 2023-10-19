import random

tarolo = []

for i in range(4):
    list = []
    for i in range(3):
        x = random.randint(0,25)
        list.append(x)
    tarolo.append(list)

print(tarolo)
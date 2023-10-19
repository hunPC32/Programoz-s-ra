tarolo = []

for i in range (3):
    list=[]
    for i in range(3):
        x=str("O")
        list.append(x)
    tarolo.append(list)

for row in tarolo:
    row = str(row)
    row = row.replace(', ', " ").replace('[', '').replace(']', '').replace()
    print(row)


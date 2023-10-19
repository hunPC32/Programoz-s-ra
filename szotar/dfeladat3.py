szotar = []

macska = {
    "nev": "Kiscica",
    "kor": "4"
}

szotar.append(macska)

print(macska)

for num in range(2):
    kulcs = input("kulcs: ")
    macska[kulcs] = input("Új érték: ")
    print(macska)
    print(szotar)

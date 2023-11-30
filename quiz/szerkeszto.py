kerdes = input("Kérdés: ")
valaszok = []
while True:
    valasz = input("Válaszlehetőség: ")
    if valasz == "":
        break

    helyes = input("Igaz vagh Hamis: ")
    if helyes.upper() == "I":
        valaszok.append(f"{valasz};1")
    else:
        valaszok.append(f"{valasz};0")

print("="*20)
print(kerdes)
print(valaszok)
print("="*20)

f = open("kveszcsönsz.txt", "a", encoding="utf-8")
f.write(f"{kerdes};{len(valaszok)}\n")
for valasz in valaszok:
    f.write(valasz + "\n")

f.close()

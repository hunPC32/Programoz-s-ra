import random
kutya = []

for num in range(1):
    nev = input("Név:")
    kor = int(input("Kor:"))
    faj = input("Fajta:")
    veszett = input("Veszettség elleni oltás:")

    kutya.append({
        "nev": nev,
        "kor": kor,
        "faj": faj,
        "veszett": veszett
    })

print(kutya)
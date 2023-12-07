f = open("adatok.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

sz = []
adatok = []
szam = []

for line in lines:
    line.strip()
    parts = line.split(";")
    sz = [int(parts[11]), int(parts[12]), int(parts[13]), int(parts[14]), int(parts[15])]
    lotto_week = {
        "ev": parts[0],
        'het': parts[1],
        'datum': parts[2],
        '5_talalat': parts[3],
        '5_nyeremeny': parts[4],
        '4_talalat': parts[5],
        '4_nyeremeny': parts[6],
        '3_talalat': parts[7],
        '3_nyeremeny': parts[8],
        '2_talalat': parts[9],
        '2_nyeremeny': parts[10],
        'szamok': sz
    }
    adatok.append(lotto_week)

for i in range(5):
    szam.append(int(input("Szám: ")))


for szamok in adatok:
    if szamok['szamok'] == sorted(szam):
        print("Volt lottó ötösöd. Ebben az évben: ", szamok["ev"], ", Ezen a dátumon: ", szamok['datum'])


# példa dictionary:
# lotto_week = {
#     "ev" : 2023,
#     'het': 48,
#     'datum': '2023.12.02.',
#     '5_talalat': 0,
#     '5_nyeremeny': '0 Ft',
#     '4_talalat': 27,
#     '4_nyeremeny': '1 889 595 Ft',
#     '3_talalat': 2775,
#     '3_nyeremeny': '19 185 Ft',
#     '2_talalat': 75113,
#     '2_nyeremeny': '2 420 Ft',
#     'szamok': [3, 6, 30, 51, 68]
# }

# Kérj be 5 számot!
# A program írja ki, hogy ha megjátszod a számokat, akkor lett volna valaha ötösöd? Ha igen, akkor mikor?
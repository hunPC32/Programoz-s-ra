szam = input("2 szám: ")

parts = szam.split(" ")
szam1 = int(parts[0])
szam2 = int(parts[1])

while szam2 != 0:
    szam1, szam2 = szam2, szam1 % szam2

if szam1 == 1:
    print("IGEN")
else:
    print("NEM")
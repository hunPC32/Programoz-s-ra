import math

ár = int(input("Ár: "))
darab = int(input("Darab: "))
fizetendo = ár*darab+500

print("Jegy ára:", ár)
print("Darabszám:", darab)
print("Fizetendő összeg:", math.floor(int(fizetendo)))

if fizetendo<=10000:
    fizetendo = fizetendo - fizetendo * 0.10
else:
    fizetendo = fizetendo - fizetendo * 0.15

print("Kedvezményes ár:", math.floor(int(fizetendo)))
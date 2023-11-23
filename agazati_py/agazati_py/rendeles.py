szállítás = 2000

ar = int(input("Ár:"))
db = int(input("Darab:"))

fizetendo = ar * db + szállítás


if int(fizetendo) < 20000:
    fizet = int(fizetendo) - int(fizetendo)/20
else:
    fizet = int(fizetendo) - (fizetendo)/10

print("Termék egységára: ", ar)
print("Darabszám: ", db)
print("Fizetendő összeg: ", fizetendo)
print("Kedvezményes ár: ", fizet)
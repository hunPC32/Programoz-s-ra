ar = int(input("Írd be a vásárolt termékért fizetendő összeget: "))
szallitas = int(input("Írd be a szállítsi költséget: "))

print(f"Összesen fizetendő: {ar + szallitas} Ft")
if ar + szallitas >= 10000:
    print("A vásárló ajándékot kap.")
else:
    print("A vásárló nem kap plusz ajándékot.")
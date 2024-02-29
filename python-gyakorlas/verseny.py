pont = int(input("Írd be a pontszámot: "))

if pont >= 250:
    print(f"A versenyző továbbjutott, pontszáma {pont}, százalékos eredménye: {pont/4}%")
else:
    print("A versenyző nem jutott tovább.")
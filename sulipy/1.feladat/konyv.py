adatok = []

while True:
    szerzo = input("Szerző: ")
    if szerzo == "":
        break
    cim = input("Cím: ")
    if cim == "":
        break
    
    konyv = {
    "Szerző: " : szerzo,
    "Cím: " : cim,
}   
    adatok.append(konyv)  
print(adatok)
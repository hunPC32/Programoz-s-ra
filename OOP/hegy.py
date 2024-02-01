class Hegy:
    #def __init__(self, nev, hegyseg, magassag):
     #   self.nev = nev
      #  self.hegyseg = hegyseg
       # self.magassag = magassag
    
    def __init__(self, line):
        parts = line.split(";")

        self.nev = parts[0]
        self.hegyseg = parts[1]
        self.magassag = int(parts[2])

    def magassag_labban(self):
        return self.magassag * 3.280839895
        


f = open("hegyek.csv", "r", encoding="utf-8")
f.readline()
lines = f.readlines()
f.close()

hegyek = []

for line in lines:
    parts = line.strip().split(";")

    hegyek.append(Hegy(line.strip()))

print(len(hegyek))

sumMagassag = 0

for hegy in hegyek:
    sumMagassag += hegy.magassag

print(sumMagassag / len(hegyek))

for hegy in hegyek:
    if hegy.magassag_labban() > 3000:
        print(hegy.nev)
class Kutya():
    def __init__(self, nev, fajta = "buzi"):
        self.nev = nev
        self.fajta = fajta

    def ugat(self):
        print(f"Vau vau - {self.nev}")

class JuhaszKutya():
    def __init__(self, nev, fajta = "puli"):
        super().__init__(nev, fajta)
    
    def terel(self, haszonallat = "birka"):
        print(f"{self.nev} {haszonallat}-t/-ot terel.")

zoli = Kutya("Zoli")
zoli.ugat()

print(zoli.nev)
print(zoli.fajta)

Zsóti = Kutya("Zsóti", "🤓")

print(Zsóti.fajta)

rex = JuhaszKutya("Rex Felügyelő", "Német Juhász")

rex.terel()
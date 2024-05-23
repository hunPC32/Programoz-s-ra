class Negyzet:
    def __init__(self, oldalHossz):
        self.oldal=oldalHossz
    def kerulet(self):
        return 4*self.oldal
    def terulet(self):
        return self.oldal**2
    def kiirkerulet(self):
        print(self.kerulet())

elso = Negyzet(5)
print(elso.kerulet())
print(elso.terulet())
elso.kiirkerulet()
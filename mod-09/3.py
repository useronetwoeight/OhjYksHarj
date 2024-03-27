class Auto:
    def __init__(self, rekkari, nopeus, vauhti, matka):
        self.rekkari = rekkari; self.nopeus = nopeus; self.vauhti = vauhti; self.matka = matka

    def tulosta_ominaisuudet(self):
        print("Tiedot: \nRekisteritunnus:", self.rekkari, "\nHuippunopeus:", self.nopeus, "km/h \nTämänhetkinen nopeus:", self.vauhti, "km/h \nKuljettu matka:", self.matka, "km")

    def kiihdytys_methodi(self, x):
        self.vauhti += x
        print(f"Auto kiihdyttää {x} km/h verran.")
        if self.nopeus > self.vauhti:
            self.nopeus = self.vauhti
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika
        return

auto3 = Auto("ABC-123", 142, 0, 0)
auto3.nopeus = 143

print(auto3.nopeus)
auto3.nopeus = 10

x = int(30)
x = int(50)
x = int(70)

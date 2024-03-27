import random

class Auto:
    def __init__(self, rekkari, nopeus):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.vauhti = 0
        self.matka = 0

    def tulostus(self):
        print("Tiedot: \nRekisteritunnus:", self.rekkari,
              "\nHuippunopeus:", self.nopeus, "km/h "
              "\nTämänhetkinen nopeus:", self.vauhti, "km/h "
              "\nKuljettu matka:", self.matka, "km")

    def kiihdytys_methodi(self, x):
        self.vauhti += x
        print(f"Auto kiihdyttää {x} km/h verran.")
        if self.vauhti > self.nopeus:
            self.vauhti = self.nopeus
        if self.vauhti < 0:
            self.vauhti = 0

    def kulje(self, aika):
        self.matka += self.vauhti * aika


autoja = []

for i in range(1, 11):
    rekkari = "abc-" + str(i)
    maksimi = random.randint(100, 200)
    auto = Auto(rekkari, maksimi)
    autoja.append(auto)

aijka = 0
tavoita = 10000
continuw = True

while continuw:
    for auto in autoja:
        muutos = random.randint(-10, 15)
        auto.kiihdytys_methodi(muutos)
        auto.kulje(1)
        if auto.matka >= tavoita:
            continuw = False
            break
    aijka += 1

print(f"kilp ohi, se kesti {aijka} kierrosta")
print("rekkari\thuippu\tnopeus\tmatka")
for auto in autoja:
    print(auto.rekkari, "\t", auto.nopeus, "\t", auto.vauhti, "\t", auto.matka)

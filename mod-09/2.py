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

fresh_whip = Auto("ABC-123", 142, 0, 0)
auto = Auto("ABC-123", 142, 0, 0)
auto.nopeus = 143
auto2 = Auto("BCD-234", 111, 0, 0)
auto3 = Auto("dBCD-44234", 111, 0, 0)
auto4 = Auto("aBCD-44234", 111, 0, 0)

print(auto.nopeus)
print(auto2.nopeus)
auto2.nopeus = 10
print(auto2.nopeus)
print(auto3.nopeus)
print(auto4.nopeus)

x = int(30)
x = int(50)
x = int(70)

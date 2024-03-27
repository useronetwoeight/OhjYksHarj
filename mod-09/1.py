class Auto:
    def __init__(self, rekkari, nopeus, vauhti, matka):
        self.rekkari = rekkari; self.nopeus = nopeus; self.vauhti = vauhti; self.matka = matka

    def tulosta_ominaisuudet(self):
        print("Tiedot: \nRekisteritunnus:", self.rekkari, "\nHuippunopeus:", self.nopeus, "km/h \nTämänhetkinen nopeus:", self.vauhti, "km/h \nKuljettu matka:", self.matka, "km")


fresh_whip = Auto("ABC-123", 142, 0, 0)
fresh_whip.tulosta_ominaisuudet()

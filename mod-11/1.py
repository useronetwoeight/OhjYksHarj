class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumaara)


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
        print("Päätoimittaja:", self.paatoimittaja)


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
aku_ankka.tulosta_tiedot()

hyttino6 = Kirja("hytti n:o 6", "Rosa Liksom", "200")
hyttino6.tulosta_tiedot()


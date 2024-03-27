class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittarilukema = 0

    def aja(self, tuntimaara):
        self.matkamittarilukema += self.huippunopeus * tuntimaara


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def aja(self, tuntimaara):
        super().aja(tuntimaara)
        print("Sähköautolla ajetut kilometrit:", self.huippunopeus * tuntimaara)


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def aja(self, tuntimaara):
        super().aja(tuntimaara)
        print("Polttomoottoriautolla ajetut kilometrit:", self.huippunopeus * tuntimaara)


# Pääohjelma
def main():
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)

    print("Sähköauton matkamittarilukema:", sahkoauto.matkamittarilukema, "km")
    print("Polttomoottoriauton matkamittarilukema:", polttomoottoriauto.matkamittarilukema, "km")


if __name__ == "__main__":
    main()

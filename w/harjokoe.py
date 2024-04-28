class Tili():
    lkm = 0

    def __init__(self, omistaja, saldo):
        self.omistaja = omistaja
        self.saldo = saldo
        self.lkm += 1

    def maksa(self, summa):
        if self.saldo >= summa:
            self.saldo -= summa
            print("maksu ok")
        else:
            print("maksu ei ok")

    def tulostus(self):
        print("omistaja on ", self.omistaja)
        print("saldo on", self.saldo)


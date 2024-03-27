class Hissi:
    def __init__(self, alin, ylim):
        self.ihminen = alin
        self.alin = alin
        self.ylim = ylim

    def siirry_kerrokseen(self, kohde):
        while self.ihminen != kohde:
            if self.ihminen < kohde:
                self.ylos()
            elif self.ihminen > kohde:
                self.alas()

    def ylos(self):
        if self.ihminen < self.ylim:
            self.ihminen += 1
        print(f"Hissi on kerroksessa: {self.ihminen}")

    def alas(self):
        if self.ihminen > self.alin:
            self.ihminen -= 1
        print(f"Hissi on kerroksessa: {self.ihminen}")


class Talo:
    def __init__(self, alin, ylin, lkm):
        self.alin = alin
        self.ylin = ylin
        self.lkm = lkm
        self.hissit = []

        for i in range(lkm):
            uushissi = Hissi(self.alin, self.ylin)
            self.hissit.append(uushissi)

    def aja_hissia(self, mikahissi, mihin):
        ajettavahissi = self.hissit[mikahissi - 1]
        ajettavahissi.siirry_kerrokseen(mihin)

    def palohälytin(self):
        for lift in self.hissit:
            lift.siirry_kerrokseen(self.alin)


ekatalo = Talo(1, 50, 30)
reree = int(input("Millä hissillä?"))
syöte = int(input("mihin kerrokseen?"))
ekatalo.aja_hissia(reree, syöte)

ekahissi = ekatalo.hissit[0]
print(f"eka hisi {ekahissi}")
tokahissi = ekatalo.hissit[1]
print(f"toinen hisi {tokahissi}")
kolmashissi = ekatalo.hissit[2]
print(f"kolmas hisi {kolmashissi}")

print(f"palohälytys!!")
ekatalo.palohälytin()

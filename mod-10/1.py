class Hissi:
    def __init__(self, alin_kerros, ylim_kerros):
        self.ihminen = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylim_kerros = ylim_kerros

    def siirry_kerrokseen(self, kohde):
        while self.ihminen != kohde:
            if self.ihminen < kohde:
                self.ylos()
            elif self.ihminen > kohde:
                self.alas()
    def ylos(self):
        if self.ihminen < self.ylim_kerros:
            self.ihminen += 1
        print(f"Hissi on kerroksessa: {self.ihminen}")

    def alas(self):
        if self.ihminen > self.alin_kerros:
            self.ihminen -= 1
        print(f"Hissi on kerroksessa: {self.ihminen}")


hissi = Hissi(1, 10)
xx = int(input("xx"))
hissi.siirry_kerrokseen(xx)
yx = int(input("yx"))
hissi.siirry_kerrokseen(yx)

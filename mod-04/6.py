import random
# tehtävä 6
pallo = int(input("anna arvottavien pallojen määrä: "))
pallurat = 0
b = 0
while b < pallo:
    b += 1
    eka = random.uniform(-1,1)
    vika = random.uniform(-1,1)
    if eka ** 2 + vika ** 2 < 1:
        pallurat += 1
    piijuttu = 4 * pallurat / pallo
print("Pii arvo: ", piijuttu)

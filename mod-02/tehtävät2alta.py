import math
import random
'''
# 1. tehtävä
nimi = input("nimesi? ")
print("Terve, " + nimi + "!")

# 2. tehtävä
pii = math.pi
rStr = input("ympyrän säde? ")
r = int(rStr)
print(pii * r ** 2)

# 3. tehtävä
aStr = input("suorakulmion kanta? ")
a = int(aStr)
hStr = input("entä korkeus? ")
h = int(hStr)
piiri = (a + h) * 2
pintaala = a * h
print("Suorakulmion piiri = " + str(piiri) + " ja pinta-ala = " + str(pintaala))

# 4. tehtävä
nro1 = input("syötä ensimmäinen numero: ")
nro2 = input("syötä toinen numero: ")
nro3 = input("syötä kolmas numero: ")
nro1 = int(nro1)
nro2 = int(nro2)
nro3 = int(nro3)
summa = nro1 + nro2 + nro3
tulo = nro1 * nro2 * nro3
keskiarvo = (nro1 + nro2 + nro3) / 3
print("Antamiesi numeroiden summa = " + str(summa) + ". Sekä numeroiden tulo = " + str(tulo) + ". Sekä numeroiden keskiarvo = " + str(keskiarvo))
'''
# 5. tehtävä
lei = input("Anna leiviskät. \n")
nau = input("Anna naulat. \n")
luo = input("Anna luodit. \n")
lei = float(lei)
nau = float(nau)
luo = float(luo)
lei = int(lei)
nau = int(nau)
luo = int(luo)
leiv = lei * 85120
naul = nau * 4256
luod = luo * 133
luod = float(luod)
naul = float(naul)
leiv = float(leiv)
paino = leiv + naul + luod / 10
paino = int(paino)
kg = paino / 10000
kg = int(kg)
g = paino - kg * 10000
g = int(g)
print("Massa nykymittojen mukaan: \n" + str(kg) + " kilogrammaa ja "+str(f"{g/10:5.1f}") + " grammaa.")

# 6. tehtävä
a = random.randint(0, 9, )
b = random.randint(0, 9, )
c = random.randint(0, 9, )
aa = random.randint(1, 6, )
bb = random.randint(1, 6, )
cc = random.randint(1, 6, )
dd = random.randint(1, 6, )
print(f'{a}{b}{c}')
print(f'{aa}{bb}{cc}{dd}')

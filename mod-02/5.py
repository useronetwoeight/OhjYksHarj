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

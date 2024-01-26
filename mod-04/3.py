import math
# tehtävä 3
numrot = []
pienin = math.inf
suurin = math.inf
miguel = input("anna numeroita ja jos annat tyhjän mä lopetan \n")
while miguel != "":
    miguel = input("")
    if not miguel:
        print("ei ole bumero")
    try:
        luku = float(miguel)
        numrot.append(luku)
    except ValueError:
        print("ei tällästä, vaan numero tai tyhjä.")
    pienin = min(numrot)
    suurin = max(numrot)
print(pienin)
print(suurin)

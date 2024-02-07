gargamel = set()
while True:
    miguel = input("anna nimi, tyhjä lopettaa                                                                       \n")
    if not miguel:
        break
    if miguel in gargamel:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        gargamel.add(miguel)
print("Annoit nämä nimet:\n")
for tallennetut in gargamel:
    print(tallennetut)

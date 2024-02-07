lista = {}
while True:
    wiguel = int(input("Anna numero 1, jos haluat luoda uuden lentoaseman. "
                       "\nAnna numero 2, jos haluat hakea jo olemassa olevia tietoja. "
                       "\nAnna numero 3 jos haluat lopettaa.\n"))
    if wiguel == 1:
        print("Luodaan uusi lentoasema järjestelmään.")
        cacao = input("Lentoaseman ICAO-koodi:")
        mimi = input("Lentoaseman nimi:")
        lista[cacao] = mimi
        print(cacao + " " + mimi + " tallennettu")
    elif wiguel == 2:
        print("Haetaan olemassaolevan lentokentän tietoja. ")
        qwerty = input("Lentoaseman ICAO-koodi: ")
        if qwerty in lista:
            print (qwerty + " lentoaseman nimi: " + lista[qwerty])
        else:
            print("Ei löydy kyseistä lentoasemaa")
    elif wiguel == 3:
        print("/ᐠ - ˕ -マᶻ 𝗓 𐰁")
        break
    else:
        print("numero yhden ja kolmen väliltä, kiitos.")

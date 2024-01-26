# tehtävä 4
vuosi = int(input("Syötä vuosiluku: "))
if vuosi % 4 == 0:
    if vuosi % 100 != 0:
        print(str(vuosi) + " on karkausvuosi.")
    elif vuosi % 400 == 0:
        print(str(vuosi) + " on karkausvuosi.")
    else:
        print(str(vuosi) + " ei ole karkausvuosi.")
else:
    print(str(vuosi) + " ei ole karkausvuosi.")

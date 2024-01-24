
# tehtävä 1
kuha = input("sun kalasi pituus senttimetreinä?")
kuha = int(kuha)
kala = 37 - kuha
if kuha <= 37:
    print(f' kalas on liian pieni, itseasiassa, {kala} senttii liian pieni. Heitä se takasin järvee. ')
else:
    print("se on hyvän kokoinen")

# tehtävä 2
g = input("Hytti? : \n")
if g == 'LUX' or g == 'lux':
    print("LUX on parvekkeellinen hytti yläkannella.")
elif g == 'A' or g == 'a':
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif g == 'B' or g == 'b':
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif g == 'C' or g == 'c':
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

# tehtävä 3
a = input("F eli nainen vai M eli mies? \n")
if a == 'F' or a == 'f':
    fh = input("Mikä on hemoglobiini arvosi? \n")
    fh = int(fh)
    if fh <= 117:
        print("hemo alhainen")
    elif fh >= 175:
        print("hemo korkea")
    elif fh > 117 < 175:
        print("hemo normaali")
    else:
        print("koita uusiks")
elif a == 'M' or a == 'm':
    mh = input("Mikä on hemoglobiini arvosi? \n")
    mh = int(mh)
    if mh <= 134:
        print("hemo alhainen")
    elif mh >= 195:
        print("hemo korkea")
    elif mh > 134 < 195:
        print("hemo normaali")
    else:
        print("koita uusiks")
else:
    print("Virheellinen")

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


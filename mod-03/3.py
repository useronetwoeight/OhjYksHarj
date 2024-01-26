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

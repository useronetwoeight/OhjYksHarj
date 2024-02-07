def ooo():
    print("bruh")
    return

print("woo woo")
ooo()

def te(kerrat):
    for i in range(kerrat):
        print("Terve")
    return
te(6)

def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print ("Tervehditään lisää.")
tervehdi(2)

# tehtävä 5
ni = input("Käyttäjätunnus?\n")
sa = input("Salasana?\n")
oi = 'python'
ok = 'rules'
if not ni == oi:
    print()
    if not sa == ok:
        print("pääsy evätty")
else:
    print("Tervetuloa")

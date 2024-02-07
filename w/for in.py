
# kysytään käyttäjältä nimiä ja
# laitetaan ne listaan

# tyhjälista
nimet = []

# kysytään käyttäjältä eka nimi
name = input("anna eka nimi bro")

# while-toisto jatkuu kunnes saadaan
# tyhjä merkkijono
while name != "":
    # lisätään saatu nimi listan loppuun
    nimet.append(name)
    # HUOM muista kysyä uusi nimi
    name = input("seuraava nimi kiitoss")

# len funktio kertoo montako inputtia listassa on
print(f"annnoit {len(nimet)} nimeä")

print("annoit nimet: ")
print(nimet) # tulostaa koko listan

# lajitellaan nimet aakkosiin
nimet.sort()
print("nimet aakkosjärjestyksessä: ")
print(nimet)

nimet[1] = 'Toka'
print(nimet)

# printataan tiettyjä nimiä,
# - aloittaa toisesta päästä
# x:y ottaa x ja y ja välissä
# x: printtaa kaiken x jälkeen
# 0 1 2 3 4
nimm = ["wiwi", "amhed", "peka", "olga", "mari"]
print(nimm[3])
print(nimm[1])
print(nimm[-2])
print(nimm[1:3])
print(nimm[2:])




# tehtävä 1
kuha = input("sun kalasi pituus senttimetreinä?")
kuha = int(kuha)
kala = 37 - kuha
if kuha <= 37:
    print(f' kalas on liian pieni, itseasiassa, {kala} senttii liian pieni. Heitä se takasin järvee. ')
else:
    print("se on hyvän kokoinen")

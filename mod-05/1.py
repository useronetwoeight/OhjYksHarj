import random
nopat = int(input("Syötä noppien määrä: "))
ran = [random.randint(1, 6) for i in range(nopat)]
x = sum(ran)
print(x)

import random
def plus(M):
    Ra = [random.randint(1, 21) for _ in range(M)]
    totaali = sum(Ra)
    return Ra, totaali


L = int(input("Montako numeroa?\n"))
num, summ = plus(L)
print(f"numerot {num}")
print(f"yhteensä {summ}")

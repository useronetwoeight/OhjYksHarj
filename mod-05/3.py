num = int(input("Anna kokonaisluku: "))
if num >= 2:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Luku ei ole alkuluku."); break
    else:
        print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")

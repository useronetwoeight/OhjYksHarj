i = input("anna numero\n")
miguel = []
while i != "":
    miguel.append(i)
    i = input("anna numero\n")
miguel.sort(reverse=True)
print(miguel[0:5])

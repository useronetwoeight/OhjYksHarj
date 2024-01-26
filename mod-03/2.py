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

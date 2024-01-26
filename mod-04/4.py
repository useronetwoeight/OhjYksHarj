import random
# tehtävä 4
goblin = random.randint(1,10)
gublin = int(input("arvaa numero •̀⩊•́\n"))
while goblin != gublin:
    gublin = int(input("arvaa uuestaan ٩(ˊᗜˋ*)و\n"))
    if gublin == goblin:
        print("lucky")
    elif gublin > goblin:
        print("liian iso bro")
    elif gublin < goblin:
        print("liian pieni bro")

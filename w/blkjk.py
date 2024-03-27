import random
import time

raha = 1000
dirk = 0
life = 0
bums = ["bum"]
bum = random.choice(bums)

airport_comment = [
    "During your exploration, you come upon a passage where a small group of bums can be seen; "
    "you decide to check it out.",
    "While navigating around the airport, you discover a hallway with a handful of bums, "
    "leading you to investigate further.",
    "As you move about, a corridor with a few bums becomes evident, compelling you to make your way there.",
    "In your journey, you stumble upon a passage where a few bums are present, prompting you to explore.",
    "While exploring the surroundings, you find a hallway with a small group of bums, "
    "and you decide to head in that direction.",
    "As you wander, a corridor filled with bums in need of a gambling catches your attention, "
    "urging you to approach.",
    "During your journey, you encounter a passage where a small group of bums can be observed; "
    "you decide to investigate.",
    "While navigating, you chance upon a hallway with a handful of bums, motivating you to explore further.",
    "As you stroll, a corridor featuring a few bums becomes visible, compelling you to make your way there.",
    "In your exploration, you happen upon a passage where a few bums are present, prompting you to investigate.",
    "As you walk around, a corridor occupied by bums in need of gambling captures your attention, "
    "urging you to approach.",
    "During your journey, you discover a passage where a small group of bums can be seen; you decide to check it out.",
    "While navigating around the airport, you notice a hallway with a handful of bums, "
    "motivating you to explore further.",
    "As you move about, a corridor with a few bums becomes evident, compelling you to make your way there.",
    "In your exploration, you stumble upon a passage where a few bums are present, prompting you to explore.",
    "While exploring the surroundings, you find a hallway with a small group of bums, "
    "and you decide to head in that direction.",
    "As you wander, a corridor filled with bums in need of gambling catches your attention, "
    "urging you to approach.",
    "During your journey, you encounter a passage where a small group of bums can be observed; "
    "you decide to investigate."
]
print_airport_comment = random.choice(airport_comment)


def random_airport():
    airports = [
        "Helsinkivantaa", "Rio de Janeiro"
    ]
    return random.choice(airports)


def bum_encounter(bum_count):
    global raha
    global dirk
    global life

    time.sleep(3)
    dialog_bum_encounter1 = [
        f"You have stumbled upon a wild {bum}.",
        f"A feral figure appears in your path, a {bum}.",
        f"In your way stands an untamed wanderer, a {bum}.",
        f"A rogue character emerges before you, a {bum}.",
        f"You find yourself face to face in the home turf of the {bum}.",
        f"Your travels are halted, you notice an uncontrolled street dweller, a {bum}.",
        f"A rogue individual appears in your presence, a {bum}."
    ]
    print_bum_encounter1 = random.choice(dialog_bum_encounter1)
    print(print_bum_encounter1)

    time.sleep(2)
    dialog_bum_encounter2 = [
        "Will you engage in a game with the bum, procure a knife from them, or attempt to extract information?",
        "Are you inclined to partake in a game with the bum, buy a knife, or seek information?",
        "Will you entertain the possibility of a game with the bum, making a knife purchase, "
        "or extracting information?",
        "Are you open to participating in a game with the bum, securing a knife, or obtaining information?",
        "Would you consider joining a game with the bum, procuring a knife, or attempting to gather information?",
        "Are you up for engaging in a game with the bum, buying a knife, or seeking information?",
        "Will you consider playing a game with the bum, purchasing a knife, or extracting information?",
        "Do you desire to participate in a game with the bum, obtain a knife, or try to gather information?"
    ]
    print_bum_encounter2 = random.choice(dialog_bum_encounter2)
    print(print_bum_encounter2)

    time.sleep(2)
    dialog_bum_encounter3 = [
        "Choose your action: ",
        "Decide what to do: ",
        "Pick your action: ",
        "Choose your next step: ",
        "Decide your course of action: ",
        "Select an option: ",
        "Opt for your action: ",
        "Decide your move: "
        ]
    print_bum_encounter3 = random.choice(dialog_bum_encounter3)
    print(print_bum_encounter3)

    dialog_action1 = [
        "Engage in a game. ",
        "Engage in a gaming session. ",
        "Participate in a game. ",
        "Participate in a gaming session. ",
        "Take part in a game. ",
        "Take part in a gaming session. ",
        "Indulge in some gaming. "
    ]
    print_action1 = random.choice(dialog_action1)
    dialog_action2 = [
        "Proceed with a transaction. ",
        "Conduct a buying activity. ",
        "Make a deal. ",
        "Make a transaction. ",
        "Commit purchasing activities. ",
        "Commit a deal. ",
        "Indulge in some purchasing activities. ",
        "Indulge in some dealing. "
        "Initiate a buying process. ",
        "Initiate a purchase. ",
        "Initiate in some purchasing activities. ",
        "Initiate a buying activity. "
    ]
    print_action2 = random.choice(dialog_action2)
    dialog_action3 = [
        "Inquire for details on TheBauss. ",
        "Inquire for information. ",
        "Inquire for knowledge. ",
        "Seek information. ",
        "Seek insights. ",
        "Seek knowledge. ",
        "Ask for insights. ",
        "Ask for knowledge. ",
        "Ask for information. ",
        "Request information. ",
        "Gather intel. ",
        "Kindly request information. ",
        "Pose a query. ",
        "Solicit information. ",
        "Probe for details. ",
        "Request insights. ",
        "Inquire for knowledge. "
    ]
    print_action3 = random.choice(dialog_action3)
    dialog_action4 = [
        "Continue your journey. ",
        "Keep moving forward. ",
        "Proceed on your path. ",
        "Move along. ",
        "Walk on. ",
        "Keep walking. "
    ]
    print_action4 = random.choice(dialog_action4)
    action = input("\n1. " + print_action1 +
                   "\n2. " + print_action2 +
                   "\n3. " + print_action3 +
                   "\n4. " + print_action4 + "\n")

    if action == "1":
        play_game(bum_count)
    elif action == "2":
        purchase_knife(bum_count)
    elif action == "3":
        request_information(bum_count)
    elif action == "4":
        print("You continued on your way. ")
        bum_count -= 1
        return bum_count
    else:
        print("Invalid input, encounter will now end. Better luck next time.")
    bum_count -= 1
    return bum_count


def play_game(bum_count):
    print("mustajaakko ei löytyny")
    # laitetaan tähän mustajaakko
    bum_count -= 1
    return bum_count


def purchase_knife(bum_count):
    global raha
    global dirk
    global bum

    knife_buy = input(f"{bum}: So you wish to purchase a knife huh? \nInput yes / no\n")
    if knife_buy == 'yes':
        acquire_a_shank = input(f"{bum}: You can have it for 300. \nInput yes / no\n")
        if acquire_a_shank == 'yes':
            print("shank acquired")
            raha -= 300
            dirk = 1
            time.sleep(1)
            print(f"{bum}: A favorable deal")
            time.sleep(1)
            print("Bum takes off and disappears to the crowds. ")
            time.sleep(2)
            return bum_count
        elif acquire_a_shank == 'no':
            print(f"{bum}: Stop bothering me then??")
            time.sleep(1)
            print("Bum takes off and disappears to the crowds. ")
            time.sleep(2)
            bum_count -= 1
            return bum_count
        else:
            print("Invalid input, encounter will now end. Better luck next time.")
            bum_count -= 1
            return bum_count
    elif knife_buy == 'no':
        print(f"{bum}: Stop bothering me then??")
        bum_count -= 1
        return bum_count
    else:
        print("Invalid input, encounter will now end. Better luck next time.")
        bum_count -= 1
        return bum_count


def request_information(bum_count):
    global raha
    global dirk
    global life

    inforequest = [1, 2, 3, 4]
    inforequest_outcome = random.choice(inforequest)
    if inforequest_outcome == 1:
        print("The less fortunate individual extends an invitation, "
              "challenging you to engage in a refined fencing duel. ")
        time.sleep(3)
        if dirk == 1:
            print("You pull your knife out.")
            time.sleep(1)
            print("The bum notices the knife and decides to exit the fencing duel by running away.")
            time.sleep(2)
        else:
            print("The call to join was not voluntary and the bum charges towards you")
            time.sleep(2)
            time.sleep(1)
            bumcharge_outcome = random.randint(1, 3)
            if bumcharge_outcome == 1:
                print("With agile finesse, you skillfully evaded the oncoming advance of the bum, "
                      "escaping their charge, and gracefully exited the scene, "
                      "leaving the duel behind")
                time.sleep(4)
            else:
                dialog_death = [
                    "After an agile maneuver, the bum successfully struck, leaving me wounded and bleeding.",
                    "A quick and nimble move from the bum resulted in a successful hit, leaving you wounded.",
                    "Executing a swift and nimble move, the bum landed a successful strike, leaving you injured.",
                    "The bum executed a swift maneuver, landing a successful hit that left you wounded.",
                    "A nimble move from the bum resulted in a successful strike, leaving you injured and bleeding.",
                    "Executing a swift maneuver, the homeless bum landed a hit, leaving you wounded and bleeding.",
                    "A speedy move from the bum resulted in a successful strike, leaving you injured and bleeding.",
                    "A nimble maneuver from the homeless bum resulted in a successful hit, leaving you wounded.",
                    "With a quick move, the bum executed a hit, causing you to be injured and bleeding.",
                    "A rapid maneuver from the bum led to a successful strike, leaving you wounded and bleeding.",
                    "Following a swift move by the bum, a precise strike ensued, resulting in you being injured.",
                    "After a quick maneuver by the bum, they executed a hit, causing you to be wounded.",
                    "After a nimble maneuver by the bum, they executed a hit, leaving you wounded and bleeding.",
                    "Following a rapid maneuver by the bum, a successful hit ensued, resulting in you being wounded.",
                    "Executing a speedy move, the bum landed a hit, resulting in you being injured and bleeding.",
                    "In the wake of a swift move by the homeless bum, they struck, leaving you injured and bleeding.",
                    "In the aftermath of a rapid move by the homeless bum, they struck, causing you to be injured.",
                    "In the wake of a quick maneuver by the bum, they struck, causing you to be wounded and bleeding.",
                    "In the aftermath of a nimble maneuver by the homeless bum, they struck, leaving you wounded and.",
                    "In the wake of a nimble move by the homeless bum, they struck, causing you to be bleeding."
                ]
                print_death = random.choice(dialog_death)
                print(print_death)
                time.sleep(4)
                print("You Died. ")
                life = 1
    elif inforequest_outcome == 2:
        print(f"{bum}: I am no snitch. ")
        print(f"{bum} walks away. ")
        bum_count -= 1
        return bum_count
    else:
        info_buy = input(f"{bum}: I can sell you a clue for 100. \nInput yes / no\n")
        if info_buy == 'yes':
            raha -= 100
            print("clue")
        elif info_buy == 'no':
            print(f"{bum}: Stop bothering me then??")
            time.sleep(1)
            print(f"{bum} takes off and disappears to the crowds. ")
            bum_count -= 1
            return bum_count
        else:
            print("Invalid input, encounter will now end. Better luck next time. ")
            bum_count -= 1
            return bum_count


def beginning():
    print("Game ✧ Start")
    print("Your objective: \nFind TheBausses lair and them "
          "\nvia purchasing information from various bums you encounter on your travels."
          "\nBeat TheBauss because they are very bad for the climate. ")


def airport_visit():
    print(f"You start from {random_airport()} the airport."
          "\nThere are a lot of people here. ")
    time.sleep(1)
    print(print_airport_comment)

    bum_count = int(random.randint(3, 5))
    while bum_count > 0:
        bum_count = bum_encounter(bum_count)


def airport_arrive():
    print(f"You arrive to {random_airport()} the airport."
          "\nThere are a lot of people here. ")
    time.sleep(1)
    print(print_airport_comment)

    bum_count = int(random.randint(3, 5))
    while bum_count > 0:
        bum_count = bum_encounter(bum_count)


airport_visit()

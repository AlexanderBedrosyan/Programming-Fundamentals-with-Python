type = input()

type_list = type.strip().split("|")

COINS = 100
ENERGY = 100

for i in range(len(type_list)):
    new_list = type_list[i].strip().split("-")

    if new_list[0] == "order":
        if ENERGY >= 30:
            ENERGY -= 30
            COINS += int(new_list[1])
            print(f"You earned {int(new_list[1])} coins.")
        else:
            print(f"You had to rest!")
            ENERGY += 50
    elif new_list[0] == "rest":
        if (int(new_list[1]) + ENERGY) > 100:
            print(f"You gained {int(100 - ENERGY)} energy.")
            ENERGY = 100
        else:
            ENERGY += int(new_list[1])
            print(f"You gained {int(new_list[1])} energy.")
        print(f"Current energy: {int(ENERGY)}.")
    else:
        if int(new_list[1]) <= COINS:
            COINS -= float(new_list[1])
            print(f"You bought {new_list[0]}.")
        else:
            print(f"Closed! Cannot afford {new_list[0]}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {int(COINS)}")
    print(f"Energy: {int(ENERGY)}")

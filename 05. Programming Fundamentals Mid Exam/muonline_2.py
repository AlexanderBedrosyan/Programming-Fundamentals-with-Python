def potion(potion, current_health):
    current_health += potion

    if current_health > 100:
        used_potion = current_health - 100
        potion -= used_potion
        current_health = 100
    print(f"You healed for {potion} hp.")
    print(f"Current health: {current_health} hp.")
    return current_health


def chest(bitcoins, current_bitcoins):
    bitcoins += current_bitcoins
    print(f"You found {current_bitcoins} bitcoins.")
    return bitcoins


def monster(power, monster, current_health, room):
    current_health -= power
    if current_health > 0:
        print(f"You slayed {monster}.")
    else:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {room}")
        exit()
    return current_health


def final_result(health, bitcoins):
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")


HEALTH = 100
BITCOINS = 0
dungeon_rooms = input().split("|")
room_position = 0

for room in dungeon_rooms:
    room_position += 1
    option, points = room.split(" ")

    if option == "potion":
        HEALTH = potion(int(points), HEALTH)
    elif option == "chest":
        BITCOINS = chest(BITCOINS, int(points))
    else:
        HEALTH = monster(int(points), option, HEALTH, room_position)

final_result(HEALTH, BITCOINS)

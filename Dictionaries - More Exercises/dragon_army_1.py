def change_null(damage, health, armor):
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    return damage, health, armor


def modify_dragon_dict(dict, type, name, damage, health, armor):
    if type not in dict:
        dict[type] = {}

    dict[type][name] = [damage, health, armor]
    return dict


n = int(input())
dragon_dict = {}

for i in range(n):
    current_information = input().split(" ")
    type, name, damage, health, armor = current_information[0], current_information[1], current_information[2], \
                                        current_information[3], current_information[4]

    if "null" in current_information:
        damage, health, armor = change_null(damage, health, armor)

    dragon_dict = modify_dragon_dict(dragon_dict, type, name, damage, health, armor)


for ch in dragon_dict:
    damage = 0
    health = 0
    armor = 0
    count = 0
    type = ch
    for key, value in sorted(dragon_dict[ch].items()):
        damage += int(value[0])
        health += int(value[1])
        armor += int(value[2])
        count = len(dragon_dict[ch])
    print(f"{type}::({damage/count:.2f}/{health/count:.2f}/{armor/count:.2f})")

    for key, value in sorted(dragon_dict[ch].items()):
        print(f"-{key} -> damage: {int(value[0])}, health: {int(value[1])}, armor: {int(value[2])}")
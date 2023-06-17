def loot(current_list, item_list):
    for item in item_list:
        if item not in current_list:
            current_list.insert(0, item)
    return current_list


def drop(current_list, ind):
    if 0 <= ind < len(current_list):
        ch = current_list.pop(ind)
        current_list.append(ch)
    return current_list


def steal(current_list, counter):
    stolen_items = []
    while len(current_list) > 0:
        counter -= 1
        ch = current_list.pop(-1)
        stolen_items.append(ch)
        if counter == 0:
            break
    print(*stolen_items[::-1], sep=", ")
    return current_list


initial_loot = input().split("|")

command = input()

while command != "Yohoho!":
    current_command = command.split(" ")

    if current_command[0] == "Loot":
        rest_items = current_command[1::]
        initial_loot = loot(initial_loot, rest_items)
    elif current_command[0] == "Drop":
        needed_index = int(current_command[1])
        initial_loot = drop(initial_loot, needed_index)
    elif current_command[0] == "Steal":
        count = int(current_command[1])
        initial_loot = steal(initial_loot, count)

    command = input()

if initial_loot:
    print(f"Average treasure gain: {sum([len(ch) for ch in initial_loot]) / len(initial_loot):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

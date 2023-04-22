gifts = input()

gifts_list = gifts.strip().split()

while True:
    commands = input()

    if commands == "No Money":
        break

    commands_list = commands.strip().split()

    if commands_list[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == commands_list[1]:
                gifts_list[i] = "None"
    elif commands_list[0] == "Required":
        for index, digits in enumerate(gifts_list):
            if index == int(commands_list[2]):
                gifts_list[index] = commands_list[1]
    elif commands_list[0] == "JustInCase":
        for item in range(len(gifts_list) - 1, - 1, - 1):
            if gifts_list[item] != "None":
                gifts_list[item] = commands_list[1]
                break
            else:
                continue

new_list = []

for item in range(len(gifts_list)):
    if gifts_list[item] != "None":
        new_list.append(gifts_list[item])

print(*new_list, sep=" ")

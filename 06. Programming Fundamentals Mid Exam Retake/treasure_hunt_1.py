treasure = input().split("|")

steal_list = []

while True:
    command = input()

    if command == "Yohoho!":
        break

    commands = command.split()

    if commands[0] == "Loot":
        new_list = []
        for i in range(1, len(commands)):
            if commands[i] not in treasure:
                new_list.append(commands[i])
        for ch in new_list:
            treasure.insert(0, ch)
        new_list = []

    elif commands[0] == "Drop":
        current_string = ""
        if int(commands[1]) < len(treasure) - 1:
            current_string = treasure[int(commands[1])]
            del treasure[int(commands[1])]
            treasure.append(current_string)
        current_string = ""

    elif commands[0] == "Steal":
        if int(commands[1]) >= len(treasure):
            for chart in treasure:
                steal_list.append(chart)
            print(*steal_list, sep=", ")
            treasure = []
            continue
        else:
            for digit in range(len(treasure) - 1, (len(treasure) - 1 - int(commands[1])), - 1):
                steal_list.append(treasure[digit])
                del treasure[digit]

        new_list_steal = []
        for numbers in range(len(steal_list) - 1, - 1, -1):
            new_list_steal.append(steal_list[numbers])
        print(*new_list_steal, sep=", ")
        new_list_steal = []
        steal_list = []

if len(treasure) == 0:
    print("Failed treasure hunt.")
else:
    count = 0
    for check in range(len(treasure)):
        count += len(treasure[check])
    print(f"Average treasure gain: {count / len(treasure):.2f} pirate credits.")
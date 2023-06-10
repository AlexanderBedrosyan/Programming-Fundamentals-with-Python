items = input().split(", ")

condition = True

while condition:
    command = input()

    if command == "Craft!":
        condition = False

    command = command.split(" - ")

    if command[0] == "Collect":
        if command[1] not in items:
            items.append(command[1])

    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])

    elif command[0] == "Combine Items":
        current_list = command[1].split(":")
        for i in range(len(items) - 1, - 1, - 1):
            if current_list[0] == items[i]:
                items.insert(i + 1, current_list[1])

    elif command[0] == "Renew":
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])

print(*items, sep=", ")
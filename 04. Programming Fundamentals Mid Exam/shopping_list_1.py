shopping_list = input().split("!")

count = 0

while True:
    commands = input()

    if commands == "Go Shopping!":
        print(*shopping_list, sep=", ")
        break

    commands = commands.split()

    if commands[0] == "Urgent":
        if commands[1] not in shopping_list:
            shopping_list.insert(0, commands[1])

    elif commands[0] == "Unnecessary":
        if commands[1] in shopping_list:
            shopping_list.remove(commands[1])

    elif commands[0] == "Correct":
        if commands[2] not in shopping_list:
            for i in range(len(shopping_list)):
                if shopping_list[i] == commands[1]:
                    shopping_list[i] = commands[2]

    elif commands[0] == "Rearrange":
        for i in range(len(shopping_list)):
            if shopping_list[i] == commands[1]:
                del shopping_list[i]
                shopping_list.append(commands[1])
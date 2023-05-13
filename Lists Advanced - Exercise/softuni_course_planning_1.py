fundamental_list = input().split(", ")

while True:
    command = input()

    if command == "course start":
        break

    current_command = command.split(":")

    if current_command[0] == "Add":
        if current_command[1] not in fundamental_list:
            fundamental_list.append(current_command[1])
    elif current_command[0] == "Insert":
        if (current_command[1] not in fundamental_list) and (0 <= int(current_command[2]) <= (len(fundamental_list) - 1)):
            fundamental_list.insert(int(current_command[2]), current_command[1])
    elif current_command[0] == "Swap":
        if (current_command[1] in fundamental_list) and (current_command[2] in fundamental_list):
            index1 = 0
            index2 = 0

            for index, items in enumerate(fundamental_list):
                if items == current_command[1] :
                    index1 = index
                elif items == current_command[2]:
                    index2 = index

            fundamental_list[index1], fundamental_list[index2] = fundamental_list[index2], fundamental_list[index1]

            checking_word = f"{current_command[1]}-Exercise"
            checking_word2 = f"{current_command[2]}-Exercise"

            if checking_word in fundamental_list:
                new_index = fundamental_list.index(checking_word)
                for index, items in enumerate(fundamental_list):
                    if items == current_command[1]:
                        fundamental_list.insert(index + 1, fundamental_list.pop(new_index))
            if checking_word2 in fundamental_list:
                new_index = fundamental_list.index(checking_word2)
                for index, items in enumerate(fundamental_list):
                    if items == current_command[2]:
                        fundamental_list.insert(index + 1, fundamental_list.pop(new_index))

    elif current_command[0] == "Exercise":
        name = f"{current_command[1]}-Exercise"
        if (current_command[1] in fundamental_list) and (name not in fundamental_list):
            for index, items in enumerate(fundamental_list):
                if items == current_command[1]:
                    fundamental_list.insert(index + 1, name)
        elif current_command[1] not in fundamental_list:
            fundamental_list.append(current_command[1])
            fundamental_list.append(name)

    elif current_command[0] == "Remove":
        name = f"{current_command[1]}-Exercise"
        if name in fundamental_list:
            fundamental_list.remove(name)
        if current_command[1] in fundamental_list:
            fundamental_list.remove(current_command[1])

for index, items in enumerate(fundamental_list):
    print(f"{index + 1}.{items}")

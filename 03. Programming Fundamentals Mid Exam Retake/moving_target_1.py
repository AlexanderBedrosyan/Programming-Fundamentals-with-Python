targets = input()

targets_area = [int(ch) for ch in targets.strip().split()]

while True:
    command = input()

    if command == "End":
        break

    command_list = command.split()

    if command_list[0] == "Shoot":
        if (int(command_list[1]) <= (len(targets_area)) - 1) and (int(command_list[1]) >= 0):
            if int(command_list[2]) < targets_area[int(command_list[1])]:
                targets_area[int(command_list[1])] -= int(command_list[2])
            else:
                targets_area.remove(targets_area[int(command_list[1])])
    elif command_list[0] == "Add":
        if (int(command_list[1]) <= (len(targets_area)) - 1) and (int(command_list[1]) >= 0):
            targets_area.insert((int(command_list[1])), int(command_list[2]))
        else:
            print("Invalid placement!")
    elif command_list[0] == "Strike":
        if (int(command_list[1]) <= (len(targets_area)) - int(command_list[2])) and (int(command_list[1]) >= int(command_list[2])):
            targets_area.remove(targets_area[int(command_list[1])])
            for i in range(int(command_list[2])):
                targets_area.remove(targets_area[int(command_list[1]) - i])
                targets_area.remove(targets_area[int(command_list[1]) + i - 1])
        else:
            print("Strike missed!")


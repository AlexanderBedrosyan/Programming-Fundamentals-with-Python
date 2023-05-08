to_do_list = [0] * 10

while True:
    command = input()

    if command == "End":
        for i in range(len(to_do_list) - 1, - 1, - 1):
            if to_do_list[i] == 0:
                to_do_list.pop(i)
        print(to_do_list)
        break

    current_command = command.split("-")

    to_do_list[int(current_command[0]) - 1] = current_command[1]

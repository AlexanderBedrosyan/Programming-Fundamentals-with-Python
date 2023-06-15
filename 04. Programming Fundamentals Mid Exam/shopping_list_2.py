def urgent(current_list, item):
    if item not in current_list:
        current_list.insert(0, item)
    return current_list


def unnecessary(current_list, item):
    while item in current_list:
        current_list.remove(item)
    return current_list


def correct(current_list, old_name, new_name):
    while old_name in current_list:
        ind = current_list.index(old_name)
        current_list[ind] = new_name
    return current_list


def rearrange(current_list, item):
    count = 0
    while item in current_list:
        current_list.remove(item)
        count += 1
    if count > 0:
        for i in range(count):
            current_list.append(item)
    return current_list


groceries = [ch for ch in input().split("!")]

while True:
    command = input()

    if command == "Go Shopping!":
        print(*groceries, sep=", ")
        break

    command = command.split(" ")

    if command[0] == "Urgent":
        item = command[1]
        groceries = urgent(groceries, item)
    elif command[0] == "Unnecessary":
        item = command[1]
        groceries = unnecessary(groceries, item)
    elif command[0] == "Correct":
        old_name = command[1]
        new_name = command[2]
        groceries = correct(groceries, old_name, new_name)
    elif command[0] == "Rearrange":
        item = command[1]
        groceries = rearrange(groceries, item)

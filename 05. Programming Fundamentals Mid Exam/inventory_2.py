def collect(item, current_list):
    if item not in current_list:
        current_list.append(item)
    return current_list


def drop(current_list, item):
    while item in current_list:
        current_list.remove(item)
    return current_list


def combine_items(current_list, items):
    old_item, new_item = items.split(":")
    for i in range(len(current_list)):
        if current_list[i] == old_item:
            current_list.insert(i + 1, new_item)
    return current_list


def renew(current_list, item):
    counter = 0
    while item in current_list:
        current_list.remove(item)
        counter += 1
    if counter > 0:
        for i in range(counter):
            current_list.append(item)
    return current_list


def print_final_result(current_list):
    print(*current_list, sep=", ")


journal = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        break

    current_command, option = command.split(" - ")

    if current_command == "Collect":
        journal = collect(option, journal)
    elif current_command == "Drop":
        journal = drop(journal, option)
    elif current_command == "Combine Items":
        journal = combine_items(journal, option)
    elif current_command == "Renew":
        journal = renew(journal, option)

print_final_result(journal)

def required(gift, ind, gifts_list):
    if 0 <= ind < len(gifts_list):
        gifts_list[ind] = gift
    return gifts_list


def outofstock(gift, gifts_list):
    while gift in gifts_list:
        ind = gifts_list.index(gift)
        gifts_list[ind] = None
    return gifts_list


def justincase(gift, gifts_list):
    gifts_list[len(gifts_list) - 1] = gift
    return gifts_list


easter_gifts = input().split(" ")

while True:
    command = input()

    if command == "No Money":
        break

    command = command.split(" ")

    if len(command) == 3:
        easter_gifts = required(command[1], int(command[2]), easter_gifts)
    else:
        if command[0] == "OutOfStock":
            easter_gifts = outofstock(command[1], easter_gifts)
        elif command[0] == "JustInCase":
            easter_gifts = justincase(command[1], easter_gifts)

print(' '.join(ch for ch in easter_gifts if ch != None))

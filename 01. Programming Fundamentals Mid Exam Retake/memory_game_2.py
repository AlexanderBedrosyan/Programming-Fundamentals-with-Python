def index_checker(ind_1, ind_2, current_list):
    if current_list[ind_1] == current_list[ind_2]:
        print(f"Congrats! You have found matching elements - {current_list[ind_1]}!")
        if ind_1 > ind_2:
            del current_list[ind_1]
            del current_list[ind_2]
        else:
            del current_list[ind_2]
            del current_list[ind_1]
    else:
        print("Try again!")
    return current_list


def add_elements_in_the_list(moves, current_list):
    ind = int(len(current_list) / 2)
    for _ in range(2):
        current_list.insert(ind, f"-{moves}a")
    return current_list


number_list = [ch for ch in input().split(" ")]
moves = 0

while True:
    command = input()

    if command == "end":
        if len(number_list) == 0:
            print(f"You have won in {moves} turns!")
        break

    if len(number_list) == 0:
        print(f"You have won in {moves} turns!")
        break

    ind_1, ind_2 = command.split(" ")
    moves += 1

    if 0 <= int(ind_1) < len(number_list) and 0 <= int(ind_2) < len(number_list) and ind_1 != ind_2 and \
            int(ind_1) >= 0 and int(ind_2) >= 0:
        number_list = index_checker(int(ind_1), int(ind_2), number_list)
    else:
        print("Invalid input! Adding additional elements to the board")
        number_list = add_elements_in_the_list(moves, number_list)

if len(number_list) > 0:
    print("Sorry you lose :(")
    print(' '.join(number_list))

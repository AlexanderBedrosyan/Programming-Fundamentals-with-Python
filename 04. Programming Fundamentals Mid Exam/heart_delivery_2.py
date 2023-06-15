def cupid_jump(current_list, ind):
    if current_list[ind] != 0:
        current_list[ind] -= 2
        if current_list[ind] == 0:
            print(f"Place {ind} has Valentine's day.")
    else:
        print(f"Place {ind} already had Valentine's day.")
    return current_list


def final_result(current_list, position):
    print(f"Cupid's last position was {position}.")
    if sum(current_list) == 0:
        print("Mission was successful.")
    else:
        count = 0
        for ch in current_list:
            if ch != 0:
                count += 1
        print(f"Cupid has failed {count} places.")


houses = [int(ch) for ch in input().split("@")]
position = 0

while True:
    command = input()

    if command == "Love!":
        final_result(houses, position)
        break

    skip_command, new_position = command.split(" ")

    current_position = int(new_position) + position
    if current_position > len(houses) - 1:
        current_position = 0

    houses = cupid_jump(houses, current_position)
    position = current_position

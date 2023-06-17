def fire(ind, attach_damage, current_list):
    if 0 <= ind < len(current_list):
        current_list[ind] -= attach_damage
        if current_list[ind] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return current_list


def defend(str_ind, end_ind, dmg, current_list):
    if 0 <= str_ind < end_ind < len(current_list):
        for ship in range(str_ind, end_ind + 1):
            current_list[ship] -= dmg
            if current_list[ship] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return current_list


def repair(index, health, max_health, current_list):
    if 0 <= index < len(current_list):
        current_list[index] += health
        if current_list[index] > max_health:
            current_list[index] = max_health
    return current_list


def status():
    pass


pirate_ships = [int(ch) for ch in input().split(">")]
warship = [int(ch) for ch in input().split(">")]
max_health_capacity = int(input())

command = input()

while command != "Retire":
    current_command = command.split()

    if current_command[0] == "Fire":
        index, damage = int(current_command[1]), int(current_command[2])
        warship = fire(index, damage, warship)
    elif current_command[0] == "Defend":
        start_index, end_index, damage = int(current_command[1]), int(current_command[2]), int(current_command[3])
        pirate_ships = defend(start_index, end_index, damage, pirate_ships)
    elif current_command[0] == "Repair":
        index, health = int(current_command[1]), int(current_command[2])
        pirate_ships = repair(index, health, max_health_capacity, pirate_ships)
    elif current_command[0] == "Status":
        print(f"{len([ch for ch in pirate_ships if ch < (max_health_capacity * 0.20)])} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ships)}\nWarship status: {sum(warship)}")
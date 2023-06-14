def print_result(counter_of_won_battles, flag, energy):
    if flag:
        print(f"Won battles: {counter_of_won_battles}. Energy left: {energy}" )
    else:
        print(f"Not enough energy! Game ends with {counter_of_won_battles} won battles and {energy} energy")


def battles(current_energy):
    won_battles = 0
    winner_flag = False
    while True:
        command = input()

        if command == "End of battle":
            winner_flag = True
            print_result(won_battles, winner_flag, current_energy)
            break

        current_opponent = int(command)

        if current_energy >= current_opponent:
            current_energy -= current_opponent
            won_battles += 1
            if won_battles % 3 == 0:
                current_energy += won_battles
        else:
            print_result(won_battles, winner_flag, current_energy)
            break


ENERGY = int(input())
battles(ENERGY)

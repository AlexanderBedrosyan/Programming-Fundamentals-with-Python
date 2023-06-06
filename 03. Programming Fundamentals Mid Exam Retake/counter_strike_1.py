energy = int(input())

wins = 0

while energy >= 0:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break

    if int(command) <= energy:
        wins += 1
        energy -= int(command)
        if wins % 3 == 0:
            energy += wins
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
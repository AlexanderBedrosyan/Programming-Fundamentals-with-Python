pirate_ship = [int(ch) for ch in input().strip().split(">")]
warship = [int(chart) for chart in input().strip().split(">")]
maximum_health = int(input())

while True:
    command = input()

    if command == "Retire":
        break

    acts = command.split()

    if acts[0] == "Fire":
        if 0 <= int(acts[1]) <= (len(warship) - 1):
            warship[int(acts[1])] -= int(acts[2])
            if warship[int(acts[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif acts[0] == "Defend":
        if (0 <= int(acts[1]) <= int(acts[2])) and (int(acts[2]) <= len(pirate_ship) - 1):
            for i in range(int(acts[1]), int(acts[2]) + 1):
                pirate_ship[i] -= int(acts[3])
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif acts[0] == "Repair":
        if 0 <= int(acts[1]) <= (len(pirate_ship) - 1):
            pirate_ship[int(acts[1])] += int(acts[2])
            if pirate_ship[int(acts[1])] > maximum_health:
                pirate_ship[int(acts[1])] = maximum_health

    elif acts[0] == "Status":
        count = 0
        for i in range(0, len(pirate_ship)):
            if pirate_ship[i] < (maximum_health * 0.20):
                count += 1
        print(f"{count} sections need repair.")
        count = 0

print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
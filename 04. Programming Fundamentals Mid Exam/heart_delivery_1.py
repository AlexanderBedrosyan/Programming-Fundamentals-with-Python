neighborhood = input()

neighborhood_list = [int(ch) for ch in neighborhood.strip().split("@")]

count = 0

while True:
    command = input()

    if command == "Love!":
        break

    command = command.split()
    count += int(command[1])

    if count > (len(neighborhood_list) - 1):
        count = 0

    if neighborhood_list[count] > 2:
        neighborhood_list[count] -= 2
    elif neighborhood_list[count] == 2:
        neighborhood_list[count] -= 2
        print(f"Place {count} has Valentine's day.")
    elif neighborhood_list[count] == 0:
        print(f"Place {count} already had Valentine's day.")


print(f"Cupid's last position was {count}.")
if sum(neighborhood_list) == 0:
    print("Mission was successful.")
else:
    no_love_houses = 0
    for i in range(len(neighborhood_list)):
        if neighborhood_list[i] != 0:
            no_love_houses += 1
    print(f"Cupid has failed {no_love_houses} places.")
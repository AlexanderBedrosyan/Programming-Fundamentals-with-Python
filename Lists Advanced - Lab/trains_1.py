wagons_number = int(input())
wagons = []
for i in range(0, wagons_number):
    current_number = 0
    wagons.append(current_number)

while True:
    command = input()

    if command == "End":
        print(wagons)
        break

    new_command = command.split()

    if new_command[0] == "add":
        wagons[-1] += int(new_command[1])
    elif new_command[0] == "insert":
        index = int(new_command[1])
        wagons[index] += int(new_command[2])
    elif new_command[0] == "leave":
        index = int(new_command[1])
        wagons[index] -= int(new_command[2])
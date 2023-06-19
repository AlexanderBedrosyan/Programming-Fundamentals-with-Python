def add(wagons, passangers):
    wagons[-1] += passangers
    return wagons


def insert(wagons, index, passangers):
    if 0 <= index < len(wagons):
        wagons[index] += passangers
    return wagons


def leave(wagons, index, passangers):
    if 0 <= index < len(wagons):
        wagons[index] -= passangers
    return wagons


wagons = [0 for _ in range(int(input()))]

command = input()

while command != "End":
    current_command = command.split(" ")

    if current_command[0] == "add":
        people = int(current_command[1])
        wagons = add(wagons, people)
    elif current_command[0] == "insert":
        index, people = int(current_command[1]), int(current_command[2])
        wagons = insert(wagons, index, people)
    elif current_command[0] == "leave":
        index, people = int(current_command[1]), int(current_command[2])
        wagons = leave(wagons, index, people)

    command = input()

print(wagons)

def print_the_result(targets):
    print('|'.join(str(ch) for ch in targets))


def strike(current_target, index, radius):
    first_ind = index - radius
    second_ind = index
    third_ind = index + radius
    if 0 <= first_ind < second_ind < third_ind < len(current_target):
        for i in range(third_ind, first_ind - 1, - 1):
            del current_target[i]
    else:
        print("Strike missed!")
    return current_target


def add(current_target, index, value):
    if 0 <= index < len(current_target):
        current_target.insert(index, value)
    else:
        print("Invalid placement!")
    return current_target


def shoot(current_targets, index, power):
    if 0 <= index < len(current_targets):
        current_targets[index] -= power
        if current_targets[index] <= 0:
            del current_targets[index]
    return current_targets


def manipulating(targets):
    while True:
        command = input()

        if command == "End":
            print_the_result(targets)
            break

        current_command, ind, digits = command.split(" ")

        if current_command == "Shoot":
            targets = shoot(targets, int(ind), int(digits))
        elif current_command == "Add":
            targets = add(targets, int(ind), int(digits))
        elif current_command == "Strike":
            targets = strike(targets, int(ind), int(digits))


sequence_of_targets = [int(ch) for ch in input().split(" ")]
manipulating(sequence_of_targets)

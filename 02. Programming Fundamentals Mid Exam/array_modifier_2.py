def swap(first_index, second_index, current_list):
    current_list[first_index], current_list[second_index] = current_list[second_index], current_list[first_index]
    return current_list


def multiply(first_index, second_index, current_list):
    multiplier = current_list[second_index]
    current_list[first_index] *= multiplier
    return current_list


def decrease(current_list):
    for i in range(len(current_list)):
        current_list[i] -= 1
    return current_list


array = [int(ch) for ch in input().split(" ")]

while True:
    command = input()

    if command == "end":
        break

    current_command = command.split(" ")

    if current_command[0] == "swap":
        array = swap(int(current_command[1]), int(current_command[2]), array)
    elif current_command[0] == "multiply":
        array = multiply(int(current_command[1]), int(current_command[2]), array)
    elif current_command[0] == "decrease":
        array = decrease(array)

print(', '.join(str(ch) for ch in array))

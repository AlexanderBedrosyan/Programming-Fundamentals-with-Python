list_of_positions = [int(ch) for ch in input().split()]

total_sum = 0

while len(list_of_positions) > 0:
    index = int(input())

    current_number = 0
    if index > len(list_of_positions) - 1:
        index = len(list_of_positions) - 1
        current_number += list_of_positions[index]
        del list_of_positions[index]
        list_of_positions.append(list_of_positions[0])
    elif index < 0:
        index = 0
        current_number += list_of_positions[0]
        del list_of_positions[0]
        list_of_positions.insert(0, list_of_positions[-1])
    else:
        current_number += list_of_positions[index]
        del list_of_positions[index]

    for i in range(0, len(list_of_positions)):
        if list_of_positions[i] > current_number:
            list_of_positions[i] -= current_number
        elif list_of_positions[i] <= current_number:
            list_of_positions[i] += current_number

    total_sum += current_number

print(total_sum)
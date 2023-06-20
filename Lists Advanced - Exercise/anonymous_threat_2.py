def merge(current_list, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(current_list):
        end_index = len(current_list) - 1
    needed_index_list = []
    for index, letters in enumerate(current_list):
        if index in range(start_index + 1, end_index + 1):
            current_list[start_index] += current_list[index]
            needed_index_list.append(index)
    for current_index in needed_index_list[::-1]:
        if current_index != start_index:
            current_list.pop(current_index)
    return current_list


def divide(current_list, index, divide_rate):
    new_word = []
    current_word = current_list.pop(index)
    range_of_letters = 0
    new_range_ind = 0
    if divide_rate > len(current_word) - 1:
        new_range_ind = 1
    else:
        new_range_ind = len(current_word) // divide_rate
    for charts in range(divide_rate):
        if charts == divide_rate - 1:
            new_word.append(current_word[range_of_letters::])
            break
        else:
            new_word.append(current_word[range_of_letters: range_of_letters + new_range_ind:])
        range_of_letters += new_range_ind
    for ch in reversed(new_word):
        current_list.insert(index, ch)
    return current_list


array_of_data = input().split(" ")

command = input()

while command != "3:1":
    current_command, start_index, end_split_index = command.split(" ")

    if current_command == "merge":
        array_of_data = merge(array_of_data, int(start_index), int(end_split_index))
    elif current_command == "divide":
        array_of_data = divide(array_of_data, int(start_index), int(end_split_index))

    command = input()

print(*array_of_data)

numbers = input()

list_numbers = [int(ch) for ch in numbers.strip().split()]
new_list = []

for i in range(len(list_numbers)):
    if list_numbers[i] > 0:
        new_list.append(-list_numbers[i])
    elif list_numbers[i] < 0:
        new_list.append(int(-1 * list_numbers[i]))
    else:
        new_list.append(list_numbers[i])

print(new_list)

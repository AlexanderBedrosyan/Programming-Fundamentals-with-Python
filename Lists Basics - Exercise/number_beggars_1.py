numbers = input().replace(",", " ")
beggars = int(input())

numbers_list = [int(ch) for ch in numbers.strip().split()]
current_number = 0
new_list = []
counter = 0

while len(new_list) != beggars and (len(numbers_list) + len(new_list)) >= beggars:
    if counter > (len(numbers_list) - 1):
        numbers_list.remove(numbers_list[0])
        new_list.append(current_number)
        counter = 0
        current_number = 0
    else:
        current_number += numbers_list[counter]
        counter += beggars

if (len(numbers_list) + len(new_list)) < beggars:
    for i in range(beggars - len(numbers_list)):
        numbers_list.append(0)
    print(numbers_list)
else:
    print(new_list)

def tribonacci(number):
    number_list = [1, 1, 2]
    for i in range(3, number):
        new_number = number_list[i - 1] + number_list[i - 2] + number_list[i - 3]
        number_list.append(new_number)
    print(*number_list)


number = int(input())

if number >= 3:
    tribonacci(number)
elif number == 2:
    number_list = [1, 1]
    print(*number_list)
elif number == 1:
    number_list = [1]
    print(*number_list)
else:
    print(0)

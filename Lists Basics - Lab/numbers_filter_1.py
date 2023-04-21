n = int(input())

number_list = []
final_list = []

for i in range(n):
    current_number = int(input())

    number_list.append(current_number)

command = input()

for i in range(n):
    if command == "even":
        if number_list[i] % 2 == 0 or number_list[i] == 0:
            final_list.append(number_list[i])
    elif command == "odd":
        if number_list[i] % 2 != 0:
            final_list.append(number_list[i])
    elif command == "negative":
        if number_list[i] < 0:
            final_list.append(number_list[i])
    elif command == "positive":
        if number_list[i] >= 0:
            final_list.append(number_list[i])

print(final_list)

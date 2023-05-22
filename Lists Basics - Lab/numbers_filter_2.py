def the_list(num):
    number_list = []
    for i in range(num):
        current_number = int(input())

        number_list.append(current_number)

    return number_list


def final_list(n):
    final_list = []
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
    return final_list


n = int(input())

number_list = the_list(n)
final_list = final_list(n)

print(final_list)

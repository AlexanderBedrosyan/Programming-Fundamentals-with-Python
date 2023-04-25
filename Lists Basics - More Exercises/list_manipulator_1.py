def exchange(list, index):
    left_side = list[:(index + 1)]
    right_side = list[(index + 1):]
    return right_side + left_side


def min_even_odd(list, command):
    even_numbers = [even for even in beginning_list if even % 2 == 0]
    odd_numbers = [odd for odd in beginning_list if odd % 2 != 0]
    if command == "odd":
        return len(list) - list[::-1].index(min(odd_numbers)) - 1
    elif command == "even":
        return len(list) - list[::-1].index(min(even_numbers)) - 1


def max_even_odd(list, command):
    even_numbers = [even for even in beginning_list if even % 2 == 0]
    odd_numbers = [odd for odd in beginning_list if odd % 2 != 0]
    if command == "odd":
        return len(list) - list[::-1].index(max(odd_numbers)) - 1
    elif command == "even":
        return len(list) - list[::-1].index(max(even_numbers)) - 1


def first_even_odd(list, count, command):
    even_numbers = [even for even in list if even % 2 == 0]
    odd_numbers = [odd for odd in list if odd % 2 != 0]
    if command == "even":
        return even_numbers[0:count]
    elif command == "odd":
        return odd_numbers[0:count]


def last_even_odd(list, count, command):
    even_numbers = [even for even in list if even % 2 == 0]
    odd_numbers = [odd for odd in list if odd % 2 != 0]
    if command == "even":
        return even_numbers[-count::]
    elif command == "odd":
        return odd_numbers[-count::]


beginning_list = [int(ch) for ch in input().split(" ")]

while True:
    current_command = input()
    if current_command == "end":
        print(beginning_list)
        break

    even_numbers = [even for even in beginning_list if even % 2 == 0]
    odd_numbers = [odd for odd in beginning_list if odd % 2 != 0]

    command = current_command.split(" ")

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(beginning_list):
            beginning_list = exchange(beginning_list, int(command[1]))
        else:
            print("Invalid index")
    elif command[0] == "max":
        if command[1] == "even" and even_numbers:
            print(max_even_odd(beginning_list, command[1]))
        elif command[1] == "odd" and odd_numbers:
            print(max_even_odd(beginning_list, command[1]))
        else:
            print("No matches")
    elif command[0] == "min":
        if command[1] == "even" and even_numbers:
            print(min_even_odd(beginning_list, command[1]))
        elif command[1] == "odd" and odd_numbers:
            print(min_even_odd(beginning_list, command[1]))
        else:
            print("No matches")
    elif command[0] == "first":
        if 0 < int(command[1]) <= len(beginning_list):
            print(first_even_odd(beginning_list, int(command[1]), command[2]))
        else:
            print("Invalid count")
    elif command[0] == "last":
        if 0 < int(command[1]) <= len(beginning_list):
            print(last_even_odd(beginning_list, int(command[1]), command[2]))
        else:
            print("Invalid count")

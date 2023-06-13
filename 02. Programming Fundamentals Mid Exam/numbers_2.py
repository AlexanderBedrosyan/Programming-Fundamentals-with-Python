from statistics import mean


def print_the_result(current_list):
    if 0 < len(current_list) < 5:
        print(*current_list)
    elif len(current_list) == 0:
        print("No")
    else:
        counter = 0
        for ch in current_list:
            counter += 1
            if counter == 5:
                print(ch)
                break
            print(ch, end=" ")


def find_the_greater_numbers(current_list, average_number):
    new_list = []
    for _ in range(len(current_list)):
        ch = max(current_list)
        ind = current_list.index(ch)
        current_list.pop(ind)
        if ch > average_number:
            new_list.append(ch)
    print_the_result(new_list)


integers = [int(ch) for ch in input().split(" ")]
average = mean(integers)

if len(integers) <= 1:
    print("No")
    exit()

find_the_greater_numbers(integers, average)

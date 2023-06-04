def print_the_result(result):
    print(result)


def absolute_values(numbers):
    final_list = []
    for num in numbers:
        final_list.append(abs(num))
    print_the_result(final_list)


sequence_of_numbers = [float(ch) for ch in input().split()]
absolute_values(sequence_of_numbers)

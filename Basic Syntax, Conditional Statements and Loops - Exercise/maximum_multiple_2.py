def find_maximum_multiple(first_num, second_num):
    return (second_num // first_num) * first_num


print(find_maximum_multiple(int(input()), int(input())))

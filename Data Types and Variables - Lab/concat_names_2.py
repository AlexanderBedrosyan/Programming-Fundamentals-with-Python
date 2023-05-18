def concat_names():
    first_name = ""
    second_name = ""
    for i in range(1, 4):
        current_string = input()
        if i % 2 == 0:
            second_name += current_string
        else:
            first_name += current_string
    return first_name + second_name


print(concat_names())

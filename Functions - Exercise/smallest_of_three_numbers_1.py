def smallest_number(n1, n2, n3):
    tuple_list = []
    tuple_list.append(n1), tuple_list.append(n2), tuple_list.append(n3)
    return min(tuple_list)


print(smallest_number(int(input()), int(input()), int(input())))

def final_list(list_of_integers, row_min_numbers):
    for _ in range(row_min_numbers):
        ind = list_of_integers.index(min(list_of_integers))
        ch = list_of_integers.pop(ind)
    return list_of_integers


list_of_integers = [int(ch) for ch in input().split(" ")]
row_min_numbers = int(input())

print(', '.join(str(ch) for ch in final_list(list_of_integers, row_min_numbers)))

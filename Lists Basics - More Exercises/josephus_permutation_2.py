def new_list(starting_string, row):
    counter = 0
    current_list = []
    while len(starting_string) > 0:
        chart = starting_string.pop(0)
        counter += 1
        if counter == row:
            current_list.append(chart)
            counter = 0
        else:
            starting_string.append(chart)
    return current_list


starting_string = [ch for ch in input().split()]
row = int(input())
final_list = new_list(starting_string, row)
print(f"[{','.join(final_list)}]")

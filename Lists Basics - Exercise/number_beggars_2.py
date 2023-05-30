def list_changing(starting_list, n, starting_position, current_list):
    current_amount = 0
    for position in range(starting_position, len(starting_list), n):
        current_amount += starting_list[position]
    current_list.append(current_amount)
    return current_list


beggars = [int(ch) for ch in input().split(", ")]
n = int(input())
new_list = []
starting_position = 0

while sum(beggars) > sum(new_list):
    new_list = list_changing(beggars, n, starting_position, new_list)
    starting_position += 1

while len(new_list) < n:
    new_list.append(0)

print(new_list)

row = int(input())
column = 0
entries = []

for i in range(row):
    column_list = [int(ch) for ch in input().split(" ")]
    column = len(column_list)
    entries.append(column_list)

matrix = entries

battle_list = input().split(" ")
ship_destroy = 0

for i in range(len(battle_list)):
    row, current_column = [int(ch) for ch in battle_list[i].split("-")]

    if matrix[row][current_column] > 0:
        matrix[row][current_column] -= 1
        if matrix[row][current_column] == 0:
            ship_destroy += 1

print(ship_destroy)
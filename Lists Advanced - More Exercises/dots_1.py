matrix = []
rows = int(input())
moves_dict = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}

for _ in range(rows):
    matrix.append([ch for ch in input().split()])

columns = len(matrix[0])
checker = []
[checker.append("True") for ch in matrix if "." in ch]
counter = 0
position_dot = []
next_moves = []
final_count = [0]


while len(checker) > 0:
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == ".":
                position_dot.append([row, col])
                counter += 1
                matrix[row][col] = "-"
                break
        if len(position_dot) > 0:
            break

    while len(position_dot) > 0:
        for ch in position_dot:
            chart = position_dot.pop()
            position_col, position_row = chart[0], chart[1]
            for key in moves_dict:
                next_row, next_col = (position_col + moves_dict[key][0]), (position_row + moves_dict[key][1])
                if 0 <= next_row < rows and 0 <= next_col < columns:
                    if matrix[next_row][next_col] == ".":
                        counter += 1
                        next_moves.append([next_row, next_col])
                        matrix[next_row][next_col] = "-"

        while len(next_moves) > 0:
            position = next_moves.pop()
            position_dot.append(position)

    if len(position_dot) == 0:
        final_count.append(counter)
        counter = 0

    checker = []
    [checker.append("True") for ch in matrix if "." in ch]

print(max(final_count))

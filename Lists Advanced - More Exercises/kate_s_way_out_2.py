rows = int(input())
matrix = []
moves_dict = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}

for i in range(rows):
    matrix.append([ch for ch in input()])

column = len(matrix[0])
position_kate = []
next_moves = []
win = False
moves_counter = 0
winner_counter = []

for row in range(rows):
    for col in range(column):
        if matrix[row][col] == "k":
            position_kate.append([row, col])

while True:
    for i in range(len(position_kate)):
        current_position = position_kate.pop()
        for ch in moves_dict:
            current_row, current_col = (moves_dict[ch][0] + current_position[0]), (moves_dict[ch][1] + current_position[1])
            if 0 <= current_row < rows and 0 <= current_col < column:
                if matrix[current_row][current_col] == " ":
                    matrix[current_row][current_col] = "k"
                    next_moves.append([current_row, current_col])
                    matrix[current_position[0]][current_position[1]] = "#"
            else:
                winner_counter.append(moves_counter + 1)
                win = True

    if len(next_moves) >= 1:
        moves_counter += 1
    else:
        break

    for i in range(len(next_moves)):
        position_kate.append(next_moves[i])

    next_moves = []

if win:
    print(f"Kate got out in {max(winner_counter)} moves")
else:
    print("Kate cannot get out")

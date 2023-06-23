def fill_the_board(rows):
    board = []
    for _ in range(rows):
        line = [ch for ch in input().split(" ")]
        board.append(line)
    return board


def find_a_dot(current_list):
    coordinates = []
    column = len(current_list[0])
    condition = False
    for row in range(rows):
        for col in range(column):
            if current_list[row][col] == ".":
                coordinates.append([row, col])
                condition = True
                break
        if condition:
            break
    return coordinates


def count_the_chain_of_dots(board, count_connected_dots, position, directions):
    counter = 1
    column = len(board[0])
    while position:
        list_of_positions = [ch for ch in position]
        position = []
        while list_of_positions:
            current_position = list_of_positions.pop(0)
            board[current_position[0]][current_position[1]] = "-"
            for key, coordinates in directions.items():
                row = current_position[0] + coordinates[0]
                col = current_position[1] + coordinates[1]
                if 0 <= row < len(board) and 0 <= col < column:
                    if board[row][col] == ".":
                        position.append([row, col])
                        board[row][col] = "-"
                        counter += 1
    count_connected_dots.append(counter)
    return board, count_connected_dots, position_dot


rows = int(input())
directions = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
moves = 0
count_connected_dots = []
dots_board = fill_the_board(rows)
position_dot = find_a_dot(dots_board)

while position_dot:
    dots_board, count_connected_dots, position_dot = count_the_chain_of_dots(dots_board, count_connected_dots,
                                                                             position_dot, directions)
    position_dot = find_a_dot(dots_board)

if count_connected_dots:
    print(max(count_connected_dots))
else:
    print(0)

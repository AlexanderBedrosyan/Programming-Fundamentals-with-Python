def board_and_kate_position(maze, where_is_kate):
    for row in range(rows):
        line = [ch for ch in input()]
        if "k" in line:
            where_is_kate.append([row, line.index("k")])
        maze.append(line)
    return board, where_is_kate


def next_kate_positions(current_kat_position, maze, directions):
    flag = False
    new_position = []
    column = len(maze[0])
    while current_kat_position:
        current_positon = current_kat_position.pop(0)
        for key, coordinates in directions.items():
            row = current_positon[0] + coordinates[0]
            col = current_positon[1] + coordinates[1]
            if 0 <= row < len(maze) and 0 <= col < column:
                if maze[row][col] == "#":
                    continue
                elif maze[row][col] == " ":
                    new_position.append([row, col])
            else:
                flag = True
        board[current_positon[0]][current_positon[1]] = "#"
    return new_position, board, flag


def result(out_of_maze):
    if out_of_maze:
        return f"Kate got out in {max(out_of_maze)} moves"
    else:
        return "Kate cannot get out"


rows = int(input())
directions = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
board = []
kate_position = []
moves = 0
out_of_maze = []

board, kate_position = board_and_kate_position(board, kate_position)

while kate_position:
    condition = False
    kate_position, board, condition = next_kate_positions(kate_position, board, directions)
    if condition:
        out_of_maze.append(moves + 1)
    if kate_position:
        moves += 1

print(result(out_of_maze))

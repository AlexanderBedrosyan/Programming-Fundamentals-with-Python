def add(dict, piece, composer, key):
    dict[piece] = {}
    dict[piece][composer] = key
    return dict


def remove(dict, piece):
    dict.pop(piece)
    return dict


def changekey(dict, piece, key):
    for keys in dict:
        if keys == piece:
            for ch in dict[keys]:
                dict[keys][ch] = key
    return dict


pieces = int(input())

pieces_dict = {}

for i in range(pieces):
    piece = input().split("|")

    pieces_dict[piece[0]] = {}
    pieces_dict[piece[0]][piece[1]] = piece[2]

while True:
    command = input()

    if command == "Stop":
        break

    list_command = command.split("|")

    if list_command[0] == "Add":
        if list_command[1] in pieces_dict:
            print(f"{list_command[1]} is already in the collection!")
        else:
            pieces_dict = add(pieces_dict, list_command[1], list_command[2], list_command[3])
            print(f"{list_command[1]} by {list_command[2]} in {list_command[3]} added to the collection!")
    elif list_command[0] == "Remove":
        if list_command[1] not in pieces_dict:
            print(f"Invalid operation! {list_command[1]} does not exist in the collection.")
        else:
            pieces_dict = remove(pieces_dict,list_command[1])
            print(f"Successfully removed {list_command[1]}!")
    elif list_command[0] == "ChangeKey":
        if list_command[1] not in pieces_dict:
            print(f"Invalid operation! {list_command[1]} does not exist in the collection.")
        else:
            pieces_dict = changekey(pieces_dict, list_command[1], list_command[2])
            print(f"Changed the key of {list_command[1]} to {list_command[2]}!")


for keys in pieces_dict:
    Piece = keys
    composer = ""
    key = ""
    for ch in pieces_dict[keys]:
        composer = ch
        key = pieces_dict[keys][ch]

    print(f"{Piece} -> Composer: {composer}, Key: {key}")
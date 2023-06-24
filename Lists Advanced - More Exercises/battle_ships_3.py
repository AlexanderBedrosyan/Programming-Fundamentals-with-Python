def ships_on_the_field(rows):
    final_field = []
    for row in range(rows):
        line = [int(ch) for ch in input().split(" ")]
        final_field.append(line)
    return final_field


def the_attack(field_of_fight, current_coordinate, counter):
    if field_of_fight[current_coordinate[0]][current_coordinate[1]] != 0:
        field_of_fight[current_coordinate[0]][current_coordinate[1]] -= 1
        if field_of_fight[current_coordinate[0]][current_coordinate[1]] == 0:
            counter += 1
    return field_of_fight, counter


rows = int(input())
field = ships_on_the_field(rows)
destroyed_ships = 0

attack_coordinates = [ch for ch in input().split(" ")]

for coordinate in attack_coordinates:
    current_coordinate = [int(ch) for ch in coordinate.split("-")]
    field, destroyed_ships = the_attack(field, current_coordinate, destroyed_ships)

print(destroyed_ships)

def if_not_enough_chairs(chairs, visitors, room):
    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {room}")


def if_enough_chairs(chairs, visitors):
    if chairs >= visitors:
        print(f"Game On, {chairs - visitors} free chairs left")


chairs = 0
visitors = 0
room_number = 0

for i in range(int(input())):
    room_number += 1
    current_chairs, current_visitors = input().split(" ")
    current_visitors = int(current_visitors)

    chairs += len(current_chairs)
    visitors += current_visitors

    if_not_enough_chairs(len(current_chairs), current_visitors, room_number)

if_enough_chairs(chairs, visitors)

def checking_chairs(giving_list, counter, free_spaces):
    free_spaces_index = (chair_index - people)
    free_spaces += free_spaces_index
    return free_spaces


def checking_missing_chairs(giving_list, counter):
    print(f"{people - chair_index} more chairs needed in room {counter}"),
    return False


rooms = int(input())
counter = 0
missing_chairs = True
free_spaces = 0

for i in range(rooms):
    giving_list = input().split()
    counter += 1
    chair_index = len(giving_list[0])
    people = int(giving_list[1])

    if chair_index >= people:
        free_spaces = checking_chairs(giving_list, counter, free_spaces)
    elif people > chair_index:
        missing_chairs = checking_missing_chairs(giving_list, counter)


if missing_chairs:
    print(f"Game On, {free_spaces} free chairs left")

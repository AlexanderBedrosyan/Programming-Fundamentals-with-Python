force_dict = {}

while True:
    command = input()
    side_number = 0
    user_number = 0

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")

        for key, value in force_dict.items():
            if key == side:
                side_number += 1
            if user in value:
                user_number += 1

        if side_number == user_number == 0:
            force_dict[side] = []
            force_dict[side].append(user)
        if side_number > 0 and user_number == 0:
            force_dict[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")

        for key, value in force_dict.items():
            if user in value:
                force_dict[key].remove(user)
            if side == key:
                side_number += 1

        if side_number == user_number == 0:
            force_dict[side] = []
            force_dict[side].append(user)
        if side_number > 0 and user_number == 0:
            force_dict[side].append(user)

        print(f"{user} joins the {side} side!")

for key, value in force_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in range(len(value)):
            print(f"! {value[i]}")
def new_force_and_user(current_dict, side, user):
    no_such_user = True
    if current_dict:
        for sides, users in current_dict.items():
            if user in users:
                no_such_user = False
                break

    if no_such_user:
        if side not in current_dict:
            current_dict[side] = []
        current_dict[side].append(user)
    return current_dict


def transfer_the_user_to_new_force(current_dict, user, side):
    if current_dict:
        for sides, users in current_dict.items():
            if user in users:
                users.remove(user)
                break
    if side not in current_dict:
        current_dict[side] = []
    current_dict[side].append(user)
    print(f"{user} joins the {side} side!")
    return current_dict


force_command = input()
force_dictionary = {}

while force_command != "Lumpawaroo":
    if "|" in force_command:
        side, user = force_command.split(" | ")
        force_dictionary = new_force_and_user(force_dictionary, side, user)
    else:
        user, side = force_command.split(" -> ")
        force_dictionary = transfer_the_user_to_new_force(force_dictionary, user, side)

    force_command = input()

for sides, users in force_dictionary.items():
    if not users:
        continue
    print(f"Side: {sides}, Members: {len(users)}")
    for name in users:
        print(f"! {name}")

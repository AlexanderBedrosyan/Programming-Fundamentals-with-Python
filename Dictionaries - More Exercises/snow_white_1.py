def checking(name, color, physics):
    if (" " not in name) and ("<" not in name) and (":" not in name) and (">" not in name) and \
            (" " not in color) and ("<" not in color) and (":" not in color) and (">" not in color) \
            and (physics in range(0, 2 ** 31 - 1)):
        return True
    else:
        return False


def modify_dict(dict, name, color, physics):
    if color not in dict:
        dict[color] = {}
        dict[color][name] = physics
    else:
        if name not in dict[color]:
            dict[color][name] = physics
        else:
            if dict[color][name] < physics:
                dict[color][name] = physics
    return dict


dwarfs_dict = {}

while True:
    information = input()

    if information == "Once upon a time":
        break

    name, hat_color, physics = information.split(" <:> ")

    conditions = checking(name, hat_color, int(physics))

    if conditions:
        dwarfs_dict = modify_dict(dwarfs_dict, name, hat_color, int(physics))

final_list = []

for ch in dwarfs_dict:
    for key, value in dwarfs_dict[ch].items():
        final_list.append({"nested_dict_charts": len(dwarfs_dict[ch]), "name_dwarfs": key, "power": value, "color":ch})

for charts in sorted(final_list, key=lambda x: (-x["power"], -x["nested_dict_charts"])):
    print(f"({charts['color']}) {charts['name_dwarfs']} <-> {charts['power']}")
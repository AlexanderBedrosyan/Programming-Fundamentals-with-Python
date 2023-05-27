my_dict = {}


def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)


while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split(" ")
    if name not in my_dict:
        my_dict[name] = {}
        my_dict[name][price] = float(quantity)
    else:
        for key in my_dict[name]:
            change_dict_key(my_dict[name], key, price)
            break

        my_dict[name][price] += float(quantity)


for ch in my_dict:
    for item in my_dict[ch]:
        print(f"{ch} -> {float(item) * my_dict[ch][item]:.2f}")

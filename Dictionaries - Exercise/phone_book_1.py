def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


phonebook_dict = {}
n = 0

while True:
    command = input()
    if is_integer(command):
        n = int(command)
        break

    key, value = command.split("-")
    phonebook_dict[key] = value

for i in range(0, n):
    name = input()

    if name in phonebook_dict:
        print(f"{name} -> {phonebook_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")
def remove_str_start_end(name, start, end):
    return name[:start] + name[end + 1:]


def add(name, index, new_name):
    return f"{name[:index] + new_name + name[index:]}"


def switch(name, old_name, new):
    return name.replace(old_name, new)


travel = input()

while True:
    command = input()

    if command == "Travel":
        break

    stop, index, new_name = command.split(":")

    if "Add Stop" == stop:
        if 0 <= int(index) < len(travel):
            travel = add(travel, int(index), new_name)
        print(travel)

    if "Remove Stop" == stop:
        if int(index) in range(len(travel)) and int(new_name) in range(len(travel)):
            travel = remove_str_start_end(travel, int(index), int(new_name))
        print(travel)
    if "Switch" == stop:
        if index in travel:
            travel = switch(travel, index, new_name)
        print(travel)

print(f"Ready for world tour! Planned stops: {travel}")
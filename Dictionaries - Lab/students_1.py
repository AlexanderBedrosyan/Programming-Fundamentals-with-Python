students = {}
lesson = ""

while True:
    command = input()

    if ":" in command:
        name, id, keys = command.split(":")
        if keys not in students:
            students[keys] = []
        students[keys].append(f"{name} - {id}")
    else:
        if "_" in command:
            lesson = command.replace("_", " ")
            break
        else:
            lesson = command
            break

print('\n'.join(students[lesson]))
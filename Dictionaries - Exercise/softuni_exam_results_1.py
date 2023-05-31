name_points = {}
language_counter = {}

while True:
    command = input()

    if command == "exam finished":
        break

    current_command = command.split("-")

    if len(current_command) == 3:
        username, language, points = current_command
        if username not in name_points:
            name_points[username] = 0
        if name_points[username] < int(points):
            name_points[username] = int(points)
        if language not in language_counter:
            language_counter[language] = 0
        language_counter[language] += 1

    else:
        if current_command[0] in name_points:
            del name_points[current_command[0]]

print("Results:")
for key, values in name_points.items():
    print(f"{key} | {values}")
print("Submissions:")
for key, values in language_counter.items():
    print(f"{key} - {values}")
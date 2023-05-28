courses_dict = {}

while True:
    command = input()

    if command == "end":
        break

    course, student = command.split(" : ")

    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)

for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
def exam_information(current_dict, name, course, result):
    if course not in current_dict:
        current_dict[course] = []

    if not current_dict[course]:
        current_dict[course].append({name: result})
    else:
        condition = False
        for dicts in current_dict[course]:
            if name in dicts:
                if dicts[name] < result:
                    dicts[name] = result
                current_dict[course].append({})
                condition = True
        if not condition:
            current_dict[course].append({name: result})
    return current_dict


def ban_the_student(current_dict, name):
    for key, values in current_dict.items():
        for elements in range(len(values)):
            for current_name, result in values[elements].items():
                if current_name == name:
                   values[elements][current_name] = "banned"
    return current_dict


softuni_exam_information = {}

command = input()

while command != "exam finished":
    command = command.split("-")
    if command[1] != "banned":
        name, course, result = command[0], command[1], int(command[2])
        softuni_exam_information = exam_information(softuni_exam_information, name, course, result)
    else:
        name = command[0]
        softuni_exam_information = ban_the_student(softuni_exam_information, name)
    command = input()

results = []
submissions = []

for course, students in softuni_exam_information.items():
    submissions.append(f"{course} - {len(students)}")

    for i in range(len(students)):
        if len(students[i]) == 0:
            continue
        for name, result in students[i].items():
            if result == "banned":
                continue
            results.append(f"{name} | {result}")

print(f"Results:")
print('\n'.join(results))
print("Submissions:")
print('\n'.join(submissions))

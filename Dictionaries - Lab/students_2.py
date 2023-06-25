def points_of_courses():
    current_dict = {}
    needed_course_statistics = ''

    while True:
        command = input().split(":")

        if len(command) == 1:
            needed_course_statistics = command[0]
            break

        name, points, course = command[0], command[1], command[2]
        if course not in current_dict:
            current_dict[course] = {}
        current_dict[course][name] = points

    return current_dict, needed_course_statistics


students_dict, needed_statistics = points_of_courses()
if "_" in needed_statistics:
    needed_statistics = needed_statistics.replace("_", " ")
[print(f"{name} - {points}") for name, points in students_dict[needed_statistics].items()]

def add(current_list, new_element):
    if new_element not in current_list:
        current_list.append(new_element)
    return current_list


def insert(current_list, new_element, index):
    if new_element not in current_list:
        current_list.insert(index, new_element)
    return current_list


def remove(current_list, element):
    exercise = element + '-Exercise'
    if element in current_list:
        current_list.remove(element)
    if exercise in current_list:
        current_list.remove(exercise)
    return current_list


def swap(current_list, first_element, second_element):
    if first_element in current_list and second_element in current_list:
        index_first_element = current_list.index(first_element)
        index_second_element = current_list.index(second_element)
        current_list[index_first_element], current_list[index_second_element] = \
            current_list[index_second_element], current_list[index_first_element]

        exercise_first_element = first_element + '-Exercise'
        exercise_second_element = second_element + '-Exercise'

        if exercise_first_element in current_list:
            current_list.remove(exercise_first_element)
            current_list.insert(index_second_element + 1, exercise_first_element)
        if exercise_second_element in current_list:
            current_list.remove(exercise_second_element)
            current_list.insert(index_first_element + 1, exercise_second_element)
    return current_list


def exercise_if_element_in(current_list, element):
    exercise = element + '-Exercise'
    ind = current_list.index(element)
    if exercise not in current_list:
        current_list.insert(ind + 1, exercise)
    return current_list


def exercise_if_element_not_in(current_list, element):
    exercise = element + '-Exercise'
    current_list.append(element)
    current_list.append(exercise)
    return current_list


lessons = [ch for ch in input().split(", ")]

command = input()

while command != "course start":
    current_command = command.split(":")
    title_of_lesson = current_command[1]

    if current_command[0] == "Add":
        lessons = add(lessons, title_of_lesson)
    elif current_command[0] == "Insert":
        index = int(current_command[2])
        lessons = insert(lessons, title_of_lesson, index)
    elif current_command[0] == "Remove":
        lessons = remove(lessons, title_of_lesson)
    elif current_command[0] == "Swap":
        second_lesson_for_swap = current_command[2]
        lessons = swap(lessons, title_of_lesson, second_lesson_for_swap)
    elif current_command[0] == "Exercise":
        if title_of_lesson in lessons:
            lessons = exercise_if_element_in(lessons, title_of_lesson)
        else:
            lessons = exercise_if_element_not_in(lessons, title_of_lesson)

    command = input()

count = 0

for chart in lessons:
    count += 1
    print(f"{count}.{chart}")

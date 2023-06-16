from math import ceil


def final_prints(result_list, attendance_list):
    if len(result_list) == 0 or len(attendance_list) == 0:
        print(f"Max Bonus: {0}.")
        print(f"The student has attended {0} lectures.")
        exit()
    needed_result = max(result_list)
    ind = result_list.index(needed_result)
    needed_attendance = attendance_list[ind]
    print(f"Max Bonus: {ceil(needed_result)}.")
    print(f"The student has attended {needed_attendance} lectures.")


def fulfill_result_list(result_list, attendance, lectures, bonus):
    total_bonus = attendance / lectures * (5 + bonus)
    result_list.append(total_bonus)
    return result_list


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
result_lists = []
attendance_list = []

for _ in range(number_of_students):
    current_attendance = int(input())
    attendance_list.append(current_attendance)

    result_lists = fulfill_result_list(result_lists, current_attendance, number_of_lectures, additional_bonus)

final_prints(result_lists, attendance_list)

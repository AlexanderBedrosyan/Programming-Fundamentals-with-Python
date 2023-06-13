def softuni_reception(first_employee, second_employee, third_employee, students):
    needed_hours = 0
    answers_per_hour = first_employee + second_employee + third_employee
    while students > 0:
        needed_hours += 1
        if needed_hours % 4 == 0:
            continue
        students -= answers_per_hour
    print(f"Time needed: {needed_hours}h.")


softuni_reception(int(input()), int(input()), int(input()), int(input()))

employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())

counter = 0
counter_hours = 0

while students > 0:
    if counter == 3:
        counter_hours += 1
        counter = 0
        continue

    counter += 1
    counter_hours += 1
    students -= (employee_one + employee_two + employee_three)

print(f"Time needed: {counter_hours}h.")
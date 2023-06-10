from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
attendances_max = 0

for i in range(students):
    attendances = int(input())

    current_bonus = attendances / lectures * (5 + bonus)

    if current_bonus > max_bonus:
        max_bonus = current_bonus
        attendances_max = attendances
    else:
        continue

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendances_max} lectures.")
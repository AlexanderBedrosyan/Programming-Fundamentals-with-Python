employees_list = [int(ch) for ch in input().split()]
multiply_coef = int(input())

employees_list = list(map(lambda x: x * multiply_coef, employees_list))

total_sum_employees_list = sum(employees_list)
count_employees_list = len(employees_list)

new_list = [int(ch) for ch in employees_list if ch >= (total_sum_employees_list / count_employees_list)]

if len(new_list) >= (total_sum_employees_list / count_employees_list):
    print(f"Score: {len(new_list)}/{count_employees_list}. Employees are happy!")
else:
    print(f"Score: {len(new_list)}/{count_employees_list}. Employees are not happy!")

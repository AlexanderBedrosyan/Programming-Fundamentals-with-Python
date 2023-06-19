employees = [int(ch) for ch in input().split(" ")]
rate = int(input())
employees_happiness = [ch * rate for ch in employees]
happiness = [ch for ch in employees_happiness if ch >= (sum(employees_happiness) / len(employees))]

if len(happiness) / len(employees) >= 0.5:
    print(f"Score: {len(happiness)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happiness)}/{len(employees)}. Employees are not happy!")
courses_dict = {}
num = int(input())

for i in range(num):
    name, grade = input(), float(input())

    if name not in courses_dict:
        courses_dict[name] = []
    courses_dict[name].append(grade)

for key, value in courses_dict.items():
    if (sum(value) / len(value)) >= 4.50:
        print(f"{key} -> {(sum(value) / len(value)):.2f}")
employee_dict = {}

while True:
    command = input()

    if command == "End":
        break

    company, client_id = command.split(" -> ")

    if company not in employee_dict:
        employee_dict[company] = []
    if client_id not in employee_dict[company]:
        employee_dict[company].append(client_id)

for key, value in employee_dict.items():
    print(key)
    for i in range(len(value)):
        print(f"-- {value[i]}")
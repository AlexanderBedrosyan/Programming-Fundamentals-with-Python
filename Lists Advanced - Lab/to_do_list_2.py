def final_result(current_dict):
    result = []
    for key, values in sorted(current_dict.items()):
        result.append(values)
    return result


to_do_dict = {}

command = input()

while command != "End":
    importance, note = command.split("-")
    to_do_dict[int(importance)] = note

    command = input()

print(final_result(to_do_dict))
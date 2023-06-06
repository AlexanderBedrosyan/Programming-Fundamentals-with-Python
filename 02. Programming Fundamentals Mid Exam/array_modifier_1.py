numbers = input()

single_number = ""
listn = []
action = ""
action_list = []

for i in range(0, len(numbers)):
    if numbers[i] == " ":
        listn.append(int(single_number))
        single_number = ""
        continue
    elif i == (len(numbers) - 1):
        single_number += numbers[i]
        listn.append(int(single_number))
        break
    else:
        single_number += numbers[i]

while True:
    function = input()
    if function == "end":
        break
    else:
        for item in range(0, len(function)):
            if function[item] == " ":
                action_list.append(action)
                action = ""
                continue
            elif item == len(function) - 1:
                action += function[item]
                action_list.append(action)
                action = ""
                break
            else:
                action += function[item]

    if action_list[0] == "swap":
        listn[int(action_list[1])], listn[int(action_list[2])] = listn[int(action_list[2])], listn[int(action_list[1])]
        action_list = []
    elif action_list[0] == "multiply":
        listn[int(action_list[1])] = listn[int(action_list[1])] * listn[int(action_list[2])]
        action_list = []
    elif action_list[0] == "decrease":
        for num in range(0, len(listn)):
            listn[num] = listn[num] - 1
        action_list = []

print(*listn, sep=", ")
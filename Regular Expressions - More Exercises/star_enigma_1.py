import re

def modify_dict(dict, code_list):
    value = ""
    key = ""
    for i in range(len(code_list)):
        if code_list[i] == "@":
            index = code_list.index(code_list[i])
            value = code_list[index + 1]
        if code_list[i] == "!":
            index = code_list.index(code_list[i])
            if code_list[index + 1] == "A":
                key = "Attacked"
                break
            else:
                key = "Destroyed"
                break
    if key not in dict:
        dict[key] = []
    dict[key].append(value)
    return dict


num = int(input())
pattern = r'[sStTaArR]'
action_pattern = r'(\@)([A-Za-z]+)([^\@\-\!\:\>]*)?(\:)([0-9]+)([^\@\-\!\:\>]*)?(\!)([AD])(\!)([^\@\-\!\:\>]*)?(\->)([0-9]+)'

final_dict = {}

for i in range(num):
    codes = input()
    new_code = ''

    find_symbols = re.findall(pattern, codes)
    count_value = len(find_symbols)

    for ch in codes:
        new_ch = ord(ch) - count_value
        new_code += chr(new_ch)

    all_details = re.findall(action_pattern, new_code)

    if len(all_details) > 0:
        final_dict = modify_dict(final_dict, all_details[0])

attached_list = []
destroyed_list = []

for ch in final_dict:
    if ch == "Attacked":
        for item in sorted(final_dict[ch]):
            attached_list.append(item)
    else:
        for item in sorted(final_dict[ch]):
            destroyed_list.append(item)

if len(attached_list) == 0:
    print("Attacked planets: 0")
else:
    print(f"Attacked planets: {len(attached_list)}")
    for i in attached_list:
        print(f"-> {i}")

if len(destroyed_list) == 0:
    print("Destroyed planets: 0")
else:
    print(f"Destroyed planets: {len(destroyed_list)}")
    for i in destroyed_list:
        print(f"-> {i}")


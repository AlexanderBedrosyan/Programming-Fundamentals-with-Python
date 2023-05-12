def isvalidint(number):
    if 97 <= ord(number.lower()) <= 122:
        return str(number)
    else:
        return int(number)


code = input().split()
new_code = []

for i in range(len(code)):
    current_list = [ch for ch in code[i]]

    for item in range(len(current_list)):
        current_list[item] = isvalidint(current_list[item])

    magic_number = ""

    for digit in range(len(current_list)):
        if 97 <= ord(str(current_list[digit]).lower()) <= 122:
            break
        else:
            magic_number += str(current_list[digit])

    current_list = [ch for ch in current_list if ch == str(ch)]
    current_list.insert(0, chr(int(magic_number)))
    current_list[1], current_list[-1] = current_list[-1], current_list[1]

    print(''.join(current_list), end=" ")

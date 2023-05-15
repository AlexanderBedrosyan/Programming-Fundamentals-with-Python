string_name = input()

number_list = []
string_list = []
take_list = []
skip_list = []

for i in range(len(string_name)):
    if string_name[i].isdigit():
        number_list.append(int(string_name[i]))
    else:
        string_list.append(string_name[i])

for x in range(len(number_list)):
    if x % 2 == 0:
        take_list.append(number_list[x])
    else:
        skip_list.append(number_list[x])

take_number = 0
skip_number = 0

index = 0
new_string = ""

for i in range(len(take_list)):
    take_number = take_list[i]
    skip_number = skip_list[i]
    new_string += "".join(string_list[:take_number])
    del string_list[0:take_number+skip_number]

print(new_string)

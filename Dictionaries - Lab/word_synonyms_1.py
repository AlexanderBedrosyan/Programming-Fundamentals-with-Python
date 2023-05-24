my_dictionary = {}
number = int(input())

for i in range(0, number):
    keys = input()
    values = input()
    if keys in my_dictionary:
        my_dictionary[keys].append(values)
    else:
        my_dictionary[keys] = []
        my_dictionary[keys].append(values)

for keys in my_dictionary:
    print(f"{keys} - {', '.join(my_dictionary[keys])}")
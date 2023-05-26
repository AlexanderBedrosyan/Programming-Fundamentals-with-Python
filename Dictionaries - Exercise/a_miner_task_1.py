my_dictionary = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())

    if command not in my_dictionary:
        my_dictionary[command] = quantity
    else:
        my_dictionary[command] += quantity

for keys in my_dictionary:
    print(f"{keys} -> {my_dictionary[keys]}")
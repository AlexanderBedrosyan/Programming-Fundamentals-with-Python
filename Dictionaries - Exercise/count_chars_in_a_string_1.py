my_list = [ch for ch in str(input()) if ch != " "]
my_dictionary = {}

for i in my_list:
    if i not in my_dictionary:
        my_dictionary[i] = 1
    else:
        my_dictionary[i] += 1

for keys in my_dictionary:
    print(f"{keys} -> {my_dictionary[keys]}")
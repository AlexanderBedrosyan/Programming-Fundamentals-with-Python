my_list = [ch.lower() for ch in input().split()]
my_dictionary = {}

for i in my_list:
    if my_list.count(i) % 2 != 0:
        my_dictionary[i] = ""

print(' '.join(my_dictionary.keys()))
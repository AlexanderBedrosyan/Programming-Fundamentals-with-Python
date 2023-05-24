current_list = input().split(", ")
my_dictonary = {}

for items in current_list:
    my_dictonary[items] = ord(items)

print(my_dictonary)
numbers = input()

numbers_list = [int(ch) for ch in numbers.strip().split(",")]

for items in numbers_list:
    if items == 0:
        numbers_list.remove(items)
        numbers_list.append(0)

print(numbers_list)

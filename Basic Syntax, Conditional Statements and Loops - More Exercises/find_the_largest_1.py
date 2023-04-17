number = int(input())

numbers_list = []
max_number = []

for index, digits in enumerate(str(number)):
    numbers_list.append(int(digits))

for i in range(0, len(numbers_list)):
    max_number.append(max(numbers_list))
    numbers_list.remove(max(numbers_list))

print(*max_number, sep="")
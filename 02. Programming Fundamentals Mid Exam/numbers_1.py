import heapq

numbers = input().strip()

list_numbers = [int(ch) for ch in (numbers.strip()).split(" ")]
avarage_number = sum(list_numbers) / len(list_numbers)
above_avarage_list = []

for i in range(0, len(list_numbers)):
    if list_numbers[i] > avarage_number:
        above_avarage_list.append(list_numbers[i])
    else:
        continue

if len(above_avarage_list) == 0:
    print("No")
else:
    print(*heapq.nlargest(5, above_avarage_list))
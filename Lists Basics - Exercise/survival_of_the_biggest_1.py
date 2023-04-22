numbers = input()
needed_numbers = int(input())

number_list = [int(ch) for ch in numbers.strip().split()]

for i in range(needed_numbers):
    number_list.remove(min(number_list))

print(*number_list, sep=", ")

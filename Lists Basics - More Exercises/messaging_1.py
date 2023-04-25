index_numbers = input()
words = input()

index_numbers_list = [int(ch) for ch in index_numbers.strip().split()]
words_list = [str(items) for items in words.strip()]
new_list = []

for i in range(len(index_numbers_list)):
    current_list = []
    while index_numbers_list[i] > 0:
        current_list.append(index_numbers_list[i] % 10)
        index_numbers_list[i] = (index_numbers_list[i] - index_numbers_list[i] % 10) // 10

    amount_current_list = sum(current_list)

    while amount_current_list >= len(words_list):
        amount_current_list -= len(words_list)

    new_list.append(words_list[amount_current_list])
    words_list.remove(words_list[amount_current_list])
    amount_current_list = 0

print(*new_list, sep="")

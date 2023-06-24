from collections import deque

final_string = ''
current_string = input()

number_list = [int(ch) for ch in current_string if ch.isdigit()]
letter_list = deque([ch for ch in current_string if not ch.isdigit()])

take_list = [int(number_list[digit]) for digit in range(len(number_list)) if digit % 2 == 0]
skip_list = [int(digit) for index, digit in enumerate(number_list) if index % 2 != 0]

for i in range(len(take_list)):
    if take_list[i] != 0 and len(letter_list) > 0:
        for _ in range(take_list[i]):
            ch = letter_list.popleft()
            final_string += ch
            if len(letter_list) == 0:
                break

    if skip_list[i] != 0 and len(letter_list) > 0:
        for _ in range(skip_list[i]):
            ch = letter_list.popleft()
            if len(letter_list) == 0:
                break

print(final_string)

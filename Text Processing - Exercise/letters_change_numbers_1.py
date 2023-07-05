def lower_letter_start(num, letter):
    letter_sum = ord(letter.lower()) - 96
    return num * letter_sum


def upper_letter_start(num, letter):
    letter_sum = ord(letter.lower()) - 96
    return num / letter_sum


def lower_letter_end(letter):
    letter_sum = ord(letter.lower()) - 96
    return letter_sum


def upper_letter_end(letter):
    letter_sum = ord(letter.lower()) - 96
    return letter_sum


text_list = input().split()
total_sum = 0

for i in range(len(text_list)):
    current_sum = 0
    if len(text_list[i]) > 2:
        first_letter = text_list[i][0]
        last_letter = text_list[i][-1]
        number = int(text_list[i][1:-1])
        if 65 <= ord(first_letter) <= 90:
            current_sum += upper_letter_start(number, first_letter)
        elif 97 <= ord(first_letter) <= 122:
            current_sum += lower_letter_start(number, first_letter)

        if 65 <= ord(last_letter) <= 90:
            current_sum -= upper_letter_end(last_letter)
        elif 97 <= ord(last_letter) <= 122:
            current_sum += lower_letter_end(last_letter)

    total_sum += current_sum

print(f"{total_sum:.2f}")

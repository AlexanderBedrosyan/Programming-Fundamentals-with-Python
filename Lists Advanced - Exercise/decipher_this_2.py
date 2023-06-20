def number_finder(word):
    number = ''
    number_index = 1
    for ch in word:
        if ch.isdigit():
            number += ch
        if not ch.isdigit():
            number_index -= 1
            break
        number_index += 1
    word = word[number_index::]
    return chr(int(number)) + word


def exchange_second_to_last(word):
    current_list_word = [ch for ch in word]
    current_list_word[1], current_list_word[-1] = current_list_word[-1], current_list_word[1]
    return ''.join((current_list_word))


current_message = input().split(" ")

for i in range(len(current_message)):
    current_message[i] = number_finder(current_message[i])
    current_message[i] = exchange_second_to_last(current_message[i])

print(*current_message)

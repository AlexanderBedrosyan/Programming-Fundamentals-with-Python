def character_multiplier(word):
    total_sum = 0
    number = 0

    if len(word[0]) > len(word[1]):
        number = len(word[0])
    else:
        number = len(word[1])

    for i in range(number):
        if (len(word[0]) - 1) < i <= (len(word[1]) - 1):
            total_sum += ord(word[1][i])
        elif len(word[0]) - 1 >= i > len(word[1]) - 1:
            total_sum += ord(word[0][i])
        else:
            total_sum += (ord(word[0][i]) * ord(word[1][i]))

    return total_sum


list_word = input().split(" ")

print(character_multiplier(list_word))
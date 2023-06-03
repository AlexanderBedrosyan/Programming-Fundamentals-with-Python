def convert(word):
    new_word = ""
    for i in range(len(word)):
        new_word += (word[i] * len(word[i]))
    return new_word


current_word = input().split(" ")
print(convert(current_word))

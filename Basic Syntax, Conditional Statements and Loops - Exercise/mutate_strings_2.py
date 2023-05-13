def mutate_string(word1, word2):
    for ind in range(len(word1)):
        if word1[ind] != word2[ind]:
            word1 = word1[:ind] + word2[ind] + word1[ind + 1:]
            print(word1)


first_word = input()
second_word = input()
mutate_string(first_word, second_word)

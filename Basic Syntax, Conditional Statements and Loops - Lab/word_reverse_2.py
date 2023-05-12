def word_reverse(word):
    final_word = ''
    for ch in word[::-1]:
        final_word += ch

    return final_word


word = input()
final_word = word_reverse(word)

print(final_word)
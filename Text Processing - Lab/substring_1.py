def substring(sub_word, word):
    new_word = word
    while sub_word in new_word:
        new_word = new_word.replace(sub_word, "")

    return new_word


checking_word = input()
final_word = input()
print(substring(checking_word, final_word))

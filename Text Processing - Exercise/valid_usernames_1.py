def valid_usernames(word):
    new_word = []
    checking_word = True
    symbols = ["-", "_"]

    for i in range(len(word)):
        if 3 > len(word[i]) or len(word[i]) > 16:
            continue

        for letter in word[i]:
            if (letter not in symbols) and (not letter.isdigit()) and (not letter.isalpha()):
                checking_word = False
                break

        if checking_word:
            new_word.append(word[i])
        else:
            checking_word = True

    return new_word


text = input().split(", ")

print(*valid_usernames(text), sep="\n")
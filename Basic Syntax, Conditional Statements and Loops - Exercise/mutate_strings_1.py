word = input()
new_word = input()

list_word = list(word)

for i in range(0, len(word)):
    if new_word[i] != list_word[i]:
        list_word[i] = new_word[i]
        print(*list_word, sep="")
    else:
        continue

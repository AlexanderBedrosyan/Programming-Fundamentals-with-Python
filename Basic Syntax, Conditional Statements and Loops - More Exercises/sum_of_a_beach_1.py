word = input().lower()
new_word = ""

counter = 0

for i in range(0, len(word)):
    new_word += word[i]
    if "sand" in new_word:
        counter += 1
        new_word = ""
    elif "sun" in new_word:
        counter += 1
        new_word = ""
    elif "water" in new_word:
        counter += 1
        new_word = ""
    elif "fish" in new_word:
        counter += 1
        new_word = ""

print(counter)

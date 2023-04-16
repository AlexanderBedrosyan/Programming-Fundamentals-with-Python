while True:
    word = input()
    if word == "End":
        break
    elif word == "SoftUni":
        continue

    for i in range(0, len(word)):
        if i < (len(word) - 1):
            print(word[i] * 2, end="")
        elif i == (len(word) - 1):
            print(word[i] * 2)

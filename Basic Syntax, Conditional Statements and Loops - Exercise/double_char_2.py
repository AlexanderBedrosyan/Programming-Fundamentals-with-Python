def double_char():
    while True:
        current_word = ''
        sentence = input()
        if sentence == "End":
            break
        if sentence != "SoftUni":
            for ch in sentence:
                current_word += (2 * ch)
            print(current_word)


double_char()
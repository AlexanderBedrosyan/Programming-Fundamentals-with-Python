def split_symbols(single_string):
    digits = []
    letters = []
    others = []
    for i in single_string:
        if i.isdigit():
            digits.append(i)
        elif i.isalpha():
            letters.append(i)
        else:
            others.append(i)
    return f"{''.join(digits)}\n{''.join(letters)}\n{''.join(others)}"


word = input()
print(split_symbols(word))

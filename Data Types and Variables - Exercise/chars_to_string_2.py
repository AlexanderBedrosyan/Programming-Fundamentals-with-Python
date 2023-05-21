def concatenate_strings(list):
    word = ''
    for ch in list:
        word += ch
    return word


chars = [input() for _ in range(3)]
print(concatenate_strings(chars))

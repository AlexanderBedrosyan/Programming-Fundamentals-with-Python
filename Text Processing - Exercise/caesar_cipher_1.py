def encrypted_message(text):
    new_word = []
    for letter in text:
        new_letter = ord(letter) + 3
        new_word.append(chr(new_letter))

    return f"{''.join(new_word)}"


code = input()

print(encrypted_message(code))
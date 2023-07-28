def find_the_right_letter(func):
    def wrapper(word):
        new_word = ''
        for ch in word:
            new_word += chr(ord(ch) + 3)
        return new_word
    return wrapper


@find_the_right_letter
def encrypted_version(current_text):
    return text


text = input()
print(encrypted_version(text))

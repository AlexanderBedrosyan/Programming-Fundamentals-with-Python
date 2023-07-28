def find_no_repeating_text(func):
    def wrapper(text):
        word = ''
        for ch in text:
            if word and ch == word[-1]:
                continue
            word += ch
        return word
    return wrapper


@find_no_repeating_text
def no_repeating_letters(text):
    return text


word = [ch for ch in input()]
print(no_repeating_letters(word))

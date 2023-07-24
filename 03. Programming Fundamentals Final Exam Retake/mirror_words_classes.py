import re


def decorator(func):
    def wrapper(text):
        first_sentence = ''
        result = []
        pattern = r'([\#\@])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
        matches = re.findall(pattern, text)
        for ch in matches:
            if ch[1] == ch[2][::-1]:
                result.append(f"{ch[1]} <=> {ch[2]}")
        if not matches:
            first_sentence = "No word pairs found!" + '\n'
        else:
            first_sentence = f"{len(matches)} word pairs found!" + '\n'

        if not result:
            first_sentence += "No mirror words!"
        else:
            first_sentence += "The mirror words are:"
        return f"{first_sentence}\n" + f"{', '.join(result)}"
    return wrapper


@decorator
def final_result(word):
    return word


print(final_result(input()))

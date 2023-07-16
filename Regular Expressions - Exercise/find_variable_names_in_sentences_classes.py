import re


def correct_word(func):
    def wrapper(current_string):
        pattern = r'\b_{1}[a-zA-Z]+\b'
        matches = re.findall(pattern, current_string)
        for i in range(len(matches)):
            matches[i] = matches[i].replace("_","")
        return ','.join(matches)
    return wrapper


@correct_word
def final_result(word):
    return word


print(final_result(input()))

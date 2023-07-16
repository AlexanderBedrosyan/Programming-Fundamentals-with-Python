import re


def count_times(func):
    def wrapper(needed_word, sentence):
        pattern = fr'\b{needed_word}\b'
        matches = re.findall(pattern, sentence, re.IGNORECASE)
        return len(matches)
    return wrapper


@count_times
def find_the_result(word, sentence):
    return word


sentence_looking = input()
needed_word = input()

print(find_the_result(needed_word, sentence_looking))

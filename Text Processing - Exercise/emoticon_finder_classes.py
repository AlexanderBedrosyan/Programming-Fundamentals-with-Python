def emoticon_finder(func):
    def wrapper(current_word):
        result = []
        while ":" in current_word:
            ind = current_word.index(":")
            if ind == (len(current_word) - 1):
                break
            result.append(current_word[ind:ind + 2])
            current_word = current_word[ind + 1:]
        return '\n'.join(result)
    return wrapper


@emoticon_finder
def find_emoticon(words):
    return words


text = input()
print(find_emoticon(text))

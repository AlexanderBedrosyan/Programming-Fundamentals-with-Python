def correct_word(func):
    def wrapper(*args):
        new_word = []
        checking_word = True
        symbols = ["-", "_"]

        for i in range(len(args[0])):
            if 3 > len(args[0][i]) or len(args[0][i]) > 16:
                continue

            for letter in args[0][i]:
                if (letter not in symbols) and (not letter.isdigit()) and (not letter.isalpha()):
                    checking_word = False
                    break

            if checking_word:
                new_word.append(args[0][i])
            else:
                checking_word = True

        return new_word
    return wrapper


@correct_word
def find_the_words(list_of_words):
    return list_of_words


text = input().split(", ")
print(*find_the_words(text), sep='\n')

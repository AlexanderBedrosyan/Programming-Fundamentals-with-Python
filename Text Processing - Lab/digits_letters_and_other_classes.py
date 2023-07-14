def change_the_result(func):
    def wrapper(*args):
        digits = ''
        strings = ''
        symbols = ''
        for ch in args[0]:
            if ch.isnumeric():
                digits += ch
            elif ch.isalpha():
                strings += ch
            else:
                symbols += ch
        return f"{digits}\n{strings}\n{symbols}"
    return wrapper


@change_the_result
def final_result(word):
    return f"{word}"


current_string = input()
print(final_result(current_string))

def translate(text, char, replacement):
    new_char = text.replace(char, replacement)
    print(new_char)
    return new_char


def includes(text, substring):
    print("True" if substring in text else "False")
    return text


def start(text, substring):
    print("True" if text.startswith(substring) else "False")
    return text


def lowercase(text):
    new_text = text.lower()
    print(new_text)
    return new_text


def find_index(text, char):
    for i in range(len(text) - 1, - 1, - 1):
        if text[i] == char:
            print(i)
            break
    return text


def remove(text, start_index, count):
    new_text = text[:start_index] + text[start_index + count:]
    print(new_text)
    return new_text


word = input()

command = input()

while command != "End":
    option, *args = command.split(" ")

    if option == "Translate":
        word = translate(word, args[0], args[1])
    elif option == "Includes":
        word = includes(word, args[0])
    elif option == "Start":
        word = start(word, args[0])
    elif option == "Lowercase":
        word = lowercase(word)
    elif option == "FindIndex":
        word = find_index(word, args[0])
    elif option == "Remove":
        word = remove(word, int(args[0]), int(args[1]))

    command = input()

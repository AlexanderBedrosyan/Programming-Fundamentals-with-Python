def takeodd(word):
    new_word = ""
    for i in range(len(word)):
        if i % 2 != 0:
            new_word += word[i]
    return new_word


def cut(word, index, lenght):
    return word[0:index] + word[index + lenght:]


def substitute(word, old_string, new_string):
    if old_string in word:
        return word.replace(old_string, new_string), ""
    else:
        return word, "Nothing to replace!"


password = input()

while True:
    command = input()

    if command == "Done":
        break

    if " " not in command:
        password = takeodd(password)
        print(password)
    else:
        new_command = command.split(" ")
        if new_command[0] == "Cut":
            password = cut(password, int(new_command[1]), int(new_command[2]))
            print(password)
        elif new_command[0] == "Substitute":
            password, message = substitute(password, new_command[1], new_command[2])
            if len(message) > 1:
                print(message)
            else:
                print(password)

print(f"Your password is: {password}")
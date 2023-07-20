def insertspace(word, index):
    return word[:index] + " " + word[index:]


def reverse(word, substring):
    word = word.replace(substring, "", 1)
    return word + substring[::-1]


def changeall(word, old_text, new_text):
    if old_text in word:
        return word.replace(old_text, new_text)
    else:
        return word


message = input()

while True:
    command = input()

    if command == "Reveal":
        break

    new_command = command.split(":|:")

    if new_command[0] == "InsertSpace":
        index = int(new_command[1])
        message = insertspace(message, index)
        print(message)
    elif new_command[0] == "Reverse":
        substring = new_command[1]
        if substring in message:
            message = reverse(message, substring)
            print(message)
        else:
            print("error")
    elif new_command[0] == "ChangeAll":
        substring = new_command[1]
        replacement = new_command[2]
        message = changeall(message, substring, replacement)
        print(message)

print(f"You have a new text message: {message}")
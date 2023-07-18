def move(message, numbers):
    new_letters = message[:numbers]
    current_message = message.replace(new_letters, "")
    final_message = current_message + new_letters
    return final_message


def insert(message, indx, value):
    current_message = list(message)
    current_message.insert(indx, value)
    return ''.join(current_message)


def ChangeAll(message, old, new):
    current_message = message.replace(old, new)
    return current_message


message = input()

while True:
    command = input()
    if command == "Decode":
        break

    current_command = command.split("|")

    if current_command[0] == "Move":
        message = move(message, int(current_command[1]))
    elif current_command[0] == "Insert":
        message = insert(message, int(current_command[1]), current_command[2])
    elif current_command[0] == "ChangeAll":
        message = ChangeAll(message, current_command[1], current_command[2])

print(f"The decrypted message is: {message}")
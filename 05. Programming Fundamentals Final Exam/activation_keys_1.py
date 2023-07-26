def contains(the_string, substring):
    if substring in the_string:
        return f"{the_string} contains {substring}"
    return "Substring not found!"


def flip(the_string, position, start_index, end_index):
    if position == "Upper":
        new_word = the_string[start_index:end_index].upper()
        return the_string[:start_index] + new_word + the_string[end_index:]
    elif position == "Lower":
        new_word = the_string[start_index:end_index].lower()
        return the_string[:start_index] + new_word + the_string[end_index:]


def slice_the_string(the_string, start_index, end_index):
    return the_string[:start_index] + the_string[end_index:]


activation_key = input()

command = input()

while command != "Generate":
    current_command = command.split(">>>")

    if current_command[0] == "Contains":
        print(contains(activation_key, current_command[1]))
    elif current_command[0] == "Flip":
        activation_key = flip(activation_key, current_command[1], int(current_command[2]), int(current_command[3]))
        print(activation_key)
    elif current_command[0] == "Slice":
        activation_key = slice_the_string(activation_key, int(current_command[1]), int(current_command[2]))
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")

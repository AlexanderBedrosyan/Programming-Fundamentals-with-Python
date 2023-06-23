def fill_the_lists(message, starting_list, even_list, odd_list):
    counter = 0
    for ch in message:
        if not ch.isdigit():
            starting_list.append(ch)
        else:
            if counter % 2 == 0:
                even_list.append(int(ch))
            else:
                odd_list.append(int(ch))
            counter += 1
    return starting_list, even_list, odd_list


def find_the_message(current_message, take_list, skip_list):
    final_message = ''
    string_message = ''.join(current_message)
    for i in range(len(take_list)):
        if take_list[i] > 0:
            final_message += string_message[0:take_list[i]]
            string_message = string_message[take_list[i]:]
        if skip_list[i] > 0:
            string_message = string_message[skip_list[i]:]
    return final_message


message = input()
hidden_message = []
take_list = []
skip_list = []

hidden_message, take_list, skip_list = fill_the_lists(message, hidden_message, take_list, skip_list)
print(find_the_message(hidden_message, take_list, skip_list))

def message(dict, number):
    if number in dict:
        return dict[number]
    elif number > max(dict):
        return "Bye."
    else:
        return "GREAT!"


message_dict = {88: "Hello", 86: "How are you?"}
num = int(input())

for i in range(num):
    print(message(message_dict, int(input())))
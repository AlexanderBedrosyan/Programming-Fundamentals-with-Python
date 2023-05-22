def filter(num, searching_word):
    full_list = []
    searching_list = []
    for ch in range(num):
        current_string = input()
        full_list.append(current_string)
        if searching_word in current_string:
            searching_list.append(current_string)
    print(full_list)
    print(searching_list)


num = int(input())
searching_word = input()
filter(num, searching_word)
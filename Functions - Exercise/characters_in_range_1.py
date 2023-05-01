symbol_one = input()
symbol_two = input()


def ascii_symbol():
    ascii_list = []
    for item in range(ord(symbol_one) + 1, ord(symbol_two)):
        ascii_list.append(chr(item))
    return print(*ascii_list, sep=" ")


ascii_symbol()

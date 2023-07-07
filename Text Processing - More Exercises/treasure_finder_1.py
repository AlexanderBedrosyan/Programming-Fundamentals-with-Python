def original_text(text_list, code):
    code_counter = -1
    original_text = ""

    for i in range(len(text_list)):
        code_counter += 1
        original_text += chr(ord(text_list[i]) - int(code[code_counter]))
        if len(code) - 1 == code_counter:
            code_counter = -1

    return original_text


def find_treasure(new_text_list):
    type_counter = 0
    coordinates_counter = 0
    type = ""
    coordinates = ""
    for ch in new_text_list:
        if ch == "&":
            type_counter += 1
        if ch == "<" or ch == ">":
            coordinates_counter += 1
        if 0 < type_counter < 2:
            type += ch
        if 0 < coordinates_counter < 2:
            coordinates += ch

    return type[1::], coordinates[1::]


decreasing_list = [int(ch) for ch in input().split(" ")]

while True:
    text = input()
    if text == "find":
        break

    text_list = [str(ch) for ch in text]
    new_text = [str(ch) for ch in original_text(text_list, decreasing_list)]

    type, coordinates = find_treasure(new_text)

    print(f"Found {type} at {coordinates}")
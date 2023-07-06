def finding_name(text):
    name_found = False
    new_name = ""
    for i in range(len(text)):
        if text[i] == "|":
            name_found = False
            break
        if name_found:
            new_name += text[i]
        if text[i] == "@":
            name_found = True
    return new_name


def finding_age(text):
    age_found = False
    new_age = ""
    for i in range(len(text)):
        if text[i] == "*":
            age_found = False
            break
        if age_found:
            new_age += text[i]
        if text[i] == "#":
            age_found= True
    return new_age


num = int(input())

for i in range(num):
    list_text = [str(ch) for ch in input()]

    name = finding_name(list_text)
    age = finding_age(list_text)

    print(f"{name} is {age} years old.")
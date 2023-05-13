def if_pure_string(num):
    for i in range(num):
        sentence = input()
        if "," not in sentence and "." not in sentence and "_" not in sentence:
            print(f"{sentence} is pure.")
        else:
            print(f"{sentence} is not pure!")


if_pure_string(int(input()))
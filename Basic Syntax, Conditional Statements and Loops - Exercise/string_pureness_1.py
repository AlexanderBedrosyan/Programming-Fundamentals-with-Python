n = int(input())

not_pure = [",", ".", "_"]
pure = True

for i in range(0, n):
    string = input()

    for letter in range(0, len(string)):
        if string[letter] not in not_pure:
            pure = True
            continue
        elif string[letter] in not_pure:
            pure = False
            print(f"{string} is not pure!")
            break

    if pure:
        print(f"{string} is pure.")

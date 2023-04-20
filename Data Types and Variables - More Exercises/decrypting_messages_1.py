key_number = int(input())
rows = int(input())

word = ""

for i in range(1, rows + 1):
    letter = input()

    word += chr(ord(letter) + key_number)

print(word)

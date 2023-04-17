word = input()

counter = 0
number_of_capitals = []

for index, letters in enumerate(word):
    if letters == " ":
        index += 1

    elif letters == letters.upper() and 65 <= ord(letters) <= 90:
        number_of_capitals.append(index)

print(number_of_capitals)

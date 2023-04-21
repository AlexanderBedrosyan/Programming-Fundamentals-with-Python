n = int(input())
key_word = input()

list_of_strings = []
list_of_strings_with_key_word = []

for i in range(n):
    strings = input()

    if key_word in strings:
        list_of_strings_with_key_word.append(strings)

    list_of_strings.append(strings)

print(list_of_strings)
print(list_of_strings_with_key_word)

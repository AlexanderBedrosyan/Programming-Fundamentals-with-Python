import re

pattern = r'([#@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

word = input()
new_word = re.findall(pattern, word)
match_dict = {}

if len(new_word) == 0:
    print("No word pairs found!")
else:
    print(f"{len(new_word)} word pairs found!")
    for i in range(len(new_word)):
        if new_word[i][1] == new_word[i][2][::-1]:
            match_dict[new_word[i][1]] = new_word[i][2]

if len(match_dict) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    final_list = []
    for ch in match_dict:
        final_list.append(f"{ch} <=> {match_dict[ch]}")
    print(*final_list, sep=", ")
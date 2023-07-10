import re

word = input()
searching_word = input()
pattern_type = ""

for i in searching_word:
    current_word = f"[{i.upper()}{i.lower()}]"
    pattern_type += current_word

pattern = fr"\b{pattern_type}\b"
word_list = re.findall(pattern, word)

print(len(word_list))

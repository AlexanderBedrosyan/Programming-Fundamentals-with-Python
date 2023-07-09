import re

pattern = r'[0-9]+'

while True:
    old_text = input()
    if len(old_text) == 0:
        break

    text = re.findall(pattern, old_text)
    if len(text) > 0:
        print(*text, end=" ")

import re

word = input()
pattern = r"(:?^|\s)([a-zA-Z0-9]+[\.\-\_]?[a-zA-Z0-9]+)(@[a-zA-Z]+[-]?[a-zA-Z]+)(\.[a-zA-Z]+[-]?[a-zA-Z]+)+\b"
matches = re.finditer(pattern, word)

for ch in matches:
    print(ch.group().strip())

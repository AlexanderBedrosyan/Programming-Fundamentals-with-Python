import re

pattern = r'\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b'

numbers = input()

valid_numbers = re.findall(pattern, numbers)

print(*valid_numbers, sep=", ")
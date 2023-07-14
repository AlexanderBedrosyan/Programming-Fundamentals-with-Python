import re

pattern = r'(^|(?<=\s))-?([0]|[0-9][0-9]*)(\.?[0-9]+)?($|(?=\s))'
matches = re.finditer(pattern, input())

for match in matches:
    print(match.group(), end=" ")


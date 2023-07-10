import re

pattern = r'(\www\.\b)([A-Za-z0-9\-]+)(\.[a-z]{1,})+'
links = []

while True:
    command = input()

    if len(command) == 0:
        break

    correct_emails = re.finditer(pattern, command)

    for link in correct_emails:
        links.append(link.group())

print(*links, sep="\n")
import re

word = input()
current_word = word.replace("\\n", "")

title_pattern = r'<title>[^\/]+<\/title>'
body_pattern = r'<body>[ -~]+<\/body>'
checking_title = re.findall(title_pattern, current_word)
checking_body = re.findall(body_pattern, current_word)

title = ""
body = ""
typing_word = False

for ch in checking_title[0]:
    if ch == "<":
        typing_word = False
    if typing_word:
        title += ch
    if ch == ">":
        index = checking_title[0].index(ch)
        if checking_title[0][index + 1] != "<" and len(checking_title[0]) >= (index + 1):
            typing_word = True


for ch in checking_body[0]:
    if ch == "<":
        typing_word = False
    if typing_word:
        body += ch
    if ch == ">":
        index = checking_title[0].index(ch)
        if checking_body[0][index + 1] != "<" and len(checking_body[0]) >= (index + 1):
            typing_word = True

print(f"Title: {title}")
print(f"Content: {body}")

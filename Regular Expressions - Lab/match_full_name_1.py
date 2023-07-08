import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

final_text = re.findall(patern, text)

print(*final_text)
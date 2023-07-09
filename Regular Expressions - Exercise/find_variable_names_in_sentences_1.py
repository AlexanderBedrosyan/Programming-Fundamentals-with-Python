import re

pattern = r'\b_[a-zA-Z0-9]+\b'

valid_names = re.findall(pattern, input())
final_names = []
for i in valid_names:
    current_names = i.replace("_","")
    final_names.append(current_names)

print(*final_names, sep=",")

import re

pattern = r'\b([0-9]{2})([\/.-])([A-Z][a-z]{2})\2([0-9]{4})\b'

dates = input()
correct_dates = re.findall(pattern, dates)

for i in correct_dates:
    print(f"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}")
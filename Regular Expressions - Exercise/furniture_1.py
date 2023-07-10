import re

pattern = r'>>([A-Za-z]+)<<([0-9]+[\.]?[0-9]{2}?)!([0-9]+)'


total_amount = 0
furniture = []

while True:
    command = input()
    if command == "Purchase":
        break
    correct_data = re.findall(pattern, command)

    for i in correct_data:
        furniture.append(i[0])
        total_amount += (float(i[1]) * int(i[2]))

print("Bought furniture:")
for ch in furniture:
    print(ch)
print(f"Total money spend: {total_amount:.2f}")

ticket = 150
clothes_max = 50
shoes_max = 35
accessories_max = 20

items = input()
budget = float(input())

items_list = [str(ch) for ch in items.strip().split("|")]

total_price = 0
new_number = 0
new_list = []

for i in range(len(items_list)):
    type_list = [str(chart) for chart in items_list[i].strip().split("->")]
    if float(type_list[1]) >= 0:
        if (type_list[0] == "Clothes") and (float(type_list[1]) <= clothes_max) and (float(type_list[1]) <= budget):
            budget -= float(type_list[1])
            total_price += float(type_list[1])
            new_number = f"{float(type_list[1]) * 1.40:.2f}"
            new_list.append(new_number)
            new_number = 0
        elif (type_list[0] == "Shoes") and (float(type_list[1]) <= shoes_max) and (float(type_list[1]) <= budget):
            budget -= float(type_list[1])
            total_price += float(type_list[1])
            new_number = f"{float(type_list[1]) * 1.40:.2f}"
            new_list.append(new_number)
            new_number = 0
        elif (type_list[0] == "Accessories") and (float(type_list[1]) <= accessories_max) and (float(type_list[1]) <= budget):
            budget -= float(type_list[1])
            total_price += float(type_list[1])
            new_number = f"{float(type_list[1]) * 1.40:.2f}"
            new_list.append(new_number)
            new_number = 0
        else:
            continue
    else:
        continue

print(*new_list, sep=" ")
print(f"Profit: {total_price * 0.40:.2f}")
if (total_price * 1.40 + budget) >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

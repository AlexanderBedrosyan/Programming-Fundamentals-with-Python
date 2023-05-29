def is_correct_amount(item_dict, current_item, amount, budget):
    flag = False
    if amount <= item_dict[current_item] and amount <= budget:
        flag = True
    return flag


def calculation_budget_items(amount, total_amount, budget, cells_list, profit):
    new_amount = amount * 1.40
    budget -= amount
    total_amount += new_amount
    cells_list.append(new_amount)
    profit += (new_amount - amount)
    return total_amount, budget, cells_list, profit


type_maximum_price = {"Clothes": 50, "Shoes": 35, "Accessories": 20.50}
ticket_cost = 150
items_total_amount = 0
items = input().split("|")
budget = int(input())
list_of_cells = []
profit = 0

for i in range(len(items)):
    item, amount = items[i].split("->")
    if is_correct_amount(type_maximum_price, item, float(amount), budget):
        items_total_amount, budget, list_of_cells, profit = calculation_budget_items(float(amount), items_total_amount,
                                                                             budget, list_of_cells, profit)

print(' '.join(str(f"{ch:.2f}") for ch in list_of_cells))
print(f"Profit: {profit:.2f}")
if (budget + items_total_amount) >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")

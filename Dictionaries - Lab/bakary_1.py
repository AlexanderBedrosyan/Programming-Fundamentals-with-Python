food_list = [ch for ch in input().split()]
bakery = {}

for i in range(0, len(food_list), 2):
    keys = food_list[i]
    values = int(food_list[i + 1])
    bakery[keys] = values

print(bakery)
food_list = [ch for ch in input().split()]
checking_list = [ch for ch in input().split()]
bakery = {}

for i in range(0, len(food_list), 2):
    keys = food_list[i]
    values = int(food_list[i + 1])
    bakery[keys] = values

for item in checking_list:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
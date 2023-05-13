def cost_spirit_function(dict, quantity, days):
    total_cost = 0
    total_spirit = 0
    for i in range(1, days + 1):
        if i % 11 == 0:
            quantity += 2
        if i % 2 == 0:
            decoration = "Ornament Set"
            total_cost += (dict[decoration][0] * quantity)
            total_spirit += dict[decoration][1]
        if i % 3 == 0:
            decoration = "Tree Skirt"
            decoration2 = "Tree Garland"
            total_cost += (dict[decoration][0] + dict[decoration2][0]) * quantity
            total_spirit += (dict[decoration][1] + dict[decoration2][1])
        if i % 5 == 0:
            decoration = "Tree Lights"
            total_cost += (dict[decoration][0] * quantity)
            total_spirit += dict[decoration][1]
        if i % 15 == 0:
            total_spirit += 30
        if i % 10 == 0:
            total_spirit -= 20
            total_cost += (dict["Tree Skirt"][0] + dict["Tree Garland"][0] + dict["Tree Lights"][0])
            if i == days:
                total_spirit -= 30
    return total_cost, total_spirit


decoration_dict = {
    "Ornament Set": [2, 5],
    "Tree Skirt": [5, 3],
    "Tree Garland": [3, 10],
    "Tree Lights": [15, 17]
}
quantity = int(input())
days = int(input())

total_cost, total_spirit = cost_spirit_function(decoration_dict, quantity, days)

print(f"Total cost: {total_cost}\nTotal spirit: {total_spirit}")

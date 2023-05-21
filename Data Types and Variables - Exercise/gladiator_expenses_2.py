def total_amount(n, helmet_price, sword_price, shield_price, armor_price):
    helmet = 0
    sword = 0
    shield = 0
    armor = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            helmet += 1
        if i % 3 == 0:
            sword += 1
        if (i % 3 == 0) and (i % 2 == 0):
            shield += 1
            if shield % 2 == 0:
                armor += 1

    total_amount = helmet * helmet_price + sword * sword_price + shield * shield_price + armor * armor_price
    return f"Gladiator expenses: {total_amount:.2f} aureus"


print(total_amount(int(input()), float(input()), float(input()), float(input()), float(input())))

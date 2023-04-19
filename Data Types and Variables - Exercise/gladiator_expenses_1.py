n = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

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

print(f"Gladiator expenses: {total_amount:.2f} aureus")

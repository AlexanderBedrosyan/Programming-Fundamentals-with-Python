group_size = int(input())
days = int(input())

total_amount = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5

    total_amount += (50 - group_size * 2)

    if i % 3 == 0:
        total_amount -= (group_size * 3)

    if i % 5 == 0:
        if i % 3 == 0:
            total_amount += (20 * group_size - 2 * group_size)
        else:
            total_amount += (20 * group_size)

print(f"{group_size} companions received {int(total_amount / group_size)} coins each.")

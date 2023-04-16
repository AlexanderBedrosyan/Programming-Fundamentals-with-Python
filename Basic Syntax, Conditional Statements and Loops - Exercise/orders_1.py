n = int(input())

total_price = 0

for i in range(1, n + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    if 1 > days or days > 31:
        continue
    if 1 > capsules_per_day or capsules_per_day > 2000:
        continue

    total_price += (price_per_capsule * capsules_per_day) * days
    current_price = (price_per_capsule * capsules_per_day) * days

    print(f"The price for the coffee is: ${current_price:.2f}")
    current_price = 0

print(f"Total: ${total_price:.2f}")

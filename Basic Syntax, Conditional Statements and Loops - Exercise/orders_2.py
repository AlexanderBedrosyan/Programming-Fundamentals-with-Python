def price_for_the_coffee(num):
    total = 0
    for i in range(num):
        price_per_capsule = float(input())
        days = int(input())
        capsules = int(input())
        if 0.01 > price_per_capsule or price_per_capsule > 100:
            continue
        if 1 > days or days > 31:
            continue
        if 1 > capsules or capsules > 2000:
            continue
        current_total = (price_per_capsule * capsules) * days
        print(f"The price for the coffee is: ${current_total:.2f}")
        total += current_total
    return total


orders = int(input())
total = price_for_the_coffee(orders)
print(f"Total: ${total:.2f}")

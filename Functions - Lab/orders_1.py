def total_price():
    if order == "coffee":
        price = 1.50
    elif order == "water":
        price = 1
    elif order == "coke":
        price = 1.40
    elif order == "snacks":
        price = 2

    return f"{quantity * price:.2f}"


order = input()
quantity = int(input())

print(total_price())

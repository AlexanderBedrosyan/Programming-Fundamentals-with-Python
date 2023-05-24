bakery = {}

while True:
    command = input()

    if command == "statistics":
        break

    product, quantity = command.split(": ")

    if product in bakery:
        bakery[product] += int(quantity)
    else:
        bakery[product] = int(quantity)

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")
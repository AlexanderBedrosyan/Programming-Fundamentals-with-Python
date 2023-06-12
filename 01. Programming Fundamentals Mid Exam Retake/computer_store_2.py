def special(current_list):
    sum_without_taxes = sum(current_list)
    taxes = sum_without_taxes * 0.20
    total_price = (sum_without_taxes + taxes) * 0.90
    return sum_without_taxes, taxes, total_price


def regular(current_list):
    sum_without_taxes = sum(current_list)
    taxes = sum_without_taxes * 0.20
    total_price = sum_without_taxes + taxes
    return sum_without_taxes, taxes, total_price


prices = []
condition = ''
sum_without_taxes, taxes, total_price = 0, 0, 0

while True:
    current_price = input()

    if current_price.isalpha():
        condition = current_price
        break

    current_price = float(current_price)

    if current_price < 0:
        print("Invalid price!")
        continue

    prices.append(current_price)

if condition == "special":
    sum_without_taxes, taxes, total_price = special(prices)
elif condition == "regular":
    sum_without_taxes, taxes, total_price = regular(prices)

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

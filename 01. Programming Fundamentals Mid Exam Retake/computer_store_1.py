total_price_net_price = 0

while True:
    n = input()
    if n == "special" or n == "regular":
        if total_price_net_price == 0:
            print("Invalid order!")
            break
        else:
            if n == "special":
                tax = total_price_net_price * 0.20
                total_amount = (total_price_net_price + tax) * 0.90
                print("Congratulations you've just bought a new computer!")
                print(f"Price without taxes: {total_price_net_price:.2f}$")
                print(f"Taxes: {tax:.2f}$\n-----------\nTotal price: {total_amount:.2f}$")
                break
            else:
                tax = total_price_net_price * 0.20
                total_amount = total_price_net_price + tax
                print("Congratulations you've just bought a new computer!")
                print(f"Price without taxes: {total_price_net_price:.2f}$")
                print(f"Taxes: {tax:.2f}$\n-----------\nTotal price: {total_amount:.2f}$")
                break
    elif float(n) < 0:
        print("Invalid price!")
        continue
    elif float(n) == 0:
        print("Invalid order!")
        continue
    else:
        total_price_net_price += float(n)
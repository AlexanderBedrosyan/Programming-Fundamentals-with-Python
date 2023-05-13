def eggs_milk_prices(flour_price):
    eggs = flour_price * 0.75
    milk = (flour_price * 1.25) / 4
    return eggs, milk


def final_result(budget, price_per_loaf):
    loaves_count = 0
    colored_eggs = 0
    while True:
        budget -= price_per_loaf
        if budget < 0:
            budget += price_per_loaf
            break

        loaves_count += 1
        colored_eggs += 3

        if loaves_count % 3 == 0:
            colored_eggs -= (loaves_count - 2)

    return loaves_count, colored_eggs, budget


budget = float(input())
flour = float(input())
eggs_price, milk_price = eggs_milk_prices(flour)
loaf_price = flour + eggs_price + milk_price

loaves_count, colored_eggs, money_left = final_result(budget, loaf_price)

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
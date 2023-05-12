def total_amount(budget, product_price):
    budget -= product_price
    return budget


def if_positive(budget):
    if budget >= 0:
        return True
    else:
        return False


def calculation_loop(budget):
    while True:
        product_price = input()
        if product_price == "End":
            print("You bought everything needed.")
            break

        budget = total_amount(budget, int(product_price))

        if if_positive(budget):
            continue
        else:
            print("You went in overdraft!")
            break


budget = int(input())

calculation_loop(budget)

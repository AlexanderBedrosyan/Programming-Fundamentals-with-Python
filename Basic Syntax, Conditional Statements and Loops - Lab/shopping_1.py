budget = int(input())

total_sum = 0

while True:
    product_amount = input()

    if product_amount == "End":
        print("You bought everything needed.")
        break
    else:
        product_amount = int(product_amount)

    if total_sum + product_amount > budget:
        print("You went in overdraft!")
        break
    else:
        total_sum += product_amount

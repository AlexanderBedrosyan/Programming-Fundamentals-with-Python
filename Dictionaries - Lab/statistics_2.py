def asked_for_statistics(statistics):
    print("Products in stock:")
    total_products = 0
    total_quantities = 0
    for key, values in statistics.items():
        total_products += 1
        total_quantities += values
        print(f"- {key}: {values}")
    print(f"Total Products: {total_products}")
    print(f"Total Quantity: {total_quantities}")


def products_in_stock():
    statistics_dict = {}
    command = input()

    while command != "statistics":
        product, quantity = command.split(": ")
        if product not in statistics_dict:
            statistics_dict[product] = 0
        statistics_dict[product] += int(quantity)
        command = input()

    asked_for_statistics(statistics_dict)


products_in_stock()

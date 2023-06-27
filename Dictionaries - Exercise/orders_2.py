class GetTheOrder():

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def create_the_orders(self):
        orders_dict = {}
        for elements in self.list_of_products:
            product, price, quantity = elements.split(" ")
            if product not in orders_dict:
                orders_dict[product] = {}
            if not orders_dict[product]:
                orders_dict[product][float(price)] = float(quantity)
                continue
            for key, value in orders_dict[product].items():
                new_value = new_value = value + float(quantity)
                orders_dict[product] = {}
                orders_dict[product][float(price)] = new_value
        return orders_dict

    def __repr__(self):
        final_result = []
        for product, information in self.create_the_orders().items():
            for price, quantity in self.create_the_orders()[product].items():
                final_result.append(f"{product} -> {price * quantity:.2f}")
        return '\n'.join(final_result)


current_list = []
while True:
    command = input()

    if command == "buy":
        break

    current_list.append(command)

print(GetTheOrder(current_list))

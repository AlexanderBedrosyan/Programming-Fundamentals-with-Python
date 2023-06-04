menu = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
result = lambda a, b: f"{a * b:.2f}"
order = input()
quantity = int(input())

print(result(menu[order], quantity))

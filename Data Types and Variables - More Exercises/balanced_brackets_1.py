period = int(input())

brackets_list = []

for i in range(1, period + 1):
    symbol = input()

    if (symbol == "(") or (symbol == ")"):
        brackets_list.append(symbol)

    if len(brackets_list) == 2:
        if brackets_list[0] == "(" and brackets_list[1] == ")":
            brackets_list = []

if len(brackets_list) == 0:
    print("BALANCED")
else:
    print("UNBALANCED")

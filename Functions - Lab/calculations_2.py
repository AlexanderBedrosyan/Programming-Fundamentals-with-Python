def result(operator, n1, n2):
    if "add" == operator:
        return n1 + n2
    elif "subtract" == operator:
        return n1 - n2
    elif "multiply" == operator:
        return n1 * n2
    elif "divide" == operator:
        return int(n1 / n2)


print(result(input(), int(input()), int(input())))
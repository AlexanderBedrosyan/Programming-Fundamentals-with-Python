def act():
    if action == "multiply":
        return n1 * n2
    elif action == "divide":
        return n1 // n2
    elif action == "add":
        return n1 + n2
    elif action == "subtract":
        return n1 - n2


action = input()
n1 = int(input())
n2 = int(input())

print(act())

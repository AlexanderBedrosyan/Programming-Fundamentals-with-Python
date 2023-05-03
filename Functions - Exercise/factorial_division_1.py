def factorial_division(n1, n2):
    n1_factorial = 1
    n2_factorial = 1
    for i in range(1, n1 + 1):
        n1_factorial *= i
    for ch in range(1, n2 + 1):
        n2_factorial *= ch

    print(f"{n1_factorial / n2_factorial:.2f}")


n1 = int(input())
n2 = int(input())

factorial_division(n1, n2)

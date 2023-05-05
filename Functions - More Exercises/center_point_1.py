from math import floor

n1 = float(input())
n2 = float(input())

n3 = float(input())
n4 = float(input())

first_sum = abs(n1) + abs(n2)
second_sum = abs(n3) + abs(n4)

if first_sum <= second_sum:
    print(f"({floor(n1)}, {floor(n2)})")
else:
    print(f"({floor(n3)}, {floor(n4)})")

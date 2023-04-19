n = int(input())

capacity = 255
total_amount = 0

for i in range(1, n + 1):
    flow = int(input())

    if flow > capacity:
        print("Insufficient capacity!")
        continue

    capacity -= flow
    total_amount += flow

print(total_amount)

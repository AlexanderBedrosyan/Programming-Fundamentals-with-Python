v = int(input())
n = int(input())

all_numbers = []

for i in range(1, n + 1):
    if i % v == 0:
        all_numbers.append(i)

print(max(all_numbers))

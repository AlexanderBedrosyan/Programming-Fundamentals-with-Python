n = int(input())

for i in range(1, n + 1):
    new_number = int(input())

    if new_number % 2 != 0:
        print(f"{new_number} is odd!")
        break

    if i == n:
        print("All numbers are even.")

n = int(input())
m = int(input())

for i in range(n, m + 1):
    if i == m:
        print(chr(i))
    else:
        print(chr(i), end=" ")

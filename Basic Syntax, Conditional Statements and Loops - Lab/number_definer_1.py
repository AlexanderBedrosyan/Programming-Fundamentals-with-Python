n = float(input())

if n == 0:
    print("zero")
elif n < 0:
    if 0 < abs(n) < 1:
        print("small negative")
    elif abs(n) > 1000000:
        print("large negative")
    else:
        print("negative")
else:
    if 0 < n < 1:
        print("small positive")
    elif n > 1000000:
        print("large positive")
    else:
        print("positive")

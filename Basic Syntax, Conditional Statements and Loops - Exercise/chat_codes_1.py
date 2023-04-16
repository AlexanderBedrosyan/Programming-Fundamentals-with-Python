m = int(input())

for i in range(1, m + 1):
    n = int(input())

    if n == 88:
        print("Hello")
    elif n == 86:
        print("How are you?")
    elif n < 88 and n != 86:
        print("GREAT!")
    else:
        print("Bye.")

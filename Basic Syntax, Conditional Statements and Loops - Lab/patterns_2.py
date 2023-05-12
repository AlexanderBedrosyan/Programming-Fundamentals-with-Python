def drawing(num):
    for i in range(1, num + 1):
        print("*" * i)

    for j in range(num - 1, 0, - 1):
        print("*" * j)


number = int(input())

drawing(number)
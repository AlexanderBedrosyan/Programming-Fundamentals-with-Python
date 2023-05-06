def multiplication_sign(n1, n2, n3):
    negative = 0
    checking_list = []
    checking_list.append(n1)
    checking_list.append(n2)
    checking_list.append(n3)
    for i in range(0, 3):
        if checking_list[i] < 0:
            negative += 1
        elif checking_list[i] == 0:
            print("zero")
            exit()
    if negative == 2 or negative == 0:
        print("positive")
    else:
        print("negative")


n1 = int(input())
n2 = int(input())
n3 = int(input())

multiplication_sign(n1, n2, n3)
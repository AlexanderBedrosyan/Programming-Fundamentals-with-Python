def checker(n1):
    n1 -= electron
    return n1


def checker2(n2):
    return 0


number = int(input())
new_list = []
counter = 0

while number > 0:
    counter += 1
    electron = 2 * (counter ** 2)

    if electron <= number:
        number = checker(number)
        new_list.append(electron)
    else:
        new_list.append(number)
        number = checker2(number)


print(new_list)

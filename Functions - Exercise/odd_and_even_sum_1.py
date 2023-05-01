numbers = int(input())


def splitter(numbers):
    odd = 0
    even = 0

    while numbers > 0:
        digit = numbers % 10
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit

        numbers = (numbers - numbers % 10) // 10

    return print(f"Odd sum = {odd}, Even sum = {even}")


splitter(numbers)

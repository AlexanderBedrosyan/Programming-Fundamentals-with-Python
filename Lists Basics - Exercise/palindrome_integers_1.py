numbers = input().split(", ")

def palindrome(numbers):
    for item in range(len(numbers)):
        numbers_new = [int(ch) for ch in numbers[item]]
        print(numbers_new == list(reversed(numbers_new)))


palindrome(numbers)

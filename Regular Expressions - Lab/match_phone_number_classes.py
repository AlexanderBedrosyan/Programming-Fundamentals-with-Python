import re


def correct_number(func):
    def wrapper(numbers):
        pattern = '\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\\b'
        matches = re.findall(pattern, numbers)
        return ', '.join(str(ch) for ch in matches)
    return wrapper


@correct_number
def get_numbers(phone_numbers):
    return phone_numbers


print(get_numbers(input()))

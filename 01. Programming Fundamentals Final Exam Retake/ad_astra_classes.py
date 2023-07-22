import re

NEED_CALORIES = 2000


def decorator_of_text(func):
    def wrapper(text):
        total_amount = 0
        result = []
        pattern = r'([\#\|])([A-Za-z ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-1]?[0-9]{1,4})\1'
        matches = re.findall(pattern, text)
        for ch in matches:
            result.append(f"Item: {ch[1]}, Best before: {ch[2]}, Nutrition: {ch[3]}")
            total_amount += int(ch[3])
        days = total_amount // NEED_CALORIES
        return result, days
    return wrapper


@decorator_of_text
def find_results(text):
    return text


text_string = input()
final_result, days = find_results(text_string)
print(f"You have food to last you for: {days} days!")
print('\n'.join(final_result))

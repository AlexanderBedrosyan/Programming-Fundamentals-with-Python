import re


def correct_detector(func):
    def wrapper(word):
        pattern_letters = r"([\*]{2}|[\:]{2})([A-Z][a-z]{2,})\1"
        pattern_numbers = r'[0-9]'
        result = []

        letter_match = re.findall(pattern_letters, word)
        numbers_match = re.findall(pattern_numbers, word)
        magic_number = 1

        for ch in numbers_match:
            magic_number *= int(ch)

        result.append(f"Cool threshold: {magic_number}\n{len(letter_match)} emojis found in the text. The cool ones are:")

        for found_emoji in letter_match:
            current_result = 0

            for letter in found_emoji[1]:
                current_result += ord(letter)

            if current_result >= magic_number:
                result.append(f"{found_emoji[0]}{found_emoji[1]}{found_emoji[0]}")

        return '\n'.join(result)
    return wrapper


@correct_detector
def detector(string_for_detect):
    return string_for_detect


word = input()
print(detector(word))

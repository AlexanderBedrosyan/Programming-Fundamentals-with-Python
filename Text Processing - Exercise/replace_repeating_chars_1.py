def replace_repeating_chars(text):
    text_without_repeats = []
    current_char = ""

    for letters in text:
        if letters != current_char:
            current_char = letters
            text_without_repeats.append(current_char)

    return text_without_repeats


repeating_text = input()

print(*replace_repeating_chars(repeating_text), sep="")
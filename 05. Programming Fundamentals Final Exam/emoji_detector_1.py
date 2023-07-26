import re

word = input()
pattern = r'([\*]{2}|[\::]{2})([A-Z][a-z]{2,})\1'
matches_letters = re.findall(pattern, word)

pattern_numbers = r'[0-9]'
matches_numbers = re.findall(pattern_numbers, word)
cool_threshold = 1
final_matches = []

for ch in matches_numbers:
    cool_threshold *= int(ch)

for el in matches_letters:
    result = 0
    for ch in el[1]:
        result += ord(ch)
    if result >= cool_threshold:
        final_matches.append(f"{el[0]}{el[1]}{el[0]}")

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches_letters)} emojis found in the text. The cool ones are:")
print('\n'.join(ch.rstrip() for ch in final_matches))

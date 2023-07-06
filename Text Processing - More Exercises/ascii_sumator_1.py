first_char = input()
second_char = input()
text = input()

total_sum = 0

for ch in text:
    if ord(first_char) < ord(ch) < ord(second_char):
        total_sum += ord(ch)

print(total_sum)

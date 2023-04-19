n = int(input())

first_letter = ord("a")

for a in range(first_letter, first_letter + n):
    for b in range(first_letter, first_letter + n):
        for c in range(first_letter, first_letter + n):
            print(f"{chr(a)}{chr(b)}{chr(c)}")

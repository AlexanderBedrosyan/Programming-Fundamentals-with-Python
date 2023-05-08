word = [ch for ch in input() if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(word))

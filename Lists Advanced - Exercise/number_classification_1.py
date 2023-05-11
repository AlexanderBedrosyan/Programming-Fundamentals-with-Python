numbers = [int(item) for item in input().split(", ")]

positive = [ch for ch in numbers if ch >= 0]
negative = [ch for ch in numbers if ch < 0]
even = [ch for ch in numbers if ch % 2 == 0]
odd = [ch for ch in numbers if ch % 2 != 0]

print("Positive:", end=" ")
print(*positive, sep=", ")
print(f"Negative:", end=" ")
print(*negative, sep=", ")
print(f"Even:", end=" ")
print(*even, sep=", ")
print(f"Odd:", end=" ")
print(*odd, sep=", ")

n = int(input())

result = 0

for i in range(n):
    letter = input()
    result += ord(letter)

print(f"The sum equals: {result}")

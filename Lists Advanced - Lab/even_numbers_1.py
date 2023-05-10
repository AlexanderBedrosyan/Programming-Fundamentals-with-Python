even_list = [int(ch) for ch, index in enumerate(input().split(", ")) if int(index) % 2 == 0]

print(even_list)
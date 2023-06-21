current_list = [int(ch) for ch in input().split(", ")]
positive = ', '.join(str(ch) for ch in current_list if ch >= 0)
negative = ', '.join(str(ch) for ch in current_list if ch < 0)
even = ', '.join(str(ch) for ch in current_list if ch % 2 == 0)
odd = ', '.join(str(ch) for ch in current_list if ch % 2 != 0)

print(f"Positive: {positive}\nNegative: {negative}\nEven: {even}\nOdd: {odd}")

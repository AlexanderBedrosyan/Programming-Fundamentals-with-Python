palindrom_list = [ch for ch in input().split() if ch == ch[::-1]]
print(f"{palindrom_list}\nFound palindrome {palindrom_list.count(input())} times")
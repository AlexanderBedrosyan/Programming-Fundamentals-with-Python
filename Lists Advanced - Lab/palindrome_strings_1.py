word_list = input().split()
checking_word = input()

palindrome_list = []

for item in word_list:
    if list(item) == list(reversed(item)):
        palindrome_list.append(item)


print(palindrome_list)
print(f"Found palindrome {word_list.count(checking_word)} times")

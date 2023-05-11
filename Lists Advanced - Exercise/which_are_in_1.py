word = input().split(", ")
checking_word = input().split(", ")
final_list = []

for ch in range(len(word)):
    for i in range(len(checking_word)):
        if word[ch] in checking_word[i]:
            if word[ch] not in final_list:
                final_list.append(word[ch])

print(final_list)

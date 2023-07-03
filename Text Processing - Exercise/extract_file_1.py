list_text = input().split("\\")
new_list = list_text[-1].split(".")

print(f"File name: {new_list[0]}")
print(f"File extension: {new_list[1]}")
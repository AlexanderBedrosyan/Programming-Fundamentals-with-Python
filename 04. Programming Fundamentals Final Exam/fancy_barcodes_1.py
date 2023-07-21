import re

pattern = r'([@][#]{1,})([A-Z][a-zA-Z0-9]{4,}[A-Z])([@][#]{1,})'
num = int(input())

for i in range(num):
    word = input()
    product = ""

    if re.findall(pattern, word):
        for i in word:
            if i.isdigit():
                product += i
        if len(product) > 0:
            print(f"Product group: {product}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
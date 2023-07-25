import re


class FancyBarcodes:

    def __init__(self, number):
        self.number = number

    def product_group(self):
        product_group = '00'
        for _ in range(self.number):
            current_group = input()
            pattern = r'(\@[\#]+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@[\#]+)'
            matches = re.findall(pattern, current_group)
            if matches:
                pattern_digits = r'[0-9]'
                digit_match = re.findall(pattern_digits, matches[0][1])
                if digit_match:
                    product_group = ''.join(digit_match)
            else:
                print("Invalid barcode")
                continue
            print(f"Product group: {product_group}")
            product_group = '00'


products = FancyBarcodes(int(input()))
products.product_group()

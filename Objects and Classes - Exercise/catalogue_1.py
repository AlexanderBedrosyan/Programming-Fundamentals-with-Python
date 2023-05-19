class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        get_letter_list = []
        for i in range(len(self.products)):
            new_list = [str(ch) for ch in str(self.products[i])]
            if new_list[0] == first_letter:
                get_letter_list.append(self.products[i])
        return get_letter_list

    def __repr__(self):
        final_list = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{final_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
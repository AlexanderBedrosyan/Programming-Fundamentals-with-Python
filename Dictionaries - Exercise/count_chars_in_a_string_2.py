class CreateDictionary():

    def __init__(self, letters_list):
        self.letters_list = letters_list

    def __repr__(self):
        final_list = []
        current_dict = {}
        for ch in list_of_letters:
            if ch == " ":
                continue
            if ch not in current_dict:
                current_dict[ch] = 0
            current_dict[ch] += 1
        for letter, amount in current_dict.items():
            final_list.append(f"{letter} -> {amount}")
        return '\n'.join(final_list)


list_of_letters = [ch for ch in input()]
print(CreateDictionary(list_of_letters))

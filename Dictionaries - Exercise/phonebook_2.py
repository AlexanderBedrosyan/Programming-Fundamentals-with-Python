class GetInfoFromPhonebook():

    def __init__(self, phonebook, num_of_names):
        self.phonebook = phonebook
        self.num_of_names = num_of_names

    def __repr__(self):
        needed_info = []
        for _ in range(self.num_of_names):
            current_name = input()
            if current_name not in self.phonebook:
                needed_info.append(f"Contact {current_name} does not exist.")
            else:
                needed_info.append(f"{current_name} -> {self.phonebook[current_name]}")
        return '\n'.join(needed_info)


def phonebook():
    current_list = {}
    number = 0

    while True:
        command = input()

        if command.isdigit():
            number = int(command)
            break

        name, phone_number = command.split("-")

        current_list[name] = phone_number

    return current_list, number


phonebook_dictionary, num_of_names = phonebook()
print(GetInfoFromPhonebook(phonebook_dictionary, num_of_names))

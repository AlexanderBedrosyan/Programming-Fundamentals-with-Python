class ActivationKeys:

    def __init__(self, key):
        self.key = key
        self.result = []

    def contains(self, substring):
        if substring in self.key:
            print(f"{self.key} contains {substring}")
        else:
            print("Substring not found!")

    def flip(self, position, start_index, end_index):
        final_word = ''
        if position == "Upper":
            new_word = self.key[start_index:end_index].upper()
            final_word = self.key[:start_index] + new_word + self.key[end_index:]
        elif position == "Lower":
            new_word = self.key[start_index:end_index].lower()
            final_word = self.key[:start_index] + new_word + self.key[end_index:]
        self.key = final_word
        print(self.key)

    def slice_the_string(self, start_index, end_index):
        final_word = self.key[:start_index] + self.key[end_index:]
        self.key = final_word
        print(self.key)

    def generate_the_correct_key(self):
        command = input()

        while command != "Generate":
            command = command.split(">>>")

            if command[0] == "Contains":
                self.contains(command[1])
            elif command[0] == "Flip":
                self.flip(command[1], int(command[2]), int(command[3]))
            elif command[0] == "Slice":
                self.slice_the_string(int(command[1]), int(command[2]))

            command = input()

        print(f"Your activation key is: {self.key}")


current_word = input()
activation_key = ActivationKeys(current_word)
activation_key.generate_the_correct_key()

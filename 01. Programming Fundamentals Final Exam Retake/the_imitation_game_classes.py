class GetCode:

    def __init__(self, encrypted_message):
        self.encrypted_message = encrypted_message

    def move(self, number_of_letters):
        new_word = self.encrypted_message[number_of_letters:] + self.encrypted_message[0:number_of_letters]
        self.encrypted_message = new_word

    def insert(self, index, value):
        new_word = self.encrypted_message[:index] + value + self.encrypted_message[index:]
        self.encrypted_message = new_word

    def changeall(self, looking_symbol, changing_symbol):
        for index, letter in enumerate(self.encrypted_message):
            if letter == looking_symbol:
                new_word = self.encrypted_message[0:index] + changing_symbol + self.encrypted_message[index + 1:]
                self.encrypted_message = new_word

    def decrypt_the_message(self):
        command = input()

        while command != "Decode":
            current_command = command.split("|")
            if current_command[0] == "Move":
                self.move(int(current_command[1]))
            elif current_command[0] == "Insert":
                self.insert(int(current_command[1]), current_command[2])
            elif current_command[0] == "ChangeAll":
                self.changeall(current_command[1], current_command[2])
            command = input()

    def __repr__(self):
        return f"The decrypted message is: {self.encrypted_message}"


decrypting_app = GetCode(input())
decrypting_app.decrypt_the_message()
print(decrypting_app)
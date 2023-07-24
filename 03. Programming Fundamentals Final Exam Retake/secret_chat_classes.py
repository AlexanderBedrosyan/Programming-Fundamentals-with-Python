class SolveTheChat:

    def __init__(self, message):
        self.message = message

    def insertspace(self, index):
        new_message = self.message[0:index] + ' ' + self.message[index:]
        self.message = new_message
        print(self.message)

    def reverse(self, word):
        if word in self.message:
            new_word = self.message.replace(word, "", 1)
            self.message = new_word + word[::-1]
            print(self.message)
        else:
            print("error")

    def changeall(self, substring, new_word):
        while substring in self.message:
            word = self.message.replace(substring, new_word)
            self.message = word
        print(self.message)

    def commands(self):
        command = input()

        while command != "Reveal":
            command = command.split(":|:")

            if command[0] == "InsertSpace":
                self.insertspace(int(command[1]))
            elif command[0] == "Reverse":
                self.reverse(command[1])
            elif command[0] == "ChangeAll":
                self.changeall(command[1], command[2])

            command = input()

    def __str__(self):
        return f"You have a new text message: {self.message}"


concealed_message = input()
chat = SolveTheChat(concealed_message)
chat.commands()
print(chat)

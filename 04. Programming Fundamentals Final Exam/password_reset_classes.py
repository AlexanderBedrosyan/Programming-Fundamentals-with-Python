class PasswordReset:

    def __init__(self, current_password):
        self.current_password = current_password

    def take_odd(self):
        new_word = ''
        for index, letter in enumerate(self.current_password):
            if index % 2 != 0:
                new_word += letter
        self.current_password = new_word
        print(self.current_password)

    def cut(self, index, length):
        self.current_password = self.current_password[:index] + self.current_password[index + length:]
        print(self.current_password)

    def substitute(self, substring, substitute):
        if substring in self.current_password:
            new_password = self.current_password.replace(substring, substitute)
            self.current_password = new_password
            print(self.current_password)
        else:
            print("Nothing to replace!")

    def change_password(self):
        command = input()

        while command != "Done":
            command = command.split(" ")

            if command[0] == "TakeOdd":
                self.take_odd()
            elif command[0] == "Cut":
                self.cut(int(command[1]), int(command[2]))
            elif command[0] == "Substitute":
                self.substitute(command[1], command[2])

            command = input()

    def __repr__(self):
        return f"Your password is: {self.current_password}"


password = PasswordReset(input())
password.change_password()
print(password)

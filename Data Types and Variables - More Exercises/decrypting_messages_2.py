class DecryptingMessages:

    def __init__(self, decrypting_number):
        self.decrypting_number = decrypting_number

    def find_the_message(self):
        message = ''
        for i in range(int(input())):
            secret_letter = input()
            message += f"{chr(ord(secret_letter) + self.decrypting_number)}"
        return message


decrypting_message = DecryptingMessages(int(input()))
print(decrypting_message.find_the_message())

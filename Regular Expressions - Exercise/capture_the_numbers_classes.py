import re


class CaptureNumbers:

    def __init__(self):
        self.final_result = []

    def find_the_numbers(self):
        command = input()

        while len(command) != 0:
            pattern = r'\d+'
            matches = re.findall(pattern, command)
            for ch in matches:
                self.final_result.append(ch)
            command = input()

    def __str__(self):
        return ' '.join(str(ch) for ch in self.final_result)


numbers = CaptureNumbers()
numbers.find_the_numbers()
print(numbers)

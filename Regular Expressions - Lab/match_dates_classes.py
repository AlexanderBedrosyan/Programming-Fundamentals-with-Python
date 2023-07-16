import re


class Dates:

    def __init__(self, single_string):
        self.single_string = single_string
        self.final_result = []
        self.counter = 0

    def find_the_final_result(self):
        pattern = r'\b([0-9]{2})([\/.-])([A-Z][a-z]{2})\2([0-9]{4})\b'
        matches = re.findall(pattern, self.single_string)
        self.final_result = [ch for ch in matches]

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > len(self.final_result):
            raise StopIteration
        return f"Day: {self.final_result[self.counter - 1][0]}, " \
               f"Month: {self.final_result[self.counter - 1][2]}, " \
               f"Year: {self.final_result[self.counter - 1][3]}"


correct_dates = Dates(input())
correct_dates.find_the_final_result()
for ch in correct_dates:
    print(ch)

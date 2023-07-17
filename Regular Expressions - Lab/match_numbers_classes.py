import re


class MatchNumbers:

    def __init__(self):
        self.result = []

    def find_numbers(self):
        pattern = r'(^|(?<=\s))-?([0]|[0-9][0-9]*)(\.?[0-9]+)?($|(?=\s))'
        matches = re.finditer(pattern, input())

        for match in matches:
            self.result.append(match.group())

    def __repr__(self):
        return ' '.join(str(ch) for ch in self.result)


TheNumbers = MatchNumbers()
TheNumbers.find_numbers()
print(TheNumbers)

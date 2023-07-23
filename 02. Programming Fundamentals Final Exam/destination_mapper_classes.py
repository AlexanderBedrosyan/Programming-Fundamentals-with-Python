import re


class DestinationMapper:

    def __init__(self):
        self.destinations = []
        self.points = 0

    def information(self):
        pattern = r'([\=\/])([A-Z][A-Za-z]{2,})\1'
        matches = re.findall(pattern, input())
        for ch in matches:
            self.destinations.append(ch[1])
            self.points += len(ch[1])

    def __repr__(self):
        return f"Destinations: {', '.join(str(ch) for ch in self.destinations)}\nTravel Points: {self.points}"


destination_mapper = DestinationMapper()
destination_mapper.information()
print(destination_mapper)

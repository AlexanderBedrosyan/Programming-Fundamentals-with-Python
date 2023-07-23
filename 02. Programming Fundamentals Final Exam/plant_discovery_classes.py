class PlantDiscovery:

    def __init__(self):
        self.information = {}
        self.rating = {}

    def is_valid(self, plant):
        validation = True
        if plant not in self.information:
            validation = False
            print("error")
        return validation

    def rate(self, plant, rate):
        if plant not in self.rating:
            self.rating[plant] = {}
        if self.rating[plant]:
            for key, value in self.rating[plant].items():
                new_key = key + 1
                new_rating = value + rate
                self.rating[plant] = {}
                self.rating[plant][new_key] = new_rating
        else:
            self.rating[plant][1] = rate

    def update(self, plant, new_rarity):
        self.information[plant] = int(new_rarity)

    def reset(self, plant):
        if plant in self.rating:
            del self.rating[plant]

    def fill_the_information(self):
        n = int(input())
        for _ in range(n):
            plant, rarity = input().split("<->")
            if plant not in self.information:
                self.information[plant] = 0
            self.information[plant] = int(rarity)

    def commands(self):
        command = input()

        while command != "Exhibition":
            command = command.split(" ")
            if not self.is_valid(command[1]):
                command = input()
                continue
            if command[0] == "Rate:":
                self.rate(command[1], int(command[3]))
            elif command[0] == "Update:":
                self.update(command[1], int(command[3]))
            elif command[0] == "Reset:":
                self.reset(command[1])

            command = input()

    def __repr__(self):
        result = ["Plants for the exhibition:"]
        for key, values in self.information.items():
            average_rating = 0
            if key in self.rating:
                for count, rating in self.rating[key].items():
                    average_rating = rating / count
            result.append(f"- {key}; Rarity: {values}; Rating: {average_rating:.2f}")
        return '\n'.join(result)


plant_information = PlantDiscovery()
plant_information.fill_the_information()
plant_information.commands()
print(plant_information)

class Pirates:

    def __init__(self):
        self.city_information = {}

    def plunder(self, town, people, gold):
        if town in self.city_information:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            condition = False
            for population, current_gold in self.city_information[town].items():
                new_population = population - people
                new_gold = current_gold - gold
                if new_gold <= 0 or new_population <= 0:
                    condition = True
                self.city_information[town] = {new_population: new_gold}
            if condition:
                del self.city_information[town]
                print(f"{town} has been wiped off the map!")

    def prosper(self, town, gold):
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            if town in self.city_information:
                for population, current_gold in self.city_information[town].items():
                    new_gold = gold + current_gold
                    self.city_information[town] = {population: new_gold}
                    print(f"{gold} gold added to the city treasury. {town} now has {new_gold} gold.")

    def fill_the_city_information(self):
        command = input()

        while command != "Sail":
            city, population, gold = command.split("||")
            if city not in self.city_information:
                self.city_information[city] = {0: 0}

            for current_population, current_gold in self.city_information[city].items():
                new_population = current_population + int(population)
                new_gold = current_gold + int(gold)
                self.city_information[city] = {new_population: new_gold}

            command = input()

    def execute_the_commands(self):
        command = input()

        while command != "End":

            command = command.split("=>")

            if command[0] == "Plunder":
                self.plunder(command[1], int(command[2]), int(command[3]))

            elif command[0] == "Prosper":
                self.prosper(command[1], int(command[2]))

            command = input()


pirates_battle = Pirates()
pirates_battle.fill_the_city_information()
pirates_battle.execute_the_commands()
if pirates_battle.city_information:
    print(f"Ahoy, Captain! There are {len(pirates_battle.city_information)} wealthy settlements to go to:")
    for city, value in pirates_battle.city_information.items():
        for people, gold in value.items():
            print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

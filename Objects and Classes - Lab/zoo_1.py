class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        if species == "mammal":
            species_name = self.mammals
            species_print = "Mammals"
        elif species == "fish":
            species_name = self.fishes
            species_print = "Fishes"
        elif species == "bird":
            species_name = self.birds
            species_print = "Birds"
        names = ", ".join(species_name)

        return f"{species_print} in {zoo_name}: {names}"

    def get_total(self):
        return f"Total animals: {self.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animals(species, name)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())

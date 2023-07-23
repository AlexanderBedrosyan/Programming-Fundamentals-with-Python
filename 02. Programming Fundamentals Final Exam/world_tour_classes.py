class WorldTour:

    def __init__(self, destinations):
        self.destinations = destinations

    def __add__(self, other, second_part):
        self.destinations = other + second_part

    def is_valid_index(self, *args):
        if len(args) == 2:
            index = args[0]
            distance_of_word = args[1]
            if index in range(distance_of_word):
                return True
        else:
            starting_index = args[0]
            ending_index = args[1]
            distance_of_word = args[2]
            if starting_index in range(distance_of_word) and ending_index in range(distance_of_word):
                return True
        return False

    def switch(self, inside_word, new_word):
        if inside_word in self.destinations:
            self.destinations = self.destinations.replace(inside_word, new_word)

    def command_receiving(self):
        command = input()

        while command != "Travel":
            information = command.split(":")
            if information[0] == "Add Stop":
                index = int(information[1])
                if self.is_valid_index(index, len(self.destinations)):
                    self.__add__(self.destinations[0:index], information[2] + self.destinations[index:])
                print(self.destinations)
            elif information[0] == "Remove Stop":
                starting_index = int(information[1])
                ending_index = int(information[2])
                if self.is_valid_index(starting_index, ending_index, len(self.destinations)):
                    self.__add__(self.destinations[0:starting_index], self.destinations[ending_index + 1:])
                print(self.destinations)
            elif information[0] == "Switch":
                self.switch(information[1], information[2])
                print(self.destinations)

            command = input()


the_tour = WorldTour(input())
the_tour.command_receiving()
print(f"Ready for world tour! Planned stops: {the_tour.destinations}")

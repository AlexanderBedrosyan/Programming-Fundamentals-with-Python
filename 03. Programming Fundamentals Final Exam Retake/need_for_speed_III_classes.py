class Car:
    OLD_CAR = 100000
    MAX_LITERS_OF_FUEL = 75
    MIN_MILEAGE = 10000

    def __init__(self):
        self.car_information = {}

    def __iter__(self):
        return self

    def __next__(self):
        if not self.car_information:
            raise StopIteration
        for car in self.car_information.keys():
            for mileage, fuel in self.car_information[car].items():
                del self.car_information[car]
                return f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."

    def fill_the_information(self):
        rows = int(input())

        for _ in range(rows):
            car, mileage, fuel = input().split("|")
            self.car_information[car] = {}
            self.car_information[car][int(mileage)] = int(fuel)

    def drive(self, car, distance, fuel):
        if car in self.car_information:
            for mileage, current_fuel in self.car_information[car].items():
                if (current_fuel - fuel) >= 0:
                    new_mileage = mileage + distance
                    new_fuel = current_fuel - fuel
                    self.car_information[car] = {}
                    self.car_information[car][new_mileage] = new_fuel
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                    if new_mileage >= Car.OLD_CAR:
                        del self.car_information[car]
                        print(f"Time to sell the {car}!")
                else:
                    print("Not enough fuel to make that ride")

    def refuel(self, car, fuel):
        if car in self.car_information:
            for mileage, current_fuel in self.car_information[car].items():
                new_fuel = current_fuel + fuel
                rest_of_max = 0
                if new_fuel > Car.MAX_LITERS_OF_FUEL:
                    rest_of_max = new_fuel - Car.MAX_LITERS_OF_FUEL
                self.car_information[car] = {}
                self.car_information[car][mileage] = new_fuel - rest_of_max
                print(f"{car} refueled with {fuel - rest_of_max} liters")

    def revert(self, car, kilometers):
        if car in self.car_information:
            for mileage, fuel in self.car_information[car].items():
                if (mileage - kilometers) < Car.MIN_MILEAGE:
                    new_fuel = fuel
                    self.car_information[car] = {}
                    self.car_information[car][Car.MIN_MILEAGE] = new_fuel
                else:
                    new_mileage = mileage - kilometers
                    new_fuel = fuel
                    self.car_information[car] = {}
                    self.car_information[car][new_mileage] = new_fuel
                    print(f"{car} mileage decreased by {kilometers} kilometers")

    def instructions(self):
        command = input()

        while command != "Stop":
            command = command.split(" : ")
            if command[0] == "Drive":
                self.drive(command[1], int(command[2]), int(command[3]))
            elif command[0] == "Refuel":
                self.refuel(command[1], int(command[2]))
            elif command[0] == "Revert":
                self.revert(command[1], int(command[2]))

            command = input()


cars = Car()
cars.fill_the_information()
cars.instructions()
for ch in cars:
    print(ch)

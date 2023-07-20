def drive(dict, car, distance, fuel):
    for ch in dict:
        if ch == car:
            for key in dict[ch]:
                if dict[ch][key] < fuel:
                    return dict, "Not enough fuel to make that ride"
                elif key + distance < 100000:
                    value = dict[ch][key] - fuel
                    key = key + distance
                    dict[ch] = {}
                    dict[ch][key] = value
                    return dict, f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
                elif key + distance >= 1000:
                    del dict[car]
                    return dict, f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.\nTime to sell the {car}!"


def refuel(dict, car, fuel):
    for ch in dict:
        if ch == car:
            for key in dict[ch]:
                if (dict[ch][key]) + fuel <= 75:
                    dict[ch][key] += fuel
                else:
                    fuel = 75 - dict[ch][key]
                    dict[ch][key] = 75

    return dict, f"{car} refueled with {fuel} liters"


def revert(dict, car, km):
    for ch in dict:
        if ch == car:
            for key in dict[ch]:
                if (key - km) < 10000:
                    km = key - 1000
                    value = dict[ch][key]
                    key = 10000
                    dict[ch] = {}
                    dict[ch][key] = value
                    return dict, ""
                else:
                    value = dict[ch][key]
                    key = key - km
                    dict[ch] = {}
                    dict[ch][key] = value
                    return dict, f"{car} mileage decreased by {km} kilometers"


number_of_cars = int(input())
cars_dict = {}

for i in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    if int(mileage) < 100000:
        cars_dict[car] = {}
        cars_dict[car][int(mileage)] = int(fuel)

while True:
    command = input()
    if command == "Stop":
        break

    new_command = command.split(" : ")

    if new_command[0] == "Drive":
        cars_dict, message = drive(cars_dict, new_command[1], int(new_command[2]), int(new_command[3]))
        print(message)
    if new_command[0] == "Refuel":
        cars_dict, message = refuel(cars_dict, new_command[1], int(new_command[2]))
        print(message)
    if new_command[0] == "Revert":
        cars_dict, message = revert(cars_dict, new_command[1], int(new_command[2]))
        if len(message) > 1:
            print(message)

for ch in cars_dict:
    for key in cars_dict[ch]:
        print(f"{ch} -> Mileage: {key} kms, Fuel in the tank: {cars_dict[ch][key]} lt.")
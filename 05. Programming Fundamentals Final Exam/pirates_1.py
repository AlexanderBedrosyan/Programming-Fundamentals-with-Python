def plunder(city_information, town, people, gold):
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    for citizens, current_gold in city_information[town].items():
        new_citizens = citizens - people
        new_gold = current_gold - gold
        if new_citizens == 0 or new_gold == 0:
            print(f"{town} has been wiped off the map!")
            del city_information[town]
            return city_information
        city_information[town] = {}
        city_information[town][new_citizens] = new_gold
        return city_information


def prosper(city_information, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
        return city_information
    for key in city_information[town].keys():
        city_information[town][key] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {city_information[town][key]} gold.")
        return city_information


cities_population_gold = {}

command = input()

while command != "Sail":
    city, population, gold = command.split("||")
    if city not in cities_population_gold:
        cities_population_gold[city] = {}
        cities_population_gold[city][int(population)] = int(gold)
    else:
        for popul, current_gold in cities_population_gold[city].items():
            new_popul = popul + int(population)
            new_gold = current_gold + int(gold)
            cities_population_gold[city] = {}
            cities_population_gold[city][new_popul] = new_gold
    command = input()

action = input()

while action != "End":
    action = action.split("=>")
    if action[0] == "Plunder":
        cities_population_gold = plunder(cities_population_gold, action[1], int(action[2]), int(action[3]))
    elif action[0] == "Prosper":
        cities_population_gold = prosper(cities_population_gold, action[1], int(action[2]))

    action = input()

if cities_population_gold:
    print(f"Ahoy, Captain! There are {len(cities_population_gold)} wealthy settlements to go to:")
    for town in cities_population_gold.keys():
        for people, gold in cities_population_gold[town].items():
            print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
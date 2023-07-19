def add(dict, plant, rating):
    for ch in dict:
        if ch == plant:
            for key in dict[ch]:
                dict[ch][key].append(int(rating))
    return dict


def update(dict, plant, rarity):
    for ch in dict:
        if ch == plant:
            new_list = []
            for key in dict[ch]:
                new_list = dict[ch][key]
                dict[ch] = {}
                dict[ch][rarity] = new_list
    return dict


def reset(dict, plant):
    for ch in dict:
        if ch == plant:
            for key in dict[ch]:
                dict[ch][key] = []
    return dict


num = int(input())

plant_dict = {}

for i in range(num):
    key, value = input().split("<->")
    plant_dict[key] = {}
    plant_dict[key][value] = []

while True:
    command = input()
    if command == "Exhibition":
        break

    checking_word, new_command = command.split(": ")
    if checking_word == "Rate":
        plant, rating = new_command.split(" - ")
        if plant in plant_dict:
            plant_dict = add(plant_dict, plant, rating)
        else:
            print("error")
    if checking_word == "Update":
        plant, new_rarity = new_command.split(" - ")
        if plant in plant_dict:
            plant_dict = update(plant_dict, plant, new_rarity)
        else:
            print("error")
    if checking_word == "Reset":
        plant = new_command
        if plant in plant_dict:
            plant_dict = reset(plant_dict, plant)
        else:
            print("error")

print("Plants for the exhibition:")
for i in plant_dict:
    plant_name = i
    rarity = ""
    average_rating = 0
    for ch in plant_dict[i]:
        rarity = ch
        if len(plant_dict[i][ch]) > 0:
            average_rating = (sum(plant_dict[i][ch]) / len(plant_dict[i][ch]))

    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")
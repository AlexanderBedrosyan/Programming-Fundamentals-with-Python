def find_the_drink(dict, age):
    for key in dict:
        if dict[key][0] <= age <= dict[key][1]:
            return f"drink {key}"


drinks_dict = {"toddy": [1, 14], "coke": [15, 18], "beer": [19, 21], "whisky": [22, 120]}

print(find_the_drink(drinks_dict, int(input())))

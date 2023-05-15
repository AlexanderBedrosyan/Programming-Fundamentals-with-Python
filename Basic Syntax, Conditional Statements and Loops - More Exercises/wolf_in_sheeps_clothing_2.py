def result(list):
    ind = list.index("wolf")
    if ind == len(list) - 1:
        return "Please go away and stop eating my sheep"
    else:
        places_behind = (len(list) - 1) - ind
        return f"Oi! Sheep number {places_behind}! You are about to be eaten by a wolf!"


farm = [ch for ch in input().split(", ")]

print(result(farm))
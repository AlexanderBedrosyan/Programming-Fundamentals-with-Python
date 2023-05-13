def coffee_needed(dict):
    result = 0
    while True:
        events = input()
        if events == "END":
            break
        for key in dict:
            if events in dict[key]:
                result += key
    if result > 5:
        print("You need extra sleep")
    else:
        print(result)


events_dict = {1: ["cat", "dog", "coding", "movie"], 2: ["CAT", "DOG", "CODING", "MOVIE"]}
coffee_needed(events_dict)
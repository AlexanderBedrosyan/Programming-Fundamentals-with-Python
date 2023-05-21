class List_of_snowballs():
    snowballs = []

    def __init__(self, n):
        self.n = n

    def fill_the_snow_balls_list(self):
        for _ in range(self.n):
            current_snowball = []
            for i in range(3):
                current_snowball.append(int(input()))
            self.snowballs.append(current_snowball)
        return self.snowballs


def the_best_snowball(list):
    top_snowball = 0
    place_in_list = 0

    for index in range(len(list)):
        weight = list[index][0]
        time = list[index][1]
        quality = list[index][2]
        current_score = (weight / time) ** quality
        if current_score > top_snowball:
            top_snowball = current_score
            place_in_list = index

    weight = list[place_in_list][0]
    time = list[place_in_list][1]
    quality = list[place_in_list][2]
    return f"{weight} : {time} = {int(top_snowball)} ({quality})"


players = int(input())
current_snowballs = List_of_snowballs(players)
list_of_snowballs = current_snowballs.fill_the_snow_balls_list()

print(the_best_snowball(list_of_snowballs))

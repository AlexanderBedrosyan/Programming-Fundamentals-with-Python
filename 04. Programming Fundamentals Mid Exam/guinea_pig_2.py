def every_day(food):
    return food - 300


def every_second_day(food, hay):
    return hay - (food * 0.05)


def every_third_day(cover, pig_weight):
    return cover - (pig_weight / 3)


def check_the_rest(hay, cover, food):
    flag = True
    if hay < 0 or food < 0 or cover < 0:
        flag = False
    return flag


def final_result(hay, cover, food):
    return f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: " \
           f"{cover / 1000:.2f}."


food, hay, cover = float(input()) * 1000, float(input()) * 1000, float(input()) * 1000
pig_weight = float(input()) * 1000

for day in range(1, 31):
    food = every_day(food)

    if day % 2 == 0:
        hay = every_second_day(food, hay)
    if day % 3 == 0:
        cover = every_third_day(cover, pig_weight)

    if not check_the_rest(food, hay, cover):
        print("Merry must go to the pet store!")
        exit()

print(final_result(hay, cover, food))

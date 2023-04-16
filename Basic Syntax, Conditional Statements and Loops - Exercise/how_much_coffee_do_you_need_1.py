to_do_list = ["coding", "dog", "cat", "movie"]
cup_of_coffee = 0

while True:
    tasks = input()
    if tasks == "END":
        break
    if tasks.lower() not in to_do_list:
        continue

    if tasks == tasks.lower():
        cup_of_coffee += 1
    elif tasks == tasks.upper():
        cup_of_coffee += 2

if cup_of_coffee > 5:
    print("You need extra sleep")
else:
    print(cup_of_coffee)

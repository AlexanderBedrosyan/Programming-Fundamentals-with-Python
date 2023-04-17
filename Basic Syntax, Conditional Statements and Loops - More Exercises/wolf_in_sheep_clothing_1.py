animals = input()

word = ""
list_animals = []

for index, digits in enumerate(animals):
    if (index + 1) == len(animals):
        word += digits
        list_animals.append(word)
        break
    if digits == " ":
        continue

    if digits == ",":
       list_animals.append(word)
       word = ""
    else:
       word += digits

counter = (len(list_animals) - 1)

for i in range(0, len(list_animals)):
    if list_animals[i] == "sheep":
        counter -= 1

    if i == (len(list_animals) - 1) and list_animals[i] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif i != (len(list_animals) - 1) and list_animals[i] == "wolf":
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
        break



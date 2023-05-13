def sorting_hat():
    while True:
        name = input()
        if name == "Welcome!":
            print("Welcome to Hogwarts.")
            break
        elif name == "Voldemort":
            print("You must not speak of that name!")
            break

        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")


sorting_hat()

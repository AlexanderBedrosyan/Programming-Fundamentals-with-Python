group = [int(ch) for ch in input().split(", ")]

new_list = []
counter = 0

while len(group) > 0:
    counter += 10

    new_list = [item for item in group if item <= counter]
    for i in range(len(group) - 1, - 1, - 1):
        if group[i] in new_list:
            del group[i]

    print(f"Group of {counter}'s: {new_list}")
    new_list = []

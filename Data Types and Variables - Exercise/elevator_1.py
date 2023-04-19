number_people = int(input())
capacity = int(input())

counter = 0

while number_people > 0:
    counter += 1
    number_people -= capacity

print(counter)

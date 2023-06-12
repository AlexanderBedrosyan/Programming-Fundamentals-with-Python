def wagons_fulfill(passengers, wagons, count):
    while wagons[count] < 4 and passengers > 0:
        passengers -= 1
        wagons[count] += 1
    return passengers, wagons


passengers = int(input())
wagons = [int(ch) for ch in input().split(" ")]
count = 0

while passengers > 0 and min(wagons) < 4:
    if 0 <= count < len(wagons):
        passengers, wagons = wagons_fulfill(passengers, wagons, count)
        count += 1

if min(wagons) == 4:
    if passengers > 0:
        print(f"There isn't enough space! {passengers} people in a queue!")
elif min(wagons) != 4:
    print("The lift has empty spots!")
print(' '.join(str(ch) for ch in wagons))


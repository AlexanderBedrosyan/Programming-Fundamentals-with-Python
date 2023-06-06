numbers = input()

starting_numbers = [int(chart) for chart in numbers.strip().split()]
current_number = 0
counter = 0

while True:
    command = input()

    if command == "End":
        break

    command = int(command)

    if (command > (len(starting_numbers) - 1)) or (command < 0):
        continue
    else:
        if starting_numbers[command] != -1:
            current_number = starting_numbers[command]
            starting_numbers[command] = -1
            counter += 1
        for ch in range(len(starting_numbers)):
            if starting_numbers[ch] == -1:
                continue
            else:
                if starting_numbers[ch] > current_number:
                    starting_numbers[ch] -= current_number
                else:
                    starting_numbers[ch] += current_number

    current_number = 0

for digit in range(len(starting_numbers)):
    if digit == 0:
        print(f"Shot targets: {counter} -> {starting_numbers[0]}", end=" ")
    elif digit == (len(starting_numbers) - 1):
        print(starting_numbers[len(starting_numbers) - 1])
    else:
        print(starting_numbers[digit], end=" ")
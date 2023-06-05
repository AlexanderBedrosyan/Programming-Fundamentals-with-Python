numbers = input()

list_numbers = [str(ch) for ch in numbers.strip().split(" ")]
checking_list = []
moves = 0

while True:
    if len(list_numbers) == 0:
        print(f"You have won in {moves} turns!")
        exit()

    check_numbers = input()

    if check_numbers == "end":
        print("Sorry you lose :(")
        print(*list_numbers, sep=" ")
        exit()
    else:
        checking_list = [int(items) for items in check_numbers.strip().split(" ")]
        if (0 > checking_list[0]) or (checking_list[0] > (len(list_numbers) - 1)) or (0 > checking_list[1]) or (checking_list[1] > (len(list_numbers) - 1)) or (checking_list[0] == checking_list[1]):
            moves += 1
            print("Invalid input! Adding additional elements to the board")
            list_numbers.insert((len(list_numbers) // 2), f"-{moves}a")
            list_numbers.insert((len(list_numbers) // 2), f"-{moves}a")
            checking_list = []
        elif list_numbers[checking_list[0]] == list_numbers[checking_list[1]]:
            moves += 1
            print(f"Congrats! You have found matching elements - {list_numbers[checking_list[0]]}!")
            if checking_list[0] > checking_list[1]:
                list_numbers.remove(list_numbers[checking_list[0]])
                list_numbers.remove(list_numbers[checking_list[1]])
            elif checking_list[0] < checking_list[1]:
                list_numbers.remove(list_numbers[checking_list[0]])
                list_numbers.remove(list_numbers[checking_list[1] - 1])
            checking_list = []
        else:
            print("Try again!")
            checking_list = []
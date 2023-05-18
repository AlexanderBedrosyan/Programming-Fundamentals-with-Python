def calculation(number):
    for i in range(1, number + 1):
        current_number = i
        new_number = 0
        while i > 0:
            new_number += i % 10
            i = i // 10

        if (new_number == 5) or (new_number == 7) or (new_number == 11):
            print(f"{current_number} -> True")
            new_number = 0
        else:
            print(f"{current_number} -> False")
            new_number = 0


calculation(int(input()))
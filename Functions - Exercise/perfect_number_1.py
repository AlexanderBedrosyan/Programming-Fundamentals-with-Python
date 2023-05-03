def perfect_number(number):
    checking_number = 0
    for i in range(1, number):
        if number % i == 0:
            checking_number += i

    if checking_number == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number(number)

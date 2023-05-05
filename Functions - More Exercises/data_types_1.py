def data_type_calculation(command, number):
    if command == "int":
        print(f"{int(number) * 2}")
    elif command == "real":
        print(f"{float(number) * 1.5:.2f}")
    elif command == "string":
        print("$" + number + "$")


command = input()
number = input()

data_type_calculation(command, number)

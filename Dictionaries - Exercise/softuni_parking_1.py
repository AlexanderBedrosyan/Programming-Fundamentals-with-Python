parking_dict = {}
num = int(input())

for i in range(num):
    command = input().split(" ")

    if command[0] == "register":
        username = command[1]
        vehicle_number = command[2]
        if username in parking_dict:
            print(f"ERROR: already registered with plate number {parking_dict[username]}")
        else:
            parking_dict[username] = vehicle_number
            print(f"{username} registered {parking_dict[username]} successfully")
    else:
        username = command[1]
        if username not in parking_dict:
            print(f"ERROR: user {username} not found")
        else:
            del parking_dict[username]
            print(f"{username} unregistered successfully")

for item in parking_dict:
    print(f"{item} => {parking_dict[item]}")

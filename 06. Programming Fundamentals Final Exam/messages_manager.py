def add(information, username, sent, received):
    if username not in information:
        information[username] = {sent: received}
    return information


def message(information, sender, receiver, capacity):
    if sender in information and receiver in information:
        for sent, received in information[sender].items():
            new_sent = sent + 1
            if (new_sent + received) == capacity:
                print(f"{sender} reached the capacity!")
                del information[sender]
                break
            information[sender] = {}
            information[sender] = {new_sent: received}

        for sent, received in information[receiver].items():
            new_received = received + 1
            if (new_received + sent) == capacity:
                print(f"{receiver} reached the capacity!")
                del information[receiver]
                break
            information[receiver] = {}
            information[receiver] = {sent: new_received}

    return information


def empty(information, username):
    if username == "All":
        information = {}
    if username in information:
        del information[username]
    return information


capacity = int(input())

record = {}

command = input()

while command != "Statistics":
    option, *args = command.split("=")

    if option == "Add":
        record = add(record, args[0], int(args[1]), int(args[2]))
    elif option == "Message":
        record = message(record, args[0], args[1], capacity)
    elif option == "Empty":
        record = empty(record, args[0])

    command = input()

print(f"Users count: {len(record)}")
if record:
    for username, message_info in record.items():
        for sent, received in message_info.items():
            print(f"{username} - {sent + received}")

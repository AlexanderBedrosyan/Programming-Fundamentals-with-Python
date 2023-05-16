class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def common_function(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: "


info_list = []

while True:
    info = input()

    if info == "Stop":
        break

    full_info = info.split(" ")
    sender_index = full_info[0]
    receiver_index = full_info[1]
    content_index = full_info[2]

    information = Email(sender_index, receiver_index, content_index)
    info_list.append(information.common_function())

sent_list = [int(ch) for ch in input().split(", ")]

for i in range(len(info_list)):
    if i in sent_list:
        print(f"{info_list[i]}True")
    else:
        print(f"{info_list[i]}False")
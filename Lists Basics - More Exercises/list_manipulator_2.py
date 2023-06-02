class ListManipulator():

    def __init__(self, current_list, command_list):
        self.current_list = current_list
        self.command_list = command_list

    def exchange(self):
        if int(self.command_list[1]) > len(self.current_list) or int(self.command_list[1]) < 0:
            print("Invalid count")
            return self.current_list
        else:
            new_list = []
            for i in range(int(self.command_list[1])):
                if i <= int(self.command_list[1]):
                    chart = self.current_list.pop(0)
                    new_list.append(chart)
                else:
                    break
            final_list = [ch for ch in self.current_list]
            for ch in self.current_list:
                final_list.append(ch)
            return final_list


integer_list = [int(ch) for ch in input().split(" ")]

while True:
    command = input().split(" ")

    if command == "end":
        break

    integer_list = ListManipulator(integer_list, command)
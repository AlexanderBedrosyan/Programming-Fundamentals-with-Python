class GetInformation():

    def __init__(self, information_list):
        self.information_list = information_list

    def register(self, current_dict, name, license_plate):
        if name in current_dict:
            return current_dict, False
        else:
            current_dict[name] = license_plate
            return current_dict, True

    def unregister(self, current_dict, name):
        if name in current_dict:
            del current_dict[name]
            return current_dict, True
        else:
            return current_dict, False

    def complete_the_final_list(self, current_dict, final_list):
        for username, license_plate_number in current_dict.items():
            final_list.append(f"{username} => {license_plate_number}")
        return final_list

    def final_result(self):
        dictionary_information = {}
        final_result = []

        for element in self.information_list:
            element = element.split(" ")
            condition = True
            if element[0] == "register":
                name, license_plate_number = element[1], element[2]
                dictionary_information, condition = self.register(dictionary_information, name, license_plate_number)
                if condition:
                    final_result.append(f"{name} registered {license_plate_number} successfully")
                else:
                    final_result.append(f"ERROR: already registered with plate number {license_plate_number}")
            else:
                name = element[1]
                dictionary_information, condition = self.unregister(dictionary_information, name)
                if condition:
                    final_result.append(f"{name} unregistered successfully")
                else:
                    final_result.append(f"ERROR: user {name} not found")

        return '\n'.join(self.complete_the_final_list(dictionary_information, final_result))


starting_list = [input() for _ in range(int(input()))]
result = GetInformation(starting_list)
print(result.final_result())

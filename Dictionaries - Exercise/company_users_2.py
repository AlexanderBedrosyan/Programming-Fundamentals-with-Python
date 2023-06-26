class GetInfo():

    def __init__(self, information):
        self.information = information

    def final_dictionary(self):
        final_dict = {}
        for info in self.information:
            company, employee_id = info.split(" -> ")
            if company not in final_dict:
                final_dict[company] = []
            if employee_id not in final_dict[company]:
                final_dict[company].append(employee_id)
        return final_dict

    def __repr__(self):
        result = []
        for company, employees in self.final_dictionary().items():
            result.append(company)
            for id in employees:
                result.append(f"-- {id}")
        return '\n'.join(result)


starting_list = []
command = input()

while command != "End":

    starting_list.append(command)

    command = input()

print(GetInfo(starting_list))

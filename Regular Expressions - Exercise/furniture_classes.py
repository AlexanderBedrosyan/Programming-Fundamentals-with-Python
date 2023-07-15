import re


class Furnitures:

    def __init__(self):
        self.furnitures_list = []
        self.total_amount = 0

    def find_the_correct_information(self):
        command = input()

        while command != "Purchase":

            pattern_furn = r'[A-Za-z]+'
            pattern_amount_quantity = r'[0-9]+\.[0-9]+|[0-9]+'
            find_furnitures = re.findall(pattern_furn, command)
            find_the_amount_and_quantity = re.findall(pattern_amount_quantity, command)

            if len(find_furnitures) == 1 and len(find_the_amount_and_quantity) == 2:
                self.total_amount += (float(find_the_amount_and_quantity[0]) * float(find_the_amount_and_quantity[1]))
                self.furnitures_list.append(find_furnitures[0])

            command = input()

    def __str__(self):
        final_result = ["Bought furniture:"]
        for ch in self.furnitures_list:
            final_result.append(ch)
        final_result.append(f"Total money spend: {self.total_amount:.2f}")
        return '\n'.join(final_result)


furniture_information = Furnitures()
furniture_information.find_the_correct_information()
print(furniture_information)

class FillTheDict:

    def __init__(self):
        self.information = {}

    def fill_the_information(self):
        command = input()
        while command != "no more time":
            name, contest, points = command.split(" -> ")
            if contest not in self.information:
                self.information[contest] = {}
            if name in self.information[contest]:
                if int(points) <= self.information[contest][name]:
                    command = input()
                    continue
            self.information[contest][name] = int(points)
            command = input()

    def information_of_all_contests(self):
        final_dict = {}
        for contest, current_dict in self.information.items():
            for name, point in sorted(current_dict.items(), key=lambda x: (-x[1], x[0])):
                if contest not in final_dict:
                    final_dict[contest] = {}
                final_dict[contest][name] = point
        return final_dict

    def individual_statistics(self):
        final_dict = {}
        for contest, current_dict in self.information.items():
            for name, points in current_dict.items():
                if name not in final_dict:
                    final_dict[name] = 0
                final_dict[name] += points
        return final_dict


class JudgeFinalResult(FillTheDict):

    def __init__(self):
        super(JudgeFinalResult, self).__init__()

    def result_of_each_contest(self):
        current_dict = self.information_of_all_contests()
        result = []
        for contest, dict_element in current_dict.items():
            result.append(f"{contest}: {len(dict_element)} participants")
            position_counter = 0
            for name, points in dict_element.items():
                position_counter += 1
                result.append(f"{position_counter}. {name} <::> {points}")
        return '\n'.join(result)

    def result_of_every_participant(self):
        current_dict = self.individual_statistics()
        result = ["Individual standings:"]
        position_counter = 0
        for needed_name, points in sorted(current_dict.items(), key=lambda x: (-x[1], x[0])):
            position_counter += 1
            result.append(f"{position_counter}. {needed_name} -> {points}")
        return '\n'.join(result)


final_res = JudgeFinalResult()
final_res.fill_the_information()
final_res.information_of_all_contests()
final_res.individual_statistics()
print(final_res.result_of_each_contest())
print(final_res.result_of_every_participant())

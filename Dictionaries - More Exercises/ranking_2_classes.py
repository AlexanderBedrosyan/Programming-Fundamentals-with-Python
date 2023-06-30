class CreateContestPassword:

    def __init__(self):
        self.contest_dict = {}

    def get_information(self):
        command = input()

        while command != "end of contests":
            contest, password = command.split(":")
            self.contest_dict[contest] = password
            command = input()


class Ranking(CreateContestPassword):

    def __init__(self):
        super().__init__()
        self.final_dict = {}

    def complete_the_dictionary(self):
        command = input()

        while command != "end of submissions":
            current_contest, current_password, username, points = command.split("=>")
            if current_contest in self.contest_dict and self.contest_dict[current_contest] == current_password:
                if username not in self.final_dict:
                    self.final_dict[username] = {}
                if current_contest in self.final_dict[username]:
                    if self.final_dict[username][current_contest] >= int(points):
                        command = input()
                        continue
                self.final_dict[username][current_contest] = int(points)

            command = input()

    def find_the_best_player(self):
        player = ''
        points = 0

        for current_player, current_dict in self.final_dict.items():
            current_points = 0
            for key, point in current_dict.items():
                current_points += point
            if current_points > points:
                player = current_player
                points = current_points
        return player, points

    def result(self):
        best_student, points = self.find_the_best_player()
        result_list = [f"Best candidate is {best_student} with total {points} points.", "Ranking:"]
        sorted_dict = sorted(self.final_dict.items(), key=lambda x: x[0])
        for name, current_dict in sorted_dict:
            result_list.append(name)
            for contest, current_point in sorted(current_dict.items(), key=lambda x: -x[1]):
                result_list.append(f"#  {contest} -> {current_point}")
        return '\n'.join(result_list)


rank = Ranking()
rank.get_information()
rank.complete_the_dictionary()
print(rank.result())

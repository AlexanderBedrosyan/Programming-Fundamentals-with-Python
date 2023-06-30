class FillTheDicts:

    def __init__(self):
        self.information = {}
        self.total_points_per_player = {}

    def battle(self, first_player, second_player):
        condition = False
        if first_player in self.information and second_player in self.information:
            for key in self.information[first_player]:
                if key in self.information[second_player]:
                    condition = True
                    break
        if condition:
            if self.total_points_per_player[first_player] > self.total_points_per_player[second_player]:
                del self.information[second_player]
                del self.total_points_per_player[second_player]
            elif self.total_points_per_player[second_player] > self.total_points_per_player[first_player]:
                del self.information[first_player]
                del self.total_points_per_player[first_player]

    def complete_the_dicts(self, player, position, skill):
        condition = False
        if player not in self.information:
            self.information[player] = {}
            self.total_points_per_player[player] = 0
        if position not in self.information[player]:
            self.information[player][position] = skill
            self.total_points_per_player[player] += skill
        else:
            if self.information[player][position] < skill:
                condition = True

        if condition:
            needed_for_add_points = skill - self.information[player][position]
            self.total_points_per_player[player] += needed_for_add_points
            self.information[player][position] = skill

    def fill_the_information(self):
        command = input()

        while command != "Season end":
            if " vs " in command:
                first_player, second_player = command.split(" vs ")
                self.battle(first_player, second_player)
            else:
                player, position, skill = command.split(" -> ")
                self.complete_the_dicts(player, position, int(skill))

            command = input()


class GetResult(FillTheDicts):

    def __init__(self):
        super(GetResult, self).__init__()

    def final_result(self):
        sorted_dict = sorted(self.total_points_per_player.items(), key=lambda x: (-x[1], x[0]))
        result = []

        for name, total_points in sorted_dict:
            result.append(f"{name}: {total_points} skill")
            for position, skill in sorted(self.information[name].items(), key=lambda x: (-x[1], x[0])):
                result.append(f"- {position} <::> {skill}")

        return '\n'.join(result)


information_of_all_players = GetResult()
information_of_all_players.fill_the_information()
print(information_of_all_players.final_result())

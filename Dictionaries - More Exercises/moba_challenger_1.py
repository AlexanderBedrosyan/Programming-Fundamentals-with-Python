def modify_ranking_dict(dict, player, position, skill):
    if player not in dict:
        dict[player] = {}
        dict[player][position] = skill
    else:
        if position not in dict[player]:
            dict[player][position] = skill
        else:
            if dict[player][position] < skill:
                dict[player][position] = skill
    return dict


def battle(dict, first_player, second_player):
    if (first_player in dict) and (second_player in dict):
        for the_position in dict[first_player]:
            if the_position in dict[second_player]:
                first_total_points = sum(dict[first_player].values())
                second_total_points = sum(dict[second_player].values())
                if first_total_points > second_total_points:
                    del dict[second_player]
                elif first_total_points < second_total_points:
                    del dict[first_player]
                break

    return dict


ranking_dict = {}

while True:
    command = input()

    if command == "Season end":
        break

    if "->" in command:
        current_command = command.split(" -> ")
        player, position, skill = current_command[0], current_command[1], current_command[2]
        ranking_dict = modify_ranking_dict(ranking_dict, player, position, int(skill))
    elif " vs " in command:
        current_command = command.split(" vs ")
        player_one, player_two = current_command[0], current_command[1]
        ranking_dict = battle(ranking_dict, player_one, player_two)

rankig_by_top_scores = dict(sorted(ranking_dict.items(), key=lambda x: (-sum(x[1].values()), x)))

for key in rankig_by_top_scores:
    needed_sum = sum(rankig_by_top_scores[key].values())
    print(f"{key}: {needed_sum} skill")
    for chart, digit in sorted(rankig_by_top_scores[key].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {chart} <::> {digit}")
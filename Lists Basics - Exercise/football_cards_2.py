def team_cards(team, number, dict):
    index = number - 1
    if dict[team][index] == 1:
        dict[team][index] = 0
    return dict


def if_terminated(new_dict):
    condition = False
    for key, value in new_dict.items():
        if sum(value) < 7:
            condition = True
    return condition


teams = {"A": [1 for _ in range(11)], "B": [1 for _ in range(11)]}
command = [ch for ch in input().split(" ")]
game_terminated = False

for i in range(len(command)):
    team, number = command[i].split("-")
    teams = team_cards(team, int(number), teams)
    game_terminated = if_terminated(teams)
    if game_terminated:
        break

for team, players in teams.items():
    if team == "A":
        print(f"Team {team} - {sum(players)};", end=" ")
    else:
        print(f"Team {team} - {sum(players)}")
if game_terminated:
    print("Game was terminated")
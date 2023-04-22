cards = input()

list_cards = [str(ch) for ch in cards.split()]
checking_list = []

team_a = 11
team_b = 11

for i in range(len(list_cards)):
    if team_a < 7 or team_b < 7:
        break
    if list_cards[i] in checking_list:
        continue
    else:
        checking_list.append(list_cards[i])

    if list_cards[i][0] == "A":
        team_a -= 1
    elif list_cards[i][0] == "B":
        team_b -= 1

if team_a < 7 or team_b < 7:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")

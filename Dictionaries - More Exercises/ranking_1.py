contests_dict = {}
final_dict = {}

while True:
    current_contest = input()

    if current_contest == "end of contests":
        break

    contests_dict[current_contest] = {}

while True:
    current_student = input()

    if current_student == "end of submissions":
        break

    contest, password, username, points = current_student.split("=>")
    checking_contest = f"{contest}:{password}"
    count = 0

    if checking_contest in contests_dict:
        for ch in contests_dict[checking_contest]:
            if ch == username:
                count += 1
                if int(contests_dict[checking_contest][username]) < int(points):
                    contests_dict[checking_contest][username] = int(points)

    if (checking_contest in contests_dict) and (count == 0):
        contests_dict[checking_contest][username] = int(points)

for chart in contests_dict:
    interview, result = chart.split(":")

    for key in contests_dict[chart]:
        if key not in final_dict:
            final_dict[key] = {}
            final_dict[key][interview] = contests_dict[chart][key]
        else:
            final_dict[key][interview] = contests_dict[chart][key]

best_candidate = ""
points = 0

for ch in final_dict:
    current_points = 0
    for key in final_dict[ch]:
        current_points += final_dict[ch][key]

    if points < current_points:
        best_candidate = ch
        points = current_points

print(f"Best candidate is {best_candidate} with total {points} points.\nRanking:")

for key, value in sorted(final_dict.items(), key=lambda x: x[0], reverse=False):
    print(key)
    for chart, digit in sorted(final_dict[key].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {chart} -> {digit}")
def final_dict(dict, contests, user, points):
    if contests not in dict:
        dict[contests] = {}
        dict[contests][user] = points
    else:
        if user not in dict[contests]:
            dict[contests][user] = points
        else:
            if dict[contests][user] < points:
                dict[contests][user] = points
    return dict


users_points_dict = {}
contest_users_points_dict = {}

while True:
    command = input()

    if command == "no more time":
        break

    name, contests, points = command.split(" -> ")

    contest_users_points_dict = final_dict(contest_users_points_dict, contests, name, int(points))

for ch in contest_users_points_dict:
    for key in contest_users_points_dict[ch]:
        if key not in users_points_dict:
            users_points_dict[key] = contest_users_points_dict[ch][key]
        else:
            users_points_dict[key] += contest_users_points_dict[ch][key]

count = 1

for key, value in contest_users_points_dict.items():
    result = len(value)
    print(f"{key}: {result} participants")
    for chart, digit in sorted(contest_users_points_dict[key].items(), key=lambda x: (-x[1], x[0])):
        print(f"{count}. {chart} <::> {digit}")
        count += 1
    count = 1

print("Individual standings:")
for key, value in sorted(users_points_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{count}. {key} -> {value}")
    count += 1
n = int(input())

high_score = 0
new_high_score = ""

for i in range(1, n + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    total_score = (weight / time_needed) ** quality

    if total_score > high_score:
        high_score = total_score
        new_high_score = f"{weight} : {time_needed} = {int(total_score)} ({quality})"

print(new_high_score)

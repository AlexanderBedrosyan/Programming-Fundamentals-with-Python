def plunder_count(plunder_per_day, current_day,):
    if current_day % 3 == 0:
        plunder_per_day *= 1.5
    return plunder_per_day


def final_result(totalPlunder, needed_plunder):
    if totalPlunder >= needed_plunder:
        return f"Ahoy! {totalPlunder:.2f} plunder gained."
    else:
        return f"Collected only {(totalPlunder / needed_plunder) * 100:.2f}% of the plunder."


days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
totalPlunder = 0

for day in range(1, days + 1):
    current_plunder = plunder_count(daily_plunder, day)
    totalPlunder += current_plunder

    if day % 5 == 0:
        totalPlunder *= 0.70

print(final_result(totalPlunder, expected_plunder))

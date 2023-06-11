days = int(input())
daily_plunder = int(input())
plunder_target = float(input())

total_plunder = 0

for i in range(1, days + 1):
    if i % 3 == 0:
        if i % 5 != 0:
            total_plunder += (daily_plunder * 1.5)
        elif i % 5 == 0:
            total_plunder += (daily_plunder * 1.5)
            total_plunder *= 0.70
    elif i % 5 == 0 and i % 3 != 0:
        total_plunder += daily_plunder
        total_plunder *= 0.70
    else:
        total_plunder += daily_plunder

if total_plunder >= plunder_target:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(total_plunder / plunder_target) * 100:.2f}% of the plunder.")
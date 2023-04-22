fire_type = input()
water = int(input())

list_fire_type = [str(ch) for ch in fire_type.strip().split("#")]

effort = 0
total_fire = 0

print("Cells:")
for i in range(len(list_fire_type)):
    current_list = [str(i) for i in list_fire_type[i].strip().split()]
    for n in range(len(current_list)):
        if current_list[n] == "High":
            if 81 <= int(current_list[2]) <= 125 and int(current_list[2]) <= water:
                water -= int(current_list[2])
                total_fire += int(current_list[2])
                effort += (int(current_list[2]) * 0.25)
                print(f" - {int(current_list[2])}")
        elif current_list[n] == "Medium":
            if 51 <= int(current_list[2]) <= 80 and int(current_list[2]) <= water:
                water -= int(current_list[2])
                total_fire += int(current_list[2])
                effort += (int(current_list[2]) * 0.25)
                print(f" - {int(current_list[2])}")
        elif current_list[n] == "Low":
            if 1 <= int(current_list[2]) <= 50 and int(current_list[2]) <= water:
                water -= int(current_list[2])
                total_fire += int(current_list[2])
                effort += (int(current_list[2]) * 0.25)
                print(f" - {int(current_list[2])}")
        else:
            continue

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

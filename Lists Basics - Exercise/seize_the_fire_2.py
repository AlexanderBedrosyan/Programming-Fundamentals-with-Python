def effort_fire(chart, final_list, water, effort, total_fire):
    type, power = chart.split(" = ")
    if water >= int(power):
        water -= int(power)
        total_fire += int(power)
        effort += (int(power) * 0.25)
        final_list.append(int(power))
    return effort, total_fire, water, final_list


def if_pass(chart, dict):
    option, power = chart.split(" = ")
    flag = True
    if int(power) not in dict[option]:
        flag = False
    return flag


type_of_fire = {"High": range(81, 126), "Medium": range(51, 81), "Low": range(1, 51)}
list_fire = [ch for ch in input().split("#")]
water = int(input())
final_list = []
effort = 0
total_fire = 0

while len(list_fire) > 0:
    chart = list_fire.pop(0)
    if if_pass(chart, type_of_fire):
        effort, total_fire, water, final_list = effort_fire(chart, final_list, water, effort, total_fire)

print("Cells:")
for ch in final_list:
    print(f"- {ch}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

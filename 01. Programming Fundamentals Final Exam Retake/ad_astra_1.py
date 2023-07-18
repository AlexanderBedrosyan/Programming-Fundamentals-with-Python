import re

the_code = input()

pattern = r'(\#|\|)([a-zA-Z\s]+)\1([0-9]{2}[\/]{1}[0-9]{2}[\/]{1}[0-9]{2})\1(10000|[0-9]{1,4})\1'
food_list = []
dates_list = []
calories_list = []
CALORIES_PER_DAY = 2000

foods_tuple = re.findall(pattern, the_code)

for i in range(len(foods_tuple)):
    food_list.append(foods_tuple[i][1])
    dates_list.append(foods_tuple[i][2])
    calories_list.append(int(foods_tuple[i][3]))

print(f'You have food to last you for: {sum(calories_list) // CALORIES_PER_DAY} days!')
if (sum(calories_list) //  CALORIES_PER_DAY) > 0:
    for i in range(len(food_list)):
        print(f"Item: {food_list[i]}, Best before: {dates_list[i]}, Nutrition: {calories_list[i]}")
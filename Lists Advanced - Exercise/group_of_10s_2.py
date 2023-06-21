def dict_creation(current_list):
    final_group = max(current_list) // 10 + 1
    if max(current_list) % 10 == 0:
        final_group = max(current_list) // 10
    the_dict = {}
    while final_group:
        the_dict[final_group * 10] = []
        final_group -= 1
    return the_dict


def group_counter_list_modifier(group_dict, number):
    needed_key = (number // 10 + 1) * 10
    if number % 10 == 0:
        needed_key = (number // 10) * 10
    group_dict[needed_key].append(number)
    return group_dict


current_list = [int(ch) for ch in input().split(", ")]
group_dict = dict_creation(current_list)

for item in current_list:
    group_dict = group_counter_list_modifier(group_dict, item)

for key, values in sorted(group_dict.items()):
    print(f"Group of {key}'s: {values}")

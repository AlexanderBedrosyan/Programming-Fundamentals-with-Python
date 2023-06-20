def array_modifier(current_integer, final_list):
    position = len(final_list) + 1
    needed_result = 2 * (position ** 2)
    if needed_result > current_integer:
        needed_result = current_integer
    final_list.append(needed_result)
    return current_integer - needed_result, final_list


current_integer = int(input())
final_list = []

while current_integer:
    current_integer, final_list = array_modifier(current_integer, final_list)

print(final_list)

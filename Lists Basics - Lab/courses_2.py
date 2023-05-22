def courses(*args):
    current_list = []
    for ch in args[0]:
        current_list.append(ch)
    return current_list


num = int(input())
print(courses([input() for _ in range(num)]))
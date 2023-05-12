def final_result():
    current_list = []
    for _ in range(3):
        current_list.append(int(input()))
    print(max(current_list))


final_result()
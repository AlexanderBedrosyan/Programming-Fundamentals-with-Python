def next_happy_year(starting_year):
    new_year = 0
    new_number_list = []
    counter_list = []

    final_list = []
    while True:
        starting_year += 1
        new_year = starting_year
        while new_year > 0:
            new_number_list.append(new_year % 10)
            new_year = new_year // 10
            if new_year == 0:
                for item in new_number_list:
                    if new_number_list.count(item) > 1:
                        counter_list.append(item)
                break
        if not counter_list:
            for i in range(len(new_number_list) - 1, - 1, -1):
                final_list.append(new_number_list[i])
                if i == 0:
                    print(*final_list, sep="")
                    exit()
        else:
            new_number_list = []
            counter_list = []
            continue


next_happy_year(int(input()))
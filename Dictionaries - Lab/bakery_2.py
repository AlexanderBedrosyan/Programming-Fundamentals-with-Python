def dictionary_creation(starting_list):
    current_dict = {}
    for i in range(0, len(starting_list), 2):
        current_dict[starting_list[i]] = int(starting_list[i + 1])
    return current_dict


starting_list = input().split(" ")
baker_dict = dictionary_creation(starting_list)

print(baker_dict)

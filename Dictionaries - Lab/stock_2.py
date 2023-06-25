def dictionary_creation(current_list):
    new_dict = {}
    for i in range(0, len(current_list), 2):
        new_dict[current_list[i]] = current_list[i + 1]
    return new_dict


def result(element, current_dict):
    if element in current_dict:
        return f"We have {current_dict[element]} of {element} left"
    else:
        return f"Sorry, we don't have {element}"


starting_list = input().split()
stock_dict = dictionary_creation(starting_list)
stock_list = input().split()

for ch in stock_list:
    print(result(ch, stock_dict))

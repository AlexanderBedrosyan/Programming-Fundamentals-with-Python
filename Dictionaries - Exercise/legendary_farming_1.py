stocks_dict = {}
winner = ""

stocks_dict["shards"] = 0
stocks_dict["fragments"] = 0
stocks_dict["motes"] = 0


while True:
    list_of_stocks = input().split(" ")

    for i in range(1, len(list_of_stocks), 2):
        if "shards" in stocks_dict:
            if stocks_dict["shards"] >= 250:
                break
        if "fragments" in stocks_dict:
            if stocks_dict["fragments"] >= 250:
                break
        if "motes" in stocks_dict:
            if stocks_dict["motes"] >= 250:
                break
        if list_of_stocks[i].lower() not in stocks_dict:
            stocks_dict[list_of_stocks[i].lower()] = int(list_of_stocks[i - 1])
        else:
            stocks_dict[list_of_stocks[i].lower()] += int(list_of_stocks[i - 1])

    if "shards" in stocks_dict:
        if stocks_dict["shards"] >= 250:
            winner = "Shadowmourne"
            stocks_dict["shards"] -= 250
            break
    if "fragments" in stocks_dict:
        if stocks_dict["fragments"] >= 250:
            winner = "Valanyr"
            stocks_dict["fragments"] -= 250
            break
    if "motes" in stocks_dict:
        if stocks_dict["motes"] >= 250:
            winner = "Dragonwrath"
            stocks_dict["motes"] -= 250
            break

print(f"{winner} obtained!")
if 'shards' in stocks_dict:
    print(f"shards: {stocks_dict['shards']}")
    del stocks_dict["shards"]
if "fragments" in stocks_dict:
    print(f"fragments: {stocks_dict['fragments']}")
    del stocks_dict["fragments"]
if "motes" in stocks_dict:
    print(f"motes: {stocks_dict['motes']}")
    del stocks_dict["motes"]
for key in stocks_dict:
    print(f"{key}: {stocks_dict[key]}")
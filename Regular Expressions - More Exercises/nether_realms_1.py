import re


def dict_modification(dict, name, health_point, damage_point, math_signs):
    health = 0
    damage = 0
    if name not in dict:
        dict[name] = {}
    if len(health_point) > 0:
        for ch in health_point:
            health += ord(ch)
    if len(damage_point) > 0:
        for i in range(len(damage_point)):
            for ch in range(len(damage_point[i])):
                if damage_point[i][ch] != "":
                    damage += float(damage_point[i][ch])
    if len(math_signs) > 0:
        for item in math_signs:
            if item == "/":
                damage /= 2
            elif item == "*":
                damage *= 2
    dict[name][health] = damage
    return dict


word = re.split(", *", input())

pattern_ascii = r'[^\+\-\*\/\.\d]'
pattern_numbers = r'([\-\+]?[0-9]+[\.][0-9]+)|([\-\+]?[0-9]+)'
pattern_special_symbols = r'[\/\*]'

game_dict = {}

for i in range(len(word)):
    name = word[i].strip()

    find_ascci = re.findall(pattern_ascii, name)
    find_numbers = re.findall(pattern_numbers, name)
    find_symbols = re.findall(pattern_special_symbols, name)

    game_dict = dict_modification(game_dict, name, find_ascci, find_numbers, find_symbols)


for key, value in sorted(game_dict.items()):
    for ch in value:
        print(f"{key} - {ch} health, {value[ch]:.2f} damage")

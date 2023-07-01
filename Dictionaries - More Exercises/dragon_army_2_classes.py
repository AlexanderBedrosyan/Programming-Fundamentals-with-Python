class FillTheDragonInfo:
    __default_damage = 45
    __default_health = 250
    __default_armor = 10

    def __init__(self):
        self.information = {}

    def complete_the_information(self):
        num = int(input())
        for _ in range(num):
            type_of_dragon, name, damage, health, armor = input().split(" ")
            if type_of_dragon not in self.information:
                self.information[type_of_dragon] = {}
            self.information[type_of_dragon][name] = {}
            if damage == "null":
                damage = FillTheDragonInfo.__default_damage
            if health == "null":
                health = FillTheDragonInfo.__default_health
            if armor == "null":
                armor = FillTheDragonInfo.__default_armor
            self.information[type_of_dragon][name] = {"damage": int(damage), "health": int(health), "armor": int(armor)}


class GetInfo(FillTheDragonInfo):

    def __init__(self):
        super(GetInfo, self).__init__()

    def final_result(self):
        result = []
        for current_type, new_dict in self.information.items():
            total_damage = 0
            total_health = 0
            total_armor = 0
            counter = 0
            current_result = []
            for name, details_dict in sorted(new_dict.items(), key=lambda x: x[0]):
                counter += 1
                total_damage += details_dict["damage"]
                total_health += details_dict["health"]
                total_armor += details_dict["armor"]
                current_result.append(f"-{name} -> damage: {details_dict['damage']}, health: {details_dict['health']}, "
                                      f"armor: {details_dict['armor']}")
            result.append(f"{current_type}::({total_damage/counter:.2f}/{total_health/counter:.2f}/{total_armor/counter:.2f})")
            for ch in current_result:
                result.append(ch)
        return '\n'.join(result)


needed_info = GetInfo()
needed_info.complete_the_information()
print(needed_info.final_result())

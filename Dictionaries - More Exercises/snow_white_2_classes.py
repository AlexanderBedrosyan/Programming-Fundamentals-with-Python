class FillTheDict:

    def __init__(self):
        self.dwarf_dict = {}
        self.final_results = []

    def fill_the_dwarfs(self):
        command = input()

        while command != "Once upon a time":
            dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")

            if dwarf_hat_color not in self.dwarf_dict:
                self.dwarf_dict[dwarf_hat_color] = {}

            if dwarf_name in self.dwarf_dict[dwarf_hat_color]:
                if self.dwarf_dict[dwarf_hat_color][dwarf_name] < int(dwarf_physics):
                    self.dwarf_dict[dwarf_hat_color][dwarf_name] = int(dwarf_physics)
            else:
                self.dwarf_dict[dwarf_hat_color][dwarf_name] = int(dwarf_physics)

            command = input()

    def create_the_final_result_list(self):
        for hat, current_dict in self.dwarf_dict.items():
            for dwarf, power in current_dict.items():
                self.final_results.append({"name": dwarf, "physics": power, "hat": hat, "count_of_dwarfs": len(current_dict)})


class GetResult(FillTheDict):

    def __init__(self):
        super(GetResult, self).__init__()

    def final_result(self):
        result = []
        for item in sorted(self.final_results, key=lambda x: (-x["physics"], -x["count_of_dwarfs"])):
            result.append(f"({item['hat']}) {item['name']} <-> {item['physics']}")
        return '\n'.join(result)


get_result = GetResult()
get_result.fill_the_dwarfs()
get_result.create_the_final_result_list()
print(get_result.final_result())

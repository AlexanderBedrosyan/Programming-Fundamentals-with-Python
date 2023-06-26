class GetMiner():

    def __repr__(self):
        final_result = []
        current_dict = {}
        command = input()
        counter = 0
        current_miner = ''

        while command != "stop":
            counter += 1
            if counter == 1:
                if command not in current_dict:
                    current_dict[command] = 0
                current_miner = command
            elif counter == 2:
                current_dict[current_miner] += int(command)
                current_miner = ''
                counter = 0

            command = input()

        for miner, quantity in current_dict.items():
            final_result.append(f"{miner} -> {quantity}")

        return '\n'.join(final_result)


print(GetMiner())

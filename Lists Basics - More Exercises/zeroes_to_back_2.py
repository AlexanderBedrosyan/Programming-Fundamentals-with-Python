class ZeroesToBack():

    def __init__(self, current_list, amount_zeros):
        self.current_list = current_list
        self.amount_zeroes = amount_zeros

    def new_list(self):
        for i in range(self.amount_zeroes):
            self.current_list.remove(0)
            self.current_list.append(0)

        return f"{self.current_list}"


starting_integers = [int(ch) for ch in input().split(", ")]
zeros = starting_integers.count(0)

final_result = ZeroesToBack(starting_integers, zeros)
print(final_result.new_list())
class Ascii_symbols():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def change_in_symbols(self):
        self.symbols = [chr(ch) for ch in range(self.start, self.end + 1)]
        return ' '.join(chart for chart in self.symbols)


starting_symbol, ending_symbol = int(input()), int(input())
final_string = Ascii_symbols(starting_symbol, ending_symbol)
print(final_string.change_in_symbols())

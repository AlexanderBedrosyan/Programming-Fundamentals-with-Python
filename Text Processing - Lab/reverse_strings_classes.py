class ReverseStrings:

    def __init__(self):
        self.words = []
        self.index = 0

    def fill_the_list(self):
        command = input()

        while command != "end":

            self.words.append(f"{command} = {command[::-1]}")

            command = input()

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.words):
            raise StopIteration
        else:
            return self.words[self.index - 1]


final_result = ReverseStrings()
final_result.fill_the_list()
for ch in final_result:
    print(ch)

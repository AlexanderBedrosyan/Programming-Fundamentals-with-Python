from timeit import default_timer as tm


start = tm()


class RepeatString:

    def __init__(self, string_input):
        self.string_input = string_input
        self.result = ''

    def concatenate_string(self):
        new_word = ''
        self.string_input = self.string_input.split(" ")
        for ch in self.string_input:
            new_word += (ch * len(ch))
        self.result = new_word

    def __str__(self):
        return self.result


repeat_string = RepeatString(input())
repeat_string.concatenate_string()
print(repeat_string)

end = tm()
print(start - end)

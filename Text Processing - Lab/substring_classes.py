class Substring:

    def __init__(self, sub_string, word):
        self.sub_string = sub_string
        self.word = word

    def result(self):
        while self.sub_string in self.word:
            self.word = self.word.replace(self.sub_string, "")

    def __str__(self):
        return self.word


word_without_substring = Substring(input(), input())
word_without_substring.result()
print(word_without_substring)

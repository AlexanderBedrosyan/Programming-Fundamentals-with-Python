class TextFilter:

    def __init__(self, words_for_crypting, text):
        self.words_for_crypting = words_for_crypting
        self.text = text

    def result(self):
        list_of_words = self.words_for_crypting.split(", ")
        for ch in list_of_words:
            num = len(ch)
            while ch in self.text:
                current_word = self.text.replace(ch, f"{num * '*'}")
                self.text = current_word

    def __repr__(self):
        return f"{self.text}"


words_for_change = input()
text = input()
text_filter = TextFilter(words_for_change, text)
text_filter.result()
print(text_filter)

class TextMultiply:

    def __init__(self, current_list):
        self.list_of_text: list = current_list
        self.amount = 0

    def count_the_amount(self):
        first_word = self.list_of_text[0]
        second_word = self.list_of_text[1]

        while first_word or second_word:
            letter_first_word = None
            letter_second_word = None
            if first_word:
                letter_first_word = ord(first_word[0])
                first_word = first_word[1:]
            if second_word:
                letter_second_word = ord(second_word[0])
                second_word = second_word[1:]

            if letter_first_word and letter_second_word:
                self.amount += (letter_second_word * letter_first_word)
            elif letter_first_word and not letter_second_word:
                self.amount += letter_first_word
            elif not letter_first_word and letter_second_word:
                self.amount += letter_second_word

    def __repr__(self):
        return f"{self.amount}"


text = input().split(" ")
total_amount = TextMultiply(text)
total_amount.count_the_amount()
print(total_amount)

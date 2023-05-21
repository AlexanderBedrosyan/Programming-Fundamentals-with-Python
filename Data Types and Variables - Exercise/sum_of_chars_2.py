class Sum_of_chars():

    def __init__(self, letters):
        self.letters = letters

    def final_result(self):
        return sum(self.letters)


n = int(input())
letters = [ord(input()) for _ in range(n)]
total_amount = Sum_of_chars(letters)
print(f"The sum equals: {total_amount.final_result()}")

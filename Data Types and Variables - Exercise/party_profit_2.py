class Party_profit():
    day_coins = 50
    earn_coins = 0

    def __init__(self, members, days):
        self.members = members
        self.days = days

    def profit(self):
        for i in range(1, self.days + 1):
            if i % 10 == 0:
                self.members -= 2
            if i % 15 == 0:
                self.members += 5

            self.earn_coins += 50
            self.earn_coins -= (2 * self.members)

            if i % 3 == 0:
                self.earn_coins -= (3 * self.members)
            if i % 5 == 0:
                self.earn_coins += (20 * self.members)
                if i % 3 == 0:
                    self.earn_coins -= (2 * self.members)
        return f"{self.members} companions received {self.earn_coins // self.members} coins each."


total_profit = Party_profit(int(input()), int(input()))
print(total_profit.profit())

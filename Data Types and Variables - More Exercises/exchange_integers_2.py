class ExchangeIntegers:

    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two
        
    def exchange(self):
        return f"Before:\na = {self.number_one}\nb = {self.number_two}\n After:\na = {self.number_two}\nb = " \
               f"{self.number_one}"


exchange_result = ExchangeIntegers(int(input()), int(input()))
print(exchange_result.exchange())

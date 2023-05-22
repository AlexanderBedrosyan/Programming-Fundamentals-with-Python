class PrimeNumberChecker:

    def __init__(self, number):
        self.number = number

    def prime_checker(self):
        checker = True
        for integer in range(2, self.number):
            if self.number % integer == 0:
                checker = False
        return checker


prime_number_checker = PrimeNumberChecker(int(input()))
print(prime_number_checker.prime_checker())

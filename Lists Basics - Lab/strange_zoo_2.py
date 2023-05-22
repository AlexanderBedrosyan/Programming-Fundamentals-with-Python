class StrangeZoo:

    def __init__(self, list):
        self.list = list

    def result(self):
        print(self.list)


strange_zoo = [input() for _ in range(3)]
final_result = StrangeZoo(strange_zoo[::-1])
final_result.result()

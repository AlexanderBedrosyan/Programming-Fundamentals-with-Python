class BalancedBrackets:

    def __init__(self, number):
        self.number = number

    def brackets_checker(self):
        balanced = "BALANCED"
        brackets_needed = "()"
        current_brackets = ""
        for i in range(self.number):
            command = input()
            if command == "(" or command == ")":
                current_brackets += command
            if len(current_brackets) == 2 :
                if current_brackets == brackets_needed:
                    current_brackets = ""
                else:
                    balanced = "UNBALANCED"
                    break
        return balanced


brackets_finder = BalancedBrackets(int(input()))
print(brackets_finder.brackets_checker())

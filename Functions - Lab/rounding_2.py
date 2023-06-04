final_result = lambda x: round(x)

current_result = [float(ch) for ch in input().split(" ")]
variable = "["
for i in range(len(current_result)):
    if i == len(current_result) - 1:
        variable += f"{final_result(current_result[i])}"
        break
    variable += f"{final_result(current_result[i])}, "

variable += "]"
print(variable)

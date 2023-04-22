factor = int(input())
count = int(input())

factor_list = []
factor_number = 0

for i in range(count):
    factor_number += factor
    factor_list.append(factor_number)

print(factor_list)

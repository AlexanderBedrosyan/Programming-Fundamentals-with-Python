symbols = input()
numbers = int(input())

symbols_list = [str(ch) for ch in symbols.strip().split()]
first_half = []
second_half = []
num1 = ""
lastnum = ""

for i in range(0, len(symbols_list)):
    if i == 0:
        num1 = symbols_list[i]
        continue
    elif i == (len(symbols_list) - 1):
        lastnum = symbols_list[i]
        symbols_list = []
        break
    elif i < (len(symbols_list) // 2):
        first_half.append(symbols_list[i])
    elif i >= (len(symbols_list) // 2):
        second_half.append(symbols_list[i])

while numbers > 0:
    for n in range(0, len(first_half)):
        symbols_list.append(second_half[n])
        symbols_list.append(first_half[n])

    first_half = []
    second_half = []
    numbers -= 1

    if numbers > 0:
        for digits in range(0, len(symbols_list)):
            if digits < (len(symbols_list) // 2):
                first_half.append(symbols_list[digits])
            elif digits >= (len(symbols_list) // 2):
                second_half.append(symbols_list[digits])
        symbols_list = []

symbols_list.insert(0, num1)
symbols_list.insert(len(symbols_list), lastnum)

print(symbols_list)

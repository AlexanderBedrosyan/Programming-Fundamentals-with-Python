import re

pattern = r'(\%)([A-Z][a-z]+)(\%)([^\|\$\%\.]*)?(\<)(\w+)(\>)([^\|\$\%\.]*)?(\|)([0-9]+)(\|)([^\|\$\%\.]*)?([1-9]+[.0-9]*)(\$)'

total = 0

while True:
    information = input()

    if information == "end of shift":
        break
    customer = 0
    product = 0
    count = 0
    price = 0

    list_of_information = re.findall(pattern, information)
    if len(list_of_information) > 0:
        for i in list_of_information[0]:
            index = list_of_information[0].index(i)
            if i == "%" and list_of_information[0][index + 2] == "%":
                customer = list_of_information[0][index + 1]
            if i == "<" and list_of_information[0][index + 2] == ">":
                product = list_of_information[0][index + 1]
            if i == "|" and list_of_information[0][index + 2] == "|":
                count = int(list_of_information[0][index + 1])
            if i == "$":
                price = float(list_of_information[0][index-1])

        print(f"{customer}: {product} - {count * price:.2f}")
    total += (count * price)


print(f"Total income: {total:.2f}")
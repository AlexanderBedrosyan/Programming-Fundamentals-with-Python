def final_result(large, small, num):
    final_result = ""
    if abs(num) > large:
        final_result += "large "
    elif 0 < abs(num) < small:
        final_result += "small "

    if num > 0:
        final_result += "positive"
    elif num < 0:
        final_result += "negative"
    else:
        final_result += "zero"

    print(final_result)


number = float(input())
large = 1_000_000
small = 1

final_result(large, small, number)
# Write a program that receives a number n on the first line. On the following n lines, it receives different integer
# # numbers. If the program receives an odd number, print "{num} is odd!" and end the program. Otherwise, if all
# # numbers given are even, print "All numbers are even.".


def even_or_odd(num):
    final_result = "All numbers are even."
    for i in range(num):
        current_number = int(input())
        if current_number % 2 == 0:
            continue
        else:
            final_result = f"{current_number} is odd!"
            break
    return final_result


num = int(input())

print(even_or_odd(num))

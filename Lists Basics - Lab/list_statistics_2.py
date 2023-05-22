def list_statistics(*args):
    positive_numbers = []
    negative_numbers = []
    for ch in args[0]:
        if ch >= 0:
            positive_numbers.append(ch)
        else:
            negative_numbers.append(ch)
    print(positive_numbers)
    print(negative_numbers)
    return len(positive_numbers), sum(negative_numbers)


num = int(input())
count_positives, sum_negatives = list_statistics([int(input()) for _ in range(num)])
print(f"Count of positives: {count_positives}\nSum of negatives: {sum_negatives}")
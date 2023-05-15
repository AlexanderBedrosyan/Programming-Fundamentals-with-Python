distribution = [int(ch) for ch in input().split(", ")]
min_distribution = int(input())

sum_added = 0

for i in range(0, len(distribution)):
    if (sum(distribution) // min_distribution) < len(distribution):
        print("No equal distribution possible")
        exit()

    if distribution[i] < min_distribution:
        sum_added += (min_distribution - distribution[i])
        distribution[i] = min_distribution

    while sum_added > 0:
        index = distribution.index(max(distribution))
        if (sum_added + min_distribution) <= max(distribution):
            distribution[index] -= sum_added
            sum_added = 0
        else:
            distribution[index] -= min_distribution
            sum_added -= distribution[index]
            distribution[index] = min_distribution

print(distribution)
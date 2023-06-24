def increase_the_less_social_number(max_number, ind_min_number, ind_max_number,
                                    social_distribution, rate_of_social_equality):
    difference_needed = rate_of_social_equality - min_number
    if (max_number - difference_needed) >= rate_of_social_equality:
        social_distribution[ind_max_number] -= difference_needed
        social_distribution[ind_min_number] += difference_needed
    else:
        add_amount = max_number - rate_of_social_equality
        social_distribution[ind_min_number] += add_amount
        social_distribution[ind_max_number] -= add_amount
    return social_distribution


def final_result(social_distribution, rate_of_social_equality):
    if min(social_distribution) >= rate_of_social_equality:
        return social_distribution
    else:
        return "No equal distribution possible"


social_distribution = [int(ch) for ch in input().split(", ")]
rate_of_social_equality = int(input())

while min(social_distribution) != rate_of_social_equality and max(social_distribution) != rate_of_social_equality:
    min_number = min(social_distribution)
    ind_min_number = social_distribution.index(min_number)
    max_number = max(social_distribution)
    ind_max_number = social_distribution.index(max_number)

    social_distribution = increase_the_less_social_number(max_number, ind_min_number, ind_max_number,
                                                          social_distribution, rate_of_social_equality)

print(final_result(social_distribution, rate_of_social_equality))

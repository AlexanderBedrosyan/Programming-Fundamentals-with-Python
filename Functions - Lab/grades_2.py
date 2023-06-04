def print_the_result(result_in_word):
    print(result_in_word)


def grade_in_word(dict_of_grades, current_grade):
    result = ''
    for word_grade, range in dict_of_grades.items():
        if range[0] <= current_grade <= range[1]:
            result = word_grade
    print_the_result(result)


grades_dict = {
    "Fail": [2, 3],
    "Poor": [3, 3.50],
    "Good": [3.50, 4.49],
    "Very Good": [4.50, 5.49],
    "Excellent": [5.50, 6]
}

grade = float(input())
grade_in_word(grades_dict, grade)
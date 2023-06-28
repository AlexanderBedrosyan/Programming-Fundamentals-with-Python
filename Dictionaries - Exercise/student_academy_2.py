class GetFinalResult():

    def __init__(self, final_dict):
        self.final_dict = final_dict

    def __repr__(self):
        result_in_list = []
        for student, grades in self.final_dict.items():
            if sum(grades) / len(grades) >= 4.50:
                result_in_list.append(f"{student} -> {sum(grades) / len(grades):.2f}")
        return '\n'.join(result_in_list)


def student_grades(current_dict, student, grade):
    if student not in current_dict:
        current_dict[student] = []
    current_dict[student].append(grade)
    return current_dict


num_of_pairs = int(input())
grades = {}

for _ in range(num_of_pairs):
    name = input()
    result = float(input())
    grades = student_grades(grades, name, result)

print(GetFinalResult(grades))

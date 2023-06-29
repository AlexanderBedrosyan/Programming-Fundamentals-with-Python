class FinalResult():

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def result(self):
        final_result = []
        for course, student in self.dictionary.items():
            final_result.append(f"{course}: {len(student)}")
            for element in student:
                final_result.append(f"-- {element}")
        return final_result


class GetInfo():

    def __init__(self, course_name, student, current_dict):
        self.course_name = course_name
        self.student = student
        self.current_dict = current_dict

    def check_the_dict(self):
        if self.course_name not in self.current_dict:
            self.current_dict[self.course_name] = []
        self.current_dict[self.course_name].append(self.student)
        return self.current_dict


def information_in_dict():
    current_dict = {}

    command = input()

    while command != "end":
        course_name, registered_students = command.split(" : ")
        result = GetInfo(course_name, registered_students, current_dict)
        current_dict = result.check_the_dict()

        command = input()

    final_result = FinalResult(current_dict)

    return final_result.result()


print('\n'.join(information_in_dict()))

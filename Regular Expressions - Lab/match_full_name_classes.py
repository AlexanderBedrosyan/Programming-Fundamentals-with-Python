import re


def correct_name(func):
    def wrapper(string_of_names):
        pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
        matches = re.findall(pattern, string_of_names)
        return ' '.join(matches)
    return wrapper


@correct_name
def full_name_function(name):
    return name


print(full_name_function(input()))

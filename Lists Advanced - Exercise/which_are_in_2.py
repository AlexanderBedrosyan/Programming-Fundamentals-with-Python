def final_result(needed_string, second_string):
    result = []
    for ch in needed_string:
        for item in second_string:
            if ch in item:
                result.append(ch)
                break
    return result


needed_strings = [ch for ch in input().split(", ")]
second_string = [ch for ch in input().split(", ")]

print(final_result(needed_strings, second_string))

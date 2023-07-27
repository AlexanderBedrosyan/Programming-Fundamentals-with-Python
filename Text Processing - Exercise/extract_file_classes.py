class ExtractFile:

    def __init__(self, current_list):
        self.list_of_path: list = current_list

    def __repr__(self):
        result = []
        new_list = self.list_of_path[-1].split(".")
        result.append(f"File name: {new_list[0]}")
        result.append(f"File extension: {new_list[1]}")
        return '\n'.join(result)


list_text = input().split("\\")
file_path = ExtractFile(list_text)
print(file_path)

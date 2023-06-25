class CreatTheDictionary():

    def __init__(self, current_list):
        self.current_list = current_list

    def new_dictionary(self):
        final_dictionary = {}
        for elements in self.current_list:
            if elements not in final_dictionary:
                final_dictionary[elements] = 0
            final_dictionary[elements] += 1
        return final_dictionary


class GetResult():

    def __init__(self, final_dict):
        self.final_dict = final_dict

    def __repr__(self):
        final_result = []
        for key, value in self.final_dict.items():
            if value % 2 != 0:
                final_result.append(key)
        return ' '.join(final_result)


sequence_of_words = [ch.lower() for ch in input().split(" ")]
current_dict = CreatTheDictionary(sequence_of_words)
dictionary_of_elements = current_dict.new_dictionary()
print(GetResult(dictionary_of_elements))

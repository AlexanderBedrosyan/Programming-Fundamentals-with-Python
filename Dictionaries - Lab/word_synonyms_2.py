class SynonymsDict():

    def __init__(self, num_of_synonyms):
        self.num_of_synonyms = num_of_synonyms

    def dict_creation(self):
        synonyms_dict = {}
        condition = False
        key_needed = True
        current_key_word = ''
        for i in range(2 * self.num_of_synonyms):
            command = input()
            if command in synonyms_dict:
                current_key_word = command
                key_needed = False
                continue

            if key_needed:
                synonyms_dict[command] = []
                current_key_word = command
                key_needed = False
            else:
                synonyms_dict[current_key_word].append(command)
                key_needed = True

        return synonyms_dict


current_result = SynonymsDict(int(input()))
synonyms_dict = current_result.dict_creation()

for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")

class Pianist:

    def __init__(self):
        self.classic_pieces = {}
        self.final_result = []
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > len(self.final_result):
            raise StopIteration
        else:
            return self.final_result[self.counter - 1]

    def add(self, piece, composer, key):
        if piece not in self.classic_pieces:
            self.classic_pieces[piece] = {}
            self.classic_pieces[piece][composer] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    def remove(self, piece):
        if piece in self.classic_pieces:
            del self.classic_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    def changekey(self, piece, new_key):
        if piece in self.classic_pieces:
            for composer, key in self.classic_pieces[piece].items():
                self.classic_pieces[piece][composer] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    def get_starting_pieces(self):
        number_of_pieces = int(input())

        for _ in range(number_of_pieces):
            piece, composer, key = input().split("|")
            self.classic_pieces[piece] = {}
            self.classic_pieces[piece][composer] = key

    def preparing_the_final_dict(self):
        command = input()

        while command != "Stop":
            information = command.split("|")
            if information[0] == "Add":
                self.add(information[1], information[2], information[3])
            elif information[0] == "Remove":
                self.remove(information[1])
            elif information[0] == "ChangeKey":
                self.changekey(information[1], information[2])
            command = input()

    def final_result_preparation(self):
        for piece, current_dict in self.classic_pieces.items():
            for composer, key in current_dict.items():
                self.final_result.append(f"{piece} -> Composer: {composer}, Key: {key}")


pianist_list_info = Pianist()
pianist_list_info.get_starting_pieces()
pianist_list_info.preparing_the_final_dict()
pianist_list_info.final_result_preparation()
for item in pianist_list_info:
    print(item)

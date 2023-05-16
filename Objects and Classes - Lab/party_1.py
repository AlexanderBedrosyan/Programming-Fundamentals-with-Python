class OnePerson:

    def __init__(self, name):
        self.name = name


class Party:

    def __init__(self):
        self.party_list = []

    def invite(self, new_person):
        self.party_list.append(new_person)

    def peoplelist(self):
        return ', '.join([new_person.name for new_person in self.party_list])

    def counter(self):
        return len(self.party_list)



party = Party()

while True:
    command = input()

    if command == "End":
        break

    name = command
    new_person = OnePerson(name)
    party.invite(new_person)

print(f"Going: {party.peoplelist()}")
print(f"Total: {party.counter()}")
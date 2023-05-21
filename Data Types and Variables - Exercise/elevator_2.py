class Tours:

    def __init__(self, people, elevator):
        self.people = people
        self.elevator = elevator

    def needed_tours(self):
        if self.people % self.elevator != 0:
            return self.people // self.elevator + 1
        else:
            return self.people // self.elevator


people = int(input())
elevator = int(input())
final_result = Tours(people, elevator)
print(final_result.needed_tours())
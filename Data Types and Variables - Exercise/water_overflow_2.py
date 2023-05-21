class Fill_tank():
    tank_capacity = 255
    water_in_tank = 0

    def __init__(self, n):
        self.n = n

    def result(self):
        for i in range(self.n):
            current_water = int(input())
            if self.tank_capacity >= current_water:
                self.tank_capacity -= current_water
                self.water_in_tank += current_water
            else:
                print("Insufficient capacity!")
        return f"{self.water_in_tank}"


number = int(input())
total_number = Fill_tank(number)
print(total_number.result())

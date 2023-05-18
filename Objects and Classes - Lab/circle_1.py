class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return 2 * self.__pi * (self.diameter / 2)

    def calculate_area(self):
        return self.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle):
        return self.calculate_area() * (angle / 360)


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

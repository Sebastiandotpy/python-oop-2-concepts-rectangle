import math

class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

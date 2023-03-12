"""
Write a Python class named Circle consisting of an instance attribute radius
and two methods which will compute the area and the perimeter of a circle.
Note: import and use the constant pi from the math module.

"""
import math
class Circle():
    PI = math.pi
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.__class__.PI * self.radius **2


    def calculate_perimeter(self):
        return 2*self.__class__.PI*self.radius

circle = Circle(5)
print(f'perimeter : {circle.calculate_perimeter()}')
print(f'area : {circle.calculate_area()}')

#Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
import math
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius * self.radius
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

r = int(input("Enter Radius:"))
x = circle(r)
ax = x.area()
px = x.perimeter()

print("Radius :",r)
print("Area :",ax)
print("Perimeter:",px)

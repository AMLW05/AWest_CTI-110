# Angela Westmoreland
# Date
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print()
print("The diameter of the circle is " + format(diameter, ".1f"))
print("The circumference of the circle is " + format(circumference, ".2f"))
print("The area of the circle is " + format(area, ".3f"))
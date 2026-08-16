# Write circle_calc() function that takes radius of a circle as an input from user
# and then it calculates and returns area, circumference and diameter. You should
# get these values in your main program by calling circle_calc function and then
# print them
import math


def circle_calc(radius):

    area = math.pi * radius**2
    circumfrence = 2 * math.pi * radius
    diameter = radius * 2

    return area, circumfrence, diameter


input_user = int(input("Enter circle's radius here: "))
area, circumfrence, diameter = circle_calc(input_user)

print(f"Circle's Area is: {area:.2f}")
print(f"Circle's circumfrence is: {circumfrence:.2f}")
print(f"Circle's diamter is: {diameter:.2f}")

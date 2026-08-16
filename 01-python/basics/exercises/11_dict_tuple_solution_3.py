# Write circle_calc() function that takes radius of a circle as an input from user
# and then it calculates and returns area, circumference and diameter. You should
# get these values in your main program by calling circle_calc function and then
# print them
import math


def circle_calc(radius):

    area = math.pi * radius**2
    circumfrence = 2 * math.pi * radius
    diameter = radius * 2

    return [area, circumfrence, diameter]


input_user = int(input("Enter circle's radius here: "))
ans = circle_calc(input_user)

print(f"Circle's Area is: {ans[0]:.2f}")
print(f"Circle's circumfrence is: {ans[1]:.2f}")
print(f"Circle's diamter is: {ans[2]:.2f}")

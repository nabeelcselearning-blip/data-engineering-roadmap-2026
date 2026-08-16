# def calculate_area(base, height):
#     area = 0.5 * base * height
#     return area


def calculate_area_2(base, height, shape_type="triangle"):

    if shape_type == "triangle":
        area = 0.5 * base * height

    elif shape_type == "rectangle":
        area = base * height

    return area


base = float(input("Enter base/length: "))
height = float(input("Enter height/width: "))
shape_type = (
    input("Enter shape (triangle/rectangle): ") or "triangle"
)  # new to me, if input is emty string thn by default it will store triangle in variable
# A or B means in Python "If A has a value, use A. Otherwise, use B."

# print(calculate_area(base, height))
print(f"Area of {shape_type} is {calculate_area_2(base, height, shape_type)}")


def pattern(num):

    for i in range(num):
        for j in range(0, i + 1):
            print("*", end="")
        print()


num = int(input("Enter a number to generate pattern: "))
pattern(num)

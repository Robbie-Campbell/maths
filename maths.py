import math


def circle_algorithm():
    circle = input("Do you need to work out circumference, or radius?(c/r): ")
    if circle == "r":
        r = float(input("Enter the circumference of your circle: "))
        radius = r / (math.pi * 2)
        print("The radius of your circle is: ", radius)
    elif circle == "c":
        c = float(input("Enter the radius of your circle: "))
        circumference = math.pi * math.pow(c, 2)
        print("The circumference of your circle is: ", circumference)


def triangle_algorithm():
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Enter the height of your triangle: "))
    print("The area of your triangle is ", (base * height) / 2)


def sum_of_sides():
    sides = int(input("How many sides does your shape have?: "))
    total = (sides - 2) * 180
    print("The sum of angles is ", total, " Degrees")
    print("And the size of each angle in a regular shape with that many sides is ", total / sides, "Degrees")
    print("And the exterior angle of each side is: ", 360 / sides, "Degrees")


def quad():
    quad_type = input("Is your shape a square, rectangle or trapezium?(s/r/t): ")
    side1 = float(input("Enter a side length: "))
    if quad_type == "s":
        print("The area of your square is ", side1 * side1)
        return
    side2 = float(input("Enter another side length: "))
    if quad_type == "r":
        print("The area of your rectangle is ", side1 * side2)
    elif quad_type == "t":
        height = float(input("Enter the height of the trapezium: "))
        print("The area of your trapezium is ", ((side2 + side1)/2) * height)


math_type = input("Do you need to work out a quadrilateral, circle, the sum of angles or a triangle?(q/c/s/t): ")
if math_type == "c":
    circle_algorithm()
elif math_type == "t":
    triangle_algorithm()
elif math_type == "s":
    sum_of_sides()
elif math_type == "q":
    quad()

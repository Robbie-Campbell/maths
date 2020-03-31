"""
This is a class which is able to resolve some simple pythagoras/ trigenometry problems, using if else statements,
any calculation as long as 2 sides, or a side and an angle are known the correct answer is output
"""

import math
from maths import run_maths


# Display a tringle in the command line to display the different sides to the user.
print("       /|")
print("      / |")
print("     /  |")
print("  C /   |A")
print("   /    |")
print("  /_____|")
print("a    B   b")
print("b is a right angle.")

# Let the user calculate pythagoras or trigenometry
trig_or_pythagoras = input("Do you want to do trigonomety, pythagoras or something more simple?(t/p/other): " )


# The function for calculating pythagoras
def pythagoras():
    which = input("Which side do you want to find out?(A/B/C): ")
    if which == "C":
        A = math.pow(float(input("Please enter the value of side A: ")),2)
        B = math.pow(float(input("Please enter the value of side B: ")), 2)
        print("The size of side C (Hypotenuese) is: ", math.sqrt(A+B))
    elif which == "B":
        A = math.pow(float(input("Please enter the value of side A: ")), 2)
        C = math.pow(float(input("Please enter the value of side C: ")), 2)
        print("The size of side B (Adjacent) is: ", math.sqrt(math.sqrt(C)- math.sqrt(A)))
    elif which == "A":
        B = math.pow(float(input("Please enter the value of side B: ")), 2)
        C = math.pow(float(input("Please enter the value of side C: ")), 2)
        print("The size of side A (Opposite) is: ", math.sqrt(math.sqrt(C) - math.sqrt(B)))


# The function for working out trigonometry
def trig():

    # Allow the user to calculate a side or an angle
    side_or_angle = input("Do you want to work out a side or an angle?(s/a): ")

    # The function to calculate a side of a right angle triangle
    if side_or_angle == "s":
        for_calculation = input("which side of the triangle do you want to know?(A/B/C): ")
        a = math.radians(float(input("Please enter the degree of a: ")))
        know = input("Which side of the triangle do you know? (A/B/C): ")
        if know == "C":
            C = float(input("Please enter the value of side C: "))
            if for_calculation == "A":
                sin = C / math.sin(a)
                print("The size of side A is: ", sin)
            elif for_calculation == "B":
                cos = C * math.cos(a)
                print("The size of side B is: ", cos)
        elif know == "B":
            B = float(input("Please enter the value of side B: "))
            if for_calculation == "A":
                tan = B * math.tan(a)
                print("The size of side A is: ", tan)
            elif for_calculation == "C":
                cos = B / math.cos(a)
                print("The size of side C is: ", cos)
        elif know == "A":
            A = float(input("Please enter the value of side A: "))
            if for_calculation == "B":
                tan = A * math.tan(a)
                print("The size of side B is: ", tan)
            elif for_calculation == "C":
                sin = A / math.sin(a)
                print("The size of side C is: ", sin)
    elif side_or_angle == "a":
        angle = input("which sides do you know the length of?(1:A/B)(2:B/C)(3:A/C): ")
        if angle == "1":
            A = float(input("Input the length of A "))
            B = float(input("Input the length of B "))
            tan = math.degrees(math.atan(A/B))
            print("The size of the angle a is: ", tan)
        elif angle == "2":
            B = float(input("Input the length of B "))
            C = float(input("Input the length of C "))
            cos = math.degrees(math.acos(B / C))
            print("The size of the angle a is: ", cos)
        elif angle == "3":
            A = float(input("Input the length of A "))
            C = float(input("Input the length of C "))
            sin = math.degrees(math.asin(A / C))
            print("The size of the angle a is: ", sin)


# Runs the different functions
if trig_or_pythagoras == "p":
    pythagoras()
elif trig_or_pythagoras == "t":
    trig()
elif trig_or_pythagoras == "other":
    run_maths()
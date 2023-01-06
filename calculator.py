import math

def squareFootage():
    length = int(input("Enter the length of the house (in feet): "))
    width = int(input("Enter the width of the house (in feet): "))
    area = length * width
    print(f"The area of your house is {area} Ft")


def circumCircle():
    radius = int(input("Enter the radius of your circle (in inches): "))
    circum = radius * math.pi * 2
    print(f"The Circumference of your circle is {math.ceil(circum)} inches long")




# program to determine the distance between two points
# Autor: Chris Williams
import math

def main():
    print("Given two points I can determine the distance between them.")
    x1 = float(input("Please enter the X coordinates for the first point: "))
    y1 = float(input("Please enter the y coordinates for the first point: "))
    x2 = float(input("Please enter the X coordinates for the second point: "))
    y2 = float(input("Please enter the y coordinates for the second point: "))

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("The distance between the two points is", round(distance, 2))


main()
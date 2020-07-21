# A program to find the length of a ladder given the height and the angle
# Author: Chris Williams
import math

def main():
    print("Hello! If you give me a height and an angle I can tell you how long the ladder must be to reach the height.")
    h = float(input("Enter the height:" ))
    a = float(input("Enter the angle(In degrees): "))

    radians = (math.pi *  a) / 180

    length = h / math.sin(radians)

    print("Ladder length:", length)

main()


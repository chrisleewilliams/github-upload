# program to calculate the area of a triangle given the length of its three sides
# Author: Chris Williams
import math

def main():
    print("Hello! If you provide the length of three sides of a triangle I can find the area for you.")
    s1 = float(input("Side 1 length: "))
    s2 = float(input("Side 2 length: "))
    s3 = float(input("Side 3 length: "))

    s = (s1 + s2 + s3) / 2

    a = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

    print("The area of the triangle is", a)

main()


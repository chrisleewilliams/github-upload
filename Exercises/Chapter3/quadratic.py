# quadratic.py
# Program to compute the real roots of a quadratic equation
# Note this program crashes if the equation has no real roots
# Author: Chris Williams

import math

def main():
    print("this program finds the real solutions to to the quadratic equations.")
    print()

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b - discRoot) / (2 * a)
    root2 = (-b + discRoot) / (2 * a)

    print()
    print("The solutions are", round(root1, 3), "and", round(root2, 3))
    input("Press <Enter> to quit the program")

main()
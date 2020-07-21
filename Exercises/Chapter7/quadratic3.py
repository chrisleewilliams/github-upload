# Program to fid the real solutions to a quadratic
# Author: Chris Williams
from math import sqrt

def getVars():
    print("Enter 3 numbers.")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    return a, b, c

def main():
    print("This program finds the real solutions to a quadratic\n")

    a, b, c = getVars()
    discrim = b * b - 4 * a * c 
    if discrim < 0:
        print("This equation has no real roots")
    elif discrim == 0:
        root = -b / (2 * a)
        print(f"print there is a double root at {root}.")
    else:
        discRoot = sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print(f"The soultions are: {root1} {root2}")

main()

# A program to calculate the cost per square inch of a circlular pizza
# Author: Chris Williams
import math

def main():
    print("Hello! Enter a price and diameter to find out the cost per square inch of a pizza.")
    print()
    d = float(input("Diameter: "))
    p = float(input("Price: "))
    
    A = math.pi * (d/2) ** 2

    cost = p / A

    print("The pizza cost", cost, "dollars per square inch")

main()
# A program to calculate the cost per square inch of a circlular pizza
# Author: Chris Williams
from math import pi

def pizzaArea(d):
    return pi * (d/2) ** 2

def pizzaCost(p, d):
    return p / pizzaArea(d)

def main():
    print("Enter a price and diameter to find out the cost per square inch of pizza.")
    d = float(input("Diameter: "))
    p = float(input("Price: "))

    cost = pizzaCost(p, d)


    print("The pizza cost", cost, "dollars per square inch")

main()
# program to calculate the volume and surface area of a sphere from its radius
# Author: Chris Williams

import math

def main():
    r = int(input("Enter in the radius to find the voulme and surface area of a sphere: "))
    v = 4 / 3 * math.pi * (r ** 3)
    a = 4 * math.pi * r ** 2

    print("Volume =", v)
    print("Area =", a)

main()
    
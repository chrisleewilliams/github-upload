# program to return the surface area and volume of a sphere given its radius
# Author: Chris Williams
from math import pi
def sphereArea(r):
    return 4 * pi * r**2

def sphereVolume(r):
    return (4/3) * pi * r ** 3


def main():
    print(sphereArea(4))
    print(sphereVolume(4))

main()

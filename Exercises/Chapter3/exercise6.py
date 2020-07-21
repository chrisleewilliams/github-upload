# program to calculate the slope of a live given two points
# Author: Chris Williams

def main():
    print("Given two points I can calculate the slope of a line.")
    x1 = float(input("Please enter the X coordinates for the first point: "))
    y1 = float(input("Please enter the y coordinates for the first point: "))
    x2 = float(input("Please enter the X coordinates for the second point: "))
    y2 = float(input("Please enter the y coordinates for the second point: "))
    slope = (y2 - y1) / (x2 - x1)    
    print("The slope of the two points is", slope)

main()
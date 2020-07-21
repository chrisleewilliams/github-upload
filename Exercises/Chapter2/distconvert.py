# Program to convert kilometers to miles
# Author: Chris Williams

def main():
    kilometer = eval(input("Enter a distance in kilometers to convert to miles:"))
    mile = kilometer * .621371
    print(kilometer, "Kilometer equals", mile, "miles.")
    input("Press the <Enter> key to quit the program")

main()
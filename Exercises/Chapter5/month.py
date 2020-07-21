# Program to print the abbreviation of a month, given its number
# Author: Chris Williams

def main():
    # months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1 - 12): "))

    # compute the starting position of month n in the months lookup table
    pos = (n - 1) * 3

    # grab the appropriate slice for months
    monthbbrev = months[pos: pos + 3]

    # print the result
    print("The month abbreviation is", monthbbrev + ".")

main()


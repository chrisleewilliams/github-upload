# An impoved version of the futval program from chapter 2
# Author: Chris Williams

def main():
    print("This program calculates the future value of a 10-year investment.\n")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years you will hold the investment: "))

    print("{:9} {:9}".format("Year","Value"))
    print("-" * 30)

    for i in range(years):
        principal = principal * (1 + apr)
        print("{:<9} ${:<9.2f}".format(i + 1, principal))

    input("Press <Enter> to quit.")

main()

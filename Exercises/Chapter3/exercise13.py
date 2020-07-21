# Program to sum a series of numbers entered by the user
# Author: Chris Williams

def main():
    print("Hello! If you provide a series of numbers I can find the sum of the numbers for you.")
    n = int(input("How many numbers will I be adding? "))
    total = 0
    x = 0
    
    for i in range(n):
        x = float(input("provide a number to add: "))
        total = total + x

    print("The sum of the numbers you provided is", total)
main()


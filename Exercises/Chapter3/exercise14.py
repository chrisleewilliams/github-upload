# program to find the average of a list of numbers a user provides
# Author: Chris Williams

def main():
    print("Hello, If you provide a list of numbers I can find the average of the numbers.")
    y = int(input("How many numbers will you be providing? "))
    total = 0
    num = 0

    for i in range(y):
        num = float(input("Enter a number: "))
        total = num + total
    
    avg = total / y

    print("The average of the numbers you provided is", avg)
main()
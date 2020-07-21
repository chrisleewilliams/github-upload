# factorial.py
# program to find the factoraial of a number
# Author: Chris Williams

def main():
    n = int(input("Please enter the factorial of a number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factoiral of", n, "is", fact)

main()
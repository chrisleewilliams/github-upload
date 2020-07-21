# Program to return the sum of the first N natural numbers and to return the the sum of the cube of the first N natural numbers
# Author: Chris williams

def sumN(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total

def sumNCubes(n):
    total = 0
    for i in range(n+1):
        total = total + i**3
    return total

def main():
    n = int(input("Enter a number to find the sum of the first natural numbers up to N: "))
    x = sumN(n)
    x3 = sumNCubes(n)

    print(f"The sum of the first {n} numbers is: {x} ")
    print(f"The sum of the  cube of the first {n} numbers is: {x3} ")

main()
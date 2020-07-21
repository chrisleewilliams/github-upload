# A program to find the sum of the first n natural number
# Author: Chris Williams

def main():
    print("Enter a number(n) to find the sum of the first natural numbers up to n:")
    n = int(input("Enter a number: "))
    total = 0
    for i in range(n + 1):
        total = i + total

    print("sum:", total)

main()


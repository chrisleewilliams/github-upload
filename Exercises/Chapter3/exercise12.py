# program to find the sum of cubes of the first n natural numbers, where the value n is provided by the user.
# Author: Chris Williams

def main():
    print("Hello. If you provide a number(n) then i will be able to find the sum of the cubes of the first natural numbers up to n.")
    n = int(input("provide a number (n): "))
    total = 0
    for i in range(n + 1):
        total = i**3 + total

    print("The sum of the cubes of", n, "is", total)

main()
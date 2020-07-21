# a program that computes the fibonacci number where n is provided by the user
# Author: Chris Williams

def fibo(n):
    total, var = 1, 1
    for i in range(n-2):
        total, var = total + var, total
    return total

def main():
    print("Hello, if you provide a number (n) I can find its value in a Fibonacci Sequence.")
    n = int(input("Enter a number: "))
   

    print("The fibonacci number associated with", n, "is", fibo(n))

main()

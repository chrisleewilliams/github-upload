# program to attempt to assist the user in guessing the square root of a number (x)
# square roots will be rounded to the tenth place
# Author: Chris Williams
from math import sqrt

def main():
    root = int(input("Enter a number you would like to guess the square root of: "))

    # Finds the square root of x and rounds it to the tenth place
    sqrRootX = round(sqrt(root), 1)
    
    attempts = int(input("How many gueses would like to make? "))

    guess = float(input("Make your first guess"))
    nextGuess = 0
    for i in range(attempts):
        if guess == root:
            break
        else:
            nextGuess = (guess + (root / guess)) / 2 # Newton's method for gussing
        
        


    

main()
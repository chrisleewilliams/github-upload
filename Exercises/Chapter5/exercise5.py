# Program ato assign number values to letters and summing up the letters of your name
# Author: Chris Williams

def main():
    # Get users name
    name = input("Enter a name to determine your character traits.")

    numbers = " abcdefghijklmnopqrstuvwxyz"

    name = name.lower()

    score = 0

    for letter in name:
        score = score + numbers.find(letter)

    print("Your score is {}.".format(score))

main()
        
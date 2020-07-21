# A program to calculate how far lightning strikes based on how many second you hear thuner after you see lightning
# Author: Chris Williams

def main():
    print("Hello! I will calculate the distance lightning strikes from you if you can tell me how many seconds you hear the thunder after you saw the lightning")
    s = int(input("Enter the seconds that elapsed between you hearing the thunder and seeing the lightning: "))

    speed = 1100  # speed of sound in ft per sec

    distance = speed * s

    print(" The lightning stike was", round(distance / 5280, 2), "miles away from where you heard the thunder")

main()
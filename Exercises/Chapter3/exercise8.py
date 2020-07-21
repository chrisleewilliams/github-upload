# Program to find the value of the epact based on the year a user inputs
# Author: Chris Williams

def main():
    print("I can find the value of the epact if you give me a year.")
    year = int(input("Enter the year(e.g. 1984): "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    print("Epact:", epact)

main()

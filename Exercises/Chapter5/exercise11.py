# improved chaos.py program from chapter 1
# Author: Chris Williams

def main():
    print("This program illustrtes a chaotic function\n")

    x = float(input("Enter a number between 0 and 1 seperated by a coma: "))
    y = float(input("Enter another number between 0 and 1 seperated by a coma: "))
    num = int(input("How many times would you like for this program to run: "))
    

    print("{:12} {:<14} {:<12}".format("index", x, y))
    print("-" * 36)

    for i in range(num):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{:^6} {:^16.6f} {:^12.6f}". format(i + 1, x, y))

    input("Press <Enter> to quit.")


main()

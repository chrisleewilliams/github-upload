# program to display the growth of a users investment given principal time(in years) and APR
# Author: Chris Williams
from graphics import *

def main ():
    print("This program plots the growth of a 10-year investment.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annuaized interest rate: "))

    # create a grphics window with labels onthe left side of the window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    # draw bar for initial principal
    height = principal * .02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # draw bars for succesive years
    for year in range(1, 11):
        # calculate the value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40 
        height = principal * .02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    input("Press<Enter> to quit")
    win.close()

main()




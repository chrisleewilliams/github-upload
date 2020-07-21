# version 2 of the original futval_graph
# Author: Chris Williams

from graphics import *

def main():
    input_win = GraphWin("Initial investment", 600, 600)
    input_win.setCoords(0, 0, 300, 300)
    message = Text(Point(150, 280), "This program plots the growth of a 10-year investment.")
    message.draw(input_win)

    message2 = Text(Point(46, 250), "Enter the initial Principal")
    message2.draw(input_win)
    
    p_box = Entry(Point(150, 250), 9)
    p_box.draw(input_win)

    message3 = Text(Point(60, 225), "Enter the annuaized interest rate")
    message3.draw(input_win)
    
    a_box = Entry(Point(150, 225), 9)
    a_box.draw(input_win)


    input_win.getMouse()
    principal = float(p_box.getText())
    apr = float(a_box.getText())

    input_win.close()
    
    # create a grphics window with labels onthe left side of the window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    # draw a bar for subsequent years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit.")
    win.close()
main()


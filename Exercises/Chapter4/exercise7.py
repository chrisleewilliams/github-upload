# A program to compute the intersection of a circle with a horizontal line and display the info graphically and textually
# Author: Chris Williams

from graphics import *
import math

def main():
    win = GraphWin("Circle and line", 600, 600)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("white")
    intro = Text(Point(0, 9), "Program to compute the intersection of a line and a circle")
    intro.draw(win)

    radius_message = Text(Point(-6.5, 6), "Enter the radius of the circle")
    radius_message.draw(win)

    y_int_message = Text(Point(-6.2, 4), "Enter the Y-intercept of the line" )
    y_int_message.draw(win)

    radius_box = Entry(Point(-2, 6), 3)
    radius_box.draw(win)

    y_int_box = Entry(Point(-2, 4), 3)
    y_int_box.draw(win)

    win.getMouse()

    radius = float(radius_box.getText())
    y_int = float(y_int_box.getText())

    intro.undraw()
    radius_message.undraw()
    y_int_message.undraw()
    radius_box.undraw()
    y_int_box.undraw()

    user_circle = Circle(Point(0, 0), radius)
    user_circle.draw(win)

    user_line = Line(Point(-10, y_int), Point(10, y_int))
    user_line.draw(win)

    x = math.sqrt(radius ** 2 - y_int ** 2)

    print("The x values are ", x, -x)

    p1 = Circle(Point(x, y_int),0.25)
    p1.setOutline("red")
    p1.setFill("red")
    p1.draw(win)

    p2 = p1.clone()
    p2.move(-2*x, 0)
    p2.draw(win)

    win.getMouse()



main()

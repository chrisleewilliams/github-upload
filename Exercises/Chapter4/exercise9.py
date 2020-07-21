# Program to display information drawn by a user about a rectangle
# Author: Chris Williams

from graphics import *
from math import *

def main():
    win = GraphWin("rectangle", 600, 600)
    print("click where you would like the opposite corner of the rctnagle to appean in the window provided")

    point1 = win.getMouse()
    x1 = point1.getX()
    y1 = point1.getY()

    point2 = win.getMouse()
    x2 = point2.getX()
    y2 = point2.getY()

    user_rec = Rectangle(Point(x1, y1), Point(x2, y2))
    user_rec.draw(win)

    dx = x2 - x1
    dy = y2 - y1

    area = dx * dy
    perimeter = 2 * (dx + dy)

    print("Area:", round(abs(area), 3))
    print("Perimeter:",round(perimeter, 3))

    win.getMouse()


main()

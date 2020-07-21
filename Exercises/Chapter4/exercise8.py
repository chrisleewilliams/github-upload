# A program to draw a line segment and display graphcial and textual information about the line segment.
# Author: Chris Williams

from graphics import *
from math import *

def main():
    win = GraphWin("Line segment", 600, 600)
    print("Click any where in the window to create the end points for the line segment")

    endpoint1 = win.getMouse()
    x1 = endpoint1.getX()
    y1 = endpoint1.getY()
    point1 = Point(x1, y1)
    point1.draw(win)

    endpoint2 = win.getMouse()
    x2 = endpoint2.getX()
    y2 = endpoint2.getY()
    point2 = Point(x2, y2)
    point2.draw(win)

    userline = Line(point1, point2)
    userline.setWidth(2)
    userline.draw(win)

    midpoint = userline.getCenter()
    midpoint.setFill("cyan")
    midpoint.draw(win)
    
    dx = x2 - x1
    dy = y2 - y1

    slope = dy / dx
    length = sqrt(dx**2 + dy**2)

    print("length:", round(length, 3))
    print("slope:", round(slope, 3))
    
    win.getMouse()






    

main()


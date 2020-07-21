# Program to draw a triangle when the user clicks where they would like the three verticies to be. and provides the area and length
#  Author: Chris Williams

from graphics import *
from math import *

def main():
    win = GraphWin("Draw a triangle", 600, 600)
    win.setCoords(-300, -300, 300, 300)

    msg = Text(Point(0, -240),"Click where you would like the verticies of the triangle to be.")
    msg.draw(win)

    point1 = win.getMouse()
    x1 = point1.getX()
    y1 = point1.getY()
    
    point2 = win.getMouse()
    x2 = point2.getX()
    y2 = point2.getY()

    point3 = win.getMouse()
    x3 = point3.getX()
    y3 = point3.getY()
    
    triangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    triangle.draw(win)

    win.getMouse()
main()

# Program: triangle2.py
from math import sqrt
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))

    return dist

def areaTriangle(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return sqrt(s * (s - s1) * (s - s2) * (s - s3))

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three verticies of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("green")
    triangle.setOutline("black")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("Perimeter: {0:02f}".format(perim))

    # Wait for another click to exit
    win.getMouse()
    # Calculate the area of a triangle
    s1 = distance(p1, p2)
    s2 = distance(p2, p3)
    s3 = distance(p3, p1)
    message.setText("Area: {0:02f}".format(areaTriangle(s1,s2,s3)))

    # Wait for another click to exit
    win.getMouse()
    win.close()
main()
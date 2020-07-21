# A program that draws a face
# Author: Chris Williams

from graphics import *

def main():
    win = GraphWin("Face", 600, 600)
    win.setCoords(-6, -6, 6, 6)
    
    head = Circle(Point(0, 0), 3)
    head.draw(win)
    
    l_eye = Circle(Point(-1, 1.2), .5)
    l_eye.draw(win)
    
    r_eye = Circle(Point(1, 1.2), .5)
    r_eye.draw(win)

    nose = Polygon(Point(0, 1.1), Point(-.4, -.5), Point(.4, -.5))
    nose.draw(win)

    mouth = Oval(Point(-1,-1.5), Point(1,-1.2))
    mouth.draw(win)

    win.getMouse()

main()


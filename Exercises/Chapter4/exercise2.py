# Program to draw an archery taret
# Author: Chris Williams

from graphics import *

def main():
    win = GraphWin("Archery target", 600, 600)

    white_circ = Circle(Point(300, 300), 200)
    white_circ.draw(win)
    
    black_circ = Circle(Point(300, 300), 160)
    black_circ.setFill("black")
    black_circ.draw(win)
   
    blue_circ = Circle(Point(300, 300), 120)
    blue_circ.setFill("blue")
    blue_circ.draw(win)
   
    red_circ = Circle(Point(300, 300), 80)
    red_circ.setFill("red")
    red_circ.draw(win)
    
    yellow_circ = Circle(Point(300, 300), 40)
    yellow_circ.setFill("yellow")
    yellow_circ.draw(win)

    win.getMouse()
    win.close()


main()

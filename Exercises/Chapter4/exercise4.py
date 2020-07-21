# Picture of a winter scene
# Author: Chris Williams

from graphics import *

def main():
    win = GraphWin("A chirstmas scene", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("grey")
    
    snowman_bottom = Circle(Point(150,250), 60)
    snowman_bottom.setFill("white")
    snowman_bottom.draw(win)

    snowman_mid = Circle(Point(150, 330), 40)
    snowman_mid.setFill("white")
    snowman_mid.setOutline("white")
    snowman_mid.draw(win)

    snowman_top = Circle(Point(150, 390), 25)
    snowman_top.setFill("white")
    snowman_top.setOutline("white")
    snowman_top.draw(win)

    tree_base = Rectangle(Point(415, 320), Point(435, 350))
    tree_base.setFill("brown")
    tree_base.setOutline("brown")
    tree_base.draw(win)

    tree_bottom = Polygon(Point(425 , 415),Point(350 ,350),Point(500 ,350))
    tree_bottom.setFill("green")
    tree_bottom.setOutline("green")
    tree_bottom.draw(win)

    tree_mid = Polygon(Point(425 , 425),Point(370 ,380),Point(480 ,380))
    tree_mid.setFill("green")
    tree_mid.setOutline("green")
    tree_mid.draw(win)

    tree_top = Polygon(Point(425 , 445),Point(390 ,410),Point(460 ,410))
    tree_top.setFill("green")
    tree_top.setOutline("green")
    tree_top.draw(win)

    win.getMouse()
main()


# Program that draws 5 dice on the screen
# Author: Chris Williams

from graphics import *

def main():
    win = GraphWin("Dice", 600, 600)
    win.setCoords(0,0,600,600)

    dice = Rectangle(Point(90, 300), Point(150, 360))
    dice.draw(win)

    init_dot = Circle(Point(120, 330), 6)
    init_dot.setFill("black")
    init_dot.draw(win)


    dice = dice.clone()
    dice.move(90, 30)
    dice.draw(win)
    
    dot_2a = init_dot.clone()
    dot_2a.move(70, 15)
    dot_2a.draw(win)
    dot_2b =  dot_2a.clone()
    dot_2b.move(40, 33)
    dot_2b.draw(win)
    
    dice = dice.clone()
    dice.move(90, -30)
    dice.draw(win)

    dice = dice.clone()
    dice.move(90, 30)
    dice.draw(win)

    dice = dice.clone()
    dice.move(90, -30)
    dice.draw(win)



    win.getMouse()
    win.close()

main()
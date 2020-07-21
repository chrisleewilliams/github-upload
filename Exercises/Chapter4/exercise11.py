# a program to create a house in 5 clicks
# Author: Chris Williams

from graphics import *

def main ():
    win = GraphWin("Build a house", 600, 600)
    win.setCoords(-300, -300, 300, 300)

    msg = Text(Point(0, -260), "In 5 clicks build a house of any size within the window. Have fun!")
    msg.draw(win)

    base1 = win.getMouse()
    base1x = base1.getX()
    base1y = base1.getY()

    base2 = win.getMouse()
    base2x = base2.getX()
    base2y = base2.getY()

    base = Rectangle(Point(base1x, base1y), Point(base2x, base2y))
    base.draw(win)

    door_click = win.getMouse()
    door_x = door_click.getX()
    door_y = door_click.getY()

    base_width = abs(base2x - base1x)
    
    door = Rectangle(Point(door_x - base_width * .1, base1y), Point(door_x + base_width * .1 , door_y))
    door.draw(win)

    window_click = win.getMouse()
    window_x = window_click.getX()
    window_y = window_click.getY()

    window_x1 = window_x - base_width * .05
    window_y1 = window_y - base_width * .05

    window_x2 = window_x + base_width * .05
    window_y2 = window_y + base_width * .05

    window = Rectangle(Point(window_x1, window_y1), Point(window_x2, window_y2))
    window.draw(win)

    roof_click = win.getMouse()
    roof_x = roof_click.getX()
    roof_y = roof_click.getY()

    roof = Polygon(Point(base1x, base2y), Point(base2x, base2y), Point(roof_x, roof_y))
    roof.draw(winn)

    win.getMouse()
main()



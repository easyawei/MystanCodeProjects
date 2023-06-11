"""
File: draw_line.py
Name: chaowei hsieh
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants, size of ball
SIZE = 10

# Global Variable,
window = GWindow(title='draw_line')     # Main window
is_in_a_line = False                    # the switch to turn on draw_line.

lo_x0 = 0       # store the coordinate event.x by first mouse clicked.
lo_y0 = 0       # store the coordinate event.y by first mouse clicked.

window_01 = 0   # store the object location of first moused clicked.
window_02 = 0   # store the object location of second moused clicked.


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(punch_hole)


def punch_hole(mouse):
    """
    :parameter mouse: class, coordinate by mouse clicked
    :return window.add(hole), window.remove(window_01), window.remove(window_02), window.add(line): object

    the function provide the steps following from first/second click from user.

    a. First click.
        S01: A circle appears indicating the user's first click.
        S02: Get location data x,y from the first click then store in lo_x0, lo_y0.

    b. Second click
        S03: A circle appears indicating the user's second click.
        S04: Get location data x,y from the second click then store in lo_x1, lo_y1.
        S05: Draw a line at from the first/second location data using GLine.
        S06: Remove the first and second circle from window.
    """
    global is_in_a_line, lo_x0, lo_y0, window_01, window_02

    # S01 and S03: Creating first circle by GOval object.
    hole = set_up_circle(SIZE)
    window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)

    # Condition of number of mouse clicked from user.
    if is_in_a_line is False:   # the first click

        # S02 Get the mouse data from first clicked.
        lo_x0 = mouse.x
        lo_y0 = mouse.y
        window_01 = window.get_object_at(lo_x0, lo_y0)

        # turn on switch to trigger the draw_line by the next input of mouse clicked.
        is_in_a_line = True

    else:                       # the second clicked, is_in_a_line is "True"
        # S04: get the mouse data from second clicked.
        window_02 = window.get_object_at(mouse.x, mouse.y)

        # S05: creating line by GLine object.
        line = GLine(lo_x0, lo_y0, mouse.x, mouse.y)
        window.add(line)

        # S06: eliminate the first circle and second circle.
        window.remove(window_01)
        window.remove(window_02)

        is_in_a_line = False


def set_up_circle(size):
    """
    :parameter str: SIZE of circle.
    :return object: object of circle.
    """
    hole = GOval(size, size)
    hole.filled = True
    hole.fill_color = 'white'
    return hole


if __name__ == "__main__":
    main()

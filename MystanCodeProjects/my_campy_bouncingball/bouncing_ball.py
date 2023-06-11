"""
File: bounce ball.py
Name: chaowei hsieh
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

# Global Variable, switch
is_in_a_start = False

# Global Variable, circle ball,
ball = GOval(SIZE, SIZE)

# Global Variable, score dashboard
score = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    # Part 01 : initial ball.
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)

    # Part 02: moving of circle by mouse clicked
    onmouseclicked(fall_in_ground)


def fall_in_ground(event):
    """
    :para object: MouseEventType.MOUSE_CLICKED from user.
    :return: none.

    steps following
    Step_01: turn switch on 'is_in_a_start = True'
    Step_02: bouncing ball moving from left to right until out of window (ball.x >= window.width)
    Step_03: Turn switch off then reset status for the next mouse event (clicked)

    note:
    function only work when (1) number of time <3 and (2) switch 'is_in_a_start' is False.
    use score < 3 and 'is_in_a_start' for the requirement (1) and (2).
    """

    # global variable area
    global is_in_a_start, VX, GRAVITY, REDUCE, START_X, START_Y, SIZE, score, ball

    # if statement : prevent any interrupt before the completion of circle ball move.
    if score < 3 and is_in_a_start is False:

        # do nothing to eliminate the error for non use event from mouse(user),
        non = window.get_object_at(event.x, event.y)
        if non is not None:
            window.remove(non)

        # prevention setup_01 : Turn on switch (preventing of any interruption)
        is_in_a_start = True

        # ball set up for ball.move(dx, dy)
        window.add(ball, x=START_X, y=START_Y)    # ball
        vy = VX     # dy based on VX

        # starting of bouncing_ball.
        while True:
            # bouncing ball move continually.
            vy = vy+GRAVITY
            ball.move(VX, vy)

            # if 01 : check if out of window (bottom)
            if ball.y + ball.height >= window.height and vy > 0:
                vy = -vy*REDUCE

            # if 02 : check if out of window (right)
            if ball.x >= window.width:
                is_in_a_start = False
                window.add(ball, x=START_X, y=START_Y)

                # prevention setup_02 : number of execution < 3
                score += 1
                break

            pause(DELAY)


if __name__ == "__main__":
    main()

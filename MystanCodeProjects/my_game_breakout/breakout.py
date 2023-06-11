"""
File : breakout.py
Name : chaowei hsieh
---------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120         # 120 frames per second
NUM_LIVES = 3			        # Number of attempts
NUM_SUM = 0                     # Number of score

VX = 1                          # constant of velocity x
VY = 1                          # constant of velocity y


def main():
    vx = VX
    vy = VY
    num_lives = NUM_LIVES                                   # counter of lives
    num_sum = NUM_SUM                                       # counter of score

    graphics = BreakoutGraphics()
    graphics.num_lives_label_text(num_lives)                # GLabel of lives

    num_goal = graphics.get_num_brick()                     # BRICK_ROWS(10) * BRICK_COLS(10) = 100
    graphics.num_sum_label_text(num_sum)                    # GLabel of score

    # Add the animation loop here!
    while True:
        vx_new = graphics.get_vx()*vx
        vy_new = graphics.get_vy()*vy

        # pause
        pause(FRAME_RATE)

        # update
        graphics.ball.move(vx_new, vy_new)                  # move ball by __dx and __dy.

        # check
        if graphics.ball.y+graphics.ball.height >= graphics.window.height:
            num_lives -= 1                                  # NUM_LiVES -1 when ball over window bottom
            graphics.num_lives_label_text(num_lives)        # number update on score label.
            graphics.reset_ball()                           # reset the ball location for the next run.

            if num_lives == 0:                              # break condition (NUM_LIVES = 0), 3 times chances
                graphics.game_over_label()                  # "You Die Lo"
                break

        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:    # wall window.x
            vx = -vx

        if graphics.ball.y <= 0:                            # wall window.y
            vy = -vy

        first_hit = False
        for i in range(0, graphics.ball.width+1, graphics.ball.width):
            for j in range(0, graphics.ball.height+1, graphics.ball.height):

                what_object = graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j)
                
                if what_object is not None:
                    if what_object is graphics.get_paddle():
                        if vy > 0:
                            vy = - vy
                    elif what_object is not graphics.num_lives_label and what_object is not graphics.num_sum_label:
                        if not first_hit:
                            vy = -vy
                            graphics.window.remove(what_object)
                            num_sum += 1
                            graphics.num_sum_label_text(num_sum)
                            first_hit = True

        # end the game
        if num_sum == num_goal:                             # NUM_SCORE = 100
            graphics.game_win_label()                       # "You WIN"
            break


if __name__ == '__main__':
    main()

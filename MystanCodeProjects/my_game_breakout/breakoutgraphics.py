"""
File : breakoutgraphics.py
Name : chaowei hsieh
---------------------------------------

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

is_in_a_game = False
# num_lives_label = GLabel('NUM_LIVES = ' + str(""))
# num_sum_label = GLabel('NUM_SCORE = ' + str(""))


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.br = ball_radius
        self._pad_w = paddle_width
        self._pad_h = paddle_height
        self._pad_offset = paddle_offset
        self._bri_rows = brick_rows
        self._bri_cols = brick_cols
        self._bri_wid = brick_width
        self._bri_hei = brick_height
        # self._bri_off = brick_offset
        self._bri_spa = brick_spacing

        # Create a graphical window, with some extra space
        self._bri_offset = brick_offset
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = self._bri_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # create a label : num_lives_label
        self.num_lives_label = GLabel("NUM_LIVES = " + str(""))
        self.num_lives_label.font = '-10'
        self.window.add(self.num_lives_label, x=10, y=self.window.height - self.num_lives_label.height)

        # create a label : num_um_label
        self.num_sum_label = GLabel("NUM_SCORE = " + str(""))
        self.num_sum_label.font = '-10'
        self.window.add(self.num_sum_label, x=self.window_width - self.num_sum_label.width*1.3,
                        y=self.window.height - self.num_lives_label.height)

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self.window.add(self._paddle, x=(self.window_width-paddle_width)/2, y=(self.window_height-self._pad_offset))

        # Center a filled ball in the graphical window
        self.ball = GOval(self.br, self.br)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.br)/2, y=(self.window_height-self.br)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.reset_position_paddle)
        onmouseclicked(self.handle_clicked)

        # Draw bricks
        self._bricks = 0
        self.set_bricks_position()

    def reset_position_paddle(self, mouse):
        if self._paddle.width / 2 < mouse.x < self.window.width-self._paddle.width/2:
            self._paddle.x = mouse.x - self._paddle.width/2
        self._paddle.y = (self.window.height - BRICK_OFFSET)

    def handle_clicked(self, mouse):
        global is_in_a_game

        if is_in_a_game is False:
            is_in_a_game = True
            self.get_ball_velocity()

    def get_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx

    def set_bricks_position(self):

        color = ['red', 'orange', 'yellow', 'green', 'blue']
        color_index = 0

        for i in range(BRICK_ROWS):
            bricks_y_i = BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*i

            for j in range(BRICK_COLS):
                bricks_x_j = (BRICK_SPACING+BRICK_WIDTH)*j

                self._bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self._bricks.filled = True
                self._bricks.fill_color = color[color_index % len(color)]

                self.window.add(self._bricks, x=bricks_x_j, y=bricks_y_i)

            if i % 2 == 1:
                color_index += 1

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def get_paddle(self):
        return self._paddle

    def reset_ball(self):
        global is_in_a_game
        is_in_a_game = False

        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, x=(self.window_width - self.br) / 2, y=(self.window_height - self.br) / 2)

    def get_num_brick(self):
        return self._bri_rows*self._bri_cols

    def num_sum_label_text(self, nums):
        self.num_sum_label.text = 'NUM_SCORE = ' + str(nums)

    def num_lives_label_text(self, num):
        self.num_lives_label.text = 'NUM_LIVES = ' + str(num)

    def game_win_label(self):
        self.num_lives_label.text = 'YOU WIN'

    def game_over_label(self):
        self.num_lives_label.text = 'YOU LOSE'

# Paddle class
from turtle import Turtle


# TODO: Create and move a paddle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # add paddle shape
        self.shape("square")
        # add paddle color
        self.color("white")
        # change the paddle shape size
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # set up the default position
        self.goto(position)

    # move the paddle up and down methods
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

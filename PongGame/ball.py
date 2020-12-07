# ball class
# TODO: crate ball and make it move

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ball move with x and y coordinate """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Ball bounce back from up"""
        self.y_move *= -1

    def bounce_x(self):
        """Ball bounce from down """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball position and speed"""
        self.goto(0, 0)
        # move speed set to default
        self.move_speed = 0.1
        # reverse bounce
        self.bounce_x()

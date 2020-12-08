# TODO: Create player and Move the turtle with keypress
from turtle import Turtle

# constant for players
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# player class
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """Move the turtle forward """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Set starting position for turtle"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Return boolean if turtle reach the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

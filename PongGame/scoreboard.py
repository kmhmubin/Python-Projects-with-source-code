# TODO: Create score board
from turtle import Turtle

# constant
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def update_scoreboard(self):
        """Return update score values """
        # clearing the overlapping numbers
        self.clear()
        # left side score
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        # right side score
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        """Return left score by plus 1"""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Return right score by plus 1"""
        self.right_score += 1
        self.update_scoreboard()

# TODO: Create a scoreboard

from turtle import Turtle

# Constant for scoreboard
FONT = ("Courier", 24, "normal")


# scoreboard class which inherit turtle classes
class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the screen and update the scoreboard"""
        self.clear()
        self.write(f" Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """ Increase the level """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Show message when game over"""
        self.goto(0, 0)
        self.write(f" GAME OVER 😞 ", align="center", font=FONT)

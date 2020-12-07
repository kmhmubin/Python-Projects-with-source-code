from turtle import Turtle

# constant
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# TODO: Create score board


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Return updated score"""
        self.write(f" Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """if collision then game over."""
        self.goto(0, 0)
        self.write("GAME OVER 😣", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Return score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

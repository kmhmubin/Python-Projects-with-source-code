from turtle import Turtle

# constant
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# TODO: Create score board


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Return updated score"""
        self.clear()
        self.write(f" Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        """if collision then game over."""
        if self.score > self.high_score:
            self.high_score = self.score
            # it will reset to zero for new game
            self.score = 0
            self.update_scoreboard()

    def increase_score(self):
        """Return score"""
        self.score += 1
        self.update_scoreboard()

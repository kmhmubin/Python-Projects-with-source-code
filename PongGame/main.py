# Pong Game
"""TODO:
1. create the screen
2. create and move a paddle
3. create another paddle
4. create the ball and make it move
5. detect collision with wall and bounce
6. detect collision with paddle
7. detect when paddle misses
8. keep score
"""

from turtle import Screen, Turtle
from paddle import Paddle

# TODO: Create the screen
# create screen object
screen = Screen()
# make background black
screen.bgcolor("black")
# screen width and height
screen.setup(width=800, height=600)
# screen title
screen.title("Pong Game")
# turn off the turtle animation
screen.tracer(0)

# TODO: Create and move a paddle

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# creating a paddle object
paddle = Turtle()

# event listener for keypress
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# game is on
game_is_on = True

while game_is_on:
    screen.update()

# screen exit
screen.exitonclick()

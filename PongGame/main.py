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

# creating a paddle object
paddle = Turtle()
# add paddle shape
paddle.shape("square")
# add paddle color
paddle.color("white")
# change the paddle shape size
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
# set up the default position
paddle.goto(350, 0)


# move the paddle up and down function
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


# event listener for keypress
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

# game is on
game_is_on = True

while game_is_on:
    screen.update()

# screen exit
screen.exitonclick()

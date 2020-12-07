"""TODO: Snake Game
1. create a screen with 600x600 size
2. create a snake body
3. move the snake
4. create snake food
5. detect collision with food
6. create a scoreboard
7. detect collision with wall
8. detect collision with tail
"""

from turtle import Turtle, Screen
from snake import Snake
import time

# creating a object
screen = Screen()

# TODO: create a screen
# setup the screen
screen.setup(width=600, height=600)

# set background color to black
screen.bgcolor("black")

# add title of the screen
screen.title("Snake Game")

# turn off the turtle animation 
screen.tracer(0)
# create snake object
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.9)
    # move the snake
    snake.move()

# exit on click
screen.exitonclick()

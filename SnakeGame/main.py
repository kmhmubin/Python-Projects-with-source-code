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

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

# create food object
food = Food()

# create scoreboard object
scoreboard = Scoreboard()

# TODO: control the snake with keypress
# start listen the keypress
screen.listen()

# add arrow keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # move the snake
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

# exit on click
screen.exitonclick()

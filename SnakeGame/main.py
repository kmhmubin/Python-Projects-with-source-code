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

# creating a object
screen = Screen()

# TODO: create a screen
# setup the screen
screen.setup(width=600, height=600)

# set background color to black
screen.bgcolor("black")

# add title of the screen
screen.title("Snake Game")

# TODO: creating a snake body
# creating snake block
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("Green")
    new_segment.goto(position)

# exit on click
screen.exitonclick()

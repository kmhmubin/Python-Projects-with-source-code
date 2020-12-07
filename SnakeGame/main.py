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

# TODO: creating a snake body
# TODO: Move the snake body

# creating snake block
starting_position = [(0, 0), (-20, 0), (-40, 0)]

# empty segment
segments = []

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("Green")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# if game is on
game_is_on = True

while game_is_on:
    # turn on the turtle animation
    screen.update()
    time.sleep(0.1)

    # range for segment are start at 2, stop at 0 and take step back -1
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


# exit on click
screen.exitonclick()

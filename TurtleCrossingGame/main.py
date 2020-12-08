"""TODO:
1. Create screen
2. Create and move cars
3. Create player
4. Move the turtle with keypress
5. Detect collision with car
6. Detect when turtle reaches the other side
7. Create a scoreboard

"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO: Create the game screen
# creating screen object
screen = Screen()
# setup screen size
screen.setup(width=600, height=600)
# turn off turtle animation
screen.tracer(0)

# TODO: Create player
# creating player object
player = Player()

# game on or not
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    # update the screen
    screen.update()

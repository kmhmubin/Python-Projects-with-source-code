import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# creating screen object
screen = Screen()
# setup screen size
screen.setup(width=600, height=600)
# turn off turtle animation
screen.tracer(0)

# game on or not
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    # update the screen
    screen.update()

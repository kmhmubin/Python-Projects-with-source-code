from turtle import Turtle, Screen
import random

# is game start
is_race_on = False

# creating objects
new_turtle = Turtle()
screen = Screen()

# specifying screen size
screen.setup(width=500, height=400)

# user bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle win the race? Enter a color: ")

# turtle colors
colors = ["red", "yellow", "orange", "green", "blue", "purple"]

# turtle y position for add gap with each other
y_position = [-70, -40, -10, 20, 50, 80]

# empty list for all turtle
all_turtle = []

for turtle_index in range(0, 6):
    # turtle shape
    new_turtle = Turtle(shape="turtle")
    # stop pen writing
    new_turtle.penup()
    # add colors to turtle
    new_turtle.color(colors[turtle_index])
    # start from left edge of screen
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    # add all turtle on the list
    all_turtle.append(new_turtle)

# checking user bet
if user_bet:
    is_race_on = True

# Start the game
while is_race_on:

    for turtle in all_turtle:
        # checking if the x coordinate value is grater than 230
        if turtle.xcor() > 230:
            is_race_on = False
            # checking wining color
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# exit the program on click
screen.exitonclick()

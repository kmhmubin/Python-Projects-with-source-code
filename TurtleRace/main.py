from turtle import Turtle, Screen

# creating objects
tim = Turtle()
screen = Screen()

# specifying screen size
screen.setup(width=500, height=400)

# user bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle win the race? Enter a color: ")

# turtle colors
colors = ["red", "yellow", "orange", "green", "blue", "purple"]

# turtle y position for add gap with each other
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    # turtle shape
    tim = Turtle(shape="turtle")
    # add colors to turtle
    tim.color(colors[turtle_index])
    # stop pen writing
    tim.penup()
    # start from left edge of screen
    tim.goto(x=-230, y=y_position[turtle_index])

# exit the program on click
screen.exitonclick()

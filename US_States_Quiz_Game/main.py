"""TODO:
1. create a screen
2. show blank US state image
3. Take user input
4. Convert the input to Title case
5. check if the guess is amoung the 50 states
6. write correct guess onto the map
7. allow the user to keep guessing
8. record the correct guesses
9 keep track of the score
"""

import turtle
import pandas

# creating screen object
screen = turtle.Screen()
# screen title
screen.title("U.S. States Game")
# assign the image as a shape of turtle
image = "blank_states_img.gif"
# add image as turtle shape
screen.addshape(image)
# changing turtle shape
turtle.shape(image)

# # get the coordinates from mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# read csv file using pandas
data = pandas.read_csv("50_states.csv")
# assigning all state's to a list
all_states = data.state.to_list()
# empty states
guessed_states = []

while len(guessed_states) < 50:
    # popup input option and covert input into Title
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()
    print(answer_state)

    # checking answer with the csv file
    if answer_state in all_states:
        # add answer into guessed state list
        guessed_states.append(answer_state)
        # assign turtle object
        tim = turtle.Turtle()
        # hide the turtle
        tim.hideturtle()
        # hide the pen draws
        tim.penup()
        # checking user input with store values
        state_data = data[data.state == answer_state]
        # if correct then goto specific coordinates
        tim.goto(int(state_data.x), int(state_data.y))
        # write the state name on the screen
        tim.write(answer_state)

# screen exit on click
screen.exitonclick()

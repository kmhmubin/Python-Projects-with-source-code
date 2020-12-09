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

# popup input option
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer_state)

# screen exit on click
# screen.exitonclick()

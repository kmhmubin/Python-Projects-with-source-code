import turtle

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

# screen exit on click
screen.exitonclick()

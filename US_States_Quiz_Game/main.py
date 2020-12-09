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


# get the coordinates from mouse click
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# screen exit on click
# screen.exitonclick()

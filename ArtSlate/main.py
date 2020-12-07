from turtle import Turtle, Screen

# creating objects
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    # only clean the turtle drawing
    tim.clear()
    # after clear pen up
    tim.penup()
    # after clear go back to center of the screen
    tim.home()
    # after reach home then pen down
    tim.pendown()


# add event listener
screen.listen()
# when space key pressed then tim forward 50
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
# exit if clicked
screen.exitonclick()

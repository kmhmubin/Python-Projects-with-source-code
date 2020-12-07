from turtle import Turtle

# creating snake block
# Constant starting position and distance
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# creating snake class

class Snake:

    def __init__(self):
        # empty segment
        self.segments = []
        self.create_snake()

    # TODO: creating a snake body
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("Green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # TODO: Move the snake body
    def move(self):
        # range for segment are start at 2, stop at 0 and take step back -1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

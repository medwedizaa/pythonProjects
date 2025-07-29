from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def restart_position(self):
        self.goto(0, -280)

    def is_finished(self):
        return self.ycor() > FINISH_LINE_Y
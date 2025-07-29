from turtle import Turtle


class Car(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(position)


from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(x=0-i*20, y=0)

    def add_segment(self, x, y):
        segment = Turtle("square")
        segment.color('white')
        segment.penup()
        segment.goto(x, y)
        self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)

    def down(self):
        if int(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if int(self.head.heading()) != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        x, y = self.segments[-1].position()
        self.add_segment(x, y)

    def reset(self):
        for s in self.segments:
            s.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

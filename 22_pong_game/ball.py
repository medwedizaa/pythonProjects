from turtle import Turtle
import random


class Ball(Turtle):
    MOVES = [-10, 10]

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = random.choice(self.MOVES)
        self.y_move = random.choice(self.MOVES)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def restart(self):
        self.x_move *= -1
        self.y_move = random.choice(self.MOVES)
        self.move_speed = 0.1
        self.goto(0, 0)

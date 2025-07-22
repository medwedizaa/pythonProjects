import turtle
from turtle import Turtle, Screen
import colorgram
import random

t = Turtle()
turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# remove the background colors
rgb_colors = rgb_colors[2:]

t.speed(0)
t.hideturtle()

# move turtle into left-down corner
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)

# draw a picture
for i in range(10):
    for j in range(10):
        t.pendown()
        t.dot(20, random.choice(rgb_colors))
        t.penup()
        if j < 9:
            t.forward(50)
    if i % 2 == 0:
        t.left(90)
        t.forward(50)
        t.left(90)
    else:
        t.right(90)
        t.forward(50)
        t.right(90)

screen = Screen()
screen.exitonclick()

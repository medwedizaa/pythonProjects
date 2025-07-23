from turtle import Turtle, Screen
import random


def get_new_turtle(color, y):
    turt = Turtle(shape='turtle')
    turt.color(color)
    turt.penup()
    turt.goto(x=-230, y=y)
    return turt


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(user_bet)

turtles = []
for i in range(6):
    turtles.append(get_new_turtle(color=colors[i], y=(-100 + i * 40)))

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        t.forward(random.randint(0, 10))

screen.exitonclick()

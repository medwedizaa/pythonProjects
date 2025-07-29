from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ('Comic Sans MS', 15, 'normal')
GAME_OVER_FONT = ('Comic Sans MS', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-260, 270)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=GAME_OVER_FONT)

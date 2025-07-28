from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ('Comic Sans MS', 40, 'normal')
GAME_OVER_FONT = ('Comic Sans MS', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(position)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=GAME_OVER_FONT)

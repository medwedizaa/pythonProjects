from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ('Comic Sans MS', 20, 'normal')
GAME_OVER_FONT = ('Comic Sans MS', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0

        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
